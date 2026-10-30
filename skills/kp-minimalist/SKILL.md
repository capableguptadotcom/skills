---
name: kp-minimalist
description: Choose the smallest complete approach when a proposed implementation risks unnecessary features, dependencies, or abstraction. Use before implementation; use kp-simplify for cleanup of existing code.
---

# Choose less machinery

Name the actual behavior and constraints. Inspect existing components, utilities, platform features, and installed dependencies that could already satisfy them. Prefer the first approach that meets the full requirement and fits the project's conventions.

Do not silently reduce the user's scope. If the smaller option drops a requested behavior, make that tradeoff explicit and retain the request until the user changes it.

Add an abstraction or dependency only for a present benefit that outweighs its operational cost. Preserve security, data integrity, error handling, and accessibility. Readability beats compressed syntax.

State the proposed approach, why the alternatives add unnecessary machinery, and the check that establishes completeness. This is a task-specific decision, not a persistent personality or a license to challenge every later request.
