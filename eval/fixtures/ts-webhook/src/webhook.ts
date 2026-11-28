import { recordPayment, type Payment } from "./ledger.ts";

export type WebhookResponse = { status: number; body: string };

export function handleWebhook(rawBody: string): WebhookResponse {
  const event = JSON.parse(rawBody) as {
    type: string;
    data: { id: string; amount_cents: number; currency: string };
  };
  if (event.type !== "payment.succeeded") return { status: 200, body: "ignored" };
  const payment: Payment = {
    id: event.data.id,
    amountCents: event.data.amount_cents,
    currency: event.data.currency,
  };
  recordPayment(payment);
  return { status: 200, body: "ok" };
}
