# Provider webhook contract

Every webhook is a JSON object:

| Field | Type | Notes |
| --- | --- | --- |
| `type` | string | `payment.succeeded`, `payment.failed`, `refund.created`; more may be added |
| `data.id` | string | starts with `pay_` |
| `data.amount_cents` | integer | 0 or more |
| `data.currency` | string | ISO 4217, three uppercase letters |

Reply 2xx to acknowledge. Reply 400 for a payload you will never accept: the provider stops retrying it and lists it in the dashboard. Any other failure (5xx, timeout) is retried for 24 hours.
