import { test } from "node:test";
import assert from "node:assert/strict";
import { pageCount, pageSlice } from "./src/pagination.ts";

test("pageCount rounds up a partial page", () => {
  assert.equal(pageCount(21, 10), 3);
  assert.equal(pageCount(1, 10), 1);
});

test("pageCount keeps exact multiples and zero", () => {
  assert.equal(pageCount(20, 10), 2);
  assert.equal(pageCount(0, 10), 0);
});

test("pageSlice is unchanged", () => {
  assert.deepEqual(pageSlice([1, 2, 3, 4, 5], 3, 2), [5]);
});
