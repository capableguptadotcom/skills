"""Print the Git state a handoff note needs.

Usage (from the repository root):
    python <skill>/scripts/handoff_state.py

Read-only: runs only local git commands.
"""

import subprocess
import sys


def git(*args):
    result = subprocess.run(['git', *args], capture_output=True, text=True,
                            encoding='utf-8', errors='replace')
    return result.stdout.rstrip() if result.returncode == 0 else ''


def section(title, body):
    print(f'{title}:')
    print('\n'.join(f'  {line}' for line in body.splitlines()) if body else '  none')


def main():
    if git('rev-parse', '--is-inside-work-tree') != 'true':
        print('Not inside a Git work tree.')
        return 2
    branch = git('rev-parse', '--abbrev-ref', 'HEAD')
    upstream = git('rev-parse', '--abbrev-ref', '--symbolic-full-name', '@{upstream}')
    print(f'Branch: {branch}')
    print(f'Commit: {git("log", "-1", "--format=%h %s")}')
    if upstream:
        counts = git('rev-list', '--left-right', '--count', f'{upstream}...HEAD').split()
        if len(counts) == 2:
            print(f'Upstream: {upstream} (behind {counts[0]}, ahead {counts[1]})')
    else:
        print('Upstream: none (branch not pushed)')
    section('Staged', git('diff', '--cached', '--stat'))
    section('Unstaged', git('diff', '--stat'))
    section('Untracked', git('ls-files', '--others', '--exclude-standard'))
    section('Recent commits', git('log', '-5', '--format=%h %ad %s', '--date=short'))
    section('Stashes', git('stash', 'list'))
    return 0


if __name__ == '__main__':
    sys.exit(main())
