# Personal engineering skills

A small, curated Agent Skills pack for product engineering, backed by a versioned upstream inventory and explicit review decisions. The goal is better task completion and verification, not the largest collection of prompts.

Skills live in `skills/<name>/SKILL.md`. The `kp-` prefix avoids identical names when this collection is installed alongside another pack. It reduces name collisions; precise descriptions and host instructions still determine routing.

## Install and use

```sh
npx skills add capableguptadotcom/skills
```

Select the skills and agents you actually want. The shared [skills CLI](https://github.com/vercel-labs/skills) supports Codex, Claude Code, Cursor, and other hosts. Alternatively, copy selected `skills/kp-*` folders into your host's supported skill directory. Use one installation method per agent and avoid keeping a stale copy elsewhere.

In Codex, invoke a selected skill explicitly, for example `$kp-review`, or let the host match its description. Installation does not guarantee automatic selection. Skills alone do not provide browser control, authenticated connectors, or execution permissions. See [host setup and migration](docs/adoption.md).

## The owned pack

| Skill | Use |
| --- | --- |
| [kp-start](skills/kp-start/SKILL.md) | Choose the next useful activity and carry forward settled decisions. |
| [kp-change-plan](skills/kp-change-plan/SKILL.md) | Plan verifiable slices of an agreed change. |
| [kp-grill-idea](skills/kp-grill-idea/SKILL.md) | Challenge an early idea and clarify its smallest useful scope. |
| [kp-debug](skills/kp-debug/SKILL.md) | Reproduce a failure and test competing causes. |
| [kp-tdd](skills/kp-tdd/SKILL.md) | Implement explicitly test-first through observed red and green checks. |
| [kp-review](skills/kp-review/SKILL.md) | Review a bounded change against intent and conventions. |
| [kp-simplify](skills/kp-simplify/SKILL.md) | Make scoped existing code clearer while preserving behavior. |
| [kp-minimalist](skills/kp-minimalist/SKILL.md) | Choose the least machinery that meets the full requirement. |
| [kp-complexity](skills/kp-complexity/SKILL.md) | Connect branch complexity to meaningful paths and tests. |
| [kp-ui-review](skills/kp-ui-review/SKILL.md) | Assess an existing interface using rendered and interaction evidence. |
| [kp-docs](skills/kp-docs/SKILL.md) | Document implemented behavior for a named reader. |
| [kp-research](skills/kp-research/SKILL.md) | Resolve engineering questions using primary sources and versions. |
| [kp-simulate-discussion](skills/kp-simulate-discussion/SKILL.md) | Compare distinct simulated arguments and preserve unresolved tradeoffs. |
| [kp-api-design](skills/kp-api-design/SKILL.md) | Design boundaries from callers and compatibility needs. |
| [kp-domain-model](skills/kp-domain-model/SKILL.md) | Reconcile domain terms, transitions, and invariants. |
| [kp-prototype](skills/kp-prototype/SKILL.md) | Run a disposable experiment for one design uncertainty. |
| [kp-merge-conflicts](skills/kp-merge-conflicts/SKILL.md) | Reconcile both intents in an active merge or rebase. |
| [kp-handoff](skills/kp-handoff/SKILL.md) | Preserve current decisions, evidence, and the next action. |
| [kp-verify-change](skills/kp-verify-change/SKILL.md) | Prove changed behavior at a named revision and report gaps. |
| [kp-skill-maintenance](skills/kp-skill-maintenance/SKILL.md) | Assess source changes before promoting curated wording. |

The router is optional. Simple implementation proceeds directly. Research does not mandate delegation; review does not imply edits; an interface design does not imply implementation. These boundaries preserve the user's requested activity.

## Source inventory and decisions

The initial public inventory contains **815 skill entrypoints across 11 sources**. Generated host mirrors are excluded where a canonical directory is known. The inventory includes explicitly labeled deprecated and fixture entries so contents and exclusions remain visible.

- [Complete one-line catalog](docs/catalog.md): purpose, decision, evidence level, and pinned source link.
- [Inventory summary](docs/inventory-summary.md) and [exact-name collision index](docs/collisions.md).
- [Machine-readable catalog](catalog.json): overlap, dependencies, simulated role arguments, decision, and provenance per entry.
- [Overlap and wording decisions](docs/decisions.md): what belongs in the pack and why.
- Source reviews: [pstack](docs/reviews/pstack.md), [R-stack and Ponytail](docs/reviews/rstack-ponytail.md), [Matt and other individual authors](docs/reviews/community.md), [OpenAI engineering workflows](docs/reviews/openai-engineering.md).
- [Primary evidence and issue discussions](docs/evidence.md): experiments, reported failures, licenses, and confidence limits.
- [Evaluation and promotion](docs/evaluation.md): what establishes a useful skill and what does not.
- [Observed forward smoke tests](docs/forward-testing.md): actual outcomes, preserved scope, and limits.

Source assessments are not proof of improvement. Some long community entrypoints were assessed through procedure/constraint excerpts; most vendor/domain-specific OpenAI entries receive description-level inventory and provisional optional/deferred decisions. The evidence level and inspection depth are recorded. Simulated discussions are written arguments, not independent experiments.

Private organization content and raw chat history are excluded from this public repository. The same standard skill-folder format is retained, with independently written instructions. Licenses are documented in [third-party notices](THIRD_PARTY_NOTICES.md); a public GitHub repository alone is not a reuse grant.

## Maintain

Python 3.12+, Git, and authenticated GitHub CLI are used for curation. Ordinary skill use does not need this Python tooling.

```sh
python -m pip install -r requirements.txt
python scripts/upstreams.py --refresh --write
python scripts/validate.py
python -m unittest discover -s tests -v
python scripts/propose_update.py --publish
```

The last command does the fetch and validation itself in an isolated temporary worktree, then creates or updates a draft candidate PR. Without `--publish`, it previews the diff and cleans up. It never edits `skills/`, changes reviewed decisions, or stages the user's checkout.

The daily Codex automation performs this reconciliation and review; its operational details are in [maintenance](docs/maintenance.md). Source changes enter review proposals automatically. Curated behavior changes need evidence before promotion.

Add another source to `sources.json` with its canonical skill roots, branch, tracked scope, and license note. Track shared references, scripts, licenses and adapter files as well as entrypoints. `upstream.lock.json` is the last observed snapshot; `reviews.json` preserves what was assessed. Changed tracked source files conservatively invalidate that source's old review status. This can over-report unrelated changes, but prevents shared dependencies from silently retaining approval.

License: MIT for the owned code and instructions; upstream materials retain their own terms.
