---
name: kp-api-design
description: Design or compare a module or API boundary from real caller needs, compatibility constraints, and failure behavior. Use for interface design; do not impose a new architecture on an established project.
---

# Design from the caller

Read representative callers and the code that owns state, policy, and transactions. Describe the simplest intended use, important failure paths, and compatibility obligations.

Compare meaningfully different interfaces when there is a real design choice. Show a short caller example and the responsibility each design hides. Prefer an interface that contains complexity rather than exporting coordination to every caller.

Extract shared mechanics when reuse or a concrete boundary benefit justifies it. Preserve existing layering when it fits; actions/services is one option, not a universal rule. Explicitly state side effects, retry semantics, and transaction ownership when they matter.

Recommend a design and a small caller-level check that would expose a bad boundary. Design-only work stops at the proposal unless implementation is also authorized.
