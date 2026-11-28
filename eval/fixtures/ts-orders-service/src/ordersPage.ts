import { statusLabel } from "./order.ts";
import { loadOrders } from "./store.ts";

export function renderOrdersPage(): string[] {
  return loadOrders().map((order) => `${order.id}  ${statusLabel(order.status)}  $${(order.totalCents / 100).toFixed(2)}`);
}
