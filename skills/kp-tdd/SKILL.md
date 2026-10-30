---
name: kp-tdd
description: Build a feature or fix through a failing behavioral test, minimum implementation, and refactoring. Use when test-first work is requested; do not impose TDD on unrelated edits.
---

# Test first

Identify an observable behavior and use the project's existing test tools and public seam. Inspect conventions before adding a fixture or dependency. Ask about a product decision only if it affects the expected result.

Work one behavior at a time: write the smallest meaningful failing test, run it to confirm the intended failure, implement enough to pass, then simplify while keeping it green. A test that fails to import does not yet reproduce the missing behavior.

Prefer realistic inputs and observable outcomes to mocks of internal call order. Include a boundary case when it distinguishes a correct solution from a plausible shortcut. Do not create a complete speculative test suite before implementing the first behavior.

Report the observed red and green results and any checks that could not run. Existing authorization to implement includes routine test execution; do not introduce an approval checkpoint for each test.
