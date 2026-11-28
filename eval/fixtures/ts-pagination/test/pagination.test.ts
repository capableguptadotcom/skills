import { test } from "node:test";
import assert from "node:assert/strict";
import { pageCount, pageSlice } from "../src/pagination.ts";

test("pageSlice returns the requested page", () => {
  assert.deepEqual(pageSlice([1, 2, 3, 4, 5], 2, 2), [3, 4]);
});

test("pageCount for an exact multiple", () => {
  assert.equal(pageCount(20, 10), 2);
});
