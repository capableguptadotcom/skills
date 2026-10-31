---
name: kp-review
description: Assess a code change, named code area or existing product interface. Use for actionable findings, code-quality analysis or UI critique; do not edit unless fixes are also requested.
---

# Review the change

For rendered UI or product-interaction assessment, read [UI review](references/ui.md). For requested complexity measurement, read [complexity](references/complexity.md). Otherwise use the code procedure below; do not impose unrelated modes on a routine diff.

Bound the assessment to the named change or area. For a change, establish the revision and comparison point, then read the diff and originating requirements. For a named area, inspect its contract. Read relevant instructions, callers and tests that establish the affected behavior.

Assess two questions separately: does it implement the agreed behavior, and can the changed paths fail or violate established conventions? A passing check and a review bot's score are evidence with limited coverage.

Retain a finding only when you can explain a reachable trigger, the wrong outcome, and an affected location. Label an unverified concern as uncertain; omit speculative issues and tooling-enforced style preferences. Give priority based on impact, not how easy the change is to suggest.

Return actionable findings, supporting evidence, and material coverage gaps. No findings is a valid result and does not establish universal correctness. Preserve the reviewed files; a review request alone does not authorize fixes, comments to others, or merge.
