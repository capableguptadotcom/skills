# unslop (pstack candidate): specification

A candidate, not a pack skill. The skill under test is upstream pstack's `unslop`, copied from [cursor/plugins at b7b93c3](https://github.com/cursor/plugins/tree/b7b93c36be9bcc36a74db438e0fd385d660bc559/pstack/skills/unslop) into eval workspaces outside this repository. No pack skill or Claude Code built-in owns the job. See [the second review](../../docs/research/pstack-second-review.md).

**Job.** Rewrite prose (a PR description, release notes) so it reads plainly, keeping every fact.

**Must.**

- Keep every fact, number, caveat, command, code block and quotation.
- Leave literal text (error messages, commands, quotes) byte-identical, even when it contains words a style rule would flag.

**Must not.**

- Rewrite text the request did not cover.

**Hosts.** Claude Code (measured). Codex not measured.

**Cases.** Three synthetic prose fixtures under `eval/fixtures/prose-*`.

- `pr-description`: an AI-sounding PR description with seven facts to keep, among them a latency result and an untested-browser caveat.
- `release-notes-literals`: padded release notes whose code block holds an error message with "crucial" and an em dash, plus a quotation. Literals must survive.
- `typo-only`: fix one typo in a file whose first sentence a rule list would flag. The near miss.

**Files tested.** `unslop/SKILL.md` at b7b93c3, SHA-256 `2b823fd069e031c1420180be8e0d4f5e2fd25bf2c428049e5c835c59a489b5e0` as stored in Git (LF); the copy tested was the Windows checkout (CRLF).
