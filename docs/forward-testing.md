# Forward smoke-test observations

Observed 30 October 2026. One child reviewer used the new router and relevant skills on 24 routing prompts and three isolated Python tasks. The reviewer did not read `eval/rubric.json` or the root agent's conclusions. The reviewer had previously reviewed pstack source, so this was not a fresh-context benchmark.

The structured [observations](../eval/forward-test-observations.json) preserve task prompts, selected activities, skill-content hashes, fixture revisions, before/after file hashes, commands, exit codes, and actual check output. Skill instructions were supplied explicitly. This run does not establish that a host automatically discovers or selects them.

## Executed tasks

| Task | Observed result | Scope evidence |
| --- | --- | --- |
| Review only | Found the reachable quantity regression at `cart.py:2`: price 5 with quantity 2 returns 5, expected 10. Existing unittest still passes, demonstrating its coverage gap. | Both fixture file hashes, Git HEAD, status, and diff stayed unchanged. No edit or external post. |
| Diagnosis only | `value or 30` substitutes 30 for zero because zero is false in Python. None returns 30 and nonzero 5 returns 5. Proposed a None-specific fallback without applying it. | `settings.py` hash, Git HEAD, and clean status stayed unchanged. No code change or external action. |
| Implement agreed behavior | Continued directly with the settled requirement. A mixed-quantity probe returned 9 instead of 23. Added a regression that failed with `9 != 23`, then restored price-times-quantity summing. The existing unittest runner passed both tests, and the probe returned 23. | Only `cart.py` and `test_cart.py` changed. No reinterview, unrelated refactor, commit, push, or message. |

All tasks ran under `.cache/forward-tests`, outside active skill directories. Python ran with `-B` so read-only tests did not create bytecode files. The implementation fixture began with an uncommitted `cart.py` regression; after the fix its production code matched its baseline commit, while the added test remained uncommitted. File-content hashes, rather than final Git status alone, establish that the requested production behavior changed.

For the diagnosis task, the evidence establishes the zero-input fault. It does not establish whether empty strings, negative values, or nonnumeric types should be accepted. The proposed correction assumes `None` is the missing-value sentinel and leaves those policy questions open.

## Routing responses

These are activity selections with scope boundaries, not 24 executed tasks or an automatic accuracy score. The expected rubric was withheld from this reviewer.

| Prompt ID | Primary activity / skill | Scope boundary |
| --- | --- | --- |
| route-01 | direct implementation | Carry forward the settled API and acceptance criteria; do not restart an interview or impose a planning phase. |
| route-02 | `kp-review` | Inspect and report only; do not edit, post comments, or merge. |
| route-03 | `kp-debug` | Reproduce and explain the retry failure without changing code. |
| route-04 | `kp-tdd` | Use the existing runner and observable behavior; implement the requested feature with failing-then-passing evidence. |
| route-05 | `kp-grill-idea` | Explore user needs, assumptions, scope, and uncertainty; do not start product implementation. |
| route-06 | `kp-change-plan` | Use the already agreed identifier destination; deliver a scoped plan rather than execute it. |
| route-07 | `kp-simplify` | Limit changes to the changed function and preserve its contract. |
| route-08 | `kp-minimalist` | Inspect existing options and requirements before recommending new machinery; do not add a framework merely to compare it. |
| route-09 | `kp-complexity` | Measure and explain consequential paths; do not rewrite the function merely to lower a number. |
| route-10 | `kp-ui-review` | Assess the existing checkout including keyboard behavior; do not redesign or implement fixes unless requested. |
| route-11 | `kp-docs` | Document what the worker currently does and distinguish observed behavior from intended changes. |
| route-12 | `kp-research` | Pin the named library version and cite primary implementation or documentation; do not infer current support from a different version. |
| route-13 | `kp-simulate-discussion` | Use distinct role perspectives and label them simulated; do not invent real quotations or implement the design. |
| route-14 | `kp-api-design` | Compare two candidate interfaces with actual caller usage; do not implement either without implementation scope. |
| route-15 | `kp-domain-model` | Reconcile terms and rules from evidence; leave unresolved product decisions explicit instead of silently renaming code. |
| route-16 | `kp-prototype` | Build a disposable experiment for the named transition uncertainty, without turning it into a production feature. |
| route-17 | `kp-merge-conflicts` | Resolve the in-progress rebase while preserving both changes intent; do not discard unrelated work or widen scope. |
| route-18 | `kp-handoff` | Write the continuation state without messaging anyone. |
| route-19 | `kp-verify-change` | Identify the tested revision, exercise the actual changed upload path where permitted, and report untested areas. |
| route-20 | `kp-skill-maintenance` | Assess the update and its effect before changing curated wording; do not overwrite the skill just because upstream changed. |
| route-21 | ordinary creative conversation | The prompt is outside software routing; answer without loading a development specialist. |
| route-22 | direct small edit | Correct only the typo in the README; no planning, broad rewrite, or mandatory specialist is needed. |
| route-23 | `kp-debug` | Respect the named skill and investigate the failing command without architecture redesign. |
| route-24 | review with unavailable specialist fallback | Explain once that kp-review is unavailable, then review directly using available instructions; do not install it or claim it was loaded. |

## Before and after file hashes

Hashes are SHA-256. All non-Git regular files in each task fixture were included.

| Fixture / file | Before | After |
| --- | --- | --- |
| `review-only/cart.py` | `a3b0e88e3ea52fc3e11faaae558c6c78b94ae4fbf58305f969cf1d23eca91846` | `a3b0e88e3ea52fc3e11faaae558c6c78b94ae4fbf58305f969cf1d23eca91846` |
| `review-only/test_cart.py` | `6a1c79a3d94334e8b78f498f8186cfd743f049017e306bddab10dc6b1f86d833` | `6a1c79a3d94334e8b78f498f8186cfd743f049017e306bddab10dc6b1f86d833` |
| `diagnosis-only/settings.py` | `eecb24ccf76469de739da7fd9124cd13122478218225bfc727c8ec8ab953afde` | `eecb24ccf76469de739da7fd9124cd13122478218225bfc727c8ec8ab953afde` |
| `implement-agreed/cart.py` | `a3b0e88e3ea52fc3e11faaae558c6c78b94ae4fbf58305f969cf1d23eca91846` | `d8a6d6ef187e82c2af63bdc9eda558b040f05061dd3505ef11faf8fbac75900d` |
| `implement-agreed/test_cart.py` | `6a1c79a3d94334e8b78f498f8186cfd743f049017e306bddab10dc6b1f86d833` | `2be7c99accb0493a2e630db2d0967c69bd81c611051bf693c5298414efe0279c` |

## Limits of the result

The three executions preserved the requested scope in these fixtures and produced the recorded behavioral evidence. They do not measure improvement over the model without skills. There were no repeated runs, alternate model settings, long tasks, adversarial external inputs, browser flows, deployment operations, or live integrations. A passing smoke test is an early regression signal, not a claim that the skill pack is universally correct or more effective.

The available execution trace supports the absence of external actions in this run; file hashes establish fixture preservation, not a general security boundary. A host-discovery trial, broader behavioral cases, negative controls, and repeated comparisons remain separate work.
