# Familiar capabilities in the proposed pack

The earlier Wellnest collection exposed 18 activity names. This map explains their destination in our independently authored personal pack. It maps capabilities, not private source text or an assertion that the two packages behave identically. All 18 private entrypoint bodies were inspected locally at the recorded baseline; no private bodies are reproduced here.

| Familiar activity | Personal owner | What is retained or deliberately changed |
| --- | --- | --- |
| api-design | `shape-change` → design reference | Caller examples, alternative boundaries and compatibility before implementation. |
| change-plan | `shape-change` | Scope, consequential assumptions and independently checkable slices. |
| complexity | `review-change` → complexity reference | Language-aware measurement and path risk; no universal numeric threshold or automatic refactor. |
| debug | `diagnose` | Reproduction and competing explanations; diagnosis alone does not authorize a fix. |
| docs | `develop` → documentation reference | Write about implemented behavior, using the established documentation home. |
| domain-model | `shape-change` → design reference | Scenario-based terms and invariants without silently replacing product meaning. |
| grill-idea | `shape-change` → exploration reference | Challenge the consequential assumption; preserve settled choices. |
| handoff | `handoff` | Current objective, decisions, evidence, gaps and next action. |
| merge-conflicts | `develop` → conflicts reference | Reconcile both intents in an actual merge/rebase; preserve user work. |
| minimalist | `develop`, with design choices in `shape-change` | Least machinery that meets the full requirement; no lost accessibility or failure behavior merely to shorten code. |
| prototype | `shape-change` → design reference | A bounded experiment that answers a question; no automatic production promotion. |
| research | `research` | Primary sources, actual versions and fact/inference distinctions. |
| review | `review-change` | Intent and correctness assessed separately; actionable findings, no implicit fixes. |
| simplify | `simplify-code` | Scoped cleanup with the contract and side effects preserved. |
| simulate-discussion | `simulate-discussion` | Distinct simulated arguments, honest uncertainty and no fabricated empirical consensus. |
| start | Removed from the installable pack | No extra custom router. Descriptions expose the activities; host selection adequacy remains unmeasured. |
| tdd | `develop` → testing reference | Requested red/green work at an observable seam, one behavior at a time. |
| ui-review | `review-change` → UI reference | Assess actual rendered states and recovery paths within the existing design system. |

Seventeen activities therefore have a destination; the routing entrypoint is the deliberate removal. Consolidation is not evidence that every former behavior is preserved. The prior forward tests exercised only a subset. A missed request or incorrect reference selection should lead us to revise the owner or split a capability where the task evidence warrants it. Eight remains a proposal, not a quota.

The pstack pass added conditional guidance for reusable runtime recipes and model/property maintenance. It was first placed under `develop` and now waits in `drafts/verification-skill/` for a separate explicit skill. It adds no installable language-specific or formal-verification entrypoint. [The review](pstack-first-review.md) explains the decision and its limits.
