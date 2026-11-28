import { beforeEach, test } from "node:test";
import assert from "node:assert/strict";
import { handleWebhook } from "./src/webhook.ts";
import { resetLedger, totalCents } from "./src/ledger.ts";

beforeEach(() => resetLedger());

const succeeded = (data: unknown) => JSON.stringify({ type: "payment.succeeded", data });

function rejected(body: string) {
  let response;
  assert.doesNotThrow(() => { response = handleWebhook(body); });
  assert.equal(response.status, 400, `expected 400 for ${body}`);
  assert.equal(totalCents("USD"), 0);
}

test("records valid payments with exact totals", () => {
  assert.equal(handleWebhook(succeeded({ id: "pay_1", amount_cents: 1200, currency: "USD" })).status, 200);
  assert.equal(handleWebhook(succeeded({ id: "pay_2", amount_cents: 0, currency: "USD" })).status, 200);
  assert.equal(handleWebhook(succeeded({ id: "pay_3", amount_cents: 300, currency: "USD" })).status, 200);
  assert.equal(totalCents("USD"), 1500);
});

test("rejects a string amount (the incident)", () => rejected(succeeded({ id: "pay_1", amount_cents: "1200", currency: "USD" })));
test("rejects a fractional amount", () => rejected(succeeded({ id: "pay_1", amount_cents: 12.5, currency: "USD" })));
test("rejects a negative amount", () => rejected(succeeded({ id: "pay_1", amount_cents: -5, currency: "USD" })));
test("rejects missing data", () => rejected(JSON.stringify({ type: "payment.succeeded" })));
test("rejects a lowercase currency", () => rejected(succeeded({ id: "pay_1", amount_cents: 100, currency: "usd" })));
test("rejects malformed JSON", () => rejected("{"));
test("rejects JSON that is not an object", () => { rejected("null"); rejected("[]"); });

test("still acknowledges event types it does not handle", () => {
  const response = handleWebhook(JSON.stringify({ type: "payout.paid", data: { anything: true } }));
  assert.equal(response.status, 200);
});
