import { test } from "node:test";
import assert from "node:assert/strict";
import { initialState, reduce, statusText } from "./src/orderState.ts";

const run = (...events: any[]) => events.reduce((s, e) => reduce(s, e), initialState);
const order = { id: "o1", total: 12 };

test("retrying shows the attempt", () => {
  const s = run({ type: "fetch" }, { type: "failed", message: "timeout" }, { type: "retry", attempt: 2 });
  assert.equal(statusText(s), "Retrying (attempt 2 of 3)…");
});

test("a retry that succeeds shows the orders, not the old error", () => {
  const s = run({ type: "fetch" }, { type: "failed", message: "timeout" }, { type: "retry", attempt: 2 },
    { type: "loaded", orders: [order] });
  assert.equal(statusText(s), "1 orders");
});

test("a manual reload after a failure that succeeds shows the orders", () => {
  const s = run({ type: "fetch" }, { type: "failed", message: "timeout" }, { type: "fetch" },
    { type: "loaded", orders: [order] });
  assert.equal(statusText(s), "1 orders");
});

test("the last failed attempt shows the error", () => {
  const s = run({ type: "fetch" }, { type: "failed", message: "a" }, { type: "retry", attempt: 2 },
    { type: "failed", message: "b" }, { type: "retry", attempt: 3 }, { type: "failed", message: "c" });
  assert.equal(statusText(s), "Couldn't load orders: c");
});

test("existing behavior is kept", () => {
  assert.equal(statusText(run({ type: "fetch" })), "Loading orders…");
  assert.equal(statusText(run({ type: "fetch" }, { type: "loaded", orders: [] })), "No orders yet");
});
