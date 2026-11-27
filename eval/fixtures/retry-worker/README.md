# Retry worker

`schedule_retry` decides whether a failed job is retried and after how long.

Configuration, from the environment:

- `MAX_ATTEMPTS`: total attempts including the first (default 3).
- `BACKOFF_SECONDS`: base delay between attempts. `0` means retry immediately. Required for retries.

Run the tests with `python -m unittest`.
