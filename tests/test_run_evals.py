import json
import os
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
os.environ.setdefault('EVAL_WORK_ROOT', tempfile.mkdtemp(prefix='skill-evals-test-'))

import run_evals  # noqa: E402


def case_files():
    return sorted((ROOT / 'eval').glob('*/cases.json'))


class CaseFilesTest(unittest.TestCase):
    def test_cases_point_at_real_files(self):
        for path in case_files():
            spec = json.loads(path.read_text(encoding='utf-8'))
            for case in spec['cases']:
                with self.subTest(case=case['id']):
                    self.assertTrue((ROOT / case['fixture']).is_dir())
                    if case.get('change'):
                        self.assertTrue((ROOT / case['change']['path']).is_dir())
                    for check in case.get('checks', []):
                        for name in check.get('files', []):
                            self.assertTrue((path.parent / 'hidden' / name).is_file(), name)

    def test_case_ids_are_unique(self):
        for path in case_files():
            ids = [c['id'] for c in json.loads(path.read_text(encoding='utf-8'))['cases']]
            self.assertEqual(len(ids), len(set(ids)), path)


class ChangeOverlayTest(unittest.TestCase):
    def setUp(self):
        self.dirs = []

    def tearDown(self):
        for d in self.dirs:
            shutil.rmtree(d, ignore_errors=True)

    def prepared(self, case):
        workdir = run_evals.prepare(case, 'review-change', 'claude', 'without')
        self.dirs.append(workdir)
        return workdir

    def test_branch_change_is_committed_on_top_of_main(self):
        workdir = self.prepared({'fixture': 'eval/fixtures/catalog-api',
                                 'change': {'path': 'eval/fixtures/catalog-changes/pagination', 'branch': 'feature'}})
        self.assertEqual(run_evals.git(workdir, 'branch', '--show-current').strip(), 'feature')
        self.assertIn('catalog.py', run_evals.git(workdir, 'diff', '--name-only', 'main...HEAD'))
        self.assertEqual(run_evals.full_patch(workdir), '')

    def test_uncommitted_change_is_not_the_agents_patch(self):
        workdir = self.prepared({'fixture': 'eval/fixtures/order-utils',
                                 'change': {'path': 'eval/fixtures/order-utils-changes/shipping'}})
        self.assertIn('shipping.py', run_evals.git(workdir, 'status', '--porcelain'))
        self.assertEqual(run_evals.full_patch(workdir), '')
        target = workdir / 'shipping.py'
        target.write_text(target.read_text(encoding='utf-8').replace('import os\n', ''), encoding='utf-8')
        patch = run_evals.full_patch(workdir)
        self.assertIn('-import os', patch)
        self.assertEqual(run_evals.touched_paths(patch, ['shipping.py', 'discounts.py']), ['shipping.py'])

    def test_paths_unchanged_check(self):
        case = {'checks': [{'type': 'paths_unchanged', 'paths': ['discounts.py']}]}
        patch = 'diff --git a/discounts.py b/discounts.py\n'
        result = run_evals.check(case, Path('.'), '', 'simplify-code', patch)
        self.assertFalse(result[0]['passed'])
        self.assertTrue(run_evals.check(case, Path('.'), '', 'simplify-code', '')[0]['passed'])


class RunErrorTest(unittest.TestCase):
    def test_answer_about_rate_limits_is_a_valid_run(self):
        answer = 'Which SMS provider is it, and who owns the cost and rate limits? ' + 'Detail. ' * 60
        self.assertEqual(run_evals.run_error({'exit': 0, 'answer': answer, 'condition': 'named'}), '')

    def test_short_limit_message_is_invalid(self):
        record = {'exit': 0, 'answer': "You've hit your usage limit.", 'condition': 'named'}
        self.assertEqual(run_evals.run_error(record), 'usage limit')

    def test_failed_run_with_limit_in_stderr_is_invalid(self):
        record = {'exit': 1, 'answer': '', 'stderr': 'API Error: rate limit exceeded', 'condition': 'with'}
        self.assertEqual(run_evals.run_error(record), 'rate limit')


class BlockedTest(unittest.TestCase):
    def test_refused_command_the_agent_worked_around(self):
        record = {'permission_denials': ['Bash: "for i in 1 2"'], 'answer': 'I ran each seed; all pass.'}
        self.assertEqual(run_evals.blocked(record), '')
        self.assertIn('for i in 1 2', run_evals.denied(record))

    def test_answer_that_waits_for_approval(self):
        answer = 'I need your approval to run the loop script. Once you approve it, I will continue.'
        self.assertTrue(run_evals.blocked({'answer': answer}))

    def test_conversation_reads_only_agent_turns(self):
        turns = [('user', 'grill me'), ('agent', 'Which provider?'),
                 ('user', 'Once you approve the plan, send it.'), ('agent', 'Plan: use Twilio.')]
        record = {'answer': run_evals.transcript_text(turns), 'turns': 2}
        self.assertEqual(run_evals.agent_text(record), 'Which provider?\n\nPlan: use Twilio.')
        self.assertEqual(run_evals.blocked(record), '')

    def test_ordinary_answer(self):
        self.assertEqual(run_evals.blocked({'answer': 'I ran the tests; all 5 pass.'}), '')

    def test_tally_with_and_without_blocked(self):
        rows = [{'case': 'c', 'sides': ['a:named', 'b:named'], 'winner': 'a:named', 'blocked': ['', '']},
                {'case': 'c', 'sides': ['a:named', 'b:named'], 'winner': 'a:named', 'blocked': ['', 'answer says: x']}]
        with tempfile.TemporaryDirectory() as d:
            path = Path(d) / 'v.jsonl'
            path.write_text(''.join(json.dumps(r) + '\n' for r in rows), encoding='utf-8')
            from io import StringIO
            from contextlib import redirect_stdout
            buffer = StringIO()
            with redirect_stdout(buffer):
                run_evals.retally(path)
        text = buffer.getvalue()
        self.assertIn('wins or ties 2/2', text)
        self.assertIn('wins or ties 1/1', text)


class RemoveWorkdirTest(unittest.TestCase):
    def test_removes_read_only_files_and_the_project_folder(self):
        workdir = run_evals.new_workdir('cleanup')
        run_evals.git(workdir, 'init', '-q')
        (workdir / 'a.txt').write_text('x', encoding='utf-8')
        run_evals.git(workdir, '-c', 'user.email=e@example.com', '-c', 'user.name=e', 'add', '.')
        run_evals.git(workdir, '-c', 'user.email=e@example.com', '-c', 'user.name=e', 'commit', '-qm', 'x')
        home = Path(tempfile.mkdtemp(prefix='home-'))
        original = run_evals.HOME
        run_evals.HOME = home
        try:
            folder = home / '.claude/projects' / run_evals.re.sub(r'[^A-Za-z0-9]', '-', str(workdir))
            (folder / 'session/subagents').mkdir(parents=True)
            (folder / 'session/subagents/agent.jsonl').write_text('{}', encoding='utf-8')
            run_evals.remove_workdir(workdir)
            self.assertFalse(workdir.exists())
            self.assertFalse(folder.exists())
        finally:
            run_evals.HOME = original
            shutil.rmtree(home, ignore_errors=True)


class RedactTest(unittest.TestCase):
    def test_paths_inside_lists_are_redacted(self):
        home = str(run_evals.HOME)
        record = {'answer': f'see {home}', 'permission_denials': [f'Bash: python {home}\\x.py'],
                  'checks': [{'detail': home.replace('\\', '/')}], 'exit': 0}
        text = json.dumps(run_evals.redact_record(record))
        self.assertNotIn(home.replace('\\', '/'), text)
        self.assertNotIn(json.dumps(home)[1:-1], text)
        self.assertEqual(run_evals.redact_record(record)['exit'], 0)


class WilsonTest(unittest.TestCase):
    def test_interval(self):
        low, high = run_evals.wilson(8, 12)
        self.assertAlmostEqual(low, 0.39, places=2)
        self.assertAlmostEqual(high, 0.86, places=2)
        self.assertEqual(run_evals.wilson(0, 0), (0.0, 0.0))
        self.assertEqual(run_evals.wilson(9, 9)[1], 1.0)


class JudgeTieTest(unittest.TestCase):
    def test_explicit_tie_is_a_tie_not_an_error(self):
        results = []
        with tempfile.TemporaryDirectory() as d:
            for name, condition in (('a.jsonl', 'named'), ('b.jsonl', 'named')):
                row = {'skill': 'diagnose', 'variant': name[0], 'case': 'zero-backoff-diagnose', 'repeat': 0,
                       'condition': condition, 'answer': 'x' * 500, 'exit': 0, 'checks': []}
                (Path(d) / name).write_text(json.dumps(row) + '\n', encoding='utf-8')
            args = type('Args', (), {'path': str(Path(d) / 'a.jsonl'), 'against': str(Path(d) / 'b.jsonl'),
                                     'pair': ['named', 'named'], 'seed': 7, 'out': str(Path(d) / 'v.jsonl'),
                                     'both_orders': True, 'model': 'opus', 'redo_errors': False,
                                     'outcome_only': False})()
            original = run_evals.ask_judge
            run_evals.ask_judge = lambda *a, **k: {'winner': 'tie', 'reason': 'same'}
            try:
                from contextlib import redirect_stdout
                from io import StringIO
                with redirect_stdout(StringIO()):
                    run_evals.judge(args)
            finally:
                run_evals.ask_judge = original
            results = [json.loads(l) for l in (Path(d) / 'v.jsonl').read_text(encoding='utf-8').splitlines()]
        self.assertEqual([r['winner'] for r in results], ['tie'])


class JudgePromptTest(unittest.TestCase):
    def test_hidden_results_show_only_hidden_tests(self):
        case = {'checks': [{'type': 'hidden_test', 'name': 'behavior kept'},
                           {'type': 'answer_matches', 'name': 'names the cause'}]}
        row = {'checks': [{'check': 'behavior kept', 'passed': False}, {'check': 'names the cause', 'passed': True}]}
        self.assertEqual(run_evals.hidden_results(case, row), 'behavior kept: FAILED')
        self.assertEqual(run_evals.hidden_results({'checks': []}, row), '(none for this task)')


class ConversationTest(unittest.TestCase):
    def test_session_flags(self):
        first = run_evals.command('claude', 'hi', Path('.'), session=('abc', False))
        later = run_evals.command('claude', 'hi', Path('.'), session=('abc', True))
        plain = run_evals.command('claude', 'hi', Path('.'))
        self.assertIn('--session-id', first)
        self.assertIn('--resume', later)
        self.assertNotIn('--no-session-persistence', first + later)
        self.assertIn('--no-session-persistence', plain)

    def test_conversation_turns_and_agent_only_text(self):
        calls, forgotten = [], []

        def fake_run(cmd, **kwargs):
            calls.append(cmd)
            result = {'type': 'result', 'result': f'agent turn {len(calls)}', 'total_cost_usd': 0.1}
            return type('Proc', (), {'returncode': 0, 'stdout': json.dumps(result), 'stderr': ''})()

        case = {'prompt': 'grill me', 'simulated_user': {'facts': 'x', 'replies': 2, 'final': 'sum up'}}
        args = type('Args', (), {'host': 'claude', 'model': 'sonnet', 'timeout': 10})()
        originals = run_evals.subprocess.run, run_evals.simulate_user, run_evals.forget_session
        run_evals.subprocess.run = fake_run
        run_evals.simulate_user = lambda case, transcript: ('we have no phone numbers', 0.01)
        run_evals.forget_session = forgotten.append
        try:
            _, parsed = run_evals.converse(args, case, '/shape-change grill me', Path('.'), 'shape-change')
        finally:
            run_evals.subprocess.run, run_evals.simulate_user, run_evals.forget_session = originals
        self.assertEqual(parsed['turns'], 4)  # first turn, two simulated replies, the final request
        self.assertEqual(calls[-1][2], 'sum up')
        self.assertIn('[user]\nwe have no phone numbers', parsed['answer'])
        self.assertNotIn('phone', parsed['agent_text'])
        self.assertEqual(parsed['final_answer'], 'agent turn 4')
        self.assertEqual(len(forgotten), 1)
        self.assertAlmostEqual(parsed['cost_usd'], 0.42)

    def test_conversation_cases_have_facts(self):
        for path in case_files():
            for case in json.loads(path.read_text(encoding='utf-8'))['cases']:
                if case.get('simulated_user'):
                    with self.subTest(case=case['id']):
                        self.assertTrue(case['simulated_user']['facts'])
                        self.assertIn('Judge the whole conversation', case['judge_truth'])


if __name__ == '__main__':
    unittest.main()
