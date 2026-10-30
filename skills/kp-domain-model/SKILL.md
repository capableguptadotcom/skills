---
name: kp-domain-model
description: Clarify product domain terminology, state transitions, and invariants from concrete scenarios. Use when inconsistent business meanings block design or implementation.
---

# Model the domain

Collect terms from product language, existing code, and representative scenarios. Find where one term has several meanings or several terms name the same thing. Ask the domain owner about consequential ambiguity rather than choosing silently.

Describe entities, relevant states, transitions, ownership, and rules that must hold. Work through a normal case and an invalid or concurrent case. Distinguish a domain concept from its current database or framework representation.

Keep the smallest vocabulary that explains the requested behavior. Save agreed meanings in the project's established documentation when the task calls for it. Identify remaining questions and the scenarios that would resolve them; do not redesign unrelated domains.
