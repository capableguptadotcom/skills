# statechart-everystate (draft): specification

A draft, not a pack skill: [drafts/statechart-everystate](../../drafts/statechart-everystate/). For evaluation, its `SKILL.draft.md` is copied as `SKILL.md` with `scripts/trace_chart.py` into a folder outside the repository. [`model-check.SKILL.md`](model-check.SKILL.md) is the same procedure with the chart step replaced by a written retelling, so the two isolate what the diagram adds.

**Job.** Answer "can these steps happen in a bad order?" for a small flow, by model-checking it with everystate and reporting the bug path in the product's words.

**Must.**

- Give the right verdict, with the concrete interleaving or failure, and a fix that removes the cause.
- On a safe design, say so and name what makes it safe.
- Edit no product code.

**Must not.**

- Report a double charge, double send or double run that the code prevents.

**Hosts.** Claude Code (measured). Codex not measured. Both variants need Node: the agent runs `npx --yes everystate@0.4.1`.

**Cases.** Synthetic TypeScript fixtures under `eval/fixtures/sc-*`.

- `double-submit-checkout`: `payOrder` reads, checks, awaits the charge, then marks the order paid; two requests both charge.
- `retry-sends-twice`: a timeout that does not cancel the send, and a queue retry after a crash, both resend without the provider's idempotency key.
- `lease-race`: a get-then-set lease; both pods acquire it. The store offers `setIfAbsent`.
- `safe-claim`: the near miss. An atomic claim plus an idempotency key make a double charge impossible; the real risk is an order stuck in "charging".
