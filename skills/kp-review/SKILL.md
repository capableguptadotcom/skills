---
name: kp-review
description: Assess a requested PR, branch, commit, or diff against intended behavior and repository conventions. Report evidence-backed findings without editing unless fixes are also requested.
---

# Review the change

Establish the target revision and comparison point. Read the diff, relevant instructions, originating requirements, changed callers, and the tests that establish the affected behavior. Bound the review to the requested change and consequential connected code.

Assess two questions separately: does it implement the agreed behavior, and can the changed paths fail or violate established conventions? A passing check and a review bot's score are evidence with limited coverage.

Retain a finding only when you can explain a reachable trigger, the wrong outcome, and an affected location. Label an unverified concern as uncertain; omit speculative issues and tooling-enforced style preferences. Give priority based on impact, not how easy the change is to suggest.

Return actionable findings, supporting evidence, and material coverage gaps. No findings is a valid result and does not establish universal correctness. Preserve the reviewed files; a review request alone does not authorize fixes, comments to others, or merge.
