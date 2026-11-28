import { readFileSync } from "node:fs";
import type { Order } from "./order.ts";
import { fromWire, type WireOrder } from "./wire.ts";

export function loadOrders(path = "data/orders.json"): Order[] {
  const saved = JSON.parse(readFileSync(path, "utf8")) as WireOrder[];
  return saved.map(fromWire);
}
