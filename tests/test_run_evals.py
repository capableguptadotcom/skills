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
    def test_recorded_denial(self):
        self.assertIn('command denied', run_evals.blocked({'permission_denials': ['Bash: "for i in 1 2"'], 'answer': ''}))

    def test_answer_that_waits_for_approval(self):
        answer = 'I need your approval to run the loop script. Once you approve it, I will continue.'
        self.assertTrue(run_evals.blocked({'answer': answer}))

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
                                     'both_orders': True, 'model': 'opus', 'redo_errors': False})()
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


if __name__ == '__main__':
    unittest.main()
