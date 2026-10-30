---
name: kp-merge-conflicts
description: Resolve file conflicts in an in-progress Git merge or rebase while preserving both intended changes. Use only when conflict state is present or resolving it is explicitly requested.
---

# Reconcile both intents

Inspect status, operation type, base, and both sides before editing. Preserve existing work and the user's chosen merge/rebase. Read surrounding code and history to understand why each side changed.

Construct the result from both intended behaviors; do not pick an entire side merely to remove markers. For generated artifacts, use the project's regeneration command where available. Investigate lockfile conventions instead of guessing entries.

Check for remaining markers, inspect the reconciled diff, and run relevant behavior checks. Stage only resolved task files. Continue or commit the operation when that is within the user's request and repository policy; otherwise leave the result reviewable and report the precise next step. Aborting remains a valid option when requested or needed to preserve work.
