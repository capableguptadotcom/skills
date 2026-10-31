# Language boundaries and ownership

The daily workflows should work for TypeScript, JavaScript and Python. Separate an activity from the tools that perform it. Reproducing a race, reviewing a contract, designing a boundary and preserving continuation state do not require three language-specific entrypoints.

That does not make implementation advice interchangeable. A language-specific reference is useful when the decision actually differs: runtime validation versus static annotations, cancellation semantics, packaging, framework lifecycle, test execution or a supported verifier. Use the project's own conventions and existing tooling first. A new reference should solve an observed gap, rather than duplicate a language manual. A separate skill needs its own recognizable outcome and materially different procedure; symmetry between languages is insufficient reason.

## Pstack's actual assumptions

The inspected canonical pack is not exclusively React guidance. The runtime-verification generator explicitly covers UI, CLI and services in any language; the formal generator explicitly separates event-order modeling from code-level verification in the implementation language. `typescript-best-practices` is deliberately specific. `statechart` is implemented in TypeScript but can model a Python service; its Node/Java/mise/POSIX dependencies are operational requirements, not restrictions on the target service's language. Its current helpers have not been verified on native Windows in this review.

The larger portability problem is host coupling: Cursor paths, model roles, task fields, external control skills, transcript layout and publishing assumptions. The [eight verification/host assessments](research/pstack-verification-and-host.md), [26 other workflows](research/pstack-workflows.md) and [24 principles](research/pstack-principles.md) identify these individually. A Claude adapter exists upstream, but installation compatibility alone is not behavioral compatibility. This review does not diagnose the user's Codex installation or compare its automatic selection with Claude.

Examples of decisions we must keep distinct:

| Common question | Implementation-specific evidence |
| --- | --- |
| Can invalid input enter the domain? | TypeScript types and Python annotations are not by themselves runtime input validation. Inspect the actual parser and mutation boundaries. |
| Is a retry safe? | Check persistent and external effects, transaction boundaries and cancellation points in the actual runtime. |
| Does a model establish the property? | Record its correspondence, atomic steps, bounds and assumptions; do not infer real-code correctness from a handwritten surrogate. |
| Can a verifier run here? | Use available project tools. Property-based tests of the shipped code remain tests; describe their coverage accurately. |

## Upstream copy, owned adaptation and project profile

These are different maintenance relationships. A source citation alone does not choose one.

| Relationship | What we preserve | How a later upstream change should be handled |
| --- | --- | --- |
| **Tracked upstream copy** | Canonical repository, exact source revision and paths, included references/helpers, license and any documented packaging-only changes. | Compare the whole needed package, not just `SKILL.md`. If it remains unmodified, propose a reviewed update and run its relevant checks. A newly added dependency or broader permission does not become acceptable just because the copy was previously trusted. |
| **Owned adaptation** | Upstream ancestor when known, our intended behavior, local differences and evidence for consequential wording. | Upstream is optional learning material. Assess whether a fix addresses the same failure in our version; independently adapt it when useful. Do not apply its text automatically or recreate a one-to-one source mapping. |
| **Project verification profile** | Real project commands, covered behavior/symbols, prerequisites, tool versions, bounds and the revision whose correspondence was checked. | Maintain against project code and contract changes. An upstream recipe improvement may inform it, but cannot renew a stale model's code correspondence. |

An intentional behavioral wording edit to a tracked copy makes it an adaptation. Do not decide ownership by a matching folder name, new prefix or which source moved most recently. Preserve local edits and the old base before considering an update. A clean textual merge does not prove a changed instruction has the intended behavior.

All eight current daily entrypoints are **owned adaptations/own wording**, not tracked upstream copies. There are no tracked copies to auto-update in this proposal. The two verification references added in this pass are owned adaptations of selected ideas, with evidence and limits recorded in the [pstack review](pstack-first-review.md). We retain the applicable notice in [THIRD_PARTY_NOTICES.md](../THIRD_PARTY_NOTICES.md).

This is the maintenance policy for the distinction the user requested, not an implemented updater. Daily synchronization, session mining, automatic rewriting and host configuration remain deferred. The next design should start from concrete usage failures, rather than from every upstream commit or every correction becoming another universal rule.
