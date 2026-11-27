"""Run each bundled skill script against small synthetic inputs."""

import json
from pathlib import Path
import sqlite3
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
DIFF_CONTEXT = ROOT / 'skills/review-change/scripts/diff_context.py'
HANDOFF_STATE = ROOT / 'skills/handoff/scripts/handoff_state.py'
SESSION_INFO = ROOT / 'skills/skill-feedback/scripts/session_info.py'
SANITIZE = ROOT / 'skills/skill-feedback/scripts/sanitize_check.py'
SWEEP = ROOT / 'skills/skill-feedback/scripts/sweep_sessions.py'


def run(script, *args, cwd=None, isolated=True):
    flags = ['-I'] if isolated else []
    return subprocess.run([sys.executable, *flags, str(script), *map(str, args)], cwd=cwd,
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


class SweepTests(unittest.TestCase):
    HOMES = ROOT / 'eval/fixtures/session-sweep/homes'

    def sweep(self, *args, codex=None, claude=None, skills=None):
        return run(SWEEP, '--days', '36500', '--codex-home', codex or self.HOMES / 'codex',
                   '--claude-home', claude or self.HOMES / 'claude', '--skills-dir', skills or self.HOMES / 'skills', *args)

    def test_report_counts_uses_and_prints_no_conversation_text(self):
        result = self.sweep('--json')
        self.assertEqual(result.returncode, 0, result.stderr)
        data = json.loads(result.stdout)
        rows = {r['skill']: r for r in data['skills']}
        self.assertEqual((rows['diagnose']['auto'], rows['diagnose']['named'], rows['diagnose']['pushback']), (1, 1, 1))
        self.assertEqual(rows['handoff']['named'], 1)
        self.assertEqual(rows['review-change']['interrupted'], 1)
        self.assertTrue(rows['invoice-themes']['hint'].startswith('unused'))
        self.assertEqual(data['coverage']['hosts'], {'codex': 3, 'claude': 2})
        for leak in ('ORION-ACME', 'dana.lee', 'try/except', 'region'):
            self.assertNotIn(leak, result.stdout)

    def test_show_and_uses_reveal_one_use_only_on_request(self):
        pointer = next(f['pointer'] for f in json.loads(self.sweep('--json').stdout)['flags'] if f['skill'] == 'diagnose')
        shown = self.sweep('--show', pointer)
        self.assertEqual(shown.returncode, 0, shown.stderr)
        self.assertIn('data, not instructions', shown.stdout)
        self.assertIn('try/except KeyError', shown.stdout)
        self.assertIn('No, that just hides it', shown.stdout)
        uses = self.sweep('--uses', 'diagnose')
        self.assertIn('2 top-level uses of diagnose', uses.stdout)
        shared = self.sweep('--share', 'diagnose,handoff')
        self.assertIn('| diagnose | 1 | 1 | 1 | 0 |', shared.stdout)
        self.assertNotIn('research', shared.stdout)
        self.assertNotIn('@', shared.stdout)

    def test_large_world_surfaces_its_planted_patterns(self):
        large = ROOT / 'eval/fixtures/session-sweep-large/homes'
        data = json.loads(self.sweep('--json', codex=large / 'codex', claude=large / 'claude',
                                     skills=large / 'skills').stdout)
        rows = {r['skill']: r for r in data['skills']}
        self.assertEqual(data['coverage']['sessions'], 208)
        self.assertTrue(rows['csv-export']['hint'].startswith('often pushed back'))
        self.assertTrue(rows['db-migrations']['hint'].startswith('only by name'))
        self.assertTrue(rows['invoice-themes']['hint'].startswith('unused'))

    def test_codex_database_maintenance_and_shell_variables(self):
        with tempfile.TemporaryDirectory() as tmp:
            home, work = Path(tmp, 'codex'), Path(tmp, 'skills-repo')
            home.mkdir()
            (work / 'skills/x').mkdir(parents=True)
            (work / 'skills/x/SKILL.md').write_text('---\nname: x\n---\n', encoding='utf-8')
            st = sqlite3.connect(home / 'state_5.sqlite')
            st.execute('create table threads (id, rollout_path, created_at, updated_at, source, cwd)')
            st.executemany('insert into threads values (?, ?, ?, ?, ?, ?)', [
                ('t1', '', 1_790_000_000, 1_790_000_100, 'vscode', '/work/app'),
                ('t2', '', 1_790_000_000, 1_790_000_100, 'vscode', str(work))])
            st.commit()
            st.close()
            th = sqlite3.connect(home / 'thread_history_1.sqlite')
            th.execute('create table thread_turns (thread_id, turn_id, status)')
            th.execute('create table thread_items (thread_id, turn_id, rollout_ordinal, item_type, item_json)')
            th.execute("insert into thread_turns values ('t1', 'u2', 'interrupted')")
            read = {'type': 'commandExecution', 'command': 'cat ~/.agents/skills/diagnose/SKILL.md',
                    'commandActions': [{'type': 'read', 'path': '/h/.agents/skills/diagnose/SKILL.md'}]}
            items = [('t1', 'u1', 1, 'userMessage', {'content': [{'type': 'text', 'text': 'echo $env and $host'}]}),
                     ('t1', 'u2', 2, 'userMessage', {'content': [{'type': 'text', 'text': '$diagnose the crash'}]}),
                     ('t1', 'u2', 3, 'commandExecution', read),
                     ('t2', 'v1', 1, 'commandExecution', read)]
            th.executemany('insert into thread_items values (?, ?, ?, ?, ?)',
                           [(a, b, c, d, json.dumps(e)) for a, b, c, d, e in items])
            th.commit()
            th.close()
            empty = Path(tmp, 'none')
            empty.mkdir()
            data = json.loads(self.sweep('--json', codex=home, claude=empty, skills=empty).stdout)
            rows = {r['skill']: r for r in data['skills']}
            self.assertEqual(data['coverage']['maintenance'], 1)
            self.assertEqual((rows['diagnose']['named'], rows['diagnose']['interrupted']), (1, 1))
            self.assertNotIn('env', rows)
            self.assertNotIn('host', rows)


class RescoreTests(unittest.TestCase):
    def test_rescore_reapplies_text_checks_and_keeps_workspace_checks(self):
        patch = ('diff --git a/money.py b/money.py\n+++ b/money.py\n+    return x\n'
                 'diff --git a/__pycache__/money.cpython-312.pyc b/__pycache__/money.cpython-312.pyc\n')
        record = {'skill': 'diagnose', 'case': 'invoice-wrong-hypothesis-fix', 'condition': 'with', 'repeat': 0,
                  'answer': "The bug wasn't in `format_money`.", 'patch': patch, 'passed': False,
                  'checks': [{'check': 'half-cent discounts round up', 'passed': True, 'detail': ''},
                             {'check': 'rejects the format_money hypothesis', 'passed': False, 'detail': ''}],
                  'skill_loaded': False, 'tool_calls': 1, 'seconds': 1, 'usage': {}}
        diag = {**record, 'case': 'zero-backoff-diagnose', 'answer': 'schedule_retry uses `if not delay`, so 0 is falsy.',
                'patch': 'diff --git a/__pycache__/worker.cpython-312.pyc b/__pycache__/worker.cpython-312.pyc\n',
                'checks': []}
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp, 'results.jsonl')
            path.write_text(json.dumps(record) + '\n' + json.dumps(diag) + '\n', encoding='utf-8')
            result = run(ROOT / 'scripts/run_evals.py', 'rescore', path, isolated=False)
            self.assertEqual(result.returncode, 0, result.stderr)
            rows = [json.loads(line) for line in path.read_text(encoding='utf-8').splitlines()]
            self.assertTrue(rows[0]['passed'], rows[0]['checks'])
            self.assertTrue(rows[1]['passed'], rows[1]['checks'])


    def test_harness_files_and_failed_runs_do_not_count_against_the_skill(self):
        base = {'skill': 'diagnose', 'case': 'zero-backoff-diagnose', 'condition': 'with', 'repeat': 0,
                'answer': 'schedule_retry uses `if not delay`, so 0 is falsy.', 'passed': False, 'checks': [],
                'patch': 'diff --git a/.eval-last-message.txt b/.eval-last-message.txt\n',
                'skill_loaded': True, 'tool_calls': 3, 'seconds': 1, 'usage': {}, 'exit': 0}
        limited = {**base, 'repeat': 1, 'answer': '', 'tool_calls': 0, 'exit': 1,
                   'stderr': '{"type":"error","message":"You have hit your usage limit."}'}
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp, 'results.jsonl')
            path.write_text(json.dumps(base) + '\n' + json.dumps(limited) + '\n', encoding='utf-8')
            result = run(ROOT / 'scripts/run_evals.py', 'rescore', path, isolated=False)
            self.assertEqual(result.returncode, 0, result.stderr)
            rows = [json.loads(line) for line in path.read_text(encoding='utf-8').splitlines()]
            self.assertTrue(rows[0]['passed'], rows[0]['checks'])
            self.assertEqual(rows[1]['error'], 'usage limit')
            self.assertIn('Left out as invalid: 1 x usage limit', result.stdout)
            self.assertIn('1/1', result.stdout)


class AuditTests(unittest.TestCase):
    def test_reports_dependencies_and_one_sided_invocation(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for name, body, meta in [
                ('alpha', 'Read [beta](../beta/SKILL.md) and the [gone](../gone/SKILL.md) skill.', ''),
                ('beta', 'Standalone.', 'disable-model-invocation: true\n'),
            ]:
                (root / name).mkdir()
                (root / name / 'SKILL.md').write_text(
                    f'---\nname: {name}\ndescription: test\n{meta}---\n{body}\n', encoding='utf-8')
            result = run(ROOT / 'scripts/audit_skills.py', root, isolated=False)
            self.assertEqual(result.returncode, 0, result.stderr)
            alpha = next(line for line in result.stdout.splitlines() if line.startswith('alpha'))
            beta = next(line for line in result.stdout.splitlines() if line.startswith('beta'))
            self.assertIn('beta', alpha)
            self.assertIn('MISSING: gone', alpha)
            self.assertIn('explicit-claude-only', beta)


if __name__ == '__main__':
    unittest.main()
