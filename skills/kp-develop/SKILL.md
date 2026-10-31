---
name: kp-develop
description: Implement or verify an agreed software change, including test-first work, documentation edits and active Git conflicts. Use for delivery, not a plan or assessment by itself.
---

# Deliver the requested change

Recover the intended outcome, latest steering and already settled decisions. Inspect the affected flow and repository instructions. Continue agreed work directly; resolve only consequential missing choices. A small edit needs a small check, not a mandatory lifecycle.

Choose the least new machinery that meets the full requirement. Look for existing code, project conventions, platform features and installed dependencies before introducing another layer. Keep validation, error behavior, accessibility, caller compatibility and transaction ownership intact.

Use the relevant detail only when needed:

- For test-first work, behavioral regression, runtime/UI proof or performance evidence, read [testing and verification](references/testing.md).
- For documentation as the requested deliverable, read [documentation](references/documentation.md).
- For an active merge/rebase conflict, read [conflicts](references/conflicts.md).

Implement in verifiable increments when the work is large. After each meaningful increment, inspect the result before extending it. Keep a compact record of current decisions and the next unresolved step if the task spans a long session; reuse established artifacts instead of creating a tracking framework.

Verify the requested behavior at the actual revision and report what passed, failed or could not be checked. A verification-only request does not authorize product edits. Before calling the task complete, reconcile the original goal and latest corrections with the delivered behavior. State material gaps; do not replace unfinished work with a confident summary. Commits, publication and deployment follow the task's existing authorization, not the fact that implementation finished.
