"""Scan a draft report for details that must not leave the project.

Usage:
    python sanitize_check.py <draft> [--project ROOT] [--deny TERM ...]

Flags absolute paths, email addresses, likely secrets, and any denied term.
With --project, the repository's name, folder name and Git author email are
denied too. Exits 1 when anything is found. Read-only; no network.
"""

import argparse
import re
import subprocess
import sys
from pathlib import Path

PATTERNS = {
    'absolute path': re.compile(r'(?<![\w/])(?:[A-Za-z]:\\[^\s`]+|/(?:Users|home|root|var|opt|srv)/[^\s`]+|~/[^\s`]+)'),
    'email address': re.compile(r'\b[\w.+-]+@[\w-]+(?:\.[\w-]+)+\b'),
    'secret': re.compile(r'(?:sk-[A-Za-z0-9_-]{16,}|gh[pousr]_[A-Za-z0-9]{20,}|github_pat_\w{20,}|AKIA[0-9A-Z]{16}'
                         r'|xox[abpr]-[A-Za-z0-9-]{10,}|-----BEGIN [A-Z ]*PRIVATE KEY-----'
                         r'|(?i:(?:api[_-]?key|secret|token|password)\s*[:=]\s*["\']?[^\s"\']{8,}))'),
}
ALLOWED_EMAIL = re.compile(r'noreply|example\.(?:com|org)$', re.I)


def git(root, *args):
    result = subprocess.run(['git', '-C', str(root), *args], capture_output=True, text=True,
                            encoding='utf-8', errors='replace')
    return result.stdout.strip() if result.returncode == 0 else ''


def project_terms(root):
    root = Path(root).resolve()
    terms = {root.name}
    remote = git(root, 'remote', 'get-url', 'origin')
    if remote:
        terms.add(re.sub(r'\.git$', '', remote.rstrip('/').split('/')[-1].split(':')[-1]))
        owner = re.search(r'[:/]([^/:]+)/[^/]+$', remote)
        if owner:
            terms.add(owner[1])
    email = git(root, 'config', 'user.email')
    if email:
        terms.add(email)
    return {t for t in terms if len(t) > 2}


def scan(text, deny):
    findings = []
    for number, line in enumerate(text.splitlines(), 1):
        for label, pattern in PATTERNS.items():
            for match in pattern.finditer(line):
                if label == 'email address' and ALLOWED_EMAIL.search(match[0]):
                    continue
                findings.append((number, label, match[0]))
        for term in deny:
            if re.search(re.escape(term), line, re.I):
                findings.append((number, 'denied term', term))
    return findings


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('draft')
    parser.add_argument('--project')
    parser.add_argument('--deny', action='append', default=[])
    args = parser.parse_args(argv)
    deny = set(args.deny) | (project_terms(args.project) if args.project else set())
    findings = scan(Path(args.draft).read_text(encoding='utf-8'), sorted(deny))
    for number, label, value in findings:
        print(f'line {number}: {label}: {value}')
    print(f'{len(findings)} finding(s); checked {len(deny)} denied term(s).')
    return 1 if findings else 0


if __name__ == '__main__':
    sys.exit(main())
