# Maintaining our daily skills

The product is the small set in `skills/kp-*/SKILL.md`. Each entrypoint owns a recognizable activity and keeps conditional detail in its own references. A user should not need the catalog in order to describe ordinary development work.

Change a skill for a concrete task or observed failure in our work. State what behavior should improve and what neighboring behavior must remain intact. Prefer revising the existing owner to adding another trigger. Keep a separate skill only when its output, procedure or scope would otherwise become ambiguous.

Keep every folder independently installable. Do not require sibling skills, personal paths, particular models, a fixed agent count or an unavailable integration. Use the actual host tools. Preserve the user's chosen scope, settled decisions and existing authorization.

Before publishing, run:

```sh
python scripts/validate.py
python -m unittest discover -s tests -v
git diff --check
```

For a substantive instruction change, also exercise a realistic case and a relevant boundary case. Describe a single-run smoke test as such; do not claim comparative improvement without a comparable baseline.

The upstream audit survives at tag `upstream-audit-2026-10-31`. It is historical research, not an active backlog or a source of automatic changes. Do not restore catalog synchronization or build session-based learning unless that work is requested. Keep raw conversations and private material out of this public repository.
