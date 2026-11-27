"""Hidden acceptance test, copied in only after the agent finishes."""

import unittest

from worker import Job, load_config, schedule_retry


class HiddenRetryTests(unittest.TestCase):
    def test_zero_backoff_retries_immediately(self):
        retry = schedule_retry(Job("a"), load_config({"BACKOFF_SECONDS": "0"}))
        self.assertIsNotNone(retry)
        self.assertEqual((retry.attempt, retry.delay), (2, 0.0))

    def test_missing_backoff_still_does_not_retry(self):
        self.assertIsNone(schedule_retry(Job("a"), load_config({})))

    def test_positive_backoff_unchanged(self):
        retry = schedule_retry(Job("a", attempt=2), load_config({"BACKOFF_SECONDS": "0.5", "MAX_ATTEMPTS": "5"}))
        self.assertEqual((retry.attempt, retry.delay), (3, 1.0))

    def test_max_attempts_unchanged(self):
        self.assertIsNone(schedule_retry(Job("a", attempt=3), load_config({"BACKOFF_SECONDS": "0"})))


if __name__ == "__main__":
    unittest.main()
