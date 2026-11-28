# simplify-code: specification

**Job.** Make scoped existing code easier to read while its behavior stays the same.

**Output.** The edited code, the checks run, what became clearer and any behavior that could not be verified.

**Must.**

- Keep every observable behavior: return values, error types and messages, edge cases the visible tests do not cover.
- Stay inside the scope the request names, or the current change when it names none.
- Remove imports and helpers its own edits made unused.
- Run the checks that would detect changed behavior.

**Must not.**

- Drop a check that looks redundant but is not (a `bool` guard before an `int` check, `isdigit` instead of `int()`).
- Edit code outside the scope, even when it is also messy; mention it instead.
- Churn code that is already clear.

**Hosts.** Claude Code and Codex.

**Triggers.** "clean up", "simplify", "tidy", "make this clearer", "before I commit".
**Near misses.** A feature request; a bug fix; a design question.

**Cases.** See `cases.json`, on `eval/fixtures/order-utils`. Hidden tests in `hidden/` pin the behavior the visible tests leave open.

- `named-functions`: nested-if `apply_discount` and `parse_quantity`. The traps: `""` and 0% codes keep the total, codes are case-sensitive, the error message is exact, `True` and `2.0` are rejected, `"+3"` and `"-1"` are rejected as not whole numbers.
- `current-change`: an uncommitted new `shipping.py` with an unused import, an unused helper, `== True` and `cost = cost`. The messy `discounts.py` and `quantity.py` are outside the change and must not be touched.
- `already-clear`: `receipt.py` is already short and clear. The best answer changes little or nothing and says so.
