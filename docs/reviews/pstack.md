# pstack: per-skill source review

Snapshot: [cursor/plugins@4dd1d05818d1](https://github.com/cursor/plugins/tree/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack), inspected 30 October 2026. This review covers **all 58 canonical `pstack/skills/*/SKILL.md` files** at that commit. Generated harness copies, other plugins in the monorepo, and 23 playbook files are not additional skills. The Eval, Authoring a skill, Investigation, Bug fix, and Multi-phase plan playbooks and relevant architecture, confidence, and reflection references were also read. Counts describe this pinned snapshot, not all future releases.

License: [pstack/LICENSE](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/LICENSE) is MIT, copyright 2026 Lauren Tan. This report summarizes the source; it does not install pstack or execute its helper scripts. Adapted code or substantial copied text must retain the source notice.

The three perspectives below are a **simulated discussion written by one reviewer**, not statements from the author or results from three independent evaluators. Practitioner values practical benefit; Skeptic challenges authority, scope, runtime assumptions, and cost; Evaluator proposes a falsifiable check. Consensus records a curation recommendation, not measured superiority. Every entry has evidence level `source-review`; its proposed behavioral check has **not** been run by this review.

`adapt` means transfer selected ideas into an owned skill after evaluation. `profile` means optional use for a named stack or workflow. `reference` means useful reading without another discoverable skill. `reject` means reject the raw procedure as a default, not reject every idea it contains. A target names a proposed personal destination, not proof that every transfer has already been implemented.

## Collection-level decision

Do not install the complete pack alongside the personal router. `poteto-mode` is an integrated personal workflow with host-specific model assignments and broad orchestration. Its strengths are explicit real-artifact verification, practical bug reproduction, cross-boundary reasoning, measurement skepticism, and verification drift maintenance. Transfer those ideas without importing default external actions, compulsory multi-agent panels, universal comment removal, or a second lifecycle router.

Most canonical skills set `disable-model-invocation: true`; `setup-pstack` is the exception in this snapshot. That is the source's invocation policy, not a portable guarantee across agent hosts. The source itself distinguishes canonical Cursor behavior and a generated Claude adapter. A plain `SKILL.md` copy does not establish equivalent behavior in Codex.

Two specific collisions deserve explicit names. pstack `unslop` edits **prose**, while Matt Pocock's `unslop` cleans **code**. pstack `tdd` is primarily a practical bug-regression workflow; another collection's identically named skill may cover test-first feature development. Compare capability and trigger boundaries, not names alone.

The Multi-phase plan playbook prescribes ten live verification lanes plus performance gates per PR, and depends on control skills from `cursor-team-kit`. This is a substantial process and runtime cost, not a general quality guarantee. The Eval playbook's blinding and transcript inspection are useful methods, but their presence does not prove that every release was behaviorally evaluated.

## Inventory

| Skill | One-line purpose | Decision | Personal destination |
| --- | --- | --- | --- |
| [architect](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/architect/SKILL.md) | Explore competing interfaces and type sketches before filling in an implementation. | adapt | api-design |
| [arena](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/arena/SKILL.md) | Generate independent solutions to one brief, compare them, and integrate selected strengths. | profile | api-design |
| [automate-me](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/automate-me/SKILL.md) | Draft or update a personal working-style skill using repeated transcript signals and user choices. | adapt | skill-maintenance |
| [benchmark-checklist](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/benchmark-checklist/SKILL.md) | Check that performance comparisons measure correct work under comparable conditions. | adapt | verify-change |
| [blast-radius](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/blast-radius/SKILL.md) | Trace effects beyond a diff and test the assumption on which its safety depends. | adapt | review |
| [bro](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/bro/SKILL.md) | Restate the previous reply in clearer everyday language. | reference | docs |
| [correct](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/correct/SKILL.md) | Turn repeated agent mistakes into structural checks and demonstrate that the checks catch them. | adapt | skill-maintenance |
| [create-formal-verification-skill](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/create-formal-verification-skill/SKILL.md) | Create a reusable property check tied to real code and demonstrate its ability to catch a broken variant. | profile | verify-change |
| [create-verification-skill](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/create-verification-skill/SKILL.md) | Generate and run project-specific launch, drive, evidence, and cleanup instructions. | adapt | verify-change |
| [figure-it-out](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/figure-it-out/SKILL.md) | Design and execute a bounded hypothesis-driven workflow for a large task without a suitable existing playbook. | adapt | change-plan |
| [how](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/how/SKILL.md) | Explain current subsystem behavior and ownership from code evidence. | adapt | docs |
| [in-your-own-words](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/in-your-own-words/SKILL.md) | Restate the user's intended outcome and the problem it addresses. | reference | start |
| [interrogate](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/interrogate/SKILL.md) | Have adversarial reviewers try to reproduce failures in a proposed change. | adapt | review |
| [ketchup](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/ketchup/SKILL.md) | Summarize this chat's progress and give the user enough context to resolve outstanding decisions. | adapt | handoff |
| [ketchup-video](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/ketchup-video/SKILL.md) | Render a visual catch-up as a short subtitled video. | profile | handoff |
| [maintain-formal-verification-skill](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/maintain-formal-verification-skill/SKILL.md) | Reconcile formal checks with changed code and distinguish model drift from product defects. | profile | verify-change |
| [maintain-verification-skill](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/maintain-verification-skill/SKILL.md) | Check that a project's verification instructions and feature map still match the live app. | adapt | skill-maintenance |
| [make-bot-ui](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/make-bot-ui/SKILL.md) | Build a local web UI that wakes a Grok Bot through a protected webhook and Tailscale. | profile | Optional integration/orchestration only |
| [no-comments](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/no-comments/SKILL.md) | Use a specialist reviewer to remove comments and replace claimed constraints with code or checks. | reject | simplify |
| [poteto-help](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/poteto-help/SKILL.md) | Explain pstack setup and route users to its skills and playbooks. | reference | start |
| [poteto-mode](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/poteto-mode/SKILL.md) | Route substantial work through pstack playbooks, principles, specialist agents, and verification routines. | reject | start |
| [principle-attack-the-premise](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/principle-attack-the-premise/SKILL.md) | Test a shared assumption after repeated fixes based on it fail. | adapt | debug |
| [principle-boundary-discipline](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/principle-boundary-discipline/SKILL.md) | Validate external inputs at boundaries and keep domain operations independent of framework wiring. | adapt | api-design |
| [principle-build-the-lever](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/principle-build-the-lever/SKILL.md) | Create a rerunnable tool for a nontrivial transformation or verification task. | adapt | change-plan |
| [principle-encode-lessons-in-structure](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/principle-encode-lessons-in-structure/SKILL.md) | Replace repeated prose corrections with enforceable checks where practical. | adapt | skill-maintenance |
| [principle-exhaust-the-design-space](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/principle-exhaust-the-design-space/SKILL.md) | Compare multiple prototypes for a novel interface or architecture decision. | profile | prototype |
| [principle-experience-first](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/principle-experience-first/SKILL.md) | Weigh user and maintainer experience when choosing product scope and design details. | reference | ui-review |
| [principle-explain-the-number](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/principle-explain-the-number/SKILL.md) | Identify what a measured result represents before using it to decide or claim improvement. | adapt | verify-change |
| [principle-fix-root-causes](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/principle-fix-root-causes/SKILL.md) | Trace a failure to the first incorrect decision and distinguish valid edge cases from impossible states. | adapt | debug |
| [principle-foundational-thinking](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/principle-foundational-thinking/SKILL.md) | Choose useful data structures and isolation boundaries before implementing dependent behavior. | adapt | domain-model |
| [principle-guard-the-context-window](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/principle-guard-the-context-window/SKILL.md) | Keep large investigations bounded and pass summaries instead of repeated raw payloads. | reference | handoff |
| [principle-laziness-protocol](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/principle-laziness-protocol/SKILL.md) | Prefer the smallest adequate change and avoid speculative layers or duplicated decisions. | adapt | minimalist |
| [principle-make-operations-idempotent](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/principle-make-operations-idempotent/SKILL.md) | Design retryable state changes to reconcile partial progress and converge safely. | adapt | api-design |
| [principle-migrate-callers-then-delete-legacy-apis](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/principle-migrate-callers-then-delete-legacy-apis/SKILL.md) | Migrate owned internal callers and remove the old API when coordinated breakage is acceptable. | profile | change-plan |
| [principle-minimize-reader-load](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/principle-minimize-reader-load/SKILL.md) | Reduce unnecessary indirection and hidden mutable state while preserving useful boundaries. | adapt | simplify |
| [principle-model-the-domain](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/principle-model-the-domain/SKILL.md) | Use a data model that encodes state, ownership, and invariants instead of scattered conditionals. | adapt | domain-model |
| [principle-never-block-on-the-human](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/principle-never-block-on-the-human/SKILL.md) | Proceed on authorized reversible execution decisions while reserving product choices for the user. | adapt | start |
| [principle-outcome-oriented-execution](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/principle-outcome-oriented-execution/SKILL.md) | Allow planned temporary breakage inside a bounded migration while verifying defined phase boundaries. | profile | change-plan |
| [principle-prove-it-works](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/principle-prove-it-works/SKILL.md) | Check the actual requested artifact or behavior before reporting success. | adapt | verify-change |
| [principle-redesign-from-first-principles](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/principle-redesign-from-first-principles/SKILL.md) | Reconsider the whole design when a new requirement exposes a structural mismatch. | reject | api-design |
| [principle-separate-before-serializing-shared-state](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/principle-separate-before-serializing-shared-state/SKILL.md) | Give concurrent actors independent mutable outputs before introducing shared-state coordination. | adapt | api-design |
| [principle-sequence-verifiable-units](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/principle-sequence-verifiable-units/SKILL.md) | Break multi-step work into checked increments that make failures easy to localize. | adapt | change-plan |
| [principle-subtract-before-you-add](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/principle-subtract-before-you-add/SKILL.md) | Remove complexity relevant to the requested change before extending it. | adapt | minimalist |
| [principle-test-behavior-not-implementation](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/principle-test-behavior-not-implementation/SKILL.md) | Use tests that detect broken observable behavior while tolerating internal refactors. | adapt | tdd |
| [principle-type-system-discipline](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/principle-type-system-discipline/SKILL.md) | Use domain types, parsed boundaries, and exhaustive variants to prevent representable mistakes. | adapt | api-design |
| [recall](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/recall/SKILL.md) | Rebuild recent topic-specific work context from scoped chat history and current artifact state. | adapt | handoff |
| [reflect](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/reflect/SKILL.md) | Review a session for durable skill improvements and separate prompt edits from structural fixes. | adapt | skill-maintenance |
| [setup-pstack](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/setup-pstack/SKILL.md) | Configure pstack model roles and reasoning budgets in an always-applied Cursor rule. | profile | Optional integration/orchestration only |
| [sharpen](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/sharpen/SKILL.md) | Rewrite a task for deeper professional rigor while keeping its scope unchanged. | reference | change-plan |
| [show-me-your-work](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/show-me-your-work/SKILL.md) | Maintain an evidence-linked decision log and audit it against the actual run. | adapt | handoff |
| [statechart](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/statechart/SKILL.md) | Check a bounded TLA+ model and explain invariant violations as state paths and Mermaid charts. | profile | verify-change |
| [swarm](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/swarm/SKILL.md) | Run parallel scoped workers and aggregate verified coverage or race results. | profile | Optional integration/orchestration only |
| [tdd](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/tdd/SKILL.md) | Write and run a focused failing regression check before a bug fix when a practical test path exists. | adapt | tdd |
| [teach](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/teach/SKILL.md) | Explain what a subsystem does and why in a learner-paced account. | adapt | docs |
| [technical-writing](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/technical-writing/SKILL.md) | Write task-focused technical documents with concrete terms and unambiguous instructions. | adapt | docs |
| [typescript-best-practices](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/typescript-best-practices/SKILL.md) | Apply domain typing, runtime boundary parsing, and behavioral-test guidance to TypeScript. | profile | api-design |
| [unslop](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/unslop/SKILL.md) | Edit prose to remove filler, unsupported claims, jargon, and repetitive machine-like phrasing. | adapt | docs |
| [why](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/why/SKILL.md) | Investigate historical design motives using code anchors and available primary records. | adapt | research |

## Simulated review of every skill

### architect

[Source at the reviewed commit](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/architect/SKILL.md). Explore competing interfaces and type sketches before filling in an implementation.

- **Practitioner.** Caller-first sketches and interface-depth comparison can expose awkward contracts before code grows.
- **Skeptic.** A design request becomes implementation by default, and every function boundary can trigger two models and several prerequisite skills.
- **Evaluator.** Give it a design-only request and a small signature change; fail if it implements the first or launches unnecessary panels for the second.
- **Consensus.** Keep caller examples and alternative interface shapes; retain the user's design-only scope and use parallel candidates only when the decision earns their cost.

Decision: **adapt**. Destination: `api-design`. Overlap: `design-an-interface`, `codebase-design`, `api-design`, `arena`. Dependencies: how, why, arena, Cursor Task, per-role model config.

### arena

[Source at the reviewed commit](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/arena/SKILL.md). Generate independent solutions to one brief, compare them, and integrate selected strengths.

- **Practitioner.** Independent candidates and a held-back rubric can reveal alternatives a single solution misses.
- **Skeptic.** Multiple agents and an enforced different-family judge are costly and unavailable in some harnesses; convergence is not independent proof.
- **Evaluator.** Compare a fixed design task with one versus two candidates; grade outcome blindly and include total latency and cost.
- **Consensus.** Offer as an optional design experiment with isolated outputs, explicit budget, and real verification; do not make a panel the default for ordinary edits.

Decision: **profile**. Destination: `api-design`. Overlap: `design-an-interface`, `simulate-discussion`, `swarm`. Dependencies: Cursor Task, multiple model families, worktrees, poteto-mode.

### automate-me

[Source at the reviewed commit](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/automate-me/SKILL.md). Draft or update a personal working-style skill using repeated transcript signals and user choices.

- **Practitioner.** Workspace scoping and evidence across multiple time slices reduce one-conversation overfitting.
- **Skeptic.** Transcript formats and Cursor authoring tools are host-specific; the flow also commits and opens a PR even when the user only asked for a draft.
- **Evaluator.** Seed repeated preferences, a contradictory one-off, and an unrelated private workspace; verify the draft uses only the supported in-scope signals and does not publish.
- **Consensus.** Keep scoped evidence collection and user correction; use host-native history access, separate preference agreement from routing tests, and preserve draft-only intent.

Decision: **adapt**. Destination: `skill-maintenance`. Overlap: `reflect`, `skill-creator`, `personal-mode`. Dependencies: Cursor transcripts, AskQuestion, create-skill, unslop, git PR tooling.

### benchmark-checklist

[Source at the reviewed commit](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/benchmark-checklist/SKILL.md). Check that performance comparisons measure correct work under comparable conditions.

- **Practitioner.** Checks for skipped work, errors, tuning, warmup, and realistic end-to-end impact catch misleading speed claims.
- **Skeptic.** Fixed five-run and limiter requirements can overburden exploratory measurements, and Unix diagnostic commands are not portable.
- **Evaluator.** Supply a fast no-op benchmark, asymmetric cache states, and noisy samples; reject unsupported winners and preserve an honest inconclusive verdict.
- **Consensus.** Keep correctness, comparable configurations, repetitions, spread, and practical relevance; scale effort to the decision and adapt platform tools.

Decision: **adapt**. Destination: `verify-change`. Overlap: `principle-explain-the-number`, `performance-optimization`, `autoresearch`. Dependencies: runtime profilers, platform counters, benchmark harness.

### blast-radius

[Source at the reviewed commit](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/blast-radius/SKILL.md). Trace effects beyond a diff and test the assumption on which its safety depends.

- **Practitioner.** Pinned dependency source and wire-format consumers reveal breakage that symbol searches miss.
- **Skeptic.** Requiring a runnable proof for every concern can suppress valid static findings, and a single safety assumption may not cover a distributed change.
- **Evaluator.** Review a JSON-field rename with a consumer outside the edited language; require identification of the actual consumer and an honest proof level.
- **Consensus.** Add cross-boundary consumers and load-bearing assumptions to review; report static evidence and blocked reproductions without treating either as a pass.

Decision: **adapt**. Destination: `review`. Overlap: `review`, `interrogate`, `how`, `why`. Dependencies: git history, dependency source, real runtime, optional arena, unslop.

### bro

[Source at the reviewed commit](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/bro/SKILL.md). Restate the previous reply in clearer everyday language.

- **Practitioner.** A focused rewrite request can rescue an explanation that uses unexplained jargon.
- **Skeptic.** One sentence adds little specialized procedure and would compete with general prose instructions if installed automatically.
- **Evaluator.** Rewrite a technical reply containing units, negation, and an exact error; verify those facts survive.
- **Consensus.** Treat as a user-invoked phrasing convenience or a docs reference, not another default engineering skill.

Decision: **reference**. Destination: `docs`. Overlap: `unslop`, `technical-writing`, `in-your-own-words`. Dependencies: none beyond the agent.

### correct

[Source at the reviewed commit](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/correct/SKILL.md). Turn repeated agent mistakes into structural checks and demonstrate that the checks catch them.

- **Practitioner.** Grouping repeated failures and reproducing them against a guardrail can prevent prompt instructions from accumulating without effect.
- **Skeptic.** The fixed architecture-first hierarchy can cause broad refactors, and the body immediately fixes classes and changes agent rules.
- **Evaluator.** Provide two repeated import mistakes and one unrelated failure; require the smallest effective check, a failing mutation, and no unrelated redesign.
- **Consensus.** Adopt evidence-linked prevention with the least disruptive mechanism; a correction is evidence to assess, not authority for a repository-wide cleanup.

Decision: **adapt**. Destination: `skill-maintenance`. Overlap: `reflect`, `principle-encode-lessons-in-structure`, `code-quality`. Dependencies: git/review history, local CI tooling, agent instruction file.

### create-formal-verification-skill

[Source at the reviewed commit](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/create-formal-verification-skill/SKILL.md). Create a reusable property check tied to real code and demonstrate its ability to catch a broken variant.

- **Practitioner.** Code-to-model mapping, bounds, counterexamples, and mutation checks provide stronger evidence for hard concurrency or invariant bugs.
- **Skeptic.** A hand model can omit real behavior, installation cost may be high, and generated instructions depend on statechart for TLA+ results.
- **Evaluator.** Use a two-actor double-claim race; compare model transitions to code atomicity and require the broken code variant to fail.
- **Consensus.** Use only for a named high-value invariant; preserve assumptions, state bounds, and the distinction between proof of a model and proof of production behavior.

Decision: **profile**. Destination: `verify-change`. Overlap: `statechart`, `maintain-formal-verification-skill`, `property-based-testing`. Dependencies: model checker/prover/SMT tool, tool installation, generated project skill, statechart for TLA+.

### create-verification-skill

[Source at the reviewed commit](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/create-verification-skill/SKILL.md). Generate and run project-specific launch, drive, evidence, and cleanup instructions.

- **Practitioner.** A reusable user-path harness with readiness, isolation, and surviving evidence is a distinctive operational contribution.
- **Skeptic.** It mandates Cursor paths and a feature-map structure, and may drift into fixing startup unrelated to the requested generator task.
- **Evaluator.** Generate against an app with slow initialization and a failing drive; require usable readiness, correct ownership, cleanup, and preserved evidence.
- **Consensus.** Keep real commands, observable results, process ownership, and a demonstrated run; use the target agent's native skill location and bound startup repairs to authorized work.

Decision: **adapt**. Destination: `verify-change`. Overlap: `evidence-driven-testing`, `verify-change`, `maintain-verification-skill`. Dependencies: existing app harness or browser/PTY/HTTP driver, project runtime, maintain-verification-skill.

### figure-it-out

[Source at the reviewed commit](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/figure-it-out/SKILL.md). Design and execute a bounded hypothesis-driven workflow for a large task without a suitable existing playbook.

- **Practitioner.** A falsifiable completion predicate, smallest-change experiments, and an audit trail can make unattended work reviewable.
- **Skeptic.** Mandatory rigor biased high, tool-building, architecture panels, and audit machinery can overwhelm otherwise clear changes.
- **Evaluator.** Give it a mechanical migration and an uncertain large change; grade whether it chooses different rigor and stops at a concrete predicate.
- **Consensus.** Keep scope, success criteria, hypotheses, checkpoints, and honest unresolved outcomes; remove the universal orchestration sequence and respect plan-only requests.

Decision: **adapt**. Destination: `change-plan`. Overlap: `autoresearch`, `change-plan`, `show-me-your-work`, `poteto-mode`. Dependencies: poteto-mode, architect, arena, worktrees, show-me-your-work, optional subagents.

### how

[Source at the reviewed commit](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/how/SKILL.md). Explain current subsystem behavior and ownership from code evidence.

- **Practitioner.** Separating current runtime mechanics from historical motivation makes explanations easier to verify.
- **Skeptic.** Even a simple module forces an explainer subagent, and prescribed model families create unnecessary runtime dependencies.
- **Evaluator.** Ask about a one-function utility and a cross-service flow; require accurate citations without mandatory fan-out for the small question.
- **Consensus.** Keep code-grounded ownership and flow explanations; explore directly for narrow questions and delegate only when scope supports it.

Decision: **adapt**. Destination: `docs`. Overlap: `docs`, `project-wiki`, `teach`, `why`. Dependencies: Cursor Task, per-role model config, explorer/explainer reference prompts.

### in-your-own-words

[Source at the reviewed commit](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/in-your-own-words/SKILL.md). Restate the user's intended outcome and the problem it addresses.

- **Practitioner.** An early intent restatement can expose a consequential misunderstanding cheaply.
- **Skeptic.** It contains no task-specific method and can produce repetitive confirmations across turns.
- **Evaluator.** Continue an already-agreed implementation after a follow-up; fail if it restarts scope negotiation or alters the goal.
- **Consensus.** Put one brief assumption check in routing when useful; do not install a standalone always-on skill for this sentence.

Decision: **reference**. Destination: `start`. Overlap: `start`, `grill-idea`. Dependencies: none beyond the agent.

### interrogate

[Source at the reviewed commit](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/interrogate/SKILL.md). Have adversarial reviewers try to reproduce failures in a proposed change.

- **Practitioner.** Keeping reproducible defects and rerunning their commands filters speculative review noise.
- **Skeptic.** Only-run findings exclude sound static defects, inaccessible deployment risks, and designs that cannot yet execute.
- **Evaluator.** Review a runnable defect plus an obvious statically provable security flaw that cannot be exercised locally; require both with distinct evidence labels.
- **Consensus.** Use adversarial repros for consequential changes, while preserving valid static evidence and reporting inaccessible checks explicitly; review requests remain read-only.

Decision: **adapt**. Destination: `review`. Overlap: `review`, `blast-radius`, `arena`, `code-review`. Dependencies: arena, Cursor Task, worktrees, runnable target, multiple models.

### ketchup

[Source at the reviewed commit](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/ketchup/SKILL.md). Summarize this chat's progress and give the user enough context to resolve outstanding decisions.

- **Practitioner.** It checks live artifact status and keeps user-owned decisions distinct from work the agent can continue.
- **Skeptic.** Rigid word limits and mandatory visuals may add formatting effort or obscure details in technical handoffs.
- **Evaluator.** Seed completed work, a still-open PR, a stale earlier claim, and an outstanding decision; require an accurate self-contained catch-up.
- **Consensus.** Keep verified status, unfinished work, and decision context; scale format to the reader and preserve needed technical identifiers.

Decision: **adapt**. Destination: `handoff`. Overlap: `handoff`, `recall`, `bro`. Dependencies: chat context, git/PR status, bro, optional visual tools.

### ketchup-video

[Source at the reviewed commit](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/ketchup-video/SKILL.md). Render a visual catch-up as a short subtitled video.

- **Practitioner.** A video can help an asynchronous stakeholder understand visual changes quickly.
- **Skeptic.** Rendering and frame verification are expensive for a status update, and no video helper is shipped in the skill body.
- **Evaluator.** Use a visual before/after task and check subtitle legibility, timing, factual accuracy, and fallback when rendering fails.
- **Consensus.** Offer only on an explicit video-summary request with suitable artifacts; normal catch-ups stay in text.

Decision: **profile**. Destination: `handoff`. Overlap: `ketchup`, `launch-video`, `presentations`. Dependencies: ketchup, video renderer, source screenshots/recordings.

### maintain-formal-verification-skill

[Source at the reviewed commit](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/maintain-formal-verification-skill/SKILL.md). Reconcile formal checks with changed code and distinguish model drift from product defects.

- **Practitioner.** Sync commits, code-linked transitions, mutation tests, and separate bug outcomes address stale proofs that still pass.
- **Skeptic.** Reading all changes and installing verifiers is costly; a changed promise must not be inferred from a convenient passing test.
- **Evaluator.** Change an atomic operation into two steps without changing the model; require detection of stale verification and replay of its counterexample.
- **Consensus.** Keep as a targeted maintenance profile for existing formal checks, with verification-only edits and no weakened properties to make a run green.

Decision: **profile**. Destination: `verify-change`. Overlap: `create-formal-verification-skill`, `maintain-verification-skill`. Dependencies: existing formal verify skill, covered-code history, model checker/prover.

### maintain-verification-skill

[Source at the reviewed commit](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/maintain-verification-skill/SKILL.md). Check that a project's verification instructions and feature map still match the live app.

- **Practitioner.** Source coverage plus one coordinator driving the app can expose stale selectors, missing preconditions, and false success maps.
- **Skeptic.** One agent per feature and every-feature live coverage may be excessive; it also opens a PR automatically for corrections.
- **Evaluator.** Use a stale selector, a genuine product regression, and an unreachable entitlement; require distinct drift, bug, and blocked outcomes with surviving evidence.
- **Consensus.** Adopt verification-only drift repair and explicit coverage gaps; scale sampling and delegation to changes and keep publishing within the maintenance authorization.

Decision: **adapt**. Destination: `skill-maintenance`. Overlap: `create-verification-skill`, `evidence-driven-testing`, `skill-maintenance`. Dependencies: existing verify skill/feature map, source readers, live app driver, git PR tooling.

### make-bot-ui

[Source at the reviewed commit](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/make-bot-ui/SKILL.md). Build a local web UI that wakes a Grok Bot through a protected webhook and Tailscale.

- **Practitioner.** Server-side secret handling and a harmless wake probe are useful for this exact integration.
- **Skeptic.** It assumes Cursor routine and secret-card tools, opens a network listener, installs Tailscale, and prescribes HTTP and authentication configuration.
- **Evaluator.** In a sandbox, verify the key never reaches browser output or logs and unavailable routine tools are reported instead of invented.
- **Consensus.** Keep upstream as a named integration profile; do not import its network or installation defaults into generic development workflows.

Decision: **profile**. No default personal skill destination. Overlap: `sites`, `automation`, `webhook-development`. Dependencies: Cursor Grok Bot routines, update_state, SendToUser secret-request, Tailscale, local server.

### no-comments

[Source at the reviewed commit](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/no-comments/SKILL.md). Use a specialist reviewer to remove comments and replace claimed constraints with code or checks.

- **Practitioner.** Reviewing stale narrative comments and encoding a real invariant can improve maintainability.
- **Skeptic.** The body directs deletion of ambiguous constraints and deletes a constraint comment even when an encoding is declined; it also depends on a custom reviewer.
- **Evaluator.** Give it an unverified external-platform constraint comment and deny the proposed encoding; any deletion or product change fails the case.
- **Consensus.** Reject the raw workflow; a bounded simplification skill may remove demonstrably obsolete comments while preserving unresolved external constraints.

Decision: **reject**. Destination: `simplify`. Overlap: `simplify`, `code-simplifier`, `unslop`. Dependencies: Cursor comment-sicko subagent, how, why, architect, poteto-mode.

### poteto-help

[Source at the reviewed commit](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/poteto-help/SKILL.md). Explain pstack setup and route users to its skills and playbooks.

- **Practitioner.** The guide accurately distinguishes help questions, real work requests, playbooks, and missing dependencies.
- **Skeptic.** It is specific to one plugin and contains version-sensitive model, path, and UI guidance.
- **Evaluator.** Ask a help-only question and a work request; verify the first answers without starting the job and the second preserves the requested task.
- **Consensus.** Keep as pstack's own support reference; the personal pack needs its own small installation and routing guide.

Decision: **reference**. Destination: `start`. Overlap: `start`, `poteto-mode`, `setup-pstack`. Dependencies: pstack installed files, Cursor UI/Custom Modes, optional Claude adapter.

### poteto-mode

[Source at the reviewed commit](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/poteto-mode/SKILL.md). Route substantial work through pstack playbooks, principles, specialist agents, and verification routines.

- **Practitioner.** Its integrated playbooks, explicit verification, and fallback handling demonstrate a coherent personal engineering system.
- **Skeptic.** It broadly triggers architecture panels, comment removal, skill repair PRs, and external team-chat or ticket actions; it competes with the personal router and host authority.
- **Evaluator.** Run help-only, design-only, trivial-edit, and no-messaging cases; fail on implementation, unsolicited messages, heavy panels, or edits to unrelated skills.
- **Consensus.** Reject wholesale installation alongside the personal router; adapt only individually justified procedures and keep authorization and runtime decisions in the host.

Decision: **reject**. Destination: `start`. Overlap: `start`, `develop`, `finish`, `figure-it-out`. Dependencies: Cursor Task/poteto-agent, model rules, 23 playbooks, principle skills, cursor-team-kit, create-skill.

### principle-attack-the-premise

[Source at the reviewed commit](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/principle-attack-the-premise/SKILL.md). Test a shared assumption after repeated fixes based on it fail.

- **Practitioner.** A direct discriminating observation can end repeated patching of the wrong mechanism.
- **Skeptic.** A fixed two-failure trigger may be too late or too early, and linked principles create needless loading overhead.
- **Evaluator.** Supply two fixes that assume stale cache data while the fault is a wrong key; require a test that distinguishes the premise.
- **Consensus.** Merge a compact premise-checking step into diagnosis, triggered by evidence rather than a compulsory failure count.

Decision: **adapt**. Destination: `debug`. Overlap: `debug`, `principle-fix-root-causes`, `principle-build-the-lever`. Dependencies: principle-build-the-lever, principle-fix-root-causes, principle-laziness-protocol.

### principle-boundary-discipline

[Source at the reviewed commit](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/principle-boundary-discipline/SKILL.md). Validate external inputs at boundaries and keep domain operations independent of framework wiring.

- **Practitioner.** Boundary parsing and explicit domain representations reduce repeated assumptions across callers.
- **Skeptic.** Trusting internal types unconditionally is unsafe with mutable state, casts, FFI, persistence, and runtime invariant changes.
- **Evaluator.** Inject malformed persisted data and a corrupted internal state through real boundaries; verify both receive proportionate handling.
- **Consensus.** Keep boundary parsing and ownership clarity; remove unconditional trust and mandatory pure-function extraction for every candidate.

Decision: **adapt**. Destination: `api-design`. Overlap: `code-structure`, `domain-model`, `typescript-best-practices`. Dependencies: typed boundary model, project architecture.

### principle-build-the-lever

[Source at the reviewed commit](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/principle-build-the-lever/SKILL.md). Create a rerunnable tool for a nontrivial transformation or verification task.

- **Practitioner.** A small script can make repeated work consistent and allow a reviewer to reproduce the result.
- **Skeptic.** The body requires a file for every nontrivial one-off, which can create more maintenance than the task deserves.
- **Evaluator.** Compare a three-file one-off and a hundred-file migration; require a tool only when rerun value exceeds setup cost.
- **Consensus.** Retain deterministic automation when repetition, fragility, or reviewability justifies it; do not require a new script as proof of diligence.

Decision: **adapt**. Destination: `change-plan`. Overlap: `autoresearch`, `principle-prove-it-works`, `skill-maintenance`. Dependencies: appropriate scripting runtime, optional delegate skill.

### principle-encode-lessons-in-structure

[Source at the reviewed commit](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/principle-encode-lessons-in-structure/SKILL.md). Replace repeated prose corrections with enforceable checks where practical.

- **Practitioner.** A type, lint, or invariant check can prevent recurrence even when an agent skips a prompt.
- **Skeptic.** A second instruction alone is weak evidence for a permanent guardrail, and some errors require contextual judgment.
- **Evaluator.** Replay a repeated failure against a proposed check and a legitimate exception; require rejection of the failure without breaking the exception.
- **Consensus.** Use observed recurrence and a narrow failing example to justify structural enforcement; keep judgment-dependent guidance concise.

Decision: **adapt**. Destination: `skill-maintenance`. Overlap: `correct`, `reflect`, `code-quality`. Dependencies: local type/lint/runtime/test mechanism.

### principle-exhaust-the-design-space

[Source at the reviewed commit](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/principle-exhaust-the-design-space/SKILL.md). Compare multiple prototypes for a novel interface or architecture decision.

- **Practitioner.** Concrete alternatives can reveal interaction and structural tradeoffs that prose hides.
- **Skeptic.** Always building two or three candidates may waste time when an existing pattern or constraint already decides the shape.
- **Evaluator.** Compare a genuinely uncertain interaction and a prescribed component reuse; require alternatives only for the unresolved decision.
- **Consensus.** Offer targeted competing prototypes when the result can change a consequential choice; evidence should settle the fork rather than multiply artifacts.

Decision: **profile**. Destination: `prototype`. Overlap: `prototype`, `design-an-interface`, `arena`. Dependencies: prototype runtime, optional independent candidates.

### principle-experience-first

[Source at the reviewed commit](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/principle-experience-first/SKILL.md). Weigh user and maintainer experience when choosing product scope and design details.

- **Practitioner.** It includes maintainers and library consumers in the definition of user, reducing implementation-only reasoning.
- **Skeptic.** Delight is subjective and can override accessibility, delivery limits, or an explicit user preference if treated as an absolute.
- **Evaluator.** Present polished motion that harms reduced-motion users and a smaller accessible option; require the latter when it meets the task.
- **Consensus.** Keep as a design decision lens tied to actual user needs; do not install a broad taste rule as an automatic mandate.

Decision: **reference**. Destination: `ui-review`. Overlap: `ui-review`, `journey-first-design`, `prototype`. Dependencies: product context, existing design system.

### principle-explain-the-number

[Source at the reviewed commit](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/principle-explain-the-number/SKILL.md). Identify what a measured result represents before using it to decide or claim improvement.

- **Practitioner.** Decision thresholds, noise, skipped work, and physical limits guard against persuasive but invalid metrics.
- **Skeptic.** Requiring a fully identified resource limiter for every evaluation result can be impossible and distract from a valid effect estimate.
- **Evaluator.** Provide a metric improved by omitted work and an effect smaller than run variation; require rejection or an inconclusive verdict.
- **Consensus.** Retain decision criteria, task correctness, run spread, and confounder checks; distinguish explanatory uncertainty from invalid measurement.

Decision: **adapt**. Destination: `verify-change`. Overlap: `benchmark-checklist`, `autoresearch`, `plugin-eval`. Dependencies: benchmark-checklist, measurement artifacts, profiles/counters where relevant.

### principle-fix-root-causes

[Source at the reviewed commit](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/principle-fix-root-causes/SKILL.md). Trace a failure to the first incorrect decision and distinguish valid edge cases from impossible states.

- **Practitioner.** The explicit test for whether a triggering state is legitimate helps separate proper handling from symptom masking.
- **Skeptic.** The body invites fixing every matching instance and declares paragraph-long workaround comments evidence that code is wrong.
- **Evaluator.** Use one real invalid transition plus a legitimate missing record; require a root fix for the first and supported handling for the second without unrelated edits.
- **Consensus.** Merge causal tracing and state legitimacy into diagnosis; inspect analogous sites but change only authorized instances supported by evidence.

Decision: **adapt**. Destination: `debug`. Overlap: `debug`, `diagnosing-bugs`, `principle-attack-the-premise`. Dependencies: reproduction, observability, affected-source access.

### principle-foundational-thinking

[Source at the reviewed commit](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/principle-foundational-thinking/SKILL.md). Choose useful data structures and isolation boundaries before implementing dependent behavior.

- **Practitioner.** Access patterns and concurrent ownership can expose a poor shape before callers depend on it.
- **Skeptic.** Scaffold-first and remove-dead-code-first rules can expand scope or impose infrastructure before a useful vertical slice.
- **Evaluator.** Give a local bug and a new stateful workflow; require no infrastructure setup for the former and a justified state model for the latter.
- **Consensus.** Keep data-shape and shared-state reasoning; let a thin verifiable slice determine sequencing and preserve unrelated code.

Decision: **adapt**. Destination: `domain-model`. Overlap: `domain-model`, `api-design`, `change-plan`. Dependencies: project types, access patterns, concurrency context.

### principle-guard-the-context-window

[Source at the reviewed commit](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/principle-guard-the-context-window/SKILL.md). Keep large investigations bounded and pass summaries instead of repeated raw payloads.

- **Practitioner.** Scoped reads and compact evidence pointers conserve room for decisions in long tasks.
- **Skeptic.** Defaulting bulk work to subagents can violate host limits and merely move rather than reduce reading cost.
- **Evaluator.** Run an investigation with large logs and no delegation; require bounded relevant extracts and no loss of decisive evidence.
- **Consensus.** Use as a compact operational reference in long-task handoffs; delegation remains a host and task choice.

Decision: **reference**. Destination: `handoff`. Overlap: `handoff`, `swarm`, `how`. Dependencies: optional subagents, scoped file/log search.

### principle-laziness-protocol

[Source at the reviewed commit](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/principle-laziness-protocol/SKILL.md). Prefer the smallest adequate change and avoid speculative layers or duplicated decisions.

- **Practitioner.** It encourages one source of truth and resists abstractions that add no current capability.
- **Skeptic.** Fewer lines are an unreliable quality metric and can reward compressed or under-specified behavior.
- **Evaluator.** Offer a terse change that drops an edge case and a slightly longer complete fix; require the complete fix.
- **Consensus.** Retain minimal scope and justified abstractions; evaluate behavior and maintainability rather than line count.

Decision: **adapt**. Destination: `minimalist`. Overlap: `minimalist`, `simplify`, `Ponytail`. Dependencies: none beyond the agent.

### principle-make-operations-idempotent

[Source at the reviewed commit](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/principle-make-operations-idempotent/SKILL.md). Design retryable state changes to reconcile partial progress and converge safely.

- **Practitioner.** Crash-point and repeat-run questions make durable commands and synchronizers easier to reason about.
- **Skeptic.** Not every external effect is repeatable, and local reconciliation cannot create exactly-once semantics without a remote protocol.
- **Evaluator.** Interrupt a file update before rename and repeat a remote creation after an unknown result; require recovery without duplicate effects.
- **Consensus.** Keep observed-state reconciliation and explicit idempotency keys where supported; document non-repeatable boundaries rather than promising universal idempotence.

Decision: **adapt**. Destination: `api-design`. Overlap: `durable-execution`, `api-design`, `skill-maintenance`. Dependencies: state ownership, atomic update or compare-and-swap where applicable.

### principle-migrate-callers-then-delete-legacy-apis

[Source at the reviewed commit](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/principle-migrate-callers-then-delete-legacy-apis/SKILL.md). Migrate owned internal callers and remove the old API when coordinated breakage is acceptable.

- **Practitioner.** Removing redundant internal entry points can prevent future callers from copying a deprecated path.
- **Skeptic.** The description is broader than the body's compatibility exclusions, and simultaneous migration can be unsuitable for large deployments.
- **Evaluator.** Include an unknown external caller and a closed internal module; require a compatibility investigation before deletion in the former.
- **Consensus.** Use only for known internal callers within the authorized migration and deployment boundary; retain compatibility when ownership or rollout requires it.

Decision: **profile**. Destination: `change-plan`. Overlap: `deprecation-and-migration`, `simplify`, `change-plan`. Dependencies: complete caller inventory, controlled rollout boundary.

### principle-minimize-reader-load

[Source at the reviewed commit](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/principle-minimize-reader-load/SKILL.md). Reduce unnecessary indirection and hidden mutable state while preserving useful boundaries.

- **Practitioner.** Tracing layers and state ownership provides a better maintenance lens than line count alone.
- **Skeptic.** Automatic inlining of one-caller wrappers can destroy a useful policy, test seam, or abstraction boundary.
- **Evaluator.** Review a pass-through wrapper and a one-caller adapter that hides policy; remove only the former if behavior remains intact.
- **Consensus.** Use layer and state costs to justify a scoped simplification; do not infer that caller count proves a module is unnecessary.

Decision: **adapt**. Destination: `simplify`. Overlap: `codebase-design`, `code-simplifier`, `complexity`. Dependencies: affected callers, behavioral checks.

### principle-model-the-domain

[Source at the reviewed commit](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/principle-model-the-domain/SKILL.md). Use a data model that encodes state, ownership, and invariants instead of scattered conditionals.

- **Practitioner.** The body explicitly allows boring local code and asks whether a new structure removes actual invalid states or duplicated rules.
- **Skeptic.** Introducing a state machine or registry can still become premature architecture when the current behavior is small.
- **Evaluator.** Give an impossible boolean combination and a two-case local conditional; require a model for the first only when it reduces real complexity.
- **Consensus.** Merge into domain modeling with concrete allowed and forbidden states and a small-change counterexample.

Decision: **adapt**. Destination: `domain-model`. Overlap: `domain-model`, `domain-modeling`, `complexity`. Dependencies: domain examples, access patterns, existing project types.

### principle-never-block-on-the-human

[Source at the reviewed commit](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/principle-never-block-on-the-human/SKILL.md). Proceed on authorized reversible execution decisions while reserving product choices for the user.

- **Practitioner.** It reduces needless confirmation loops during implementation already requested by the user.
- **Skeptic.** Reversibility does not itself grant permission, and the examples blur local edits with external actions that affect others.
- **Evaluator.** Give a reversible but unrequested issue update and an authorized local fix; require only the fix to proceed.
- **Consensus.** Keep action within the user's existing scope and authority; ask about consequential unresolved intent and report reasonable execution assumptions.

Decision: **adapt**. Destination: `start`. Overlap: `start`, `autonomy guidance`. Dependencies: conversation authorization, host approval policy.

### principle-outcome-oriented-execution

[Source at the reviewed commit](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/principle-outcome-oriented-execution/SKILL.md). Allow planned temporary breakage inside a bounded migration while verifying defined phase boundaries.

- **Practitioner.** It can avoid disposable compatibility code during a private, coordinated rewrite.
- **Skeptic.** Unstable intermediate states can hide causal failures and conflict with sequential verifiable-unit guidance or deployment needs.
- **Evaluator.** Plan a private module rewrite and a rolling service migration; require different stability boundaries and recovery paths.
- **Consensus.** Use only with explicit reversible phase boundaries and required checks; preserve deployability and bisectability where the project needs them.

Decision: **profile**. Destination: `change-plan`. Overlap: `change-plan`, `principle-sequence-verifiable-units`, `migration`. Dependencies: isolated branch, rollback/verification boundaries.

### principle-prove-it-works

[Source at the reviewed commit](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/principle-prove-it-works/SKILL.md). Check the actual requested artifact or behavior before reporting success.

- **Practitioner.** Direct observation and rerunnable checks reduce false completion claims based on agent summaries or compilation alone.
- **Skeptic.** A real production action may be unauthorized or unavailable, and suspecting the observation method first is a heuristic rather than a rule.
- **Evaluator.** Provide a passing build with broken user behavior and an inaccessible live environment; require failure for the first and explicit limits for the second.
- **Consensus.** Keep outcome-specific evidence and honest unverified gaps; use the closest permitted check without claiming it proves inaccessible behavior.

Decision: **adapt**. Destination: `verify-change`. Overlap: `verify-change`, `evidence-driven-testing`, `show-me-your-work`. Dependencies: task-appropriate executable or artifact inspection.

### principle-redesign-from-first-principles

[Source at the reviewed commit](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/principle-redesign-from-first-principles/SKILL.md). Reconsider the whole design when a new requirement exposes a structural mismatch.

- **Practitioner.** Imagining the requirement as foundational can reveal an abstraction that repeated patches obscure.
- **Skeptic.** The broad trigger applies to every new requirement and directs propagation through all references, conflicting with surgical maintenance.
- **Evaluator.** Give a narrow compatible requirement and an explicit architecture redesign; fail if the narrow change becomes a broad rewrite.
- **Consensus.** Reject as an automatic rule; retain the question as an optional architecture lens only after a demonstrated mismatch and explicit redesign scope.

Decision: **reject**. Destination: `api-design`. Overlap: `api-design`, `architect`, `codebase-design`. Dependencies: affected-design understanding, authorized refactor scope.

### principle-separate-before-serializing-shared-state

[Source at the reviewed commit](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/principle-separate-before-serializing-shared-state/SKILL.md). Give concurrent actors independent mutable outputs before introducing shared-state coordination.

- **Practitioner.** Per-worker ownership prevents avoidable file and branch races, and real shared invariants call for structural synchronization.
- **Skeptic.** Separate files do not eliminate a shared business invariant, and fragmentation can create inconsistent reporting or merge loss.
- **Evaluator.** Run concurrent independent report writers and two actors claiming one resource; require isolation for the first and atomic coordination for the second.
- **Consensus.** Keep the ownership-first question and enforce genuine shared invariants with the right atomic operation or coordinator.

Decision: **adapt**. Destination: `api-design`. Overlap: `code-structure`, `swarm`, `principle-make-operations-idempotent`. Dependencies: concurrency model, atomic persistence/locks when sharing is necessary.

### principle-sequence-verifiable-units

[Source at the reviewed commit](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/principle-sequence-verifiable-units/SKILL.md). Break multi-step work into checked increments that make failures easy to localize.

- **Practitioner.** Verification between meaningful units reduces the search space when a migration breaks.
- **Skeptic.** Mandatory per-edit checks and a rebase before execution can waste effort or disrupt an assigned checkout; failing-test-only commits may violate project policy.
- **Evaluator.** Use a mechanical batch and a risky staged migration; require checks at meaningful boundaries and preservation of the user's worktree.
- **Consensus.** Keep coherent checked increments and causal evidence; follow repository commit policy and avoid unsolicited rebases or per-line ceremony.

Decision: **adapt**. Destination: `change-plan`. Overlap: `change-plan`, `tdd`, `principle-outcome-oriented-execution`. Dependencies: targeted checks, git history only when delivery is authorized.

### principle-subtract-before-you-add

[Source at the reviewed commit](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/principle-subtract-before-you-add/SKILL.md). Remove complexity relevant to the requested change before extending it.

- **Practitioner.** Eliminating a redundant path can make the requested implementation smaller and easier to verify.
- **Skeptic.** The source says to remove dead code first broadly, which can turn a small task into unrelated cleanup.
- **Evaluator.** Seed unrelated dead code next to a requested fix; require it to remain untouched unless removal is necessary for the fix.
- **Consensus.** Constrain subtraction to code made obsolete by the requested change or explicitly authorized cleanup.

Decision: **adapt**. Destination: `minimalist`. Overlap: `minimalist`, `simplify`, `Ponytail`. Dependencies: behavioral equivalence checks where code is removed.

### principle-test-behavior-not-implementation

[Source at the reviewed commit](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/principle-test-behavior-not-implementation/SKILL.md). Use tests that detect broken observable behavior while tolerating internal refactors.

- **Practitioner.** Its two imagined mutations expose tests that pass on omitted effects or fail on harmless restructuring.
- **Skeptic.** Deleting a test solely because it inspects an internal invariant may discard worthwhile safety evidence.
- **Evaluator.** Provide a payment effect test, a brittle private-call-order test, and a compile-time invariant test; distinguish the actual contract in each.
- **Consensus.** Adopt requirement-derived expectations, meaningful negative controls, and refactor tolerance; retain justified internal or structural invariants.

Decision: **adapt**. Destination: `tdd`. Overlap: `tdd`, `diagnosing-bugs`, `plugin-eval`. Dependencies: project test runner, behavioral contract, optional mutation tools.

### principle-type-system-discipline

[Source at the reviewed commit](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/principle-type-system-discipline/SKILL.md). Use domain types, parsed boundaries, and exhaustive variants to prevent representable mistakes.

- **Practitioner.** Semantic identifiers and schema-derived shapes can move recurring errors into compiler feedback.
- **Skeptic.** Branding every primitive and trusting types after one parse can add ceremony or miss runtime mutation and invalid persisted data.
- **Evaluator.** Pass an OrderId where a UserId is required and inject malformed runtime data; require compile-time and runtime defenses at their actual boundaries.
- **Consensus.** Keep types that rule out concrete mistakes and derive authoritative shapes; use runtime checks where the execution model still permits invalid state.

Decision: **adapt**. Destination: `api-design`. Overlap: `typescript-best-practices`, `domain-model`, `codebase-design`. Dependencies: statically typed language, schema source, boundary parser.

### recall

[Source at the reviewed commit](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/recall/SKILL.md). Rebuild recent topic-specific work context from scoped chat history and current artifact state.

- **Practitioner.** Live PR and branch checks prevent an old transcript from being mistaken for current status.
- **Skeptic.** The fixed Cursor transcript path is host-specific and the default cross-source why sweep may overread unrelated records.
- **Evaluator.** Seed an old merged claim, a later revert, and private unrelated chats; require a current brief with topic and workspace fences.
- **Consensus.** Keep scoped history retrieval, provenance, and current-state checks; use the host's supported history access and search only sources needed for the question.

Decision: **adapt**. Destination: `handoff`. Overlap: `handoff`, `ketchup`, `why`, `project-wiki`. Dependencies: Cursor transcript format, why source investigators, git/gh, unslop.

### reflect

[Source at the reviewed commit](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/reflect/SKILL.md). Review a session for durable skill improvements and separate prompt edits from structural fixes.

- **Practitioner.** Existing-skill checks and routing failures versus body failures help avoid adding duplicate rules.
- **Skeptic.** It requires writable agent mode for investigators and files backlog items without waiting, even when the user only requested reflection.
- **Evaluator.** Use a transient tool outage, an unused skill, and a repeated misleading instruction; require different diagnoses and no unrequested tracker posts.
- **Consensus.** Keep evidence-linked narrow proposals and the distinction between routing, instruction, tooling, and execution failures; respect existing edit authorization and do not auto-post backlog.

Decision: **adapt**. Destination: `skill-maintenance`. Overlap: `automate-me`, `correct`, `skill-creator`. Dependencies: Cursor transcripts, three reviewers, synthesizer, create-skill, MCP lookups.

### setup-pstack

[Source at the reviewed commit](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/setup-pstack/SKILL.md). Configure pstack model roles and reasoning budgets in an always-applied Cursor rule.

- **Practitioner.** Detecting available model slugs avoids writing a configuration that cannot run.
- **Skeptic.** It writes user-wide Cursor configuration and hardcodes vendor role assumptions; its configuration is not a portable skills standard.
- **Evaluator.** Configure in a sandbox with a missing family and existing custom roles; require valid detected choices and preservation of intended overrides.
- **Consensus.** Use only when installing or configuring pstack for that host; personal portable skills should inherit host model choices.

Decision: **profile**. No default personal skill destination. Overlap: `poteto-mode`, `plugin setup`. Dependencies: Cursor Task model inventory, AskQuestion, ~/.cursor/rules/pstack-models.mdc.

### sharpen

[Source at the reviewed commit](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/sharpen/SKILL.md). Rewrite a task for deeper professional rigor while keeping its scope unchanged.

- **Practitioner.** Raw source material, named methods, and independent success evidence improve an under-specified brief.
- **Skeptic.** The four prompts can still expand a simple task or silently choose user-owned product decisions.
- **Evaluator.** Rewrite a narrow code review request; require a better evidence method without implementation or extra product scope.
- **Consensus.** Keep as an explicit prompt-refinement reference; existing deepen-prompt already covers this distinct activity.

Decision: **reference**. Destination: `change-plan`. Overlap: `deepen-prompt`, `in-your-own-words`. Dependencies: none beyond the agent.

### show-me-your-work

[Source at the reviewed commit](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/show-me-your-work/SKILL.md). Maintain an evidence-linked decision log and audit it against the actual run.

- **Practitioner.** Append-only corrections and evidence pointers make long unattended decisions reviewable after context is lost.
- **Skeptic.** A mandatory different-family review and exact TSV protocol add tooling cost, and logs can leak private artifacts when committed.
- **Evaluator.** Give a run with an abandoned approach and a false earlier success claim; require preserved history plus a correction supported by the transcript.
- **Consensus.** Adopt a small local decision trail for consequential long work, sanitized before sharing; make audit and review effort proportional and host-independent.

Decision: **adapt**. Destination: `handoff`. Overlap: `handoff`, `figure-it-out`, `autoresearch`. Dependencies: decision log helper or compatible writer, active transcript, optional cross-model reviewer.

### statechart

[Source at the reviewed commit](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/statechart/SKILL.md). Check a bounded TLA+ model and explain invariant violations as state paths and Mermaid charts.

- **Practitioner.** Shortest counterexample paths in domain language can make concurrency failures understandable to owners.
- **Skeptic.** The helper installs Java/TLC through mise, requires a TypeScript runtime and Pele rendering, and a chart can hide model bounds or lost transitions.
- **Evaluator.** Use a known race and a deliberately over-coarsened chart; require the violated invariant and reachable path to survive projection and replay against code.
- **Consensus.** Keep as an optional formal-analysis profile with declared tools, bounds, hidden transitions, and a code replay; do not treat a rendered model as product proof.

Decision: **profile**. Destination: `verify-change`. Overlap: `create-formal-verification-skill`, `visualize`, `Mermaid`. Dependencies: TypeScript runtime, mise, Java, TLC, network, Pele renderer.

### swarm

[Source at the reviewed commit](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/swarm/SKILL.md). Run parallel scoped workers and aggregate verified coverage or race results.

- **Practitioner.** Explicit selection rules, exact revisions, isolated outputs, and gap reporting reduce ambiguous delegation results.
- **Skeptic.** Cloud agents and model controls are host-specific, and a missing worker cannot simply be counted as clean coverage.
- **Evaluator.** Run three coverage slices with one dropout and a result from the wrong revision; require a visible gap and one bounded retry.
- **Consensus.** Keep as orchestration reference for authorized parallel work; adapt to native runtime, budget, and ownership rules instead of installing a second delegation policy.

Decision: **profile**. No default personal skill destination. Overlap: `arena`, `orchestrate`, `parallel-review`. Dependencies: Cursor Task, cloud agents by default, model config, isolated outputs.

### tdd

[Source at the reviewed commit](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/tdd/SKILL.md). Write and run a focused failing regression check before a bug fix when a practical test path exists.

- **Practitioner.** The skill preserves failing-before and passing-after evidence and explicitly rejects expensive mock-heavy test ceremony.
- **Skeptic.** Its narrow bug-fix scope differs from Matt's broader feature TDD, despite sharing the same name.
- **Evaluator.** Fix a deterministic local defect and a production-only integration issue; require a real red-green test for the first and explicit alternative evidence for the second.
- **Consensus.** Merge practical bug reproduction into one personal TDD skill and make feature-versus-bug scope clear in its trigger.

Decision: **adapt**. Destination: `tdd`. Overlap: `mattpocock/tdd`, `debug`, `evidence-driven-testing`. Dependencies: existing project test runner or closest executable reproduction.

### teach

[Source at the reviewed commit](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/teach/SKILL.md). Explain what a subsystem does and why in a learner-paced account.

- **Practitioner.** It preserves the distinction between current behavior and historical rationale and starts from the reader's need.
- **Skeptic.** It chains how and why even for many small questions and prescribes repeated diagrams or generated images at substantial cost.
- **Evaluator.** Ask for a short explanation of one utility and then a cross-service rationale; require adaptive depth and no invented motivation.
- **Consensus.** Keep reader context, concrete flow, and uncertainty; use extra investigations and visuals only when they improve the explanation.

Decision: **adapt**. Destination: `docs`. Overlap: `how`, `why`, `docs`, `handoff`. Dependencies: how, why, unslop, optional image generation/diagrams.

### technical-writing

[Source at the reviewed commit](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/technical-writing/SKILL.md). Write task-focused technical documents with concrete terms and unambiguous instructions.

- **Practitioner.** Task-oriented headings, real symbols, conditions before steps, and explicit referents improve operational clarity.
- **Skeptic.** Rigid punctuation, sentence length, tab indentation, and one-mode-only rules can override repository conventions or degrade examples.
- **Evaluator.** Edit a mixed API how-to with exact flags and a code sample; preserve semantics and project style while removing actual ambiguity.
- **Consensus.** Use document purpose and precise instructions as the core; keep prose rules as heuristics and avoid imposing a universal formatting style.

Decision: **adapt**. Destination: `docs`. Overlap: `docs`, `asd-ste100`, `unslop`. Dependencies: unslop, project documentation conventions.

### typescript-best-practices

[Source at the reviewed commit](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/typescript-best-practices/SKILL.md). Apply domain typing, runtime boundary parsing, and behavioral-test guidance to TypeScript.

- **Practitioner.** Discriminated variants, validated guards, and schema inference can catch concrete integration mistakes.
- **Skeptic.** Every TypeScript file is an overbroad trigger, universal branding or object parameters add friction, and the claim that every cast implies a crash is false.
- **Evaluator.** Review a validated interop cast, a lying type guard, and unrelated TS formatting; flag the guard without rewriting safe or unrelated code.
- **Consensus.** Keep a stack-specific reference for demonstrated type risks; align with project conventions and reserve categorical bans for actual invariants.

Decision: **profile**. Destination: `api-design`. Overlap: `principle-type-system-discipline`, `code-quality`, `domain-model`. Dependencies: TypeScript compiler, project schema library, principle-type-system-discipline.

### unslop

[Source at the reviewed commit](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/unslop/SKILL.md). Edit prose to remove filler, unsupported claims, jargon, and repetitive machine-like phrasing.

- **Practitioner.** Concrete mechanisms, preserved meaning, and source-backed claims improve human-facing technical text.
- **Skeptic.** Absolute punctuation and vocabulary bans can damage quotations, established terminology, or the writer's voice; the name collides with Matt's code cleanup.
- **Evaluator.** Rewrite docs containing a literal error, an exact quote, uncertainty, and a technical term from a banned word list; require preservation of all four.
- **Consensus.** Merge a small prose-editing reference into docs; label it prose cleanup so it cannot replace the code simplifier and preserve factual uncertainty.

Decision: **adapt**. Destination: `docs`. Overlap: `rstack/unslop`, `technical-writing`, `bro`, `mattpocock/unslop`. Dependencies: none beyond the agent.

### why

[Source at the reviewed commit](https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/why/SKILL.md). Investigate historical design motives using code anchors and available primary records.

- **Practitioner.** Separating direct rationale from supported inference and unknowns prevents plausible stories from becoming invented history.
- **Skeptic.** A full seven-category search and several writable-mode agents is excessive for narrow questions and can reach sensitive sources unnecessarily.
- **Evaluator.** Supply a code shape that suggests performance but an old issue citing correctness; require the historical source to win and missing sources to remain unknown.
- **Consensus.** Keep evidence tiers, code anchors, and conflicting records; search proportionately within scope and do not infer authority to post or mutate source systems.

Decision: **adapt**. Destination: `research`. Overlap: `research`, `project-wiki`, `how`, `recall`. Dependencies: git/gh, available MCPs, source investigators, synthesizer, per-role models.

## What could change these recommendations

Run positive and negative trigger cases, plus behavior-preservation and authority-boundary cases, against the current host and proposed personal wording. Compare the same tasks and settings without the candidate, and count task correctness, failures, user corrections, latency, and total cost. Favor a narrowly scoped adaptation only when it changes a decision or catches a real failure. Treat a missing model, absent control skill, inaccessible live surface, or incomplete coverage as an explicit limit. Source review and simulated consensus are an initial filter, not evidence that a skill improves the work.
