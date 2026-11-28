---
name: simplify-code
description: Use when asked to clean up, simplify, tidy or make existing code clearer without changing what it does. Scoped to the named code or the current change. Not for new features, bug fixes or design before coding.
---

# Simplify within the boundary

This skill does one thing: it makes scoped existing code easier to read while its behavior stays the same.

1. **Agree on the boundary** from the request and the current change. Check: you can list the files and functions in scope.
2. **Find the contract.** Read the callers and the existing checks before changing how the code is written.
3. **Remove only what makes the code harder to understand:** unneeded branches, duplication, indirection. Keep validation, error behavior, transaction ownership, accessibility and compatibility. A single caller alone does not prove an interface is unnecessary.
4. **Prefer the project's existing idiom.** Do not turn a cleanup into an architecture change. Do not delete unrelated dead code you did not create; mention it instead. Remove imports and helpers your own edits made unused.
5. **Verify.** Run the checks that would detect changed behavior, and read the diff for unrelated changes.
6. **Report** what became clearer and any behavior you could not verify. Fewer lines is an observation, not the goal.
