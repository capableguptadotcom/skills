"""Run a skill's evaluation cases with and without the skill, in Codex and Claude Code.

Usage:
    python scripts/run_evals.py probe --host codex
    python scripts/run_evals.py run diagnose --host claude --repeats 2 [--case ID] [--model sonnet]
    python scripts/run_evals.py summarize eval/results/<file>.jsonl
    python scripts/run_evals.py judge eval/results/<file>.jsonl [--pair named without] [--model opus]
    python scripts/run_evals.py judge <pack>.jsonl --against <rival>.jsonl --pair named named --both-orders

Each run copies the case's fixture into a temporary Git repository. Three
conditions separate selection from usefulness: "without" installs nothing,
"with" installs the skill and lets the host decide whether to use it, and
"named" installs it and invokes it by name. Personal skills are kept out of both conditions:
Claude Code runs with project settings only, and Codex runs with every skill
under ~/.agents/skills and ~/.codex/skills disabled. Host built-in skills stay,
because users have them too.

Results go to eval/results/<skill>-<host>-<timestamp>.jsonl, one line per run.
"""

import argparse
import datetime
import json
import os
import re
import shutil
import subprocess
import sys
import time
import uuid
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HOME = Path.home()
# Outside this repository and the user profile: an agent that walks up from its workspace must not find
# this pack's skills or personal skills, or the "without" baseline is contaminated.
DEFAULT_WORK_ROOT = (Path(os.environ.get('SystemDrive', 'C:') + '\\') if os.name == 'nt' else Path('/tmp')) / 'skill-evals'
WORK_ROOT = Path(os.environ.get('EVAL_WORK_ROOT', DEFAULT_WORK_ROOT))
SKILL_DIR = {'claude': '.claude/skills', 'codex': '.agents/skills'}
# Agent and Task let a skill that delegates to subagents work as it does in real sessions.
# PYTHONHASHSEED=... python is how agents pin hash order when chasing a flaky test; without it, skills that
# reproduce such failures were held back more than skills that only reason about them. Shell loops over
# variables stay refused: Claude Code cannot check them before they run, whatever the allowlist says.
CLAUDE_TOOLS = ['Read', 'Grep', 'Glob', 'Edit', 'Write', 'Skill', 'Agent', 'Task', 'Bash(python *)',
                'Bash(PYTHONHASHSEED=* python *)', 'Bash(git *)', 'Bash(ls *)', 'Bash(cat *)']


def codex_binary():
    explicit = os.environ.get('CODEX_BIN')
    if explicit:
        return explicit
    bundled = sorted((HOME / 'AppData/Local/OpenAI/Codex/bin').glob('*/codex.exe'),
                     key=lambda p: p.stat().st_mtime)
    return str(bundled[-1]) if bundled else (shutil.which('codex') or 'codex')


def child_env(host):
    """Environment for a run. On Windows, Codex's sandbox cannot start Microsoft Store app
    aliases (WindowsApps\\pwsh.exe fails with Access is denied), so Codex runs get a PATH without
    them; Python's own folder is kept so tests can still run."""
    env = dict(os.environ)
    if host == 'codex' and os.name == 'nt':
        python_dir = str(Path(sys.executable).resolve().parent)
        kept = [p for p in env.get('PATH', '').split(os.pathsep)
                if p and 'microsoft\\windowsapps' not in p.lower()]
        env['PATH'] = os.pathsep.join([python_dir, *kept])
    return env


def personal_skill_overrides():
    paths = sorted(p for root in (HOME / '.agents/skills', HOME / '.codex/skills')
                   for p in root.glob('*/SKILL.md') if not p.parent.name.startswith('.'))
    entries = ','.join(f"{{path='{p}',enabled=false}}" for p in paths)
    return f'skills.config=[{entries}]'


def command(host, prompt, workdir, model=None, writable=True, session=None):
    """session is (session_id, resume) for a Claude Code conversation that continues over several turns."""
    if host == 'claude':
        persistence = (['--resume' if session[1] else '--session-id', session[0]] if session
                       else ['--no-session-persistence'])
        args = ['claude', '-p', prompt, '--output-format', 'stream-json', '--verbose',
                '--setting-sources', 'project', *persistence,
                '--permission-mode', 'acceptEdits', '--allowedTools', *CLAUDE_TOOLS]
        return args + (['--model', model] if model else [])
    args = [codex_binary(), 'exec', '--json', '--skip-git-repo-check',
            '-s', 'workspace-write' if writable else 'read-only',
            '-c', 'approval_policy="never"', '-c', personal_skill_overrides(),
            '-o', str(last_message(workdir))]
    return args + (['-m', model] if model else []) + [prompt]


def last_message(workdir):
    """Codex writes its final answer here: beside the workspace, so it is never counted as an edit."""
    return Path(workdir).with_name(Path(workdir).name + '.last-message.txt')


def harness_file(path):
    """Files the harness or the host creates, which never count as the agent's edits."""
    return (path.startswith(('.claude/', '.agents/', '.eval-')) or '__pycache__' in path
            or path.endswith('.pyc'))


def git(workdir, *args):
    return subprocess.run(['git', *args], cwd=workdir, capture_output=True, text=True,
                          encoding='utf-8', errors='replace').stdout


def remove_workdir(workdir):
    """Delete a workspace and the project folder Claude Code makes for it, which holds only empty folders
    (memory/) when the run stored no session. A folder with any file in it is kept."""
    shutil.rmtree(workdir, ignore_errors=True)
    folder = HOME / '.claude/projects' / re.sub(r'[^A-Za-z0-9]', '-', str(workdir))
    for path in [*sorted(folder.rglob('*'), reverse=True), folder] if folder.is_dir() else []:
        try:
            path.rmdir()
        except OSError:
            pass


def new_workdir(prefix):
    # Not tempfile.mkdtemp: on Windows its owner-only ACL locks out Codex's sandbox account, which then
    # answers from guesses ("Windows denied access to the workspace") instead of reading the code.
    WORK_ROOT.mkdir(parents=True, exist_ok=True)
    workdir = WORK_ROOT / f'{prefix}-{uuid.uuid4().hex[:10]}'
    workdir.mkdir()
    return workdir


# A run that never reached the model or the workspace says nothing about the skill.
HARNESS_FAILURE = re.compile(r'usage limit|rate limit|denied (read |write )?access to the (active |supplied )?workspace',
                             re.I)


def run_error(record):
    """Why a run is invalid, or '' when it is a real attempt."""
    # A full answer that merely discusses rate limits (an SMS provider's, say) is not a harness failure.
    answer = record.get('answer', '')
    failed = record.get('exit') not in (0, None) or len(answer) < 400
    text = (record.get('stderr') or '') + '\n' + (answer if failed else '')
    hit = HARNESS_FAILURE.search(text)
    if hit:
        return hit[0]
    if record.get('condition') == 'without' and record.get('skill_loaded'):
        return 'baseline read the skill under test'
    if record.get('exit') not in (0, None) and not record.get('answer'):
        return f"exit {record.get('exit')} with no answer"
    return ''


# The run allowlist (CLAUDE_TOOLS) is the same for every condition, but it costs more to a skill that
# tells the agent to run shell loops. Older records lack permission_denials, so the answer is read too.
BLOCKED_ANSWER = re.compile(
    r"(need|needs|require|requires|waiting for|once you|if you|after you|please)\s+(your\s+)?(approv|permission|allow)"
    r"|approve (it|this|the|running)|(was|were|been|got) (denied|blocked)|permission (was |is )?(denied|needed|required)"
    r"|not (allowed|permitted) to run|can'?t run|cannot run|couldn'?t run|could not run|unable to run", re.I)


def blocked(record):
    """Why a run was held back by a command the harness did not allow, or '' when it was not. A refused
    command alone does not count: agents usually run the steps one by one instead (in the diagnose rerun,
    24 runs had a refused loop and every one passed its checks). Held back means the answer says it could
    not do something."""
    hit = BLOCKED_ANSWER.search(agent_text(record))
    return f'answer says: {hit[0]}' if hit else ''


def agent_text(record):
    """The agent's own words. A conversation's answer is the whole transcript, and the simulated user's
    replies ("once you approve…") must not count as the agent's."""
    answer = record.get('answer', '')
    if not record.get('turns'):
        return answer
    return '\n\n'.join(part.split('\n', 1)[-1] for part in re.split(r'\n\n(?=\[(?:user|agent)\]\n)', answer)
                       if part.startswith('[agent]\n'))


def denied(record):
    """Commands Claude Code refused during the run, whether or not the agent worked around them."""
    return ', '.join(record.get('permission_denials') or [])[:120]


def prepare(case, skill, host, condition, skill_path=None, peers=()):
    """Copy the fixture into a fresh repo. 'with' installs the skill (and any peers) at project level."""
    WORK_ROOT.mkdir(parents=True, exist_ok=True)
    workdir = new_workdir(skill)
    shutil.copytree(ROOT / case['fixture'], workdir, dirs_exist_ok=True)
    git(workdir, 'init', '-q', '-b', 'main')
    (workdir / '.git/info/exclude').write_text('__pycache__/\n*.pyc\n', encoding='utf-8')
    author = ('-c', 'user.email=eval@example.com', '-c', 'user.name=eval')
    git(workdir, *author, 'add', '.')
    git(workdir, *author, 'commit', '-qm', 'fixture')
    apply_change(case, workdir, author)
    if condition == 'with':
        sources = [Path(skill_path) if skill_path else ROOT / 'skills' / skill, *map(Path, peers)]
        for source in sources:
            shutil.copytree(source, workdir / SKILL_DIR[host] / source.name,
                            ignore=shutil.ignore_patterns('__pycache__'))
        with (workdir / '.git/info/exclude').open('a', encoding='utf-8') as handle:
            handle.write(f'{SKILL_DIR[host].split("/")[0]}/\n')
    return workdir


def apply_change(case, workdir, author):
    """A case's 'change' folder is copied over the fixture: the work to review or clean up.
    With a 'branch' it is committed there and main keeps the fixture; otherwise it stays uncommitted."""
    change = case.get('change')
    if not change:
        return
    if change.get('branch'):
        git(workdir, 'checkout', '-q', '-b', change['branch'])
    shutil.copytree(ROOT / change['path'], workdir, dirs_exist_ok=True)
    if change.get('branch'):
        git(workdir, *author, 'add', '-A')
        git(workdir, *author, 'commit', '-qm', change.get('message', 'change'))
    else:
        # Snapshot the uncommitted change so only the agent's own edits count as its patch.
        git(workdir, 'add', '-A')
        (workdir / '.git/eval-baseline').write_text(git(workdir, 'write-tree').strip(), encoding='utf-8')
        git(workdir, 'reset', '-q')


def parse(host, stdout, workdir, skill):
    loaded, tools, usage, answer, cost, available, denials = set(), 0, {}, '', None, [], []
    for line in stdout.splitlines():
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        text = json.dumps(event)
        for match in re.finditer(r'skills[\\/]+([a-z0-9-]+)[\\/]+SKILL\.md', text.replace('\\\\', '/')):
            loaded.add(match[1])
        if host == 'claude':
            message = event.get('message') if isinstance(event.get('message'), dict) else {}
            content = message.get('content') if isinstance(message.get('content'), list) else []
            for part in content:
                if isinstance(part, dict) and part.get('type') == 'tool_use':
                    tools += 1
                    if part.get('name') == 'Skill':
                        loaded.add(str((part.get('input') or {}).get('skill', '')).split(':')[-1])
            if event.get('type') == 'system' and event.get('subtype') == 'init':
                available = event.get('skills') or []
            if event.get('type') == 'result':
                answer = event.get('result') or ''
                cost = event.get('total_cost_usd')
                denials = [str(d.get('tool_name', '?')) + ': ' + json.dumps(d.get('tool_input', ''))[:80]
                           for d in event.get('permission_denials') or [] if isinstance(d, dict)]
                usage = event.get('usage') or {}
        else:
            item = event.get('item') or {}
            if event.get('type') == 'item.completed' and item.get('type') not in ('agent_message', 'reasoning'):
                tools += 1
            if event.get('type') == 'turn.completed':
                usage = event.get('usage') or usage
    if host == 'codex':
        last = last_message(workdir)
        answer = last.read_text(encoding='utf-8', errors='replace') if last.exists() else ''
    return {'skill_loaded': skill in loaded, 'skills_loaded': sorted(loaded - {''}), 'tool_calls': tools,
            'usage': usage, 'cost_usd': cost, 'answer': answer, 'skill_available': skill in available,
            'permission_denials': denials}


def redact(text):
    """Replace machine-specific paths so results can be committed to a public repository."""
    if not isinstance(text, str):
        return text
    for value, label in ((str(WORK_ROOT), '<eval-runs>'), (str(ROOT), '<repo>'), (str(HOME), '<home>')):
        for form in {value, value.replace('\\', '/'), value.replace('\\', '\\\\')}:
            text = re.sub(re.escape(form), label, text, flags=re.I)
    return text


def redact_record(record):
    """Redact every string in a record, including those inside lists such as permission_denials."""
    if isinstance(record, dict):
        return {k: redact_record(v) for k, v in record.items()}
    if isinstance(record, list):
        return [redact_record(v) for v in record]
    return redact(record)


def full_patch(workdir):
    """Everything the agent changed, new files included, before hidden tests are copied in."""
    baseline = Path(workdir) / '.git/eval-baseline'
    git(workdir, 'add', '-A')
    patch = git(workdir, 'diff', '--cached', *([baseline.read_text(encoding='utf-8')] if baseline.exists() else []))
    git(workdir, 'reset', '-q')
    return patch


def touched_paths(patch, prefixes):
    """Files under the given prefixes that the agent's patch touches."""
    files = re.findall(r'^diff --git a/(\S+)', patch, re.M)
    return sorted({f for f in files if any(f.startswith(p) for p in prefixes)})


def check(case, workdir, answer, skill, patch=''):
    results = []
    changed = [f for f in re.findall(r'^diff --git a/(\S+)', patch, re.M) if not harness_file(f)]
    for spec in case.get('checks', []):
        kind, ok, detail = spec['type'], False, ''
        if kind == 'files_unchanged':
            ok, detail = not changed, ', '.join(changed)
        elif kind == 'files_changed':
            ok = all(any(c.startswith(p) for c in changed) for p in spec['paths'])
            detail = ', '.join(changed)
        elif kind == 'paths_unchanged':
            touched = touched_paths(patch, spec['paths'])
            ok, detail = not touched, ', '.join(touched)
        elif kind == 'answer_matches':
            ok = re.search(spec['pattern'], answer, re.I | re.S) is not None
        elif kind == 'patch_lacks':
            added = '\n'.join(l for l in patch.splitlines() if l.startswith('+') and not l.startswith('+++'))
            hit = re.search(spec['pattern'], added, re.I)
            ok, detail = hit is None, hit[0] if hit else ''
        elif kind == 'file_contains':
            path = workdir / spec['path']
            ok = path.is_file() and spec['text'] in path.read_text(encoding='utf-8', errors='replace')
        elif kind == 'hidden_test':
            for name in spec['files']:
                shutil.copy(ROOT / 'eval' / skill / 'hidden' / name, workdir / name)
            run = subprocess.run([sys.executable, '-m', 'unittest', *spec['modules']], cwd=workdir,
                                 capture_output=True, text=True, encoding='utf-8', errors='replace')
            ok, detail = run.returncode == 0, run.stderr.strip().splitlines()[-1:] if run.stderr else ''
        results.append({'check': spec.get('name', kind), 'passed': ok, 'detail': str(detail)[:300]})
    return results


SIMULATED_USER = """You are playing the user in a conversation with an AI coding agent. You asked it:

{prompt}

What you know and want, as the user (the only source for your answers):
{facts}

Answer only from what you know. If the agent asks something not covered there, say you don't know or that
it should decide. Don't volunteer facts it did not ask about. Never mention that you are simulated.
Do not answer questions about the code: you expect the agent to read the code itself.

The conversation so far:
{transcript}

Write your next message to the agent: short, plain words, answering its questions. Output only the message."""


def transcript_text(turns):
    return '\n\n'.join(f'[{who}]\n{text}' for who, text in turns)


def simulate_user(case, transcript, model='sonnet'):
    """The user's next message in a multi-turn case, written by a model that knows only the case's facts."""
    workdir = new_workdir('user')
    prompt = SIMULATED_USER.format(prompt=case['prompt'], facts=case['simulated_user']['facts'],
                                   transcript=transcript)
    # The prompt goes on stdin: two conversations in one judge prompt pass Windows' 32K command-line limit.
    proc = subprocess.run(['claude', '-p', '--output-format', 'json', '--setting-sources', 'project',
                           '--no-session-persistence', '--model', model, '--disallowedTools',
                           'Bash', 'Edit', 'Write', 'Read', 'Glob', 'Grep', 'Skill', 'Agent', 'Task'],
                          cwd=workdir, capture_output=True, text=True, encoding='utf-8', errors='replace',
                          timeout=300, input=prompt)
    remove_workdir(workdir)
    try:
        result = json.loads(proc.stdout)
        return (result.get('result') or '').strip(), result.get('total_cost_usd') or 0
    except json.JSONDecodeError:
        return '', 0


def forget_session(session_id):
    """A multi-turn run stores a session so it can be resumed; delete it so eval runs never reach the
    user's own session history, or a skill-feedback sweep of it."""
    for path in (HOME / '.claude/projects').glob(f'*/{session_id}*'):
        shutil.rmtree(path, ignore_errors=True) if path.is_dir() else path.unlink(missing_ok=True)


def converse(args, case, prompt, workdir, loaded_name):
    """One case: a single turn, or, for a case with 'simulated_user' (Claude Code only), a conversation in
    which a simulated user answers the agent 'replies' times and may then ask for the 'final' result."""
    run_kwargs = dict(cwd=workdir, capture_output=True, text=True, encoding='utf-8', errors='replace',
                      timeout=args.timeout, stdin=subprocess.DEVNULL, env=child_env(args.host))
    user = case.get('simulated_user')
    if not user or args.host != 'claude':
        proc = subprocess.run(command(args.host, prompt, workdir, args.model, case.get('writable', True)),
                              **run_kwargs)
        return proc, parse(args.host, proc.stdout, workdir, loaded_name)
    replies = user.get('replies', 2)
    session_id, turns, cost, tools, loaded = str(uuid.uuid4()), [], 0.0, 0, False
    message, first, proc = prompt, None, None
    try:
        for turn in range(replies + 1 + bool(user.get('final'))):
            proc = subprocess.run(command(args.host, message, workdir, args.model, case.get('writable', True),
                                          session=(session_id, turn > 0)), **run_kwargs)
            step = parse(args.host, proc.stdout, workdir, loaded_name)
            first = first or step
            cost, tools = cost + (step['cost_usd'] or 0), tools + step['tool_calls']
            loaded = loaded or step['skill_loaded']
            turns += [('user', message if turn else case['prompt']), ('agent', step['answer'])]
            if proc.returncode != 0 or not step['answer']:
                break
            if turn < replies:
                message, user_cost = simulate_user(case, transcript_text(turns))
                cost += user_cost
                if not message:
                    break
            elif user.get('final') and turn == replies:
                message = user['final']
    finally:
        forget_session(session_id)
    agent_text = '\n\n'.join(text for who, text in turns if who == 'agent')
    return proc, {**first, 'answer': transcript_text(turns), 'agent_text': agent_text,
                  'final_answer': turns[-1][1],
                  'cost_usd': round(cost, 4), 'tool_calls': tools, 'skill_loaded': loaded or first['skill_loaded'],
                  'turns': len(turns) // 2}


def run(args):
    spec = json.loads((ROOT / 'eval' / args.skill / 'cases.json').read_text(encoding='utf-8'))
    cases = [c for c in spec['cases'] if not args.case or c['id'] in args.case]
    # Conversations resume a stored session, which only the Claude Code runner supports.
    cases = [c for c in cases if args.host == 'claude' or not c.get('simulated_user')]
    stamp = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
    # --builtin names a skill the host ships (Claude Code's /code-review, say): nothing is installed and the
    # named condition invokes the built-in, so a pack skill can be compared with what users already have.
    if args.builtin:
        args.conditions = ['named']
    variant = (f'{args.builtin}-builtin' if args.builtin
               else Path(args.skill_path).name if args.skill_path else args.skill)
    loaded_name = args.builtin or variant
    out = Path(args.out).resolve() if args.out else ROOT / 'eval' / 'results' / f'{args.skill}-{variant}-{args.host}-{stamp}.jsonl'
    out.parent.mkdir(parents=True, exist_ok=True)
    for case in cases:
        for repeat in range(args.repeats):
            for condition in args.conditions:
                installed = 'without' if condition == 'without' or args.builtin else 'with'
                workdir = prepare(case, args.skill, args.host, installed, args.skill_path, args.peer or ())
                prompt = case['prompt']
                if condition == 'named':
                    prompt = f"{'/' if args.host == 'claude' else '$'}{loaded_name} {prompt}"
                started = time.time()
                proc, parsed = converse(args, case, prompt, workdir, loaded_name)
                if condition == 'named' and args.host == 'claude' and parsed['skill_available']:
                    # Claude Code expands /<skill> into the prompt without a Skill tool call, so the stream
                    # never shows the load; the skill being listed at start-up is what makes the name resolve.
                    parsed['skill_loaded'] = True
                patch = full_patch(workdir)
                # In a conversation only the agent's turns count: the simulated user's answers must not pass a check.
                checks = check(case, workdir, parsed.pop('agent_text', None) or parsed['answer'], args.skill, patch)
                record = {'skill': args.skill, 'variant': variant, 'peers': [Path(p).name for p in args.peer or []],
                          'host': args.host, 'model': args.model, 'case': case['id'],
                          'allowlist': CLAUDE_TOOLS if args.host == 'claude' else None,
                          'condition': condition, 'repeat': repeat, 'exit': proc.returncode,
                          'seconds': round(time.time() - started, 1), 'expect_load': case.get('expect_load'),
                          'passed': all(c['passed'] for c in checks), 'checks': checks,
                          'diff': git(workdir, 'diff', '--stat')[-1500:], 'patch': patch[:8000], **parsed}
                if proc.returncode != 0:
                    errors = [l for l in proc.stdout.splitlines() if '"error"' in l or '"turn.failed"' in l]
                    record['stderr'] = (proc.stderr[-400:] + '\n'.join(errors)[-800:])
                record['error'] = run_error(record)
                with out.open('a', encoding='utf-8') as handle:
                    handle.write(json.dumps(redact_record(record)) + '\n')
                print(f"{case['id']:<22} {condition:<8} r{repeat} pass={record['passed']!s:<5} "
                      f"loaded={parsed['skill_loaded']!s:<5} tools={parsed['tool_calls']:<3} "
                      f"{record['seconds']}s exit={proc.returncode}"
                      + (f" INVALID: {record['error']}" if record['error'] else ''), flush=True)
                if 'usage limit' in record['error'].lower():
                    print('Stopping: the host reports a usage limit, so later runs would be invalid too.')
                    remove_workdir(workdir)
                    summarize(out)
                    return
                remove_workdir(workdir)
                last_message(workdir).unlink(missing_ok=True)
    print(f'\nResults: {out}')
    summarize(out)


def summarize(path):
    rows = [json.loads(line) for line in Path(path).read_text(encoding='utf-8').splitlines() if line]
    groups, invalid = {}, {}
    for row in rows:
        if run_error(row):
            invalid[run_error(row)] = invalid.get(run_error(row), 0) + 1
            continue
        groups.setdefault((row['case'], row['condition']), []).append(row)
    if invalid:
        print('Left out as invalid: ' + ', '.join(f'{n} x {why}' for why, n in invalid.items()))
    print(f"{'case':<22} {'cond':<8} {'pass':>6} {'loaded':>7} {'tools':>6} {'secs':>6} {'tokens/cost':>12}")
    for (case, condition), items in sorted(groups.items()):
        passed = sum(r['passed'] for r in items)
        loaded = sum(r['skill_loaded'] for r in items)
        tools = sum(r['tool_calls'] for r in items) / len(items)
        secs = sum(r['seconds'] for r in items) / len(items)
        costs = [r['cost_usd'] for r in items if r.get('cost_usd') is not None]
        tokens = [sum(v for k, v in (r.get('usage') or {}).items() if isinstance(v, int) and 'tokens' in k)
                  for r in items]
        spend = f"${sum(costs) / len(costs):.2f}" if costs else f"{sum(tokens) // max(len(tokens), 1)}t"
        print(f'{case:<22} {condition:<8} {passed}/{len(items):<4} {loaded}/{len(items):<5} '
              f'{tools:>6.1f} {secs:>6.0f} {spend:>12}')


def rescore(args):
    """Re-apply text-based checks (answer patterns, patch, changed files) to recorded runs after a
    check is corrected. Checks that needed the workspace (hidden tests, file contents) keep their result."""
    path = Path(args.path)
    rows = [json.loads(line) for line in path.read_text(encoding='utf-8').splitlines() if line]
    cases = {c['id']: c for c in json.loads((ROOT / 'eval' / rows[0]['skill'] / 'cases.json')
                                            .read_text(encoding='utf-8'))['cases']}
    changed_count = 0
    for row in rows:
        specs = cases[row['case']].get('checks', [])
        files = sorted({m for m in re.findall(r'^diff --git a/(\S+)', row.get('patch', ''), re.M)
                        if not harness_file(m)})
        old = {c['check']: c for c in row['checks']}
        new = []
        for spec in specs:
            name, kind = spec.get('name', spec['type']), spec['type']
            if kind == 'answer_matches':
                ok, detail = re.search(spec['pattern'], row['answer'], re.I | re.S) is not None, ''
            elif kind == 'files_unchanged':
                ok, detail = not files, ', '.join(files)
            elif kind == 'files_changed':
                ok = all(any(f.startswith(p) for f in files) for p in spec['paths'])
                detail = ', '.join(files)
            elif kind == 'paths_unchanged':
                touched = touched_paths(row.get('patch', ''), spec['paths'])
                ok, detail = not touched, ', '.join(touched)
            elif kind == 'patch_lacks':
                added = '\n'.join(l for l in row.get('patch', '').splitlines()
                                  if l.startswith('+') and not l.startswith('+++'))
                hit = re.search(spec['pattern'], added, re.I)
                ok, detail = hit is None, hit[0] if hit else ''
            elif name in old:
                new.append(old[name])
                continue
            else:
                ok, detail = False, 'not recorded'
            new.append({'check': name, 'passed': ok, 'detail': str(detail)[:300]})
        passed = all(c['passed'] for c in new)
        changed_count += passed != row['passed']
        row['checks'], row['passed'], row['error'] = new, passed, run_error(row)
    path.write_text(''.join(json.dumps(redact_record(r)) + '\n' for r in rows), encoding='utf-8')
    print(f'Rescored {len(rows)} runs; {changed_count} changed pass/fail.')
    summarize(path)


JUDGE_PROMPT = """You are grading two answers to the same software task. You do not know how either was produced.
Do not use any tools. Judge only from the text below.

TASK GIVEN TO THE AGENT:
{task}

WHAT IS ACTUALLY TRUE (ground truth for grading, not shown to the agent):
{truth}

Rubric, in order of weight:
{rubric}

=== ANSWER A ===
{a}
=== CHANGES A MADE ===
{pa}
=== HIDDEN BEHAVIOR TESTS RUN ON A'S RESULT ===
{ta}

=== ANSWER B ===
{b}
=== CHANGES B MADE ===
{pb}
=== HIDDEN BEHAVIOR TESTS RUN ON B'S RESULT ===
{tb}

Reply with one line of JSON and nothing else:
{{"winner": "A" | "B" | "tie", "reason": "<one sentence>"}}"""


DEFAULT_RUBRIC = [
    'Correct cause: identifies the real cause and does not endorse a wrong one.',
    'Evidence: claims are backed by something run or read, not asserted.',
    'Scope: did what was asked and nothing more (no edits on a diagnosis-only task; a fix that does not hide the symptom).',
    'Honesty: states what was not verified.',
    'Concision: no padding. Length alone is not a virtue.',
]


def hidden_results(case, row):
    """Results of the case's hidden behavior tests: objective, and say nothing about which skill ran."""
    names = {c.get('name', c['type']) for c in case.get('checks', []) if c['type'] == 'hidden_test'}
    found = [f"{c['check']}: {'passed' if c['passed'] else 'FAILED'}" for c in row.get('checks', [])
             if c['check'] in names]
    return '\n'.join(found) or '(none for this task)'


def ask_judge(case, first, second, model, rubric=None):
    lines = rubric or DEFAULT_RUBRIC
    limit = 16000 if case.get('simulated_user') else 6000  # a conversation is judged whole
    prompt = JUDGE_PROMPT.format(task=case['prompt'], truth=case['judge_truth'],
                                 rubric='\n'.join(f'{i}. {line}' for i, line in enumerate(lines, 1)),
                                 a=first['answer'][:limit], pa=first.get('patch', '')[:4000] or '(none)',
                                 b=second['answer'][:limit], pb=second.get('patch', '')[:4000] or '(none)',
                                 ta=hidden_results(case, first), tb=hidden_results(case, second))
    workdir = new_workdir('judge')
    # The prompt goes on stdin: two conversations in one judge prompt pass Windows' 32K command-line limit.
    proc = subprocess.run(['claude', '-p', '--output-format', 'json', '--setting-sources', 'project',
                           '--no-session-persistence', '--model', model, '--disallowedTools',
                           'Bash', 'Edit', 'Write', 'Read', 'Glob', 'Grep', 'Skill'],
                          cwd=workdir, capture_output=True, text=True, encoding='utf-8', errors='replace',
                          timeout=600, input=prompt)
    remove_workdir(workdir)
    try:
        text = json.loads(proc.stdout).get('result', '')
        return json.loads(re.search(r'\{.*\}', text, re.S)[0])
    except (json.JSONDecodeError, TypeError):
        return {'winner': 'error', 'reason': (proc.stdout or proc.stderr)[-200:]}


def side_label(row, by_variant):
    return f"{row['variant']}:{row['condition']}" if by_variant else row['condition']


def judge(args):
    """Blind pairwise verdicts per case and repeat. With --against, the right-hand condition comes from a
    second results file, so two skills run on the same cases can be compared; sides are then labelled
    variant:condition."""
    rows = [json.loads(line) for line in Path(args.path).read_text(encoding='utf-8').splitlines() if line]
    others = ([json.loads(line) for line in Path(args.against).read_text(encoding='utf-8').splitlines() if line]
              if args.against else rows)
    skill = rows[0]['skill']
    spec = json.loads((ROOT / 'eval' / skill / 'cases.json').read_text(encoding='utf-8'))
    cases = {c['id']: c for c in spec['cases']}
    left, right = args.pair
    by_variant = bool(args.against)
    left_label = side_label({'variant': rows[0]['variant'], 'condition': left}, by_variant)
    right_label = side_label({'variant': others[0]['variant'], 'condition': right}, by_variant)
    if left_label == right_label:
        sys.exit(f'Both sides are {left_label}; pick different conditions or a different file.')
    # --outcome-only judges on the suite's outcome_rubric: what was found or kept, scope and concision, with the
    # criteria that reward a skill's reporting style (evidence shown, coverage stated) left out.
    rubric = spec.get('outcome_rubric') if args.outcome_only else spec.get('rubric')
    if args.outcome_only and not rubric:
        sys.exit(f'{skill} has no outcome_rubric in its cases.json.')
    rng = __import__('random').Random(args.seed)
    if args.out:
        out = Path(args.out).resolve()
    else:
        suffix = (f'.judge-{left_label}-vs-{right_label}' if by_variant else f'.judge-{left}-vs-{right}').replace(':', '-')
        out = Path(str(Path(args.path).resolve()).replace('.jsonl', suffix + '.jsonl'))
    WORK_ROOT.mkdir(parents=True, exist_ok=True)
    # --redo-errors re-judges only the pairs an earlier run recorded as judge errors; every other verdict stays.
    kept, redo = {}, set()
    if args.redo_errors and out.exists():
        for line in out.read_text(encoding='utf-8').splitlines():
            if line:
                previous = json.loads(line)
                key = (previous['case'], previous['repeat'])
                (redo.add(key) if previous['winner'] == 'error' else kept.__setitem__(key, previous))
        out.write_text(''.join(json.dumps(v) + '\n' for v in kept.values()), encoding='utf-8')
    for row in rows:
        if row['condition'] != left:
            continue
        other = next((r for r in others if r['case'] == row['case'] and r['repeat'] == row['repeat']
                      and r['condition'] == right), None)
        case = cases.get(row['case'], {})
        if other is None or not case.get('judge_truth') or run_error(row) or run_error(other):
            continue
        flip = rng.random() < 0.5  # drawn for every pair, so a redo shows each pair in its original order
        if args.redo_errors and (row['case'], row['repeat']) not in redo:
            continue
        orders = [(other, row) if flip else (row, other)]
        if args.both_orders:
            orders.append(orders[0][::-1])
        labels, reasons = [], []
        for first, second in orders:
            verdict = ask_judge(case, first, second, args.model, rubric)
            names = {'A': side_label(first, by_variant), 'B': side_label(second, by_variant), 'TIE': 'tie'}
            labels.append(names.get(str(verdict.get('winner', '')).strip().upper(), 'error'))
            reasons.append(verdict.get('reason', ''))
        # With both orders, a win counts only when both verdicts agree; otherwise it is a tie.
        label = 'error' if 'error' in labels else labels[0] if len(set(labels)) == 1 else 'tie'
        first = orders[0][0]
        verdict_row = {'case': row['case'], 'repeat': row['repeat'], 'sides': [left_label, right_label],
                       'shown_first': side_label(first, by_variant), 'winner': label, 'verdicts': labels,
                       'reasons': [redact(r) for r in reasons], 'judge': args.model,
                       'blocked': [redact(blocked(row)), redact(blocked(other))],
                       'denied': [redact(denied(row)), redact(denied(other))],
                       'rubric': 'outcome' if args.outcome_only else 'suite'}
        with out.open('a', encoding='utf-8') as handle:
            handle.write(json.dumps(verdict_row) + '\n')
        print(f"{row['case']:<28} r{row['repeat']} winner={label:<24} {reasons[0][:100]}", flush=True)
    print(f'\nJudge: {args.model}. Verdicts: {out}')
    retally(out)


def retally(path):
    """Tally a verdict file twice: every pair, and without pairs where either run was held back by the allowlist."""
    rows = [json.loads(line) for line in Path(path).read_text(encoding='utf-8').splitlines() if line]
    if not rows:
        print('No verdicts.')
        return
    left, right = rows[0]['sides']
    for title, keep in (('All judged pairs', lambda r: True),
                        ('Without pairs where a run was held back by the allowlist', lambda r: not any(r.get('blocked', ())))):
        tally = {}
        for row in filter(keep, rows):
            tally.setdefault(row['case'], {}).setdefault(row['winner'], 0)
            tally[row['case']][row['winner']] += 1
        print(f'{title}:')
        report_tally(tally, left, right)


def wilson(k, n, z=1.96):
    """95% interval for a share of k in n pairs. With a dozen pairs it is wide: 8/12 spans about 39% to 86%,
    so a share near a threshold does not show which side of it the skill is on."""
    if not n:
        return 0.0, 0.0
    p, d = k / n, 1 + z * z / n
    centre, half = (p + z * z / (2 * n)) / d, z * ((p * (1 - p) + z * z / (4 * n)) / n) ** 0.5 / d
    return max(0.0, centre - half), min(1.0, centre + half)


def report_tally(tally, left, right):
    total = {}
    for case, counts in tally.items():
        print(f'  {case:<28} ' + ', '.join(f'{k}={v}' for k, v in sorted(counts.items())))
        for k, v in counts.items():
            total[k] = total.get(k, 0) + v
    errors = total.pop('error', 0)
    n = sum(total.values())
    if n:
        wins_or_ties = total.get(left, 0) + total.get('tie', 0)
        print(f"  overall: {left} wins {total.get(left, 0)}, ties {total.get('tie', 0)}, loses {total.get(right, 0)}; "
              f'wins or ties {wins_or_ties}/{n} ({100 * wins_or_ties / n:.0f}%, 95% interval '
              f'{100 * wilson(wins_or_ties, n)[0]:.0f}-{100 * wilson(wins_or_ties, n)[1]:.0f}%) against {right}'
              + (f'; {errors} judge errors left out' if errors else ''))


def probe(args):
    workdir = new_workdir('probe')
    git(workdir, 'init', '-q')
    prompt = 'List the names of every skill available to you, comma separated, nothing else.'
    proc = subprocess.run(command(args.host, prompt, workdir, args.model, writable=False), cwd=workdir,
                          capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=300,
                          stdin=subprocess.DEVNULL, env=child_env(args.host))
    print(parse(args.host, proc.stdout, workdir, '')['answer'] or proc.stderr[-1000:])
    remove_workdir(workdir)


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest='command', required=True)
    p_probe = sub.add_parser('probe')
    p_run = sub.add_parser('run')
    p_sum = sub.add_parser('summarize')
    p_rescore = sub.add_parser('rescore', help='re-apply corrected text-based checks to recorded runs')
    p_rescore.add_argument('path')
    p_judge = sub.add_parser('judge', help='blind pairwise comparison of two conditions in a results file')
    p_judge.add_argument('path')
    p_judge.add_argument('--pair', nargs=2, default=['named', 'without'], metavar=('CONDITION', 'BASELINE'))
    p_judge.add_argument('--model', default='opus', help='use a different model from the one under test')
    p_judge.add_argument('--seed', type=int, default=7)
    p_judge.add_argument('--against', help='take the right-hand condition from this results file (another skill)')
    p_judge.add_argument('--out', help='write verdicts here instead of beside the results file')
    p_judge.add_argument('--redo-errors', action='store_true',
                         help='re-judge only the pairs the verdict file records as judge errors')
    p_judge.add_argument('--outcome-only', action='store_true',
                         help="judge on the suite's outcome_rubric, without criteria about reporting style")
    p_judge.add_argument('--both-orders', action='store_true',
                         help='judge each pair in both orders; count a win only when the verdicts agree')
    for p in (p_probe, p_run):
        p.add_argument('--host', choices=['claude', 'codex'], required=True)
        p.add_argument('--model')
    p_run.add_argument('skill')
    p_run.add_argument('--repeats', type=int, default=3)
    p_run.add_argument('--case', action='append')
    p_run.add_argument('--timeout', type=int, default=900)
    p_run.add_argument('--conditions', nargs='+', default=['without', 'with', 'named'],
                       choices=['without', 'with', 'named'],
                       help='without: no skill; with: installed, host decides; named: installed and invoked by name')
    p_run.add_argument('--out', help='append to this results file instead of starting a new one')
    p_run.add_argument('--skill-path', help='test another skill folder (e.g. a third-party skill) against these cases')
    p_run.add_argument('--peer', action='append', help='also install this skill folder, for skills that call others')
    p_run.add_argument('--builtin', help="invoke the host's own skill of this name instead of installing one")
    p_sum.add_argument('path')
    p_tally = sub.add_parser('tally', help='re-count a verdict file, with and without allowlist-blocked pairs')
    p_tally.add_argument('path')
    args = parser.parse_args()
    {'probe': probe, 'run': run, 'judge': judge, 'rescore': rescore,
     'summarize': lambda a: summarize(a.path), 'tally': lambda a: retally(a.path)}[args.command](args)


if __name__ == '__main__':
    main()
