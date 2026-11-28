# Development skills

Agent skills for everyday product engineering. They work the same in Claude Code and Codex.

| Skill | Runs | What you get |
| --- | --- | --- |
| [shape-change](skills/shape-change/SKILL.md) | automatically | Decisions and a plan in small, checkable steps, before any code |
| [develop](skills/develop/SKILL.md) | automatically | The agreed change, with evidence that it works |
| [diagnose](skills/diagnose/SKILL.md) | automatically | The cause of a bug, backed by a reproduction |
| [review-change](skills/review-change/SKILL.md) | automatically | Findings with evidence, no edits |
| [research](skills/research/SKILL.md) | automatically | A cited answer from primary sources |
| [simplify-code](skills/simplify-code/SKILL.md) | automatically | Clearer code with the same behavior |
| [handoff](skills/handoff/SKILL.md) | by name | A note for the next session |
| [simulate-discussion](skills/simulate-discussion/SKILL.md) | by name | Opposing views on a decision, and what would settle it |

"Automatically" means you just ask ("why does this test fail?", "review my branch") and the agent picks the skill. To run one by name, type `/diagnose` in Claude Code or `$diagnose` in Codex.

## Install

In your project's root folder:

```sh
npx skills add capableguptadotcom/skills --copy --agent claude-code codex -y
```

Commit the new `.claude/skills/`, `.agents/skills/` and `skills-lock.json`. Teammates get the skills with `git pull`.

Why the flags:

- **`--copy`.** Without it, the skills are stored as links to a path on your own machine, and those links are broken for everyone else.
- **`--agent claude-code codex`.** This installs for these two tools only. Otherwise the CLI adds folders for every other agent it finds on your computer.

To install for yourself across all projects, add `-g` and skip the commit.

## Update

Run the same command again, then commit the changes in a PR:

```sh
npx skills add capableguptadotcom/skills --copy --agent claude-code codex -y
```

Don't use `npx skills update`: it turns the copies back into links. `skills-lock.json` records where each skill came from and a hash of its files, so the PR shows exactly which skills changed.

Nothing updates on its own. A project stays on what it last installed until someone runs the command.

If you have a personal skill that does the same job (your own `code-review` or `grill-me`, say), remove it, so the agent doesn't have to choose between two.

## Report a problem

Tell the maintainers what you asked, what the skill did and what should have happened. Leave out project names, code and data. Please don't open issues or pull requests here.

## Maintain

Maintainers also install `skill-feedback`, which turns problems from their own sessions into reports and draft PRs. It is hidden from the install above:

```sh
INSTALL_INTERNAL_SKILLS=1 npx skills add capableguptadotcom/skills -g --copy --agent claude-code codex --skill skill-feedback -y
```

In PowerShell, run `$env:INSTALL_INTERNAL_SKILLS=1` first, then the command without that prefix. It runs only by name or on a schedule you set up. It posts only to a repository you name and can push to. See [CONTRIBUTING.md](CONTRIBUTING.md).

Before publishing a change:

```sh
python -m pip install -r requirements.txt
python scripts/validate.py
python -m unittest discover -s tests -v
git diff --check
```

Evaluation results are in [docs/open-decisions.md](docs/open-decisions.md), with cases in `eval/`. Sources and licenses: [provenance](docs/provenance.md), [third-party notices](THIRD_PARTY_NOTICES.md). License: MIT.
