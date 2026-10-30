---
name: kp-simplify
description: Simplify scoped existing code while preserving behavior, contracts, and project conventions. Use for requested cleanup or a demonstrated clarity problem in changed code.
---

# Simplify within the boundary

Agree on the code boundary from the request and current change. Read its callers and existing checks. Identify the contract before changing its expression.

Remove unnecessary branches, duplication, or indirection only when doing so improves understanding. Keep validation, error behavior, transaction ownership, accessibility, and compatibility. A single caller alone does not prove an interface is unnecessary.

Prefer the existing project idiom. Do not turn a local cleanup into an architecture migration or delete pre-existing unrelated dead code. Remove imports and helpers made unused by your own edits.

Run the checks that can detect changed behavior and inspect the diff for unrelated changes. Explain what became clearer and any behavior you could not verify. Fewer lines is an observation, not the success criterion.
