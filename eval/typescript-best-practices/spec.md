# typescript-best-practices (pstack candidate): specification

A candidate, not a pack skill. The skill under test is upstream pstack's `typescript-best-practices` with its two principle peers (`principle-type-system-discipline`, `principle-boundary-discipline`), copied from [cursor/plugins at b7b93c3](https://github.com/cursor/plugins/tree/b7b93c36be9bcc36a74db438e0fd385d660bc559/pstack/skills/typescript-best-practices) into eval workspaces outside this repository. See [the second review](../../docs/research/pstack-second-review.md).

**Job.** Write TypeScript whose types make bad states and unchecked external data impossible, in proportion to the change.

**Must.**

- Model state that has variants so a contradictory or stale state cannot be represented.
- Parse external data (`JSON.parse`, request bodies) at the boundary into checked domain types; no `as` cast over unchecked data.
- Update every caller of a changed type.

**Must not.**

- Turn a one-line fix into a type refactor, or touch code the task did not name.

**Hosts.** Claude Code (measured). Codex not measured.

**Cases.** Three synthetic TypeScript fixtures under `eval/fixtures/ts-*`, with hidden behavior tests in `hidden/` run by Node's type stripping (`node --experimental-strip-types`). No type checker is installed, so type quality is judged, not compiled.

- `orders-retry-state`: add a retry state to an optional-field state bag whose `error` is never cleared, so a successful retry still shows the error.
- `webhook-boundary`: a webhook handler casts `JSON.parse` output; a string amount corrupted the ledger.
- `pagination-small-fix`: a `Math.floor` that should be `Math.ceil`, beside an `any`-typed legacy file to leave alone. The near miss.

**Files tested.** SHA-256 of the upstream files at b7b93c3, as stored in Git (LF line ends); the copies tested were the Windows checkout of the same files (CRLF).

- `typescript-best-practices/SKILL.md` `ec1dac086d3708e5940d45d250c30a37dd953b4e3cb2ca0692f5851d7a039e27`. The main runs removed only its `paths: ["**/*.ts", "**/*.tsx"]` line, because Claude Code never offers the skill with it (see the as-published runs); that copy is `827145b1bd795b2b03ba0d1ca6087fe20c37aacd1b367e6a37c87ce4a2b4a6bf` (LF).
- `typescript-best-practices/references/patterns.md` `12e70c9419a8b3f5d6a1ab80e272c1f00a43ac0b3bbf72d68199033570e5de77`
- `principle-type-system-discipline/SKILL.md` `9cd1ce345bc9d666c73c64c89c89164217b659aa4c4dde5600cbbe6f6e775461`
- `principle-boundary-discipline/SKILL.md` `c02c26cca3906bfd57829535f8fa7ee9e00df037b4dbb24e5f85ec9e12710b48`
