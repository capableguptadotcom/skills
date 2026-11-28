# notify-service

Tells customers when their order ships.

- `jobs.py` pulls jobs from the queue. A job that raises is retried as a whole, up to `MAX_ATTEMPTS`, with backoff. Production runs four worker processes (see `Procfile`).
- `notify.py` builds and sends the shipping email for one order.
- `customers.py` is the customer record we get from the accounts service.
- `db.py` is our Postgres connection; the service already owns the `notify` schema.

Run the tests with `python -m unittest`.
