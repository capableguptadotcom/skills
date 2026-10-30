---
name: kp-verify-change
description: Establish observable evidence that a changed behavior works at a named revision. Use when runtime verification or before/after proof is needed; scale checks to the change.
---

# Verify the claim

Name the behavior, revision, environment, preconditions, and expected result. Verify that the running process or deployment serves that revision. Reuse valid evidence from the task rather than recreating it for presentation.

Choose proof that can distinguish success from a plausible incorrect result: a failing/passing reproduction for a fix, assertions on a real user flow for UI, output comparisons for CLI/API behavior, and matched workloads for performance. Static screenshots cannot prove an interaction occurred. Synthetic recorder input cannot prove the application worked.

Run the behavior and inspect the output. Mark each target passed, failed, or untested with a reason. A process exit code or video file existing alone does not establish the claimed behavior. Relevant automated checks complement the observed flow.

Keep captures local unless publication to a particular destination is already authorized. Do not upload private data to a default public image host. Report evidence, limitations, and what failed; a review score is never a substitute for functional proof.
