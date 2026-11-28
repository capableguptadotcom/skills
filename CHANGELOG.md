# Changelog

Each release records what changed and the evaluation summary that justified it.

## Unreleased

- Second pstack review ([docs/research/pstack-second-review.md](docs/research/pstack-second-review.md)), pinned at cursor/plugins `b7b93c3` (0.15.48). It covers what changed since `4dd1d05`, evidence of real use, all 59 entrypoints classified, the `statechart` adaptation and what the verification draft needs to ship. No skill added or changed.
  - Evaluated the three most-installed pstack skills on Claude Code with Sonnet, 3 repeats, judged blind by Opus in both orders. Wins or ties by name, suite rubric / outcome-only, with 95% intervals:

    | Candidate | vs no skill | vs the pack owner |
    | --- | --- | --- |
    | `typescript-best-practices` (with its `paths:` line removed) | 8/9 (56–98%) / 9/9 (70–100%) | vs `develop`: 4/9 (19–73%) / 5/9 (27–81%) |
    | `blast-radius` | 9/9 (70–100%) / 5/9 (27–81%) | vs `review-change`: 9/9 (70–100%) / 7/9 (45–94%) |
    | `unslop` | 8/9 (56–98%) / 6/9 (35–88%) | no owner |

  - New draft [drafts/statechart-everystate](drafts/statechart-everystate/): `statechart` without Java, TLC or a TypeScript runtime.
    - Instructions in `SKILL.draft.md` (not installable).
    - `trace_chart.py` (read-only Python) turns everystate's `-json` trace, and optionally its state graph, into a Mermaid chart and a numbered bug path. Tested in `tests/test_scripts.py`.
    - everystate 0.4.1 matched TLC 2.19 on all 33 of upstream statechart's recorded cases (exit code, rule and shortest trace; state counts where TLC printed them; state graphs).
    - Evaluated on four TypeScript flows (`eval/statechart-everystate`). Against no skill it won 12/12 on the suite rubric but only 3/12 outcome-only. The same procedure without the chart did no worse (chart vs no chart: 5/12 suite, 8/12 outcome-only). It stays a draft.
  - None clears `CONTRIBUTING.md`: `develop` and `review-change` already cover the first two, and `blast-radius` and `unslop` gain only in the report. As published, `typescript-best-practices` never loads in Claude Code: its `paths:` glob hides it in all 18 runs.
  - New eval suites with synthetic fixtures: `eval/typescript-best-practices` (TypeScript state, webhook boundary, one-line near miss; hidden tests on Node's type stripping), `eval/blast-radius` (a TypeScript service whose changes break a Python job and saved data, plus a safe change), `eval/unslop` (PR description, release notes with literals, typo-only near miss).
- Eval harness (Claude Code):
  - The `PowerShell` tool is removed (`--disallowedTools PowerShell`). On Windows the agent then uses Bash, where the allowlist applies; before, PowerShell commands were refused, which cost most to skills that run code. Five earlier results files record such refusals.
  - The allowlist adds `node`, `npm test`, `head`, `tail` and `grep`.
  - Redaction also catches Git Bash paths (`/c/Users/<name>`).
  - Runs record the disallowed tools.
  - The allowlist adds `npx everystate@0.4.1`, pinned.
  - Output is written as UTF-8, so a judge reason with an arrow no longer stops a judge run on Windows.

- `skill-feedback` sets `metadata.internal: true`. The skills CLI leaves it out unless `INSTALL_INTERNAL_SKILLS=1`, so the team install is now `npx skills add capableguptadotcom/skills --copy --agent claude-code codex -y`, with no skill list. A test checks that only `skill-feedback` is internal.
- New [docs/writing-skills.md](docs/writing-skills.md): how to write and evaluate a skill, with a checklist and the candidates considered so far (`grill-me`, `grill-with-docs`, formal verification, `statechart`) and where each stands. The README gains usage examples.
- README rewritten shorter. Updating means running the install command again: tested with skills CLI 1.8.1, `npx skills update` replaces copied folders with links to an absolute path on the installer's machine, which break once committed.

## 1.0.0 (27 November 2026)

The v1 restructure, evaluated against no skill, the personal skills in daily use and the host's built-ins (see [docs/open-decisions.md](docs/open-decisions.md)). Measured mainly in Claude Code with Sonnet. In Codex, only `review-change` and `simplify-code` have been measured so far.

- Dropped the `kp-` prefix. New names: `shape-change`, `develop`, `diagnose`, `review-change`, `research`, `simplify-code`, `handoff`, `simulate-discussion`. Four names avoid collisions with host built-ins and common third-party skills.
- `handoff` and `simulate-discussion` are explicit-only in both hosts. `simulate-discussion` is rebased on the original version in daily use.
- New explicit skill `skill-feedback`: turns a session problem into a sanitized issue or draft PR, with `session_info.py` and `sanitize_check.py`.
- Added output templates (plan, diagnosis, findings, answer, handoff, issue, PR body), a performance reference for `diagnose`, a source-ranking reference for `research`, and scripts `diff_context.py` (`review-change`) and `handoff_state.py` (`handoff`).
- Moved the verification-recipe and property references out of `develop` into `drafts/verification-skill/` for a later release.
- Validator: name and reserved-name rules, description and body length, allowed frontmatter keys, matching invocation settings for both hosts, Python-only scripts without network access, no package or tool-server files, no personal paths. Tests cover each rule and run every bundled script.
- Added `CONTRIBUTING.md` and a Skill problem issue template.
- `skill-feedback` gains a weekly sweep: `sweep_sessions.py` reads the user's own Codex (history database and rollout files) and Claude Code sessions and reports, per skill, uses on its own and by name, pushback, interruptions and installed skills that never ran. It prints pointers, not conversation text; `--show`, `--uses` and `--share` read one use, sample uses, or print a shareable count table. `CONTRIBUTING.md` gains the rule for when a skill earns or loses a place.
- Evaluation, Claude Code with Sonnet, judged blind by Opus in both orders. On a 5-session sample world, `skill-feedback` tied no skill twice and lost once: five files are easy to read by hand. On a 208-session world it passed 3 of 3 against 1 of 3 without it and won 3 of 3 judged pairs: without it, agents found the loud recurring complaint but mostly missed the skill that only ran by name and the unused one. Cost per run $0.26 with the skill, $0.49 without.
- Eval harness: workspaces live outside the repository and user profile so a baseline cannot find the skill under test; runs that hit a usage limit, a locked workspace, or a baseline that read the skill are marked invalid and left out.
- Head-to-head against the personal skills people use most today. Each pair ran the same cases on Claude Code with Sonnet, 3 repeats, installed and left to the host (`with`) and invoked by name (`named`); Opus judged each pair blind in both orders, and a win counts only when both orders agree. The table counts wins or ties for the pack skill; 70% is the bar `CONTRIBUTING.md` sets against no skill, used here only as a reference. "Held back" pairs are those where either run's answer says a command was denied by the eval allowlist (only `python`, `git`, `ls`, `cat` shell commands), which is the same for both sides but costs more to a skill that asks for shell loops.

  | Pair (pack vs personal) | Named, all pairs | Named, held-back left out | Host decides, all pairs | Host decides, held-back left out |
  | --- | --- | --- | --- | --- |
  | `diagnose` vs `diagnosing-bugs` (6 cases) | 15/18, 83% (15 W, 0 T, 3 L) | 12/13, 92% | 12/18, 67% (11 W, 1 T, 6 L) | 12/16, 75% |
  | `simplify-code` vs `code-simplifier` (3) | 7/9, 78% (7 W, 2 L) | 6/8, 75% | 9/9 (8 W, 1 T) | 9/9 |
  | `review-change` vs `code-review` (3) | 9/9 (9 W) | 9/9 | 9/9 (8 W, 1 T) | 9/9 |
  | `shape-change` vs `grill-me` (3) | 6/9, 67% (5 W, 1 T, 3 L) | 6/9 | 6/9, 67% (4 W, 2 T, 3 L) | 6/9 |

  - `review-change` wins every pair. Both sides found the bugs; the judge preferred `review-change` for run evidence, locations, severity order and stated coverage. `code-review` loaded on its own in 3 of 9 runs, `review-change` in 9 of 9.
  - `simplify-code` wins. `code-simplifier` won 2 of 3 named pairs on `named-functions`; `simplify-code` won every pair on the scoped `current-change` and the `already-clear` case. `code-simplifier` never loaded on its own (0 of 9); `simplify-code` loaded 9 of 9.
  - `diagnose` wins by name in both counts. With the host deciding, `diagnose` wins more pairs (11 against 6, or 11 against 4), but whether it clears 70% depends on the count: 67% with every pair, 75% with held-back pairs left out. By name, the rival's 3 wins are on the flaky-test cases, where it ran wider seed sweeps; with the host deciding it also won 2 of 3 on `zero-backoff-diagnose`, often in runs where it had not loaded. `diagnose` loaded on its own in 15 of 18 runs, `diagnosing-bugs` in 8 of 18; neither loaded on the docstring near miss. Held back: 5 `diagnose` runs and 3 `diagnosing-bugs` runs, mostly `PYTHONHASHSEED=… python` commands the allowlist does not match.
  - `shape-change` against `grill-me` is not settled by these cases. `shape-change` wins more pairs, but under 70% in every count, and its lead comes from `agreed-plan`, where `grill-me` interviews instead of writing the agreed plan (3 of 3 named). On the two cases both skills claim, `grill-me` won 3 named pairs and `shape-change` 2 (1 tie); with the host deciding they split 3 and 3. `grill-me` did not load on its own for the design question (0 of 3) and then missed the four-worker fact.
  - Automated checks passed in 182 of 186 runs (failures: one `diagnosing-bugs` run that stopped to ask for a denied loop, and `grill-me` on the design question when it did not load), so these fixtures separate the skills mostly through judging. Cost per run was $0.07 to $0.11 on both sides. Each interview case is one turn (`claude -p`). Not measured: Codex, other models, the no-skill baseline for the three new suites. Personal skills tested: `~/.agents/skills/diagnosing-bugs` and `code-review`, `~/.codex/skills/code-simplifier` and `grill-me` (the standalone versions; the `~/.agents` `grill-me` only delegates to another skill).
- `skill-feedback` is a maintainers' tool.
  - It runs when named, or on a schedule the maintainer sets up with the repository named in its prompt. Implicit invocation stays off.
  - It posts only to a repository the person names, and only if the signed-in GitHub account can push to it (`gh api repos/<repo> --jq .permissions.push`). It never forks, and it no longer defaults to the skill's source repository. A maintainer's scheduled sweep can open draft PRs here; anyone else's stops at local drafts.
  - The README's team install leaves it out. A test fails if the skill regains a default destination or drops the push-access check.
  - `CONTRIBUTING.md` tells people who use the pack to report problems to the maintainers, not to open issues or PRs here.
- Open decisions from the head-to-head, tested one by one: see [docs/open-decisions.md](docs/open-decisions.md).
  - `diagnose` now pins what varies in an intermittent failure and watches the failing check fail first. Against `diagnosing-bugs`, by name, it went from 11-2-5 to 13-3-2.
  - `shape-change` no longer restates the plan mid-interview. Against `grill-me` in conversations it went from 3-0-6 to 4-1-4.
  - All three new suites beat no skill on their suite rubric. On an outcome-only rubric, `review-change` and `diagnose` do not: no skill already solves those fixtures.
  - `diagnose`'s description now covers "find out why" questions that ask for no changes. On that case it loaded in 18 of 20 runs, against 10 of 20 before.
  - `diagnose` and `review-change` scale their reports to the problem: about 20 to 25% shorter, with no loss on the suite rubric.
  - `simplify-code` matches Claude Code's `/simplify` on code. `review-change` beats `/code-review` on outcomes.
  - The harness gains no-skill baselines, `--builtin`, conversations with a simulated user, `--outcome-only` and intervals.
  - On Codex (2 repeats), by name, against no skill: `review-change` 6/6 and `simplify-code` 5/6 on the suite rubric; `shape-change` 3/5. Codex has not yet run `diagnose`.
- New eval suites with specs, cases and fixtures: `review-change` (a branch with an off-by-one that breaks an unchanged caller, a return-type change that breaks an untested caller, a correct change), `simplify-code` (nested code with edge behavior the visible tests leave open, an uncommitted change beside messy code that is out of scope, already-clear code; hidden tests pin behavior) and `shape-change` (a "grill me" plan with facts the code answers, a design choice, an agreed plan).
- Eval harness: `judge --against` compares two results files, with a per-suite rubric, hidden-test results shown to the judge, explicit ties counted as ties and `--redo-errors` for pairs the judge failed to answer; `judge` and the new `tally` print verdicts with and without allowlist-held-back pairs. Cases can put a change on a branch or leave it uncommitted, and check that paths outside the scope stay untouched. Agent and Task are allowed so skills that delegate to subagents run as they do in real sessions. Named Claude Code runs now record that the name resolved to the installed skill. An answer that discusses rate limits no longer marks a run invalid. Runs record Claude Code's permission denials.
- `diagnose` check fix: the `wrong-hypothesis` check "rejects the user's hypothesis" missed answers that reject it in other words, so it also accepts `load_config … does read`, a table row for "ignores MAX_ATTEMPTS" marked rejected, and "(guess|theory|assumption) … wrong". In the head-to-head, `diagnose` named went from 1 of 3 to 3 of 3 on that check; every other count, and every run in the earlier `diagnose` results files, is unchanged.
