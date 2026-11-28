import type { Order, OrderStatus } from "./order.ts";

// The shape written to exports/orders.jsonl and served by GET /orders.
export type WireOrder = {
  id: string;
  status: OrderStatus;
  placedAt: number; // epoch milliseconds
  total_cents: number;
};

export function toWire(order: Order): WireOrder {
  return {
    id: order.id,
    status: order.status,
    placedAt: order.placedAt.getTime(),
    total_cents: order.totalCents,
  };
}

export function fromWire(wire: WireOrder): Order {
  return {
    id: wire.id,
    status: wire.status,
    placedAt: new Date(wire.placedAt),
    totalCents: wire.total_cents,
  };
}
