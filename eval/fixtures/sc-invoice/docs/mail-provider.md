# Mail provider API

`POST /v1/send` with `{ to, template, data, idempotencyKey? }`.

- Replies 202 once the message is queued for delivery. Typical latency 300 ms; under load it can take more than 10 seconds to reply, and the message is still delivered.
- `idempotencyKey` (optional): a second request with the same key within 24 hours is acknowledged and not delivered again.
