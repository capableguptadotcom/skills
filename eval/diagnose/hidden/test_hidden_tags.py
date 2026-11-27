"""Hidden acceptance test: order must hold under every hash seed, in the shipped code."""

import os
import subprocess
import sys
import unittest

CHECK = (
    "from tags import normalize_tags, tag_line;"
    "assert normalize_tags('Python, web,python , API') == ['python', 'web', 'api'], normalize_tags('Python, web,python , API');"
    "assert normalize_tags('b,a,c,a,b') == ['b', 'a', 'c'];"
    "assert tag_line('Zed, alpha, zed') == '#zed #alpha'"
)


class HiddenTagTests(unittest.TestCase):
    def test_order_is_stable_across_hash_seeds(self):
        for seed in range(12):
            env = dict(os.environ, PYTHONHASHSEED=str(seed))
            run = subprocess.run([sys.executable, "-c", CHECK], env=env, capture_output=True, text=True)
            self.assertEqual(run.returncode, 0, f"seed {seed}: {run.stderr.strip()[-200:]}")


if __name__ == "__main__":
    unittest.main()
