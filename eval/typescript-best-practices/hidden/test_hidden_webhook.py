import subprocess
import unittest


class Hidden(unittest.TestCase):
    def test_behavior(self):
        run = subprocess.run(['node', '--experimental-strip-types', '--test', 'hidden_webhook.test.ts'],
                             capture_output=True, text=True, encoding='utf-8', errors='replace')
        failed = [line for line in run.stdout.splitlines() if line.startswith('not ok')]
        self.assertEqual(run.returncode, 0, '; '.join(failed) or run.stdout[-600:])


if __name__ == '__main__':
    unittest.main()
