import type { OrderStore, Payments } from "./deps.ts";

export async function payOrder(orderId: string, orders: OrderStore, payments: Payments) {
  const order = await orders.get(orderId);
  if (!order) return { status: 404, body: "no such order" };
  if (!(await orders.claim(orderId, "pending", "charging"))) {
    return { status: 409, body: "payment already in progress or done" };
  }
  await payments.charge({ customerId: order.customerId, amountCents: order.totalCents, idempotencyKey: `order-${orderId}` });
  await orders.update(orderId, { status: "paid" });
  return { status: 200, body: "paid" };
}
