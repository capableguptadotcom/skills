# shape-change: specification

**Job.** Turn an unsettled idea or design question into decisions and a plan someone can assess, before code is written.

**Output.** Depending on the request: an interview turn (settled points, the next question with a recommended answer), a recommendation with its reasons, or a plan in verifiable slices. Confirmed decisions and open questions kept apart.

**Must.**

- Look up what the repository answers before asking; ask only what the user alone can decide.
- Surface the risks the code reveals, not generic checklists.
- Recommend, with reasons, when asked to choose.
- Carry settled decisions forward without reopening them.
- Leave every file unchanged.

**Must not.**

- Write production code or edit files during planning or an interview.
- Ask the user a fact the code answers.
- Reopen a decision the user says is agreed.

**Hosts.** Claude Code and Codex. Each run is one turn (`claude -p`), so an interview is judged on its first turn.

**Triggers.** "grill me on this plan", "should we use X or Y", "give me a plan before I build this".
**Near misses.** Building an agreed change; reviewing a diff; fixing a bug.

**Cases.** See `cases.json`, on `eval/fixtures/notify-service`. The repository facts that matter: `Customer` has no phone field; a failing job is retried as a whole; production runs four worker processes; the service owns a Postgres schema.

- `grill-sms-plan`: "grill me" on adding SMS next to the email in `notify()`. A good first turn finds that there is no phone number to send to and that a whole-job retry would resend the email when SMS fails, and asks only what the user must decide.
- `dedupe-design`: in-memory set or database table for deduplicating retried emails. Four processes and restarts rule out the in-memory set; a mailer timeout means exactly-once is not available.
- `agreed-plan`: one job per channel is agreed; write the plan. Jobs already queued in the old shape must keep working during the deploy. No interview, no edits.
