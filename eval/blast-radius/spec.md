# blast-radius (pstack candidate): specification

A candidate, not a pack skill. The skill under test is upstream pstack's `blast-radius`, copied from [cursor/plugins at b7b93c3](https://github.com/cursor/plugins/tree/b7b93c36be9bcc36a74db438e0fd385d660bc559/pstack/skills/blast-radius) into eval workspaces outside this repository. The pack's owner of the job is `review-change`, which runs on the same cases for comparison. See [the second review](../../docs/research/pstack-second-review.md).

**Job.** Find what a small change breaks outside its diff, and say plainly when it breaks nothing.

**Must.**

- Look past the type checker and a symbol search: other languages reading the same bytes, saved data, appended files, API consumers.
- Rest the verdict on the fact that decides it, checked against real code where cheap.
- Leave every project file unchanged. Scratch scripts outside the project are fine; `paths_unchanged` checks only project paths.

**Must not.**

- Invent breakage on a safe change.

**Hosts.** Claude Code (measured). Codex not measured.

**Cases.** One synthetic TypeScript orders service (`eval/fixtures/ts-orders-service`) with a change from `eval/fixtures/ts-orders-service-changes` committed on a `feature` branch. Every change keeps the TypeScript tests green.

- `epoch-breaks-report`: `placedAt` becomes epoch milliseconds; the unchanged Python finance job parses it as an ISO string and crashes.
- `rename-breaks-saved-data`: `"canceled"` becomes `"cancelled"`; saved records still use the old spelling, so the orders page throws and the report undercounts.
- `safe-eviction`: eviction on read instead of on a timer. Safe, because evicted entries are exactly those `get()` already ignores. The trap is inventing a defect.

**Files tested.** `blast-radius/SKILL.md` at b7b93c3, SHA-256 `4248d03e22365207d2e5f90c9542720f80a88a6b42fd542ef88dde3cf9f9223f` as stored in Git (LF); the copy tested was the Windows checkout (CRLF). It mentions `arena`, `how`, `why` and `unslop`, which were not installed.

**Known bias.** `safe-eviction` was written after reading the skill, and the skill's own example of a safety fact ("this call only drops already-dead cache entries") has the same shape. Read results with and without that case.
