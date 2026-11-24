# Familiar capabilities in the proposed pack

The earlier Wellnest collection exposed 18 activity names. This map explains their destination in our independently authored personal pack. It maps capabilities, not private source text or an assertion that the two packages behave identically. All 18 private entrypoint bodies were inspected locally at the recorded baseline; no private bodies are reproduced here.

| Familiar activity | Personal owner | What is retained or deliberately changed |
| --- | --- | --- |
| api-design | `kp-shape` → design reference | Caller examples, alternative boundaries and compatibility before implementation. |
| change-plan | `kp-shape` | Scope, consequential assumptions and independently checkable slices. |
| complexity | `kp-review` → complexity reference | Language-aware measurement and path risk; no universal numeric threshold or automatic refactor. |
| debug | `kp-debug` | Reproduction and competing explanations; diagnosis alone does not authorize a fix. |
| docs | `kp-develop` → documentation reference | Write about implemented behavior, using the established documentation home. |
| domain-model | `kp-shape` → design reference | Scenario-based terms and invariants without silently replacing product meaning. |
| grill-idea | `kp-shape` → exploration reference | Challenge the consequential assumption; preserve settled choices. |
| handoff | `kp-handoff` | Current objective, decisions, evidence, gaps and next action. |
| merge-conflicts | `kp-develop` → conflicts reference | Reconcile both intents in an actual merge/rebase; preserve user work. |
| minimalist | `kp-develop`, with design choices in `kp-shape` | Least machinery that meets the full requirement; no lost accessibility or failure behavior merely to shorten code. |
| prototype | `kp-shape` → design reference | A bounded experiment that answers a question; no automatic production promotion. |
| research | `kp-research` | Primary sources, actual versions and fact/inference distinctions. |
| review | `kp-review` | Intent and correctness assessed separately; actionable findings, no implicit fixes. |
| simplify | `kp-simplify` | Scoped cleanup with the contract and side effects preserved. |
| simulate-discussion | `kp-simulate-discussion` | Distinct simulated arguments, honest uncertainty and no fabricated empirical consensus. |
| start | Removed from the installable pack | No extra custom router. Descriptions expose the activities; host selection adequacy remains unmeasured. |
| tdd | `kp-develop` → testing reference | Requested red/green work at an observable seam, one behavior at a time. |
| ui-review | `kp-review` → UI reference | Assess actual rendered states and recovery paths within the existing design system. |

Seventeen activities therefore have a destination; the routing entrypoint is the deliberate removal. Consolidation is not evidence that every former behavior is preserved. The prior forward tests exercised only a subset. A missed request or incorrect reference selection should lead us to revise the owner or split a capability where the task evidence warrants it. Eight remains a proposal, not a quota.

The pstack pass adds conditional guidance for reusable runtime recipes and model/property maintenance under `kp-develop`. It adds no installable language-specific or formal-verification entrypoint. [The review](pstack-first-review.md) explains the decision and its limits.
