# Changelog

Each release records what changed and the evaluation summary that justified it.

## Unreleased

Restructure toward v1. Not yet evaluated against a no-skill baseline; no release tag.

- Dropped the `kp-` prefix. New names: `shape-change`, `develop`, `diagnose`, `review-change`, `research`, `simplify-code`, `handoff`, `simulate-discussion`. Four names avoid collisions with host built-ins and common third-party skills.
- `handoff` and `simulate-discussion` are explicit-only in both hosts. `simulate-discussion` is rebased on the original version in daily use.
- New explicit skill `skill-feedback`: turns a session problem into a sanitized issue or draft PR, with `session_info.py` and `sanitize_check.py`.
- Added output templates (plan, diagnosis, findings, answer, handoff, issue, PR body), a performance reference for `diagnose`, a source-ranking reference for `research`, and scripts `diff_context.py` (`review-change`) and `handoff_state.py` (`handoff`).
- Moved the verification-recipe and property references out of `develop` into `drafts/verification-skill/` for a later release.
- Validator: name and reserved-name rules, description and body length, allowed frontmatter keys, matching invocation settings for both hosts, Python-only scripts without network access, no package or tool-server files, no personal paths. Tests cover each rule and run every bundled script.
- Added `CONTRIBUTING.md` and a Skill problem issue template.
