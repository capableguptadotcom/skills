# Pstack, second review: what changed, what is used, what to adopt

28 November 2026. This follows the [first review](../pstack-first-review.md) (pinned at [`4dd1d05`](https://github.com/cursor/plugins/tree/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack), 0.15.36) and does not repeat it. New pin: [`b7b93c3`](https://github.com/cursor/plugins/tree/b7b93c36be9bcc36a74db438e0fd385d660bc559/pstack), 0.15.48, 26 November 2026. No upstream installer, helper or test was run. Third-party skill files were copied only into eval workspaces outside this repository.

**Short answer.** pstack is widely installed and actively maintained, but nobody has published a measured effect on outcomes, its authors included. Its three most-installed skills were evaluated here against no skill and against the pack skill that owns the job. None clears the bar in `CONTRIBUTING.md`, so none is added:

- `typescript-best-practices` beats no skill, including on outcomes, but not `develop`, which already owns the job. As published it does not run in Claude Code at all.
- `blast-radius` and `unslop` win on the suite rubric but not on outcomes. Their gain is in the report, not the work.

Two ideas are worth testing inside the pack skills that own them: modeling variant state as a discriminated union (in `develop`), and naming the one fact a verdict rests on (in `review-change`). `statechart` can be adapted without its TypeScript runtime and Java, and the verification draft has a concrete list of what it needs to ship.

## 1. What changed since the first pin

Seven merged PRs touch `pstack/` between 29 October and 24 November, all by the author ([poteto](https://github.com/poteto)), none with review comments. Net: 113 files, +714/−2,401 lines. One entrypoint was added (`reframe`), none removed, so there are now 59.

| PR | What it did | Evidence the PR gives |
| --- | --- | --- |
| [#1236](https://github.com/cursor/plugins/pull/1236) | `why` and `how` cut to one short file each (12 `why` reference files and both `how` prompt templates deleted; nothing routes to `how` any more). `statechart` reports SANY's line and column on a parse error and draws arrows into a parent state through its border. `sharpen` asks for prototypes. New default models (Fable 5.2, Opus 5.5, Gemini 4 Carbon). | Structural checks. For statechart: 3 new tests fail before and pass after; full suite 373 pass with TLC. No behavior comparison for the `why`/`how` cuts. |
| [#1249](https://github.com/cursor/plugins/pull/1249) | Shorter texts for 14 principles, `unslop`, `technical-writing` and three playbooks (−2,764 lines). `reflect` and `architect` lose their reference files and subagents. The Orchestrate playbook and `check-plan.mjs` are removed. New `poteto-mode/worker.md` that every started agent reads. Opus-first routing capped at xhigh. | Structural checks only. The PR states the shorter `architect` and principle texts "drop the interface-depth wording". No before/after runs. |
| [#1283](https://github.com/cursor/plugins/pull/1283), [#1284](https://github.com/cursor/plugins/pull/1284) | Gemini panel seat moves to Gemini 4 Neon, then to its xhigh level. | #1284 reports a blind comparison: both levels caught every planted flaw, xhigh found more unplanted problems, about 50% slower. No counts given. |
| [#1292](https://github.com/cursor/plugins/pull/1292) | `statechart` on native Windows: no `/bin/sh`, `taskkill /t /f` instead of process groups, TLC's `\r\n` line ends. Fixes community issue [#1170](https://github.com/cursor/plugins/issues/1170). | 34 new tests fail before and pass after; corpus replayed with `\r\n` 33/33. "Nothing ran on Windows, so every Windows claim above is inferred." |
| [#1324](https://github.com/cursor/plugins/pull/1324), [#1326](https://github.com/cursor/plugins/pull/1326) | New `/reframe`: 8 to 12 expert terms with cited real uses, 2 or 3 neighboring fields, and the description rewritten; first lists the problems a vague description could be. | Three runs on in-repo cases; separate agents opened all 42 cited links and confirmed them. No baseline. |

What this changes from the first review:

- **Subtraction without measurement.** The first review praised [#419](https://github.com/cursor/plugins/pull/419) for testing each cut. The November cuts (#1236, #1249) remove more text than any earlier pass and report only structural checks. Earlier, [#634](https://github.com/cursor/plugins/pull/634)'s unmeasured cut broke step numbering ([#807](https://github.com/cursor/plugins/pull/807)). Treat the current short texts as unvalidated rewrites, not as the tested versions the first review read.
- **`statechart` is no longer POSIX-only by design.** The first review's reason for not adopting it was its TypeScript runtime, a Java/TLC installer through mise and POSIX process handling. #1292 removes the third, but only by inference: it was not run on Windows. The first two remain.
- **`worker.md` makes pstack's delegation less compatible with this pack.** It tells every started agent never to ask a person a question, to add no check above the brief, and to open every PR ready for review, never as a draft. This pack's rules (ask about a choice that changes the result; draft PRs) conflict with both.
- **Model routing churned again** (three PRs in four days). As the first review said, this is host and provider maintenance, not evidence that a skill got better.

## 2. Evidence about real use

Measured here means someone counted or ran something and reported the number. Everything else is a claim.

**Installs and attention (counted).**

| Signal | Number | Source |
| --- | --- | --- |
| skills.sh installs, upstream source `cursor/plugins` | `unslop` 41,867; `typescript-best-practices` 13,006; `blast-radius` 8,908; `technical-writing` 7,140; `setup-pstack` 5,585; most principles 5,800–6,800; `poteto-help` 2,655 | [skills.sh search API](https://skills.sh/api/search?q=pstack), 28 November 2026. Counts are per skill and cumulative; an install is not a use. |
| skills.sh installs, port `backnotprop/pstack` | `unslop` 15,502; `why` 13,755; `arena` 13,687; `poteto-mode` 13,579; others 12,700–13,500 | same |
| GitHub stars | `cursor/plugins` 20,092 (the whole plugin repository, not pstack alone); ports [backnotprop/pstack](https://github.com/backnotprop/pstack) 5,356, [michael-denyer/pstack-claude](https://github.com/michael-denyer/pstack-claude) 4,971, [ericlitman/open-pstack](https://github.com/ericlitman/open-pstack) 596 | `gh api`, 28 November 2026 |
| Issues mentioning pstack in `cursor/plugins` | 85 issues from 65 accounts, August to November 2026 (37 in October, 39 in November); 71 open | [issue search](https://github.com/cursor/plugins/issues?q=pstack) |
| Cursor marketplace | No install count shown | [marketplace page](https://cursor.com/marketplace/cursor/pstack) |

The issues are the strongest sign of real use: people hit concrete problems in `watch-pr`, worktree cleanup, `statechart`, and the Claude Code and Codex mappings, for example [#1053](https://github.com/cursor/plugins/issues/1053) (PRs that are blocked reported as ready), [#1054](https://github.com/cursor/plugins/issues/1054) (untracked files labeled safe to drop), [#1235](https://github.com/cursor/plugins/issues/1235) (a rule "holds" when the action that could break it never fires), [#864](https://github.com/cursor/plugins/issues/864) (in Claude Code, delegates skip principle reads) and [#1165](https://github.com/cursor/plugins/issues/1165) (`typescript-best-practices` uses `z.string().uuid()`, deprecated in Zod 4). Most of the skills.sh volume is for the three prose and TypeScript skills, not for `poteto-mode`.

**Results (measured).** One comparison exists outside the repository: a video by Rob Shocks, summarized by [The Agent Daily](https://the-agent-daily.org/agentnews-experimental/deep-dives/pstack-is-agent-overkill-use-it-anyway), built one feature with and without pstack: about one hour with it, thirty minutes without, with the pstack result described as more hardened and catching three false claims. That is one task, one person, no blinding. The [voices index](https://pstack.ganhai.cloud/en/voices/) collects anecdotes (about 12 PRs in two days; Core Web Vitals "all green") with no before/after data. Hacker News has no substantive thread; the most concrete comment reports a weekend unattended run of about 15 PRs ([item 50298405](https://news.ycombinator.com/item?id=50298405)); two recommend `unslop` and `technical-writing` ([50225446](https://news.ycombinator.com/item?id=50225446), [50190586](https://news.ycombinator.com/item?id=50190586)); one objects that stacks encode their author's habits ([50001225](https://news.ycombinator.com/item?id=50001225)).

**Author evaluations.** The README and the ten guide pages publish no results. Individual PRs report small experiments; the first review listed them ([#633](https://github.com/cursor/plugins/pull/633), [#716](https://github.com/cursor/plugins/pull/716), [#721](https://github.com/cursor/plugins/pull/721), [#729](https://github.com/cursor/plugins/pull/729)). Since then only #1284 and #1324 report runs, neither with counts against a baseline.

**Claims (not measured).**

- *"2,000 / 2,500 PRs a month."* The author's own posts and talk ([talk](https://www.youtube.com/watch?v=NjoZoUm85x0), [summary](https://www.selfaligned.me/newsletter/how-poteto-ships-2500-prs/)). This is her personal PR volume, with no baseline, no definition of a PR and no revert or defect rate; she has said the number "was never a goal" ([write-up](https://redreamality.com/blog/lauren-tan-poteto-trust-before-parallel/)). It does not isolate pstack's effect.
- *"1,150 PRs in 4 days."* Only an aggregator states it, without a source ([besthub.dev](https://www.besthub.dev/articles/grok-s-potato-sister-open-sources-pstack-agent-harness-for-1150-prs-in-4-days-fcc0f85853f3)).
- *"10,000 agent runs in a week."* A usage count from a Cursor landing page that now redirects; a count of runs, not an outcome.
- *Skill counts* vary from 45 to 58 across write-ups ([Flavio Copes](https://flaviocopes.com/pstack/), [Firecrawl](https://www.firecrawl.dev/blog/best-cursor-plugins), [nakaji](https://note.com/nakaji3/n/ne542e2cadf94?hl=en)); none of these authors reports measured use.
- The author was [reported](https://aicoder.com/news/news-20261103-x-discussion-poteto-adversarial-code-review-waste-of-tokens-empirical-formal-verification-pstack) on 3 November to call adversarial agent review "mostly a waste of tokens" and to plan less use of `interrogate`; no repository change followed by 26 November.

Common criticisms across the write-ups: overkill for small changes, high token cost, and an assumed worktree-and-PR workflow.

## 3. Every entrypoint, classified

"Covered" names the owner that already does the job. "Adopt or adapt" means worth carrying in some form. "Not worth it" gives the reason. Skills marked † were evaluated in section 4.

| Entrypoint | Changed since pin | Class | Owner or reason |
| --- | --- | --- | --- |
| architect | Cut to 11 lines | Covered | `shape-change` ([design reference](../../skills/shape-change/references/design.md)): compare caller-facing shapes before code. |
| arena | Shorter | Not worth it | A multi-model panel keyed to Cursor model slugs; Claude Code subagents and workflows run parallel attempts when a user asks. |
| automate-me | Wording | Not worth it | Infers a personal working mode from history; session learning stays with `skill-feedback`'s maintainer sweep. |
| benchmark-checklist | No | Covered | `diagnose` ([performance reference](../../skills/diagnose/references/performance.md)). |
| blast-radius † | Two references to `why` dropped | Covered; adapt one idea | `review-change`. By name it beats no skill and `review-change` on the suite rubric (9/9 each), but not no skill on outcomes (5/9), and it costs about 1.5 times as much. Worth testing in `review-change`: name the one fact the verdict rests on and check it against real code. |
| bro | No | Not worth it | A one-line preference ("say it plainly"). |
| correct | No | Not worth it | Turning repeated mistakes into lints and types is the pack's own maintenance rule (`AGENTS.md`: script or validator first), not a daily skill. |
| create-verification-skill, maintain-verification-skill | No | Adapt | Into the by-name verification skill drafted in [drafts/verification-skill](../../drafts/verification-skill/) (section 5). |
| create-formal-verification-skill, maintain-formal-verification-skill | No | Adapt | Same draft; see section 5 for what it needs. |
| figure-it-out | No | Covered | `shape-change` (agreed plan, verifiable slices) and `develop`. |
| how | One file, 21 lines | Covered | `research`, and Claude Code's Explore subagent. Upstream itself stopped routing to it. |
| in-your-own-words | No | Covered | `shape-change` restates the goal when it resolves ambiguity. |
| interrogate | No | Covered | `review-change` and Claude Code's `/code-review` (including its multi-agent mode). Its author now questions the approach. |
| ketchup | No | Covered | `handoff`. |
| ketchup-video | No | Not worth it | Video output is outside product development work. |
| make-bot-ui | No | Not worth it | Specific to one internal control plane. |
| no-comments | Traces instead of `/how` | Not worth it | The literal deletion policy was rejected in the first review; `simplify-code` and `/simplify` cover scoped comment cleanup. |
| poteto-help | Catalog edits | Not worth it | Help for pstack's own catalog. |
| poteto-mode (+ `worker.md`, 22 playbooks) | Rewritten, Orchestrate removed | Not worth it | A router with model routing and autonomy rules (never ask, never draft) that conflict with this pack's authorization rules. |
| recall | Own investigators | Covered | `handoff` plus the host's session resume. |
| reflect | One file, no subagents | Covered | `skill-feedback` (maintainers), which also keeps raw sessions private. |
| reframe | **New** | Not worth it yet | Prose-only and portable, but unmeasured (three runs, no baseline), needs web access to confirm citations, and no one has reported the job in this pack's teams. Watch. |
| setup-pstack | Routing ladder | Not worth it | Cursor model configuration. |
| sharpen | Last line | Not worth it | Prompt rewriting; optional and outside daily development. |
| show-me-your-work | Model line | Covered | `handoff` and `develop` keep a compact decision trail. |
| statechart | Windows, SANY, borders | Not adopted; adaptable | Still a 3,980-line TypeScript compiler with a Java/TLC installer. A Python-only adaptation is possible (section 5). |
| swarm | Model line | Covered | Host subagents and workflows. |
| tdd | No | Covered | `develop` ([testing reference](../../skills/develop/references/testing.md)) and `diagnose`. |
| teach | Points at new `why` | Covered | `research`. |
| technical-writing | Cut from 106 to 70 lines | Not worth it | Not evaluated. It overlaps `unslop`, whose gain held only on the suite rubric, and a team's style guide belongs in its own `AGENTS.md`. |
| typescript-best-practices † | No | Covered; adapt one idea | `develop`. As published, Claude Code never offers it, by name or on its own: its `paths:` glob hides it in all 18 runs, and one run found the file and read it anyway. With that line removed, by name, it beats no skill (8/9 suite, 9/9 outcomes) but not `develop` (4/9, 5/9). It wins the state-modeling case 3-0-0 against both and loses the boundary case to `develop`. Worth testing in `develop`: model variant state as a discriminated union. |
| unslop † | Cut from 62 to 40 lines: one line per rule, examples gone | Not worth it | No pack owner and no built-in, but by name it wins only on the suite rubric (8/9); on outcomes it is 6/9 against no skill. It cleans PR descriptions a little better and drops facts from release notes. Sonnet already does this job without it. |
| why | One file, 9 lines | Covered | `research` (history and rationale with citations). |

The 24 principles do not justify installed entrypoints of their own; each has an owner. Most were shortened in #1249 without behavior checks.

| Principle | Owner |
| --- | --- |
| attack-the-premise, fix-root-causes | `diagnose` |
| boundary-discipline, type-system-discipline † | Installed beside `typescript-best-practices` in its runs; `develop` for the job. Not evaluated on their own. |
| build-the-lever, encode-lessons-in-structure | Pack maintenance rule in `AGENTS.md` |
| exhaust-the-design-space, experience-first, foundational-thinking, model-the-domain, redesign-from-first-principles | `shape-change` |
| explain-the-number | `diagnose` performance reference |
| guard-the-context-window | Host behavior (subagents, summaries) |
| laziness-protocol, minimize-reader-load, subtract-before-you-add | `simplify-code`, `develop` |
| make-operations-idempotent, separate-before-serializing-shared-state | `review-change`; the verification draft for races |
| migrate-callers-then-delete-legacy-apis, outcome-oriented-execution, sequence-verifiable-units | `develop`, `shape-change` |
| never-block-on-the-human | Rejected as an absolute rule (first review) |
| prove-it-works, test-behavior-not-implementation | `develop` testing reference |

**For TypeScript, React, Next.js and Effect teams.** pstack has one TypeScript-specific skill (`typescript-best-practices` and its two principles) and nothing specific to React, Next.js or Effect. `blast-radius` mentions React and Solid teardown timing in one line. The TypeScript skill's "schemas before guards" rule names Zod but says to use the repository's own schema library, which in an Effect codebase means Effect Schema; its Zod example is out of date for Zod 4 ([#1165](https://github.com/cursor/plugins/issues/1165)). Its frontmatter sets `disable-model-invocation: true` and a `paths:` glob, so it does not load on its own in Claude Code (measured below); a team would have to invoke it by name or restate it in `AGENTS.md`.

## 4. Evaluations

**Why these three.** They are the most-installed pstack skills (section 2), and each does a daily job for a TypeScript team: writing TypeScript, judging a small change, cleaning up prose. The other entrypoints either have a clear owner already or are not daily jobs.

**Setup.** Claude Code 2.1.332, Sonnet, 3 repeats per case. Each skill was copied from the new pin into eval workspaces outside the repository; each suite's `spec.md` records the SHA-256 of every file tested. Conditions: `without` (no skill) and `named` (invoked by name). All three skills set `disable-model-invocation: true`, so the host never loads them on its own. `with` (installed, the host decides) ran only for `typescript-best-practices`, to see whether its `paths:` glob loads it when a `.ts` file is edited. It never did. The pack skill that owns the job ran by name on the same cases: `develop` for the TypeScript cases, `review-change` for the blast-radius cases. Opus judged each pair blind in both orders, and a win counts only when both orders agree. Each comparison was judged twice: on the suite rubric, and with `--outcome-only`, which ignores how the answer reports its work. Intervals are 95% Wilson intervals on wins or ties.

| Suite (3 cases, 9 pairs) | Comparison | Suite rubric: W-T-L, wins or ties | Outcome only: W-T-L, wins or ties |
| --- | --- | --- | --- |
| `typescript-best-practices`, `paths:` line removed | named vs no skill | 6-2-1, 8/9 (89%, 56–98%) | 5-4-0, 9/9 (100%, 70–100%) |
| | named vs `develop` named | 3-1-5, 4/9 (44%, 19–73%) | 3-2-4, 5/9 (56%, 27–81%) |
| | `develop` named vs no skill (reference) | 6-1-2, 7/9 (78%, 45–94%) | 5-2-2, 7/9 (78%, 45–94%) |
| `blast-radius` | named vs no skill | 9-0-0, 9/9 (100%, 70–100%) | 5-0-4, 5/9 (56%, 27–81%) |
| | named vs `review-change` named | 9-0-0, 9/9 (100%, 70–100%) | 6-1-2, 7/9 (78%, 45–94%) |
| | `review-change` named vs no skill (reference) | 8-1-0, 9/9 (100%, 70–100%) | 3-4-2, 7/9 (78%, 45–94%) |
| `unslop` | named vs no skill | 3-5-1, 8/9 (89%, 56–98%) | 2-4-3, 6/9 (67%, 35–88%) |

Automated checks and cost per run (mean):

| Suite and condition | Checks passed | Loaded | Cost | Seconds |
| --- | --- | --- | --- | --- |
| `typescript-best-practices` as published: without / with / named | 4/9, 5/9, 5/9 | 0, 0, 1 of 9 | $0.10 | 20 |
| `typescript-best-practices`, `paths:` removed: without / with / named | 6/9, 4/9, 7/9 | 0, 0, 9 of 9 | $0.09 / $0.10 / $0.11 | 20–23 |
| `develop` named on the TypeScript cases | 7/9 | 9 of 9 | $0.10 | 21 |
| `blast-radius`: without / named | 9/9, 9/9 | 0, 9 of 9 | $0.08 / $0.13 | 18 / 36 |
| `review-change` named on the blast-radius cases | 9/9 | 9 of 9 | $0.09 | 20 |
| `unslop`: without / named | 9/9, 9/9 | 0, 9 of 9 | $0.06 / $0.07 | 8 / 9 |

**What the cases show.**

- **`typescript-best-practices` helps with state modeling and nothing else measured.** On `orders-retry-state` it won all three pairs against no skill and against `develop`: every named run replaced the bag of optional fields with a discriminated union, so a stale error could not outlive a successful reload. No-skill and `develop` runs often kept the bag, and 1 of 3 no-skill and 2 of 3 `develop` runs failed the hidden reload test. On `webhook-boundary`, `develop` won 3-0-0: two of the three named runs rejected `amount_cents: 0`, which the contract allows, and one of them also accepted a lowercase currency, which it does not (hidden tests 1/3 against `develop`'s 3/3). On the one-line `pagination-small-fix`, no run over-engineered; `develop` won on adding a regression test. Installed and left to the host, it never loaded, so a team gets nothing from it unless they type its name.
- **`blast-radius` writes a better report, not a better finding.** Every condition found the planted breakage in every run (all checks pass). The suite-rubric wins come from stating the deciding fact and the run that proves it. On outcomes, no skill won 4 of 6 pairs on the two breakage cases, for concision. Its outcome lead over `review-change` comes mostly from `safe-eviction`, and that case favors it: the skill's own example of a safety fact ("this call only drops already-dead cache entries") has the same shape as the fixture, which was written after reading the skill. Without that case, it is 4 of 6 wins or ties against `review-change` and 2 of 6 against no skill. It takes about twice as long per run.
- **`unslop` matches what Sonnet already does.** Edits were nearly the same size with or without it, all literals survived in all runs, and nobody rewrote the user's own sentence in the typo near miss. It cleaned the PR description slightly better (2-0-1 on outcomes) and lost on the release notes (0-1-2), where named runs dropped a stated reason or left a fragment that no longer said the flag was removed.

**Harness problems found and fixed on the way.** Results from before each fix are not used.

- Claude Code on Windows offers a `PowerShell` tool that the eval allowlist never permitted. In the first `blast-radius` runs, named runs had about 30 refused PowerShell commands, mostly the `node` and `python` probes the skill asks for. The harness now removes that tool (`--disallowedTools PowerShell`), so agents use Bash, where the allowlist applies. Five earlier results files also record refused PowerShell commands (for example 12 in `h2h3-diagnose-pack-v2`); those comparisons had the same handicap on both sides, but it cost more to the skills that run things.
- The allowlist now permits `node`, `npm test`, `head`, `tail` and `grep`, so TypeScript fixtures can run their tests and pipe the output. Before, most TypeScript runs could not run any test.
- Stopping a judge script left its judge processes running, and they appended to verdict files that were being rewritten. Every affected verdict file was deleted and judged again. All 14 committed verdict files have 9 pairs, no duplicates and no judge errors.
- Judging the same TypeScript pairs twice moved the suite tally from 7-0-2 to 6-2-1. With nine pairs, one verdict moves a rate by 11 points.

Files: [`eval/typescript-best-practices`](../../eval/typescript-best-practices/), [`eval/blast-radius`](../../eval/blast-radius/), [`eval/unslop`](../../eval/unslop/), and the `pstack2-*` files in [`eval/results`](../../eval/results/). The as-published TypeScript runs are kept as `pstack2-typescript-as-published-claude-sonnet.jsonl`, unjudged.

## 5. The two specific questions

### Can `statechart` work without its TypeScript runtime, Java/TLC installer and POSIX process handling?

Yes, for most of what a reader uses, by splitting the work differently. What `statechart` does today: run TLC with `-tool` framing, re-run it with each broken rule removed until none breaks (bounded at 100,000 states), dump the full state graph with `-dump dot,actionlabels`, collapse model states into reader labels with an executable JavaScript view module, mark states that break or may break each rule, and write `chart.mmd` and a report. That is 3,980 lines of TypeScript ([scripts](https://github.com/cursor/plugins/tree/b7b93c36be9bcc36a74db438e0fd385d660bc559/pstack/skills/statechart/scripts)) with 33 recorded corpus cases.

A portable adaptation:

1. **Checker: everystate instead of TLC.** [everystate](https://github.com/mattzcarey/everystate) is a Rust TLA+ checker with TLC's command line, output and exit codes (0 pass, 11 deadlock, 12 invariant, 13 liveness, 150/151 parse errors), `-json` (status, counts and the shortest `{action, state}` trace on the last line) and `-dump dot,actionlabels`. No Java. The agent runs it, pinned: `npx --yes everystate@0.4.1 -json Spec.tla`. The skill's own scripts never touch the network or start processes, so there is no process-group handling to port.
2. **Renderer: one read-only Python script.** `trace_to_mermaid.py` reads the `-json` result and, when present, the DOT dump, and writes a Mermaid `stateDiagram-v2`: the shortest bad path for a violation, or the whole graph under a state budget. Reader labels come from a declarative JSON map (variable values to label, action to step label), not executable view modules, so no code from the model author runs.
3. **Re-runs for every rule** stay with the agent: the skill tells it to remove a broken invariant from a copy of the `.cfg` and run again, and to list rules it did not check.

What is lost against upstream: parent states and parallel regions, `mayBreak` marks for merged states, the automatic per-rule re-run loop, Pele rendering, and 33 corpus regressions and differential tests against TLC. A first version should cover flat charts and bug paths only.

What is unknown. everystate is 16 days old (created 12 November 2026, v0.4.1, one maintainer, 267 stars). Its [conformance notes](https://github.com/mattzcarey/everystate/blob/main/CONFORMANCE.md) claim 122/122 matches on the tlaplus Examples, 383/414 on TLC's own test models, and that pstack's unmodified statechart corpus gives byte-identical output (33/33) with everystate standing in for Java. Those are the author's claims; none was reproduced here, because doing so means installing the package. `npx` also downloads a native binary at use time, so a project should pin the version.

**Building it was requested later and stopped at step 1.** The plan was: run everystate on upstream statechart's recorded corpus (including the #741 broken variants and #982's `CounterInstance`) and compare verdict, state counts and shortest bad trace with the recorded TLC output; only if they matched, prototype `drafts/statechart-everystate/` (instructions plus a read-only Python JSON-to-Mermaid script) and evaluate it on double-submit, double-send retry and lease-race fixtures against no skill and against model checking without a diagram. Step 1 needs everystate downloaded and run (`everystate@0.4.1`: registry tarball, about 19.8 MB unpacked, MIT, no dependencies, no install scripts). Permission to download and run it was asked for on 28 November 2026 and not given, so nothing was downloaded, and no prototype or evaluation exists. The next attempt starts at step 1, with that permission.

Fit with this pack's rules: Python-only scripts, no network in scripts and nothing outside the skill folder all hold. The skill does need the network once, through the agent, to fetch the checker; say so in its description. It belongs as part of the by-name verification skill, not as a separate statechart entrypoint: a chart is one way to report a counterexample, and the first review already found that a counterexample can be explained without a renderer. The personal `formal-verification` skill does the checking half; it was not copied or evaluated here.

### What would a by-name verification skill built on `drafts/verification-skill/` need to ship?

1. **A recurring job.** `CONTRIBUTING.md` asks for sweeps and reports from more than one person showing that people ask for a reusable verification recipe or a model check. None exists yet. This is the main blocker, and it is not one more prompt can fix.
2. **The entrypoint.** One `SKILL.md`, by name only (`disable-model-invocation: true` and `policy.allow_implicit_invocation: false`), with two modes that share one record: *runtime recipe* (start, drive, evidence, cleanup) and *property check* (model or generated-input tests tied to code). Upstream splits this into four skills; one owner is enough here.
3. **Two scripts, both read-only Python.** `check_anchor.py`: read the project's verification record (covered paths, last confirmed commit per check) and report which covered files changed since each anchor, with `git diff --name-only`. `scaffold_verify.py`: write the project-local `verify-<name>/SKILL.md` and record from a template; writing is its job, so it may write, but only inside the project.
4. **A template** for the generated recipe and record: owned instance, readiness beyond an open port, public-path drive, evidence kept through cleanup; for checks, property, covered symbols, bounds, tool and command, deliberate-failure check, anchor.
5. **Checker choice.** everystate as the default for event-order models (no Java), the project's own property-testing library for code-level checks, and an explicit statement when neither exists. The `trace_to_mermaid.py` renderer above is optional and should ship only if a case uses it.
6. **Cases, run against no skill in both hosts.** The existing [verification-practice fixtures](../../eval/verification-practice/) give four: the Python lease model whose stale atomic model still passes (drift and a real duplicate-claim bug), the blocked second check that must keep its old anchor, generated tests that must call the shipped JavaScript range function rather than a copy, and the Notes API whose health check answers before the list does. Add the near miss (an agreed one-line log label change that needs no new check) and a TypeScript lease or retry case for the teams that install this pack. Upstream's measured gains point at what to test: shipped code instead of a surrogate ([#721](https://github.com/cursor/plugins/pull/721), 9/9 against 3/9) and blocked anchors kept ([#716](https://github.com/cursor/plugins/pull/716), 9/9 against 0/9), while correctness itself did not improve in #716.
7. **The bar.** At least 70% wins or ties against no skill on its rubric, with the outcome-only re-judge and intervals; a Codex run; the validator and tests. Until then it stays in `drafts/`.

## 6. What this evidence cannot show

- **Synthetic, small cases.** Three cases per candidate, three repeats, one host (Claude Code), one model (Sonnet), one judge model (Opus, a sibling of the tested model). The 95% intervals are wide.
- **No real sessions.** Install counts and issues show people install and run these skills; they do not show what the skills change in their work. Nothing here measures the time, cost or defect rate of real work.
- **No Codex.** The pack's skills run in Codex too; these candidates were not measured there.
- **Upstream skills ran as published, outside their system.** `typescript-best-practices` normally loads under `poteto-mode` with its principles; `blast-radius` suggests running `arena`, which was not installed. Results apply to the skill as a team would install it from skills.sh, not to pstack as a whole.
- **No type checker.** The TypeScript fixtures run on Node's type stripping; type quality was judged, not compiled.
- **Nothing in pstack was executed**, including `statechart` and everystate. Their test and conformance claims are reported, not reproduced.
