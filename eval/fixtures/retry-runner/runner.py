"""Runs failed jobs again until they succeed or run out of attempts."""

from worker import Job, load_config, schedule_retry

DEFAULTS = {"max_attempts": 3, "backoff": 0.5}


def effective_config(env=None):
    """Configuration with defaults for anything the environment leaves out."""
    return {**load_config(env), **DEFAULTS}


def attempts_until_give_up(job_id, env=None):
    """How many attempts a job that always fails gets before the runner gives up."""
    config = effective_config(env)
    job = Job(job_id)
    while (retry := schedule_retry(job, config)) is not None:
        job = Job(job_id, attempt=retry.attempt)
    return job.attempt
