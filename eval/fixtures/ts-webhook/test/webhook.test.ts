import { beforeEach, test } from "node:test";
import assert from "node:assert/strict";
import { handleWebhook } from "../src/webhook.ts";
import { resetLedger, totalCents } from "../src/ledger.ts";

beforeEach(() => resetLedger());

test("records a succeeded payment", () => {
  const body = JSON.stringify({ type: "payment.succeeded", data: { id: "pay_1", amount_cents: 1200, currency: "USD" } });
  assert.equal(handleWebhook(body).status, 200);
  assert.equal(totalCents("USD"), 1200);
});

test("ignores other event types", () => {
  const body = JSON.stringify({ type: "refund.created", data: { id: "re_1" } });
  assert.deepEqual(handleWebhook(body), { status: 200, body: "ignored" });
});
