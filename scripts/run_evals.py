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
CLAUDE_TOOLS = ['Read', 'Grep', 'Glob', 'Edit', 'Write', 'Skill', 'Agent', 'Task', 'Bash(python *)',
                'Bash(git *)', 'Bash(ls *)', 'Bash(cat *)']


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


def command(host, prompt, workdir, model=None, writable=True):
    if host == 'claude':
        args = ['claude', '-p', prompt, '--output-format', 'stream-json', '--verbose',
                '--setting-sources', 'project', '--no-session-persistence',
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
    loaded, tools, usage, answer, cost, available = set(), 0, {}, '', None, []
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
            'usage': usage, 'cost_usd': cost, 'answer': answer, 'skill_available': skill in available}


def redact(text):
    """Replace machine-specific paths so results can be committed to a public repository."""
    if not isinstance(text, str):
        return text
    for value, label in ((str(WORK_ROOT), '<eval-runs>'), (str(ROOT), '<repo>'), (str(HOME), '<home>')):
        for form in {value, value.replace('\\', '/'), value.replace('\\', '\\\\')}:
            text = re.sub(re.escape(form), label, text, flags=re.I)
    return text


def redact_record(record):
    return {k: redact(v) if isinstance(v, str) else v for k, v in record.items()}


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


def run(args):
    spec = json.loads((ROOT / 'eval' / args.skill / 'cases.json').read_text(encoding='utf-8'))
    cases = [c for c in spec['cases'] if not args.case or c['id'] in args.case]
    stamp = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
    variant = Path(args.skill_path).name if args.skill_path else args.skill
    loaded_name = variant
    out = Path(args.out).resolve() if args.out else ROOT / 'eval' / 'results' / f'{args.skill}-{variant}-{args.host}-{stamp}.jsonl'
    out.parent.mkdir(parents=True, exist_ok=True)
    for case in cases:
        for repeat in range(args.repeats):
            for condition in args.conditions:
                installed = 'without' if condition == 'without' else 'with'
                workdir = prepare(case, args.skill, args.host, installed, args.skill_path, args.peer or ())
                prompt = case['prompt']
                if condition == 'named':
                    prompt = f"{'/' if args.host == 'claude' else '$'}{loaded_name} {prompt}"
                started = time.time()
                proc = subprocess.run(command(args.host, prompt, workdir, args.model,
                                              case.get('writable', True)),
                                      cwd=workdir, capture_output=True, text=True, encoding='utf-8',
                                      errors='replace', timeout=args.timeout,
                                      stdin=subprocess.DEVNULL, env=child_env(args.host))
                parsed = parse(args.host, proc.stdout, workdir, loaded_name)
                if condition == 'named' and args.host == 'claude' and parsed['skill_available']:
                    # Claude Code expands /<skill> into the prompt without a Skill tool call, so the stream
                    # never shows the load; the skill being listed at start-up is what makes the name resolve.
                    parsed['skill_loaded'] = True
                patch = full_patch(workdir)
                checks = check(case, workdir, parsed['answer'], args.skill, patch)
                record = {'skill': args.skill, 'variant': variant, 'peers': [Path(p).name for p in args.peer or []],
                          'host': args.host, 'model': args.model, 'case': case['id'],
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
                    shutil.rmtree(workdir, ignore_errors=True)
                    summarize(out)
                    return
                shutil.rmtree(workdir, ignore_errors=True)
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
    prompt = JUDGE_PROMPT.format(task=case['prompt'], truth=case['judge_truth'],
                                 rubric='\n'.join(f'{i}. {line}' for i, line in enumerate(lines, 1)),
                                 a=first['answer'][:6000], pa=first.get('patch', '')[:4000] or '(none)',
                                 b=second['answer'][:6000], pb=second.get('patch', '')[:4000] or '(none)',
                                 ta=hidden_results(case, first), tb=hidden_results(case, second))
    workdir = new_workdir('judge')
    proc = subprocess.run(['claude', '-p', prompt, '--output-format', 'json', '--setting-sources', 'project',
                           '--no-session-persistence', '--model', model, '--disallowedTools',
                           'Bash', 'Edit', 'Write', 'Read', 'Glob', 'Grep', 'Skill'],
                          cwd=workdir, capture_output=True, text=True, encoding='utf-8', errors='replace',
                          timeout=600, stdin=subprocess.DEVNULL)
    shutil.rmtree(workdir, ignore_errors=True)
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
    rng = __import__('random').Random(args.seed)
    if args.out:
        out = Path(args.out).resolve()
    else:
        suffix = (f'.judge-{left_label}-vs-{right_label}' if by_variant else f'.judge-{left}-vs-{right}').replace(':', '-')
        out = Path(str(Path(args.path).resolve()).replace('.jsonl', suffix + '.jsonl'))
    tally = {}
    WORK_ROOT.mkdir(parents=True, exist_ok=True)
    for row in rows:
        if row['condition'] != left:
            continue
        other = next((r for r in others if r['case'] == row['case'] and r['repeat'] == row['repeat']
                      and r['condition'] == right), None)
        case = cases.get(row['case'], {})
        if other is None or not case.get('judge_truth') or run_error(row) or run_error(other):
            continue
        flip = rng.random() < 0.5
        orders = [(other, row) if flip else (row, other)]
        if args.both_orders:
            orders.append(orders[0][::-1])
        labels, reasons = [], []
        for first, second in orders:
            verdict = ask_judge(case, first, second, args.model, spec.get('rubric'))
            names = {'A': side_label(first, by_variant), 'B': side_label(second, by_variant)}
            labels.append(names.get(verdict.get('winner'), 'error'))
            reasons.append(verdict.get('reason', ''))
        # With both orders, a win counts only when both verdicts agree; otherwise it is a tie.
        label = 'error' if 'error' in labels else labels[0] if len(set(labels)) == 1 else 'tie'
        first = orders[0][0]
        tally.setdefault(row['case'], {}).setdefault(label, 0)
        tally[row['case']][label] += 1
        with out.open('a', encoding='utf-8') as handle:
            handle.write(json.dumps({'case': row['case'], 'repeat': row['repeat'],
                                     'shown_first': side_label(first, by_variant), 'winner': label,
                                     'verdicts': labels, 'reasons': [redact(r) for r in reasons],
                                     'judge': args.model}) + '\n')
        print(f"{row['case']:<28} r{row['repeat']} winner={label:<24} {reasons[0][:100]}", flush=True)
    print(f'\nJudge: {args.model}. Verdicts: {out}')
    report_tally(tally, left_label, right_label)


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
              f'wins or ties {wins_or_ties}/{n} ({100 * wins_or_ties / n:.0f}%) against {right}'
              + (f'; {errors} judge errors left out' if errors else ''))


def probe(args):
    workdir = new_workdir('probe')
    git(workdir, 'init', '-q')
    prompt = 'List the names of every skill available to you, comma separated, nothing else.'
    proc = subprocess.run(command(args.host, prompt, workdir, args.model, writable=False), cwd=workdir,
                          capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=300,
                          stdin=subprocess.DEVNULL, env=child_env(args.host))
    print(parse(args.host, proc.stdout, workdir, '')['answer'] or proc.stderr[-1000:])
    shutil.rmtree(workdir, ignore_errors=True)


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
    p_sum.add_argument('path')
    args = parser.parse_args()
    {'probe': probe, 'run': run, 'judge': judge, 'rescore': rescore,
     'summarize': lambda a: summarize(a.path)}[args.command](args)


if __name__ == '__main__':
    main()
