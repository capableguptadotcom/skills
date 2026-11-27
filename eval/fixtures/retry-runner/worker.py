"""Schedules retries for failed background jobs."""

import logging
import os
from dataclasses import dataclass

log = logging.getLogger("worker")


@dataclass
class Job:
    id: str
    attempt: int = 1


@dataclass
class Retry:
    job_id: str
    attempt: int
    delay: float


def load_config(env=None):
    env = os.environ if env is None else env
    config = {"max_attempts": int(env.get("MAX_ATTEMPTS", "3"))}
    if "BACKOFF_SECONDS" in env:
        config["backoff"] = float(env["BACKOFF_SECONDS"])
    return config


def schedule_retry(job, config):
    """Return the next Retry for a failed job, or None when it should not retry."""
    if job.attempt >= config["max_attempts"]:
        log.info("job %s exhausted %s attempts", job.id, job.attempt)
        return None
    delay = config.get("backoff")
    if delay is None:
        log.warning("retry backoff not configured; dropping retry for %s", job.id)
        return None
    return Retry(job_id=job.id, attempt=job.attempt + 1, delay=delay * job.attempt)
