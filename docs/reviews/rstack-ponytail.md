# R-stack and Ponytail review

These are source assessments of pinned instructions, not rerun benchmarks. Practitioner, Skeptic, and Evaluator are simulated roles; consensus is a curation judgment. Upstream instructions were inspected as data and were not installed or executed.

## ponytail: ponytail-audit

[Pinned source](https://github.com/DietrichGebert/ponytail/blob/96608e078b2d5ea607c5c3b8b5a54d1c1fba6846/skills/ponytail-audit/SKILL.md)

Assess a requested repository area for defects, operational risk, and avoidable complexity.

- **Practitioner (simulated):** Maps high-impact flows instead of treating all files as equally important.
- **Skeptic (simulated):** Whole-repository scope can exceed available context; proposed line savings are estimates, not observed benefit.
- **Evaluator (simulated):** Audit a multi-service fixture with an inaccessible service; explicitly bound coverage and omit unsupported deletion claims.
- **Consensus (simulated):** Offer repository-wide assessment only when requested; distinguish it from a bounded change review.

Decision: **profile**. Owner: `review`. Dependencies: Repository context, Runtime evidence when available. Overlap: code-review-and-quality, security-and-hardening.

## ponytail: ponytail-debt

[Pinned source](https://github.com/DietrichGebert/ponytail/blob/96608e078b2d5ea607c5c3b8b5a54d1c1fba6846/skills/ponytail-debt/SKILL.md)

Collect explicitly marked shortcuts and the conditions for revisiting them.

- **Practitioner (simulated):** Turns documented deliberate limits into a discoverable ledger.
- **Skeptic (simulated):** Only captures one comment convention; absence of markers cannot establish absence of debt.
- **Evaluator (simulated):** Scan a repo with one marked shortcut and one known unmarked compromise; report marker coverage without declaring the repo debt-free.
- **Consensus (simulated):** Use a documented grep/report when useful; another default skill is unnecessary.

Decision: **reference**. Owner: `docs`. Dependencies: Repository marker convention. Overlap: documentation-and-adrs.

## ponytail: ponytail-gain

[Pinned source](https://github.com/DietrichGebert/ponytail/blob/96608e078b2d5ea607c5c3b8b5a54d1c1fba6846/skills/ponytail-gain/SKILL.md)

Display the author's published benchmark results and their stated scope.

- **Practitioner (simulated):** Makes the measurement setup and no-skill baseline visible.
- **Skeptic (simulated):** Historical author-controlled averages do not establish savings in this project or transfer to another model.
- **Evaluator (simulated):** Ask how much the current task saved without a measured baseline; do not invent a counterfactual saving.
- **Consensus (simulated):** Keep linked benchmark evidence, not an active skill or a personal-project performance claim.

Decision: **reference**. Owner: `reference only`. Dependencies: Author's benchmark report. Overlap: benchmark-checklist, plugin-eval.

## ponytail: ponytail-help

[Pinned source](https://github.com/DietrichGebert/ponytail/blob/96608e078b2d5ea607c5c3b8b5a54d1c1fba6846/skills/ponytail-help/SKILL.md)

Explain Ponytail modes, entrypoints, installation, and update commands.

- **Practitioner (simulated):** Useful for people who selected that external product.
- **Skeptic (simulated):** Installation-specific help adds no capability to the independent personal pack and can encourage duplicate installation.
- **Evaluator (simulated):** Ask about the personal pack; show its actual installed names rather than Ponytail commands.
- **Consensus (simulated):** Link the external guide from source notes only; keep one owned installation guide.

Decision: **reference**. Owner: `reference only`. Dependencies: Ponytail installation and host adapter. Overlap: poteto-help, setup-matt-pocock-skills.

## ponytail: ponytail-review

[Pinned source](https://github.com/DietrichGebert/ponytail/blob/96608e078b2d5ea607c5c3b8b5a54d1c1fba6846/skills/ponytail-review/SKILL.md)

Review a changed flow for correctness, safety, realistic load, and unnecessary machinery.

- **Practitioner (simulated):** Requires a concrete failure case and follows callers beyond the diff.
- **Skeptic (simulated):** A clean review ending in Ship can imply more verification than occurred; test presence does not prove test effectiveness.
- **Evaluator (simulated):** Give a green narrow test suite with a reachable missed edge case and a clean diff; produce only reproducible findings and state coverage.
- **Consensus (simulated):** Fold evidence-backed findings and realistic workload assumptions into the existing reviewer.

Decision: **adapt**. Owner: `review`. Dependencies: Repository and comparison point. Overlap: code-review, review-change, pstack:interrogate.

## ponytail: ponytail

[Pinned source](https://github.com/DietrichGebert/ponytail/blob/96608e078b2d5ea607c5c3b8b5a54d1c1fba6846/skills/ponytail/SKILL.md)

Choose a small complete implementation by reusing existing code and platform capabilities.

- **Practitioner (simulated):** The reuse-first ladder challenges unnecessary dependencies and speculative abstractions.
- **Skeptic (simulated):** Broad session-persistent activation can override later intent; minimum line count is a poor proxy for correctness.
- **Evaluator (simulated):** Compare a native date input task and a locale-sensitive custom control; retain required behavior even when it takes more code.
- **Consensus (simulated):** Use a task-scoped approach choice; keep explicit requirements, validation, accessibility, and readable syntax.

Decision: **adapt**. Owner: `minimalist`. Dependencies: no extra runtime requirement. Overlap: minimalist, simplify, code-simplification.

## rstack: before-and-after

[Pinned source](https://github.com/michaelshimeles/rstack/blob/11b15767d7587bab11f6c4957507b5f26d1785c7/before-and-after/SKILL.md)

Capture matched visual states and prepare a comparison for a review.

- **Practitioner (simulated):** Consistent viewport and baseline make visual changes easier to assess.
- **Skeptic (simulated):** Default public image upload and restrictive licensing do not suit every destination or use.
- **Evaluator (simulated):** Use sensitive local screenshots with publication unauthorized; retain local captures and do not use the public default.
- **Consensus (simulated):** Keep as an optional external tool reference; inspect the actual license and authorized image destination first.

Decision: **profile**. Owner: `ui-review`. Dependencies: @vercel/before-and-after, agent-browser, PolyForm Shield terms. Overlap: product-design:audit, ui-review.

## rstack: code-structure

[Pinned source](https://github.com/michaelshimeles/rstack/blob/11b15767d7587bab11f6c4957507b5f26d1785c7/code-structure/SKILL.md)

Separate repeated operations from flow-specific business rules when the project needs that boundary.

- **Practitioner (simulated):** Shared mechanics can prevent fixes being applied to only one flow.
- **Skeptic (simulated):** An actions/services convention can add layers where an established domain architecture already fits; no explicit license for the original.
- **Evaluator (simulated):** Compare two real callers with shared mechanics and different transaction rules; preserve the existing owner of those rules.
- **Consensus (simulated):** Use as a design reference; author the caller-driven procedure independently and retain project architecture.

Decision: **reference**. Owner: `api-design`. Dependencies: Existing repository architecture. Overlap: codebase-design, api-and-interface-design, architect.

## rstack: evidence-driven-testing

[Pinned source](https://github.com/michaelshimeles/rstack/blob/11b15767d7587bab11f6c4957507b5f26d1785c7/evidence-driven-testing/SKILL.md)

Capture a live test session or measured output with assertions tied to the changed revision.

- **Practitioner (simulated):** Separates observed behavior from assertions that a check merely ran.
- **Skeptic (simulated):** Recorder and browser tooling are substantial dependencies, and original skill lacks an explicit license grant.
- **Evaluator (simulated):** Supply synthetic recorder output and a wrong-revision server; neither should count as proof of the changed application.
- **Consensus (simulated):** Reference the evidence discipline; keep owned verification tool-neutral and scale proof to the behavior.

Decision: **reference**. Owner: `verify-change`. Dependencies: Python, ffmpeg/ffprobe for recording, Live app or headless test tooling. Overlap: create-verification-skill, verification-before-completion.

## rstack: greploop-apps

[Pinned source](https://github.com/michaelshimeles/rstack/blob/11b15767d7587bab11f6c4957507b5f26d1785c7/greploop-apps/SKILL.md)

Use Greptile's alternate large-change trigger through the existing review loop.

- **Practitioner (simulated):** Recovers an integration path when the normal trigger refuses the diff size.
- **Skeptic (simulated):** Adds an entrypoint without a new procedure and requires greploop beside it.
- **Evaluator (simulated):** Install this entrypoint alone; it should report the missing sibling rather than inventing a workflow or installing it.
- **Consensus (simulated):** Document as an integration option instead of another default reviewer.

Decision: **reference**. Owner: `review`. Dependencies: greploop, @greptile-apps. Overlap: greploop.

## rstack: greploop

[Pinned source](https://github.com/michaelshimeles/rstack/blob/11b15767d7587bab11f6c4957507b5f26d1785c7/greploop/SKILL.md)

Iterate on fresh Greptile findings for a named revision with a bounded stopping rule.

- **Practitioner (simulated):** Ties findings to current work and stops on timeouts, caps, or unavailable integrations.
- **Skeptic (simulated):** A 5/5 bot score is not functional proof; issue reports describe stale-state edge cases in the helper.
- **Evaluator (simulated):** Queue a new review after an older 5/5 result; fail if old score or no inline threads is accepted as a fresh complete review.
- **Consensus (simulated):** Use only with an explicit Greptile workflow; retain local checks, bounded attempts, and revision freshness.

Decision: **profile**. Owner: `review`. Dependencies: Greptile integration, authenticated gh/glab/p4, Python helper. Overlap: coderabbit-review, pstack:interrogate, review.

## rstack: new-feature

[Pinned source](https://github.com/michaelshimeles/rstack/blob/11b15767d7587bab11f6c4957507b5f26d1785c7/new-feature/SKILL.md)

Create or preserve an isolated task worktree before editing a repository.

- **Practitioner (simulated):** Separates concurrent file changes and checks overlapping PRs.
- **Skeptic (simulated):** Defaults to origin/main and force-deletes merged branches; original skill has no explicit license grant.
- **Evaluator (simulated):** Test an already assigned worktree and a repo whose default branch is not main; preserve both user choices.
- **Consensus (simulated):** Reference isolation principles; use the host's managed worktree tools and actual branch policy, without copying unlicensed instructions.

Decision: **reference**. Owner: `start`. Dependencies: Git, repository host CLI. Overlap: pstack:poteto-mode, using-git-worktrees.

## rstack: unslop

[Pinned source](https://github.com/michaelshimeles/rstack/blob/11b15767d7587bab11f6c4957507b5f26d1785c7/unslop/SKILL.md)

Edit human-facing prose to remove repetitive generated phrasing while preserving meaning.

- **Practitioner (simulated):** Improves readability of reports and documents the agent actually touches.
- **Skeptic (simulated):** Its name can be mistaken for code cleanup, and style recipes can erase a user's voice or technical qualifications.
- **Evaluator (simulated):** Edit a technical paragraph containing a negation and precise units; preserve both and leave unrelated prose untouched.
- **Consensus (simulated):** Keep concise reader-focused writing guidance; do not install an overlapping prose router or confuse it with code simplification.

Decision: **adapt**. Owner: `docs`. Dependencies: no extra runtime requirement. Overlap: pstack:unslop, better-writing.
