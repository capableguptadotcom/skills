---
name: review-change
description: Use when asked to review a PR, branch, commit, diff, named code area or existing UI. Returns evidence-backed findings and coverage gaps. Edits nothing unless fixes are also requested.
---

# Review the change

This skill does one thing: it reports what is wrong with a bounded change, with evidence. A review request does not authorize fixes, comments to others or a merge.

1. **Bound the review.** Establish the target revision and the comparison point. In a Git repository, run this skill's `scripts/diff_context.py` from the repository root, optionally passing a base ref. It prints the base, the changed files and the tests that mention them. Check: you can name exactly which changes are in scope.
2. **Pick the mode.**
   - Rendered UI or product interaction: read [UI review](references/ui.md).
   - A requested complexity measurement: read [complexity](references/complexity.md).
   - Otherwise: the code review below. Do not add unrelated modes to a routine diff.
3. **Read what defines correct.** The diff, the originating requirement, the repository's instructions, the changed callers and the tests that establish the affected behavior.
4. **Ask two questions separately.** Does the change implement the agreed behavior? Can the changed paths fail or break an established convention? A passing check or a review bot's score is evidence with limited coverage.
5. **Keep only findings you can support.** Each needs a reachable trigger, the wrong outcome and a location. Mark an unverified concern as uncertain. Drop speculation and style that a tool already enforces. Rank by impact, not by how easy the fix is.
6. **Report** with [the findings template](assets/findings.md), including what you could not cover. No findings is a valid result; it does not prove the change correct.

Preserve the reviewed files.
