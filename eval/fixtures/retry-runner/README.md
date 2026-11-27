# Retry runner

`runner.attempts_until_give_up` retries a failing job using `worker.schedule_retry`.

Configuration, from the environment:

- `MAX_ATTEMPTS`: total attempts including the first (default 3).
- `BACKOFF_SECONDS`: base delay between attempts (default 0.5).

Run the tests with `python -m unittest`.
