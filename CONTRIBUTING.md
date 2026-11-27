# Contributing

Most contributions start as a problem a skill caused in real work. Raw sessions never leave your machine; only sanitized synthetic cases do.

## Report a skill problem

**Right after it happens.** Run `/skill-feedback` (Claude Code) or `$skill-feedback` (Codex) in that session. It collects the skill version, host and model, classifies the problem, writes a synthetic case, checks the draft for private details, and shows you the exact text. Nothing is posted until you approve.

**Once a week.** Run `skill-feedback` and ask for a sweep of the last 7 days. Its script reads your own Codex and Claude Code sessions and reports, per skill, how often it ran on its own or by name, how often you pushed back or interrupted right after, and which installed skills never ran. The agent reads only the flagged uses and a small sample of ordinary ones, drops the false alarms, and drafts one report per real problem. You can schedule the sweep; a scheduled run only prepares drafts.

**Share usage.** The sweep can print a count table for just this pack's skills, with no session pointers. Post it on the monthly usage issue. Counts from several people are how maintainers decide what stays.

**By hand.** Open an issue with the **Skill problem** template and fill in the same fields. Replace project names, paths, code and data with neutral stand-ins.

Where it goes: the feedback repository your project's `AGENTS.md` names, or this repository if it names none. Organizations that keep reports private add one line to their project `AGENTS.md`, for example: `Skill feedback issues go to <org>/<private-repo>.`

## Propose a fix

1. Fork or branch this repository.
2. Add a case to `eval/<skill>/cases.json` that shows the problem.
3. Make the smallest change that fixes it, in the skill that owns the job.
4. Run the validator and tests (see the README).
5. Open a draft PR with: why, what changed, evidence (the case before and after), and what you could not test.

A PR that only rewords a description still needs a selection check, because descriptions decide when a skill loads.

## When a skill earns a place

A skill joins or stays in this pack only if all four hold:

1. **A recurring job.** People ask for it in real sessions, shown by sweeps from more than one person.
2. **Measurably better.** Against no skill, on its own cases, it wins or ties at least 70% of blind-judged pairs, or it passes a check the baseline fails.
3. **Not already covered.** No other skill in the pack, and no built-in host feature, does the job.
4. **Cheap to carry.** It passes the validator, installs alone, and its description earns its place in every session's skill listing.

Something that fails these goes elsewhere: a project convention goes in that project's `AGENTS.md`; a rule a tool can check goes in a script, linter or CI; one person's preference stays a personal skill.

**Retire** a skill that no sweep shows running for 60 days, that loses to no skill, or that a host feature replaced. Retiring is a normal release: note it in `CHANGELOG.md`.

## Maintainer triage

Weekly. A problem becomes a class once it happens twice, or once if it caused harm. Each fix carries its case, reruns selection for the whole pack and behavior for the touched skill, and lands in a tagged release with the evaluation summary in `CHANGELOG.md`. Monthly, add up the shared usage tables and apply the retirement rule.
