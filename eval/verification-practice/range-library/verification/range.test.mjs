import assert from 'node:assert/strict';
import { test } from 'node:test';
import { normalizeRange } from '../range.mjs';

function checkPairs(normalize, pairs) {
  const failures = [];
  let checked = 0;
  for (const [a, b] of pairs) {
    const actual = normalize(a, b);
    const expected = [Math.min(a, b), Math.max(a, b)];
    checked++;
    try {
      assert.deepEqual(actual, expected);
    } catch {
      failures.push({ input: [a, b], actual, expected });
    }
  }
  return { checked, failures };
}

function verify(pairs) {
  const result = checkPairs(normalizeRange, pairs);
  assert.equal(result.failures.length, 0,
    JSON.stringify({ checked: result.checked, failed: result.failures.length,
      examples: result.failures.slice(0, 3) }));
}

test('regression: decimal digit widths retain numeric ordering', () => {
  verify([[2, 10], [10, 2]]);
});

test('all 4225 ordered input pairs in [-32, 32]', () => {
  const pairs = [];
  for (let a = -32; a <= 32; a++) {
    for (let b = -32; b <= 32; b++) pairs.push([a, b]);
  }
  verify(pairs);
});

test('49 ordered endpoint and sign boundary pairs', () => {
  const values = [Number.MIN_SAFE_INTEGER, -10, -1, 0, 1, 10, Number.MAX_SAFE_INTEGER];
  verify(values.flatMap(a => values.map(b => [a, b])));
});

test('1000 repeatable generated safe integer pairs, seed 0x1a2b3c4d', () => {
  let seed = 0x1a2b3c4d;
  const next = () => {
    seed = (Math.imul(seed, 1664525) + 1013904223) >>> 0;
    return seed - 0x80000000;
  };
  verify(Array.from({ length: 1000 }, () => [next(), next()]));
});

test('verification sensitivity: clean control passes, lexical mutation fails', () => {
  const pairs = [[2, 10], [10, 2], [-2, -10], [0, 0]];
  assert.equal(checkPairs((a, b) => [a, b].sort((x, y) => x - y), pairs).failures.length, 0);
  assert.equal(checkPairs((a, b) => [a, b].sort(), pairs).failures.length, 2);
});
