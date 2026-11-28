# Open decisions after the head-to-head (27 November 2026)

The head-to-head against the personal skills in daily use (see `CHANGELOG.md`) left eight questions open. This record takes them one at a time: the hypothesis, the experiment that could disprove it, what happened, the decision, and why. Every number comes from a results file in `eval/results/`. Claude Code runs use Sonnet, with 3 repeats unless stated; Opus judges each pair blind in both orders, and a win counts only when both orders agree.

## How to read the numbers

- **Wins or ties** is the share of pairs the first-named skill wins or ties. 70% is the bar `CONTRIBUTING.md` sets against no skill.
- **The interval** is a 95% Wilson interval, now printed by `run_evals.py tally`. With 9 pairs it is wide: 7/9 spans 45-94%, and even 9/9 only shows the true share is above 70%. A result on the near side of 70% with 9 or 18 pairs does not say which side the skill is really on.
- **Suite rubric** is the rubric in each `cases.json`, written from the skill's spec. It rewards evidence shown and coverage stated, because the specs require them.
- **Outcome-only rubric** (`judge --outcome-only`) keeps what was found or kept, scope and concision, and tells the judge not to reward evidence or coverage for their own sake. It was added in this pass to test whether a win is in the work or in the report.

## 1. `diagnose` against `diagnosing-bugs` with the host deciding

**Open question.** The first round counted 12/18 (67%) with every pair and 12/16 (75%) with held-back pairs left out, on opposite sides of 70%. The cause was the eval allowlist: `PYTHONHASHSEED=… python` did not match `Bash(python *)`.

**Hypothesis.** The split comes from the allowlist, not the skills. Allow the env-prefixed form, rerun both sides, and the two counts should agree.

**Experiment.** A probe confirmed `Bash(PYTHONHASHSEED=* python *)` lets the env-prefixed form through, and that shell loops over a variable are refused whatever the allowlist says (Claude Code cannot check them before they run). Both skills were rerun on the six judged cases, by name and host-decides (72 runs).

**Result.** Held-back answers fell from 8 to 2. The two counts now agree: host-decides 13/18 (72%) or 12/17 (71%); by name 13/18 (72%) or 13/17 (76%). Runs now record Claude Code's refused commands. 24 runs had a refused loop, and every one passed its checks because the agent ran the seeds one by one. So a refused command no longer counts as held back. A run is held back only when its answer says it could not do something.

**What the rerun showed instead.** Wherever the rival won, both skills had found the right cause. The rival won on evidence: it reproduced the failure under 20 to 50 pinned hash seeds, or it watched the regression test fail before the fix. `diagnose` said "trigger the failure on demand, or state why you cannot", and many runs took the second branch. `diagnosing-bugs` insists on a failing loop first and raises the reproduction rate of flaky bugs.

**Second hypothesis.** Telling `diagnose` to pin what varies and count failures, and to watch the failing check fail on the unfixed code, should remove those losses without hurting the cases where it already won.

**Experiment.** First, a new check on both flaky cases, "reports runs under pinned seeds", calibrated on existing answers. Before the edit it passed 13 of 24 `diagnose` runs and 19 of 24 rival runs. Then two sentences were added to `skills/diagnose/SKILL.md`, steps 1 and 7. The edited skill was rerun on the same cases (36 runs) and on the docstring near miss, the neighboring request that must stay unchanged. It was judged against the same rival runs.

**Result.**

| `diagnose` vs `diagnosing-bugs` | Before the edit | After the edit |
| --- | --- | --- |
| Checks passed (36 runs) | 30 | 34 |
| Pinned-seed check, flaky cases | 6/12 | 10/12 |
| Named, wins-ties-losses | 11-2-5, 72% | 13-3-2, 89% (67-97%) |
| Host decides, wins-ties-losses | 8-5-5, 72% | 10-3-5, 72% (49-88%) |
| Held-back answers | 2 | 0 |
| Docstring near miss loads the skill | 0/3 | 0/3 |

All the host-decides losses that remain come from selection. When both skills loaded, `diagnose` won 4, lost 2 and tied 3. When the host did not load `diagnose`, it lost all 3 pairs. `zero-backoff-diagnose` loads `diagnose` in 1 of 3 runs in every round (3 of 9 overall).

**Decision.** Keep `diagnose` with the edit. `diagnosing-bugs` can be retired from personal use: by name, the edited `diagnose` wins 13 of 18 pairs and loses 2.

**Why.** The edit removes a measured weakness, and the neighboring request stays unchanged. Host-decides is still 72% with an interval down to 49%, so "clears 70%" is not established there. The remaining gap is a selection miss on one prompt shape, not the skill's procedure.

**Selection follow-up, done.** With the current description, `zero-backoff-diagnose` ("Find out why. Don't change any files.") loaded `diagnose` in 10 of 20 runs. A description that adds "a question of why something does not work" and "asks for no changes" loaded it in 18 of 20.

| | Current description | New description |
| --- | --- | --- |
| `zero-backoff-diagnose` loads `diagnose` | 10/20 (30-70%) | 18/20 (70-97%) |
| Docstring near miss loads `diagnose` | 0/3 | 0/5 |
| `shape-change` design prompts also load `diagnose` | 6/10 | 7/10 |

The difference on the target case is significant (Fisher exact, two-sided p = 0.014). The neighbors are unchanged: on the near miss, and on the two `shape-change` design prompts with both skills installed (p = 1.0). There, `shape-change` loaded in every run and every check passed. The new description is adopted. `diagnose` also loading alongside `shape-change` on design questions about duplicate emails happens with either description; it is noted here, not fixed.

## 2. No-skill baselines for `review-change`, `simplify-code` and `shape-change` (rule 2)

**Open question.** The head-to-head compared each pack skill only with a rival. Rule 2 asks whether it beats no skill.

**Experiment.** Each suite was run with nothing installed (27 runs). The pack's earlier runs were judged against these, first on the suite rubric and then on the outcome-only rubric. The review suite was also run on Codex (2 repeats) before Codex hit its usage limit.

**Result.**

| Pack skill vs no skill | Suite rubric, named | Suite rubric, host decides | Outcome-only, named | Outcome-only, host decides |
| --- | --- | --- | --- | --- |
| `review-change`, Claude Code | 8/9 (8-0-1) | 9/9 | 1/9 (0-1-8) | 2/9 (0-2-7) |
| `review-change`, Codex | 6/6 (4-2-0) | not run | 1/6 (0-1-5) | not run |
| `simplify-code` | 9/9 (8-1-0) | 8/9 (8-0-1) | 9/9 (3-6-0) | 9/9 (4-5-0) |
| `shape-change` | 7/9 (7-0-2) | 9/9 (7-2-0) | no outcome rubric | no outcome rubric |

Automated checks passed in every no-skill review and simplify run (9/9 each) and in 5 of 9 shape runs.

**What this says.**

- **`simplify-code` is better in the code itself.** It never loses to no skill on outcomes. Its wins come from keeping behavior exactly: the no-skill rewrite turned `code is None or code == ""` into `if not code`, which changes falsy non-string inputs.
- **`review-change` wins only on the report.** On these three fixtures, Sonnet with no skill finds every planted defect, so the outcome rubric sees equal findings and penalizes the pack's evidence table and coverage section as padding. The suite rubric scores those same sections as the spec's Musts (evidence, stated coverage), and the pack wins.
- **`shape-change` beats no skill on its suite rubric.** It loses 2 of 3 named pairs on `agreed-plan`, where the no-skill answer was the shorter plan.

**Decision.** Keep all three; each clears rule 2 on its suite rubric. For `review-change`, record that the measured gain is in the report, not in finding more, and that its fixtures are too easy to show a difference in substance.

**Why.** Rule 2 is about the job as the spec defines it, and a review that shows its evidence and says what it did not check is that job. But "measurably better" should not rest only on a rubric that rewards the skill's own style. The outcome-only re-judge is how that showed up, so `CONTRIBUTING.md` now asks for both rubrics (see below).

**Follow-up.** Add a `review-change` fixture where a no-skill review misses a defect, for example one that only shows when a check is run, then measure again.

## 3. Host built-ins: Claude Code's `/code-review` and `/simplify` (rule 3)

**Open question.** Claude Code ships `code-review`, `simplify`, `debug` and `verify` skills, available in every condition. Per Claude Code's documentation, `/debug` reads Claude Code's own session log and is not a code-debugging skill, and `/verify` runs the app. Only `/code-review` (reports correctness bugs, edits nothing without `--fix`) and `/simplify` (cleanup, applies its fixes) overlap the pack.

**Experiment.** New `run --builtin NAME`: installs nothing and invokes the host's skill by name. 18 runs, judged against the pack by name on both rubrics.

**Result.**

| Pack vs built-in, named | Suite rubric | Outcome-only |
| --- | --- | --- |
| `review-change` vs `/code-review` | 9/9 (9-0-0) | 7/9 (7-0-2) |
| `simplify-code` vs `/simplify` | 9/9 (9-0-0) | 8/9 (1-7-1) |

- `/code-review` ran in about 13 seconds at about $0.05 and passed every check. On the correct change it reported findings that do not exist, such as treating negative stock as a contradiction when stock is never negative. That is where `review-change` wins on outcomes.
- `/simplify` produced essentially the same code as `simplify-code`.
- Without the pack, Claude Code chose `/simplify` on its own in 3 of 9 simplify runs and never chose `/code-review`. With the pack installed, the pack skill was chosen in 9 of 9 for both.

**Decision.** Keep `review-change`. Keep `simplify-code`, and record that in Claude Code its code is not better than `/simplify`.

**Why.** `review-change` beats the built-in review on outcomes, not only on the report. For `simplify-code`, rule 3 ("no built-in host feature does the job") is not met in Claude Code on code quality alone. It stays for three measured reasons: Codex has no such built-in, it beats no skill on outcomes, and it reports what it checked. If a later Codex run shows it does no better than no skill there, it should be retired.

## 4. `shape-change` against `grill-me`

**Open question.** In single-turn cases `shape-change` led, but under 70%, and only because of `agreed-plan`. An interview skill judged on its first turn may be understated.

**Hypothesis.** Over a real interview, with answers to its questions, `grill-me` catches up or overtakes `shape-change`.

**Experiment.** New conversation cases: `run` drives a Claude Code session in which a simulated user answers the agent. The simulated user is a second model that knows only the case's facts and wants a plan, not code. It gives three replies and then asks for the write-up. Checks read only the agent's turns, and stored sessions are deleted afterwards. There are three cases: the SMS plan and the dedupe question as interviews, plus a new French-launch case where the code shows the email body is English for everyone. Each ran 3 times by name for both skills and for no skill (27 conversations, about $0.70 to $1.10 each).

**Result.** The hypothesis held. `grill-me` beat `shape-change` 6-0-3 in conversations, so `shape-change` won or tied 3/9 (33%). `shape-change` also did no better than no skill (4-0-5). `grill-me` against no skill was 4-1-4. The judges' reasons point at `shape-change`'s step 5. It restated the full plan on every turn (4,286 characters per turn, against 3,159 for `grill-me`), twice wrote a plan file in the final turn, and once cut off its write-up.

**Edit tested.** Mid-interview, reply with what is settled and the next question, each question with a recommended answer. Use the plan template only for the write-up, and put it in the reply unless a file is requested. The edit is in `SKILL.md` step 5 and `references/exploration.md`. The edited skill was rerun (9 conversations, 18 single-turn runs) and judged against the same `grill-me` and no-skill runs.

| Edited `shape-change` | Before the edit | After the edit |
| --- | --- | --- |
| Conversation checks passed | 7/9 | 9/9 |
| Characters per agent turn | 4,286 | 3,514 |
| Conversations vs `grill-me` | 3-0-6 (33%) | 4-1-4 (56%) |
| Conversations vs no skill | 4-0-5 (44%) | 5-0-4 (56%) |
| Single turn vs `grill-me`, named | 5-1-3 (67%) | 6-0-3 (67%) |
| Single turn vs `grill-me`, host decides | 4-2-3 (67%) | 6-0-3 (67%) |
| Single turn vs no skill, named | 7-0-2 (78%) | 7-0-2 (78%) |
| Single turn vs no skill, host decides | 7-2-0 (100%) | 7-0-2 (78%) |
| Single-turn checks passed | 18/18 | 18/18 |

The drop against no skill with the host deciding (9/9 to 7/9) is inside both intervals (70-100% and 45-94%). 22 single-turn verdicts first failed on a usage limit and were re-judged with `--redo-errors`.

**Decision.** Keep the edit; it removed the measured failure without hurting single-turn cases. The question of `shape-change` against `grill-me` stays open: in conversations they are now even (4-1-4), and neither clears 70% against no skill there.

**Why.** Sonnet without a skill already interviews well on these cases. Neither skill shows a measured gain in multi-turn interviews, so the evidence does not support retiring either one.

## 5. Codex

**Open question.** The README says a change ships when it beats no skill in both hosts.

**Experiment.** Codex's usage limit had reset, so a Codex batch ran with 2 repeats: the pack and the rival by name, plus no skill. Codex finished the review suite and then hit its usage limit again. Partial results for the other suites were deleted, not reported.

**Result.** On Codex, `review-change` by name beat no skill on the suite rubric, 6/6 (4-2-0), and lost on outcome-only, 1/6. It beat the personal `code-review` 6/6 on both rubrics. That matches Claude Code.

**Second batch.** After the limit reset, Codex ran `simplify-code` in full and `shape-change` with no skill, then hit the limit again. The `grill-me` and `diagnose` runs did not happen, and their partial files were deleted. These runs used the final versions of the skills.

| Codex, by name (2 repeats) | Suite rubric | Outcome-only |
| --- | --- | --- |
| `review-change` vs no skill | 6/6 (4-2-0) | 1/6 (0-1-5) |
| `review-change` vs `code-review` | 6/6 (6-0-0) | 6/6 (4-2-0) |
| `simplify-code` vs no skill | 5/6 (2-3-1) | 5/6 (2-3-1) |
| `simplify-code` vs `code-simplifier` | 4/6 (3-1-2) | 4/6 (3-1-2) |
| `shape-change` vs no skill | 3/5 (2-1-2) | no outcome rubric |

Codex phrased two `shape-change` findings in ways the checks missed: "carries neither a phone number" and "five identical shipping emails" after a sentence about retries. Both patterns were widened. On every recorded run, the widening changes only those 6 Codex results, all from fail to pass, and no Claude Code result.

**Decision.**

- `review-change` and `simplify-code` behave in Codex as in Claude Code.
- `simplify-code` beats no skill in Codex as well. That is the measured reason it stays, although Claude Code's `/simplify` writes the same code.
- `shape-change` is at 3/5 against no skill in Codex. That is below 70% on five pairs, so it is not settled.
- `diagnose` and `shape-change` against `grill-me` have not run in Codex.

To finish: `scripts/run_evals.py run diagnose --host codex --repeats 2 --conditions named without` with the six judged cases; then the `grill-me` runs on the three single-turn shape cases; then the same judges.

## 6. Sweeps from more than one person (rule 1)

**Decision.** Not testable here. Every sweep so far is one person's sessions. Nothing in this pass changes that, and no skill's place is claimed on rule 1.

## 7. Retiring the losing personal skills

The personal skills live outside this repository, in `~/.agents/skills` and `~/.codex/skills`, so deleting them is the owner's call. Recommendation from the measured results:

- **`code-review` (personal):** retire. `review-change` beats it by name on both rubrics, in both hosts. With the host deciding, it loaded in only 3 of 9 runs.
- **`code-simplifier`:** retire. It never loaded on its own (0/9), and `simplify-code` ties or beats it on code (named 1-8-0, host decides 2-7-0).
- **`diagnosing-bugs`:** retire once the edited `diagnose` is in use. Its one measured strength, pinned reproduction, is now in `diagnose`.
- **`grill-me`:** keep for now. It ties the edited `shape-change` in conversations; retire it only if a later run favors `shape-change`.

## What these fixtures cannot show

The edited `diagnose` beats no skill on the suite rubric: named 18-0-0 (interval 82-100%), host decides 15-2-1 (74-99%). On the outcome-only rubric it does not: named 3-2-13, host decides 4-5-9. No skill found the right cause and fix in every `diagnose` and `review-change` fixture. There, the pack's measured gain is evidence and reporting, and the outcome rubric counts those sections as padding. Its one gain in outcome was the regression test on the invoice fix. Only `simplify-code` gained in the work itself. Next steps: harder fixtures that no skill fails, and a test of shorter reports for simple bugs.

**Shorter reports, adopted.** The hypothesis: `diagnose` and `review-change` lose the outcome-only judging because their templates have the same sections for a one-line bug as for a hard one. Each skill's report step now says to scale the report. For `diagnose`, that means a line per section and no table when one cause was plausible. For `review-change`, a short list instead of the table when there are one or two findings. Both variants were run by name on the same cases and judged against the same no-skill and rival runs.

| By name | Before | Shorter reports |
| --- | --- | --- |
| `review-change` vs no skill, suite rubric | 8-0-1 | 8-1-0 |
| `review-change` vs no skill, outcome-only | 0-1-8 (1/9) | 1-3-5 (4/9) |
| `review-change` answer length (no skill 1,524) | 2,051 | 1,654 |
| `diagnose` vs no skill, suite rubric | 18-0-0 | 18-0-0 |
| `diagnose` vs no skill, outcome-only | 3-2-13 (5/18) | 3-4-11 (7/18) |
| `diagnose` vs `diagnosing-bugs` | 13-3-2 | 14-2-2 |
| `diagnose` answer length (no skill 1,055) | 1,822 | 1,390 |
| `diagnose` checks passed | 18/18 | 17/18 (one pinned-seed report missing) |

**Why adopted.** Reports are 20 to 25% shorter, with no loss on the suite rubric or against the rival. Outcome-only moved the predicted way for both skills, but the gain is not significant (pooled 6/27 to 11/27). Neither skill clears 70% on outcome-only, so the conclusion above stands.

**A first harder review fixture did not separate them.** The hypothesis: a large, mostly cosmetic diff hides a subtle change from an unaided review. The new case `noisy-tidy-boundary` sends "just type hints and tidying, no behavior change". The diff touches every module and hides two things. One is a real defect: the size check became exclusive at 100, and the README allows 100. The other is a decoy: a removed `.strip()` that `float()` makes harmless. No skill found the defect in 3 of 3 runs and correctly dismissed the decoy, and so did `review-change`. The hypothesis is rejected for a diff this size. The case stays as a regression check. Separating them on substance probably needs a larger codebase than these fixtures.

## 8. Publishing

The branch is pushed. No pull request is merged from this work.

## Process changes this pass made

- **Allowlist:** allows `PYTHONHASHSEED=… python`. Refused commands are recorded. "Held back" means the answer says it could not do something.
- **Tallies:** print a 95% interval.
- **`judge --outcome-only`:** judges on a suite's `outcome_rubric`.
- **`run --builtin NAME`:** compares against a host's own skill.
- **Conversation cases** (`simulated_user`): run as multi-turn Claude Code sessions.
- **Judge and simulated-user prompts:** go on stdin. Two conversations passed Windows' 32K command-line limit.
- **Workspaces:** they are now really deleted, along with the `~/.claude/projects` folder Claude Code makes for each.
  - On Windows, `rmtree(ignore_errors=True)` silently failed on Git's read-only object files: 386 old workspaces had piled up in the eval folder.
  - Claude Code stores subagent transcripts in that project folder even without session persistence, so eval output could reach the user's session history.
  - Both were cleaned up: 652 empty project folders, 10 with subagent transcripts, and the 386 workspaces.
- **`CONTRIBUTING.md`, rule 2:** now names the rubric and asks for the outcome-only re-judge and the interval.

## Simulated review of the decision rule

A simulated discussion, used as a reasoning aid, not as evidence. Participants: an evaluator, a daily engineer, a maintainer and a skeptic.

- **Evaluator:** With 9 pairs, 7/9 and 9/9 have overlapping intervals. A bar of 70% on point estimates will flip on noise, as `diagnose` did between rounds (67%, then 72%).
- **Skeptic:** Worse, the rubric was written alongside the skill. The outcome-only re-judge turned `review-change` from 8/9 into 1/9. If we had not looked, we would have claimed it finds more bugs.
- **Daily engineer:** But I do want a review that says what it ran and what it skipped. That saves me re-checking. It is a real gain, just not the gain of finding more.
- **Maintainer:** Then the rule should say which rubric, report both, and a skill whose win is only in its report should say so in the changelog. It should not be retired for it.
- **Evaluator:** And a skill should not be admitted on a fixture where no skill already passes every check. Then the judge only measures style.

**Outcome.**

- Rule 2 names the suite rubric and requires reporting the outcome-only re-judge and the interval.
- A win that exists only on the suite rubric is recorded as a reporting gain.
- A skill whose no-skill baseline passes every check needs a harder case before claiming more than that.
