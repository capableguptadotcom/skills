## Skill problem: <skill> — <one-line summary>

**Skill and version:** <name> @ <commit or hash from skills-lock.json>
**Host and model:** <Codex or Claude Code, version> · <model>
**Class:** wrong trigger / wrong instruction / missing depth

### What happened

- **Asked:** <the request, generalized>
- **The skill led the agent to:** <behavior>
- **Correction:** <what the user had to say or undo>
- **Expected:** <what should have happened>

### Synthetic case

```json
{
  "prompt": "<a neutral prompt that reproduces it>",
  "setup": "<tiny fixture, or none>",
  "expect": "<observable correct behavior>",
  "must_not": "<the behavior that went wrong>"
}
```

### Suggested fix

<description wording, instruction change, or the reference / script / template that was missing>

<sub>Drafted with skill-feedback. Sanitized: sanitize_check passed.</sub>
