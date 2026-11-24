"""Check independently installable skill folders and their local references."""

from pathlib import Path
import re

import yaml

ROOT = Path(__file__).resolve().parents[1]


def validate(root=ROOT):
    errors, names = [], []
    for entry in sorted((root / 'skills').glob('*/SKILL.md')):
        folder = entry.parent.resolve()
        text = entry.read_text(encoding='utf-8')
        match = re.match(r'\A---\s*\n(.*?)\n---(?:\s*\n|$)', text, re.S)
        try:
            meta = yaml.safe_load(match[1]) if match else None
            if not isinstance(meta, dict):
                raise ValueError('missing frontmatter mapping')
            name = meta.get('name')
            if not isinstance(name, str) or not re.fullmatch(r'kp-[a-z0-9-]{1,60}', name) or name != entry.parent.name:
                raise ValueError('name must match its kp- folder')
            if not isinstance(meta.get('description'), str) or not meta['description'].strip():
                raise ValueError('missing description')
            if name in names:
                raise ValueError('duplicate name')
            names.append(name)
        except (ValueError, yaml.YAMLError) as exc:
            errors.append(f'{entry}: {exc}')
        for document in sorted(entry.parent.rglob('*.md')):
            for target in re.findall(r'\]\(([^)]+)\)', document.read_text(encoding='utf-8')):
                if re.match(r'[a-z]+://|#', target):
                    continue
                resolved = (document.parent / target.split('#')[0]).resolve()
                if not resolved.is_relative_to(folder):
                    errors.append(f'{document}: reference leaves independently installable folder: {target}')
                elif not resolved.is_file():
                    errors.append(f'{document}: missing reference: {target}')
    if not names:
        errors.append('No discoverable skills')
    return errors, names


if __name__ == '__main__':
    errors, names = validate()
    for error in errors:
        print(error)
    print(f'{len(names)} installable skills; {len(errors)} structural errors.')
    raise SystemExit(bool(errors))
