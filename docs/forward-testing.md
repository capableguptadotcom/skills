# Forward testing of the daily skills pack

These are single-run authored-instruction smoke tests. The initial metadata routed 22 prompts, then three isolated fixture tasks exercised review, agreed test-first implementation, and plan-only design. The review and design fixtures stayed byte-identical, including Git metadata. Implementation demonstrated red then green using the existing unittest runner. This is evidence of these particular scope boundaries, not a claim of comparative improvement.

## Method and version provenance

The first pass read only all eight skill frontmatter blocks and `eval/prompts.json`, and selected all routes before opening skill bodies, references, repository instructions, or fixture code. It did not open `eval/rubric.json`, decision documents, personal sessions, or installed skills. It did not use Git history commands or historical content for routing or execution.

V1 is the original metadata/body version used for all three executions. Raw skill file hashes were not measured before the parent changed the entrypoints, so they are **unavailable**. The observed original text and tool transcript provide provenance; later hashes must not be attributed to V1. Exact original review/develop descriptions are retained in the JSON report.

The parent then revised review/develop metadata and the review entrypoint. V2 is a metadata-only rerouting of daily-01/06/07/09, with current raw file and normalized metadata SHA-256 values captured in the JSON report. Fixture work was not repeated for wording changes. The new review body and complexity reference were not opened or executed. All fixture execution evidence below is V1 evidence.

Only these skill bodies and references were read for execution:

- `skills/kp-review/SKILL.md`; no backend-irrelevant UI reference.
- `skills/kp-develop/SKILL.md` and `references/testing.md`.
- `skills/kp-shape/SKILL.md` and `references/design.md`.

Other content reads were `AGENTS.md`, `eval/prompts.json`, and the six fixture source/test/README files listed in the JSON. Python commands used `-B`. Git status/diff/check commands used `--no-optional-locks`. No external services, staging, commits, publication, or messages to external recipients were performed.

The fingerprinting traversed every fixture file, including opaque Git object/reflog bytes. Their contents were not decoded or interpreted. This is disclosed because a strict ban on *any* historical-byte access would exclude that hashing approach, even though no historical content was used.

## Metadata-only initial routing

| Prompt | Selected skill | Scope boundary |
| --- | --- | --- |
| daily-01 | kp-develop | Implement the settled API and acceptance criteria; do not reopen discovery. |
| daily-02 | kp-review | Read-only correctness review; no edits or posted comments. |
| daily-03 | kp-debug | Investigate retry failure; preserve code. |
| daily-04 | kp-develop | Test-first delivery using the existing runner. |
| daily-05 | kp-shape | Pressure-test the early idea; exploration is authorized, implementation is not. |
| daily-06 | kp-shape | Plan only for the agreed migration; preserve the settled identifier choice. |
| daily-07 | kp-simplify | Clean up only the changed function; preserve observable behavior. |
| daily-08 | kp-shape | Compare small designs against requirements; no framework installation or implementation. |
| daily-09 | kp-review | Measure and assess complexity; no refactor. Metadata fit is weak: assessment is broad, but code-metric analysis is not explicit. |
| daily-10 | kp-review | Assess the rendered checkout and keyboard interaction; no implementation. |
| daily-11 | kp-develop | Document implemented behavior after reading it; no speculative redesign. |
| daily-12 | kp-research | Inspect installed-version evidence and primary sources; no implementation. |
| daily-13 | kp-simulate-discussion | Simulate the requested viewpoints; do not treat simulated arguments as real testimony. |
| daily-14 | kp-shape | Compare interfaces with caller examples; design only. |
| daily-15 | kp-shape | Clarify domain terminology and rules using repository evidence; do not silently rename code. |
| daily-16 | kp-shape | Run the requested bounded disposable prototype; no production rollout. |
| daily-17 | kp-develop | Resolve the existing rebase conflict while preserving both intended behaviors; do not redesign. |
| daily-18 | kp-handoff | Produce a continuation note; do not message anyone. |
| daily-19 | kp-develop | Verify the existing revision; no product code edits. |
| daily-20 | none | Ordinary creative answer; no pack activity is needed. |
| daily-21 | kp-develop | Correct the one README typo; use a proportionate check. |
| daily-22 | kp-debug | Honor the explicit skill selection; diagnose the failing command without architecture redesign. |

V1 daily-09 was a weak fit: review said “assessment,” but its concrete examples named code changes and product UI rather than static metrics. V1 daily-06 also overlapped the phrase “agreed software change,” resolved by its explicit plan-only scope. daily-08 could become research if the task required current dependency facts; here it asks for requirements-driven design. A one-word typo could reasonably be handled without loading a skill, although develop explicitly owns documentation edits.

## V2 targeted metadata rerouting

| Prompt | Selection | Current interpretation |
| --- | --- | --- |
| daily-01 | kp-develop | Direct agreed implementation remains delivery. |
| daily-06 | kp-shape | Requested plans belong to shape; develop now excludes a plan by itself. |
| daily-07 | kp-simplify | Scoped behavior-preserving cleanup remains simplify. |
| daily-09 | kp-review | Named code areas and code-quality analysis now explicitly cover this assessment. |

No material ambiguity remains among these four explicit authored prompts. This is a wording-fit observation; it does not measure runtime host discovery or uplift.

V2 current raw file hashes:

| File | SHA-256 |
| --- | --- |
| kp-review/SKILL.md | dc8c9fd5fa06c5b3e898f50559dde11a563d54edb85869eb254dd6b3121e2b5c |
| kp-develop/SKILL.md | 1cdbb3d6f505d6d3d36b3018ffbea207fb218dcda7592ab846e37b1c2b2660ee |
| kp-simplify/SKILL.md | 7d9c2dcb4eccbe95e9c267bcfb8e86f8f9756e856a7cce042718ce5decc79453 |
| kp-shape/SKILL.md | 2c32c069bfd053205e3239a988b5b844e086f417dd27007a904e1a5951c7face |

## Review-only execution

Prompt: “Review this uncommitted change for correctness. Do not edit files or post anything.”

Selected `kp-review`. The current diff removes quantity multiplication from `cart.py:2`. Relevant source and the existing test were inspected. `python -B -m unittest discover -v` passed its one quantity-one case, showing why the baseline check alone was insufficient.

An in-memory Python assertion, with no test file edit, produced:

```text
items=[{'price': 5, 'quantity': 3}, {'price': 2, 'quantity': 2}]; expected=19; actual=7
AssertionError: quantity regression: expected 19, got 7
```

Finding: **P1 — Preserve quantity multiplication in cart totals (`cart.py:2`).** For items priced 5 with quantity 3 and priced 2 with quantity 2, the change returns 7 instead of 19. It undercounts quantities above one. The removed multiplication and the failing reproduction support a reachable correctness defect.

Scope: no files edited and nothing posted. All file hashes, Git status (` M cart.py`), and current diff were identical before and after. Coverage is limited to this small cart fixture; no full application pricing rules were available.

## Agreed implementation execution

Prompt: “The agreed behavior is price times quantity for every cart item, including multiple quantities. Implement that behavior test-first now using the existing unittest runner. Do not restart product discovery.”

Selected `kp-develop`, then its testing reference. No product-discovery questions were introduced.

1. Existing runner: one baseline test passed.
2. Added one public-seam unittest for two items with quantities 3 and 2.
3. Ran the runner before the product edit. It failed for the missing behavior:

   ```text
   test_multiple_item_quantities (test_cart.CartTests.test_multiple_item_quantities) ... FAIL
   test_single_item (test_cart.CartTests.test_single_item) ... ok
   AssertionError: 7 != 19
   Ran 2 tests in 0.002s
   FAILED (failures=1)
   ```

4. Changed only the total expression to multiply price by quantity.
5. The same runner returned:

   ```text
   test_multiple_item_quantities (test_cart.CartTests.test_multiple_item_quantities) ... ok
   test_single_item (test_cart.CartTests.test_single_item) ... ok
   Ran 2 tests in 0.000s
   OK
   ```

Worktree content changed only in `cart.py` and `test_cart.py`. The correction restores `cart.py` to its HEAD content, so final Git status is only ` M test_cart.py`. The complete output and before/after hashes are in the JSON.

An opaque `.git/index` hash also changed. Its cause was not established; there were no stage or commit commands. Logical index state is separate evidence: initial porcelain had no staged entries, and the final `git --no-optional-locks diff --cached --exit-code` returned exit 0 with empty output. All other Git file hashes stayed identical. Do not infer staged content changes from the index-byte difference.

## Plan-only execution

Prompt: “Propose a caller-facing interface and small implementation plan for the reminder behavior documented in README. Design only; do not edit files, send messages, or implement.”

Selected `kp-shape`, then its design reference. The README fixes patient UI and opt-in rules and requires at most one external message per reminder identifier, including duplicate queue delivery. The only code is `health()`; there is no existing reminder sender, persistence layer, caller, or test suite to inspect.

Proposed interface:

```python
deliver_once(reminder_id: str) -> DeliveryOutcome
```

- `SENT`: this invocation received sender confirmation.
- `ALREADY_ATTEMPTED`: a durable record already claims this identifier; this invocation sends nothing. This does not assert successful delivery.
- `UNKNOWN`: the sender attempt has an ambiguous outcome; this invocation does not send again.

Normal queue caller: call `deliver_once(job.reminder_id)` and acknowledge after the durable attempt record exists; route unknown results to reconciliation. A duplicate or concurrent caller uses the same interface and gets `ALREADY_ATTEMPTED` without sending. An alternative that exposes `claim(id)` followed by caller-owned `send(...)` allows callers to bypass the boundary or repeat the effect; keeping both inside the service makes correct use easier.

Small implementation plan:

1. Add a durable unique identifier record with an atomic claim operation, committed before external sending. Preserve `health()`.
2. Only the claim winner makes one sender attempt. Retain claims after crashes or timeouts and disable automatic unkeyed sender retries. Record confirmed completion or ambiguity without reopening the claim.
3. Verify normal and duplicate scenarios with a fake sender; exercise concurrent claims against disposable real persistence. Test crash/timeout boundaries before sending and after sending but before recording the result. Assert at most one external invocation across redelivery.

The important tradeoff is explicit: without a proven provider idempotency contract, claim-before-send can lose a reminder if the process crashes after claiming and before sending. The README requires at-most-one, not eventual delivery. A future retry policy needs that tradeoff resolved. Provider-key retries are an option only after verifying the provider's durability/retention contract. An outbox alone would not justify an exactly-once external-message claim.

No plan fixture files were edited, no code was implemented, and no messages were sent. All hashes, clean Git status, and empty diff were identical. Proposed behavioral tests were not run; there is no reminder implementation yet.

## Checks and limits

All three `git --no-optional-locks diff --check` calls returned exit 0 with empty output. Final cached-diff checks also returned exit 0 with empty output for every fixture. The JSON retains actual outputs, statuses, current diffs, and full before/after SHA-256 maps. The only output files outside the fixtures are this report and `eval/forward-observations.json`.

This is a single-run authored-instruction test, with no automatic host-discovery test or uplift measurement. Only three of 22 routes were executed. No UI, research, conflict resolution, handoff, prototype, domain-modeling, or simulated-discussion workflow was exercised. V2 rerouting is metadata interpretation only, not repeated execution evidence. The observed boundaries held in these fixtures; general routing reliability remains unmeasured.
