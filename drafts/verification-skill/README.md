# verification-skill (draft, not installable)

These references moved out of `develop` so its everyday instructions stay short. They will become an explicit `verification-skill` that creates and maintains a project's own `verify-*` skills: a runtime recipe, or a formal or property check tied to a code revision.

Still needed before it ships: the skill entrypoint, a `scaffold_verify.py` script, a `check_anchor.py` script that reports whether covered files changed since the recorded revision, a skeleton template, and evaluation cases. The existing evidence for this guidance is in [docs/verification-practice.md](../../docs/verification-practice.md).

This folder has no `SKILL.md`, so installers do not pick it up.
