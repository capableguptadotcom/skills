# Writing a skill

Use this guide when you add a skill or make a real change to one. It combines the public guidance ([Claude's skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices), the [Agent Skills specification](https://agentskills.io/specification) and [Codex's guide](https://learn.chatgpt.com/docs/build-skills)) with what this pack's evaluations taught us. The validator (`scripts/validate.py`) checks the mechanical rules. The rest is up to you and the reviewer.

## 1. Earn the place first

A skill exists to fix something an agent gets wrong without it. Before writing anything:

1. **Name the job and the failure.** For example: "Asked why a test is flaky, the agent guesses a cause and never reruns the test." Get it from a `skill-feedback` report, a sweep, or a correction you keep making. If you can't name a failure, stop.
2. **Check it isn't already covered.** It shouldn't be covered by a skill in this pack, a host built-in (`/code-review`, `/simplify`, `/debug` in Claude Code), or a line in a project's `AGENTS.md`. If a pack skill owns the job, improve that skill instead.
3. **Write the cases before the skill.** See [step 6](#6-evaluate-before-and-after). Run them with no skill. If the agent already passes, the skill has nothing to add.

The bar a skill must clear to ship is in [CONTRIBUTING.md](../CONTRIBUTING.md#when-a-skill-earns-a-place).

## 2. Folder layout

```text
skills/<name>/
  SKILL.md              required: frontmatter and instructions
  references/*.md       guidance read only when a step needs it
  assets/*.md           output templates the answer follows
  scripts/*.py          deterministic helpers the agent runs
  agents/openai.yaml    Codex settings, required for skills that run only by name
```

| Put it in | When | Example in this pack |
| --- | --- | --- |
| `SKILL.md` | Steps every use needs | `diagnose`'s seven steps |
| `references/` | Detail that only some uses need. Link it from the step that needs it, one level deep: no reference links to another. | `diagnose/references/performance.md`, read only for slowdowns |
| `assets/` | The shape of the answer, when it must be consistent | `review-change/assets/findings.md` |
| `scripts/` | Work that must be exact or repeatable, and that prose would leave to chance | `review-change/scripts/diff_context.py`, `skill-feedback/scripts/sanitize_check.py` |

Rules the validator enforces:

- No links outside the skill's folder.
- Scripts are Python, never use the network, and are read-only unless writing is the skill's job.
- No `package.json`, `requirements.txt` or tool-server config.
- No personal paths.

A file stays only if an evaluation case exercises it.

## 3. Name and description

The description is the only part the agent sees before it decides to load a skill. It decides when the skill runs.

- **Name.** Lowercase words joined by hyphens, at most 64 characters, matching the folder. It must not collide with a host built-in (the validator keeps a reserved list). Use the job's name (`review-change`), not a vague one (`helper`, `utils`).
- **Description.** At most 400 characters here: the specification allows 1,024, but every installed skill's description sits in every session. Write it in the third person ("Reproduces before fixing...", not "I can help..."). Say:
  - **When** it applies, with the words people actually use: "an error, a failing or flaky test, a wrong result, a crash, a slowdown".
  - **Edge cases that should still trigger it**: "including when the user already names a suspected cause or asks for no changes".
  - **What it does differently**: "Reproduces before fixing, tests competing causes".

Every description change needs a selection check. Wording decides loading: adding "asks for no changes" to `diagnose` took one case from loading in 10 of 20 runs to 18 of 20.

## 4. Instructions

- **Numbered steps, each with a check.** End each step with how the agent knows it is done: "you have run it and seen it fail, or you state why you cannot." A step without a check gets skipped.
- **Give a default, not a menu.** "Use X. If X cannot run, use Y." Leave detail open where many approaches work, and give exact commands where one mistake breaks the result.
- **Scale the output to the problem.** A one-cause bug needs a few lines, not a table. Telling `diagnose` and `review-change` this made their reports 20 to 25% shorter with no loss on the rubric.
- **Don't make the agent repeat itself.** `shape-change` lost interviews when it restated the whole plan every turn. Replying with what was settled plus the next question fixed that.
- **Say what not to do** only for mistakes you have seen. Each rule costs attention.
- **Stay under 500 lines** (the validator enforces this). Every skill here is under 80 lines. When a section grows, move it to `references/`.
- **Keep it portable.** It must work in Claude Code and Codex. No model names, no subagent counts, no paths outside the skill.

## 5. How it runs

- **Automatically** (the default): the agent loads it when a request matches the description. Use this for everyday jobs.
- **By name only**: for skills with side effects, or ones people want only on request (`handoff`, `simulate-discussion`). Set both `disable-model-invocation: true` in the frontmatter and `policy.allow_implicit_invocation: false` in `agents/openai.yaml`. The validator fails if only one is set.
- **Hidden from installs**: `metadata: {internal: true}` keeps the skills CLI from installing it unless `INSTALL_INTERNAL_SKILLS=1` is set. `skill-feedback` uses this because it is for maintainers only.

## 6. Evaluate before and after

Each skill has `eval/<name>/spec.md` and `eval/<name>/cases.json`.

- **`spec.md`** states the job, the output, and what the skill must and must not do.
- **`cases.json`** contains:
  - a rubric for the judge, plus an outcome-only rubric that ignores how the report reads;
  - cases, each with:
    - `fixture`: a small synthetic project;
    - `prompt`: the request, as a person would type it;
    - `kind`: `behavior` (does the work), `selection` (loads on its own, or correctly doesn't for a near miss) or `conversation` (several turns with a simulated user);
    - `judge_truth`: what a good answer contains;
    - `checks`: automated assertions such as files changed or left alone, text that must appear, and hidden tests that must pass.

Cover at least three cases: the core job, a harder version, and a near miss that should not trigger the skill or should leave something alone.

```sh
python scripts/run_evals.py run <name> --host claude --repeats 3
python scripts/run_evals.py run <name> --host codex --repeats 3
python scripts/run_evals.py judge eval/results/<file>.jsonl --pair named without --both-orders
python scripts/run_evals.py judge eval/results/<file>.jsonl --pair named without --both-orders --outcome-only
```

Each run tries three conditions: `without` (no skill), `with` (installed, the host decides whether to load it) and `named` (invoked by name). The judge sees two answers without knowing which is which, in both orders, and a win counts only when both orders agree.

Read the results honestly:

- **A single run is a smoke test.** Claim an improvement only against a no-skill or previous-version baseline.
- **Report the interval**, not only the rate.
- **Check the outcome-only re-judge.** If the skill wins only on the suite rubric, it improves the report, not the work. Say so.
- **For a change to an existing skill**, add the case that shows the problem and confirm it fails before the change and passes after.

## 7. Checklist for the PR

- [ ] The failure it fixes, stated in one sentence, with where it came from.
- [ ] Nothing in the pack or the host already does it.
- [ ] Description: when, with real trigger words, in the third person, under 400 characters.
- [ ] Steps each end with a check. Defaults, not menus. Output scaled to the problem.
- [ ] Every reference, asset and script is used by a case.
- [ ] Results against no skill in both hosts, with the interval and the outcome-only re-judge.
- [ ] `python scripts/validate.py`, `python -m unittest discover -s tests -v` and `git diff --check` pass.
- [ ] A `CHANGELOG.md` entry with the evaluation summary.

## Candidates we looked at

Skills that have been discussed, and where each one stands. A candidate moves into the pack by going through the steps above.

| Candidate | Where it came from | Status | Why |
| --- | --- | --- | --- |
| `grill-me` | Personal skill | Not in the pack. `shape-change` covers the job. | In conversations with a simulated user, the two are even (4 wins, 1 tie, 4 losses), and neither clears 70% against no skill. No evidence to retire or replace either. Keep using it personally if you prefer it, but don't install both in one project. See [open decisions, part 4](open-decisions.md). |
| `grill-with-docs` | Personal skill | Not evaluated | A short wrapper that runs another interview skill and also writes decision records and a glossary. The interview part is `shape-change`'s job. Writing the documents would need its own cases first. |
| Formal verification (create and maintain a model check) | Upstream pstack | Drafted, not shipped | Its guidance waits in [drafts/verification-skill](../drafts/verification-skill/). Still missing: evidence that people ask for it, the entrypoint, `check_anchor.py` and `scaffold_verify.py`, a template, and cases run against no skill. The [second review](research/pstack-second-review.md#what-would-a-by-name-verification-skill-built-on-draftsverification-skill-need-to-ship) lists each. It should be a skill you ask for, not one that loads in every session. |
| `formal-verification` (everystate) | Personal skill | Not evaluated | Model-checks a small TLA+ model with `everystate` (`npx everystate`, no Java) and reports counterexamples in the code's terms. It is the most practical way into the formal-verification draft above. Next step: verification cases (a lease race, a retry that sends twice), run against no skill. |
| `statechart` | Upstream pstack | Not adopted; adaptable | Turns model-checker output into diagrams. Upstream is still a 3,980-line TypeScript compiler that installs Java and TLC; it now claims native Windows support, untested on Windows. A portable version would run everystate (`-json`, `-dump dot`) and render with one read-only Python script, as part of the verification skill. [Approach](research/pstack-second-review.md#can-statechart-work-without-its-typescript-runtime-javatlc-installer-and-posix-process-handling). |
| `typescript-best-practices` | Upstream pstack | Not adopted. `develop` covers the job. | Beats no skill (8/9 suite, 9/9 outcome-only) but not `develop` (4/9, 5/9). Its one clear win is modeling variant state as a discriminated union; test that inside `develop`. As published it never loads in Claude Code (its `paths:` glob hides it). [Results](research/pstack-second-review.md#4-evaluations). |
| `blast-radius` | Upstream pstack | Not adopted. `review-change` covers the job. | Beats no skill and `review-change` on the suite rubric (9/9 each) but not no skill on outcomes (5/9); it costs about 1.5 times as much. Worth testing in `review-change`: name the one fact the verdict rests on and check it against real code. [Results](research/pstack-second-review.md#4-evaluations). |
| `unslop` | Upstream pstack | Not adopted | No owner in the pack, but it wins only on the suite rubric (8/9); outcome-only 6/9 against no skill. Sonnet already does this job. [Results](research/pstack-second-review.md#4-evaluations). |
| `reframe` | Upstream pstack, new in November 2026 | Not evaluated | Prose-only, but unmeasured upstream (three runs, no baseline), needs web access to check citations, and no one in the pack's teams has asked for the job. |
| `exhaust-the-design-space` | Upstream pstack | Folded into `shape-change` | Comparing materially different caller examples before a big interface choice is in `shape-change`'s [design reference](../skills/shape-change/references/design.md). Literally exhausting every option was rejected. |
| `open-pr` | This pack's roadmap | Not yet built | Needs a recurring failure and cases first. |
