"""Audit installed skill folders: size, invocation, scripts, and dependencies on other skills.

Usage:
    python scripts/audit_skills.py <skills-root> [<skills-root> ...] [--only NAME ...]

Each root is a folder of skill folders (for example ~/.agents/skills or a repo's
.agents/skills). Reads files only; runs nothing from the skills.
"""

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from validate import check_files, check_metadata, frontmatter  # noqa: E402

SIBLING_LINK = re.compile(r'\]\((\.\./[^)]+)\)|`\.\./([a-z0-9-]+)/SKILL\.md`|\.\./<name>/SKILL\.md')
MENTION = re.compile(r'(?:`/?\$?|\*\*|/)([a-z][a-z0-9]*(?:-[a-z0-9]+)+)(?:`|\*\*)')


def audit(folder, known):
    entry = folder / 'SKILL.md'
    text = entry.read_text(encoding='utf-8', errors='replace')
    files = [p for p in folder.rglob('*') if p.is_file() and '__pycache__' not in p.parts]
    size = sum(p.stat().st_size for p in files)
    try:
        meta = frontmatter(text)
    except Exception:  # noqa: BLE001 - report, don't crash on third-party content
        meta = {}
    claude_explicit = meta.get('disable-model-invocation') is True
    codex_yaml = folder / 'agents' / 'openai.yaml'
    codex_explicit = codex_yaml.is_file() and re.search(
        r'allow_implicit_invocation:\s*false', codex_yaml.read_text(encoding='utf-8', errors='replace')) is not None
    siblings = set()
    for doc in [p for p in files if p.suffix == '.md']:
        body = doc.read_text(encoding='utf-8', errors='replace')
        for match in SIBLING_LINK.finditer(body):
            target = match[1] or match[2] or '<any sibling>'
            name = target.split('/')[1] if target.startswith('../') else target
            siblings.add(name)
    mentions = {m for m in MENTION.findall(text) if m in known and m != folder.name}
    problems = []
    try:
        problems = check_metadata(folder.resolve(), meta) + check_files(folder.resolve())
    except Exception as exc:  # noqa: BLE001
        problems = [str(exc)]
    return {
        'name': folder.name, 'kb': size / 1024, 'lines': text.count('\n'), 'files': len(files),
        'scripts': sum(1 for p in files if p.parent.name == 'scripts'),
        'invocation': ('explicit' if claude_explicit and codex_explicit else
                       'explicit-claude-only' if claude_explicit else
                       'explicit-codex-only' if codex_explicit else 'auto'),
        'siblings': sorted(siblings), 'missing': sorted(s for s in siblings if s not in known and s != '<any sibling>'),
        'mentions': sorted(mentions), 'problems': problems,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('roots', nargs='+')
    parser.add_argument('--only', nargs='*')
    args = parser.parse_args()
    folders = [f for root in args.roots for f in sorted(Path(root).expanduser().glob('*/'))
               if (f / 'SKILL.md').is_file()]
    known = {f.name for f in folders}
    rows = [audit(f, known) for f in folders if not args.only or f.name in args.only]
    print(f"{'skill':<34}{'KB':>7}{'lines':>7}{'scr':>5}  {'invocation':<20} depends on other skills")
    for r in rows:
        deps = ', '.join(r['siblings'] + [f'mentions {m}' for m in r['mentions'] if m not in r['siblings']])
        missing = f"  MISSING: {', '.join(r['missing'])}" if r['missing'] else ''
        print(f"{r['name']:<34}{r['kb']:>7.1f}{r['lines']:>7}{r['scripts']:>5}  {r['invocation']:<20} {deps}{missing}")
    print(f"\n{len(rows)} skills, {sum(r['kb'] for r in rows):.0f} KB. "
          f"{sum(1 for r in rows if r['siblings'] or r['mentions'])} depend on another skill; "
          f"{sum(1 for r in rows if r['missing'])} reference a skill that is not installed alongside.")


if __name__ == '__main__':
    main()
