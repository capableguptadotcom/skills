---
name: shape-change
description: Use when someone wants to think through an idea, choose a design or architecture, settle domain terms, or get a plan before any code is written. Produces decisions and a plan in verifiable slices. Not for building a change that is already agreed.
---

# Shape the change

This skill does one thing: it turns an unsettled idea or design question into decisions and a plan that someone can assess. Building an agreed change is a delivery task, not this one.

1. **Find what is settled.** Identify the desired outcome, current behavior, agreed constraints and the unknowns that would change the decision. Inspect the code and product evidence before asking anything. Check: each question you ask is a choice only the user can make, not a fact the repository answers.
2. **Pick the mode.**
   - Early idea, or the user wants to be interviewed: read [exploration](references/exploration.md).
   - Interface, module boundary, shared logic, domain terms or a prototype: read [design](references/design.md).
   - An agreed change that needs a plan: go straight to step 3. Do not repeat discovery.
3. **Recommend the smallest complete approach.** State what changes, what stays compatible and the observation that would show success. Check: every requirement the user named is met or explicitly deferred.
4. **Sequence only when needed.** Split dependent work into a few slices that each end in a verifiable state. A small fix needs no slices.
5. **Deliver** using [the plan template](assets/plan.md). Keep confirmed decisions and open questions apart. During a long discussion, restate them when they change.

## Boundaries

- Planning, design and interviews do not authorize production edits, tracker updates or implementation.
- A requested prototype authorizes only that bounded experiment.
- If implementation was already requested and the decisions are settled, carry the agreement forward and continue. Do not ask for the same approval again.
