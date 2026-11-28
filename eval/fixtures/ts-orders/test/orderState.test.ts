import { test } from "node:test";
import assert from "node:assert/strict";
import { initialState, reduce, statusText } from "../src/orderState.ts";

test("shows loading while fetching", () => {
  const state = reduce(initialState, { type: "fetch" });
  assert.equal(statusText(state), "Loading orders…");
});

test("shows the order count once loaded", () => {
  const state = reduce(reduce(initialState, { type: "fetch" }), {
    type: "loaded",
    orders: [{ id: "o1", total: 12 }],
  });
  assert.equal(statusText(state), "1 orders");
});

test("shows the error when the fetch fails", () => {
  const state = reduce(reduce(initialState, { type: "fetch" }), { type: "failed", message: "timeout" });
  assert.equal(statusText(state), "Couldn't load orders: timeout");
});
