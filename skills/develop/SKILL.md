---
name: develop
description: Use when implementing an agreed change - building a feature, fixing a known bug, writing tests first, documenting implemented behavior, or resolving an active merge or rebase conflict. Delivers the change with evidence it works. Not for a plan, review or diagnosis on its own.
---

# Deliver the requested change

This skill does one thing: it delivers an agreed change and shows that the changed behavior works. A small edit needs a small check, not a lifecycle.

1. **Recover the agreement.** Find the intended outcome, the latest steering and the decisions already settled. Inspect the affected flow and the repository's instructions. Continue agreed work directly; ask only about a missing choice that changes the result.
2. **Choose the least new machinery.** Look for existing code, project conventions, platform features and installed dependencies before adding a layer. Keep validation, error behavior, accessibility, caller compatibility and transaction ownership intact.
3. **Read the detail the task needs, and only that:**
   - Test-first work, a regression test, UI or runtime proof, or performance evidence: [testing and verification](references/testing.md).
   - Documentation as the deliverable: [documentation](references/documentation.md).
   - An active merge or rebase conflict: [conflicts](references/conflicts.md).
4. **Build in verifiable increments** when the work is large. Inspect each increment before extending it. In a long session, keep a short record of decisions and the next step instead of a tracking framework.
5. **Verify at the actual revision.** Run the checks that could tell success from a plausible wrong result. Report each target as passed, failed or not checked, with the reason.
6. **Reconcile before calling it done.** Compare the delivered behavior with the original goal and every later correction. State material gaps plainly.

## Boundaries

- A verification-only request does not authorize product edits.
- Commits, pushes, publication and deployment follow the task's existing authorization, not the fact that the code is finished.
