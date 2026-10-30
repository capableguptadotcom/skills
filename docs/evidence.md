# Evidence for a curated engineering skills repository

Research snapshot: 2026-10-30. This document separates specification, vendor guidance, author-controlled experiments, and user reports. No benchmarks were rerun in this investigation. Recommendations below are reasoned inferences, not measured results for the proposed personal collection.

## Source identities and important corrections

| User wording | Resolved source | Scope and qualification |
| --- | --- | --- |
| P-stack | [cursor/plugins, pstack/](https://github.com/cursor/plugins/tree/main/pstack) | Lauren Tan/poteto's engineering workflow. This is the original source. Current README includes Cursor and Claude adapters and model-specific routing. |
| P-stack portable alternative | [finografic/pstack](https://github.com/finografic/pstack) | A separate harness-neutral extraction, not the upstream author. Its [UPSTREAM.md](https://github.com/finografic/pstack/blob/master/UPSTREAM.md) pins the original to `60c641e4fad674784b30abcf9f8915dea39df38d` (2026-08-18), explains removed Cursor machinery, and requires manual upstream reconciliation. Track the fork and original as separate sources. |
| R-stack (user-confirmed) | [michaelshimeles/rstack](https://github.com/michaelshimeles/rstack) | Seven development workflows covering worktree isolation, shared code structure, behavioral evidence, screenshots, Greptile loops and writing cleanup. This is distinct from rstackjs/agent-skills, which is excluded from the core review. |
| Ponytail | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | Real named source, not an approximate reference to Superpowers. The current [skill](https://github.com/DietrichGebert/ponytail/blob/main/skills/ponytail/SKILL.md) applies minimal complete changes broadly across coding and persists for a session. |
| Matt Pocock | [mattpocock/skills](https://github.com/mattpocock/skills) | Composable engineering workflows; current distribution includes plugins and editable skills. Its README explicitly advises selecting one installation method per agent to prevent duplication. |
| OpenAI skills | [openai/skills](https://github.com/openai/skills) and [openai/plugins](https://github.com/openai/plugins) | The former now [declares itself deprecated](https://github.com/openai/skills/blob/main/README.md) and points to the latter. Retain the former as historical provenance; inspect the latter for current examples. |
| G-stack | [garrytan/gstack](https://github.com/garrytan/gstack) | Distinct engineering-role workflow collection, a useful additional source if requested; it must not silently replace P-stack. |

The personal destination, confirmed by the main task, is `capableguptadotcom/skills`. Private organization material is not reproduced here. The similarly named `rstackjs/agent-skills` was investigated during disambiguation; its Rspack/Rsbuild skills and two proposed evaluations are outside the user-confirmed R-stack scope and are not used as evidence for michaelshimeles/rstack.

## How skill selection and progressive disclosure actually work

The [Agent Skills specification](https://agentskills.io/specification) defines `name` and `description` frontmatter, followed by instructions and optional resources. Metadata is available first; the body loads on activation; supporting files load as needed. It recommends a main file below 500 lines and instructions below approximately 5,000 tokens. Those are design recommendations, not proof of quality or a universal runtime limit. Its `allowed-tools` field is experimental, so it should not be treated as a portable security control.

[OpenAI's current skill documentation](https://learn.chatgpt.com/docs/build-skills) distinguishes explicit invocation from implicit description matching. It says duplicate names are not merged: both can appear in selectors. Descriptions should lead with the main use case so their important meaning survives host shortening. Repository, user, administrator and system skills can coexist, which makes collision review a whole-environment task rather than a check of a single repository.

[OpenAI's September 2026 guidance](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra) warns that many long descriptions consume the discovery budget and can be shortened, and that overbroad or contradictory descriptions cause unnecessary loading. It recommends minimal routers with references and revisiting elaborate recipes as model capabilities improve. This directly supports a small active collection with a much larger inactive research catalog; it does not establish a magic maximum number of installed skills.

[Anthropic's original engineering explanation](https://www.anthropic.com/research/equipping-agents-for-the-real-world-with-agent-skills) describes the same metadata/body/resources layers. Its context claim concerns selective access to resources, not zero overhead from a huge skill catalog. A folder full of references still needs a clear route and the agent still must actually read and follow the relevant content.

Inference: good progressive disclosure is conditional routing plus evidence that the correct path was followed. Splitting a long file into many fragments without routing tests can increase missed dependencies and indirection.

## Current source-owned successes, failures, and limits

| Evidence | What it supports | What it does not support | Implication for this collection |
| --- | --- | --- | --- |
| [Ponytail #126](https://github.com/DietrichGebert/ponytail/issues/126), closed; maintainer acknowledged the critique | A baseline that returned multiple verbose options inflated the apparent LOC benefit. A commenter changed the baseline prompt, and the maintainer agreed the original comparison was unfair. | It does not prove that minimality instructions have no effect. | Compare with a competent no-skill baseline, plus a short-principle baseline, in the same agent harness. |
| [Ponytail #121](https://github.com/DietrichGebert/ponytail/issues/121), closed; external contributor's reproducible Cursor SDK report | Smaller written output sometimes coincided with more tool calls and higher estimated session cost. Only a few of the indexed skills were read. | The ten finished runs on one task family do not establish universal cost or model rankings; costs were estimated, not billed totals. | Record actual skill reads, successful outcomes, latency and total usage separately from LOC and installed count. |
| [Ponytail agentic benchmark README](https://github.com/DietrichGebert/ponytail/blob/main/benchmarks/agentic/README.md) | The author documents a contaminated baseline caused by a SessionStart hook, and a revised isolation method. Outcomes vary by over-build opportunity. | An author-maintained benchmark is not independent validation for this user's projects or models. | Isolate home skills, project skills, plugins, hooks and settings for each evaluation arm. |
| [Ponytail PR #1317](https://github.com/DietrichGebert/ponytail/pull/1317), open on 2026-10-30 | A contributor found graders that accepted omitted behavior, including tests promised in prose and rate limits that were never applied. The proposed regrade changes recorded verdicts. | An open proposal is not a merged fix, and the reported regrade has not been independently reproduced here. | Test the graders with intentionally wrong outputs. Require executable behavioral evidence rather than keywords or a claimed check. |
| [R-stack #22](https://github.com/michaelshimeles/rstack/issues/22), open | A report tied to commit `ababbf720c1335f258700fd2d060a81aa72bf021` says a queued check with null start time is discarded, allowing an existing score to produce premature `review_ready`. | This investigation has not reproduced the report or confirmed a fix. | Test queued checks and stale scores before trusting automatic review completion. A 5/5 label alone is insufficient. |
| [R-stack #20](https://github.com/michaelshimeles/rstack/issues/20) and [#21](https://github.com/michaelshimeles/rstack/issues/21), open | Two related reports describe a failed pre-posting reservation leaving a zero-byte attempt file that blocks retry. | These are related failure paths, not two independent outcome experiments. | Check recovery and idempotency before letting an updater post or retrigger review comments. |
| [Matt #1319](https://github.com/mattpocock/skills/issues/1319), open/needs triage | A user reports `grill-me` fails when its sibling `grilling` dependency is absent after individual installation. | It does not establish that every installation path is broken. | Validate each distributable skill's referenced files and dependency closure. Test clean single-skill installs. |
| [Matt #1337](https://github.com/mattpocock/skills/issues/1337), open/needs triage | A user provides a specific plugin/model session where a preferred one-question interview style was ignored despite being in context. | The reporter's hypothesis about later instructions winning is not an instruction-priority rule or a proven root cause. | Test user overrides explicitly. Skill defaults must yield to the user's stated preferences. |
| [Matt #1327](https://github.com/mattpocock/skills/issues/1327), open/needs triage | A user reports loss of original requirements during long interviews and suggests compact confirmed-decision checkpoints. | No exact revision, minimal transcript or measured context threshold was recorded; compaction is suspected, not proven. | Evaluate long-session retention and source reconciliation, while labeling this mitigation unverified until tested. |

These issue discussions are more useful than star counts because they identify falsifiable failure modes. Their existence does not imply that a source is worse than a source with no tests or public feedback. An unresolved issue is a candidate evaluation case, not an automatic rejection.


## R-stack-specific scrutiny

The seven skills, in one line each, are:

| Skill | Use and decision concern |
| --- | --- |
| `new-feature` | Creates or preserves task worktree isolation; its [instructions](https://github.com/michaelshimeles/rstack/blob/main/new-feature/SKILL.md) default to `origin/main` and include forced branch deletion after merge, so base selection and cleanup need local policy. |
| `code-structure` | Shares operational logic across workflows; overlaps existing service/module design guidance and should remain narrowly triggered. Original content has no established license grant. |
| `evidence-driven-testing` | Captures observed runtime behavior through recording, headless captures or measured outputs; distinct evidence mechanics, but tool and publication dependencies require an adapter. Original content has no established license grant. |
| `before-and-after` | Produces visual comparisons for review; conditional noncompete license and public upload defaults make it an opt-in reference until terms and destination fit. |
| `greploop` | Iterates against fresh Greptile review of the current revision with a cap and timeout; useful integration profile, not a portable universal completion gate. |
| `greploop-apps` | Thin alternative trigger for large PRs; depends on `greploop`, so avoid a separate competing default workflow. |
| `unslop` | Removes patterns from human-facing writing; this is prose cleanup derived from P-stack, distinct from code simplification despite the name collision. |

The [greploop skill](https://github.com/michaelshimeles/rstack/blob/main/greploop/SKILL.md) already limits iterations, stops on unavailable integration or timeouts, respects the requested scope and forbids chasing a score by changing correct code. Preserve these safeguards in any licensed adaptation. Its issue reports identify implementation checks still worth reproducing. The [evidence skill](https://github.com/michaelshimeles/rstack/blob/main/evidence-driven-testing/SKILL.md) explicitly scales proof to the change and limits publication to requested destinations. Do not turn it into mandatory video recording for documentation edits. Tests listed by R-stack are infrastructure tests with stated coverage limits, not a controlled evaluation of end-to-end skill uplift.

## What “OpenAI research” can mean

The current public plugins tree contains several different research capabilities. [Product Design research](https://github.com/openai/plugins/blob/main/plugins/product-design/skills/research/SKILL.md) investigates UX friction for a named digital product; it depends on a plugin router, critical-overrides reference and user-context/preflight workflow. [Notion research documentation](https://github.com/openai/plugins/tree/main/plugins/notion/skills/notion-research-documentation) organizes research through the Notion environment. The same repository includes a life-science-research plugin and an NVIDIA `aiq-research` skill. None should be silently substituted for a portable generic technical-research workflow.

[Plugin architecture documentation](https://developers.openai.com/plugins/concepts/plugins) separates instructions from optional MCP tools and UI. A skill can work without an MCP server, while a tool-backed plugin can add authentication, controlled actions and live information. Copying only `SKILL.md` does not transfer those capabilities. A compatible Markdown format does not guarantee runtime equivalence.

## Conflicts worth preventing

These are synthesis from the inspected files and documentation, not measured collision rates:

1. **Duplicate discovery:** plugin plus copied skill, two installed copies with the same name, or renamed duplicates with near-identical descriptions. Prefer one installed owner for each workflow and preserve upstream names in provenance, not aliases that all auto-trigger.
2. **Competing workflow owners:** a generic orchestrator, a personal SDLC pack, P-stack mode and Superpowers can all claim routine coding. Select one front door per active profile; use another collection as a reference source or explicit opt-in.
3. **Cross-domain “research”:** product UX, scientific investigation, Notion synthesis and engineering fact checking share a word but differ in goal, tools and evidence. Qualify descriptions around the user goal and environment.
4. **Minimality versus completeness:** Ponytail's current text asks for the smallest complete change and preserves security, validation and accessibility. The vague-request smallest-version default and one-line pressure still need counterexamples where the user's whole goal requires broader work. Keep completeness as the gate; do not optimize only LOC.
5. **Portable instructions versus host machinery:** model panels, native subagent APIs, proprietary tools, hooks, browser sessions and absolute paths need adapters or explicit compatibility. Missing features should not be papered over by simulated execution.
6. **Review and test conflation:** code review, static analysis, runtime tests and an acceptance check provide different evidence. One may route to another, but a finished review is not proof that an application runs.
7. **Automatic upstream overwrite:** a wording change can alter triggers, permissions, persistence, test obligations or dependencies without touching code. New upstream text should enter a candidate area and undergo a semantic review before promotion.

## A practical acceptance bar

[OpenAI's skill evaluation guide](https://developers.openai.com/blog/eval-skills) recommends defining success first, capturing runs and artifacts, checking explicit/implicit/contextual invocation plus negative controls, and using deterministic checks alongside rubric grading. It is a method, not proof that any particular community collection improves outcomes.

Recommended acceptance gates for this repository:

- **Purpose:** one user goal, positive trigger, adjacent negative trigger, and a concrete expected artifact or observable result.
- **Distinct contribution:** document the behavior missing from the model baseline or another installed owner. Absorb a useful sentence into an existing skill when a new skill adds only duplicate metadata.
- **Structure:** parse frontmatter, resolve bundled paths, check dependencies, retain notices, validate platform requirements, and keep the root as a short router where appropriate.
- **Routing:** test explicit requests, implicit requests, near misses and multi-skill collision cases. Log which files were actually read.
- **Behavior:** verify artifacts and invariants, test a deliberately wrong result against each grader, and check that user overrides remain effective.
- **Comparative value:** run paired no-skill, short-principle, upstream and curated arms on held-out tasks under fixed versions/settings. Repeat enough to show variance; report task and run counts rather than overstating small samples.
- **Long work:** exercise interruption, resumption, requirements retention and failure reporting. Check confirmed user constraints against durable source pointers after context reduction.
- **Decision:** classify as active, opt-in profile, candidate/reference, absorbed, or rejected, with reasons and evidence confidence. Do not assign “validated” from static review alone.

Suggested metrics are task success, false activation/missed activation, forbidden actions, regressions, unsupported claims, complete acceptance coverage, time, tokens/cost where available, and user rework. A composite score must never conceal a failed correctness or authority invariant.

## Provenance and license findings

The original P-stack [LICENSE](https://github.com/cursor/plugins/blob/main/pstack/LICENSE) is MIT with Lauren Tan's copyright. The extraction says it retains that notice even though GitHub's automatic license detector returned `NOASSERTION` for the fork; inspect the actual license text rather than relying only on API classification. Ponytail and Matt Pocock carry MIT licenses at the investigated sources. R-stack has no blanket root grant: its [license issue #12](https://github.com/michaelshimeles/rstack/issues/12) specifically calls out the original `new-feature`, `code-structure`, and `evidence-driven-testing` files. Catalog these originals without public vendoring until rights are clear. The vendored `greploop`, `greploop-apps` and `unslop` have MIT notices. Its [before-and-after license](https://github.com/michaelshimeles/rstack/blob/main/before-and-after/LICENSE) is labeled PolyForm Shield and includes an express noncompete condition; do not label it MIT or treat all R-stack content alike. Preserve original notices alongside substantial adaptations, and retain the reviewed commit, path and adaptation record.

OpenAI's historical skills README says licensing is per skill. The current plugins repository has no root blanket license in its recursive tree and only selected packages contain license files. For example, [Notion research documentation's license](https://github.com/openai/plugins/blob/main/plugins/notion/skills/notion-research-documentation/LICENSE.txt) grants permissive rights while retaining Notion's notice; Product Design research has no adjacent license file in the inspected tree. **Do not assume public visibility or an OpenAI namespace licenses every plugin for republication.** Catalog and link uncertain items; resolve the applicable terms before vendoring. Installed proprietary/bundled runtime content should not be copied into a public personal repository without established rights.

## Daily-update policy implied by the evidence

Use daily automation to discover upstream movement and automatically write a structured candidate delta: pinned old/new commits, changed paths, additions/removals, hashes, applicable license changes, referenced dependencies and an evidence summary. Preserve local overrides and never execute fetched scripts merely to inventory them. Test the updater against unchanged sources, errors, deleted paths, force-pushed history and edited local adaptations.

Automatically syncing candidate evidence satisfies freshness; automatically changing active instructions is a separate promotion step. The proposed daily task can prepare a review branch or PR and run deterministic checks. The promotion record should identify which wording was retained, rewritten or rejected and why. If future policy authorizes automatic promotion for a narrow class, define that class with meaningful behavioral gates first. Do not equate a clean Markdown parse with a safe or useful behavioral update.

Remaining uncertainty: these sources and reports justify a curation method, but they do not measure the proposed combined collection on this user's engineering workload. A simulated expert discussion can expose tradeoffs; it cannot substitute for those execution results.
