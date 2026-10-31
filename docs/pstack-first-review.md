# Pstack first: what should become ours

31 October 2026. The objective is a useful owned development pack for TypeScript, JavaScript and Python, with pstack examined deeply before adding more material. The proposed eight activities remain provisional. This review does not install skills, merge the proposal, configure a host or resume source-sync automation.

## What was actually examined

Canonical source: [cursor/plugins pstack at `4dd1d05818d19792e7cd6e818f1667f95f7e1dbe`](https://github.com/cursor/plugins/tree/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack), identifying itself as 0.15.36. The full available Git history was fetched; the first public import is a port of an existing system. Earlier private development is not observable here.

All **58 canonical entrypoint bodies** were read and assessed, along with their per-path public histories and selected substantive diffs. Generated Claude copies are not extra skills. The mode's 23 playbooks are not extra entrypoints either. References and helpers received the explicitly stated coverage below; this is not a complete executable dependency audit.

| Reading path | Contents and inspection depth |
| --- | --- |
| [Actual history and feedback](research/pstack-history.md) | Selected merged PR bodies, review discussions, shipped diffs and tests; author-reported experiments separated from reproduced facts. |
| [26 workflow assessments](research/pstack-workflows.md) | Each body, per-path history, named references and selected helpers; language/host assumptions, overlap, simulated arguments, proposed falsification and disposition. |
| [24 principle assessments](research/pstack-principles.md) | Every principle body and path history, selected changes and dependencies; where the reasoning helps and where literal rules overreach. |
| [8 verification and host assessments](research/pstack-verification-and-host.md) | Creation/maintenance of runtime and formal checks; statechart, setup, help and operating mode. Selected executable dependencies inspected statically. |

These are engineering judgments grounded in primary material. **Simulated** practitioner, skeptic and evaluator roles are labeled throughout. Proposed evaluations have not passed simply because they are described. Upstream comparative results are reports, not our independent replications. No upstream installer/helper was executed. The current owned-reference smoke tests and their precise limits are recorded separately in [verification practice](verification-practice.md).

## Every entrypoint at a glance

“Absorb” means an idea has a possible owner; it is not an instruction to copy the source or immediately add wording. Only the two conditional verification references described below change active skill instructions in this pass. Full reasons, history, objections and falsifiable cases are in the linked assessments.

| Workflow entrypoint | One-line use | Provisional disposition |
| --- | --- | --- |
| architect | Compare caller-facing module designs and implement a selected shape. | Absorb design questions in shape; preserve a design-only stopping point. |
| arena | Compare independent attempts and integrate the best parts. | Conditional tactic; verify the integrated result and avoid model-family certainty. |
| automate-me | Infer a personal working mode from scoped session history. | Defer with session-learning design. |
| benchmark-checklist | Check that a performance measurement represents correct useful work. | Absorb evidence questions; adapt tools and sampling to the claim. |
| blast-radius | Trace effects beyond a small diff and probe its critical assumptions. | Absorb in review without forcing exactly one safety fact. |
| bro | Restate the previous answer plainly. | Communication preference, not another daily activity. |
| correct | Replace repeated mistakes with appropriate structural enforcement. | Conditional prevention work; do not expand ordinary fixes into hardening sweeps. |
| create-formal-verification-skill | Create a code-linked, rerunnable property-verification procedure. | Adapt as a requested develop mode, without mandatory sibling tools. |
| create-verification-skill | Create a real-app launch/drive/evidence/cleanup recipe. | Adapt as a project-specific develop mode. |
| figure-it-out | Design an evidence-driven workflow for a large unfamiliar task. | Absorb bounded increments and goal checks, not an umbrella router. |
| how | Explain current behavior from traced code/data flow. | Absorb in research; proportional decomposition. |
| in-your-own-words | Check the intended goal before starting consequential work. | Use concise restatement where it resolves ambiguity. |
| interrogate | Seek executable adversarial findings on a change. | Absorb in review; retain material source-backed risks that cannot be run. |
| ketchup | Catch the returning user up with individually decidable pending items. | Absorb in handoff; no hard word cap that hides work. |
| ketchup-video | Turn a catch-up into subtitled visual slides/video. | On-demand artifact, outside the default pack. |
| maintain-formal-verification-skill | Reconcile a model/property suite with changed implementation. | Adapt per-check fidelity, drift/bug distinction and blocked-anchor handling. |
| maintain-verification-skill | Reconcile a runtime recipe and feature map with the actual app. | Adapt requested coverage and resource-lifetime invariants. |
| make-bot-ui | Build a UI connected to a particular Grok Bot control plane. | Exclude; integration-specific, not general product development. |
| no-comments | Aggressively remove comments using an adversarial deletion policy. | Reject literal policy; understand/enforce constraints before deleting them. |
| poteto-help | Navigate pstack setup, commands and recipes. | README/descriptions suffice for our smaller proposal. |
| poteto-mode | Run a Cursor-oriented engineering operating mode and playbooks. | Do not copy the router or inherited permissions. Adopt bounded mechanisms selectively. |
| recall | Recover scoped prior-work context from several evidence sources. | Handoff technique; cross-session access remains separately scoped. |
| reflect | Turn a completed session's lessons into proposed skill changes. | Defer; cache ownership, evidence and session scope need their own design. |
| setup-pstack | Configure per-role models and a persistent rule in a host. | Exclude from the portable activity pack. |
| sharpen | Deepen a prompt while preserving its intended deliverable. | Optional framing; do not turn prompt editing into task execution. |
| show-me-your-work | Keep and audit a decision trail for long work. | Compact optional trail in develop/handoff, without mandatory tooling rituals. |
| statechart | Compile TLC results into domain-labeled charts and bug paths. | Optional tool evaluation; do not bundle its runtime stack into prompts. |
| swarm | Coordinate partitioned or raced workers with coverage and provenance. | Conditional delegation mechanics using available host capabilities. |
| tdd | Reproduce and fix a bug through behavior-first red/green evidence. | Absorb in debug/develop; distinguish pstack's bug-fix scope from general TDD. |
| teach | Explain mechanisms in language the recipient can use. | Research/handoff technique; diagrams only when they help. |
| technical-writing | Write clear, accurate task-oriented technical material. | Absorb clarity and ambiguity checks, not universal punctuation rules. |
| typescript-best-practices | Guide TypeScript state, boundary and type design. | Selective language detail; correct guarantees and use project conventions. |
| unslop | Remove empty or misleading patterns from prose. | Writing habit, distinct from behavior-preserving code cleanup. |
| why | Recover historical reasons with source and confidence distinctions. | Research technique; no compulsory sweep across unavailable integrations. |

The following are the 24 `principle-<name>` entrypoints. None currently justifies another installed entrypoint merely by being a principle.

| Principle name | One-line use | Provisional disposition |
| --- | --- | --- |
| attack-the-premise | Test the assumption shared by repeated failed interventions. | Debug principle; the assumption may survive. |
| boundary-discipline | Translate external inputs and separate business decisions from adapters. | Adapt to actual runtime/mutation guarantees. |
| build-the-lever | Make repeated work or proof reproducible with a checked tool. | Conditional on cost; do not require a new script for every task. |
| encode-lessons-in-structure | Enforce a settled repeated rule instead of accumulating reminders. | Keep cost and contract checks; no session-mining implication. |
| exhaust-the-design-space | Compare materially different designs before a consequential choice. | Shape tactic; reject literal exhaustive exploration. |
| experience-first | Evaluate product choices through user-visible outcomes. | Shape question; existing requirements still constrain scope. |
| explain-the-number | Identify what a measurement means before acting on it. | Evidence principle, without universal statistical ritual. |
| fix-root-causes | Distinguish legitimate states from symptoms of an upstream defect. | Debug principle; bounded mitigation may still be appropriate. |
| foundational-thinking | Choose enabling data and ownership decisions early. | Distribute concrete questions rather than add another broad rule. |
| guard-the-context-window | Keep decisive evidence accessible without flooding the coordinator. | Bounded reading and summaries; delegation optional. |
| laziness-protocol | Centralize real repeated decisions and keep the change small. | Merge with scoped simplicity guidance. |
| make-operations-idempotent | Reconcile retries and interrupted work without unintended duplicate effects. | Conditional stateful-work principle. |
| migrate-callers-then-delete-legacy-apis | Finish a coordinated internal API migration. | Verify dynamic consumers and release boundaries first. |
| minimize-reader-load | Reduce hidden state and needless indirection. | Simplify principle; caller count alone does not decide a boundary. |
| model-the-domain | Represent actual invariants instead of synchronizing scattered conditions. | Shape principle; no forced framework for a short calculation. |
| never-block-on-the-human | Progress on authorized work without needless permission turns. | Preserve authorization and consequential product ambiguity; reject an absolute rule. |
| outcome-oriented-execution | Allow bounded intermediate breakage inside an agreed rewrite. | Narrow migration exception with checkpoints. |
| prove-it-works | Observe the promised artifact or behavior at the actual revision. | Completion principle with explicit coverage limits. |
| redesign-from-first-principles | Use a counterfactual design to expose poor seams. | Shape question; reject automatic redesign for every requirement. |
| separate-before-serializing-shared-state | Isolate independent writers and coordinate genuine shared invariants. | Conditional ownership principle; preserve transactions. |
| sequence-verifiable-units | Order work and delivery around coherent evidence-producing increments. | Adapt to meaningful boundaries, including intentional red evidence. |
| subtract-before-you-add | Remove obsolete complexity in the affected path before replacement. | Scoped question; no unrelated deletion sweep. |
| test-behavior-not-implementation | Catch contract breakage while surviving an internal refactor. | Keep the decision test; reject assertion-syntax blacklists. |
| type-system-discipline | Represent semantic distinctions and validate actual boundaries. | Language-specific detail where useful; types do not replace runtime validation. |

## What the actual revisions teach us

Several histories are unusually informative. [#633](https://github.com/cursor/plugins/pull/633) replaces assertion and lock prescriptions that overfit particular examples. [#729](https://github.com/cursor/plugins/pull/729) restores a prompt-rewriting deliverable after it had drifted into execution. [#573](https://github.com/cursor/plugins/pull/573) distinguishes an answering database port from usable initialized state. [#716](https://github.com/cursor/plugins/pull/716) openly reports no corrected correctness gain in its main comparison, then isolates a blocked-anchor failure with a separate wording comparison. [#982](https://github.com/cursor/plugins/pull/982) turns a real wrong trace label into an executable corpus regression.

There are also limits. Some changes have only structural validation or equivalence claims. The reflection cache fix retains unresolved review concerns about copied dependencies and lost local edits. The statechart implementation has stronger executable tests than a prose-only rule, but those tests cannot establish that an agent chose a faithful model of production code. Ports and model-default refreshes do not by themselves demonstrate maturation. Read the [history note](research/pstack-history.md) for the reported results, inspected patches and caveats.

## Simulated discussion and the present decision

**Practitioner:** The useful result is a small set I can ask to do work. Runtime recipes and model drift matter across Python and JavaScript; they should not require learning pstack's whole operating system.

**Maintainer:** Put general procedure in its existing owner and the real commands/properties in the project. Keep an unchanged upstream copy distinguishable from owned wording; never let a local edit disappear on update.

**Skeptic:** Consolidation can conceal a giant workflow. Two extra references still need observable value, and 58 plausible assessments do not establish 58 useful instructions. A rule that prevented one mistake can damage a neighboring valid case.

**Evaluator:** Exercise the new verification modes on actual shipped functions and a stale model, plus a small request where neither mode should activate. Record exactly which text was used. Compare a baseline before claiming uplift; this pass's small smoke test cannot supply that comparison.

**Synthesis:** Keep the eight entrypoints provisional. Add only conditional, independently installable guidance for requested project-runtime recipes and property/model fidelity under `kp-develop`. The new wording omits pstack paths, model names, mandatory renderers, fixed worker counts and automatic publication. Track unchanged copies differently from owned adaptations as described in [the ownership policy](language-and-ownership.md). The current pack contains no tracked upstream copies. Preserve the [familiar capabilities](capability-map.md) visibly, and defer session-learning automation and host-selection diagnosis.

Unresolved by this review: whether a separate verification entrypoint becomes worthwhile in repeated daily use; which stack-specific detail genuinely needs a reusable reference; how reliably the host selects the right owner during long sessions; and which comparative cases will establish that our wording helps beyond the host's existing instructions. These questions require usage or controlled behavioral evidence, not another source inventory.
