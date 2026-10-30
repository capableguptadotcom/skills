# Community skill review

Snapshot review: 30 October 2026. This report covers six author-owned collections at the exact commits below. It is a source review, not a live benchmark. The roles below are simulated perspectives, not quotations from the authors or independent agents.

**Coverage:** all 164 discovered entrypoints are inventoried and have purpose, procedure and constraint excerpts inspected. Long entrypoints and supporting resources were not read exhaustively; no upstream helper was executed. These are provisional curation decisions. They do not certify all 164 skills or establish measured effectiveness. Seven Matt Pocock `in-progress` entries remain deferred. No plugin mirrors or duplicate skill bodies occur within these six checked-out canonical trees.

Practitioner evaluates operational benefit; Skeptic challenges scope, portability and conflicting assumptions; Evaluator proposes a falsifiable behavior check. Consensus means a reasoned curation choice under this evidence limit, not a claim that the test passed.

| Source | Commit | Entrypoints | License |
| --- | --- | ---: | --- |
| [mattpocock/skills](https://github.com/mattpocock/skills/tree/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa) | `a496f5513d4a4cf889bc48e189e579f4b0bdf6aa` | 38 | [MIT](https://github.com/mattpocock/skills/blob/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa/LICENSE) |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills/tree/eb07f19f52c2669f2364897aaa293e2aaddd7b1c) | `eb07f19f52c2669f2364897aaa293e2aaddd7b1c` | 25 | [MIT](https://github.com/addyosmani/agent-skills/blob/eb07f19f52c2669f2364897aaa293e2aaddd7b1c/LICENSE) |
| [emilkowalski/skills](https://github.com/emilkowalski/skills/tree/a81dbca07f2217b7103e510c0f13f8d5b017afc9) | `a81dbca07f2217b7103e510c0f13f8d5b017afc9` | 16 | [MIT](https://github.com/emilkowalski/skills/blob/a81dbca07f2217b7103e510c0f13f8d5b017afc9/LICENSE) |
| [jakubkrehel/skills](https://github.com/jakubkrehel/skills/tree/592aedc44d7d5b3e29740984252902f3e5402a1c) | `592aedc44d7d5b3e29740984252902f3e5402a1c` | 14 | [MIT](https://github.com/jakubkrehel/skills/blob/592aedc44d7d5b3e29740984252902f3e5402a1c/LICENSE) |
| [ibelick/ui-skills](https://github.com/ibelick/ui-skills/tree/59193a75432e5f41c6980f53b9e6a7bd56919947) | `59193a75432e5f41c6980f53b9e6a7bd56919947` | 9 | [MIT](https://github.com/ibelick/ui-skills/blob/59193a75432e5f41c6980f53b9e6a7bd56919947/LICENSE) |
| [davidondrej/skills](https://github.com/davidondrej/skills/tree/3e30b519f897861f97943fc5f2e74c34151fd2ef) | `3e30b519f897861f97943fc5f2e74c34151fd2ef` | 62 | [MIT](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/LICENSE) |

## Decisions that change the old shortlist

- Current Matt `grilling` asks a whole independent decision frontier per round. It no longer matches the older one-question description. Preserve the useful dependency model and select question size for the actual conversation.
- Current Jakub `better-colors` requires measured contrast, preserves project notation and distinguishes a preference from a defect. A blanket rejection carried forward from an older snapshot would be inaccurate.
- Matt `tdd` requires the user to confirm test seams before any test. Preserve existing authorization and known behavioral boundaries instead of adding repetitive approval stops.
- Jakub `build-design` can remove loading or error branches not pictured in the design. Preserve necessary runtime behavior when borrowing its fidelity workflow.
- Matt `prototype` answers a bounded question with disposable code; Emil `prototype` presents visual variants in the real UI. Name collisions conceal different deliverables.
- David `total-review` demands full permissions and fixed maximum-effort models. Independent review does not require importing those permission and cost defaults.
- David `save-idea` imports an author-specific claim of preauthorized commits and pushes. Authorization cannot be copied from a source skill into another user's workflow.

## One-line catalog

| Source / skill | Purpose | Decision | Owned target |
| --- | --- | --- | --- |
| [mattpocock/ask-matt](https://github.com/mattpocock/skills/blob/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa/skills/engineering/ask-matt/SKILL.md) | Route a request through Matt's engineering and productivity workflows. | reference | start |
| [mattpocock/code-review](https://github.com/mattpocock/skills/blob/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa/skills/engineering/code-review/SKILL.md) | Review a bounded diff independently against standards and intended behavior. | adapt | review |
| [mattpocock/codebase-design](https://github.com/mattpocock/skills/blob/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa/skills/engineering/codebase-design/SKILL.md) | Evaluate modules by how much behavior they hide behind a small interface. | adapt | api-design |
| [mattpocock/diagnosing-bugs](https://github.com/mattpocock/skills/blob/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa/skills/engineering/diagnosing-bugs/SKILL.md) | Build a red-capable reproduction before iterating on bug hypotheses. | adapt | debug |
| [mattpocock/domain-modeling](https://github.com/mattpocock/skills/blob/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa/skills/engineering/domain-modeling/SKILL.md) | Clarify domain language and record consequential decisions as glossary entries and ADRs. | adapt | domain-model |
| [mattpocock/grill-with-docs](https://github.com/mattpocock/skills/blob/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa/skills/engineering/grill-with-docs/SKILL.md) | Combine requirements interviewing with persistent domain documentation. | reference | grill-idea |
| [mattpocock/implement](https://github.com/mattpocock/skills/blob/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa/skills/engineering/implement/SKILL.md) | Implement a specification or ticket using agreed TDD seams and project checks. | reference | — |
| [mattpocock/implement-spec](https://github.com/mattpocock/skills/blob/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa/skills/engineering/implement-spec/SKILL.md) | Coordinate ready tickets across implementer agents onto one integration branch. | defer | — |
| [mattpocock/improve-codebase-architecture](https://github.com/mattpocock/skills/blob/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa/skills/engineering/improve-codebase-architecture/SKILL.md) | Find architectural friction and present deepening opportunities for selection. | profile | api-design |
| [mattpocock/pr](https://github.com/mattpocock/skills/blob/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa/skills/engineering/pr/SKILL.md) | Write PR descriptions around the change, evidence and merge implications. | adapt | docs |
| [mattpocock/prototype](https://github.com/mattpocock/skills/blob/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa/skills/engineering/prototype/SKILL.md) | Build a disposable experiment to settle a specific design or state-model question. | adapt | prototype |
| [mattpocock/research](https://github.com/mattpocock/skills/blob/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa/skills/engineering/research/SKILL.md) | Investigate a technical question using primary sources and save cited findings. | adapt | research |
| [mattpocock/retro](https://github.com/mattpocock/skills/blob/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa/skills/engineering/retro/SKILL.md) | Review a session for environmental improvements that prevent repeated mistakes. | adapt | skill-maintenance |
| [mattpocock/setup-matt-pocock-skills](https://github.com/mattpocock/skills/blob/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa/skills/engineering/setup-matt-pocock-skills/SKILL.md) | Configure tracker roles and domain documentation for Matt's engineering workflow. | reference | — |
| [mattpocock/tdd](https://github.com/mattpocock/skills/blob/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa/skills/engineering/tdd/SKILL.md) | Develop through short red-green-refactor cycles at behaviorally meaningful interfaces. | adapt | tdd |
| [mattpocock/to-spec](https://github.com/mattpocock/skills/blob/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa/skills/engineering/to-spec/SKILL.md) | Synthesize an existing discussion into an actionable specification. | adapt | change-plan |
| [mattpocock/to-tickets](https://github.com/mattpocock/skills/blob/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa/skills/engineering/to-tickets/SKILL.md) | Split a specification into independently verifiable vertical tickets with blocking edges. | adapt | change-plan |
| [mattpocock/triage](https://github.com/mattpocock/skills/blob/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa/skills/engineering/triage/SKILL.md) | Classify tracker requests and turn them into agent-ready briefs. | profile | — |
| [mattpocock/wayfinder](https://github.com/mattpocock/skills/blob/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa/skills/engineering/wayfinder/SKILL.md) | Map a large ambiguous effort into dependency-linked decision tickets. | profile | change-plan |
| [mattpocock/wizard](https://github.com/mattpocock/skills/blob/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa/skills/engineering/wizard/SKILL.md) | Generate a guided Bash wizard for setup steps only a human can perform. | profile | — |
| [mattpocock/chief-of-staff](https://github.com/mattpocock/skills/blob/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa/skills/in-progress/chief-of-staff/SKILL.md) | Coordinate subagents and persistent notes toward a long-running goal. | defer | — |
| [mattpocock/claude-handoff](https://github.com/mattpocock/skills/blob/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa/skills/in-progress/claude-handoff/SKILL.md) | Write a context summary and launch a fresh Claude background agent. | defer | handoff |
| [mattpocock/loop-me](https://github.com/mattpocock/skills/blob/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa/skills/in-progress/loop-me/SKILL.md) | Interview recurring workflows into complete execution specifications. | defer | change-plan |
| [mattpocock/setup-ts-deep-modules](https://github.com/mattpocock/skills/blob/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa/skills/in-progress/setup-ts-deep-modules/SKILL.md) | Enforce TypeScript package entry-point boundaries with dependency-cruiser. | defer | api-design |
| [mattpocock/writing-beats](https://github.com/mattpocock/skills/blob/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa/skills/in-progress/writing-beats/SKILL.md) | Assemble an article through user-selected beats while grounding each concept first. | defer | — |
| [mattpocock/writing-fragments](https://github.com/mattpocock/skills/blob/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa/skills/in-progress/writing-fragments/SKILL.md) | Collect raw writing fragments before imposing an article structure. | defer | — |
| [mattpocock/writing-shape](https://github.com/mattpocock/skills/blob/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa/skills/in-progress/writing-shape/SKILL.md) | Turn a fixed collection of writing material into a structured article. | defer | — |
| [mattpocock/git-guardrails-claude-code](https://github.com/mattpocock/skills/blob/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa/skills/misc/git-guardrails-claude-code/SKILL.md) | Install Claude hooks that block dangerous Git commands before execution. | profile | — |
| [mattpocock/migrate-to-shoehorn](https://github.com/mattpocock/skills/blob/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa/skills/misc/migrate-to-shoehorn/SKILL.md) | Replace unsafe test assertions with partial TypeScript fixtures using shoehorn. | profile | — |
| [mattpocock/scaffold-exercises](https://github.com/mattpocock/skills/blob/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa/skills/misc/scaffold-exercises/SKILL.md) | Create course exercise folders conforming to AI Hero conventions. | reference | — |
| [mattpocock/setup-pre-commit](https://github.com/mattpocock/skills/blob/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa/skills/misc/setup-pre-commit/SKILL.md) | Configure Husky, lint-staged, formatting, type checks and tests. | profile | — |
| [mattpocock/grill-me](https://github.com/mattpocock/skills/blob/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa/skills/productivity/grill-me/SKILL.md) | Invoke the shared requirements-grilling procedure. | reference | grill-idea |
| [mattpocock/grilling](https://github.com/mattpocock/skills/blob/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa/skills/productivity/grilling/SKILL.md) | Resolve a decision tree through rounds of independently answerable questions. | adapt | grill-idea |
| [mattpocock/handoff](https://github.com/mattpocock/skills/blob/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa/skills/productivity/handoff/SKILL.md) | Save a compact continuation document with state, evidence and pointers. | adapt | handoff |
| [mattpocock/teach](https://github.com/mattpocock/skills/blob/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa/skills/productivity/teach/SKILL.md) | Maintain a learning workspace with lessons, references and learning records. | profile | — |
| [mattpocock/to-questionnaire](https://github.com/mattpocock/skills/blob/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa/skills/productivity/to-questionnaire/SKILL.md) | Draft questions for a person who holds information the user lacks. | profile | grill-idea |
| [mattpocock/wait-what](https://github.com/mattpocock/skills/blob/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa/skills/productivity/wait-what/SKILL.md) | Re-explain the last message using project terms and simpler English. | reference | — |
| [mattpocock/writing-for-agents](https://github.com/mattpocock/skills/blob/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa/skills/productivity/writing-for-agents/SKILL.md) | Write discoverable instruction pointers and task-specific agent procedures. | adapt | skill-maintenance |
| [addyosmani/api-and-interface-design](https://github.com/addyosmani/agent-skills/blob/eb07f19f52c2669f2364897aaa293e2aaddd7b1c/skills/api-and-interface-design/SKILL.md) | Design stable contracts, error semantics and idempotent public interfaces. | adapt | api-design |
| [addyosmani/browser-testing-with-devtools](https://github.com/addyosmani/agent-skills/blob/eb07f19f52c2669f2364897aaa293e2aaddd7b1c/skills/browser-testing-with-devtools/SKILL.md) | Inspect real browser behavior using Chrome DevTools MCP. | profile | verify-change |
| [addyosmani/ci-cd-and-automation](https://github.com/addyosmani/agent-skills/blob/eb07f19f52c2669f2364897aaa293e2aaddd7b1c/skills/ci-cd-and-automation/SKILL.md) | Configure project quality checks and staged deployment pipelines. | profile | — |
| [addyosmani/code-review-and-quality](https://github.com/addyosmani/agent-skills/blob/eb07f19f52c2669f2364897aaa293e2aaddd7b1c/skills/code-review-and-quality/SKILL.md) | Review correctness, clarity, architecture, security and performance with evidence. | adapt | review |
| [addyosmani/code-simplification](https://github.com/addyosmani/agent-skills/blob/eb07f19f52c2669f2364897aaa293e2aaddd7b1c/skills/code-simplification/SKILL.md) | Simplify changed code while preserving behavior and project conventions. | adapt | simplify |
| [addyosmani/constraint-driven-development](https://github.com/addyosmani/agent-skills/blob/eb07f19f52c2669f2364897aaa293e2aaddd7b1c/skills/constraint-driven-development/SKILL.md) | Record enforceable quality constraints and prevent silently weakening them. | adapt | skill-maintenance |
| [addyosmani/context-engineering](https://github.com/addyosmani/agent-skills/blob/eb07f19f52c2669f2364897aaa293e2aaddd7b1c/skills/context-engineering/SKILL.md) | Choose and compress relevant rules, specs, source and error context. | adapt | handoff |
| [addyosmani/debugging-and-error-recovery](https://github.com/addyosmani/agent-skills/blob/eb07f19f52c2669f2364897aaa293e2aaddd7b1c/skills/debugging-and-error-recovery/SKILL.md) | Reproduce, localize, reduce and verify a root-cause fix. | adapt | debug |
| [addyosmani/deprecation-and-migration](https://github.com/addyosmani/agent-skills/blob/eb07f19f52c2669f2364897aaa293e2aaddd7b1c/skills/deprecation-and-migration/SKILL.md) | Move users and data safely through additive replacement and removal phases. | profile | change-plan |
| [addyosmani/documentation-and-adrs](https://github.com/addyosmani/agent-skills/blob/eb07f19f52c2669f2364897aaa293e2aaddd7b1c/skills/documentation-and-adrs/SKILL.md) | Document consequential decisions, API behavior and operational context. | adapt | docs |
| [addyosmani/doubt-driven-development](https://github.com/addyosmani/agent-skills/blob/eb07f19f52c2669f2364897aaa293e2aaddd7b1c/skills/doubt-driven-development/SKILL.md) | Try to falsify consequential decisions with bounded independent review. | adapt | review |
| [addyosmani/frontend-ui-engineering](https://github.com/addyosmani/agent-skills/blob/eb07f19f52c2669f2364897aaa293e2aaddd7b1c/skills/frontend-ui-engineering/SKILL.md) | Build accessible, responsive interfaces with consistent states and design tokens. | profile | ui-review |
| [addyosmani/git-workflow-and-versioning](https://github.com/addyosmani/agent-skills/blob/eb07f19f52c2669f2364897aaa293e2aaddd7b1c/skills/git-workflow-and-versioning/SKILL.md) | Organize changes into atomic commits, short-lived branches and reviewable history. | reference | — |
| [addyosmani/idea-refine](https://github.com/addyosmani/agent-skills/blob/eb07f19f52c2669f2364897aaa293e2aaddd7b1c/skills/idea-refine/SKILL.md) | Explore alternatives, test assumptions and converge on a scoped product idea. | adapt | grill-idea |
| [addyosmani/incremental-implementation](https://github.com/addyosmani/agent-skills/blob/eb07f19f52c2669f2364897aaa293e2aaddd7b1c/skills/incremental-implementation/SKILL.md) | Deliver multi-file changes in thin, independently verifiable increments. | adapt | change-plan |
| [addyosmani/interview-me](https://github.com/addyosmani/agent-skills/blob/eb07f19f52c2669f2364897aaa293e2aaddd7b1c/skills/interview-me/SKILL.md) | Clarify the user's actual intent through focused questions and a restatement. | adapt | grill-idea |
| [addyosmani/observability-and-instrumentation](https://github.com/addyosmani/agent-skills/blob/eb07f19f52c2669f2364897aaa293e2aaddd7b1c/skills/observability-and-instrumentation/SKILL.md) | Choose and verify telemetry that answers concrete production questions. | adapt | debug |
| [addyosmani/performance-optimization](https://github.com/addyosmani/agent-skills/blob/eb07f19f52c2669f2364897aaa293e2aaddd7b1c/skills/performance-optimization/SKILL.md) | Profile a real bottleneck and retain only measured improvements. | profile | debug |
| [addyosmani/planning-and-task-breakdown](https://github.com/addyosmani/agent-skills/blob/eb07f19f52c2669f2364897aaa293e2aaddd7b1c/skills/planning-and-task-breakdown/SKILL.md) | Build a dependency-ordered plan of small tasks with acceptance criteria. | adapt | change-plan |
| [addyosmani/security-and-hardening](https://github.com/addyosmani/agent-skills/blob/eb07f19f52c2669f2364897aaa293e2aaddd7b1c/skills/security-and-hardening/SKILL.md) | Threat-model exposed boundaries and inspect application hardening controls. | profile | review |
| [addyosmani/shipping-and-launch](https://github.com/addyosmani/agent-skills/blob/eb07f19f52c2669f2364897aaa293e2aaddd7b1c/skills/shipping-and-launch/SKILL.md) | Prepare rollout gates, monitoring and rollback for a production launch. | profile | verify-change |
| [addyosmani/source-driven-development](https://github.com/addyosmani/agent-skills/blob/eb07f19f52c2669f2364897aaa293e2aaddd7b1c/skills/source-driven-development/SKILL.md) | Verify version-sensitive implementation choices against official documentation. | adapt | research |
| [addyosmani/spec-driven-development](https://github.com/addyosmani/agent-skills/blob/eb07f19f52c2669f2364897aaa293e2aaddd7b1c/skills/spec-driven-development/SKILL.md) | Turn an ambiguous initiative into a scoped specification with testable capabilities. | adapt | change-plan |
| [addyosmani/test-driven-development](https://github.com/addyosmani/agent-skills/blob/eb07f19f52c2669f2364897aaa293e2aaddd7b1c/skills/test-driven-development/SKILL.md) | Use failing behavioral tests to guide implementation and regression fixes. | adapt | tdd |
| [addyosmani/using-agent-skills](https://github.com/addyosmani/agent-skills/blob/eb07f19f52c2669f2364897aaa293e2aaddd7b1c/skills/using-agent-skills/SKILL.md) | Select engineering skills by the current delivery activity. | reference | start |
| [emilkowalski/animate](https://github.com/emilkowalski/skills/blob/a81dbca07f2217b7103e510c0f13f8d5b017afc9/skills/animate/SKILL.md) | Implement purposeful web motion with interruption, exits and reduced-motion handling. | profile | — |
| [emilkowalski/animate-expo](https://github.com/emilkowalski/skills/blob/a81dbca07f2217b7103e510c0f13f8d5b017afc9/skills/animate-expo/SKILL.md) | Build React Native and Expo gestures, transitions and haptics. | profile | — |
| [emilkowalski/animation-performance](https://github.com/emilkowalski/skills/blob/a81dbca07f2217b7103e510c0f13f8d5b017afc9/skills/animation-performance/SKILL.md) | Diagnose animation frame misses across layout, paint, compositing and React. | profile | debug |
| [emilkowalski/animation-vocabulary](https://github.com/emilkowalski/skills/blob/a81dbca07f2217b7103e510c0f13f8d5b017afc9/skills/animation-vocabulary/SKILL.md) | Name a described motion effect using a motion glossary. | reference | — |
| [emilkowalski/apple-design](https://github.com/emilkowalski/skills/blob/a81dbca07f2217b7103e510c0f13f8d5b017afc9/skills/apple-design/SKILL.md) | Apply direct manipulation and interruptible Apple-style motion to web interactions. | profile | — |
| [emilkowalski/ask-sonner](https://github.com/emilkowalski/skills/blob/a81dbca07f2217b7103e510c0f13f8d5b017afc9/skills/ask-sonner/SKILL.md) | Configure and troubleshoot Sonner toast behavior and styling. | profile | — |
| [emilkowalski/break-ui](https://github.com/emilkowalski/skills/blob/a81dbca07f2217b7103e510c0f13f8d5b017afc9/skills/break-ui/SKILL.md) | Stress a UI with plausible worst-case content and report rendered failures. | adapt | ui-review |
| [emilkowalski/emil-design-eng](https://github.com/emilkowalski/skills/blob/a81dbca07f2217b7103e510c0f13f8d5b017afc9/skills/emil-design-eng/SKILL.md) | Provide an umbrella catalog of design-engineering and motion heuristics. | reference | ui-review |
| [emilkowalski/find-animation-opportunities](https://github.com/emilkowalski/skills/blob/a81dbca07f2217b7103e510c0f13f8d5b017afc9/skills/find-animation-opportunities/SKILL.md) | Propose justified motion opportunities without editing source. | profile | ui-review |
| [emilkowalski/improve-animations](https://github.com/emilkowalski/skills/blob/a81dbca07f2217b7103e510c0f13f8d5b017afc9/skills/improve-animations/SKILL.md) | Audit motion across a codebase and write selected implementation plans. | profile | ui-review |
| [emilkowalski/mobile-native](https://github.com/emilkowalski/skills/blob/a81dbca07f2217b7103e510c0f13f8d5b017afc9/skills/mobile-native/SKILL.md) | Fix mobile web viewport, touch, safe-area and browser behavior problems. | profile | ui-review |
| [emilkowalski/pick-ui-library](https://github.com/emilkowalski/skills/blob/a81dbca07f2217b7103e510c0f13f8d5b017afc9/skills/pick-ui-library/SKILL.md) | Recommend a UI library from an opinionated task-based shortlist. | reference | — |
| [emilkowalski/prototype](https://github.com/emilkowalski/skills/blob/a81dbca07f2217b7103e510c0f13f8d5b017afc9/skills/prototype/SKILL.md) | Build distinct UI variants behind a live picker and promote a selected option. | profile | prototype |
| [emilkowalski/remove-animations](https://github.com/emilkowalski/skills/blob/a81dbca07f2217b7103e510c0f13f8d5b017afc9/skills/remove-animations/SKILL.md) | Subtract unnecessary motion and clean up orphaned animation code. | profile | ui-review |
| [emilkowalski/review-animations](https://github.com/emilkowalski/skills/blob/a81dbca07f2217b7103e510c0f13f8d5b017afc9/skills/review-animations/SKILL.md) | Review a motion change for purpose, continuity, accessibility and performance. | adapt | ui-review |
| [emilkowalski/write-swift](https://github.com/emilkowalski/skills/blob/a81dbca07f2217b7103e510c0f13f8d5b017afc9/skills/write-swift/SKILL.md) | Write and review modern Swift modeling, concurrency and ownership code. | profile | — |
| [jakubkrehel/better-accessibility](https://github.com/jakubkrehel/skills/blob/592aedc44d7d5b3e29740984252902f3e5402a1c/skills/better-accessibility/SKILL.md) | Check rendered semantics, names, focus, keyboard, announcements and zoom against WCAG criteria. | adapt | ui-review |
| [jakubkrehel/better-colors](https://github.com/jakubkrehel/skills/blob/592aedc44d7d5b3e29740984252902f3e5402a1c/skills/better-colors/SKILL.md) | Build semantic palettes and measure rendered contrast and gamut behavior. | adapt | ui-review |
| [jakubkrehel/better-interface](https://github.com/jakubkrehel/skills/blob/592aedc44d7d5b3e29740984252902f3e5402a1c/skills/better-interface/SKILL.md) | Combine specialist UI evidence into one ranked interface review. | adapt | ui-review |
| [jakubkrehel/better-layout](https://github.com/jakubkrehel/skills/blob/592aedc44d7d5b3e29740984252902f3e5402a1c/skills/better-layout/SKILL.md) | Check grouping, responsive structure, translation growth and RTL layout. | adapt | ui-review |
| [jakubkrehel/better-typography](https://github.com/jakubkrehel/skills/blob/592aedc44d7d5b3e29740984252902f3e5402a1c/skills/better-typography/SKILL.md) | Review font loading, type scales, wrapping, truncation and language behavior. | profile | ui-review |
| [jakubkrehel/better-ui](https://github.com/jakubkrehel/skills/blob/592aedc44d7d5b3e29740984252902f3e5402a1c/skills/better-ui/SKILL.md) | Polish visual surfaces, icons, radii, shadows and motion. | profile | ui-review |
| [jakubkrehel/better-writing](https://github.com/jakubkrehel/skills/blob/592aedc44d7d5b3e29740984252902f3e5402a1c/skills/better-writing/SKILL.md) | Make interface labels, errors and empty states clear and consistent. | adapt | docs |
| [jakubkrehel/break](https://github.com/jakubkrehel/skills/blob/592aedc44d7d5b3e29740984252902f3e5402a1c/skills/break/SKILL.md) | Render plausible component scenarios together on an isolated stress-test page. | profile | ui-review |
| [jakubkrehel/build-design](https://github.com/jakubkrehel/skills/blob/592aedc44d7d5b3e29740984252902f3e5402a1c/skills/build-design/SKILL.md) | Implement a Figma or image design using the project's existing primitives. | profile | — |
| [jakubkrehel/explain-interface](https://github.com/jakubkrehel/skills/blob/592aedc44d7d5b3e29740984252902f3e5402a1c/skills/explain-interface/SKILL.md) | Explain how a visual effect or website was built from inspectable evidence. | reference | research |
| [jakubkrehel/interface-review](https://github.com/jakubkrehel/skills/blob/592aedc44d7d5b3e29740984252902f3e5402a1c/skills/interface-review/SKILL.md) | Review UI regressions introduced by a specific diff. | adapt | ui-review |
| [jakubkrehel/state-machine](https://github.com/jakubkrehel/skills/blob/592aedc44d7d5b3e29740984252902f3e5402a1c/skills/state-machine/SKILL.md) | Expose every relevant component state in a temporary fixture workbench. | profile | prototype |
| [jakubkrehel/teardown](https://github.com/jakubkrehel/skills/blob/592aedc44d7d5b3e29740984252902f3e5402a1c/skills/teardown/SKILL.md) | Create technical illustrations that explain objects and construction. | reference | — |
| [jakubkrehel/variant](https://github.com/jakubkrehel/skills/blob/592aedc44d7d5b3e29740984252902f3e5402a1c/skills/variant/SKILL.md) | Build deliberately different component designs for live comparison and selection. | profile | prototype |
| [ibelick/baseline-ui](https://github.com/ibelick/ui-skills/blob/59193a75432e5f41c6980f53b9e6a7bd56919947/skills/baseline-ui/SKILL.md) | Apply a compact opinionated baseline for layout, type, components and motion. | reference | ui-review |
| [ibelick/component-canvas](https://github.com/ibelick/ui-skills/blob/59193a75432e5f41c6980f53b9e6a7bd56919947/skills/component-canvas/SKILL.md) | Explore existing UI components and variants on a pan-and-zoom canvas. | profile | prototype |
| [ibelick/create-canvas](https://github.com/ibelick/ui-skills/blob/59193a75432e5f41c6980f53b9e6a7bd56919947/skills/create-canvas/SKILL.md) | Build a source-backed workspace for freeform visual exploration. | profile | prototype |
| [ibelick/create-design-md](https://github.com/ibelick/ui-skills/blob/59193a75432e5f41c6980f53b9e6a7bd56919947/skills/create-design-md/SKILL.md) | Document a product's actual visual system from source or a rendered site. | adapt | docs |
| [ibelick/fixing-accessibility](https://github.com/ibelick/ui-skills/blob/59193a75432e5f41c6980f53b9e6a7bd56919947/skills/fixing-accessibility/SKILL.md) | Audit and repair accessible names, keyboard, focus, forms and contrast. | adapt | ui-review |
| [ibelick/fixing-metadata](https://github.com/ibelick/ui-skills/blob/59193a75432e5f41c6980f53b9e6a7bd56919947/skills/fixing-metadata/SKILL.md) | Check titles, canonicals, indexing, social cards and structured metadata. | profile | ui-review |
| [ibelick/fixing-motion-performance](https://github.com/ibelick/ui-skills/blob/59193a75432e5f41c6980f53b9e6a7bd56919947/skills/fixing-motion-performance/SKILL.md) | Audit layout thrashing, compositing, scroll motion and animation cost. | profile | debug |
| [ibelick/improve-ui](https://github.com/ibelick/ui-skills/blob/59193a75432e5f41c6980f53b9e6a7bd56919947/skills/improve-ui/SKILL.md) | Review a product against its own design evidence and write selected fix plans. | adapt | ui-review |
| [ibelick/ui-skills-root](https://github.com/ibelick/ui-skills/blob/59193a75432e5f41c6980f53b9e6a7bd56919947/skills/ui-skills-root/SKILL.md) | Select a small set of UI skill contexts through the UI Skills CLI. | reference | start |
| [davidondrej/bb-cli](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/agent-orchestration/bb-cli/SKILL.md) | Inspect and manage BB threads, projects, runtimes and services. | profile | — |
| [davidondrej/bb-plugins](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/agent-orchestration/bb-plugins/SKILL.md) | Build and debug full-trust BB plugins and extension surfaces. | profile | — |
| [davidondrej/cmux](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/agent-orchestration/cmux/SKILL.md) | Control macOS cmux workspaces, panes, browsers and terminals. | profile | — |
| [davidondrej/codex-subagent](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/agent-orchestration/codex-subagent/SKILL.md) | Launch Codex CLI to perform an isolated delegated task. | reference | — |
| [davidondrej/fable-review](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/agent-orchestration/fable-review/SKILL.md) | Launch a specified Fable review through Cloudroom. | reference | review |
| [davidondrej/fable-safe-prompt](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/agent-orchestration/fable-safe-prompt/SKILL.md) | Rewrite prompt wording to reduce a provider's false-positive refusals. | reject | — |
| [davidondrej/git-worktree](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/agent-orchestration/git-worktree/SKILL.md) | Choose managed or native worktree isolation for parallel agents. | reference | — |
| [davidondrej/goal-loop](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/agent-orchestration/goal-loop/SKILL.md) | Define autonomous loops with verifiable stop conditions and budgets. | adapt | verify-change |
| [davidondrej/gpt-review](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/agent-orchestration/gpt-review/SKILL.md) | Launch a fixed GPT review through Cloudroom and Codex. | reference | review |
| [davidondrej/handoff](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/agent-orchestration/handoff/SKILL.md) | Capture precise session state and pointers for another agent. | adapt | handoff |
| [davidondrej/herdr](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/agent-orchestration/herdr/SKILL.md) | Coordinate terminal agents inside Herdr workspaces in Ghostty. | profile | — |
| [davidondrej/kimi-review](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/agent-orchestration/kimi-review/SKILL.md) | Launch a fixed Kimi review using ordered provider routes. | reference | review |
| [davidondrej/larp-detector](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/agent-orchestration/larp-detector/SKILL.md) | Evaluate whether an outside contribution solves a real project problem. | reject | review |
| [davidondrej/muse-review](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/agent-orchestration/muse-review/SKILL.md) | Launch a specific Meta Muse review through Pi and OpenRouter. | reference | review |
| [davidondrej/nagent](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/agent-orchestration/nagent/SKILL.md) | Create a BB worker with the requested project, model and checkout. | profile | — |
| [davidondrej/new-grok-bot](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/agent-orchestration/new-grok-bot/SKILL.md) | Draft a narrowly scoped role and setup prompt for a Grok Bot. | reference | — |
| [davidondrej/reset-cursor-acp](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/agent-orchestration/reset-cursor-acp/SKILL.md) | Reset one stuck Cursor ACP thread while preserving history. | profile | — |
| [davidondrej/self-archive](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/agent-orchestration/self-archive/SKILL.md) | Archive the current Cloudroom thread and release its runtime. | reference | — |
| [davidondrej/total-review](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/agent-orchestration/total-review/SKILL.md) | Run five fixed high-effort model reviews and reconcile findings. | reject | review |
| [davidondrej/anti-sleep](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/ops-and-setup/anti-sleep/SKILL.md) | Keep a Mac awake through a scoped one-shot LaunchAgent. | profile | — |
| [davidondrej/boat](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/ops-and-setup/boat/SKILL.md) | Manage Boat cloud sandboxes, snapshots and execution environments. | profile | — |
| [davidondrej/create-readonly-db-role](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/ops-and-setup/create-readonly-db-role/SKILL.md) | Prepare restricted PostgreSQL agent access and connection settings. | profile | — |
| [davidondrej/cua-driver](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/ops-and-setup/cua-driver/SKILL.md) | Drive desktop apps using a local accessibility and screenshot tool. | profile | — |
| [davidondrej/github-outside-sandbox](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/ops-and-setup/github-outside-sandbox/SKILL.md) | Retry an authorized GitHub operation using an allowed host execution mechanism. | reference | — |
| [davidondrej/global-agent-guardrails](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/ops-and-setup/global-agent-guardrails/SKILL.md) | Maintain a shared destructive-command guard with agent-specific adapters. | profile | — |
| [davidondrej/openrouter](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/ops-and-setup/openrouter/SKILL.md) | Build OpenRouter integrations with explicit routing, validation and retry semantics. | profile | — |
| [davidondrej/persistent-localhost](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/ops-and-setup/persistent-localhost/SKILL.md) | Manage local development services that survive shell exit using launchd. | profile | — |
| [davidondrej/prompt-for-others](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/ops-and-setup/prompt-for-others/SKILL.md) | Write a tested, self-contained setup or fix prompt for a teammate's agent. | adapt | handoff |
| [davidondrej/rename-process](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/ops-and-setup/rename-process/SKILL.md) | Coordinate a repository or service rename while preserving state and references. | profile | — |
| [davidondrej/repo-sync](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/ops-and-setup/repo-sync/SKILL.md) | Configure macOS automatic commits, rebases and pushes for shared document repos. | reference | — |
| [davidondrej/risky-changes](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/ops-and-setup/risky-changes/SKILL.md) | Validate customer impact and live-data assumptions beyond passing tests. | adapt | verify-change |
| [davidondrej/setup-help](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/ops-and-setup/setup-help/SKILL.md) | Guide manual setup one coherent step at a time with a short remaining list. | reference | — |
| [davidondrej/browser-harness](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/research-and-web/browser-harness/SKILL.md) | Control existing or isolated browsers through a CDP-based harness. | profile | — |
| [davidondrej/browser-use](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/research-and-web/browser-use/SKILL.md) | Automate browser interactions, screenshots and logged-in flows through Browser Use. | profile | — |
| [davidondrej/deep-research](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/research-and-web/deep-research/SKILL.md) | Submit an asynchronous DeepAPI research job and save sourced output. | profile | research |
| [davidondrej/deep-scrape](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/research-and-web/deep-scrape/SKILL.md) | Build a sourced structured dossier on one public subject through DeepAPI. | profile | — |
| [davidondrej/deepapi](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/research-and-web/deepapi/SKILL.md) | Route web research, scraping, email, browser and image operations through DeepAPI. | reference | research |
| [davidondrej/domain-checker](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/research-and-web/domain-checker/SKILL.md) | Check domain registration through public RDAP services in small batches. | profile | — |
| [davidondrej/fireflies-transcript](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/research-and-web/fireflies-transcript/SKILL.md) | Retrieve raw Fireflies meeting transcripts through its GraphQL API. | profile | — |
| [davidondrej/online-shopping](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/research-and-web/online-shopping/SKILL.md) | Research prices and seller credibility without executing purchases. | reference | — |
| [davidondrej/varied-search](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/research-and-web/varied-search/SKILL.md) | Collect web, GitHub and social search results using a fixed DeepAPI quota. | reference | research |
| [davidondrej/who-is-this](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/research-and-web/who-is-this/SKILL.md) | Assess a person's public track record using corroborated profiles. | reference | — |
| [davidondrej/distribute-skill-to-all-agents](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/skill-authoring/distribute-skill-to-all-agents/SKILL.md) | Synchronize a personal skill across several agent discovery roots. | reference | — |
| [davidondrej/effective-agent-skills](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/skill-authoring/effective-agent-skills/SKILL.md) | Author and troubleshoot skill metadata, routing and progressive disclosure. | adapt | skill-maintenance |
| [davidondrej/push-skills](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/skill-authoring/push-skills/SKILL.md) | Publish an author's private skills repository and verify its sanitized mirror. | reference | — |
| [davidondrej/4x4](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/thinking-and-docs/4x4/SKILL.md) | Collect product and engineering decisions in four rounds of four questions. | reference | grill-idea |
| [davidondrej/adr-verbatim](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/thinking-and-docs/adr-verbatim/SKILL.md) | Record concise ADRs while preserving the user's decision and context. | adapt | docs |
| [davidondrej/ask-then-build](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/thinking-and-docs/ask-then-build/SKILL.md) | Clarify consequential choices before drafting a build prompt for another agent. | adapt | grill-idea |
| [davidondrej/before-building](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/thinking-and-docs/before-building/SKILL.md) | Surface a few consequential hidden choices immediately from an idea. | reference | grill-idea |
| [davidondrej/better-prompt](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/thinking-and-docs/better-prompt/SKILL.md) | Deepen a task's professional method without enlarging its scope. | reference | — |
| [davidondrej/decisions](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/thinking-and-docs/decisions/SKILL.md) | List consequential choices that remain uncertain in the current work. | reference | — |
| [davidondrej/designs](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/thinking-and-docs/designs/SKILL.md) | Generate four new visual design directions as separate images. | reference | — |
| [davidondrej/file-tree](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/thinking-and-docs/file-tree/SKILL.md) | Show a compact high-level file tree for the topic at hand. | reference | — |
| [davidondrej/image-prompt](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/thinking-and-docs/image-prompt/SKILL.md) | Write four distinct copyable prompts for image generation. | reference | — |
| [davidondrej/keep-track](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/thinking-and-docs/keep-track/SKILL.md) | Maintain a short list of unresolved topics and decisions across replies. | reference | handoff |
| [davidondrej/read-all-adrs](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/thinking-and-docs/read-all-adrs/SKILL.md) | Read every ADR in a fixed project directory when explicitly requested. | reject | docs |
| [davidondrej/remind](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/thinking-and-docs/remind/SKILL.md) | Restate the current topic and last answer in simpler, shorter language. | reference | handoff |
| [davidondrej/rename](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/thinking-and-docs/rename/SKILL.md) | Rename the current Cloudroom thread with a short descriptive title. | reference | — |
| [davidondrej/save-idea](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/thinking-and-docs/save-idea/SKILL.md) | Append an idea to an author's chosen repository and automatically commit and push it. | reject | — |
| [davidondrej/signal-from-expert](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/thinking-and-docs/signal-from-expert/SKILL.md) | Compare a user's notes with attributed expert sources and identify gaps. | profile | research |
| [davidondrej/stop-overthinking](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/thinking-and-docs/stop-overthinking/SKILL.md) | Give a concise practical next step while surfacing serious unresolved issues. | reference | minimalist |
| [davidondrej/teach](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/thinking-and-docs/teach/SKILL.md) | Maintain concise teaching chat backed by persistent lesson artifacts. | profile | — |

## Per-skill simulated discussion

### mattpocock/skills

<details><summary>ask-matt — reference</summary>

[Pinned source](https://github.com/mattpocock/skills/blob/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa/skills/engineering/ask-matt/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Explains the main delivery flow and its entry points.
- **Skeptic:** A second router competes with the owned start skill and assumes the whole collection.
- **Evaluator:** Ask for a small agreed fix and confirm no interview or tracker setup is forced.
- **Consensus:** Retain as a linked reference, not another active trigger. A second router competes with the owned start skill and assumes the whole collection.
- **Overlap:** start, using-agent-skills, poteto-mode
- **Prerequisites:** Sibling skills

</details>

<details><summary>code-review — adapt</summary>

[Pinned source](https://github.com/mattpocock/skills/blob/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa/skills/engineering/code-review/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Separates conformity from specification coverage and labels code smells as heuristics.
- **Skeptic:** Mandatory parallel reviewers and tracker setup add cost; three-dot diff alone omits unstaged work.
- **Evaluator:** Review a dirty worktree and prove the intended files and spec deviations are included.
- **Consensus:** Absorb the useful procedure into review; resolve this source-specific limit before promotion: Mandatory parallel reviewers and tracker setup add cost; three-dot diff alone omits unstaged work. Behavioral benefit remains unmeasured.
- **Overlap:** review, code-review-and-quality, interrogate
- **Prerequisites:** Git, subagents, configured issue tracker

</details>

<details><summary>codebase-design — adapt</summary>

[Pinned source](https://github.com/mattpocock/skills/blob/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa/skills/engineering/codebase-design/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Makes caller knowledge and testable seams explicit.
- **Skeptic:** Forbidding ordinary API or service vocabulary can conflict with the project's domain language.
- **Evaluator:** Compare two interfaces using realistic caller examples and preserve existing terminology.
- **Consensus:** Absorb the useful procedure into api-design; resolve this source-specific limit before promotion: Forbidding ordinary API or service vocabulary can conflict with the project's domain language. Behavioral benefit remains unmeasured.
- **Overlap:** api-design, code-structure
- **Prerequisites:** Project glossary and ADRs when present

</details>

<details><summary>diagnosing-bugs — adapt</summary>

[Pinned source](https://github.com/mattpocock/skills/blob/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa/skills/engineering/diagnosing-bugs/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** The reproduction must catch the user's exact symptom rather than merely run.
- **Skeptic:** An absolute ban on hypotheses before reproduction can block useful read-only diagnosis when access is missing.
- **Evaluator:** Give an inaccessible production incident; expect bounded hypotheses and explicit evidence gaps rather than invented proof.
- **Consensus:** Absorb the useful procedure into debug; resolve this source-specific limit before promotion: An absolute ban on hypotheses before reproduction can block useful read-only diagnosis when access is missing. Behavioral benefit remains unmeasured.
- **Overlap:** debug, debugging-and-error-recovery
- **Prerequisites:** Reproduction environment, optional capture or instrumentation

</details>

<details><summary>domain-modeling — adapt</summary>

[Pinned source](https://github.com/mattpocock/skills/blob/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa/skills/engineering/domain-modeling/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Uses adversarial scenarios to expose ambiguous terms.
- **Skeptic:** Fixed documentation layouts can conflict with established wiki or ADR conventions.
- **Evaluator:** Introduce two meanings for one term and verify examples distinguish them without reorganizing docs.
- **Consensus:** Absorb the useful procedure into domain-model; resolve this source-specific limit before promotion: Fixed documentation layouts can conflict with established wiki or ADR conventions. Behavioral benefit remains unmeasured.
- **Overlap:** domain-model, documentation-and-adrs
- **Prerequisites:** Existing project documentation

</details>

<details><summary>grill-with-docs — reference</summary>

[Pinned source](https://github.com/mattpocock/skills/blob/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa/skills/engineering/grill-with-docs/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Retains decisions across sessions rather than repeating interviews.
- **Skeptic:** It is a thin wrapper over grilling and domain-modeling; installing it alone cannot supply them.
- **Evaluator:** Invoke on an already settled decision and check it does not restart discovery.
- **Consensus:** Retain as a linked reference, not another active trigger. It is a thin wrapper over grilling and domain-modeling; installing it alone cannot supply them.
- **Overlap:** grill-me, grilling, domain-modeling
- **Prerequisites:** grilling, domain-modeling, Skill tool

</details>

<details><summary>implement — reference</summary>

[Pinned source](https://github.com/mattpocock/skills/blob/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa/skills/engineering/implement/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Connects implementation to concrete acceptance criteria.
- **Skeptic:** It unconditionally commits to the current branch and assumes TDD and tracker conventions.
- **Evaluator:** Request a local implementation without a commit; expect changes and evidence but no unsolicited commit.
- **Consensus:** Retain as a linked reference, not another active trigger. It unconditionally commits to the current branch and assumes TDD and tracker conventions.
- **Overlap:** start, tdd, implement-spec
- **Prerequisites:** tdd, issue tracker when referenced

</details>

<details><summary>implement-spec — defer</summary>

[Pinned source](https://github.com/mattpocock/skills/blob/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa/skills/engineering/implement-spec/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Treats work as a dependency graph rather than an arbitrary task list.
- **Skeptic:** Concurrent agents and automatic tracker closure require integration and authority rules beyond a generic skill.
- **Evaluator:** Use tickets sharing a schema and verify ordering, isolation, integration tests and authorized closure.
- **Consensus:** Do not promote this version. Concurrent agents and automatic tracker closure require integration and authority rules beyond a generic skill. Reconsider after a demonstrated recurring need and a behavioral evaluation.
- **Overlap:** change-plan, implement, poteto-mode
- **Prerequisites:** Subagents, Git worktrees, tracker, configured workflow

</details>

<details><summary>improve-codebase-architecture — profile</summary>

[Pinned source](https://github.com/mattpocock/skills/blob/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa/skills/engineering/improve-codebase-architecture/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Uses history hot spots to focus architecture work.
- **Skeptic:** A broad codebase sweep and mandated vocabulary or HTML output can exceed a local refactor request.
- **Evaluator:** Provide one troublesome boundary; expect bounded alternatives and no speculative rewrite.
- **Consensus:** Keep available for a matching project rather than the default catalog. Validate the named prerequisites and check: Provide one troublesome boundary; expect bounded alternatives and no speculative rewrite.
- **Overlap:** codebase-design, api-design
- **Prerequisites:** codebase-design, glossary, ADRs, HTML preview

</details>

<details><summary>pr — adapt</summary>

[Pinned source](https://github.com/mattpocock/skills/blob/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa/skills/engineering/pr/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Before/after proof helps a reviewer assess behavior quickly.
- **Skeptic:** A visual template becomes ceremony when the change is a small text or internal edit.
- **Evaluator:** Describe a one-line configuration fix accurately without manufacturing a diagram or screenshot.
- **Consensus:** Absorb the useful procedure into docs; resolve this source-specific limit before promotion: A visual template becomes ceremony when the change is a small text or internal edit. Behavioral benefit remains unmeasured.
- **Overlap:** docs, show-me-your-work
- **Prerequisites:** PR context and available evidence

</details>

<details><summary>prototype — adapt</summary>

[Pinned source](https://github.com/mattpocock/skills/blob/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa/skills/engineering/prototype/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Makes the question decide the prototype's shape.
- **Skeptic:** Automatic capture on a throwaway branch or tracker assumes permission to commit or publish.
- **Evaluator:** Ask whether retries preserve state and verify a runnable experiment answers that question without production integration.
- **Consensus:** Absorb the useful procedure into prototype; resolve this source-specific limit before promotion: Automatic capture on a throwaway branch or tracker assumes permission to commit or publish. Behavioral benefit remains unmeasured.
- **Overlap:** prototype, variant, state-machine
- **Prerequisites:** Optional HTML runtime, Git and tracker for capture

</details>

<details><summary>research — adapt</summary>

[Pinned source](https://github.com/mattpocock/skills/blob/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa/skills/engineering/research/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Follows claims back to official docs, code or first-party APIs.
- **Skeptic:** Mandatory background delegation is unnecessary for a narrow lookup and is not universally available.
- **Evaluator:** Compare two documented APIs with contradictory secondary advice and trace the recommendation to versioned primary evidence.
- **Consensus:** Absorb the useful procedure into research; resolve this source-specific limit before promotion: Mandatory background delegation is unnecessary for a narrow lookup and is not universally available. Behavioral benefit remains unmeasured.
- **Overlap:** research, source-driven-development, deep-research
- **Prerequisites:** Web or source access, optional subagents

</details>

<details><summary>retro — adapt</summary>

[Pinned source](https://github.com/mattpocock/skills/blob/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa/skills/engineering/retro/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Prefers deterministic checks for mechanical failures instead of more prompt prose.
- **Skeptic:** Treating every missing guardrail as a finding can expand a narrow retrospective into tooling work.
- **Evaluator:** Use a session where a linter existed but was unwired and propose wiring it rather than another rule.
- **Consensus:** Absorb the useful procedure into skill-maintenance; resolve this source-specific limit before promotion: Treating every missing guardrail as a finding can expand a narrow retrospective into tooling work. Behavioral benefit remains unmeasured.
- **Overlap:** reflect, correct, effective-agent-skills
- **Prerequisites:** Session evidence, project check configuration

</details>

<details><summary>setup-matt-pocock-skills — reference</summary>

[Pinned source](https://github.com/mattpocock/skills/blob/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa/skills/engineering/setup-matt-pocock-skills/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Makes implicit workflow dependencies visible before use.
- **Skeptic:** It changes remotes and persistent instructions; personal conventions are not a universal product setup.
- **Evaluator:** Inspect a repository with an existing tracker and instructions and preserve them while reporting missing prerequisites.
- **Consensus:** Retain as a linked reference, not another active trigger. It changes remotes and persistent instructions; personal conventions are not a universal product setup.
- **Overlap:** start, using-agent-skills
- **Prerequisites:** Git, gh or glab, project instructions

</details>

<details><summary>tdd — adapt</summary>

[Pinned source](https://github.com/mattpocock/skills/blob/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa/skills/engineering/tdd/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Rejects tautological assertions and tests coupled to internal implementation.
- **Skeptic:** Requiring fresh user confirmation for every test seam can stall already authorized work.
- **Evaluator:** Change internals while preserving public behavior; tests should pass, and a real behavioral defect should fail.
- **Consensus:** Absorb the useful procedure into tdd; resolve this source-specific limit before promotion: Requiring fresh user confirmation for every test seam can stall already authorized work. Behavioral benefit remains unmeasured.
- **Overlap:** tdd, test-driven-development
- **Prerequisites:** Project test runner, agreed public behavior

</details>

<details><summary>to-spec — adapt</summary>

[Pinned source](https://github.com/mattpocock/skills/blob/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa/skills/engineering/to-spec/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Preserves settled context instead of opening another requirements interview.
- **Skeptic:** It also publishes tracker issues and requests seam confirmation despite claiming no interview.
- **Evaluator:** Turn a settled conversation into a local spec without invented requirements or unrequested publication.
- **Consensus:** Absorb the useful procedure into change-plan; resolve this source-specific limit before promotion: It also publishes tracker issues and requests seam confirmation despite claiming no interview. Behavioral benefit remains unmeasured.
- **Overlap:** change-plan, spec-driven-development
- **Prerequisites:** Configured tracker, project glossary

</details>

<details><summary>to-tickets — adapt</summary>

[Pinned source](https://github.com/mattpocock/skills/blob/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa/skills/engineering/to-tickets/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Explicit dependencies make parallel readiness auditable.
- **Skeptic:** Automatic issue publication and prefactoring can expand a planning-only request.
- **Evaluator:** Break a three-layer feature into demoable slices and detect a deliberately introduced dependency cycle.
- **Consensus:** Absorb the useful procedure into change-plan; resolve this source-specific limit before promotion: Automatic issue publication and prefactoring can expand a planning-only request. Behavioral benefit remains unmeasured.
- **Overlap:** change-plan, planning-and-task-breakdown
- **Prerequisites:** Configured tracker and triage vocabulary

</details>

<details><summary>triage — profile</summary>

[Pinned source](https://github.com/mattpocock/skills/blob/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa/skills/engineering/triage/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Separates category from workflow state and reuses prior reporter answers.
- **Skeptic:** Labels, public disclaimers and comments need the team's tracker policy and posting authority.
- **Evaluator:** Triage an issue with answered questions and verify no repeated questions or contradictory state labels.
- **Consensus:** Keep available for a matching project rather than the default catalog. Validate the named prerequisites and check: Triage an issue with answered questions and verify no repeated questions or contradictory state labels.
- **Overlap:** review, grill-idea
- **Prerequisites:** Tracker configuration, labels, AGENT-BRIEF reference

</details>

<details><summary>wayfinder — profile</summary>

[Pinned source](https://github.com/mattpocock/skills/blob/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa/skills/engineering/wayfinder/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Separates decisions that clear a path from implementation work.
- **Skeptic:** A persistent issue map and claiming tickets add overhead for ordinary changes.
- **Evaluator:** Use a decision blocked on research; resolve other independent decisions without pretending the blocker is settled.
- **Consensus:** Keep available for a matching project rather than the default catalog. Validate the named prerequisites and check: Use a decision blocked on research; resolve other independent decisions without pretending the blocker is settled.
- **Overlap:** change-plan, to-tickets
- **Prerequisites:** Tracker labels and assignment, related skills

</details>

<details><summary>wizard — profile</summary>

[Pinned source](https://github.com/mattpocock/skills/blob/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa/skills/engineering/wizard/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Keeps secrets hidden and confirms irreversible manual operations.
- **Skeptic:** The Bash template and hosted dashboard assumptions are not portable to every shell or setup.
- **Evaluator:** Run with missing credentials in a scratch environment; no secret should enter logs or tracked files.
- **Consensus:** Keep available for a matching project rather than the default catalog. Validate the named prerequisites and check: Run with missing credentials in a scratch environment; no secret should enter logs or tracked files.
- **Overlap:** setup-help, prompt-for-others
- **Prerequisites:** Bash, template.sh, optional gh and browser

</details>

<details><summary>chief-of-staff — defer</summary>

[Pinned source](https://github.com/mattpocock/skills/blob/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa/skills/in-progress/chief-of-staff/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Keeps tactical execution and durable project knowledge connected.
- **Skeptic:** The in-progress prompt says all work goes to agents and every message invites environment improvement.
- **Evaluator:** Give a bounded feature task and detect unsolicited tooling work or scheduling.
- **Consensus:** Do not promote this version. The in-progress prompt says all work goes to agents and every message invites environment improvement. Reconsider after a demonstrated recurring need and a behavioral evaluation.
- **Overlap:** poteto-mode, goal-loop
- **Prerequisites:** Subagents, scheduling support, wiki

</details>

<details><summary>claude-handoff — defer</summary>

[Pinned source](https://github.com/mattpocock/skills/blob/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa/skills/in-progress/claude-handoff/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Combines a continuation brief with an immediate runtime handoff.
- **Skeptic:** It is in-progress and starts another worker through a Claude-specific CLI.
- **Evaluator:** Produce the summary first and verify launch occurs only with an authorized compatible runtime.
- **Consensus:** Do not promote this version. It is in-progress and starts another worker through a Claude-specific CLI. Reconsider after a demonstrated recurring need and a behavioral evaluation.
- **Overlap:** handoff
- **Prerequisites:** Claude CLI, temporary directory

</details>

<details><summary>loop-me — defer</summary>

[Pinned source](https://github.com/mattpocock/skills/blob/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa/skills/in-progress/loop-me/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Separates the recurring loop from the workflow description.
- **Skeptic:** The in-progress life-workflow interview exceeds the default engineering catalog.
- **Evaluator:** Specify a recurring check and distinguish an actual trigger and stop condition from an assumed schedule.
- **Consensus:** Do not promote this version. The in-progress life-workflow interview exceeds the default engineering catalog. Reconsider after a demonstrated recurring need and a behavioral evaluation.
- **Overlap:** grill-idea, wayfinder
- **Prerequisites:** grilling, workflow notes

</details>

<details><summary>setup-ts-deep-modules — defer</summary>

[Pinned source](https://github.com/mattpocock/skills/blob/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa/skills/in-progress/setup-ts-deep-modules/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Turns a chosen architectural seam into an executable import rule.
- **Skeptic:** The in-progress universal package layout can conflict with intentional export structures.
- **Evaluator:** Seed one permitted entry import and one illegal internal import; verify only the latter fails.
- **Consensus:** Do not promote this version. The in-progress universal package layout can conflict with intentional export structures. Reconsider after a demonstrated recurring need and a behavioral evaluation.
- **Overlap:** codebase-design, api-design
- **Prerequisites:** TypeScript, dependency-cruiser, package layout

</details>

<details><summary>writing-beats — defer</summary>

[Pinned source](https://github.com/mattpocock/skills/blob/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa/skills/in-progress/writing-beats/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Preserves user edits and exposes dependencies between explanations.
- **Skeptic:** The in-progress interaction is editorial rather than general engineering delivery.
- **Evaluator:** Edit an earlier beat and verify later choices adapt without overwriting it.
- **Consensus:** Do not promote this version. The in-progress interaction is editorial rather than general engineering delivery. Reconsider after a demonstrated recurring need and a behavioral evaluation.
- **Overlap:** writing-shape, writing-fragments
- **Prerequisites:** Source notes, article file, user choices

</details>

<details><summary>writing-fragments — defer</summary>

[Pinned source](https://github.com/mattpocock/skills/blob/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa/skills/in-progress/writing-fragments/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Keeps exploration separate from premature outlines.
- **Skeptic:** In-progress and designed for creative interviewing rather than product engineering.
- **Evaluator:** Collect disconnected observations without forcing a thesis or changing their meaning.
- **Consensus:** Do not promote this version. In-progress and designed for creative interviewing rather than product engineering. Reconsider after a demonstrated recurring need and a behavioral evaluation.
- **Overlap:** writing-beats, writing-shape
- **Prerequisites:** grilling, chosen notes file

</details>

<details><summary>writing-shape — defer</summary>

[Pinned source](https://github.com/mattpocock/skills/blob/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa/skills/in-progress/writing-shape/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Keeps raw source material read-only and stages concept introduction.
- **Skeptic:** This in-progress workflow overlaps writing-beats and requires repeated editorial decisions.
- **Evaluator:** Supply a raw transcript and verify the source remains unchanged and the article stands alone.
- **Consensus:** Do not promote this version. This in-progress workflow overlaps writing-beats and requires repeated editorial decisions. Reconsider after a demonstrated recurring need and a behavioral evaluation.
- **Overlap:** writing-beats, writing-fragments
- **Prerequisites:** Raw source file, article destination

</details>

<details><summary>git-guardrails-claude-code — profile</summary>

[Pinned source](https://github.com/mattpocock/skills/blob/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa/skills/misc/git-guardrails-claude-code/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Provides an executable accident barrier rather than a reminder.
- **Skeptic:** Regex hooks are harness-specific and may also block authorized routine pushes.
- **Evaluator:** Test allowed commands plus direct and wrapped destructive variants; preserve existing hook settings.
- **Consensus:** Keep available for a matching project rather than the default catalog. Validate the named prerequisites and check: Test allowed commands plus direct and wrapped destructive variants; preserve existing hook settings.
- **Overlap:** global-agent-guardrails
- **Prerequisites:** Claude Code hooks, Bash, hook script

</details>

<details><summary>migrate-to-shoehorn — profile</summary>

[Pinned source](https://github.com/mattpocock/skills/blob/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa/skills/misc/migrate-to-shoehorn/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Targets a concrete test-data maintenance problem.
- **Skeptic:** It adds a library and is valid only for projects choosing this fixture strategy.
- **Evaluator:** Compile partial test fixtures and verify production code receives no shoehorn imports.
- **Consensus:** Keep available for a matching project rather than the default catalog. Validate the named prerequisites and check: Compile partial test fixtures and verify production code receives no shoehorn imports.
- **Overlap:** tdd
- **Prerequisites:** TypeScript, @total-typescript/shoehorn

</details>

<details><summary>scaffold-exercises — reference</summary>

[Pinned source](https://github.com/mattpocock/skills/blob/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa/skills/misc/scaffold-exercises/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Encodes a repeatable educational repository shape.
- **Skeptic:** It assumes pnpm ai-hero-cli and automatically commits; unrelated to ordinary product repos.
- **Evaluator:** Generate one exercise in a matching fixture and run its actual linter without unrelated edits.
- **Consensus:** Retain as a linked reference, not another active trigger. It assumes pnpm ai-hero-cli and automatically commits; unrelated to ordinary product repos.
- **Overlap:** prototype
- **Prerequisites:** AI Hero repository, pnpm, ai-hero-cli

</details>

<details><summary>setup-pre-commit — profile</summary>

[Pinned source](https://github.com/mattpocock/skills/blob/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa/skills/misc/setup-pre-commit/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Makes selected checks run before a commit.
- **Skeptic:** The Node-specific package choices and automatic commit must fit an explicitly requested setup.
- **Evaluator:** Preserve existing hooks and prove a bad staged file blocks a commit while a good one passes.
- **Consensus:** Keep available for a matching project rather than the default catalog. Validate the named prerequisites and check: Preserve existing hooks and prove a bad staged file blocks a commit while a good one passes.
- **Overlap:** constraint-driven-development, global-agent-guardrails
- **Prerequisites:** Node, package manager, Husky, lint-staged, Prettier

</details>

<details><summary>grill-me — reference</summary>

[Pinned source](https://github.com/mattpocock/skills/blob/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa/skills/productivity/grill-me/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** A memorable explicit entry point is easy to request.
- **Skeptic:** It adds no procedure beyond grilling and creates another overlapping trigger.
- **Evaluator:** Invoke it with a clear scope and verify it reaches the same bounded interview as grilling.
- **Consensus:** Retain as a linked reference, not another active trigger. It adds no procedure beyond grilling and creates another overlapping trigger.
- **Overlap:** grilling, grill-with-docs
- **Prerequisites:** grilling, Skill tool

</details>

<details><summary>grilling — adapt</summary>

[Pinned source](https://github.com/mattpocock/skills/blob/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa/skills/productivity/grilling/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** The frontier model exposes which decisions can be made without guessing prerequisites.
- **Skeptic:** A relentless interview can overrun a simple request; current rounds differ from older one-question versions.
- **Evaluator:** Provide settled answers plus one dependent decision and verify only genuinely open frontier questions are asked.
- **Consensus:** Absorb the useful procedure into grill-idea; resolve this source-specific limit before promotion: A relentless interview can overrun a simple request; current rounds differ from older one-question versions. Behavioral benefit remains unmeasured.
- **Overlap:** grill-idea, interview-me, 4x4
- **Prerequisites:** Optional fact-finding subagents

</details>

<details><summary>handoff — adapt</summary>

[Pinned source](https://github.com/mattpocock/skills/blob/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa/skills/productivity/handoff/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Avoids repeating durable artifacts and redacts sensitive values.
- **Skeptic:** A temporary path may be inconvenient for a shared handoff and must be chosen for the actual audience.
- **Evaluator:** A fresh session should resume from the brief without repeating resolved work or reading secrets.
- **Consensus:** Absorb the useful procedure into handoff; resolve this source-specific limit before promotion: A temporary path may be inconvenient for a shared handoff and must be chosen for the actual audience. Behavioral benefit remains unmeasured.
- **Overlap:** handoff, claude-handoff
- **Prerequisites:** Writable handoff destination

</details>

<details><summary>teach — profile</summary>

[Pinned source](https://github.com/mattpocock/skills/blob/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa/skills/productivity/teach/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Supports multi-session learning tied to a learner's mission.
- **Skeptic:** The full teaching workspace is excessive for a single conceptual explanation.
- **Evaluator:** Teach one codebase concept without creating persistent lesson infrastructure unless requested.
- **Consensus:** Keep available for a matching project rather than the default catalog. Validate the named prerequisites and check: Teach one codebase concept without creating persistent lesson infrastructure unless requested.
- **Overlap:** teach, handoff
- **Prerequisites:** Teaching templates, HTML preview, chosen workspace

</details>

<details><summary>to-questionnaire — profile</summary>

[Pinned source](https://github.com/mattpocock/skills/blob/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa/skills/productivity/to-questionnaire/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Targets the recipient's knowledge gap instead of grilling the sender on unknowable facts.
- **Skeptic:** A drafting request does not authorize sending the questionnaire.
- **Evaluator:** Prepare a decision-focused questionnaire that a recipient can answer without this chat.
- **Consensus:** Keep available for a matching project rather than the default catalog. Validate the named prerequisites and check: Prepare a decision-focused questionnaire that a recipient can answer without this chat.
- **Overlap:** grill-idea, ask-then-build
- **Prerequisites:** Recipient role and requested decisions

</details>

<details><summary>wait-what — reference</summary>

[Pinned source](https://github.com/mattpocock/skills/blob/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa/skills/productivity/wait-what/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Provides a quick recovery when an explanation did not land.
- **Skeptic:** A tiny explicit prompt does not justify an always-loaded specialist.
- **Evaluator:** Re-explain a technical result and preserve units, conditions and uncertainty.
- **Consensus:** Retain as a linked reference, not another active trigger. A tiny explicit prompt does not justify an always-loaded specialist.
- **Overlap:** remind, bro
- **Prerequisites:** Existing conversation, optional glossary

</details>

<details><summary>writing-for-agents — adapt</summary>

[Pinned source](https://github.com/mattpocock/skills/blob/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa/skills/productivity/writing-for-agents/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Treats the trigger wording as a separate source of routing failures.
- **Skeptic:** Strong wording alone cannot establish behavioral reliability or invocation precedence across harnesses.
- **Evaluator:** Use positive, negative and neighboring prompts to test the description before enlarging the body.
- **Consensus:** Absorb the useful procedure into skill-maintenance; resolve this source-specific limit before promotion: Strong wording alone cannot establish behavioral reliability or invocation precedence across harnesses. Behavioral benefit remains unmeasured.
- **Overlap:** effective-agent-skills, skill-creator
- **Prerequisites:** SKILL-MECHANICS reference, actual harness

</details>

### addyosmani/agent-skills

<details><summary>api-and-interface-design — adapt</summary>

[Pinned source](https://github.com/addyosmani/agent-skills/blob/eb07f19f52c2669f2364897aaa293e2aaddd7b1c/skills/api-and-interface-design/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Explains who owns retry identity and how callers observe failures.
- **Skeptic:** A broad REST and TypeScript template catalog can distract from a small local interface.
- **Evaluator:** Replay an idempotent request concurrently and verify one operation with consistent responses.
- **Consensus:** Absorb the useful procedure into api-design; resolve this source-specific limit before promotion: A broad REST and TypeScript template catalog can distract from a small local interface. Behavioral benefit remains unmeasured.
- **Overlap:** api-design, codebase-design
- **Prerequisites:** Actual API contracts and stack

</details>

<details><summary>browser-testing-with-devtools — profile</summary>

[Pinned source](https://github.com/addyosmani/agent-skills/blob/eb07f19f52c2669f2364897aaa293e2aaddd7b1c/skills/browser-testing-with-devtools/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Connects DOM, console, network and screenshot evidence to a UI symptom.
- **Skeptic:** It assumes a specific MCP and broad activation for any browser work.
- **Evaluator:** Reproduce a network-driven UI failure in an isolated profile and verify evidence without using personal sessions.
- **Consensus:** Keep available for a matching project rather than the default catalog. Validate the named prerequisites and check: Reproduce a network-driven UI failure in an isolated profile and verify evidence without using personal sessions.
- **Overlap:** verify-change, browser-use, ui-review
- **Prerequisites:** Chrome DevTools MCP, isolated test profile

</details>

<details><summary>ci-cd-and-automation — profile</summary>

[Pinned source](https://github.com/addyosmani/agent-skills/blob/eb07f19f52c2669f2364897aaa293e2aaddd7b1c/skills/ci-cd-and-automation/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Turns agreed quality criteria into repeatable CI gates.
- **Skeptic:** Example Node, database and deployment snippets require adaptation and operational authority.
- **Evaluator:** Break one project check deliberately and verify CI blocks the change using the repository's real commands.
- **Consensus:** Keep available for a matching project rather than the default catalog. Validate the named prerequisites and check: Break one project check deliberately and verify CI blocks the change using the repository's real commands.
- **Overlap:** constraint-driven-development, setup-pre-commit
- **Prerequisites:** CI provider, project runners, configured secrets

</details>

<details><summary>code-review-and-quality — adapt</summary>

[Pinned source](https://github.com/addyosmani/agent-skills/blob/eb07f19f52c2669f2364897aaa293e2aaddd7b1c/skills/code-review-and-quality/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Verifies that reported checks actually establish the claimed behavior.
- **Skeptic:** Always-review and multi-model defaults add cost and may overreach trivial changes.
- **Evaluator:** Review a clean diff and a seeded regression; accept no findings on the former and prove the latter.
- **Consensus:** Absorb the useful procedure into review; resolve this source-specific limit before promotion: Always-review and multi-model defaults add cost and may overreach trivial changes. Behavioral benefit remains unmeasured.
- **Overlap:** review, code-review, interrogate
- **Prerequisites:** Diff and acceptance context, optional reviewers

</details>

<details><summary>code-simplification — adapt</summary>

[Pinned source](https://github.com/addyosmani/agent-skills/blob/eb07f19f52c2669f2364897aaa293e2aaddd7b1c/skills/code-simplification/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Explicitly rejects line-count optimization and unscoped cleanup.
- **Skeptic:** Dead-code removal requires proof and must stay within the requested scope.
- **Evaluator:** Refactor a fixture with edge-case behavior and compare public outputs before and after.
- **Consensus:** Absorb the useful procedure into simplify; resolve this source-specific limit before promotion: Dead-code removal requires proof and must stay within the requested scope. Behavioral benefit remains unmeasured.
- **Overlap:** simplify, minimalist
- **Prerequisites:** Project checks and observable behavior

</details>

<details><summary>constraint-driven-development — adapt</summary>

[Pinned source](https://github.com/addyosmani/agent-skills/blob/eb07f19f52c2669f2364897aaa293e2aaddd7b1c/skills/constraint-driven-development/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Distinguishes measured dimensions from enforced floors and catches suppressions.
- **Skeptic:** Default numerical targets are hypotheses and may not fit the project; setup can be intrusive.
- **Evaluator:** Try lowering a threshold or skipping a failing test and verify the change is surfaced rather than accepted as progress.
- **Consensus:** Absorb the useful procedure into skill-maintenance; resolve this source-specific limit before promotion: Default numerical targets are hypotheses and may not fit the project; setup can be intrusive. Behavioral benefit remains unmeasured.
- **Overlap:** verify-change, correct, retro
- **Prerequisites:** Project checks, CONSTRAINTS.md, selected tooling

</details>

<details><summary>context-engineering — adapt</summary>

[Pinned source](https://github.com/addyosmani/agent-skills/blob/eb07f19f52c2669f2364897aaa293e2aaddd7b1c/skills/context-engineering/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Preserves durable decisions and uses restartable boundaries for long tasks.
- **Skeptic:** The broad session-start trigger duplicates harness behavior and other routers.
- **Evaluator:** Resume a long task from bounded pointers and verify no loss of authorization or open blockers.
- **Consensus:** Absorb the useful procedure into handoff; resolve this source-specific limit before promotion: The broad session-start trigger duplicates harness behavior and other routers. Behavioral benefit remains unmeasured.
- **Overlap:** handoff, start, writing-for-agents
- **Prerequisites:** Project instructions and artifacts

</details>

<details><summary>debugging-and-error-recovery — adapt</summary>

[Pinned source](https://github.com/addyosmani/agent-skills/blob/eb07f19f52c2669f2364897aaa293e2aaddd7b1c/skills/debugging-and-error-recovery/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Includes error-specific triage and end-to-end confirmation.
- **Skeptic:** A universal stop-the-line rule can be disproportionate to an unrelated known failure.
- **Evaluator:** Seed a failing symptom plus an unrelated existing test failure and keep attribution separate.
- **Consensus:** Absorb the useful procedure into debug; resolve this source-specific limit before promotion: A universal stop-the-line rule can be disproportionate to an unrelated known failure. Behavioral benefit remains unmeasured.
- **Overlap:** debug, diagnosing-bugs
- **Prerequisites:** Reproduction and project tools

</details>

<details><summary>deprecation-and-migration — profile</summary>

[Pinned source](https://github.com/addyosmani/agent-skills/blob/eb07f19f52c2669f2364897aaa293e2aaddd7b1c/skills/deprecation-and-migration/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Expand-contract protects mixed-version rollouts.
- **Skeptic:** Migration steps must be checked against real consumers, rollback limits and deployment ownership.
- **Evaluator:** Run old and new clients during a schema transition and verify both remain valid before contraction.
- **Consensus:** Keep available for a matching project rather than the default catalog. Validate the named prerequisites and check: Run old and new clients during a schema transition and verify both remain valid before contraction.
- **Overlap:** change-plan, api-design
- **Prerequisites:** Consumer inventory, migration environment, rollout policy

</details>

<details><summary>documentation-and-adrs — adapt</summary>

[Pinned source](https://github.com/addyosmani/agent-skills/blob/eb07f19f52c2669f2364897aaa293e2aaddd7b1c/skills/documentation-and-adrs/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Matches established conventions and avoids comments that restate code.
- **Skeptic:** Mandatory docs for every feature would create low-value maintenance work.
- **Evaluator:** Document a real changed contract and verify commands and limitations against code.
- **Consensus:** Absorb the useful procedure into docs; resolve this source-specific limit before promotion: Mandatory docs for every feature would create low-value maintenance work. Behavioral benefit remains unmeasured.
- **Overlap:** docs, domain-model, adr-verbatim
- **Prerequisites:** Existing docs and decision evidence

</details>

<details><summary>doubt-driven-development — adapt</summary>

[Pinned source](https://github.com/addyosmani/agent-skills/blob/eb07f19f52c2669f2364897aaa293e2aaddd7b1c/skills/doubt-driven-development/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Makes claims and contracts explicit before a reviewer sees the artifact.
- **Skeptic:** Invoking a fresh model for every branch is costly; self-questioning is not independent review.
- **Evaluator:** Hide a specification defect from the reviewer and check whether a fresh review finds it without seeing the expected answer.
- **Consensus:** Absorb the useful procedure into review; resolve this source-specific limit before promotion: Invoking a fresh model for every branch is costly; self-questioning is not independent review. Behavioral benefit remains unmeasured.
- **Overlap:** review, interrogate, simulate-discussion
- **Prerequisites:** Independent reviewer runtime when available

</details>

<details><summary>frontend-ui-engineering — profile</summary>

[Pinned source](https://github.com/addyosmani/agent-skills/blob/eb07f19f52c2669f2364897aaa293e2aaddd7b1c/skills/frontend-ui-engineering/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Covers missing error, empty and loading states as product behavior.
- **Skeptic:** Its broad trigger and component templates overlap specialist UI skills and may impose structure.
- **Evaluator:** Exercise keyboard, narrow viewport and failure states using the existing component system.
- **Consensus:** Keep available for a matching project rather than the default catalog. Validate the named prerequisites and check: Exercise keyboard, narrow viewport and failure states using the existing component system.
- **Overlap:** ui-review, baseline-ui, better-interface
- **Prerequisites:** Frontend stack, browser, design system

</details>

<details><summary>git-workflow-and-versioning — reference</summary>

[Pinned source](https://github.com/addyosmani/agent-skills/blob/eb07f19f52c2669f2364897aaa293e2aaddd7b1c/skills/git-workflow-and-versioning/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Separates concerns and explains worktree isolation.
- **Skeptic:** An always-on Git workflow can conflict with the team's branching policy and existing authorization.
- **Evaluator:** Separate mixed work without losing user changes or pushing without a request.
- **Consensus:** Retain as a linked reference, not another active trigger. An always-on Git workflow can conflict with the team's branching policy and existing authorization.
- **Overlap:** new-feature, git-worktree, merge-conflicts
- **Prerequisites:** Git, repository workflow

</details>

<details><summary>idea-refine — adapt</summary>

[Pinned source](https://github.com/addyosmani/agent-skills/blob/eb07f19f52c2669f2364897aaa293e2aaddd7b1c/skills/idea-refine/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Separates option generation from selecting a direction.
- **Skeptic:** An extra interview skill competes with interview-me and already settled decisions.
- **Evaluator:** Refine an unclear idea while preserving explicit constraints and stopping at the requested artifact.
- **Consensus:** Absorb the useful procedure into grill-idea; resolve this source-specific limit before promotion: An extra interview skill competes with interview-me and already settled decisions. Behavioral benefit remains unmeasured.
- **Overlap:** grill-idea, interview-me, grilling
- **Prerequisites:** Product context, optional idea document

</details>

<details><summary>incremental-implementation — adapt</summary>

[Pinned source](https://github.com/addyosmani/agent-skills/blob/eb07f19f52c2669f2364897aaa293e2aaddd7b1c/skills/incremental-implementation/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Keeps each increment compilable and tied to a user-visible capability.
- **Skeptic:** Automatic commits and feature flags for every incomplete slice may add unnecessary machinery.
- **Evaluator:** Build one vertical slice and prove it works before expanding the next.
- **Consensus:** Absorb the useful procedure into change-plan; resolve this source-specific limit before promotion: Automatic commits and feature flags for every incomplete slice may add unnecessary machinery. Behavioral benefit remains unmeasured.
- **Overlap:** change-plan, to-tickets
- **Prerequisites:** Project build and tests, optional feature flags

</details>

<details><summary>interview-me — adapt</summary>

[Pinned source](https://github.com/addyosmani/agent-skills/blob/eb07f19f52c2669f2364897aaa293e2aaddd7b1c/skills/interview-me/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Checks whether a requested solution solves the intended problem.
- **Skeptic:** A claimed 95% confidence is subjective and the mandatory terminal stop can interrupt authorized implementation.
- **Evaluator:** Give a settled scope and verify it does not restart an interview; clarify only a consequential ambiguity.
- **Consensus:** Absorb the useful procedure into grill-idea; resolve this source-specific limit before promotion: A claimed 95% confidence is subjective and the mandatory terminal stop can interrupt authorized implementation. Behavioral benefit remains unmeasured.
- **Overlap:** grill-idea, grilling, ask-then-build
- **Prerequisites:** User decisions, available project facts

</details>

<details><summary>observability-and-instrumentation — adapt</summary>

[Pinned source](https://github.com/addyosmani/agent-skills/blob/eb07f19f52c2669f2364897aaa293e2aaddd7b1c/skills/observability-and-instrumentation/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Distinguishes correlation identity from the entry point that started work.
- **Skeptic:** Instrumenting every feature indiscriminately creates noise, cost and privacy exposure.
- **Evaluator:** Follow one failed request across boundaries and prove the telemetry answers the diagnostic question without sensitive payloads.
- **Consensus:** Absorb the useful procedure into debug; resolve this source-specific limit before promotion: Instrumenting every feature indiscriminately creates noise, cost and privacy exposure. Behavioral benefit remains unmeasured.
- **Overlap:** debug, verify-change
- **Prerequisites:** Existing telemetry stack, retention and data policy

</details>

<details><summary>performance-optimization — profile</summary>

[Pinned source](https://github.com/addyosmani/agent-skills/blob/eb07f19f52c2669f2364897aaa293e2aaddd7b1c/skills/performance-optimization/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Checks cache keys, correctness and repeatable before/after measurement.
- **Skeptic:** Generic budgets cannot establish the actual user environment or rule out benchmark artifacts.
- **Evaluator:** Compare representative workloads with repeated timings and a correctness oracle.
- **Consensus:** Keep available for a matching project rather than the default catalog. Validate the named prerequisites and check: Compare representative workloads with repeated timings and a correctness oracle.
- **Overlap:** debug, animation-performance
- **Prerequisites:** Profiler, representative workload, baseline

</details>

<details><summary>planning-and-task-breakdown — adapt</summary>

[Pinned source](https://github.com/addyosmani/agent-skills/blob/eb07f19f52c2669f2364897aaa293e2aaddd7b1c/skills/planning-and-task-breakdown/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Protects incomplete plans from accidental overwrite.
- **Skeptic:** Mandatory plan mode and fixed tasks paths are harness and repository choices.
- **Evaluator:** Plan work alongside an existing incomplete plan without replacing or silently merging it.
- **Consensus:** Absorb the useful procedure into change-plan; resolve this source-specific limit before promotion: Mandatory plan mode and fixed tasks paths are harness and repository choices. Behavioral benefit remains unmeasured.
- **Overlap:** change-plan, to-tickets, wayfinder
- **Prerequisites:** Existing plan convention, optional tracker

</details>

<details><summary>security-and-hardening — profile</summary>

[Pinned source](https://github.com/addyosmani/agent-skills/blob/eb07f19f52c2669f2364897aaa293e2aaddd7b1c/skills/security-and-hardening/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Includes SSRF, access control, secrets and derived-path destruction.
- **Skeptic:** Its near-universal trigger and broad approval taxonomy can exceed a normal code edit.
- **Evaluator:** Audit a concrete trust boundary with an exploit or negative test and distinguish proven flaws from possibilities.
- **Consensus:** Keep available for a matching project rather than the default catalog. Validate the named prerequisites and check: Audit a concrete trust boundary with an exploit or negative test and distinguish proven flaws from possibilities.
- **Overlap:** review, security review specialists
- **Prerequisites:** Stack-specific security guidance, test environment

</details>

<details><summary>shipping-and-launch — profile</summary>

[Pinned source](https://github.com/addyosmani/agent-skills/blob/eb07f19f52c2669f2364897aaa293e2aaddd7b1c/skills/shipping-and-launch/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Separates deployment from release and defines abort conditions.
- **Skeptic:** A deployment checklist does not grant production access or permission to launch.
- **Evaluator:** Rehearse rollback and verify health criteria with a realistic staging failure.
- **Consensus:** Keep available for a matching project rather than the default catalog. Validate the named prerequisites and check: Rehearse rollback and verify health criteria with a realistic staging failure.
- **Overlap:** verify-change, ci-cd-and-automation
- **Prerequisites:** Deployment owner, staging, monitoring, rollback path

</details>

<details><summary>source-driven-development — adapt</summary>

[Pinned source](https://github.com/addyosmani/agent-skills/blob/eb07f19f52c2669f2364897aaa293e2aaddd7b1c/skills/source-driven-development/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Starts with installed stack versions and treats fetched prose as untrusted instructions.
- **Skeptic:** Requiring a citation for every framework decision can waste time on stable or locally evidenced facts.
- **Evaluator:** Resolve an API mismatch using the installed version and cite the relevant primary contract.
- **Consensus:** Absorb the useful procedure into research; resolve this source-specific limit before promotion: Requiring a citation for every framework decision can waste time on stable or locally evidenced facts. Behavioral benefit remains unmeasured.
- **Overlap:** research, effective-agent-skills
- **Prerequisites:** Installed versions, official documentation access

</details>

<details><summary>spec-driven-development — adapt</summary>

[Pinned source](https://github.com/addyosmani/agent-skills/blob/eb07f19f52c2669f2364897aaa293e2aaddd7b1c/skills/spec-driven-development/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Separates multi-capability scope before planning implementation.
- **Skeptic:** The mandatory stop after each artifact conflicts with a user already authorizing the whole delivery.
- **Evaluator:** Create a spec for agreed work and continue only through activities already included in the user's scope.
- **Consensus:** Absorb the useful procedure into change-plan; resolve this source-specific limit before promotion: The mandatory stop after each artifact conflicts with a user already authorizing the whole delivery. Behavioral benefit remains unmeasured.
- **Overlap:** change-plan, to-spec
- **Prerequisites:** Project conventions, acceptance criteria

</details>

<details><summary>test-driven-development — adapt</summary>

[Pinned source](https://github.com/addyosmani/agent-skills/blob/eb07f19f52c2669f2364897aaa293e2aaddd7b1c/skills/test-driven-development/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Discovers the actual project runner and verifies the red-to-green transition.
- **Skeptic:** Its any-logic trigger is broader than requested TDD and duplicates browser-test guidance.
- **Evaluator:** Add a defect-catching test with an independent expected result and prove it fails before the fix.
- **Consensus:** Absorb the useful procedure into tdd; resolve this source-specific limit before promotion: Its any-logic trigger is broader than requested TDD and duplicates browser-test guidance. Behavioral benefit remains unmeasured.
- **Overlap:** tdd, diagnosing-bugs
- **Prerequisites:** Project test runner, optional browser tools

</details>

<details><summary>using-agent-skills — reference</summary>

[Pinned source](https://github.com/addyosmani/agent-skills/blob/eb07f19f52c2669f2364897aaa293e2aaddd7b1c/skills/using-agent-skills/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Makes the collection's intended routing visible.
- **Skeptic:** A second all-session router competes with start and poteto-mode.
- **Evaluator:** Route a research-only request without forcing planning, implementation or deployment.
- **Consensus:** Retain as a linked reference, not another active trigger. A second all-session router competes with start and poteto-mode.
- **Overlap:** start, ask-matt, poteto-mode
- **Prerequisites:** Sibling skills

</details>

### emilkowalski/skills

<details><summary>animate — profile</summary>

[Pinned source](https://github.com/emilkowalski/skills/blob/a81dbca07f2217b7103e510c0f13f8d5b017afc9/skills/animate/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Orders decisions from user purpose through mechanism and accessibility.
- **Skeptic:** Fixed curves and a never-animate frequency rule turn taste into universal requirements.
- **Evaluator:** Exercise rapid repeated interactions and reduced motion, checking continuity and user task latency.
- **Consensus:** Keep available for a matching project rather than the default catalog. Validate the named prerequisites and check: Exercise rapid repeated interactions and reduced motion, checking continuity and user task latency.
- **Overlap:** ui-review, better-ui, review-animations
- **Prerequisites:** Web runtime, optional motion library

</details>

<details><summary>animate-expo — profile</summary>

[Pinned source](https://github.com/emilkowalski/skills/blob/a81dbca07f2217b7103e510c0f13f8d5b017afc9/skills/animate-expo/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Accounts for UI versus JS threads and gesture handoff.
- **Skeptic:** Platform versions and blanket tab-motion rules require project-specific validation.
- **Evaluator:** Profile a gesture on real target hardware with accessibility settings enabled.
- **Consensus:** Keep available for a matching project rather than the default catalog. Validate the named prerequisites and check: Profile a gesture on real target hardware with accessibility settings enabled.
- **Overlap:** animate, animation-performance
- **Prerequisites:** Expo, Reanimated, Gesture Handler, device

</details>

<details><summary>animation-performance — profile</summary>

[Pinned source](https://github.com/emilkowalski/skills/blob/a81dbca07f2217b7103e510c0f13f8d5b017afc9/skills/animation-performance/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Separates visual taste from measurable frame cost.
- **Skeptic:** Compositor eligibility depends on the actual browser, property values and scene.
- **Evaluator:** Capture a trace under representative load and compare dropped frames after one change.
- **Consensus:** Keep available for a matching project rather than the default catalog. Validate the named prerequisites and check: Capture a trace under representative load and compare dropped frames after one change.
- **Overlap:** fixing-motion-performance, performance-optimization
- **Prerequisites:** Browser profiler, representative device

</details>

<details><summary>animation-vocabulary — reference</summary>

[Pinned source](https://github.com/emilkowalski/skills/blob/a81dbca07f2217b7103e510c0f13f8d5b017afc9/skills/animation-vocabulary/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Useful for translating vague requests into a shared term.
- **Skeptic:** A lookup reference need not be a separately active workflow.
- **Evaluator:** Describe a motion ambiguously and return likely terms with distinguishing cues rather than false certainty.
- **Consensus:** Retain as a linked reference, not another active trigger. A lookup reference need not be a separately active workflow.
- **Overlap:** docs, explain-interface
- **Prerequisites:** Optional reference image or video

</details>

<details><summary>apple-design — profile</summary>

[Pinned source](https://github.com/emilkowalski/skills/blob/a81dbca07f2217b7103e510c0f13f8d5b017afc9/skills/apple-design/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Explains velocity handoff, spatial consistency and gesture response.
- **Skeptic:** Apple-inspired aesthetic choices do not establish the product's design or accessibility requirements.
- **Evaluator:** Test interrupted drag, keyboard alternatives and reduced motion against the existing product behavior.
- **Consensus:** Keep available for a matching project rather than the default catalog. Validate the named prerequisites and check: Test interrupted drag, keyboard alternatives and reduced motion against the existing product behavior.
- **Overlap:** animate, better-ui
- **Prerequisites:** Pointer events, motion implementation, browser

</details>

<details><summary>ask-sonner — profile</summary>

[Pinned source](https://github.com/emilkowalski/skills/blob/a81dbca07f2217b7103e510c0f13f8d5b017afc9/skills/ask-sonner/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Makes duplicate Toaster mounting and lifecycle mistakes concrete.
- **Skeptic:** It is useful only for the installed Sonner version and actual toast requirements.
- **Evaluator:** Mount and update one toast across loading, success and dismissal without duplicates.
- **Consensus:** Keep available for a matching project rather than the default catalog. Validate the named prerequisites and check: Mount and update one toast across loading, success and dismissal without duplicates.
- **Overlap:** ui-review
- **Prerequisites:** React, Sonner

</details>

<details><summary>break-ui — adapt</summary>

[Pinned source](https://github.com/emilkowalski/skills/blob/a81dbca07f2217b7103e510c0f13f8d5b017afc9/skills/break-ui/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Uses realistic long, missing, translated and extreme data.
- **Skeptic:** Adding a production-visible demo toggle can leak fixtures or expand a review request.
- **Evaluator:** Render long translated labels and missing values in an isolated fixture with no live data effects.
- **Consensus:** Absorb the useful procedure into ui-review; resolve this source-specific limit before promotion: Adding a production-visible demo toggle can leak fixtures or expand a review request. Behavioral benefit remains unmeasured.
- **Overlap:** break, state-machine, verify-change
- **Prerequisites:** Component fixtures, browser

</details>

<details><summary>emil-design-eng — reference</summary>

[Pinned source](https://github.com/emilkowalski/skills/blob/a81dbca07f2217b7103e510c0f13f8d5b017afc9/skills/emil-design-eng/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Collects interaction details that generic code review often misses.
- **Skeptic:** It duplicates narrower skills and mandates a style or report shape even when irrelevant.
- **Evaluator:** Audit an established design and suppress findings based only on differing taste.
- **Consensus:** Retain as a linked reference, not another active trigger. It duplicates narrower skills and mandates a style or report shape even when irrelevant.
- **Overlap:** better-interface, baseline-ui, ui-review
- **Prerequisites:** Design context, browser

</details>

<details><summary>find-animation-opportunities — profile</summary>

[Pinned source](https://github.com/emilkowalski/skills/blob/a81dbca07f2217b7103e510c0f13f8d5b017afc9/skills/find-animation-opportunities/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Requires candidates to pass frequency, purpose, speed and functional gates.
- **Skeptic:** Exact recipe values remain hypotheses and can compete with the product's motion language.
- **Evaluator:** Give a high-frequency shortcut and verify no decorative animation is proposed.
- **Consensus:** Keep available for a matching project rather than the default catalog. Validate the named prerequisites and check: Give a high-frequency shortcut and verify no decorative animation is proposed.
- **Overlap:** animate, remove-animations
- **Prerequisites:** Code or rendered UI

</details>

<details><summary>improve-animations — profile</summary>

[Pinned source](https://github.com/emilkowalski/skills/blob/a81dbca07f2217b7103e510c0f13f8d5b017afc9/skills/improve-animations/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Separates advisor work from applying code changes.
- **Skeptic:** Parallel audits and self-contained plan files add overhead and duplicate review-animations.
- **Evaluator:** Audit one complete flow and prove source remains unchanged while selected plans contain testable outcomes.
- **Consensus:** Keep available for a matching project rather than the default catalog. Validate the named prerequisites and check: Audit one complete flow and prove source remains unchanged while selected plans contain testable outcomes.
- **Overlap:** review-animations, ui-review
- **Prerequisites:** Motion code, browser, optional subagents

</details>

<details><summary>mobile-native — profile</summary>

[Pinned source](https://github.com/emilkowalski/skills/blob/a81dbca07f2217b7103e510c0f13f8d5b017afc9/skills/mobile-native/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Focuses on platform defects that desktop emulation misses.
- **Skeptic:** Removing native selection or zoom can harm usability if treated as cosmetic defaults.
- **Evaluator:** Test the target mobile browser with zoom, safe areas, keyboard and touch gestures.
- **Consensus:** Keep available for a matching project rather than the default catalog. Validate the named prerequisites and check: Test the target mobile browser with zoom, safe areas, keyboard and touch gestures.
- **Overlap:** better-accessibility, frontend-ui-engineering
- **Prerequisites:** Real mobile hardware, web app

</details>

<details><summary>pick-ui-library — reference</summary>

[Pinned source](https://github.com/emilkowalski/skills/blob/a81dbca07f2217b7103e510c0f13f8d5b017afc9/skills/pick-ui-library/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Checks installed dependencies before proposing churn.
- **Skeptic:** A curated preference list is not evidence of current maintenance, compatibility or best fit.
- **Evaluator:** For an already-solved dependency need, reuse the installed library and verify current compatibility.
- **Consensus:** Retain as a linked reference, not another active trigger. A curated preference list is not evidence of current maintenance, compatibility or best fit.
- **Overlap:** research, minimalist
- **Prerequisites:** package.json, current library documentation

</details>

<details><summary>prototype — profile</summary>

[Pinned source](https://github.com/emilkowalski/skills/blob/a81dbca07f2217b7103e510c0f13f8d5b017afc9/skills/prototype/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Makes visual tradeoffs tangible instead of describing superficial alternatives.
- **Skeptic:** It changes the real page and shares a name with Matt's question-driven throwaway prototype.
- **Evaluator:** Create three structurally different variants and remove temporary picker code after selection.
- **Consensus:** Keep available for a matching project rather than the default catalog. Validate the named prerequisites and check: Create three structurally different variants and remove temporary picker code after selection.
- **Overlap:** prototype, variant, component-canvas
- **Prerequisites:** Frontend app, browser, user selection

</details>

<details><summary>remove-animations — profile</summary>

[Pinned source](https://github.com/emilkowalski/skills/blob/a81dbca07f2217b7103e510c0f13f8d5b017afc9/skills/remove-animations/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Treats high-frequency friction and hidden start states as removal hazards.
- **Skeptic:** Subtraction can still break state transitions, focus or perceived continuity.
- **Evaluator:** Remove one transition and verify final visibility, focus and reduced-motion behavior remain correct.
- **Consensus:** Keep available for a matching project rather than the default catalog. Validate the named prerequisites and check: Remove one transition and verify final visibility, focus and reduced-motion behavior remain correct.
- **Overlap:** find-animation-opportunities, animate
- **Prerequisites:** Motion source, behavioral checks

</details>

<details><summary>review-animations — adapt</summary>

[Pinned source](https://github.com/emilkowalski/skills/blob/a81dbca07f2217b7103e510c0f13f8d5b017afc9/skills/review-animations/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Keeps scope to motion and points to detailed standards only when needed.
- **Skeptic:** Default-to-flag posture and exact craft values can generate subjective blockers.
- **Evaluator:** Review a deliberate product easing choice and require a demonstrated failure before blocking it.
- **Consensus:** Absorb the useful procedure into ui-review; resolve this source-specific limit before promotion: Default-to-flag posture and exact craft values can generate subjective blockers. Behavioral benefit remains unmeasured.
- **Overlap:** ui-review, better-ui, animation-performance
- **Prerequisites:** Motion diff, STANDARDS.md, browser

</details>

<details><summary>write-swift — profile</summary>

[Pinned source](https://github.com/emilkowalski/skills/blob/a81dbca07f2217b7103e510c0f13f8d5b017afc9/skills/write-swift/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Connects actor reentrancy, Sendable and lifetime semantics to concrete code risks.
- **Skeptic:** It claims a specific Swift toolchain baseline; language features must match installed compiler support.
- **Evaluator:** Compile representative code on the project's toolchain and test the suspected race or lifetime issue.
- **Consensus:** Keep available for a matching project rather than the default catalog. Validate the named prerequisites and check: Compile representative code on the project's toolchain and test the suspected race or lifetime issue.
- **Overlap:** api-design, debug, tdd
- **Prerequisites:** Swift toolchain, platform SDK, Swift Testing

</details>

### jakubkrehel/skills

<details><summary>better-accessibility — adapt</summary>

[Pinned source](https://github.com/jakubkrehel/skills/blob/592aedc44d7d5b3e29740984252902f3e5402a1c/skills/better-accessibility/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Separates actual A or AA failures from larger-target and heading heuristics.
- **Skeptic:** A source checklist cannot replace keyboard and assistive-technology verification.
- **Evaluator:** Complete a dialog flow by keyboard and screen reader, including error announcement and focus restoration.
- **Consensus:** Absorb the useful procedure into ui-review; resolve this source-specific limit before promotion: A source checklist cannot replace keyboard and assistive-technology verification. Behavioral benefit remains unmeasured.
- **Overlap:** fixing-accessibility, ui-review
- **Prerequisites:** Browser, assistive technology, WCAG evidence

</details>

<details><summary>better-colors — adapt</summary>

[Pinned source](https://github.com/jakubkrehel/skills/blob/592aedc44d7d5b3e29740984252902f3e5402a1c/skills/better-colors/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Current source forbids guessed contrast values and treats notation as a project choice.
- **Skeptic:** One-filled-action and fixed ramp preferences remain contextual design guidance.
- **Evaluator:** Compute a rendered failing pair and preserve a different but valid existing token notation.
- **Consensus:** Absorb the useful procedure into ui-review; resolve this source-specific limit before promotion: One-filled-action and fixed ramp preferences remain contextual design guidance. Behavioral benefit remains unmeasured.
- **Overlap:** better-accessibility, better-ui
- **Prerequisites:** Color computation, rendered styles, design tokens

</details>

<details><summary>better-interface — adapt</summary>

[Pinned source](https://github.com/jakubkrehel/skills/blob/592aedc44d7d5b3e29740984252902f3e5402a1c/skills/better-interface/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Distinguishes user impact from personal taste and names uninspected scope.
- **Skeptic:** Its handoff to explicit-only interface-review can interrupt a change review unnecessarily.
- **Evaluator:** Review one flow and consolidate repeated symptoms into one evidenced systemic finding.
- **Consensus:** Absorb the useful procedure into ui-review; resolve this source-specific limit before promotion: Its handoff to explicit-only interface-review can interrupt a change review unnecessarily. Behavioral benefit remains unmeasured.
- **Overlap:** ui-review, interface-review, better-*
- **Prerequisites:** Sibling domain skills, rendered evidence

</details>

<details><summary>better-layout — adapt</summary>

[Pinned source](https://github.com/jakubkrehel/skills/blob/592aedc44d7d5b3e29740984252902f3e5402a1c/skills/better-layout/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Requires visible clipping, overlap or reading-order failure for findings.
- **Skeptic:** Default spacing numbers should not override an established density system.
- **Evaluator:** Resize and mirror a translated fixture, then prove the reported failure in the DOM and rendering.
- **Consensus:** Absorb the useful procedure into ui-review; resolve this source-specific limit before promotion: Default spacing numbers should not override an established density system. Behavioral benefit remains unmeasured.
- **Overlap:** better-ui, baseline-ui
- **Prerequisites:** Browser, design tokens, translated fixtures

</details>

<details><summary>better-typography — profile</summary>

[Pinned source](https://github.com/jakubkrehel/skills/blob/592aedc44d7d5b3e29740984252902f3e5402a1c/skills/better-typography/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Connects typography to measurable clipping and access to truncated text.
- **Skeptic:** Several exact font-weight and measure thresholds are aesthetic heuristics rather than universal defects.
- **Evaluator:** Stress long text and text zoom while preserving the existing font and intentional scale.
- **Consensus:** Keep available for a matching project rather than the default catalog. Validate the named prerequisites and check: Stress long text and text zoom while preserving the existing font and intentional scale.
- **Overlap:** better-writing, better-layout
- **Prerequisites:** Rendered fonts, styles, browser

</details>

<details><summary>better-ui — profile</summary>

[Pinned source](https://github.com/jakubkrehel/skills/blob/592aedc44d7d5b3e29740984252902f3e5402a1c/skills/better-ui/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Places interaction failures above decorative polish.
- **Skeptic:** Exact press scale and easing values can conflict with an existing valid design system.
- **Evaluator:** Compare interaction quality using existing tokens and flag only observable defects or documented convention violations.
- **Consensus:** Keep available for a matching project rather than the default catalog. Validate the named prerequisites and check: Compare interaction quality using existing tokens and flag only observable defects or documented convention violations.
- **Overlap:** review-animations, baseline-ui
- **Prerequisites:** Design system, browser

</details>

<details><summary>better-writing — adapt</summary>

[Pinned source](https://github.com/jakubkrehel/skills/blob/592aedc44d7d5b3e29740984252902f3e5402a1c/skills/better-writing/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Preserves brand voice and requires errors to offer a usable next action.
- **Skeptic:** Broad prose cleanup can alter product promises or established terminology.
- **Evaluator:** Rewrite a failure message without changing its cause, recovery action or contractual claim.
- **Consensus:** Absorb the useful procedure into docs; resolve this source-specific limit before promotion: Broad prose cleanup can alter product promises or established terminology. Behavioral benefit remains unmeasured.
- **Overlap:** docs, domain-model, unslop prose
- **Prerequisites:** Product strings, domain vocabulary

</details>

<details><summary>break — profile</summary>

[Pinned source](https://github.com/jakubkrehel/skills/blob/592aedc44d7d5b3e29740984252902f3e5402a1c/skills/break/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Uses fixture data and marks observable breaks rather than taste judgments.
- **Skeptic:** A single visual skim cannot establish interactive, keyboard or asynchronous behavior.
- **Evaluator:** Seed a long-label overflow and a focus defect; report visual coverage separately from interactive coverage.
- **Consensus:** Keep available for a matching project rather than the default catalog. Validate the named prerequisites and check: Seed a long-label overflow and a focus defect; report visual coverage separately from interactive coverage.
- **Overlap:** break-ui, state-machine
- **Prerequisites:** Component harness, browser, scenarios reference

</details>

<details><summary>build-design — profile</summary>

[Pinned source](https://github.com/jakubkrehel/skills/blob/592aedc44d7d5b3e29740984252902f3e5402a1c/skills/build-design/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Separates design measurements from invented styling.
- **Skeptic:** Removing loading or error states absent from the mockup can delete necessary runtime behavior.
- **Evaluator:** Match a screenshot while preserving real loading, error and accessibility states missing from the image.
- **Consensus:** Keep available for a matching project rather than the default catalog. Validate the named prerequisites and check: Match a screenshot while preserving real loading, error and accessibility states missing from the image.
- **Overlap:** prototype, image-to-code workflows
- **Prerequisites:** Design source, Figma or image access, frontend app

</details>

<details><summary>explain-interface — reference</summary>

[Pinned source](https://github.com/jakubkrehel/skills/blob/592aedc44d7d5b3e29740984252902f3e5402a1c/skills/explain-interface/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Distinguishes measured, derived and inferred properties and distrusts page instructions.
- **Skeptic:** A screenshot supports reconstruction rather than exact recovery of hidden implementation.
- **Evaluator:** Explain a layered gradient while marking unobservable CSS or structure as inferred.
- **Consensus:** Retain as a linked reference, not another active trigger. A screenshot supports reconstruction rather than exact recovery of hidden implementation.
- **Overlap:** research, animation-vocabulary
- **Prerequisites:** Browser or supplied screenshot

</details>

<details><summary>interface-review — adapt</summary>

[Pinned source](https://github.com/jakubkrehel/skills/blob/592aedc44d7d5b3e29740984252902f3e5402a1c/skills/interface-review/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Reads removed lines and maps changed code to affected rendered surfaces.
- **Skeptic:** It depends on several sibling review skills and can confuse empty scope with approval unless checked.
- **Evaluator:** Give a clean tree and no target; expect a missing-scope report, not a guessed last-commit review.
- **Consensus:** Absorb the useful procedure into ui-review; resolve this source-specific limit before promotion: It depends on several sibling review skills and can confuse empty scope with approval unless checked. Behavioral benefit remains unmeasured.
- **Overlap:** review, better-interface
- **Prerequisites:** Git, diff, better-* skills

</details>

<details><summary>state-machine — profile</summary>

[Pinned source](https://github.com/jakubkrehel/skills/blob/592aedc44d7d5b3e29740984252902f3e5402a1c/skills/state-machine/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Enumerates actual branch combinations without an indiscriminate cross product.
- **Skeptic:** Despite its name it is a visual state harness, not formal state-machine verification.
- **Evaluator:** Render loading, empty, error and role-limited states without production state or side effects.
- **Consensus:** Keep available for a matching project rather than the default catalog. Validate the named prerequisites and check: Render loading, empty, error and role-limited states without production state or side effects.
- **Overlap:** prototype, break, verify-change
- **Prerequisites:** Component fixtures, browser

</details>

<details><summary>teardown — reference</summary>

[Pinned source](https://github.com/jakubkrehel/skills/blob/592aedc44d7d5b3e29740984252902f3e5402a1c/skills/teardown/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Distinguishes presentation geometry from manufacturing accuracy.
- **Skeptic:** This is an illustration workflow outside the core engineering skill pack.
- **Evaluator:** Render all labeled parts and verify annotation correspondence without inventing toleranced accuracy.
- **Consensus:** Retain as a linked reference, not another active trigger. This is an illustration workflow outside the core engineering skill pack.
- **Overlap:** docs, visualization tools
- **Prerequisites:** Geometry renderer, reference images, preview

</details>

<details><summary>variant — profile</summary>

[Pinned source](https://github.com/jakubkrehel/skills/blob/592aedc44d7d5b3e29740984252902f3e5402a1c/skills/variant/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Names the design axis and preserves a common accessibility floor.
- **Skeptic:** A required count of three and refusing to recommend can overconstrain a small decision.
- **Evaluator:** Compare distinct layout directions, then promote the selected one without leaving unused variants.
- **Consensus:** Keep available for a matching project rather than the default catalog. Validate the named prerequisites and check: Compare distinct layout directions, then promote the selected one without leaving unused variants.
- **Overlap:** prototype, component-canvas
- **Prerequisites:** Frontend page, browser, user selection

</details>

### ibelick/ui-skills

<details><summary>baseline-ui — reference</summary>

[Pinned source](https://github.com/ibelick/ui-skills/blob/59193a75432e5f41c6980f53b9e6a7bd56919947/skills/baseline-ui/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Catches common inconsistent spacing and inaccessible primitive choices.
- **Skeptic:** Mandatory Tailwind, motion/react and cn assumptions make it unsuitable as a universal baseline.
- **Evaluator:** Review a non-Tailwind project and improve an actual defect without adding its preferred stack.
- **Consensus:** Retain as a linked reference, not another active trigger. Mandatory Tailwind, motion/react and cn assumptions make it unsuitable as a universal baseline.
- **Overlap:** ui-review, better-ui, frontend-ui-engineering
- **Prerequisites:** Tailwind and React preferences

</details>

<details><summary>component-canvas — profile</summary>

[Pinned source](https://github.com/ibelick/ui-skills/blob/59193a75432e5f41c6980f53b9e6a7bd56919947/skills/component-canvas/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Keeps preview infrastructure separate from component implementation.
- **Skeptic:** An interactive canvas is unnecessary for a single component check and must isolate side effects.
- **Evaluator:** Preview a component with destructive actions and prove no production calls occur.
- **Consensus:** Keep available for a matching project rather than the default catalog. Validate the named prerequisites and check: Preview a component with destructive actions and prove no production calls occur.
- **Overlap:** prototype, variant, state-machine
- **Prerequisites:** Frontend app, browser, isolated fixtures

</details>

<details><summary>create-canvas — profile</summary>

[Pinned source](https://github.com/ibelick/ui-skills/blob/59193a75432e5f41c6980f53b9e6a7bd56919947/skills/create-canvas/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Separates persisted layout from authoritative content and preserves live edits.
- **Skeptic:** The broad canvas abstraction can exceed a question that needs one simple prototype.
- **Evaluator:** Reload and rearrange items while verifying source membership and content remain authoritative.
- **Consensus:** Keep available for a matching project rather than the default catalog. Validate the named prerequisites and check: Reload and rearrange items while verifying source membership and content remain authoritative.
- **Overlap:** component-canvas, prototype
- **Prerequisites:** Frontend stack, browser storage

</details>

<details><summary>create-design-md — adapt</summary>

[Pinned source](https://github.com/ibelick/ui-skills/blob/59193a75432e5f41c6980f53b9e6a7bd56919947/skills/create-design-md/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Records evidence and avoids promoting incidental values into policy.
- **Skeptic:** A website screenshot cannot establish exact tokens or intentional design decisions.
- **Evaluator:** Extract a token with its source and mark an inferred pattern as uncertain.
- **Consensus:** Absorb the useful procedure into docs; resolve this source-specific limit before promotion: A website screenshot cannot establish exact tokens or intentional design decisions. Behavioral benefit remains unmeasured.
- **Overlap:** docs, better-interface
- **Prerequisites:** Repository or browser evidence, DESIGN.md destination

</details>

<details><summary>fixing-accessibility — adapt</summary>

[Pinned source](https://github.com/ibelick/ui-skills/blob/59193a75432e5f41c6980f53b9e6a7bd56919947/skills/fixing-accessibility/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Prioritizes concrete access failures over broad cosmetic cleanup.
- **Skeptic:** Markup checks alone cannot prove screen-reader or keyboard task completion.
- **Evaluator:** Complete an invalid-form recovery and a modal interaction using keyboard and assistive technology.
- **Consensus:** Absorb the useful procedure into ui-review; resolve this source-specific limit before promotion: Markup checks alone cannot prove screen-reader or keyboard task completion. Behavioral benefit remains unmeasured.
- **Overlap:** better-accessibility, ui-review
- **Prerequisites:** Browser, HTML and accessibility tools

</details>

<details><summary>fixing-metadata — profile</summary>

[Pinned source](https://github.com/ibelick/ui-skills/blob/59193a75432e5f41c6980f53b9e6a7bd56919947/skills/fixing-metadata/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Prioritizes duplicate or incorrect indexing behavior and deterministic values.
- **Skeptic:** SEO requirements depend on page access intent; private pages should not inherit public defaults.
- **Evaluator:** Render public and private page metadata and verify canonical and robots values match actual access intent.
- **Consensus:** Keep available for a matching project rather than the default catalog. Validate the named prerequisites and check: Render public and private page metadata and verify canonical and robots values match actual access intent.
- **Overlap:** docs, verify-change
- **Prerequisites:** Rendered head, framework metadata API

</details>

<details><summary>fixing-motion-performance — profile</summary>

[Pinned source](https://github.com/ibelick/ui-skills/blob/59193a75432e5f41c6980f53b9e6a7bd56919947/skills/fixing-motion-performance/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Requires measurement and warns that compositor promotion cannot be assumed.
- **Skeptic:** Never-pattern lists still need context, device evidence and proportional scope.
- **Evaluator:** Measure one janky interaction before and after an isolated change under representative load.
- **Consensus:** Keep available for a matching project rather than the default catalog. Validate the named prerequisites and check: Measure one janky interaction before and after an isolated change under representative load.
- **Overlap:** animation-performance, performance-optimization
- **Prerequisites:** Browser profiler, animation source

</details>

<details><summary>improve-ui — adapt</summary>

[Pinned source](https://github.com/ibelick/ui-skills/blob/59193a75432e5f41c6980f53b9e6a7bd56919947/skills/improve-ui/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Requires proof and keeps product identity and existing owners intact.
- **Skeptic:** Generating handoff plans for every finding adds work when the user only requested a report.
- **Evaluator:** Audit a deliberate stylistic choice and avoid reporting it as a defect without contrary local evidence.
- **Consensus:** Absorb the useful procedure into ui-review; resolve this source-specific limit before promotion: Generating handoff plans for every finding adds work when the user only requested a report. Behavioral benefit remains unmeasured.
- **Overlap:** better-interface, ui-review
- **Prerequisites:** Design evidence, browser, design-plans destination

</details>

<details><summary>ui-skills-root — reference</summary>

[Pinned source](https://github.com/ibelick/ui-skills/blob/59193a75432e5f41c6980f53b9e6a7bd56919947/skills/ui-skills-root/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Tries to keep the loaded context smaller than the whole catalog.
- **Skeptic:** Another UI router and a new CLI duplicate the owned routing layer.
- **Evaluator:** Route a metadata request to one relevant profile without loading unrelated design or motion rules.
- **Consensus:** Retain as a linked reference, not another active trigger. Another UI router and a new CLI duplicate the owned routing layer.
- **Overlap:** start, using-agent-skills, better-interface
- **Prerequisites:** ui-skills CLI, sibling skills

</details>

### davidondrej/skills

<details><summary>bb-cli — profile</summary>

[Pinned source](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/agent-orchestration/bb-cli/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Requires real context and IDs before operating on app state.
- **Skeptic:** The CLI is specific to BB and does not transfer to Codex app tools.
- **Evaluator:** Attempt a scoped thread lookup and verify no unrelated thread is read or messaged.
- **Consensus:** Keep available for a matching project rather than the default catalog. Validate the named prerequisites and check: Attempt a scoped thread lookup and verify no unrelated thread is read or messaged.
- **Overlap:** nagent, bb-plugins
- **Prerequisites:** BB CLI and account

</details>

<details><summary>bb-plugins — profile</summary>

[Pinned source](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/agent-orchestration/bb-plugins/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Makes plugin trust and dependency packaging explicit.
- **Skeptic:** Same-origin and in-process extensions need a BB-specific review rather than generic installation.
- **Evaluator:** Install a local fixture in a test app and verify settings keep secret values out of output.
- **Consensus:** Keep available for a matching project rather than the default catalog. Validate the named prerequisites and check: Install a local fixture in a test app and verify settings keep secret values out of output.
- **Overlap:** bb-cli
- **Prerequisites:** BB runtime, TypeScript, plugin tooling

</details>

<details><summary>cmux — profile</summary>

[Pinned source](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/agent-orchestration/cmux/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Anchors actions to owned workspace identity rather than visual focus.
- **Skeptic:** macOS and cmux commands are irrelevant to other hosts.
- **Evaluator:** Create one owned test surface and verify all commands stay in the requested workspace.
- **Consensus:** Keep available for a matching project rather than the default catalog. Validate the named prerequisites and check: Create one owned test surface and verify all commands stay in the requested workspace.
- **Overlap:** herdr, bb-cli
- **Prerequisites:** macOS 14+, cmux

</details>

<details><summary>codex-subagent — reference</summary>

[Pinned source](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/agent-orchestration/codex-subagent/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Documents a subscription-authenticated noninteractive route.
- **Skeptic:** The hard-coded model and CLI invocation policy can become stale and conflict with the chosen model.
- **Evaluator:** Discover the installed model catalog and preserve the user's choice before a harmless delegated task.
- **Consensus:** Retain as a linked reference, not another active trigger. The hard-coded model and CLI invocation policy can become stale and conflict with the chosen model.
- **Overlap:** nagent, total-review
- **Prerequisites:** Codex CLI, subscription login, compatible model

</details>

<details><summary>fable-review — reference</summary>

[Pinned source](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/agent-orchestration/fable-review/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** An independent reviewer can inspect a bounded artifact.
- **Skeptic:** The fixed model and missing room-cli dependency make it an adapter rather than portable review guidance.
- **Evaluator:** Verify runtime availability and read-only scope before requesting a review.
- **Consensus:** Retain as a linked reference, not another active trigger. The fixed model and missing room-cli dependency make it an adapter rather than portable review guidance.
- **Overlap:** review, gpt-review, kimi-review
- **Prerequisites:** Cloudroom, room-cli, Fable provider

</details>

<details><summary>fable-safe-prompt — reject</summary>

[Pinned source](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/agent-orchestration/fable-safe-prompt/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Could clarify benign intent in a legitimate request.
- **Skeptic:** Provider-classifier optimization is not a quality or engineering primitive and must not disguise intent.
- **Evaluator:** For a benign refused task, clarify purpose without changing authorization or evading safety boundaries.
- **Consensus:** Do not install raw. Provider-classifier optimization is not a quality or engineering primitive and must not disguise intent. Retain only any independently useful idea within the owned scope.
- **Overlap:** better-prompt
- **Prerequisites:** Specific provider behavior

</details>

<details><summary>git-worktree — reference</summary>

[Pinned source](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/agent-orchestration/git-worktree/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Respects lifecycle ownership in hosted runtimes.
- **Skeptic:** One-worktree-per-agent is a runtime policy and not always necessary for read-only work.
- **Evaluator:** Reuse an assigned task checkout and verify no duplicate or unmanaged checkout is created.
- **Consensus:** Retain as a linked reference, not another active trigger. One-worktree-per-agent is a runtime policy and not always necessary for read-only work.
- **Overlap:** new-feature, start
- **Prerequisites:** Git or managed worktree runtime

</details>

<details><summary>goal-loop — adapt</summary>

[Pinned source](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/agent-orchestration/goal-loop/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Explicitly checks whether the installed harness supports persistent goals.
- **Skeptic:** Prompt text cannot provide durability, scheduling or runtime capabilities the host lacks.
- **Evaluator:** Run a bounded fixture task and stop at success, explicit pause or budget without fabricating a persistent service.
- **Consensus:** Absorb the useful procedure into verify-change; resolve this source-specific limit before promotion: Prompt text cannot provide durability, scheduling or runtime capabilities the host lacks. Behavioral benefit remains unmeasured.
- **Overlap:** start, poteto-mode
- **Prerequisites:** Harness goal support, observable completion check

</details>

<details><summary>gpt-review — reference</summary>

[Pinned source](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/agent-orchestration/gpt-review/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Verifies requested model and effort after launch.
- **Skeptic:** Fixed model, tier and orchestration choices are personal cost preferences.
- **Evaluator:** Preserve a user-selected review model and reject unavailable capabilities without substitution.
- **Consensus:** Retain as a linked reference, not another active trigger. Fixed model, tier and orchestration choices are personal cost preferences.
- **Overlap:** review, total-review
- **Prerequisites:** Cloudroom, room-cli, Codex provider

</details>

<details><summary>handoff — adapt</summary>

[Pinned source](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/agent-orchestration/handoff/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Distinguishes completed, active and blocked work and redacts values.
- **Skeptic:** A handoff should not import the author's runtime or destination assumptions.
- **Evaluator:** Resume from the brief and recover open work, authorization and proof without reading private values.
- **Consensus:** Absorb the useful procedure into handoff; resolve this source-specific limit before promotion: A handoff should not import the author's runtime or destination assumptions. Behavioral benefit remains unmeasured.
- **Overlap:** handoff, claude-handoff
- **Prerequisites:** Chosen handoff destination

</details>

<details><summary>herdr — profile</summary>

[Pinned source](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/agent-orchestration/herdr/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Discovers sessions and panes and scopes interaction to ownership.
- **Skeptic:** The local socket and terminal integration are not native agent communication or shared memory.
- **Evaluator:** List owned panes and verify a command cannot target an unrelated session by implicit focus.
- **Consensus:** Keep available for a matching project rather than the default catalog. Validate the named prerequisites and check: List owned panes and verify a command cannot target an unrelated session by implicit focus.
- **Overlap:** cmux, bb-cli
- **Prerequisites:** Herdr, Ghostty, local socket

</details>

<details><summary>kimi-review — reference</summary>

[Pinned source](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/agent-orchestration/kimi-review/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Keeps model and effort stable across transport fallback.
- **Skeptic:** Fallback routes can change billing and privacy and require the user's actual route preferences.
- **Evaluator:** Simulate one unavailable route and verify no unapproved paid or privacy-changing fallback occurs.
- **Consensus:** Retain as a linked reference, not another active trigger. Fallback routes can change billing and privacy and require the user's actual route preferences.
- **Overlap:** review, gpt-review
- **Prerequisites:** Cloudroom, Pi, provider model configuration

</details>

<details><summary>larp-detector — reject</summary>

[Pinned source](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/agent-orchestration/larp-detector/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Prompts reviewers to challenge unsupported hypothetical fixes.
- **Skeptic:** It attributes motives and taste to contributors instead of establishing defects from evidence.
- **Evaluator:** Review identical code under different author identities and require the same technical conclusion.
- **Consensus:** Do not install raw. It attributes motives and taste to contributors instead of establishing defects from evidence. Retain only any independently useful idea within the owned scope.
- **Overlap:** review, code-review
- **Prerequisites:** Public contribution context

</details>

<details><summary>muse-review — reference</summary>

[Pinned source](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/agent-orchestration/muse-review/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Separates an independent review route from the current agent.
- **Skeptic:** A fixed paid provider and model cannot be the general review baseline.
- **Evaluator:** Check a route and price policy before a harmless review; no silent provider substitution.
- **Consensus:** Retain as a linked reference, not another active trigger. A fixed paid provider and model cannot be the general review baseline.
- **Overlap:** review, total-review
- **Prerequisites:** Cloudroom, Pi, OpenRouter, model access

</details>

<details><summary>nagent — profile</summary>

[Pinned source](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/agent-orchestration/nagent/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Checks project path and actual provider capabilities after spawn.
- **Skeptic:** Personal default model and service tier do not transfer to every team.
- **Evaluator:** Spawn a fixture worker only in the named project and confirm its actual configuration.
- **Consensus:** Keep available for a matching project rather than the default catalog. Validate the named prerequisites and check: Spawn a fixture worker only in the named project and confirm its actual configuration.
- **Overlap:** bb-cli, codex-subagent
- **Prerequisites:** BB CLI, provider access

</details>

<details><summary>new-grok-bot — reference</summary>

[Pinned source](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/agent-orchestration/new-grok-bot/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Uses a unit-of-work test to avoid an incoherent all-purpose agent.
- **Skeptic:** Product capabilities and persistent-machine claims require current official verification.
- **Evaluator:** Draft a role with observable output and stop conditions without claiming an unverified bot capability.
- **Consensus:** Retain as a linked reference, not another active trigger. Product capabilities and persistent-machine claims require current official verification.
- **Overlap:** goal-loop, ask-then-build
- **Prerequisites:** Current Grok Bot documentation

</details>

<details><summary>reset-cursor-acp — profile</summary>

[Pinned source](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/agent-orchestration/reset-cursor-acp/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Distinguishes per-thread subprocesses from a nonexistent global server.
- **Skeptic:** Recovery commands are app-specific and broad process matching can affect other sessions.
- **Evaluator:** Reset an owned test thread and verify unrelated threads and processes stay active.
- **Consensus:** Keep available for a matching project rather than the default catalog. Validate the named prerequisites and check: Reset an owned test thread and verify unrelated threads and processes stay active.
- **Overlap:** bb-cli
- **Prerequisites:** Compatible chat app, Cursor ACP runtime

</details>

<details><summary>self-archive — reference</summary>

[Pinned source](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/agent-orchestration/self-archive/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Requires an explicit request and reports command failure honestly.
- **Skeptic:** Its CLI also targets children; that side effect is not universal archive semantics.
- **Evaluator:** Archive an owned fixture only when requested and verify success before claiming completion.
- **Consensus:** Retain as a linked reference, not another active trigger. Its CLI also targets children; that side effect is not universal archive semantics.
- **Overlap:** bb-cli
- **Prerequisites:** Cloudroom, room-cli

</details>

<details><summary>total-review — reject</summary>

[Pinned source](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/agent-orchestration/total-review/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Independent reviewers can surface different concrete defects.
- **Skeptic:** It demands full or bypass permissions and maximum-cost models even for review-only work.
- **Evaluator:** Compare read-only review outcomes and reject any requirement to widen permissions solely to inspect a diff.
- **Consensus:** Do not install raw. It demands full or bypass permissions and maximum-cost models even for review-only work. Retain only any independently useful idea within the owned scope.
- **Overlap:** review, interrogate, doubt-driven-development
- **Prerequisites:** Cloudroom, five model providers, full permissions demanded upstream

</details>

<details><summary>anti-sleep — profile</summary>

[Pinned source](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/ops-and-setup/anti-sleep/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Verifies assertions instead of claiming a background process survives.
- **Skeptic:** It changes host power behavior and is macOS-specific.
- **Evaluator:** Start and stop a short test session and verify no persistent restart loop remains.
- **Consensus:** Keep available for a matching project rather than the default catalog. Validate the named prerequisites and check: Start and stop a short test session and verify no persistent restart loop remains.
- **Overlap:** persistent-localhost
- **Prerequisites:** macOS, launchd, caffeinate, script

</details>

<details><summary>boat — profile</summary>

[Pinned source](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/ops-and-setup/boat/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Distinguishes existing Box-era configuration from a requested migration.
- **Skeptic:** Provisioning and credentials need service-specific cost and lifecycle handling.
- **Evaluator:** Create a disposable authorized sandbox and verify cleanup and credential redaction.
- **Consensus:** Keep available for a matching project rather than the default catalog. Validate the named prerequisites and check: Create a disposable authorized sandbox and verify cleanup and credential redaction.
- **Overlap:** bb-cli
- **Prerequisites:** Boat account, API or CLI, SSH

</details>

<details><summary>create-readonly-db-role — profile</summary>

[Pinned source](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/ops-and-setup/create-readonly-db-role/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Explains grants, row security and transaction settings as separate controls.
- **Skeptic:** Grant-all-then-denylist can expose future sensitive tables; defaults are examples, not a universal safe role.
- **Evaluator:** In a database fixture, prove writes and sensitive reads fail including newly created sensitive tables.
- **Consensus:** Keep available for a matching project rather than the default catalog. Validate the named prerequisites and check: In a database fixture, prove writes and sensitive reads fail including newly created sensitive tables.
- **Overlap:** security review, global-agent-guardrails
- **Prerequisites:** PostgreSQL, DB owner, agreed table access

</details>

<details><summary>cua-driver — profile</summary>

[Pinned source](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/ops-and-setup/cua-driver/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Checks targeting and coordinate systems before issuing input.
- **Skeptic:** It is a separate native host-control tool and is not interchangeable with Codex computer use.
- **Evaluator:** Operate one owned test window and verify its screenshot and accessibility identity match.
- **Consensus:** Keep available for a matching project rather than the default catalog. Validate the named prerequisites and check: Operate one owned test window and verify its screenshot and accessibility identity match.
- **Overlap:** browser-use, computer-use workflows
- **Prerequisites:** Cua Driver, OS permissions

</details>

<details><summary>github-outside-sandbox — reference</summary>

[Pinned source](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/ops-and-setup/github-outside-sandbox/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Distinguishes sandbox failure from broken authentication.
- **Skeptic:** Its Codex escalation example is invalid when the current harness forbids escalation.
- **Evaluator:** Given a blocked command, preserve permission policy and report the limit without wrapper bypasses.
- **Consensus:** Retain as a linked reference, not another active trigger. Its Codex escalation example is invalid when the current harness forbids escalation.
- **Overlap:** GitHub connector, Git workflow
- **Prerequisites:** Harness escalation capability, gh

</details>

<details><summary>global-agent-guardrails — profile</summary>

[Pinned source](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/ops-and-setup/global-agent-guardrails/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Includes allow and deny cases and admits regex is an accident barrier.
- **Skeptic:** Regex cannot enforce a security boundary against arbitrary equivalent programs.
- **Evaluator:** Run direct and obfuscated command fixtures and report both coverage and bypass limits.
- **Consensus:** Keep available for a matching project rather than the default catalog. Validate the named prerequisites and check: Run direct and obfuscated command fixtures and report both coverage and bypass limits.
- **Overlap:** git-guardrails-claude-code
- **Prerequisites:** Hook or native guard support, pattern tests

</details>

<details><summary>openrouter — profile</summary>

[Pinned source](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/ops-and-setup/openrouter/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Checks real request fields and treats HTTP success separately from valid task output.
- **Skeptic:** Live model capabilities, route costs and data policies cannot be frozen in a prompt.
- **Evaluator:** Exercise truncation and a provider error, preserving schema validation and the authorized fallback budget.
- **Consensus:** Keep available for a matching project rather than the default catalog. Validate the named prerequisites and check: Exercise truncation and a provider error, preserving schema validation and the authorized fallback budget.
- **Overlap:** research, api-design
- **Prerequisites:** OpenRouter API, installed SDK, credentials

</details>

<details><summary>persistent-localhost — profile</summary>

[Pinned source](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/ops-and-setup/persistent-localhost/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Verifies readiness and prevents duplicate watchers.
- **Skeptic:** macOS LaunchAgents do not solve persistent process management on Windows or Linux.
- **Evaluator:** Start, crash and stop a disposable server and verify readiness and restart behavior.
- **Consensus:** Keep available for a matching project rather than the default catalog. Validate the named prerequisites and check: Start, crash and stop a disposable server and verify readiness and restart behavior.
- **Overlap:** anti-sleep
- **Prerequisites:** macOS, launchd, optional watchexec

</details>

<details><summary>prompt-for-others — adapt</summary>

[Pinned source](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/ops-and-setup/prompt-for-others/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Carries prerequisites, exact checks and a stop rule for a fresh machine.
- **Skeptic:** Testing on one machine does not prove portability to the teammate's environment.
- **Evaluator:** Execute the prompt in a different clean fixture with a missing prerequisite and verify a bounded stop.
- **Consensus:** Absorb the useful procedure into handoff; resolve this source-specific limit before promotion: Testing on one machine does not prove portability to the teammate's environment. Behavioral benefit remains unmeasured.
- **Overlap:** handoff, wizard
- **Prerequisites:** Verified commands, known target environment

</details>

<details><summary>rename-process — profile</summary>

[Pinned source](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/ops-and-setup/rename-process/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Maps exact identities, remotes, machines and ignored files before moving.
- **Skeptic:** Cross-system moves have wider operational impact than renaming a symbol.
- **Evaluator:** Rehearse a repository move and verify local changes, worktrees and service paths remain recoverable.
- **Consensus:** Keep available for a matching project rather than the default catalog. Validate the named prerequisites and check: Rehearse a repository move and verify local changes, worktrees and service paths remain recoverable.
- **Overlap:** change-plan
- **Prerequisites:** Git, affected runtime or services, explicit rename scope

</details>

<details><summary>repo-sync — reference</summary>

[Pinned source](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/ops-and-setup/repo-sync/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Separates document synchronization from software PR workflows.
- **Skeptic:** Automatic publication is unsuitable for curated skills whose changes require review and evaluations.
- **Evaluator:** Use a scratch documents repo and verify feature branches and nonapproved files never auto-publish.
- **Consensus:** Retain as a linked reference, not another active trigger. Automatic publication is unsuitable for curated skills whose changes require review and evaluations.
- **Overlap:** skill-maintenance, push-skills
- **Prerequisites:** macOS, repo-sync binary, launchd

</details>

<details><summary>risky-changes — adapt</summary>

[Pinned source](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/ops-and-setup/risky-changes/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Catches a technically correct filter that removes nearly all useful behavior.
- **Skeptic:** A single anecdote does not justify a full external research pass for every default change.
- **Evaluator:** Use representative real-shaped data and detect the intended effect disappearing despite green unit tests.
- **Consensus:** Absorb the useful procedure into verify-change; resolve this source-specific limit before promotion: A single anecdote does not justify a full external research pass for every default change. Behavioral benefit remains unmeasured.
- **Overlap:** review, performance-optimization
- **Prerequisites:** Representative data, product owner, impact metrics

</details>

<details><summary>setup-help — reference</summary>

[Pinned source](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/ops-and-setup/setup-help/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Reduces handoff friction while retaining all unfinished steps internally.
- **Skeptic:** A rigid format is a personal conversational preference rather than a core capability.
- **Evaluator:** Guide a multi-screen setup without splitting one form into many needless exchanges.
- **Consensus:** Retain as a linked reference, not another active trigger. A rigid format is a personal conversational preference rather than a core capability.
- **Overlap:** wizard, prompt-for-others
- **Prerequisites:** Actual setup context

</details>

<details><summary>browser-harness — profile</summary>

[Pinned source](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/research-and-web/browser-harness/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Separates static fetching from interactions that need a real browser.
- **Skeptic:** Personal Chrome connections, cloud billing and optional domain skills require explicit environment decisions.
- **Evaluator:** Exercise a login-free fixture without reading unrelated tabs or leaving billed sessions running.
- **Consensus:** Keep available for a matching project rather than the default catalog. Validate the named prerequisites and check: Exercise a login-free fixture without reading unrelated tabs or leaving billed sessions running.
- **Overlap:** browser-use, cua-driver
- **Prerequisites:** Browser harness, Chrome, optional cloud key

</details>

<details><summary>browser-use — profile</summary>

[Pinned source](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/research-and-web/browser-use/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** States when plain HTTP is sufficient and warns about running cloud sessions.
- **Skeptic:** It overlaps browser-harness but has separate CLI and setup assumptions.
- **Evaluator:** Choose one browser adapter for a fixture and verify state and cleanup instead of running both.
- **Consensus:** Keep available for a matching project rather than the default catalog. Validate the named prerequisites and check: Choose one browser adapter for a fixture and verify state and cleanup instead of running both.
- **Overlap:** browser-harness, cua-driver
- **Prerequisites:** Browser Use CLI, CDP, optional cloud account

</details>

<details><summary>deep-research — profile</summary>

[Pinned source](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/research-and-web/deep-research/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Uses idempotency for retries and separates research subquestions.
- **Skeptic:** It requires a paid service and another research-prompt skill not present in this snapshot.
- **Evaluator:** Retry a fixture job with the same identity and verify one billable task and preserved citations.
- **Consensus:** Keep available for a matching project rather than the default catalog. Validate the named prerequisites and check: Retry a fixture job with the same identity and verify one billable task and preserved citations.
- **Overlap:** research, deepapi
- **Prerequisites:** DeepAPI API key, research-prompt, async polling

</details>

<details><summary>deep-scrape — profile</summary>

[Pinned source](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/research-and-web/deep-scrape/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Keeps polling from triggering a second paid request.
- **Skeptic:** Person and company dossiers are not the generic engineering research workflow.
- **Evaluator:** Test an ambiguous subject and a dry-run response without silently submitting paid follow-up work.
- **Consensus:** Keep available for a matching project rather than the default catalog. Validate the named prerequisites and check: Test an ambiguous subject and a dry-run response without silently submitting paid follow-up work.
- **Overlap:** deepapi, who-is-this
- **Prerequisites:** DeepAPI, curl, jq, uuidgen

</details>

<details><summary>deepapi — reference</summary>

[Pinned source](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/research-and-web/deepapi/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Provides workflow-specific references and idempotent service protocols.
- **Skeptic:** Claiming all web tasks and replacing available native tools creates vendor lock-in and routing collisions.
- **Evaluator:** For a public docs lookup, prefer an already available official source tool unless DeepAPI was specifically chosen.
- **Consensus:** Retain as a linked reference, not another active trigger. Claiming all web tasks and replacing available native tools creates vendor lock-in and routing collisions.
- **Overlap:** research, deep-research, browser-use
- **Prerequisites:** DeepAPI account, credentials, service endpoints

</details>

<details><summary>domain-checker — profile</summary>

[Pinned source](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/research-and-web/domain-checker/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Separates no record from actual purchasability and keeps errors unknown.
- **Skeptic:** Only direct-under-TLD names are supported; registry absence does not prove availability.
- **Evaluator:** Check registered, absent and unsupported-suffix fixtures without labeling unknowns available.
- **Consensus:** Keep available for a matching project rather than the default catalog. Validate the named prerequisites and check: Check registered, absent and unsupported-suffix fixtures without labeling unknowns available.
- **Overlap:** research
- **Prerequisites:** Python, RDAP network access

</details>

<details><summary>fireflies-transcript — profile</summary>

[Pinned source](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/research-and-web/fireflies-transcript/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Matches meetings using time and content rather than title alone.
- **Skeptic:** Transcript access and secret loading depend on the actual account and local configuration.
- **Evaluator:** Retrieve one authorized fixture transcript and keep keys and raw personal content out of logs.
- **Consensus:** Keep available for a matching project rather than the default catalog. Validate the named prerequisites and check: Retrieve one authorized fixture transcript and keep keys and raw personal content out of logs.
- **Overlap:** research, handoff
- **Prerequisites:** Fireflies API account, secure credential source

</details>

<details><summary>online-shopping — reference</summary>

[Pinned source](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/research-and-web/online-shopping/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Separates buying advice from account or payment mutations.
- **Skeptic:** It is outside development scope and hard-wires a paid search service and model preference.
- **Evaluator:** Compare dated purchase evidence without entering payment details or claiming a purchase occurred.
- **Consensus:** Retain as a linked reference, not another active trigger. It is outside development scope and hard-wires a paid search service and model preference.
- **Overlap:** research
- **Prerequisites:** DeepAPI, current retailer evidence

</details>

<details><summary>varied-search — reference</summary>

[Pinned source](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/research-and-web/varied-search/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Can broaden discovery beyond one search channel.
- **Skeptic:** Five searches in each category measures activity, not decision coverage or evidence quality.
- **Evaluator:** Answer a narrow API question without requiring fifteen irrelevant searches.
- **Consensus:** Retain as a linked reference, not another active trigger. Five searches in each category measures activity, not decision coverage or evidence quality.
- **Overlap:** research, deep-research
- **Prerequisites:** DeepAPI, web and social endpoints

</details>

<details><summary>who-is-this — reference</summary>

[Pinned source](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/research-and-web/who-is-this/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Checks namesake identity before synthesizing credibility.
- **Skeptic:** Social prominence and selected activity do not establish engineering reliability or honest intent.
- **Evaluator:** Give two people with the same name and verify uncertainty rather than a merged profile.
- **Consensus:** Retain as a linked reference, not another active trigger. Social prominence and selected activity do not establish engineering reliability or honest intent.
- **Overlap:** research, deep-scrape
- **Prerequisites:** DeepAPI, public identity evidence

</details>

<details><summary>distribute-skill-to-all-agents — reference</summary>

[Pinned source](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/skill-authoring/distribute-skill-to-all-agents/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Makes duplicate-path and symlink assumptions explicit.
- **Skeptic:** It asserts a particular Mac layout and all-five distribution policy that need not apply elsewhere.
- **Evaluator:** Inspect actual roots and detect a duplicate installation without overwriting unrelated skills.
- **Consensus:** Retain as a linked reference, not another active trigger. It asserts a particular Mac layout and all-five distribution policy that need not apply elsewhere.
- **Overlap:** skill-maintenance, push-skills
- **Prerequisites:** Selected agent roots, filesystem or symlinks

</details>

<details><summary>effective-agent-skills — adapt</summary>

[Pinned source](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/skill-authoring/effective-agent-skills/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Explains discovery, instruction loading and supporting resources separately.
- **Skeptic:** Approximate token counts and syntax advice do not prove a skill activates or improves outcomes.
- **Evaluator:** Validate YAML and links, then run neighboring positive and negative invocation cases.
- **Consensus:** Absorb the useful procedure into skill-maintenance; resolve this source-specific limit before promotion: Approximate token counts and syntax advice do not prove a skill activates or improves outcomes. Behavioral benefit remains unmeasured.
- **Overlap:** skill-creator, writing-for-agents
- **Prerequisites:** Actual harness, skill validation tools

</details>

<details><summary>push-skills — reference</summary>

[Pinned source](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/skill-authoring/push-skills/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Reviews outgoing commits and preserves a single mirror publisher.
- **Skeptic:** Its private remotes, global-instruction inclusion and standing scope are author-specific.
- **Evaluator:** Publish a scratch fixture with a secret sentinel and verify excluded content never enters any outgoing commit.
- **Consensus:** Retain as a linked reference, not another active trigger. Its private remotes, global-instruction inclusion and standing scope are author-specific.
- **Overlap:** skill-maintenance, repo-sync
- **Prerequisites:** Configured private repo, mirror automation, Git

</details>

<details><summary>4x4 — reference</summary>

[Pinned source](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/thinking-and-docs/4x4/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Forces attention onto consequential decisions only the user can make.
- **Skeptic:** A fixed sixteen-question quota creates low-value questions when the decision is smaller.
- **Evaluator:** Resolve a three-choice decision without padding it to sixteen unanswered items.
- **Consensus:** Retain as a linked reference, not another active trigger. A fixed sixteen-question quota creates low-value questions when the decision is smaller.
- **Overlap:** grilling, ask-then-build
- **Prerequisites:** Explicit user invocation

</details>

<details><summary>adr-verbatim — adapt</summary>

[Pinned source](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/thinking-and-docs/adr-verbatim/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Separates meaning from a verbatim conversation transcript.
- **Skeptic:** The title can imply literal transcription; decisions still need accurate scope and alternatives.
- **Evaluator:** Record a qualified decision and preserve its condition and uncertainty during editing.
- **Consensus:** Absorb the useful procedure into docs; resolve this source-specific limit before promotion: The title can imply literal transcription; decisions still need accurate scope and alternatives. Behavioral benefit remains unmeasured.
- **Overlap:** docs, domain-model, documentation-and-adrs
- **Prerequisites:** Existing ADR convention, approved decision

</details>

<details><summary>ask-then-build — adapt</summary>

[Pinned source](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/thinking-and-docs/ask-then-build/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Produces a self-contained handoff once decisions are settled.
- **Skeptic:** Strictly one-question-at-a-time conflicts with independent-frontier interviews and can slow trivial work.
- **Evaluator:** Use existing answers and ask only unresolved decisions before producing the requested prompt.
- **Consensus:** Absorb the useful procedure into grill-idea; resolve this source-specific limit before promotion: Strictly one-question-at-a-time conflicts with independent-frontier interviews and can slow trivial work. Behavioral benefit remains unmeasured.
- **Overlap:** grill-idea, grilling, handoff
- **Prerequisites:** User decisions, build context

</details>

<details><summary>before-building — reference</summary>

[Pinned source](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/thinking-and-docs/before-building/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Can expose an important product fork before implementation.
- **Skeptic:** It forbids inspecting the project and forces gut recommendations, risking avoidable incorrect assumptions.
- **Evaluator:** Give an idea whose answer is in the repo and verify the owned approach reads facts before asking.
- **Consensus:** Retain as a linked reference, not another active trigger. It forbids inspecting the project and forces gut recommendations, risking avoidable incorrect assumptions.
- **Overlap:** grill-idea, minimalist
- **Prerequisites:** Conversation only upstream

</details>

<details><summary>better-prompt — reference</summary>

[Pinned source](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/thinking-and-docs/better-prompt/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Asks what evidence and raw material would establish correctness.
- **Skeptic:** The prompt rewrite itself is not execution or proof of a better task outcome.
- **Evaluator:** Rewrite a bounded task and verify no new feature or deliverable is introduced.
- **Consensus:** Retain as a linked reference, not another active trigger. The prompt rewrite itself is not execution or proof of a better task outcome.
- **Overlap:** research, skill-maintenance
- **Prerequisites:** Original task and domain context

</details>

<details><summary>decisions — reference</summary>

[Pinned source](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/thinking-and-docs/decisions/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Surfaces alternatives to fragile assumptions.
- **Skeptic:** Self-reported confidence is not a calibrated measure and must be tied to evidence.
- **Evaluator:** Name only unresolved consequential choices and state what evidence would resolve them.
- **Consensus:** Retain as a linked reference, not another active trigger. Self-reported confidence is not a calibrated measure and must be tied to evidence.
- **Overlap:** review, simulate-discussion
- **Prerequisites:** Current work context

</details>

<details><summary>designs — reference</summary>

[Pinned source](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/thinking-and-docs/designs/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Makes alternatives inspectable.
- **Skeptic:** A count of four and an image-only request are not a reusable engineering process.
- **Evaluator:** Produce alternatives on meaningful axes without assuming implementation fidelity.
- **Consensus:** Retain as a linked reference, not another active trigger. A count of four and an image-only request are not a reusable engineering process.
- **Overlap:** prototype, variant
- **Prerequisites:** Image generation tool, design brief

</details>

<details><summary>file-tree — reference</summary>

[Pinned source](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/thinking-and-docs/file-tree/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Provides a quick structural explanation.
- **Skeptic:** A presentation preference adds little non-obvious value as an active skill.
- **Evaluator:** Show the actual relevant structure without inventing nonexistent files.
- **Consensus:** Retain as a linked reference, not another active trigger. A presentation preference adds little non-obvious value as an active skill.
- **Overlap:** docs
- **Prerequisites:** Filesystem or explicit proposed structure

</details>

<details><summary>image-prompt — reference</summary>

[Pinned source](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/thinking-and-docs/image-prompt/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Separates text prompt creation from rendering.
- **Skeptic:** Its exact-count and output-format preferences are unrelated to engineering delivery.
- **Evaluator:** Create distinct prompts while preserving the requested subject and constraints.
- **Consensus:** Retain as a linked reference, not another active trigger. Its exact-count and output-format preferences are unrelated to engineering delivery.
- **Overlap:** designs
- **Prerequisites:** Image brief

</details>

<details><summary>keep-track — reference</summary>

[Pinned source](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/thinking-and-docs/keep-track/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Carries a bounded queue and removes resolved items.
- **Skeptic:** A repeated list after every reply can dominate conversation and should be requested.
- **Evaluator:** Resolve one item and verify it disappears without new unsolicited topics entering the queue.
- **Consensus:** Retain as a linked reference, not another active trigger. A repeated list after every reply can dominate conversation and should be requested.
- **Overlap:** handoff, change-plan
- **Prerequisites:** Current conversation and agreed queue

</details>

<details><summary>read-all-adrs — reject</summary>

[Pinned source](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/thinking-and-docs/read-all-adrs/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Offers a full-history mode for a specifically requested audit.
- **Skeptic:** Abusive wording and an indiscriminate context dump add no engineering guidance.
- **Evaluator:** Choose relevant decisions for an ordinary task; reserve full-corpus reading for explicit scope.
- **Consensus:** Do not install raw. Abusive wording and an indiscriminate context dump add no engineering guidance. Retain only any independently useful idea within the owned scope.
- **Overlap:** docs, domain-model
- **Prerequisites:** Fixed docs/adr convention upstream

</details>

<details><summary>remind — reference</summary>

[Pinned source](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/thinking-and-docs/remind/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Can recover context after a long discussion.
- **Skeptic:** Repeating the first user prompt on every use may revive stale scope or expose irrelevant detail.
- **Evaluator:** Summarize the current goal and steering without treating the first prompt as overriding later corrections.
- **Consensus:** Retain as a linked reference, not another active trigger. Repeating the first user prompt on every use may revive stale scope or expose irrelevant detail.
- **Overlap:** handoff, wait-what, bro
- **Prerequisites:** Conversation history

</details>

<details><summary>rename — reference</summary>

[Pinned source](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/thinking-and-docs/rename/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** A tiny explicit action is easy to verify.
- **Skeptic:** The exact room-cli command and prohibition on discovery prevent portability.
- **Evaluator:** Use the actual host's title operation and verify only the intended thread changes.
- **Consensus:** Retain as a linked reference, not another active trigger. The exact room-cli command and prohibition on discovery prevent portability.
- **Overlap:** bb-cli
- **Prerequisites:** Cloudroom, room-cli

</details>

<details><summary>save-idea — reject</summary>

[Pinned source](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/thinking-and-docs/save-idea/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Captures ideas durably in a known personal backlog.
- **Skeptic:** It imports another author's claimed standing publication authorization and a placeholder path.
- **Evaluator:** Capture an idea locally without inheriting push permission or inventing the destination.
- **Consensus:** Do not install raw. It imports another author's claimed standing publication authorization and a placeholder path. Retain only any independently useful idea within the owned scope.
- **Overlap:** docs, handoff
- **Prerequisites:** Author-specific ideas repo, Git

</details>

<details><summary>signal-from-expert — profile</summary>

[Pinned source](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/thinking-and-docs/signal-from-expert/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Requires an explicit corpus and source locations for comparisons.
- **Skeptic:** Forced gap-finding can invent disagreement; exact quotations have attribution and reuse limits.
- **Evaluator:** Use a corpus already agreeing with the expert and allow no material gap when evidence supports that.
- **Consensus:** Keep available for a matching project rather than the default catalog. Validate the named prerequisites and check: Use a corpus already agreeing with the expert and allow no material gap when evidence supports that.
- **Overlap:** research, simulate-discussion
- **Prerequisites:** Named corpus, expert primary sources

</details>

<details><summary>stop-overthinking — reference</summary>

[Pinned source](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/thinking-and-docs/stop-overthinking/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Counters process overhead for a bounded reversible decision.
- **Skeptic:** Brevity must not turn missing evidence into permission or success.
- **Evaluator:** Keep a material blocker visible while removing repetitive speculation.
- **Consensus:** Retain as a linked reference, not another active trigger. Brevity must not turn missing evidence into permission or success.
- **Overlap:** minimalist, decisions
- **Prerequisites:** Current task context

</details>

<details><summary>teach — profile</summary>

[Pinned source](https://github.com/davidondrej/skills/blob/3e30b519f897861f97943fc5f2e74c34151fd2ef/skills/thinking-and-docs/teach/SKILL.md). Inspection: entrypoint excerpts; behavioral test not run.

- **Practitioner:** Supports a learner's mission and evolving knowledge across sessions.
- **Skeptic:** It duplicates Matt's teaching workflow with personal style and layout assumptions.
- **Evaluator:** Answer a one-off conceptual question without creating a teaching workspace unless requested.
- **Consensus:** Keep available for a matching project rather than the default catalog. Validate the named prerequisites and check: Answer a one-off conceptual question without creating a teaching workspace unless requested.
- **Overlap:** teach, handoff
- **Prerequisites:** Learning templates, chosen workspace

</details>

## Promotion standard

A source-review recommendation enters the owned pack only after its description is discriminating, side effects respect the actual request, dependencies exist or degrade honestly, and a realistic positive case plus negative and neighboring cases pass. For consequential procedures, compare a no-skill baseline and repeat uncertain runs. Keep routing evidence separate from task-success evidence and record the exact model, harness and source version. No stars, author reputation, word count or static lint score substitutes for those checks.
