import unittest

from worker import Job, load_config, schedule_retry


class ScheduleRetryTests(unittest.TestCase):
    def test_retries_with_configured_backoff(self):
        config = load_config({"BACKOFF_SECONDS": "0.5"})
        retry = schedule_retry(Job("a"), config)
        self.assertEqual((retry.attempt, retry.delay), (2, 0.5))

    def test_stops_after_max_attempts(self):
        config = load_config({"BACKOFF_SECONDS": "0.5", "MAX_ATTEMPTS": "2"})
        self.assertIsNone(schedule_retry(Job("a", attempt=2), config))


if __name__ == "__main__":
    unittest.main()
