# Orders service

TypeScript service behind the customer orders page and the nightly finance report.

- `src/order.ts`: the order model and status labels shown on the orders page.
- `src/wire.ts`: the JSON shape served by `GET /orders` and appended to `exports/orders.jsonl`.
- `src/export.ts`: appends today's orders to the export file.
- `src/store.ts`: loads saved orders from `data/orders.json` (written by earlier releases, same wire shape).
- `src/cache.ts`: a small TTL cache for price lookups.
- `jobs/nightly_report.py`: the finance team's nightly job. It reads `exports/orders.jsonl` and prints revenue per day and the count of canceled orders. It runs on the reporting box with Python 3.11, not in this repo's CI.

TypeScript tests run on Node's type stripping (`node --experimental-strip-types --test "test/*.test.ts"`).
