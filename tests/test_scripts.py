"""Run each bundled skill script against small synthetic inputs."""

import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
DIFF_CONTEXT = ROOT / 'skills/review-change/scripts/diff_context.py'
HANDOFF_STATE = ROOT / 'skills/handoff/scripts/handoff_state.py'
SESSION_INFO = ROOT / 'skills/skill-feedback/scripts/session_info.py'
SANITIZE = ROOT / 'skills/skill-feedback/scripts/sanitize_check.py'


def run(script, *args, cwd=None):
    return subprocess.run([sys.executable, '-I', str(script), *map(str, args)], cwd=cwd,
                          capture_output=True, text=True, encoding='utf-8')


def git(cwd, *args):
    subprocess.run(['git', *args], cwd=cwd, check=True, capture_output=True)


class GitRepoTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.repo = Path(self.tmp.name)
        git(self.repo, 'init', '-q', '-b', 'main')
        git(self.repo, 'config', 'user.email', 'test@example.com')
        git(self.repo, 'config', 'user.name', 'Test')
        (self.repo / 'cart.py').write_text('def total(items):\n    return 0\n', encoding='utf-8')
        (self.repo / 'tests').mkdir()
        (self.repo / 'tests/test_totals.py').write_text('from cart import total\n', encoding='utf-8')
        git(self.repo, 'add', '.')
        git(self.repo, 'commit', '-q', '-m', 'base')
        git(self.repo, 'switch', '-q', '-c', 'feature')
        (self.repo / 'cart.py').write_text('def total(items):\n    return sum(items)\n', encoding='utf-8')
        git(self.repo, 'commit', '-q', '-am', 'change')
        (self.repo / 'notes.txt').write_text('draft\n', encoding='utf-8')

    def tearDown(self):
        self.tmp.cleanup()

    def test_diff_context_finds_changes_and_related_tests(self):
        result = run(DIFF_CONTEXT, 'main', cwd=self.repo)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('cart.py', result.stdout)
        self.assertIn('untracked     notes.txt', result.stdout)
        self.assertIn('cart: tests/test_totals.py', result.stdout)

    def test_diff_context_defaults_to_merge_base(self):
        result = run(DIFF_CONTEXT, cwd=self.repo)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('merge-base with main', result.stdout)

    def test_handoff_state_reports_branch_and_files(self):
        result = run(HANDOFF_STATE, cwd=self.repo)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('Branch: feature', result.stdout)
        self.assertIn('not pushed', result.stdout)
        self.assertIn('notes.txt', result.stdout)

    def test_scripts_refuse_outside_git(self):
        with tempfile.TemporaryDirectory() as empty:
            self.assertEqual(run(DIFF_CONTEXT, cwd=empty).returncode, 2)
            self.assertEqual(run(HANDOFF_STATE, cwd=empty).returncode, 2)


class SessionInfoTests(unittest.TestCase):
    def write(self, lines):
        handle = tempfile.NamedTemporaryFile('w', suffix='.jsonl', delete=False, encoding='utf-8')
        handle.write('\n'.join(json.dumps(line) for line in lines))
        handle.close()
        self.addCleanup(Path(handle.name).unlink)
        return handle.name

    def test_codex_session(self):
        path = self.write([
            {'type': 'session_meta', 'timestamp': 't1', 'payload': {'cli_version': '0.1'}},
            {'type': 'turn_context', 'payload': {'model': 'model-a'}},
            {'type': 'event_msg', 'payload': {'type': 'task_started'}},
            {'type': 'response_item', 'payload': {'type': 'function_call',
             'arguments': 'cat C:\\x\\.agents\\skills\\diagnose\\SKILL.md'}},
            {'type': 'response_item', 'payload': {'type': 'message', 'role': 'user',
             'content': 'SECRET PROMPT TEXT'}},
        ])
        result = run(SESSION_INFO, path)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('Host: Codex 0.1', result.stdout)
        self.assertIn('model-a', result.stdout)
        self.assertIn('User turns: 1', result.stdout)
        self.assertIn('diagnose: 1', result.stdout)
        self.assertNotIn('SECRET', result.stdout)

    def test_claude_session(self):
        path = self.write([
            {'type': 'user', 'sessionId': 's', 'version': '2.0', 'message': {'role': 'user', 'content': 'SECRET'}},
            {'type': 'assistant', 'sessionId': 's', 'message': {'model': 'model-b', 'content': [
                {'type': 'tool_use', 'name': 'Skill', 'input': {'skill': 'review-change'}}]}},
        ])
        result = run(SESSION_INFO, path)
        self.assertIn('Host: Claude Code 2.0', result.stdout)
        self.assertIn('model-b', result.stdout)
        self.assertIn('review-change: 1', result.stdout)
        self.assertNotIn('SECRET', result.stdout)

    def test_lock_lookup(self):
        with tempfile.TemporaryDirectory() as tmp:
            Path(tmp, 'skills-lock.json').write_text(json.dumps({'skills': {
                'diagnose': {'source': 'owner/skills', 'computedHash': 'abcdef1234567890'}}}), encoding='utf-8')
            found = run(SESSION_INFO, '--lock', tmp, '--skill', 'diagnose')
            self.assertEqual(found.returncode, 0)
            self.assertIn('source=owner/skills', found.stdout)
            self.assertEqual(run(SESSION_INFO, '--lock', tmp, '--skill', 'missing').returncode, 1)


class SanitizeTests(unittest.TestCase):
    def check(self, text, *args):
        with tempfile.TemporaryDirectory() as tmp:
            draft = Path(tmp, 'draft.md')
            draft.write_text(text, encoding='utf-8')
            return run(SANITIZE, draft, *args)

    def test_clean_draft_passes(self):
        result = self.check('A list component overflows with a long name.\nnoreply@github.com\n')
        self.assertEqual(result.returncode, 0, result.stdout)

    def test_each_leak_is_flagged(self):
        cases = {
            'absolute path': 'See C:\\Work\\app\\main.py',
            'email address': 'Ask person@company.io',
            'secret': 'token: ghp_' + 'a' * 30,
            'denied term': 'In the acme-billing repo',
        }
        for label, text in cases.items():
            with self.subTest(label=label):
                result = self.check(text + '\n', '--deny', 'acme-billing')
                self.assertEqual(result.returncode, 1)
                self.assertIn(label, result.stdout)

    def test_project_name_is_denied(self):
        with tempfile.TemporaryDirectory() as tmp:
            project = Path(tmp, 'secret-product')
            project.mkdir()
            result = self.check('Seen in secret-product today.\n', '--project', project)
            self.assertEqual(result.returncode, 1)
            self.assertIn('denied term: secret-product', result.stdout)


if __name__ == '__main__':
    unittest.main()
