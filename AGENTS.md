# Maintaining these skills

The product is the set of folders in `skills/`. Each folder is one skill that does one job, installs on its own, and works the same in Codex and Claude Code.

## Change a skill for a reason

Start from a concrete problem: a `skill-feedback` report, an evaluation failure, or a repeated correction in real work. Do not add a skill or a rule because an upstream collection has one. Prefer improving the skill that owns the job over adding another trigger.

For each change, name the behavior that should improve and the neighboring request that must stay unchanged. Add the case to `eval/<skill>/cases.json` and confirm it fails before the change and passes after. Fix at the highest level that works: a script or validator rule first, then a template or reference, then wording. Try a shorter version first.

## Keep every skill portable

- No references outside the skill's own folder, no sibling paths, no personal paths, no particular model or agent count.
- Scripts are Python, read-only unless the skill's job is to write, and never use the network.
- Explicit-only skills set both `disable-model-invocation: true` and `policy.allow_implicit_invocation: false` in `agents/openai.yaml`.
- A reference, script or template stays only if an evaluation case uses it.

## Before publishing

```sh
python scripts/validate.py
python -m unittest discover -s tests -v
git diff --check
```

Describe a single run as a smoke test. Do not claim an improvement without a comparable no-skill or previous-version baseline.

## Session data

Developers may use their own session logs to report skill problems through `skill-feedback`. Only sanitized synthetic cases enter this public repository: no transcripts, code, project names, customer data or credentials. Raw material stays local and ignored, under `private/`.
