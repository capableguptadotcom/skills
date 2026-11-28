import { test } from "node:test";
import assert from "node:assert/strict";
import { statusLabel } from "../src/order.ts";

test("labels every status", () => {
  assert.equal(statusLabel("pending"), "Awaiting payment");
  assert.equal(statusLabel("paid"), "Paid");
  assert.equal(statusLabel("canceled"), "Canceled");
});
