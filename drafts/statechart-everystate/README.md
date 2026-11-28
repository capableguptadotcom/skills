# statechart-everystate (draft, not installable)

A portable take on pstack's `statechart`: model-check a small TLA+ model with [everystate](https://github.com/mattzcarey/everystate) instead of TLC, and draw the counterexample as a Mermaid statechart with a short Python script. No Java, no TypeScript runtime, no process handling in the skill.

- `SKILL.draft.md`: the instructions. It is not named `SKILL.md`, so installers ignore this folder.
- `scripts/trace_chart.py`: reads everystate's `-json` result (and optionally its `-dump dot,actionlabels` graph) with a labels file, and prints a Mermaid chart and a numbered bug path. Python only, read-only, no network.

**Dependency.** The agent runs `npx --yes everystate@0.4.1`, so the project needs Node and network access the first time npx fetches the package (about 7 MB; a prebuilt binary for Linux, macOS and Windows, no install scripts). The skill's own script never touches the network.

**Why everystate can stand in for TLC here.** Checked on 28 November 2026 against the 33 recorded TLC 2.19 runs in pstack's statechart corpus (cursor/plugins `b7b93c3`): the same exit code, rule and shortest bad trace in 33 of 33; the same state counts in all 31 where TLC printed counts; and the same reachable state graph, as labeled edges, in 33 of 33. Details in [the second pstack review](../../docs/research/pstack-second-review.md).

**What it leaves out compared with upstream `statechart`:** parent states and parallel regions, `mayBreak` marks for merged states, re-running TLC once per broken rule, and Pele rendering.

**Evaluation and status.** On four synthetic TypeScript flows (Claude Code, Sonnet, 3 repeats), it beat no skill on the suite rubric (12/12) but not on outcomes (3/12). No skill reached the same verdicts and fixes, and the same procedure without the chart did as well (chart vs no chart 5/12 on the suite rubric, 8/12 on outcomes). It stays a draft. The next step is a case where reading the code gives the wrong verdict. See [eval/statechart-everystate](../../eval/statechart-everystate/) and [the review](../../docs/research/pstack-second-review.md#can-statechart-work-without-its-typescript-runtime-javatlc-installer-and-posix-process-handling).
