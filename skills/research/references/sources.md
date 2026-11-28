# Source ranking

Prefer the source that owns the claim. From strongest to weakest for a technical fact:

1. **Specification or standard** for what must happen.
2. **Implementation** at the installed version: source code, type definitions, tests. This is what actually happens.
3. **Official documentation and release notes** for the version in use. Check the version selector; docs often show the latest release.
4. **Maintainer statements** in issues, discussions or changelogs.
5. **Reproducible experiment** you ran, with the command and output kept.
6. **Commentary**: blog posts, answers, videos. Useful to find the primary source, not to replace it.

When two sources disagree:

- Docs and implementation disagree: the implementation describes current behavior; the docs may describe intent. Report both.
- Versions differ: answer for the installed version and name what changes on upgrade.
- Only commentary exists: say so, label the claim unverified, and propose the check that would settle it.

An experiment beats any document for the narrow case it covers. Say how narrow that case is.
