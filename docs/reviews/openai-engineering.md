# OpenAI engineering skill review

Snapshot: `openai/plugins@0722921d5542fc593105c27bd52630babd8b8c2a`. Review date: 2026-10-30.

**Evidence level: source-review.** The 55 listed SKILL.md bodies were inspected. This static source critique uses simulated perspectives; it is not measured task-quality validation. Supporting references, scripts, services and end-to-end plugin installation were not comprehensively audited or executed. No upstream skill body is reproduced.

Scope: Superpowers 14; plugin-eval 9 including four fixtures; Product Design 10; OpenAI Developers 5; repository-local `.agents/skills/plugin-creator` 1; CodeRabbit 1; Codex Security 15. There is no `plugins/skills` directory at this snapshot. Other OpenAI entries are outside this body's review coverage.

Disposition counts: adapt: 13, profile: 35, reference: 2, reject: 5.

The simulated participants are an engineering practitioner, who assesses execution benefit; a skeptical maintainer, who examines collisions, portability and cost; and an evaluator, who proposes a concrete falsification case. Consensus is provisional curation. A profile means an optional native integration, not an immediate installation recommendation or a license grant. Adapt means integrate useful behavior into one existing owner after rights checks and local evaluation.

## Cross-cutting decisions

- Keep one owner for execution, plans, diagnosis, tests, reviews, UI review and skill maintenance. Imported routers should not compete for every coding turn.
- Superpowers contributes hypotheses, ledgers and review packaging; blanket approval, deletion, model selection and mandatory delegation require rewriting. Reject using-superpowers as an active router.
- plugin-eval is an optional measurement adapter. Its four fixtures are test data. Static scores do not establish behavioral improvement, and improve-skill contains a personal absolute dependency path.
- Product Design contributes visual capture/comparison. UX research is distinct from engineering research. Host APIs, asset rules, saved state and generated-image gates belong in its native profile.
- OpenAI Developers, CodeRabbit and Codex Security require platform tools/current contracts. Copying Markdown does not transfer those capabilities.
- Licensing is per package. This review establishes no blanket redistribution rights for openai/plugins; no unlicensed body is copied.

## Per-skill simulated scrutiny

### plugins/superpowers/skills/brainstorming/SKILL.md

[brainstorming](https://github.com/openai/plugins/blob/0722921d5542fc593105c27bd52630babd8b8c2a/plugins/superpowers/skills/brainstorming/SKILL.md): Clarify intent and compare designs before implementing.

- Practitioner: Scales discovery across probes, bounded edits and architectural work.
- Skeptic: Every path demands fresh approval; architectural work commits a spec automatically.
- Evaluator: Give an already-authorized one-file fix: reject extra approval and spec gates; ask only for materially missing information.
- Consensus: **adapt** → `grill-idea`. Absorb scope-sensitive discovery; remove blanket approval and commit rules. Benefit remains unmeasured.
- Overlap: grill-idea; change-plan; Matt grilling; pstack how.
- Dependencies: writing-plans; optional visual-companion.md.

### plugins/superpowers/skills/dispatching-parallel-agents/SKILL.md

[dispatching-parallel-agents](https://github.com/openai/plugins/blob/0722921d5542fc593105c27bd52630babd8b8c2a/plugins/superpowers/skills/dispatching-parallel-agents/SKILL.md): Delegate independent problem domains and verify their combined result.

- Practitioner: Excludes shared state and dependent failures before parallel work.
- Skeptic: Adds orchestration cost and universally forbids inherited context; independence may be misjudged.
- Evaluator: Use three failures with one shared root cause; require coupling detection and no conflicting fixes.
- Consensus: **profile** → `start`. Enable only for authorized independent work with ownership and integration checks.
- Overlap: start; subagent-driven-development.
- Dependencies: subagent runtime; task ownership; project tests.

### plugins/superpowers/skills/executing-plans/SKILL.md

[executing-plans](https://github.com/openai/plugins/blob/0722921d5542fc593105c27bd52630babd8b8c2a/plugins/superpowers/skills/executing-plans/SKILL.md): Execute a written plan with checks and recorded task progress.

- Practitioner: Critiques the plan before editing and verifies tasks.
- Skeptic: Stops for routine missing dependencies and redirects to subagents whenever available.
- Evaluator: Execute a plan with one stale command and an installable dependency; require bounded repair and transparent updates.
- Consensus: **adapt** → `start`. Absorb plan critique and evidence tracking into the existing execution owner.
- Overlap: start; change-plan.
- Dependencies: using-git-worktrees; finishing-a-development-branch; optional subagent-driven-development.

### plugins/superpowers/skills/finishing-a-development-branch/SKILL.md

[finishing-a-development-branch](https://github.com/openai/plugins/blob/0722921d5542fc593105c27bd52630babd8b8c2a/plugins/superpowers/skills/finishing-a-development-branch/SKILL.md): Verify a branch and carry out its requested integration.

- Practitioner: Preserves PR worktrees and checks the merged result before cleanup.
- Skeptic: Forces an integration menu despite clear requests and infers cleanup ownership from directory names.
- Evaluator: Request a draft PR from a managed worktree under worktrees/: require no new menu and no checkout deletion.
- Consensus: **adapt** → `verify-change`. Retain verification and preservation; use explicit ownership and existing authorization.
- Overlap: verify-change; handoff; R-stack new-feature.
- Dependencies: Git; forge tooling; tests; worktree provenance.

### plugins/superpowers/skills/receiving-code-review/SKILL.md

[receiving-code-review](https://github.com/openai/plugins/blob/0722921d5542fc593105c27bd52630babd8b8c2a/plugins/superpowers/skills/receiving-code-review/SKILL.md): Check review suggestions against source before applying them.

- Practitioner: Encourages technical rejection of wrong feedback and compatibility checks.
- Skeptic: Bans gratitude and blocks all fixes when any feedback item is unclear.
- Evaluator: Supply one valid fix, one false positive and one independent ambiguous item; require correct triage without blocking independent work.
- Consensus: **adapt** → `review`. Keep source-based triage; remove personal rhetoric and unconditional all-or-nothing pauses.
- Overlap: review; greploop; CodeRabbit.
- Dependencies: feedback; current source; tests.

### plugins/superpowers/skills/requesting-code-review/SKILL.md

[requesting-code-review](https://github.com/openai/plugins/blob/0722921d5542fc593105c27bd52630babd8b8c2a/plugins/superpowers/skills/requesting-code-review/SKILL.md): Give an independent reviewer a bounded diff and requirements.

- Practitioner: Separates requirements from implementer claims.
- Skeptic: Mandatory delegation adds cost; HEAD~1 examples can omit earlier commits.
- Evaluator: Review a three-commit task with a defect in the first commit; require full task-range coverage.
- Consensus: **adapt** → `review`. Absorb explicit base/head binding and independent review when warranted.
- Overlap: review; Matt code-review.
- Dependencies: code-reviewer.md; Git range; authorized reviewer runtime.

### plugins/superpowers/skills/subagent-driven-development/SKILL.md

[subagent-driven-development](https://github.com/openai/plugins/blob/0722921d5542fc593105c27bd52630babd8b8c2a/plugins/superpowers/skills/subagent-driven-development/SKILL.md): Coordinate plan tasks through durable progress and bounded reviews.

- Practitioner: Per-plan ledgers prevent redispatch after compaction; scoped re-reviews limit churn.
- Skeptic: A 568-line controller mandates models and multiple seats, can complete tasks with parked findings, and deletes scratch evidence.
- Evaluator: Resume partial work with a multi-commit task and critical parked finding; reject redispatch, truncated diffs, false completion and evidence deletion.
- Consensus: **reference** → `start`. Reference ledger and scoped-review techniques; avoid importing the controller without authority, cost and recovery trials.
- Overlap: start; change-plan; review; handoff.
- Dependencies: sdd-workspace; task-brief; review-package; implementer/reviewer templates; using-git-worktrees; finishing-a-development-branch; multi-agent runtime.

### plugins/superpowers/skills/systematic-debugging/SKILL.md

[systematic-debugging](https://github.com/openai/plugins/blob/0722921d5542fc593105c27bd52630babd8b8c2a/plugins/superpowers/skills/systematic-debugging/SKILL.md): Reproduce failure, test a causal hypothesis and verify the fix.

- Practitioner: Traces component boundaries and prevents accumulating speculative patches.
- Skeptic: Uses an unsupported 95% claim, arbitrary three-attempt escalation, and examples that can print sensitive environment values.
- Evaluator: Diagnose propagated secret-valued configuration: require the failing boundary with redacted observations.
- Consensus: **adapt** → `debug`. Keep hypothesis and boundary tracing; remove unsupported statistics and unsafe diagnostics.
- Overlap: debug; Matt diagnosing-bugs; pstack debug.
- Dependencies: root-cause-tracing.md; condition-based-waiting.md; defense-in-depth.md; tests.

### plugins/superpowers/skills/test-driven-development/SKILL.md

[test-driven-development](https://github.com/openai/plugins/blob/0722921d5542fc593105c27bd52630babd8b8c2a/plugins/superpowers/skills/test-driven-development/SKILL.md): Use observed failing behavior to guide minimal implementation.

- Practitioner: Requires red/green evidence and behavior-based assertions.
- Skeptic: Universal feature trigger, per-function tests and deletion mandates conflict with proportional checks and existing user work.
- Evaluator: Give a partial fix and trivial copy edit; preserve both and add meaningful regression coverage only where needed.
- Consensus: **adapt** → `tdd`. Retain requested test-first work and bug reproduction; reject deletion rituals and universal per-function coverage.
- Overlap: tdd; debug; verify-change; Matt tdd.
- Dependencies: writing-good-tests.md; project test harness.

### plugins/superpowers/skills/using-git-worktrees/SKILL.md

[using-git-worktrees](https://github.com/openai/plugins/blob/0722921d5542fc593105c27bd52630babd8b8c2a/plugins/superpowers/skills/using-git-worktrees/SKILL.md): Reuse task isolation or create it through the host adapter.

- Practitioner: Detects existing worktrees and submodules and prefers managed tools.
- Skeptic: Guesses npm/poetry setup and commits ignore changes automatically; linked state alone does not establish ownership.
- Evaluator: Open an unrelated worktree with pnpm metadata: require task ownership and correct setup without auto-committing .gitignore.
- Consensus: **adapt** → `start`. Absorb host-aware isolation checks; retain repository setup commands and ownership.
- Overlap: start; R-stack new-feature.
- Dependencies: native worktree tool or Git; project setup/test commands.

### plugins/superpowers/skills/using-superpowers/SKILL.md

[using-superpowers](https://github.com/openai/plugins/blob/0722921d5542fc593105c27bd52630babd8b8c2a/plugins/superpowers/skills/using-superpowers/SKILL.md): Force skill discovery at the start of every interaction.

- Practitioner: Makes discovery explicit and provides host references.
- Skeptic: Any-conversation trigger and 1% threshold undermine selective loading and compete with the host router.
- Evaluator: Ask an unrelated factual question; fail if it loads a process chain.
- Consensus: **reject**. Reject as an active personal router; rely on host discovery and narrowly scoped workflows.
- Overlap: start; all process routers.
- Dependencies: brainstorming; systematic-debugging; host tool references.

### plugins/superpowers/skills/verification-before-completion/SKILL.md

[verification-before-completion](https://github.com/openai/plugins/blob/0722921d5542fc593105c27bd52630babd8b8c2a/plugins/superpowers/skills/verification-before-completion/SKILL.md): Tie completion claims to observed checks and acceptance criteria.

- Practitioner: Distinguishes lint, build, behavior and requirement coverage.
- Skeptic: Same-message reruns and treating partial evidence as worthless encourage redundant checks.
- Evaluator: Provide a passing exact-tree test receipt followed by a docs-only change; require scoped claims without unrelated reruns.
- Consensus: **adapt** → `verify-change`. Keep evidence identity, freshness and limits; choose proportional verification.
- Overlap: verify-change; review; R-stack evidence-driven-testing.
- Dependencies: verification commands; diff; acceptance criteria.

### plugins/superpowers/skills/writing-plans/SKILL.md

[writing-plans](https://github.com/openai/plugins/blob/0722921d5542fc593105c27bd52630babd8b8c2a/plugins/superpowers/skills/writing-plans/SKILL.md): Break requirements into verifiable implementation tasks.

- Practitioner: Carries shared constraints and interfaces and checks spec coverage.
- Skeptic: Requires full code in plans, minute-sized steps, frequent commits and another execution-choice prompt.
- Evaluator: Plan an interface depending on unresolved library behavior; require a probe rather than invented complete code.
- Consensus: **adapt** → `change-plan`. Keep coverage and interfaces; remove speculative transcription and unnecessary execution gates.
- Overlap: change-plan; Matt to-tickets; pstack plan.
- Dependencies: spec/requirements; execution owner; repo conventions.

### plugins/superpowers/skills/writing-skills/SKILL.md

[writing-skills](https://github.com/openai/plugins/blob/0722921d5542fc593105c27bd52630babd8b8c2a/plugins/superpowers/skills/writing-skills/SKILL.md): Improve skills through baseline scenarios and repeated behavioral trials.

- Practitioner: Separates rule, technique, recognition and retrieval tests; includes no-guidance controls and repeats.
- Skeptic: 679-line root, deletion rituals and loophole hardening can overfit; trigger-only descriptions conflict with the spec's what-and-when guidance.
- Evaluator: Test a wording change on held-out negative triggers and user overrides, with deliberately wrong grader inputs.
- Consensus: **adapt** → `skill-maintenance`. Adopt paired trials and failure-specific wording in a short router; do not claim bulletproof compliance.
- Overlap: skill-maintenance; skill-creator; plugin-eval.
- Dependencies: TDD background; testing-skills-with-subagents.md; anthropic-best-practices.md; optional Graphviz.

### plugins/plugin-eval/skills/evaluate-plugin/SKILL.md

[evaluate-plugin](https://github.com/openai/plugins/blob/0722921d5542fc593105c27bd52630babd8b8c2a/plugins/plugin-eval/skills/evaluate-plugin/SKILL.md): Explain plugin structure findings and prepare benchmark follow-up.

- Practitioner: Groups manifest, budget, skill and code findings into priorities.
- Skeptic: Shares triggers with its umbrella and skill auditor; assumes a CLI and its scoring model.
- Evaluator: Evaluate a plugin with one broken link and one harmless long example; require explainable structural findings without runtime-quality claims.
- Consensus: **profile** → `skill-maintenance`. Use an optional evaluator adapter under one maintenance router; static scores are diagnostic.
- Overlap: skill-maintenance; plugin-eval; evaluate-skill.
- Dependencies: plugin-eval CLI; chat-first-workflows.md; plugin manifest.

### plugins/plugin-eval/skills/evaluate-skill/SKILL.md

[evaluate-skill](https://github.com/openai/plugins/blob/0722921d5542fc593105c27bd52630babd8b8c2a/plugins/plugin-eval/skills/evaluate-skill/SKILL.md): Inspect skill structure and distinguish estimates from observed usage.

- Practitioner: Checks metadata, references and helper quality and points to measurement.
- Skeptic: Prefers user paths over repo context and automatically writes benchmark setup for analysis requests.
- Evaluator: Install two same-named skills and request read-only analysis; require target resolution and no unsolicited benchmark files.
- Consensus: **profile** → `skill-maintenance`. Use with explicit target and write scope, avoiding competing evaluator entry points.
- Overlap: skill-maintenance; plugin-eval; evaluate-plugin.
- Dependencies: plugin-eval CLI; chat-first-workflows.md; optional improve-skill.

### plugins/plugin-eval/skills/improve-skill/SKILL.md

[improve-skill](https://github.com/openai/plugins/blob/0722921d5542fc593105c27bd52630babd8b8c2a/plugins/plugin-eval/skills/improve-skill/SKILL.md): Translate evaluation findings into a bounded skill revision.

- Practitioner: Compares before/after findings and distinguishes required fixes.
- Skeptic: Hardcodes /Users/benlesh/.codex/skills/skill-creator/SKILL.md and emphasizes static score optimization.
- Evaluator: Run on Windows and propose shorter wording that breaks routing; require portable discovery and regression rejection.
- Consensus: **adapt** → `skill-maintenance`. Absorb before/after evidence; replace personal paths and require behavior checks.
- Overlap: skill-maintenance; skill-creator; writing-skills.
- Dependencies: plugin-eval CLI; runtime-discovered skill-creator; chat-first-workflows.md.

### plugins/plugin-eval/skills/metric-pack-designer/SKILL.md

[metric-pack-designer](https://github.com/openai/plugins/blob/0722921d5542fc593105c27bd52630babd8b8c2a/plugins/plugin-eval/skills/metric-pack-designer/SKILL.md): Build deterministic local checks fitting the evaluator result schema.

- Practitioner: Stable check IDs and separated metrics support reproducible comparisons.
- Skeptic: Schema-valid metrics may grade the wrong behavior; metric scripts add a local trust boundary.
- Evaluator: Feed an incomplete result to a new metric pack; require failure with a stable explanation.
- Consensus: **profile** → `skill-maintenance`. Use for a concrete missing metric; schema validity is not grader validity.
- Overlap: skill-maintenance; plugin-eval.
- Dependencies: plugin-eval CLI; metric-pack-manifest.md; local metric script.

### plugins/plugin-eval/skills/plugin-eval/SKILL.md

[plugin-eval](https://github.com/openai/plugins/blob/0722921d5542fc593105c27bd52630babd8b8c2a/plugins/plugin-eval/skills/plugin-eval/SKILL.md): Route skill/plugin analysis to structural checks or measured benchmarks.

- Practitioner: Labels static token estimates separately from harness measurement.
- Skeptic: Overlaps focused auditors and broad chat phrases may trigger unrelated tasks.
- Evaluator: Ask what to fix first about an application bug, then explicitly request a skill benchmark; require correct routing.
- Consensus: **profile** → `skill-maintenance`. Choose this or focused entry points, not all as competing defaults.
- Overlap: skill-maintenance; evaluate-skill; evaluate-plugin; metric-pack-designer.
- Dependencies: plugin-eval CLI; benchmark harness; evaluation schema references.

### plugins/plugin-eval/fixtures/minimal-plugin/skills/minimal-plugin-skill/SKILL.md

[minimal-plugin-skill](https://github.com/openai/plugins/blob/0722921d5542fc593105c27bd52630babd8b8c2a/plugins/plugin-eval/fixtures/minimal-plugin/skills/minimal-plugin-skill/SKILL.md): Test plugin-level skill discovery.

- Practitioner: Exercises an upstream discovery or evaluation contract.
- Skeptic: A test fixture is not an end-user capability and adds catalog noise.
- Evaluator: Production discovery must exclude this fixtures/ path.
- Consensus: **reject**. Retain as upstream test data only, never an active personal skill.
- Overlap: plugin-eval fixtures.
- Dependencies: upstream evaluator tests.

### plugins/plugin-eval/fixtures/minimal-skill/SKILL.md

[minimal-skill](https://github.com/openai/plugins/blob/0722921d5542fc593105c27bd52630babd8b8c2a/plugins/plugin-eval/fixtures/minimal-skill/SKILL.md): Provide a minimal evaluation test case.

- Practitioner: Exercises an upstream discovery or evaluation contract.
- Skeptic: A test fixture is not an end-user capability and adds catalog noise.
- Evaluator: Production discovery must exclude this fixtures/ path.
- Consensus: **reject**. Retain as upstream test data only, never an active personal skill.
- Overlap: plugin-eval fixtures.
- Dependencies: upstream evaluator tests; references/details.md.

### plugins/plugin-eval/fixtures/multi-skill-plugin/skills/alpha/SKILL.md

[alpha](https://github.com/openai/plugins/blob/0722921d5542fc593105c27bd52630babd8b8c2a/plugins/plugin-eval/fixtures/multi-skill-plugin/skills/alpha/SKILL.md): Represent the first skill in a multi-skill test plugin.

- Practitioner: Exercises an upstream discovery or evaluation contract.
- Skeptic: A test fixture is not an end-user capability and adds catalog noise.
- Evaluator: Production discovery must exclude this fixtures/ path.
- Consensus: **reject**. Retain as upstream test data only, never an active personal skill.
- Overlap: plugin-eval fixtures.
- Dependencies: upstream evaluator tests.

### plugins/plugin-eval/fixtures/multi-skill-plugin/skills/beta/SKILL.md

[beta](https://github.com/openai/plugins/blob/0722921d5542fc593105c27bd52630babd8b8c2a/plugins/plugin-eval/fixtures/multi-skill-plugin/skills/beta/SKILL.md): Represent the second skill in a multi-skill test plugin.

- Practitioner: Exercises an upstream discovery or evaluation contract.
- Skeptic: A test fixture is not an end-user capability and adds catalog noise.
- Evaluator: Production discovery must exclude this fixtures/ path.
- Consensus: **reject**. Retain as upstream test data only, never an active personal skill.
- Overlap: plugin-eval fixtures.
- Dependencies: upstream evaluator tests.

### .agents/skills/plugin-creator/SKILL.md

[plugin-creator](https://github.com/openai/plugins/blob/0722921d5542fc593105c27bd52630babd8b8c2a/.agents/skills/plugin-creator/SKILL.md): Scaffold a Codex plugin and optional marketplace entry.

- Practitioner: Preserves marketplace metadata and makes companion surfaces optional.
- Skeptic: Assumes marketplace schema and personal paths; overwrite and team destination require ownership.
- Evaluator: Create a skill-only plugin beside a marketplace with custom interface metadata; require preservation and correct relative paths.
- Consensus: **profile** → `skill-maintenance`. Use a native packaging adapter with current manifest validation; packaging is not quality validation.
- Overlap: skill-maintenance; skill-creator.
- Dependencies: create_basic_plugin.py; plugin-json-spec.md; skill-creator quick_validate.py; Codex marketplace schema.

### plugins/coderabbit/skills/coderabbit-review/SKILL.md

[code-review](https://github.com/openai/plugins/blob/0722921d5542fc593105c27bd52630babd8b8c2a/plugins/coderabbit/skills/coderabbit-review/SKILL.md): Run a scoped CodeRabbit review and report its actual findings.

- Practitioner: Keeps attribution honest and parses machine-readable findings.
- Skeptic: Generic code-review name collides; automatic curl-pipe-shell install and ten-minute silence conflict with host policy.
- Evaluator: Simulate a missing CLI, malformed NDJSON and timeout; require supported prerequisite handling and no invented success.
- Consensus: **profile** → `review`. Enable only for explicit CodeRabbit requests through a supported install/auth adapter.
- Overlap: review; Matt code-review; greploop.
- Dependencies: CodeRabbit CLI/auth; network service; Git diff; optional .coderabbit.yaml/AGENTS.md.

### plugins/product-design/skills/audit/SKILL.md

[audit](https://github.com/openai/plugins/blob/0722921d5542fc593105c27bd52630babd8b8c2a/plugins/product-design/skills/audit/SKILL.md): Tie product-flow UX findings to captured and inspected states.

- Practitioner: Requires screenshots, numbered steps and accessibility limits.
- Skeptic: Capture rituals and an automatic Figma follow-up add friction; browser APIs are host-specific.
- Evaluator: Audit a login-blocked flow; require a named limit and no invented later screenshots or compliance claim.
- Consensus: **profile** → `ui-review`. Use native evidence-based product audits; avoid a second competing UX owner.
- Overlap: ui-review; design-qa.
- Dependencies: index; user-context; critical-overrides.md; browser capture; design-audit-framework.md; Figma only if requested.

### plugins/product-design/skills/design-qa/SKILL.md

[design-qa](https://github.com/openai/plugins/blob/0722921d5542fc593105c27bd52630babd8b8c2a/plugins/product-design/skills/design-qa/SKILL.md): Compare a rendered prototype to its visual source and recheck fixes.

- Practitioner: Matches viewport, state and density and requires post-fix captures.
- Skeptic: Phone-template constraints and absolute raster rules can reject valid repo-native assets.
- Evaluator: Compare 2x source with 1x implementation and supplied SVG branding; require normalization without false drift or regeneration.
- Consensus: **profile** → `ui-review`. Use as opt-in fidelity verification with bounded polish loops and established-asset reuse.
- Overlap: ui-review; audit; verify-change.
- Dependencies: source visual; rendered implementation; critical-overrides.md; browser; qa-rubric.md; mobile runtime check when applicable.

### plugins/product-design/skills/get-context/SKILL.md

[get-context](https://github.com/openai/plugins/blob/0722921d5542fc593105c27bd52630babd8b8c2a/plugins/product-design/skills/get-context/SKILL.md): Resolve the UI target and user outcome before design work.

- Practitioner: Continues once sufficient facts are known and avoids repeated questions.
- Skeptic: Competes with intake owners and includes a canned duration unsupported by task evidence.
- Evaluator: Give a complete brief/reference; require concise playback and continuation without re-asking or invented timing.
- Consensus: **reference** → `grill-idea`. Absorb minimum-brief behavior into one intake owner; retain native scope.
- Overlap: grill-idea; start; product-design index.
- Dependencies: index; user-context; critical-overrides.md; next focused skill.

### plugins/product-design/skills/ideate/SKILL.md

[ideate](https://github.com/openai/plugins/blob/0722921d5542fc593105c27bd52630babd8b8c2a/plugins/product-design/skills/ideate/SKILL.md): Generate distinct visual directions from an actual design brief.

- Practitioner: Preserves image attachments and maps selections to displayed results.
- Skeptic: Default three-image generation and forced revision-before-build can add unnecessary cost.
- Evaluator: Return images out of request order and select the second displayed image; require the correct source and constraints.
- Consensus: **profile** → `prototype`. Use when visual alternatives are wanted; respect user count and avoid a prerequisite for ordinary UI edits.
- Overlap: prototype; grill-idea; imagegen.
- Dependencies: get-context; index; user-context; critical-overrides.md; Image Gen.

### plugins/product-design/skills/image-to-code/SKILL.md

[image-to-code](https://github.com/openai/plugins/blob/0722921d5542fc593105c27bd52630babd8b8c2a/plugins/product-design/skills/image-to-code/SKILL.md): Implement a selected visual and verify its rendered interactions.

- Practitioner: Requires an exact source, working core controls and browser evidence.
- Skeptic: Unconditional generation/delegation and SVG bans conflict with existing assets; stated transparency limitation is stale for this tool.
- Evaluator: Recreate a screen with supplied SVG logo and transparent cutout; require reuse, current tool capability and matching-state verification.
- Consensus: **profile** → `prototype`. Use maintained native integration with host adaptation; do not copy stale capability assertions.
- Overlap: prototype; ui-review; imagegen.
- Dependencies: index; get-context; user-context; critical-overrides.md; local-prototype-preflight.md; Image Gen; design-qa; browser; optional asset agents.

### plugins/product-design/skills/index/SKILL.md

[index](https://github.com/openai/plugins/blob/0722921d5542fc593105c27bd52630babd8b8c2a/plugins/product-design/skills/index/SKILL.md): Route explicit Product Design requests to a focused workflow.

- Practitioner: Separates audit, clone, redesign and fidelity checking.
- Skeptic: Forces image selection for no-target builds despite broad authorization and hardcodes host APIs.
- Evaluator: Ask for a one-line UI edit then an explicit audit; require no design funnel for the edit and direct audit routing.
- Consensus: **profile**. Keep only as the native plugin router, not the general engineering front door.
- Overlap: start; Product Design focused skills.
- Dependencies: focused skills; critical-overrides.md; communication-protocol.md; host browser/Sites adapters.

### plugins/product-design/skills/research/SKILL.md

[research](https://github.com/openai/plugins/blob/0722921d5542fc593105c27bd52630babd8b8c2a/plugins/product-design/skills/research/SKILL.md): Investigate current user friction with attributable product evidence.

- Practitioner: Separates observations, inference, feature requests and reliability concerns.
- Skeptic: Generic research name collides with technical research; complaint visibility is not population frequency.
- Evaluator: Supply three reposts of one complaint and an independent issue; require deduplication and qualified frequency.
- Consensus: **profile** → `research`. Keep a narrowly scoped UX-research profile distinct from engineering fact research.
- Overlap: research; Matt research; Notion research.
- Dependencies: index; user-context; critical-overrides.md; web search; authorized internal connectors optional.

### plugins/product-design/skills/share/SKILL.md

[share](https://github.com/openai/plugins/blob/0722921d5542fc593105c27bd52630babd8b8c2a/plugins/product-design/skills/share/SKILL.md): Deploy a verified prototype to the selected hosting target.

- Practitioner: Checks concrete build artifacts and returns an actual working URL.
- Skeptic: Depends on native Sites/runtime contracts and can duplicate deployment ownership.
- Evaluator: Choose an unavailable provider; require a clear limit and no silent switch to another host/account.
- Consensus: **profile**. Keep explicit deployment scope and verify the selected target's result.
- Overlap: prototype; Sites hosting; deployment adapters.
- Dependencies: index; user-context; critical-overrides.md; chosen deployment tool; runtime checks.

### plugins/product-design/skills/url-to-code/SKILL.md

[url-to-code](https://github.com/openai/plugins/blob/0722921d5542fc593105c27bd52630babd8b8c2a/plugins/product-design/skills/url-to-code/SKILL.md): Recreate a permitted live site from observed structure and interactions.

- Practitioner: Captures source states and compares the clone on desktop/mobile.
- Skeptic: Every-interaction coverage can be unbounded; downloadable assets are not automatically licensed for reuse.
- Evaluator: Use an inaccessible authenticated state and licensed imagery; require bounded scope, rights-aware reuse and explicit limits.
- Consensus: **profile** → `prototype`. Enable for an explicit faithful clone with a defined flow, not ordinary implementation.
- Overlap: prototype; image-to-code; ui-review.
- Dependencies: index; get-context; user-context; critical-overrides.md; browser DOM/capture; local-prototype-preflight.md; design-qa; Image Gen fallback.

### plugins/product-design/skills/user-context/SKILL.md

[user-context](https://github.com/openai/plugins/blob/0722921d5542fc593105c27bd52630babd8b8c2a/plugins/product-design/skills/user-context/SKILL.md): Load and curate durable design references for the native plugin.

- Practitioner: Checks writable persistence and opens only task-relevant references.
- Skeptic: Global context can carry stale cross-project assumptions and sensitive images.
- Evaluator: Use read-only state and a new style override; require no saved claim and the current instruction to win.
- Consensus: **profile**. Use for requested design memory in native scope; exclude secrets/customer records.
- Overlap: handoff; project memory.
- Dependencies: CODEX_HOME state directory; user_context_preflight.py; init_user_context.py; onboarding.md; index; critical-overrides.md.

### plugins/openai-developers/skills/agents-sdk/SKILL.md

[agents-sdk](https://github.com/openai/plugins/blob/0722921d5542fc593105c27bd52630babd8b8c2a/plugins/openai-developers/skills/agents-sdk/SKILL.md): Build and locally verify a small OpenAI Agents SDK application.

- Practitioner: Starts with one agent and a runnable contract; evals exercise the real path.
- Skeptic: Python, PNG diagrams and deployment-manager layout may overconstrain existing projects.
- Evaluator: Extend a TypeScript agent without deployment; require its package manager, a focused smoke check and no manager checkout.
- Consensus: **profile** → `prototype`. Use only for SDK work with current official docs and project conventions.
- Overlap: prototype; api-design; docs.
- Dependencies: official Agents/sandbox docs; openai-platform-api-key; Agents SDK; Deployment Manager only when requested.

### plugins/openai-developers/skills/build-chatgpt-app/SKILL.md

[build-chatgpt-app](https://github.com/openai/plugins/blob/0722921d5542fc593105c27bd52630babd8b8c2a/plugins/openai-developers/skills/build-chatgpt-app/SKILL.md): Build an Apps SDK server/widget from current examples and contracts.

- Practitioner: Plans real side effects and tests MCP/widget behavior and retries.
- Skeptic: Long root may overfetch docs or scaffold beyond a tool-only request.
- Evaluator: Adapt an existing tool-only app; require no widget scaffold, accurate hints and a reachable MCP check.
- Consensus: **profile** → `prototype`. Keep a platform-specific native skill, with scope controlling structure.
- Overlap: prototype; api-design; docs; chatgpt-app-submission.
- Dependencies: openai-docs or official docs tools; Apps SDK/MCP Apps; archetype/validation references; optional scaffold script.

### plugins/openai-developers/skills/chatgpt-app-submission/SKILL.md

[chatgpt-app-submission](https://github.com/openai/plugins/blob/0722921d5542fc593105c27bd52630babd8b8c2a/plugins/openai-developers/skills/chatgpt-app-submission/SKILL.md): Prepare truthful Apps submission metadata from tool implementations.

- Practitioner: Inspects actual side effects and separates missing outputSchema warnings.
- Skeptic: Fixed test counts and repeated approval gates may obstruct authorized work; hint semantics need current verification.
- Evaluator: Include a read-named tool mutating through a helper; require honest hints and no invented schema.
- Consensus: **profile**. Use for an explicit submission artifact with current platform rules.
- Overlap: api-design; review; build-chatgpt-app.
- Dependencies: MCP implementation/descriptors; current submission schema/guidelines; LICENSE.txt.

### plugins/openai-developers/skills/openai-api-troubleshooting/SKILL.md

[openai-api-troubleshooting](https://github.com/openai/plugins/blob/0722921d5542fc593105c27bd52630babd8b8c2a/plugins/openai-developers/skills/openai-api-troubleshooting/SKILL.md): Classify API failures from transport and concrete service errors.

- Practitioner: Distinguishes quota from transient limits and transport from API responses.
- Skeptic: Mandates sandbox escalation and a fixed starter model, both subject to host/current-state conflicts.
- Evaluator: Provide insufficient_quota 429 and DNS failure under never-escalate policy; require distinct causes and no prohibited escalation.
- Consensus: **adapt** → `debug`. Absorb error classification into debug references; use allowed tools/current docs.
- Overlap: debug; docs; openai-platform-api-key.
- Dependencies: openai-docs; actual API error; key skill only for provisioning.

### plugins/openai-developers/skills/openai-platform-api-key/SKILL.md

[openai-platform-api-key](https://github.com/openai/plugins/blob/0722921d5542fc593105c27bd52630babd8b8c2a/plugins/openai-developers/skills/openai-platform-api-key/SKILL.md): Select or provision API credentials without exposing plaintext.

- Practitioner: Uses redacted checks, secure provisioning and confirmed destinations.
- Skeptic: Provider-unspecified triggers and mandatory reuse questions before offline coding create extra gates.
- Evaluator: Request a provider-neutral offline edit with existing authorization, then explicit new-key setup; require no unnecessary secret access and secure provisioning only for the latter.
- Consensus: **profile**. Keep native credential setup for relevant access decisions, honoring chosen provider and authorization.
- Overlap: credential adapters; agents-sdk; build-chatgpt-app.
- Dependencies: Platform connector; openai-platform-api-key.mjs; ignored env destination; destination confirmation.

### plugins/codex-security/skills/assess-patch-risk/SKILL.md

[assess-patch-risk](https://github.com/openai/plugins/blob/0722921d5542fc593105c27bd52630babd8b8c2a/plugins/codex-security/skills/assess-patch-risk/SKILL.md): Assess immutable patches through impact, protection and recovery evidence.

- Practitioner: Separates impact from likelihood and treats auto-merge labels as advice.
- Skeptic: Requires schema/storage machinery and consequential analysis cost.
- Evaluator: Provide a tiny green patch weakening tenant authorization; require block/revise and no merge.
- Consensus: **profile** → `review`. Use native integration for consequential patches; independently rewrite risk dimensions only after rights review.
- Overlap: review; verify-change.
- Dependencies: artifact-storage.md; risk-rubric.md; patch-risk-assessment schema; validator helper; immutable patch.

### plugins/codex-security/skills/attack-path-analysis/SKILL.md

[attack-path-analysis](https://github.com/openai/plugins/blob/0722921d5542fc593105c27bd52630babd8b8c2a/plugins/codex-security/skills/attack-path-analysis/SKILL.md): Trace security candidates through reachability, controls and impact.

- Practitioner: Requires counterevidence and preserves candidate decisions separately from severity.
- Skeptic: Phase/tool contracts are complex; broad activation could lack required inputs.
- Evaluator: Give two candidates sharing a sink with one unreachable source; require distinct decisions and exact counterevidence.
- Consensus: **profile** → `review`. Keep within native scans or explicit attack-path work; effectiveness is unmeasured.
- Overlap: review; validation; threat-model.
- Dependencies: threat model; validated candidates; scan-artifacts.md; severity-policy.md; attack-path-facts.md; optional workbench.

### plugins/codex-security/skills/deep-security-scan/SKILL.md

[deep-security-scan](https://github.com/openai/plugins/blob/0722921d5542fc593105c27bd52630babd8b8c2a/plugins/codex-security/skills/deep-security-scan/SKILL.md): Aggregate repeated independent security scans with durable completion.

- Practitioner: Preserves scan identity, partial coverage and terminal error distinctions.
- Skeptic: May run for days and requires a dedicated coordinator; Markdown cannot supply that runtime.
- Evaluator: Detach/rejoin a scoped scan with a failed worker; require same identity, preserved results and partial coverage.
- Consensus: **profile** → `review`. Enable only for explicit deep audits with native server and defined budget.
- Overlap: review; security-scan; security-diff-scan.
- Dependencies: Security plugin server; deep-scan coordinator; completion tool; scan-prologue.md; core-scan.md; optional Daybreak advisory.

### plugins/codex-security/skills/define-security-policy/SKILL.md

[define-security-policy](https://github.com/openai/plugins/blob/0722921d5542fc593105c27bd52630babd8b8c2a/plugins/codex-security/skills/define-security-policy/SKILL.md): Draft repository security boundaries and reportability guidance.

- Practitioner: Distinguishes reporting files from scanner policy and confirms exclusions with owners.
- Skeptic: May conflict with SECURITY.md conventions; resolver/approval workflow is host-specific.
- Evaluator: Use .github/SECURITY.md and conflicting nested policies; require no overwrite and explicit unresolved exclusions.
- Consensus: **profile** → `docs`. Keep explicit security-policy scope and reviewable owner decisions.
- Overlap: docs; domain-model; threat-model.
- Dependencies: security-guidance.md; resolve-security-md helper; owner context; source/deployment evidence.

### plugins/codex-security/skills/finding-discovery/SKILL.md

[finding-discovery](https://github.com/openai/plugins/blob/0722921d5542fc593105c27bd52630babd8b8c2a/plugins/codex-security/skills/finding-discovery/SKILL.md): Collect source-backed candidates without declaring them confirmed.

- Practitioner: Preserves concrete instances and advisory seeds.
- Skeptic: Dense enumeration costs context and may overfit old bug families; phase machinery is not portable.
- Evaluator: Seed archive containment plus louder auth flaw; require closure of the exact archive row rather than substitution.
- Consensus: **profile** → `review`. Keep native/explicit discovery and test recall/false positives on held-out repos.
- Overlap: review; security-scan; validation.
- Dependencies: security-guidance.md; scan-artifacts.md; candidate helpers; threat model; validation.

### plugins/codex-security/skills/fix-finding/SKILL.md

[fix-finding](https://github.com/openai/plugins/blob/0722921d5542fc593105c27bd52630babd8b8c2a/plugins/codex-security/skills/fix-finding/SKILL.md): Close a security boundary while preserving legitimate behavior.

- Practitioner: Orders complete security closure and compatibility before diff minimality.
- Skeptic: Investigation/review seats add cost; generate/apply/verify stages can be conflated.
- Evaluator: Test encoded traversal plus legitimate paths; require alternate-attack closure and no verified label in Apply.
- Consensus: **profile** → `debug`. Use explicit native remediation staging and preserve complete-boundary minimality.
- Overlap: debug; review; verify-change; minimalist.
- Dependencies: artifact-storage.md; finding; reproducer/control; optional read-only agents; staged workbench tools.

### plugins/codex-security/skills/propose-security-hardening/SKILL.md

[propose-security-hardening](https://github.com/openai/plugins/blob/0722921d5542fc593105c27bd52630babd8b8c2a/plugins/codex-security/skills/propose-security-hardening/SKILL.md): Compare systemic security designs against evidence and local fixes.

- Practitioner: Allows local remediation and distinguishes facts from proposals.
- Skeptic: Large portfolios and voice requirements may overproduce docs for isolated defects.
- Evaluator: Give two unrelated local defects; require local_remediation_preferred rather than invented architecture.
- Consensus: **profile** → `api-design`. Use for requested systemic decisions; proposals never count as closed vulnerabilities.
- Overlap: api-design; domain-model; complexity; simulate-discussion.
- Dependencies: artifact-storage.md; source/disclosure evidence; proposal-format.md; optional scan artifacts; optional Mermaid.

### plugins/codex-security/skills/security-diff-scan/SKILL.md

[security-diff-scan](https://github.com/openai/plugins/blob/0722921d5542fc593105c27bd52630babd8b8c2a/plugins/codex-security/skills/security-diff-scan/SKILL.md): Review an exact code-change range through security validation.

- Practitioner: Accounts for deleted files and all candidates before finalization.
- Skeptic: IDs, drafts, goals and recovery tools strongly couple to the host.
- Evaluator: Interrupt after discovery of a deleted auth guard; require resumed same scan and validation without duplication.
- Consensus: **profile** → `review`. Keep optional specialist diff review through available native tooling.
- Overlap: review; security-scan; deep-security-scan.
- Dependencies: Security tools or terminal helpers; config-preflight.md; threat-model; finding-discovery; validation; attack-path-analysis; scan schemas.

### plugins/codex-security/skills/security-scan/SKILL.md

[security-scan](https://github.com/openai/plugins/blob/0722921d5542fc593105c27bd52630babd8b8c2a/plugins/codex-security/skills/security-scan/SKILL.md): Audit one authorized repository scope with honest coverage.

- Practitioner: Keeps context/scope and distinguishes SDK-owned finalization.
- Skeptic: Broader than diff review and depends on substantial runtime contracts.
- Evaluator: Request one directory in an SDK-owned scan; require no widening, duplicate start, self-finalization or clean bill after partial review.
- Consensus: **profile** → `review`. Enable for explicit repository audits, not general review wording.
- Overlap: review; security-diff-scan; deep-security-scan.
- Dependencies: scan-prologue.md; core-scan.md; capability preflight; SDK/workbench or finalizer; scope helpers.

### plugins/codex-security/skills/threat-model/SKILL.md

[threat-model](https://github.com/openai/plugins/blob/0722921d5542fc593105c27bd52630babd8b8c2a/plugins/codex-security/skills/threat-model/SKILL.md): Map revision-bound security assumptions and trust boundaries.

- Practitioner: Binds reuse to version and keeps supplied context distinct from generated assumptions.
- Skeptic: Shared cache and artifacts are host-specific; stale reuse may hide changed paths.
- Evaluator: Change revision or supply narrower context after cache creation; require a fresh per-scan model without cache overwrite.
- Consensus: **profile** → `domain-model`. Keep explicit modeling/native phase with visible identity and assumptions.
- Overlap: domain-model; review; define-security-policy.
- Dependencies: artifact-storage.md; scan-artifacts.md; security-guidance.md; threat-model.md reference; source/deployment context.

### plugins/codex-security/skills/track-findings/SKILL.md

[track-findings](https://github.com/openai/plugins/blob/0722921d5542fc593105c27bd52630babd8b8c2a/plugins/codex-security/skills/track-findings/SKILL.md): Publish reviewed findings to a verified tracker destination.

- Practitioner: Checks source, audience, duplicates and uncertain writes.
- Skeptic: Connected-account/disclosure workflow is heavy; scans cannot imply publication.
- Evaluator: Timeout after issue creation and resume; require reconciliation/reuse, no duplicate or public fallback.
- Consensus: **profile**. Keep explicit tracking, preserving approved payload, audience and destination.
- Overlap: handoff; issue tracking.
- Dependencies: sealed artifacts; validate_tracking_source.py; selected connector/CLI; provider references; mutation approval.

### plugins/codex-security/skills/triage-finding/SKILL.md

[triage-finding](https://github.com/openai/plugins/blob/0722921d5542fc593105c27bd52630babd8b8c2a/plugins/codex-security/skills/triage-finding/SKILL.md): Assess supplied vulnerability claims from static code and policy.

- Practitioner: Separates confirmed/disproven/unresolved and ranks uncertainty separately.
- Skeptic: Static confirmed can be mistaken for runtime validation; imports/contracts require adapters.
- Evaluator: Give a claim dependent on unknown deployment; require needs_review with a precise gap.
- Consensus: **profile** → `review`. Keep distinct read-only triage with static limits; fixes/writeback need explicit scope.
- Overlap: review; validation; verify-fix.
- Dependencies: static-finding-assessment.md; security policy resolver; triage-result-contract.md; selected intake reference.

### plugins/codex-security/skills/validation/SKILL.md

[validation](https://github.com/openai/plugins/blob/0722921d5542fc593105c27bd52630babd8b8c2a/plugins/codex-security/skills/validation/SKILL.md): Test or falsify candidate vulnerabilities with proportional evidence.

- Practitioner: Uses real interfaces and controls, retaining proof gaps when setup fails.
- Skeptic: PoCs/debuggers/builds consume budget and create side effects; phase outputs do not belong in routine tests.
- Evaluator: Use nonbuilding service with complete static tuple; require bounded setup and calibrated static fallback.
- Consensus: **profile** → `verify-change`. Use within authorized security work; keep method labels and per-instance outcomes.
- Overlap: verify-change; debug; triage-finding.
- Dependencies: candidates; scan-artifacts.md; validation-guidance.md; static-finding-assessment.md; optional tests/debuggers/ASan; disposable outputs.

### plugins/codex-security/skills/verify-fix/SKILL.md

[verify-fix](https://github.com/openai/plugins/blob/0722921d5542fc593105c27bd52630babd8b8c2a/plugins/codex-security/skills/verify-fix/SKILL.md): Read-only checks that each supplied security finding is closed.

- Practitioner: Follows renamed code and alternate paths rather than trusting ticket state.
- Skeptic: Strict no-write checks exclude many test runners; JSON contract must not hijack generic verification.
- Evaluator: Rename vulnerable function and supply unrelated green suite; require still_vulnerable or inconclusive.
- Consensus: **profile** → `verify-change`. Keep explicit security verification with candid unavailable-proof reporting.
- Overlap: verify-change; validation; fix-finding.
- Dependencies: supplied finding; current source; static-finding-assessment.md; read-only focused checks.

### plugins/codex-security/skills/vulnerability-writeup/SKILL.md

[vulnerability-writeup](https://github.com/openai/plugins/blob/0722921d5542fc593105c27bd52630babd8b8c2a/plugins/codex-security/skills/vulnerability-writeup/SKILL.md): Write disclosures whose impact and versions match inspected evidence.

- Practitioner: Separates source, unexecuted PoCs, runtime observations and release evidence.
- Skeptic: One drafting agent per finding and detailed voice rules add cost; absent source requires an accepted limitation.
- Evaluator: Give unexecuted PoC and shallow history; require no fabricated output or first-affected version.
- Consensus: **profile** → `docs`. Use requested disclosure scope; adapt writing/delegation to host while preserving factual gates.
- Overlap: docs; research; review.
- Dependencies: artifact-storage.md; report-format.md; source/releases or accepted report-only scope; drafting agent per finding; authorized disposable PoC environment.

## Evidence still needed

Before promotion, run held-out trigger/negative-trigger cases, user overrides, missing-tool and interruption cases, and paired task runs against the existing owner and a competent no-skill baseline. Log actual files read, artifact correctness, omitted criteria, latency and measured usage. Seed graders with deliberately wrong outputs. These are proposed checks and were not run by this source review.
