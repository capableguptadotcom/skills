# Shop checkout

`POST /api/orders/:id/pay` calls `payOrder` in `src/checkout.ts`. The Pay button (`src/PayButton.tsx`) disables itself while a payment is in flight. Support has seen customers double-click Pay, and mobile browsers sometimes resend a POST on a flaky connection. The API runs on several instances behind a load balancer, all using the same Postgres database.
