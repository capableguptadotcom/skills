import { withTimeout } from "./timeout.ts";

export type Invoice = { id: string; email: string; sentAt?: string };
export interface Invoices {
  get(id: string): Promise<Invoice>;
  markSent(id: string): Promise<void>;
}
export interface Mail {
  send(message: { to: string; template: string; data: object; idempotencyKey?: string }): Promise<void>;
}

export async function sendInvoice(invoiceId: string, invoices: Invoices, mail: Mail, attempts = 3, timeoutMs = 5000) {
  const invoice = await invoices.get(invoiceId);
  if (invoice.sentAt) return "already sent";
  for (let attempt = 1; ; attempt++) {
    try {
      await withTimeout(mail.send({ to: invoice.email, template: "invoice", data: { invoiceId } }), timeoutMs);
      break;
    } catch (error) {
      if (attempt === attempts) throw error;
    }
  }
  await invoices.markSent(invoiceId);
  return "sent";
}
