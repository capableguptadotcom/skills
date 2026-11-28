"""Postgres access for the notify schema."""

import os


def connect():
    import psycopg  # installed in production only

    return psycopg.connect(os.environ["NOTIFY_DATABASE_URL"], options="-c search_path=notify")
