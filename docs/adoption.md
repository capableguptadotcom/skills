# Host setup and migration

This repository keeps the ordinary `skills/<name>/SKILL.md` shape. Each `kp-` skill can be used independently. `kp-start` lists optional peer skills and has a fallback when one is unavailable; installing only the router does not install its peers.

Install selected folders using the [skills CLI](https://github.com/vercel-labs/skills) or the host's documented skill location. In current Codex guidance, selection can be explicit (`$kp-review`) or implicit through descriptions. Names are not merged across installed copies. See [official skill documentation](https://learn.chatgpt.com/docs/build-skills).

If a project wants persistent routing, its maintainer may add this instruction to the existing `AGENTS.md` or host equivalent:

> For a new software task or a change in intent, consult `kp-start` if it is available. Preserve settled decisions, the user's chosen skill, scope and existing authorization. Handle clear small edits directly and skip unrelated conversation. Load only the specialist needed for the current activity. If a peer is unavailable, disclose that once and proceed with available tools.

Choose one applicable instruction location per host. This repository does not edit global instructions or install every source. No machine-wide skill installation was performed as part of the initial audit. Avoid a second persistent router from another pack in the same project unless its boundary is explicit.

For an existing collection, map its familiar activity names to the corresponding `kp-` names in the README. Keep stack-specific plugins where their tools are needed, and remove a redundant installed copy only after inspecting which projects depend on it. Starting a fresh session helps verify discovery after installation.

Test an idea request, a diagnosis-only request, a review-only request, a settled implementation, and an ordinary nontechnical question. Confirm both the selected activity and the actual file/external side effects. A correct menu choice is weaker evidence than completing the task within scope.

Markdown portability does not establish tool portability. Supply the actual browser, shell, tracker, design, or review integration in each host. Adapt commands to that environment rather than inventing APIs from examples.
