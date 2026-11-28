export type Order = { id: string; customerId: string; totalCents: number; status: "pending" | "charging" | "paid" };

// Backed by Postgres in production; this in-memory version is what the tests use.
export class OrderStore {
  private rows = new Map<string, Order>();
  async get(id: string): Promise<Order | undefined> {
    const row = this.rows.get(id);
    return row && { ...row };
  }
  async update(id: string, patch: Partial<Order>): Promise<void> {
    const row = this.rows.get(id);
    if (row) this.rows.set(id, { ...row, ...patch });
  }
  // UPDATE orders SET status = $3 WHERE id = $1 AND status = $2, true when one row changed.
  // The in-memory version checks and writes with no await in between, so it is atomic too.
  async claim(id: string, from: Order["status"], to: Order["status"]): Promise<boolean> {
    const row = this.rows.get(id);
    if (!row || row.status !== from) return false;
    this.rows.set(id, { ...row, status: to });
    return true;
  }
  seed(order: Order): void {
    this.rows.set(order.id, order);
  }
}

// The card provider. With the same idempotencyKey, a repeated charge returns the first result and moves no money.
export interface Payments {
  charge(request: { customerId: string; amountCents: number; idempotencyKey?: string }): Promise<{ chargeId: string }>;
}
