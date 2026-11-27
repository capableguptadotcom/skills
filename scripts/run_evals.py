"""Run a skill's evaluation cases with and without the skill, in Codex and Claude Code.

Usage:
    python scripts/run_evals.py probe --host codex
    python scripts/run_evals.py run diagnose --host claude --repeats 2 [--case ID] [--model sonnet]
    python scripts/run_evals.py summarize eval/results/<file>.jsonl

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
import tempfile
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HOME = Path.home()
# Under the repo's ignored .cache/: Codex's Windows sandbox cannot reach folders under %TEMP%.
WORK_ROOT = Path(os.environ.get('EVAL_WORK_ROOT', ROOT / '.cache' / 'eval-runs'))
SKILL_DIR = {'claude': '.claude/skills', 'codex': '.agents/skills'}
CLAUDE_TOOLS = ['Read', 'Grep', 'Glob', 'Edit', 'Write', 'Skill', 'Bash(python *)', 'Bash(git *)',
                'Bash(ls *)', 'Bash(cat *)']


def codex_binary():
    explicit = os.environ.get('CODEX_BIN')
    if explicit:
        return explicit
    bundled = sorted((HOME / 'AppData/Local/OpenAI/Codex/bin').glob('*/codex.exe'),
                     key=lambda p: p.stat().st_mtime)
    return str(bundled[-1]) if bundled else (shutil.which('codex') or 'codex')


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
            '-o', str(Path(workdir) / '.eval-last-message.txt')]
    return args + (['-m', model] if model else []) + [prompt]


def git(workdir, *args):
    return subprocess.run(['git', *args], cwd=workdir, capture_output=True, text=True,
                          encoding='utf-8', errors='replace').stdout


def prepare(case, skill, host, condition, skill_path=None, peers=()):
    """Copy the fixture into a fresh repo. 'with' installs the skill (and any peers) at project level."""
    WORK_ROOT.mkdir(parents=True, exist_ok=True)
    workdir = Path(tempfile.mkdtemp(prefix=f'{skill}-', dir=WORK_ROOT))
    shutil.copytree(ROOT / case['fixture'], workdir, dirs_exist_ok=True)
    git(workdir, 'init', '-q')
    git(workdir, '-c', 'user.email=eval@example.com', '-c', 'user.name=eval', 'add', '.')
    git(workdir, '-c', 'user.email=eval@example.com', '-c', 'user.name=eval', 'commit', '-qm', 'fixture')
    if condition == 'with':
        sources = [Path(skill_path) if skill_path else ROOT / 'skills' / skill, *map(Path, peers)]
        for source in sources:
            shutil.copytree(source, workdir / SKILL_DIR[host] / source.name,
                            ignore=shutil.ignore_patterns('__pycache__'))
        (workdir / '.git/info/exclude').write_text(f'{SKILL_DIR[host].split("/")[0]}/\n', encoding='utf-8')
    return workdir


def parse(host, stdout, workdir, skill):
    loaded, tools, usage, answer, cost = set(), 0, {}, '', None
    for line in stdout.splitlines():
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        text = json.dumps(event)
        for match in re.finditer(r'skills[\\/]+([a-z0-9-]+)[\\/]+SKILL\.md', text.replace('\\\\', '/')):
            loaded.add(match[1])
        if host == 'claude':
            message = event.get('message') or {}
            for part in message.get('content') or [] if isinstance(message.get('content'), list) else []:
                if part.get('type') == 'tool_use':
                    tools += 1
                    if part.get('name') == 'Skill':
                        loaded.add(str((part.get('input') or {}).get('skill', '')).split(':')[-1])
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
        last = workdir / '.eval-last-message.txt'
        answer = last.read_text(encoding='utf-8', errors='replace') if last.exists() else ''
    return {'skill_loaded': skill in loaded, 'skills_loaded': sorted(loaded - {''}), 'tool_calls': tools,
            'usage': usage, 'cost_usd': cost, 'answer': answer}


def check(case, workdir, answer, skill):
    results = []
    changed = [line[3:] for line in git(workdir, 'status', '--porcelain').splitlines()
               if not line[3:].startswith(('.claude/', '.agents/', '.eval-'))]
    for spec in case.get('checks', []):
        kind, ok, detail = spec['type'], False, ''
        if kind == 'files_unchanged':
            ok, detail = not changed, ', '.join(changed)
        elif kind == 'files_changed':
            ok = all(any(c.startswith(p) for c in changed) for p in spec['paths'])
            detail = ', '.join(changed)
        elif kind == 'answer_matches':
            ok = re.search(spec['pattern'], answer, re.I | re.S) is not None
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
    out = ROOT / 'eval' / 'results' / f'{args.skill}-{variant}-{args.host}-{stamp}.jsonl'
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
                                      errors='replace', timeout=args.timeout)
                parsed = parse(args.host, proc.stdout, workdir, loaded_name)
                checks = check(case, workdir, parsed['answer'], args.skill)
                record = {'skill': args.skill, 'variant': variant, 'peers': [Path(p).name for p in args.peer or []],
                          'host': args.host, 'model': args.model, 'case': case['id'],
                          'condition': condition, 'repeat': repeat, 'exit': proc.returncode,
                          'seconds': round(time.time() - started, 1), 'expect_load': case.get('expect_load'),
                          'passed': all(c['passed'] for c in checks), 'checks': checks,
                          'diff': git(workdir, 'diff', '--stat')[-1500:], **parsed}
                if proc.returncode != 0:
                    record['stderr'] = proc.stderr[-800:]
                with out.open('a', encoding='utf-8') as handle:
                    handle.write(json.dumps(record) + '\n')
                print(f"{case['id']:<22} {condition:<8} r{repeat} pass={record['passed']!s:<5} "
                      f"loaded={parsed['skill_loaded']!s:<5} tools={parsed['tool_calls']:<3} "
                      f"{record['seconds']}s exit={proc.returncode}", flush=True)
                shutil.rmtree(workdir, ignore_errors=True)
    print(f'\nResults: {out.relative_to(ROOT)}')
    summarize(out)


def summarize(path):
    rows = [json.loads(line) for line in Path(path).read_text(encoding='utf-8').splitlines() if line]
    groups = {}
    for row in rows:
        groups.setdefault((row['case'], row['condition']), []).append(row)
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


def probe(args):
    WORK_ROOT.mkdir(parents=True, exist_ok=True)
    workdir = Path(tempfile.mkdtemp(prefix='probe-', dir=WORK_ROOT))
    git(workdir, 'init', '-q')
    prompt = 'List the names of every skill available to you, comma separated, nothing else.'
    proc = subprocess.run(command(args.host, prompt, workdir, args.model, writable=False), cwd=workdir,
                          capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=300)
    print(parse(args.host, proc.stdout, workdir, '')['answer'] or proc.stderr[-1000:])
    shutil.rmtree(workdir, ignore_errors=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest='command', required=True)
    p_probe = sub.add_parser('probe')
    p_run = sub.add_parser('run')
    p_sum = sub.add_parser('summarize')
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
    p_run.add_argument('--skill-path', help='test another skill folder (e.g. a third-party skill) against these cases')
    p_run.add_argument('--peer', action='append', help='also install this skill folder, for skills that call others')
    p_sum.add_argument('path')
    args = parser.parse_args()
    {'probe': probe, 'run': run, 'summarize': lambda a: summarize(a.path)}[args.command](args)


if __name__ == '__main__':
    main()
