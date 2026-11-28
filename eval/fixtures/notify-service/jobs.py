"""Queue worker. Each job is {"type": "order_shipped", "order": {...}, "customer": {...}}."""

import time

from customers import Customer
from notify import notify

MAX_ATTEMPTS = 5


def handle(job, mailer):
    if job["type"] == "order_shipped":
        notify(job["order"], Customer(**job["customer"]), mailer)
    else:
        raise ValueError(f"unknown job type: {job['type']}")


def run(queue, mailer, sleep=time.sleep):
    """Process jobs forever. A job that raises is put back and retried as a whole."""
    while True:
        job = queue.pop()
        try:
            handle(job, mailer)
        except Exception:
            job["attempts"] = job.get("attempts", 0) + 1
            if job["attempts"] < MAX_ATTEMPTS:
                sleep(2 ** job["attempts"])
                queue.push(job)
            else:
                queue.dead_letter(job)
