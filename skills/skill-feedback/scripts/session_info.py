"""Print a session's metadata, or an installed skill's version. Never prints conversation text.

Usage:
    python session_info.py <session.jsonl>
    python session_info.py --lock <project-root> [--skill NAME]

A session file is one Codex rollout (~/.codex/sessions/...) or one Claude Code
transcript (~/.claude/projects/...). Read-only; no network.
"""

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

SKILL_PATH = re.compile(r'skills/(?:\.system/)?([a-z0-9][a-z0-9-]{0,63})/SKILL\.md')


def summarize(path):
    host, models, versions = None, Counter(), set()
    skills, turns, first, last = Counter(), 0, None, None
    codex_events = Counter()
    with open(path, encoding='utf-8', errors='replace') as handle:
        for line in handle:
            try:
                entry = json.loads(line)
            except json.JSONDecodeError:
                continue
            if not isinstance(entry, dict):
                continue
            kind = entry.get('type')
            payload = entry.get('payload') if isinstance(entry.get('payload'), dict) else {}
            stamp = entry.get('timestamp')
            if stamp:
                first, last = first or stamp, stamp
            if kind in ('session_meta', 'turn_context', 'response_item', 'event_msg'):
                host = 'Codex'
                if payload.get('cli_version'):
                    versions.add(payload['cli_version'])
                if kind == 'turn_context' and payload.get('model'):
                    models[payload['model']] += 1
                if kind == 'event_msg' and payload.get('type') in ('task_started', 'user_message'):
                    codex_events[payload['type']] += 1
            elif kind in ('user', 'assistant') and 'sessionId' in entry:
                host = 'Claude Code'
                if entry.get('version'):
                    versions.add(entry['version'])
                message = entry.get('message') if isinstance(entry.get('message'), dict) else {}
                if kind == 'assistant' and message.get('model'):
                    models[message['model']] += 1
                content = message.get('content')
                if kind == 'user' and isinstance(content, str):
                    turns += 1
                for part in content if isinstance(content, list) else []:
                    if isinstance(part, dict) and part.get('type') == 'tool_use' and part.get('name') == 'Skill':
                        name = (part.get('input') or {}).get('skill')
                        if isinstance(name, str):
                            skills[name.split(':')[-1]] += 1
            if 'SKILL.md' in line:
                for match in SKILL_PATH.finditer(re.sub(r'[\\/]+', '/', line)):
                    skills[match[1]] += 1
    turns += max(codex_events.values(), default=0)
    print(f'Host: {host or "unknown"} {", ".join(sorted(versions))}'.rstrip())
    print(f'Models: {", ".join(m for m, _ in models.most_common()) or "unknown"}')
    print(f'Time: {first or "?"} to {last or "?"}')
    print(f'User turns: {turns}')
    print('Skills referenced (count includes listings, not only loads):')
    for name, count in skills.most_common():
        print(f'  {name}: {count}')
    if not skills:
        print('  none')
    return 0


def lock_info(root, wanted):
    lock = Path(root) / 'skills-lock.json'
    if not lock.is_file():
        print(f'No skills-lock.json in {root}. The skill may be installed globally or copied by hand.')
        return 1
    entries = (json.loads(lock.read_text(encoding='utf-8')).get('skills') or {})
    shown = 0
    for name, info in sorted(entries.items()):
        if wanted and name != wanted:
            continue
        shown += 1
        ref = info.get('ref') or info.get('commit') or ''
        digest = (info.get('computedHash') or '')[:12]
        print(f'{name}: source={info.get("source")} {("ref=" + ref) if ref else ""} hash={digest}'.replace('  ', ' '))
    if not shown:
        print(f'{wanted} is not in {lock}.')
        return 1
    return 0


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('session', nargs='?')
    parser.add_argument('--lock', metavar='PROJECT_ROOT')
    parser.add_argument('--skill')
    args = parser.parse_args(argv)
    if args.lock:
        return lock_info(args.lock, args.skill)
    if not args.session or not Path(args.session).is_file():
        parser.error('give a session .jsonl file, or --lock PROJECT_ROOT')
    return summarize(args.session)


if __name__ == '__main__':
    sys.exit(main())
