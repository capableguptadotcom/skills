import { test } from "node:test";
import assert from "node:assert/strict";
import { fromWire, toWire } from "../src/wire.ts";

const order = { id: "o1", status: "paid" as const, placedAt: new Date("2026-11-02T10:00:00Z"), totalCents: 1250 };

test("toWire writes the export shape", () => {
  assert.deepEqual(toWire(order), { id: "o1", status: "paid", placedAt: 1793613600000, total_cents: 1250 });
});

test("fromWire round-trips", () => {
  assert.deepEqual(fromWire(toWire(order)), order);
});
