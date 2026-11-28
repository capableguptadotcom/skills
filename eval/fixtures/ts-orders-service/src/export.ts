import { appendFileSync } from "node:fs";
import type { Order } from "./order.ts";
import { toWire } from "./wire.ts";

export function exportOrders(orders: Order[], path = "exports/orders.jsonl"): void {
  const lines = orders.map((order) => JSON.stringify(toWire(order))).join("\n");
  if (lines) appendFileSync(path, lines + "\n");
}
