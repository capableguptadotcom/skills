"""Check that every skill folder is valid, self-contained and safe to install."""

from pathlib import Path
import re

import yaml

ROOT = Path(__file__).resolve().parents[1]

NAME = re.compile(r'[a-z0-9]+(?:-[a-z0-9]+)*')
RESERVED = {'review', 'simplify', 'debug', 'start', 'shape', 'plan', 'init', 'loop', 'security-review'}
ALLOWED_KEYS = {'name', 'description', 'disable-model-invocation', 'license', 'compatibility', 'metadata'}
MAX_DESCRIPTION = 400
MAX_LINES = 500
FORBIDDEN_FILES = {'.mcp.json', 'package.json', 'pyproject.toml', 'setup.py', 'requirements.txt'}
NETWORK_IMPORT = re.compile(r'^\s*(?:import|from)\s+(?:socket|urllib|http|requests|httpx|aiohttp|ftplib|smtplib)\b', re.M)
PERSONAL_PATH = re.compile(r'[A-Za-z]:\\Users\\[A-Za-z]|/Users/[A-Za-z]|/home/[a-z]')
LINK = re.compile(r'\]\(([^)]+)\)')


def frontmatter(text):
    match = re.match(r'\A---\s*\n(.*?)\n---(?:\s*\n|$)', text, re.S)
    meta = yaml.safe_load(match[1]) if match else None
    if not isinstance(meta, dict):
        raise ValueError('missing frontmatter mapping')
    return meta


def check_metadata(folder, meta):
    errors = []
    name = meta.get('name')
    if not isinstance(name, str) or not NAME.fullmatch(name) or len(name) > 64:
        errors.append('name must be lowercase letters, digits and single hyphens, at most 64 characters')
    elif name != folder.name:
        errors.append(f'name {name!r} must match its folder {folder.name!r}')
    elif name in RESERVED:
        errors.append(f'name {name!r} collides with a host built-in or a common third-party skill')
    description = meta.get('description')
    if not isinstance(description, str) or not description.strip():
        errors.append('missing description')
    elif len(description) > MAX_DESCRIPTION:
        errors.append(f'description is {len(description)} characters; keep it under {MAX_DESCRIPTION}')
    unknown = set(meta) - ALLOWED_KEYS
    if unknown:
        errors.append(f'unsupported frontmatter keys: {", ".join(sorted(unknown))}')
    explicit = meta.get('disable-model-invocation', False)
    if not isinstance(explicit, bool):
        errors.append('disable-model-invocation must be true or false')
        return errors
    errors += check_invocation(folder, explicit)
    return errors


def check_invocation(folder, explicit):
    config = folder / 'agents' / 'openai.yaml'
    implicit = None
    if config.is_file():
        data = yaml.safe_load(config.read_text(encoding='utf-8')) or {}
        policy = data.get('policy') if isinstance(data, dict) else None
        if isinstance(policy, dict) and 'allow_implicit_invocation' in policy:
            implicit = policy['allow_implicit_invocation']
            if not isinstance(implicit, bool):
                return ['agents/openai.yaml: allow_implicit_invocation must be true or false']
    if explicit and implicit is not False:
        return ['explicit-only in Claude Code but not in Codex: set policy.allow_implicit_invocation: false in agents/openai.yaml']
    if not explicit and implicit is False:
        return ['explicit-only in Codex but not in Claude Code: set disable-model-invocation: true']
    return []


def check_files(folder):
    errors = []
    for path in sorted(p for p in folder.rglob('*') if p.is_file() and '__pycache__' not in p.parts):
        relative = path.relative_to(folder).as_posix()
        if path.name in FORBIDDEN_FILES:
            errors.append(f'{relative}: skills must not install packages or tool servers')
        if relative.startswith('scripts/') and path.suffix != '.py':
            errors.append(f'{relative}: scripts must be Python so they run the same on every OS')
        if path.suffix not in {'.md', '.py', '.yaml', '.yml', '.json', '.txt'}:
            continue
        text = path.read_text(encoding='utf-8')
        if PERSONAL_PATH.search(text):
            errors.append(f'{relative}: contains a personal path')
        if path.suffix == '.py' and NETWORK_IMPORT.search(text):
            errors.append(f'{relative}: scripts must not use the network')
        if path.suffix == '.md':
            for target in LINK.findall(text):
                if re.match(r'[a-z]+://|#|mailto:', target):
                    continue
                resolved = (path.parent / target.split('#')[0]).resolve()
                if not resolved.is_relative_to(folder):
                    errors.append(f'{relative}: reference leaves the skill folder: {target}')
                elif not resolved.is_file():
                    errors.append(f'{relative}: missing reference: {target}')
    return errors


def validate(root=ROOT):
    errors, names = [], []
    for entry in sorted((root / 'skills').glob('*/SKILL.md')):
        folder = entry.parent.resolve()
        text = entry.read_text(encoding='utf-8')
        problems = []
        try:
            meta = frontmatter(text)
            problems += check_metadata(folder, meta)
            if meta.get('name') in names:
                problems.append('duplicate name')
            names.append(meta.get('name'))
        except (ValueError, yaml.YAMLError) as exc:
            problems.append(str(exc))
        if text.count('\n') > MAX_LINES:
            problems.append(f'SKILL.md is over {MAX_LINES} lines; move detail into references/')
        problems += check_files(folder)
        errors += [f'{folder.name}: {problem}' for problem in problems]
    if not names:
        errors.append('No discoverable skills')
    return errors, [n for n in names if isinstance(n, str)]


if __name__ == '__main__':
    errors, names = validate()
    for error in errors:
        print(error)
    print(f'{len(names)} installable skills; {len(errors)} errors.')
    raise SystemExit(bool(errors))
