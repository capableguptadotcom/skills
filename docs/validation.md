# Initial validation record

Observed 30 October 2026. These checks establish package integrity and selected workflow behavior, not comparative skill effectiveness.

- All 20 owned skills passed the bundled skill-creator structural validator.
- The public `skills` CLI discovered all 20 entrypoints from `capableguptadotcom/skills` using Node 24.19.0 and `--list`. No agent skill installation was performed. The currently documented CLI minimum is Node 22.20.
- The catalog contains 815 unique source/path identities: 290 source assessments and 525 description assessments. Every entry has a one-line use, disposition, simulated critique, proposed behavioral check, provenance, and inspection depth. All named owned target skills exist. None of the current upstream frontmatter entries failed parsing.
- The tracker regression suite passed: file additions/deletions, runtime and license changes, shared references, stale review invalidation, immutable provenance despite a copied old catalog row, and default deferral for new candidates.
- Seven additional proposal integration tests passed using real temporary Git repositories and local bare remotes. They exercise draft publication, open-proposal reuse with an advanced main branch, replacement after closure, line-ending no-ops, dirty primary-checkout preservation, preview behavior, and cleanup after producer/validation/test failures. GitHub responses and candidate production are simulated; validation and fixture tests execute as subprocesses. Together with the seven tracker tests, the automated suite has 14 tests.
- The independent forward smoke run recorded 24 activity selections and executed three Python fixtures. Review and diagnosis preserved files; implementation reproduced and corrected the agreed behavior. See [the trace and limits](forward-testing.md).
- The live updater fetched all 11 public sources in an isolated temporary worktree, ran validation and tests, found no actual source changes, and exited successfully without a commit or PR. The main checkout remained clean and the temporary worktree was removed. This run exposed and led to corrections for Windows path limits and line-ending-only empty commits before the final success.
- GitHub Actions validated the published repository. [Successful run for the updater fixes](https://github.com/capableguptadotcom/skills/actions/runs/41030147943); [current runs](https://github.com/capableguptadotcom/skills/actions).

Daily reconciliation is active at 09:00 Pacific host-local time through Codex. It runs locally and depends on the app/host and GitHub access. Private organization checks remain local. Current sources had no delta, so the live no-change run did not exercise a real GitHub update PR creation or changed-candidate review.

No no-skill comparison, repeated model benchmark, automatic host-routing measurement, exhaustive support-script audit, or end-to-end test of every upstream integration was performed. Claims about measured uplift require the separate evaluation process.
