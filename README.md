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
| [skill-feedback](skills/skill-feedback/SKILL.md) | by name, maintainers only | Sanitized local drafts about a skill problem; posts only where you name |

"Automatically" means the host picks the skill from its description; no router or instruction file is needed. Explicit skills run with `/name` in Claude Code and `$name` or the `/skills` picker in Codex. They set `disable-model-invocation: true` for Claude Code and `policy.allow_implicit_invocation: false` in `agents/openai.yaml` for Codex.

## Install for a team

In each product repository, at its root, install a release of the daily skills and commit the result. Teammates then get the skills with `git pull`, with nothing to install themselves:

```sh
npx skills add https://github.com/capableguptadotcom/skills/tree/<release> --copy --agent claude-code codex \
  --skill shape-change develop diagnose review-change research simplify-code handoff simulate-discussion
```

The [skills CLI](https://github.com/vercel-labs/skills) does three things:

- It writes `.claude/skills/` for Claude Code and `.agents/skills/` for Codex.
- It records the source, the ref and a content hash in `skills-lock.json`.
- Use `--copy`, because symlinks break on Windows checkouts.

Two things that look right do not work:

- `capableguptadotcom/skills@<release>`: the CLI reads the part after `@` as a skill name, not a version.
- A release name with a slash (such as `release/1.0`): the CLI cannot clone it.

Use tags such as `v1.0.0`.

**Updating.** `npx skills update -p -y` fetches the same ref the lock records again. So with a tag it changes nothing. To move to a new release, rerun the install command with the new tag, then commit the changed skill folders and `skills-lock.json` in a PR.

`skill-feedback` is left out on purpose. It is the maintainers' tool for improving the pack from their own sessions, and team members' sessions are their own work.

Use one source per skill: do not install the same skill both globally and per project. If someone already has a personal skill for the same job (a personal `code-review` or `grill-me`, say), remove it, so the host does not have to choose between two.

## Use

- **Just ask for the work.** "Why does this test fail?", "review my branch", "plan this before I build it", "tidy this function". The host picks the matching skill from its description. You can also name one: `/diagnose` in Claude Code, `$diagnose` in Codex.
- **`handoff` and `simulate-discussion` run only by name.** `handoff` writes a note for the next session. `simulate-discussion` lays out opposing views on a decision.
- **What to expect.**
  - Diagnosis and review show their evidence (what was run, what was ruled out, what was not covered) and edit nothing unless you ask for a fix.
  - `simplify-code` keeps behavior exactly and stays inside the code you point at.
  - `shape-change` asks one question at a time in an interview and writes the plan when you ask for it.

## Report a problem

If you use the pack, tell the maintainers what you asked, what the skill did and what should have happened, without project names, code or data. Do not open issues or pull requests here.

Maintainers install `skill-feedback` for themselves only, globally (`npx skills add https://github.com/capableguptadotcom/skills/tree/<release> -g --copy --agent claude-code codex --skill skill-feedback`), and run it by name. It writes sanitized local drafts, and posts or opens a draft PR only when you name the repository in that session. It never runs on its own or on a schedule. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Maintain

```sh
python -m pip install -r requirements.txt
python scripts/validate.py
python -m unittest discover -s tests -v
git diff --check
```

The validator enforces the rules every skill must meet: name format and reserved names, description length, body length, matching invocation settings for both hosts, no references outside the skill folder, Python-only scripts with no network access, no package or tool-server files, and no personal paths. The tests run each bundled script on synthetic input.

A change ships when it beats a no-skill baseline on its evaluation cases in both hosts. The current results, and what they can and cannot show, are in [docs/open-decisions.md](docs/open-decisions.md). Evaluation lives in `eval/`; earlier smoke tests are recorded in [docs/forward-testing.md](docs/forward-testing.md) under the skills' former `kp-` names. Not yet shipped: `verification-skill` (drafts in [drafts/verification-skill](drafts/verification-skill/)) and `open-pr`.

Upstream collections are reference material only. The earlier upstream audit is preserved at tag `upstream-audit-2026-10-31`. See [provenance](docs/provenance.md) and [third-party notices](THIRD_PARTY_NOTICES.md).

License: MIT.
