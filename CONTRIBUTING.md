# Contributing

Most contributions start as a problem a skill caused in real work. Raw sessions never leave your machine; only sanitized synthetic cases do.

## Report a skill problem

**If you use the pack.** Your sessions are your own work, and nothing about them needs to reach this repository. When a skill gets something wrong, tell the maintainers the way your team already shares feedback: what you asked, what the skill did, and what should have happened. Leave out project names, code and data. You do not install `skill-feedback`, and you do not open issues or pull requests here.

**If you maintain the pack.** `skill-feedback` is the maintainers' tool, and it runs only when invoked by name: `/skill-feedback` in Claude Code, `$skill-feedback` in Codex.

- **Right after a problem.** Run it in that session. It collects the skill version, host and model, classifies the problem, writes a synthetic case and checks the draft for private details.
- **Over a stretch of work.** Ask it for a sweep of the last 7 days of your own sessions. The script reports, per skill, how often it ran on its own or by name, how often you pushed back or interrupted right after, and which installed skills never ran. The agent reads only the flagged uses and a small sample of ordinary ones, drops the false alarms, and drafts one report per real problem.

In both cases the result is local drafts. It posts an issue or opens a draft pull request only when you name the repository in that session and approve the text. It never runs on a schedule and never picks a destination itself.

**By hand.** Maintainers can also open an issue with the **Skill problem** template. Replace project names, paths, code and data with neutral stand-ins.

## Propose a fix (maintainers)

1. Branch this repository.
2. Add a case to `eval/<skill>/cases.json` that shows the problem.
3. Make the smallest change that fixes it, in the skill that owns the job.
4. Run the validator and tests (see the README).
5. Open a draft PR with: why, what changed, evidence (the case before and after), and what you could not test.

A PR that only rewords a description still needs a selection check, because descriptions decide when a skill loads.

## When a skill earns a place

A skill joins or stays in this pack only if all four hold:

1. **A recurring job.** People ask for it in real sessions, shown by maintainers' sweeps and by reports from more than one person.
2. **Measurably better.** Against no skill, on its own cases, it wins or ties at least 70% of blind-judged pairs on the suite's rubric, or it passes a check the baseline fails. Report the 95% interval and the outcome-only re-judge (`judge --outcome-only`) beside it. A win that holds only on the suite rubric is a gain in the report, not in the work; say so, and add a case the baseline fails before claiming more.
3. **Not already covered.** No other skill in the pack, and no built-in host feature, does the job.
4. **Cheap to carry.** It passes the validator, installs alone, and its description earns its place in every session's skill listing.

Something that fails these goes elsewhere: a project convention goes in that project's `AGENTS.md`; a rule a tool can check goes in a script, linter or CI; one person's preference stays a personal skill.

**Retire** a skill that no sweep shows running for 60 days, that loses to no skill, or that a host feature replaced. Retiring is a normal release: note it in `CHANGELOG.md`.

## Maintainer triage

Weekly. A problem becomes a class once it happens twice, or once if it caused harm. Each fix carries its case, reruns selection for the whole pack and behavior for the touched skill, and lands in a tagged release with the evaluation summary in `CHANGELOG.md`. Monthly, add up the maintainers' sweeps and the team's reports, and apply the retirement rule.
