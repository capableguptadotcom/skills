import { test } from "node:test";
import assert from "node:assert/strict";
import { TtlCache } from "../src/cache.ts";

test("an entry expires after its ttl", () => {
  let t = 0;
  const cache = new TtlCache<number>(100, () => t);
  cache.set("a", 1);
  assert.equal(cache.get("a"), 1);
  t = 100;
  assert.equal(cache.get("a"), undefined);
});
