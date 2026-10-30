---
name: kp-start
description: Choose the next useful activity for a software task when its intent is unclear or changes. Respect a named skill and settled decisions; handle clear small edits directly.
---

# Choose the next activity

Determine the requested outcome, what is already agreed, and the next unresolved need. Use the conversation and repository before asking for facts they already contain. Continue authorized implementation when the decisions are settled.

Select at most one primary specialist for the current need. Read its actual instructions only when useful. Names below are optional peers, not dependencies: if one is unavailable, explain that limitation and perform the requested work with available tools. Do not install skills or invent commands.

| Need | Skill |
| --- | --- |
| Challenge an early idea | `kp-grill-idea` |
| Plan an agreed multi-step change | `kp-change-plan` |
| Diagnose broken or slow behavior | `kp-debug` |
| Implement explicitly test-first | `kp-tdd` |
| Assess a diff without editing | `kp-review` |
| Simplify existing changed code | `kp-simplify` |
| Choose a smaller implementation approach | `kp-minimalist` |
| Understand branching complexity | `kp-complexity` |
| Assess an existing interface | `kp-ui-review` |
| Document implemented behavior | `kp-docs` |
| Resolve a technical fact with sources | `kp-research` |
| Compare competing expert arguments | `kp-simulate-discussion` |
| Design a code interface | `kp-api-design` |
| Clarify domain rules and terms | `kp-domain-model` |
| Test one design uncertainty cheaply | `kp-prototype` |
| Resolve an active merge/rebase conflict | `kp-merge-conflicts` |
| Preserve continuation state | `kp-handoff` |
| Collect behavioral proof for a change | `kp-verify-change` |
| Review a skill or upstream update | `kp-skill-maintenance` |

A diagnosis, design, or review request ends with that outcome unless implementation was also requested. Carry forward earlier authorization. Reconsider the activity when intent changes, without restarting the interview on every turn. This file cannot force its own activation; persistent routing requires a host instruction chosen by the user.
