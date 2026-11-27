# Development skills

A small set of agent skills for everyday product engineering, written to work the same in Codex and Claude Code. Each skill does one job, carries its own templates and scripts, and must beat working without it before it ships.

| Skill | Invoked | Produces |
| --- | --- | --- |
| [shape-change](skills/shape-change/SKILL.md) | automatically | Decisions and a plan in verifiable slices, before any code |
| [develop](skills/develop/SKILL.md) | automatically | The agreed change, with evidence that it works |
| [diagnose](skills/diagnose/SKILL.md) | automatically | A cause backed by a reproduction and checks that reject the alternatives |
| [review-change](skills/review-change/SKILL.md) | automatically | Evidence-backed findings and coverage gaps, no edits |
| [research](skills/research/SKILL.md) | automatically | A cited answer from primary sources |
| [simplify-code](skills/simplify-code/SKILL.md) | automatically | Clearer scoped code with behavior unchanged |
| [handoff](skills/handoff/SKILL.md) | by name | A continuation note for the next session |
| [simulate-discussion](skills/simulate-discussion/SKILL.md) | by name | Distinct simulated viewpoints and the evidence that would settle them |
| [skill-feedback](skills/skill-feedback/SKILL.md) | by name | A sanitized issue or draft PR about a skill problem, posted only after approval |

"Automatically" means the host picks the skill from its description; no router or instruction file is needed. Explicit skills run with `/name` in Claude Code and `$name` or the `/skills` picker in Codex. They set `disable-model-invocation: true` for Claude Code and `policy.allow_implicit_invocation: false` in `agents/openai.yaml` for Codex.

## Install

In each product repository, install a pinned release and commit the result so everyone gets the same version:

```sh
npx skills add capableguptadotcom/skills@<tag> --copy
```

Select Codex and Claude Code. The [skills CLI](https://github.com/vercel-labs/skills) writes `.agents/skills/` for Codex and `.claude/skills/` for Claude Code, and records the version in `skills-lock.json`. Use `--copy` because symlinks break on Windows checkouts. Update with `npx skills check` and `npx skills update`, then commit the change in a PR.

Use one source per skill: do not install the same skill both globally and per project.

## Report a problem

Run `/skill-feedback` (Claude Code) or `$skill-feedback` (Codex) in the session where a skill went wrong. It drafts a sanitized issue or a draft PR with a synthetic test case, shows you the exact text, and posts only after you approve. Without the skill, open an issue with the **Skill problem** template. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Maintain

```sh
python -m pip install -r requirements.txt
python scripts/validate.py
python -m unittest discover -s tests -v
git diff --check
```

The validator enforces the rules every skill must meet: name format and reserved names, description length, body length, matching invocation settings for both hosts, no references outside the skill folder, Python-only scripts with no network access, no package or tool-server files, and no personal paths. The tests run each bundled script on synthetic input.

A change ships when it beats a no-skill baseline on its evaluation cases in both hosts. Evaluation lives in `eval/`; earlier smoke tests are recorded in [docs/forward-testing.md](docs/forward-testing.md) under the skills' former `kp-` names. Not yet shipped: `verification-skill` (drafts in [drafts/verification-skill](drafts/verification-skill/)) and `open-pr`.

Upstream collections are reference material only. The earlier upstream audit is preserved at tag `upstream-audit-2026-10-31`. See [provenance](docs/provenance.md) and [third-party notices](THIRD_PARTY_NOTICES.md).

License: MIT.
