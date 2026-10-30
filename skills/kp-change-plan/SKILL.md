---
name: kp-change-plan
description: Turn an agreed software change into a scoped implementation plan with observable acceptance criteria. Use for requested plans or changes whose dependencies need sequencing.
---

# Plan a change

Read the relevant code, instructions, and originating request. Separate settled decisions from material unknowns. Ask only questions that change scope or sequencing; investigate repository facts directly.

Describe the behavior to preserve and the behavior to change. Plan the smallest vertical slices that each produce something verifiable. For each slice name the affected boundary, meaningful check, and dependency on another slice. Include compatibility or data migration work only when the actual change requires it.

Make assumptions visible and give the simpler option when it meets the requirements. Keep the plan proportional: a small fix may need three lines, not a specification hierarchy.

Deliver a plan the implementer can execute and a list of unresolved decisions. Planning alone does not authorize creating tracker issues, changing code, or publishing. If implementation was already requested, continue when consequential decisions are settled.
