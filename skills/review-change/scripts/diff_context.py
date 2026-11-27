"""Print the scope of a change: base, changed files and tests that mention them.

Usage (from the repository root):
    python <skill>/scripts/diff_context.py [BASE]

Without BASE, the base is the merge-base with the default branch, or HEAD when
already on the default branch. Uncommitted changes are always included.
Read-only: runs only local git commands.
"""

import re
import subprocess
import sys
from pathlib import PurePosixPath

TEST_PATHSPECS = [':(glob)**/test_*', ':(glob)**/*_test.*', ':(glob)**/*.test.*',
                  ':(glob)**/*.spec.*', ':(glob)**/tests/**', ':(glob)**/__tests__/**']
MAX_STEMS = 30


def git(*args, check=True):
    result = subprocess.run(['git', *args], capture_output=True, text=True,
                            encoding='utf-8', errors='replace')
    if check and result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or f'git {" ".join(args)} failed')
    return result.stdout.strip() if result.returncode == 0 else ''


def default_branch():
    ref = git('symbolic-ref', '--quiet', 'refs/remotes/origin/HEAD', check=False)
    if ref:
        return ref.removeprefix('refs/remotes/')
    for name in ('origin/main', 'origin/master', 'main', 'master'):
        if git('rev-parse', '--verify', '--quiet', name, check=False):
            return name
    return None


def choose_base(requested):
    if requested:
        return requested, git('rev-parse', '--short', requested)
    branch = default_branch()
    head = git('rev-parse', 'HEAD')
    if branch:
        base = git('merge-base', 'HEAD', branch, check=False)
        if base and base != head:
            return f'merge-base with {branch}', base[:9]
    return 'HEAD (uncommitted changes only)', head[:9]


def is_test(path):
    name = PurePosixPath(path).name
    parts = PurePosixPath(path).parts
    return (name.startswith('test_') or re.search(r'(_test|\.test|\.spec)\.', name) is not None
            or 'tests' in parts or '__tests__' in parts)


def main(argv):
    if git('rev-parse', '--is-inside-work-tree', check=False) != 'true':
        print('Not inside a Git work tree.')
        return 2
    label, base = choose_base(argv[1] if len(argv) > 1 else None)
    print(f'Base: {label} ({base})')
    print(f'Head: {git("rev-parse", "--abbrev-ref", "HEAD")} ({git("rev-parse", "--short", "HEAD")})')

    changed = []
    for line in git('diff', '--numstat', '--no-renames', base).splitlines():
        added, removed, path = line.split('\t', 2)
        changed.append((path, added, removed))
    untracked = git('ls-files', '--others', '--exclude-standard').splitlines()

    print(f'\nChanged files ({len(changed)} tracked, {len(untracked)} untracked):')
    for path, added, removed in changed:
        print(f'  +{added:>5} -{removed:>5}  {path}')
    for path in untracked:
        print(f'  untracked     {path}')

    changed_paths = [p for p, _, _ in changed] + untracked
    print('\nChanged tests:')
    tests = [p for p in changed_paths if is_test(p)]
    print('\n'.join(f'  {p}' for p in tests) or '  none')

    stems = []
    for path in changed_paths:
        stem = PurePosixPath(path).stem.split('.')[0]
        if not is_test(path) and len(stem) > 2 and stem not in stems:
            stems.append(stem)
    print('\nExisting tests that mention changed modules:')
    found = False
    for stem in stems[:MAX_STEMS]:
        hits = git('grep', '-l', '-w', '-F', stem, '--', *TEST_PATHSPECS, check=False).splitlines()
        hits = [h for h in hits if h not in tests]
        if hits:
            found = True
            print(f'  {stem}: ' + ', '.join(hits[:8]) + (' ...' if len(hits) > 8 else ''))
    if not found:
        print('  none found')
    if len(stems) > MAX_STEMS:
        print(f'  (searched the first {MAX_STEMS} of {len(stems)} modules)')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
