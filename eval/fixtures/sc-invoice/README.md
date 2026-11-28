# Billing jobs

`sendInvoice` in `src/sendInvoice.ts` runs from the job queue when an invoice is finalized. The queue retries a job that throws or whose process dies, up to 5 times. The mail provider's API is described in `docs/mail-provider.md`.
