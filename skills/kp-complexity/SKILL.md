---
name: kp-complexity
description: Analyze branching or cyclomatic complexity in named code and identify behavior risks. Use for explicit complexity questions or hard-to-test branch logic, not routine formatting.
---

# Inspect decision paths

Identify the named function or module and its observable contract. Use an existing language-aware analyzer when a numerical metric is requested. State the tool, version, scope, and what its metric counts; do not present a guessed number as measured.

Map consequential branches, interactions, and invalid states. Explain which paths are difficult to reason about or exercise. High branch count is a signal to inspect, not proof of a defect.

Suggest a smaller representation, guard, or boundary only when it reduces reasoning effort without concealing the same decisions in helpers. Preserve the user's requested scope; analysis alone does not authorize refactoring.
