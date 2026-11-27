# Contributing

Most contributions start as a problem a skill caused in real work.

## Report a skill problem

**With the skill.** Run `/skill-feedback` (Claude Code) or `$skill-feedback` (Codex) in the session where it happened. It collects the skill version, host and model, classifies the problem, writes a synthetic case, checks the draft for private details, and shows you the exact text. Nothing is posted until you approve.

**By hand.** Open an issue with the **Skill problem** template and fill in the same fields. Replace project names, paths, code and data with neutral stand-ins.

Where it goes: the feedback repository your project's `AGENTS.md` names, or this repository if it names none. Organizations that keep reports private add one line to their project `AGENTS.md`, for example: `Skill feedback issues go to <org>/<private-repo>.`

## Propose a fix

1. Fork or branch this repository.
2. Add a case to `eval/<skill>/cases.json` that shows the problem.
3. Make the smallest change that fixes it, in the skill that owns the job.
4. Run the validator and tests (see the README).
5. Open a draft PR with: why, what changed, evidence (the case before and after), and what you could not test.

A PR that only rewords a description still needs a selection check, because descriptions decide when a skill loads.

## Maintainer triage

Weekly. A problem becomes a class once it happens twice, or once if it caused harm. Each fix carries its case, reruns selection for the whole pack and behavior for the touched skill, and lands in a tagged release with the evaluation summary in `CHANGELOG.md`.
