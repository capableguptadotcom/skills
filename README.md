# Our daily development skills

Eight owned workflows for the work we actually do: decide what to build, deliver it, diagnose failures, review changes, investigate facts, simplify code, and carry context forward. This repository is the source of truth for our instructions.

| Skill | Result it should produce |
| --- | --- |
| [kp-shape](skills/kp-shape/SKILL.md) | A clear problem, scoped design and proportionate plan, without reopening settled decisions. |
| [kp-develop](skills/kp-develop/SKILL.md) | The requested change with evidence that its relevant behavior works. |
| [kp-debug](skills/kp-debug/SKILL.md) | A cause supported by a reproduction and discriminating checks. |
| [kp-review](skills/kp-review/SKILL.md) | Actionable findings against intent and conventions, with coverage limits. |
| [kp-research](skills/kp-research/SKILL.md) | A source-backed answer to an engineering question. |
| [kp-simplify](skills/kp-simplify/SKILL.md) | Clearer scoped code with its behavior preserved. |
| [kp-handoff](skills/kp-handoff/SKILL.md) | Enough current state for the next session to continue accurately. |
| [kp-simulate-discussion](skills/kp-simulate-discussion/SKILL.md) | Distinct arguments, unresolved tradeoffs and a reasoned recommendation. |

The names identify different activities, not mandatory stages. A typo does not need a planning ceremony. A request to implement an agreed change does not restart discovery. Review-only and diagnosis-only work stay within those boundaries.

TDD, API/domain design, prototyping, UI assessment, documentation and conflict resolution remain available as guidance within these workflows. They no longer compete as separate installed skills. Each skill is self-contained; conditional references live inside its folder and are read only when needed.

## Use

```sh
npx skills add capableguptadotcom/skills
```

Select the workflows and agents you want. In Codex, explicit invocation looks like `$kp-review`; natural-language selection depends on the host. No always-on custom router is required. Use one installation method per host and retain the `kp-` names to distinguish these instructions from other collections.

The shared [skills CLI](https://github.com/vercel-labs/skills) currently requires Node.js 22.20+. Manual installation of a selected folder is also possible. This repository change does not replace or remove skills already installed on a machine. Tools, credentials and host execution permissions remain supplied by that environment.

## Why these eight

[The simulated discussion and disposition table](docs/daily-pack-decision.md) explain what stayed, what was combined, and what was removed from the previous 20-skill pack. Eight is a starting composition, not an empirically optimal number. A skill earns its place by improving a recognizable task or preventing a demonstrated failure beyond the host's existing instructions.

Upstream collections informed the initial research; they do not define our roadmap or update our wording automatically. The old catalog and synchronization machinery are preserved in the [historical audit tag](https://github.com/capableguptadotcom/skills/tree/upstream-audit-2026-10-31), outside the current working tree. See [provenance](docs/provenance.md) and [third-party notices](THIRD_PARTY_NOTICES.md).

## Maintain our instructions

Start from a concrete need in our work. Change the workflow that owns it, keep the instructions short, and check both the intended behavior and a neighboring request that should behave differently. Do not add a new skill for generic advice or because an upstream repository added one.

```sh
python -m pip install -r requirements.txt
python scripts/validate.py
python -m unittest discover -s tests -v
```

These checks validate the package and its local references. Behavioral smoke tests and their limits are recorded under `eval/`; they do not prove improvement across all tasks or models.

The daily upstream-sync automation has been removed. How we learn from regular Codex sessions is a separate discussion for later; no session mining, telemetry collection or automatic skill rewriting is configured here.

License: MIT for the owned instructions and tooling, with retained third-party notices.
