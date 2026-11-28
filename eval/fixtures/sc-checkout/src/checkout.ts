import type { OrderStore, Payments } from "./deps.ts";

export async function payOrder(orderId: string, orders: OrderStore, payments: Payments) {
  const order = await orders.get(orderId);
  if (!order) return { status: 404, body: "no such order" };
  if (order.status === "paid") return { status: 200, body: "already paid" };
  await payments.charge({ customerId: order.customerId, amountCents: order.totalCents });
  await orders.update(orderId, { status: "paid" });
  return { status: 200, body: "paid" };
}
