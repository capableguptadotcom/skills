# Our daily pack: simulated discussion and decision

31 October 2026. The corrected goal is a small set of instructions we own and use in ordinary product development. The previous work overemphasized discovering, cataloging and synchronizing other people's skills. The current repository should express our working habits, with upstream material serving as reference rather than an active roadmap.

The previous repository exposed 20 installable skills. Its hundreds of other entries were research records, not hundreds of installed personal skills. That distinction does not rescue the old emphasis: a source registry and growing candidate queue still made the wrong thing central. Installed personal/plugin skills are outside this change and remain untouched.

## Simulated participants

- **Daily engineer:** cares about moving from a request to a useful result without selecting a technique from a large menu.
- **Skill maintainer:** cares about clear responsibility, self-contained installation and keeping conditional detail out of unrelated tasks.
- **Skeptic of extra prompting:** asks whether each instruction changes a decision the model would otherwise get wrong.
- **Evaluator:** asks what observable behavior could disprove a proposed consolidation.

These roles are simulated reasoning aids. They are not quotations from real people, independent evaluators or measured effectiveness results.

## Discussion

**Daily engineer:** Most requests describe an outcome: clarify this idea, build the agreed change, find the failure, review this diff. Separate commands for minimalism, complexity, domain terms and API design make me choose how the agent should think before it has inspected the problem. Put those techniques inside the activity that needs them.

**Maintainer:** Fewer names can conceal an unhelpful mega-skill. Diagnosis, review and delivery must remain separate because their procedures and allowed side effects differ. Keep the selected entrypoint short, link substantial conditional modes from it, and never load all references merely because the skill was selected.

**Skeptic:** A generic instruction such as "write good code" should not earn a skill. Nor should a capability remain just because a famous collection supplies it. Some advice belongs in project conventions, and the host already handles ordinary conversation and trivial edits. A custom start/router skill adds another layer without a clear job once the menu is small.

**Daily engineer:** Keep shaping separate from building. I often want a proposal without product edits, and I do not want implementation of an agreed change to restart the interview. Keep research separate from simulated discussion too: one resolves facts with sources; the other exposes competing judgments.

**Evaluator:** Keep those distinctions only if they survive realistic cases. Test review with a reachable defect and a green but inadequate test. Test delivery with already settled requirements and requested TDD. Test a plan-only request where a technically plausible shortcut would overclaim a guarantee. Verify that only the applicable references are read.

**Maintainer:** TDD deserves careful instructions, but not necessarily another entrypoint. It can be a delivery mode loaded when test-first work is requested. UI assessment can be a review mode, and documentation/conflict resolution can be delivery modes. Handoff remains separate because it preserves continuation state rather than changing the product.

**Skeptic:** Keep cleanup separate only if it preserves the existing contract. Complexity measurement itself is assessment; do not route it to a skill whose primary purpose is editing. Keep simulated discussion because this user explicitly uses it to challenge decisions, not because every team needs a panel.

**Consensus:** Start with eight distinct activities. Preserve focused debugging, review, research, cleanup, handoff and simulated discussion. Introduce shape and develop as the owners of related techniques. Remove the custom router and runtime skill-maintenance command. Use concrete task evidence to revise this composition; eight is not a magic maximum or a demonstrated optimum.

## Disposition of the previous 20

| Previous entrypoint | Decision | New owner |
| --- | --- | --- |
| kp-start | Remove custom router; use the host's skill selection and explicit invocation. | No replacement router |
| kp-change-plan | Combine scoped planning with unresolved design decisions. | kp-shape |
| kp-grill-idea | Keep the interview procedure as a conditional mode. | kp-shape / exploration reference |
| kp-api-design | Keep caller-first interface alternatives as design guidance. | kp-shape / design reference |
| kp-domain-model | Keep scenario-based terminology and invariant checks with design. | kp-shape / design reference |
| kp-prototype | Keep a bounded experiment when it answers a design uncertainty. | kp-shape / design reference |
| kp-debug | Keep a separate hypothesis/reproduction workflow. | kp-debug |
| kp-tdd | Keep requested red/green work as a delivery mode. | kp-develop / testing reference |
| kp-minimalist | Make the smallest complete approach a delivery principle. | kp-develop |
| kp-docs | Keep documentation as a deliverable-specific mode. | kp-develop / documentation reference |
| kp-merge-conflicts | Keep the operation-specific procedure behind an actual conflict request. | kp-develop / conflicts reference |
| kp-verify-change | Integrate revision-aware proof into delivery and verification-only work. | kp-develop / testing reference |
| kp-review | Keep assessment separate from implementation; include conditional UI and code-quality analysis. | kp-review |
| kp-ui-review | Keep rendered evidence and interaction checks as a review mode. | kp-review / UI reference |
| kp-complexity | Keep requested measurement as assessment, not automatic refactoring. | kp-review / complexity reference |
| kp-simplify | Keep contract-preserving code cleanup distinct from feature delivery. | kp-simplify |
| kp-research | Keep primary-source investigation as a separate activity. | kp-research |
| kp-handoff | Keep continuation state separate from product changes. | kp-handoff |
| kp-simulate-discussion | Keep the user's requested way to compare arguments. | kp-simulate-discussion |
| kp-skill-maintenance | Remove from daily product-repository discovery; maintain this collection through its own AGENTS.md. | Repository maintenance instructions |

## What makes these ours

The entrypoints describe the work we ask for, not the organization of upstream collections. Important habits are written in the owning workflow: carry forward agreements and corrections, choose the least machinery that meets the whole requirement, distinguish evidence from a plausible claim, and reconcile the delivered result with the actual goal before calling it complete.

We retain narrow activity boundaries. A review or diagnosis is not permission to edit; a design is not an implicit implementation assignment; a prototype does not become production code merely because it runs. User authorization already given is preserved instead of becoming a new approval ceremony.

There are no hardcoded models, compulsory agent counts, personal service accounts, mandatory cross-skill dependencies or default external publishing steps. Each folder installs independently. Its conditional details live under its own references rather than in another package that may be absent.

## Removal and future additions

The bulk catalog, source locks, upstream proposal scripts and their tests are removed from the current tree. The original audit is preserved at tag `upstream-audit-2026-10-31`, including the source assessments and update history. The recurring source-sync automation is deleted; its draft update proposal is superseded by this goal correction.

A new entrypoint should have a recognizable requested outcome, a useful procedure beyond ordinary model capability, and a reason an existing activity cannot own it without confusing its scope. A conditional technique usually belongs in a reference. A skill can be removed when it duplicates another owner or adds no demonstrated value; deletion is not a failure of the collection.

How regular Codex sessions should inform future changes remains undecided. This pass does not mine sessions, infer success from tool-error counts, install skills or build an automated learning loop. That design comes later, as requested.

## Verification and uncertainty

Package checks validate metadata and local reference closure, including installing each folder without its peers. The forward test uses task fixtures and records activity choices, actual outputs and side effects. An early routing observation moved complexity analysis into review and narrowed delivery metadata; this is an observed design correction, not a routing benchmark.

See [the forward-test record](forward-testing.md) for exact results, instruction versions and limits. Synthetic cases cannot establish that the pack improves daily outcomes across models, long sessions or every project. A later discussion can decide how to collect that evidence without treating every conversation as training data.
