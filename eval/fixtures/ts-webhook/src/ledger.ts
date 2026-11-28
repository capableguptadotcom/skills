export type Payment = { id: string; amountCents: number; currency: string };

const entries: Payment[] = [];

export function recordPayment(payment: Payment): void {
  entries.push(payment);
}

export function totalCents(currency: string): number {
  return entries.filter((p) => p.currency === currency).reduce((sum, p) => sum + p.amountCents, 0);
}

export function resetLedger(): void {
  entries.length = 0;
}
