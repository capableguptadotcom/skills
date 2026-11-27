---
name: handoff
description: Write a continuation note so another session or person can pick up the work - objective, decisions, evidence, current state and next action. Invoke by name.
disable-model-invocation: true
---

# Write a handoff note

This skill does one thing: it records enough current state for the next session to continue without rediscovering it.

1. **Collect the repository state.** In a Git repository, run this skill's `scripts/handoff_state.py` from the repository root. It prints the branch, upstream, commit, uncommitted and untracked files, recent commits and stashes. Paste its output into the note rather than retyping it.
2. **Recover the intent** from the conversation: the objective, the latest steering, the scope and the decisions with their reasons.
3. **Separate what is done from what is planned or assumed.** Record checks that ran with their actual results, and checks that did not run.
4. **Link, don't copy.** Point to files, commits, PRs and logs instead of pasting transcripts. Keep a failure only if it affects the next step.
5. **Fill [the handoff template](assets/handoff.md)** and save it where the user asked, or show it in the reply.
6. **Check before saving:** no credentials or private content the next step does not need; the next action can be started without asking a question.

Writing a note does not authorize messaging anyone, committing, archiving or changing the session.
