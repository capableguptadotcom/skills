# Range contract verification

Run from this repository root:

```sh
node --test verification/range.test.mjs
```

No dependencies, installs, service, browser, or app harness are required. The tests import the shipped `normalizeRange` from `range.mjs`. The oracle is exactly `[Math.min(a, b), Math.max(a, b)]`, checking ascending numeric bounds and preserving both endpoints, including equal bounds.

At product revision `799ac5de2928e1f987d0e76204589d6aa820cc6b`, Node v22.14.0 reports four failing contract groups and one passing verification-sensitivity group. The shipped implementation uses default lexical sorting: `(2, 10)` returns `[10, 2]`, contradicting the contract.

Coverage (sample pairs can overlap between groups):

| Group | Pairs checked | Failures |
| --- | ---: | ---: |
| Two digit-width regressions | 2 | 2 |
| Exhaustive ordered pairs in [-32, 32] | 4225 | 992 |
| Safe-integer endpoints, signs, zero, equal values | 49 | 6 |
| Deterministic generated pairs, seed 0x1a2b3c4d | 1000 | 245 |

The generated sequence covers signed 32-bit integers, a subset of safe JavaScript integers. Endpoint examples include `Number.MIN_SAFE_INTEGER` and `Number.MAX_SAFE_INTEGER`. All pairs in each group are evaluated even after an earlier mismatch. The sensitivity group passes a numeric-sort scratch function and detects two failures in four examples for a deliberate lexical-sort mutation. This supports the checker, while the other groups directly test shipped code. No product source is changed.

This is bounded enumeration and generated-input testing, not formal proof over all safe integers. It establishes concrete counterexamples, not a universal guarantee. Out-of-contract inputs (fractions, nonnumbers, unsafe integers), mutation behavior beyond returning these bounds, and negative-zero identity semantics have no promised validation here. A prior scratch-control assertion expected three lexical failures; the actual result was two because `[-2, -10]` already sorts correctly lexically. That test expectation was corrected before the final run.
