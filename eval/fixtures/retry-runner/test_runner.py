import unittest

from runner import attempts_until_give_up, effective_config
from worker import load_config


class RunnerTests(unittest.TestCase):
    def test_default_attempts(self):
        self.assertEqual(attempts_until_give_up("a", {}), 3)

    def test_backoff_default_applies(self):
        self.assertEqual(effective_config({})["backoff"], 0.5)

    def test_load_config_reads_max_attempts(self):
        self.assertEqual(load_config({"MAX_ATTEMPTS": "5"})["max_attempts"], 5)


if __name__ == "__main__":
    unittest.main()
