# Curation and overlap decisions

Reviewed 30 October 2026. These are recommendations from source inspection and explicitly simulated Practitioner/Maintainer/Evaluator discussions. Each candidate's arguments and proposed falsification check are in the catalog and source reports. They are not measured rankings.

## One owner for each activity

| Overlap cluster | Sources and conflict | Owned destination and decision |
| --- | --- | --- |
| Workflow routers | Wellnest-style start, pstack poteto-mode, Matt ask-matt, Superpowers using-superpowers | `kp-start`; preserve settled intent, skip trivial work, and load one useful specialist. Do not install competing broad routers by default. |
| Requirements interviews | Matt grill-me/grilling/grill-with-docs, Addy interview-me, pstack sharpen | `kp-grill-idea`; use the user's pacing, resolve consequential uncertainty, preserve confirmed decisions. |
| Plans and specifications | Matt to-spec/to-tickets, Addy spec/planning/incremental skills, pstack playbooks | `kp-change-plan`; verifiable vertical slices without compulsory tracker publication or a fixed number of agents. |
| Diagnosis | Matt diagnosing-bugs, Addy debugging/doubt/source-driven, Superpowers systematic-debugging | `kp-debug`; reproduction, competing hypotheses, discriminating checks, explicit diagnosis-only scope. |
| Test-first development | Matt/Addy/Superpowers TDD, pstack tdd and test principles | `kp-tdd`; observable red/green behavior when test-first is requested, proportionate checks otherwise. |
| Review | Matt code-review, Ponytail review/audit, pstack interrogate, rstack greploop, CodeRabbit | `kp-review`; one bounded evidence-backed review. Bot loops are optional integrations; a score is not proof. |
| Simplicity before code | Ponytail reuse ladder, pstack principles, existing minimalist approaches | `kp-minimalist`; least machinery that meets every requested behavior. No persistent persona or code-golf target. |
| Cleanup after code | Code simplifiers, Addy code-simplification, Matt/code-oriented unslop variants | `kp-simplify`; preserve outputs, side effects, errors, and scope. Complexity measurement stays separate. |
| Writing cleanup | pstack/rstack unslop, Jakub better-writing, Matt writing-for-agents | Reader-focused guidance in `kp-docs` and reports. The same `unslop` name can mean prose or code; names alone are insufficient identity. |
| API and domain design | Matt codebase-design/domain-modeling, pstack architect, rstack code-structure, Addy interface design | `kp-api-design` and `kp-domain-model`; callers and domain meaning have separate owners. Preserve established architecture. |
| UI, accessibility, motion | Emil, Jakub, ibelick, OpenAI Product Design | `kp-ui-review` for assessment; implementation, motion, stack, and connector tooling remain optional profiles. Measure factual claims; label taste. |
| Evidence | rstack evidence/before-after, pstack verification skills, Superpowers verification | `kp-verify-change`; real behavior at the tested revision. Captures stay local unless their destination is authorized. |
| Research | Matt engineering research; OpenAI UX, Notion, biology, NVIDIA workflows | `kp-research` owns generic engineering questions. Specialized research workflows retain their actual domain and tool requirements. |
| Continuation and learning | Matt handoff/retro/teach, pstack ketchup/reflect/correct, David handoff | `kp-handoff` and `kp-skill-maintenance`; compact decisions and verified lessons, with structural checks when justified. |

## Wording changes that affect behavior

| Tempting instruction | Failure mode | Owned wording/decision |
| --- | --- | --- |
| Use on every coding task / any conversation / even a 1% possibility | Broad selection consumes context and adds process to trivial tasks. | Describe a concrete activity and likely boundary; direct work remains available. |
| Continue from interface design into implementation | Replaces the requested output with a larger task. | Design-only requests end with a proposal unless building was also requested. |
| The shortest diff wins | Can delete required behavior or obscure a readable solution. | Minimum complete approach; retain validation, errors, accessibility and contracts. |
| Ask a fixed number of questions before acting | Reopens settled decisions and creates friction. | Ask only consequential unresolved choices, using the user's preferred pace. |
| Always run several models / never block on the human | Assumes host tools, budget and authority. | Optional delegation only when authorized and useful; preserve uncertainty that requires a user decision. |
| Delete an external-rule comment when its constraint cannot be verified | Erases useful information because evidence is unavailable. | Keep the known uncertainty visible and investigate the external rule. |
| Keep working until a bot rates 5/5 | Can chase false positives or use a stale score. | Bounded attempts, current revision, actionable findings, independent checks, honest stopping result. |
| No shortcuts found means no debt | Equates marker coverage with project health. | A marker scan reports only marked debt. |
| Pull every update into active skill text | Overwrites intentional local wording and imports changed dependencies or authority assumptions. | Automatically propose pinned candidate changes; promote behavior separately. |

## Sources are not equal to runtime capabilities

pstack's original source and its portable forks have different adapters and update histories. The confirmed R-stack is `michaelshimeles/rstack`, not rstackjs. OpenAI's current plugins contain both first-party and partner examples; they are not a blanket endorsement or a shared license grant. `openai/skills` is deprecated. A skill that names a browser tool, MCP connector, model, commercial reviewer, or shell script does not provide it by being copied.

The same procedure can appear in a canonical directory, generated adapter, marketplace copy, and a fork. Keep source/path/commit/blob identity and install one chosen copy. Metadata is always part of selection cost; progressive disclosure reduces body loading, not the cost of an unbounded ambiguous catalog.

## Consensus and remaining uncertainty

The proposed default is the 20-skill owned pack. Source-specific integrations remain profiles or references. `adapt` in a source report means selected ideas are worth testing or transferring; it does not mean every upstream step was incorporated. The pack implements the central intent/scope/evidence distinctions above. Domain specialists can be added when a concrete project needs them.

The smoke tests show the intended boundaries in a few cases. They do not establish comparative quality, long-task reliability, host automatic selection, or the usefulness of every upstream skill. Repeated realistic baseline comparisons should decide later changes; neither simulated agreement nor popularity is enough.
