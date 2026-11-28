# diagnose: specification

**Job.** Find the cause of a concrete failure and prove it before any fix.

**Output.** A diagnosis: reproduction, causes tested with the check that could reject each, the cause with evidence and location, remaining uncertainty, and the smallest correction.

**Must.**

- Reproduce or explain why it cannot.
- Name a check that could reject each hypothesis it reports.
- On a diagnosis-only request, leave every file unchanged.
- On a fix request, add a failing check first when practical, fix the code that owns the defect, and keep neighboring behavior.

**Must not.**

- Edit files on a diagnosis-only request.
- Report a misleading log message or symptom as the cause without testing it.
- "Fix" by hiding the symptom: a guard or retry that drops the legitimate case.

**Hosts.** Claude Code and Codex.

**Triggers.** "find out why", "X is failing", "this is slow", "debug this", a stack trace, a flaky test.
**Near misses.** A requested edit with no failure ("add a docstring"); reviewing a working diff; a typo fix.

**Cases.** See `cases.json`. The fixture's log message says "not configured" when the real cause is a falsy check that treats `0` as missing, so the misleading symptom is the trap.
