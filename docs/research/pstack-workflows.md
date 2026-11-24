# Pstack workflow skills: mechanisms, boundaries, and evolution

Research date: 2026-10-31. Canonical source: `cursor/plugins`, pinned to **`4dd1d05818d19792e7cd6e818f1667f95f7e1dbe`**. All snapshot links below use that exact commit. Scope: the 26 workflow skills assigned to this note, not the whole plugin. The local Git remote identifies `https://github.com/cursor/plugins.git`. The plugin manifests identify pstack version 0.15.36 and Lauren Tan as its author. [Snapshot][snapshot] [Manifest][manifest]

## Inspection limits and decision standard

This is a static source and Git-history audit, not a runtime evaluation or an installation recommendation. I read all 26 current `SKILL.md` bodies, all architect, how, reflect, TypeScript, and why references, the decision-log template, and the canonical `comment-sicko` and `log.sh` Git blobs. I inspected each entrypoint's `git log --follow` history and selected actual patches described under each entry. I followed the make-bot-ui move into the skills root. History discovery covered the complete available per-file lineage; patch inspection was selective, not every patch of every file. Upstream instructions were treated as source material and were not executed. No upstream helper, workflow, tool integration, test suite, or agent benchmark was run.

Dependency coverage is limited to those named files. I did not recursively audit every sibling principle, poteto-mode playbook, built-in Cursor skill, model-rule generator, external MCP, cloud runtime, renderer, or integration implementation these entrypoints invoke. Their presence in the dependency discussion records an assumption in the entrypoint, not a claim that the dependency works or has been fully audited. In particular, source-category recipes are not verification that the named service APIs still match them. Where current reference bodies were read, their full history was not systematically reviewed. Parent research separately covers mode/setup, principles, formal verification, and statechart.

Each practitioner and skeptic below is a **simulated reasoning role**, written by this researcher. They are not interviews, independent reviewers, or measured model results. Each case is a proposed falsifiable evaluation, not a test that passed during this audit. A changed instruction can be more coherent on inspection without demonstrating improved agent behavior. Unless explicitly stated otherwise, **behavioral improvement is unknown**. Commit frequency, model-name updates, and prompt length are not maturity scores.

The target is the user's own small daily TS/JS/Python skill set, with eight proposed activity owners: **shape, develop, debug, review, research, simplify, handoff, simulate-discussion**. A decision to absorb means reuse a mechanism in the appropriate owner, with self-contained references and the actual host's tools. It does not mean create a wrapper that requires the pstack catalog. A decision to defer requires an observed need before adding an entrypoint.

## 1. architect

**Mechanism and boundary.** This is a design-and-implementation workflow, not merely an architecture report. It grounds in how and sometimes why, runs arena over at least two structurally distinct designs, derives signatures from consumer usage, screens red flags, implements the chosen sketch, and revisits the design when repeated implementation friction appears. The supporting runner and rationale templates make usage, ownership, invariants, interface depth, alternatives, and accepted tradeoffs reviewable. Useful for a consequential new module or a change in ownership. Excessive for a settled mechanical edit. [Skill][architect] [Runner][architect-runner] [Red flags][architect-flags] [Rationale][architect-rationale]

**Portability and overlap.** Its caller-first sketch fits TS types, JS examples, and Python signatures, but Python annotations do not provide the same enforcement. Unimplemented bodies and pseudocode must not accidentally become a deployable intermediate state. The exact Cursor Task fields, pstack model-rule lines, default model slugs, sibling skills, and mandatory two-design fan-out are host and cost assumptions. Its natural home is **shape**, with implementation owned by **develop**. Keep explicit stop-at-design requests intact.

**Evolution.** The May 28 usage-first change is visible in history. The inspected October 3 patch adds split ownership, competing supported paths, importable internals, and hand-synced lists to the screening reference. That is a real increase in design criteria, not a model refresh. It does not prove the resulting designs resist mistakes better. [Usage-first commit][c0fe5b8a] [Inspected patch][ca586282]

**Simulated argument.** A library maintainer argues that writing two real callers exposes an awkward API earlier than class diagrams do. A delivery engineer objects that mandatory model competition and repeated grounding turn a one-function decision into a project. **Case:** design a TS upload queue consumed by both React UI and a Node worker, then add cancellation. Count caller knowledge of transport/state internals and compare against a single-design baseline. **Decision:** absorb usage-first design, ownership screening, and explicit redesign signals into shape; make competing designs conditional on a meaningful unresolved choice.

## 2. arena

**Mechanism and boundary.** Independent candidates receive the same task, produce isolated artifacts, and are compared against a task-specific rubric. A cross-family judge and coordinator pick a base; the coordinator ports a few useful parts from losing candidates and verifies the combined result. The useful distinction is generation followed by selection followed by coherent integration. It fits genuinely different architectural or artifact options; repetition has little value for a deterministic rename. [Skill][arena]

**Portability and overlap.** Worktrees and standalone output paths work across TS and Python. The model-family classifier, Cursor `Task`, `run_in_background`, `readonly`, model aliases, and `~/.cursor/rules/pstack-models.mdc` do not transfer automatically. Distinct vendors are not evidence of independent errors, and agreement is not verification. This is an optional tactic inside **shape**, **develop**, or **simulate-discussion**, not a new daily activity owner.

**Evolution.** The October 27 patch replaces incomplete rejected-model fallbacks with replacement/dropout behavior, makes the cross-judge come from another family or be skipped, and updates downstream output requirements to acknowledge the skip. The fallback contract became internally more complete. No inspected comparison establishes that family separation improves choices. [Inspected patch][cab1f702]

**Simulated argument.** A design lead values obtaining a materially different API before committing to one. A skeptical maintainer warns that hand grafting can invalidate both candidates' tests while producing a persuasive synthesis note. **Case:** compare two cache APIs on the same workload, then rerun the complete invariant suite on the grafted implementation. A merged artifact failing a property both candidates passed falsifies the assumption that grafting preserves quality. **Decision:** retain isolated options and explicit criteria as a conditional shape method. Drop family-based certainty and fixed model policies; verify the final artifact independently.

## 3. automate-me

**Mechanism and boundary.** This mines workspace transcripts across time slices, cross-checks repeated preferences, asks structured questions, revises an existing personal mode when possible, and uses a skill authoring workflow plus prose cleanup. Its output is a durable personal working-style skill. It explicitly distinguishes a recurring style from a single task workflow. Useful when the user requests that artifact, not as automatic session learning. [Skill][automate-me]

**Portability and overlap.** The privacy boundary is valuable: use the active workspace transcript path, not every project. Cursor transcript discovery, `AskQuestion`, built-in `create-skill`, `.cursor` paths, worktrees, and a required PR are environment assumptions. No TS/Python distinction matters here. A personal mode can duplicate all eight activity owners and create contradictory global rules. It is a separate maintenance task, only loosely adjacent to **handoff** and **research**.

**Evolution.** The inspected August 2 patch changes shallow discovery to recursive personal-category discovery and preserves an existing skill's category during editing. That fixes a concrete location assumption. Subsequent visible entrypoint history includes wording and subagent-policy edits. Neither establishes that mined preferences predict future preferences. [Inspected patch][c99559f2]

**Simulated argument.** A frequent user wants recurring corrections captured instead of repeated each week. A privacy-minded engineer objects that transcript frequency measures circumstances as well as preference, and a subjective approval is not enough to test future routing conflicts. **Case:** mine two recurring response preferences and one incident-specific demand, then ask the resulting mode to handle a task where that demand would be harmful. It should preserve the real preferences and reject the one-off. **Decision:** defer as a separate tool. If requested later, require user-selected scope and explicit acceptance; do not add continual transcript mining to the daily set.

## 4. benchmark-checklist

**Mechanism and boundary.** Before reporting a speedup, write the intended claim, inspect what the script measures, identify a limiter, compare tuned configurations, check physical limits, count errors, confirm work occurred, repeat/interleave runs, and measure the end-to-end impact. It distinguishes a requested single-run ballpark from an adoption decision. This is one of the clearest task-specific mechanisms in the group. [Skill][benchmark-checklist]

**Portability and overlap.** Node CPU profiling and Python profiling are named, so this is not React-only. Browser rendering needs browser-appropriate measures rather than CPU-only conclusions. `uptime`, `nproc`, `pidstat`, `perf`, and `strace` assume Unix or Linux; Windows needs actual equivalents. Fixed five-run thresholds and median/range comparisons are a heuristic, not a general statistical guarantee. Production tuning can be inaccessible or inappropriate for a shipped-default comparison, so preserve the user's actual decision. Put this in **debug** or **develop** as a performance reference; **research** owns adoption comparisons.

**Evolution.** It appears in October 2 history. The inspected October 3 patch changes a sibling playbook reference; October 10 mainly compresses prose while retaining the seven questions. This shows a concrete checklist but little public evolution of its measurement method. [Reference change][ce43c7ee] [Compression patch][c00b14f1]

**Simulated argument.** A performance engineer values work/error counters because fast rejection or an unconsumed Python generator can masquerade as a speedup. A statistician objects that overlapping ranges or an unidentified single limiter cannot decide every workload. **Case:** benchmark an awaited JS operation and an accidentally unawaited variant, plus an unconsumed Python generator. The process should reject both false wins before ranking options. **Decision:** strongly absorb the evidence questions, adapting commands and uncertainty to the host and claim. Do not promise statistical confidence from a fixed run count.

## 5. blast-radius

**Mechanism and boundary.** Follow effects beyond symbol callers into pinned dependency behavior, timing, serialization, database/wire contracts, flags, and other languages. Identify the one or two assumptions carrying the safety argument, then progress from assertion to source citation to executable probe to running-product reproduction. It reports both remaining risks and cleared concerns. Useful for a deceptively small cross-boundary change. [Skill][blast-radius]

**Portability and overlap.** The explicit React versus Solid teardown and microtask examples are illustrations, not requirements. TS/Python services sharing JSON or bytes are a particularly good fit. Git/forge discovery and arena are dependencies that should become host-specific optional procedures. A single safety fact can organize investigation, but several independent invariants may be necessary. A **review** reference should own impact analysis; **debug** can reuse the probe technique.

**Evolution.** Added June 17. The inspected September 22 patch removes repeated warnings about unproven assumptions but keeps the final requirement to label them unproven. That is consolidation, not evidence that risk analysis improved. Later model-related edits do not change this conclusion. [Introduction][ce46364b] [Inspected patch][c70b2dc8]

**Simulated argument.** A compatibility engineer likes proving the actual library function's behavior rather than listing speculative consumers. A skeptic warns that simplifying the safety argument to one fact can miss a second independent contract. **Case:** change a TS API serializer consumed by Python. A local TS test passes, but a Python parser rejects omitted nulls. The review succeeds only if it finds the wire consumer and labels every independent assumption. **Decision:** absorb boundary tracing and proof levels into review; use 'critical assumptions' rather than require exactly one safety fact.

## 6. bro

**Mechanism and boundary.** Restate the assistant's last message more plainly and concisely. This repairs a communication failure on demand. It does not research or simplify code. [Skill][bro]

**Portability and overlap.** It has no runtime, language, framework, or integration dependency. Its ambiguity is linguistic: remove jargon without dropping necessary conditions, units, or uncertainty. It overlaps **handoff** and the prose defaults of every owner, not the code-oriented **simplify** activity.

**Evolution.** Its sole visible entrypoint commit adds the current short instruction on August 2. There is no public per-file iteration to treat as maturation. A seven-line file can be adequate, but adequacy and behavioral improvement are unmeasured. [Inspected introduction][c99559f2]

**Simulated argument.** A user returning after an implementation values a low-friction request for an understandable answer. A technical lead worries that 'speak human' removes a limitation such as 'only verified on the Linux worker'. **Case:** rewrite a dense regression report while preserving affected scope, failing condition, evidence, and uncertainty. A reader should recover those facts without reopening the original. **Decision:** fold plain restatement into handoff and shared writing guidance. Keep a command alias only if actual user use justifies it, not as another required entrypoint.

## 7. correct

**Mechanism and boundary.** Mine repeated mistake classes, then prefer architectural elimination over type enforcement, lint/CI, behavior tests, and finally docs. Prove a new check rejects an actual past mistake; keep a rule-to-enforcement table. This is repository hardening, not merely apologizing after a correction. Useful for observed recurring failures with bounded ownership. [Skill][correct]

**Portability and overlap.** TS can prevent certain bad states at compile time; JS needs runtime/lint mechanisms, and Python annotation enforcement depends on the configured checker and runtime boundaries. A required human-approved, expiring inline exception and one-commit-per-class policy are local governance choices. Automatically mining and fixing multiple classes can exceed a bug's scope. This belongs in **develop** as an explicitly requested prevention pass, and **simplify** where removing duplicate paths is the proven remedy.

**Evolution.** Added October 3. The inspected October 14 patch replaces the crude 'would pass if every function returned nothing' test criterion with two behavioral criteria: breakage should fail and internal-only changes should not. That corrects a weak proxy on paper. No inspected regression exercise validates the new wording. [Introduction][c9511e60] [Inspected patch][ce5136d8]

**Simulated argument.** A devex engineer wants repeated invalid imports blocked by package boundaries rather than another paragraph in AGENTS. A maintainer warns that 'make impossible' can create a large abstraction or noisy lint for a rare mistake. **Case:** use two recorded TS internal-import violations, add the smallest boundary check, then apply it to both old violations and one legitimate public import. **Decision:** absorb real-failure-driven enforcement and counterexamples; require bounded scope and maintenance-cost evidence before architectural expansion.

## 8. figure-it-out

**Mechanism and boundary.** For work without a narrower playbook, define a falsifiable result, quantify scope, choose rigor, build a baseline/harness before changing things, sequence independently verifiable units, run keep/revert experiments, and retain an auditable decision trail. It is a fallback workflow designer for large, uncertain work. [Skill][figure-it-out]

**Portability and overlap.** Baselines and atomic units transfer to TS/JS/Python migrations. Pixel artifacts suit UI work only when visual parity is the requirement; Python jobs need data/output properties instead. Mandatory pstack principles, architect/arena, judges, and show-me-your-work create a large dependency chain. A 'multi-hour checkpoint' is a policy choice, and time estimates must not masquerade as evidence. It overlaps **develop** heavily, with **shape**, **debug**, and **handoff** as bounded supporting modes.

**Evolution.** Added May 24, later tied to sequencing principles. The inspected September 23 patch removes an explicit instruction to audit delegates' artifacts from a line that still requires a judge; other text still requires artifact inspection. The change is deduplication, not demonstrated stronger verification. [Introduction][c35f3392] [Inspected patch][cb0b9c7a]

**Simulated argument.** A migration lead wants a baseline before touching 100 components because later screenshots cannot reconstruct the original. A skeptic objects that inventing a workflow can defer learning from the first real unit. **Case:** migrate a TS parser in independently deployable units while comparing outputs against the original on a fixed corpus, including one intentionally invalid sample. **Decision:** absorb a compact fallback procedure into develop: risky unknown first, baseline, bounded units, artifact checks, explicit inconclusive results. Do not create another umbrella skill.

## 9. how

**Mechanism and boundary.** For a small question, one explainer reads and explains; for a subsystem, two to four explorers trace separate slices and an explainer reconciles them against code. References request components, concrete call/data flow, files read, boundaries, gotchas, and honest gaps. It answers runtime and ownership questions rather than historical intent. [Skill][how] [Explorer][how-explorer] [Explainer][how-explainer]

**Portability and overlap.** It can explain TS, JS, Python, or mixed services. Framework-specific lifecycle understanding still has to come from the actual code. Even its simple path mandates a subagent, model rules, and Cursor read-only Task semantics. Do not transplant the assumption that the parent cannot answer a one-function question. Its appropriate owner is **research**, with explanation reused by shape and debug.

**Evolution.** History since May includes substantial model configuration churn. The inspected October 10 patch consolidates duplicated spawn configuration and makes the simple/complex routing more concise while preserving one explainer for simple tasks. It does not show that explanations became more accurate. [Inspected patch][c00b14f1]

**Simulated argument.** An onboarding engineer values a reconciled flow over a list of files. A skeptic warns that explorers can each be locally correct while omitting a cross-cutting cancellation or transaction boundary. **Case:** explain a React request through a TS server into a Python worker, including cancellation. Check each claimed edge against a real symbol and ask where the request can stop. **Decision:** absorb evidence-backed call/data flow and complexity-based decomposition into research. Direct exploration should remain valid for narrow questions; delegation should follow actual coverage needs.

## 10. in-your-own-words

**Mechanism and boundary.** Restate the user's goals and the problem being solved. This is a brief comprehension check, not a solution plan or a command to start implementation. [Skill][in-your-own-words]

**Portability and overlap.** No language, framework, tool, or storage dependency exists. It belongs at the opening of **shape** or uncertain **develop/debug/research** tasks. Repeating settled intent on every handoff risks noise, and a paraphrase can silently narrow the user's goal.

**Evolution.** Added October 13. The same-day inspected revision removes a mandatory wait for confirmation and changes the target from goal/intent before starting to goals/problem. This is a real autonomy change; it reduces a forced checkpoint in the text, but its effects on misunderstanding and interruptions were not measured here. [Inspected patch][cdbf4981]

**Simulated argument.** A product engineer wants the agent to say 'stop duplicate charges on retry' rather than optimize the retry loop it happened to notice. A skeptic notes that a polished restatement can still omit an explicit constraint, such as maintaining the public API. **Case:** supply a request containing a goal, a forbidden scope expansion, and a settled design. The paraphrase must retain all three without asking for redundant approval. **Decision:** absorb a concise goal/problem/constraint statement where ambiguity has cost. No standalone daily entrypoint is necessary unless the user specifically wants a restatement command.

## 11. interrogate

**Mechanism and boundary.** Multiple adversaries receive intent and the real change in isolated worktrees, prove failures with commands, and return required versus observed behavior. The lead reruns and deduplicates findings. It reports rather than fixes. This is adversarial executable review, including prototype probes of plans. [Skill][interrogate]

**Portability and overlap.** The method fits TS tests, Python reproductions, and React browser cases. It inherits arena's host configuration; uncommitted changes must actually be copied into each worker's tree. 'Only run-proven findings' is too strict as the entire **review** contract: an exposed credential, inaccessible production race, or missing authorization can be material before a safe local exploit exists. Preserve an explicit unverified risk channel rather than interpret no reproduced failures as safety.

**Evolution.** October 27 is a substantial redesign. The inspected diff removes subjective review buckets, agreement maps, code-quality/reference rubrics, and a 1,000-line-file concern. It replaces them with artifact-producing adversaries and lead reruns. This is a meaningful shift from consensus and taste to reproducible behavior, while narrowing what the review can report. Comparative precision and recall remain unknown. [Inspected patch][cab1f702]

**Simulated argument.** A reviewer tired of speculative nits wants each bug claim to survive an actual rerun. A security engineer warns that reproduction-only filtering can hide a real deployment-specific risk. **Case:** seed one deterministic parser bug, one style concern, and one source-provable secret exposure. The review should reproduce the bug, dismiss the style issue, and retain the secret exposure with its evidence class. **Decision:** absorb executable adversarial review into review; do not adopt the rule that non-runnable concerns disappear.

## 12. ketchup

**Mechanism and boundary.** A read-only catch-up starts from the last actual user message, refreshes touched live states, explains user-visible changes, and lists every decision still owned by the user with enough context to decide. It separates decisions from work the agent can continue. Existing screenshots/recordings and small explanatory diagrams support the text. [Skill][ketchup]

**Portability and overlap.** No TS/Python distinction is intrinsic. UI work often has screenshots; backend changes may need a short flow or no visual. It assumes access to live PR, CI, and agent states, and an inline artifact-capable chat. Arbitrary six-box/eight-word limits and mandatory per-item risk can produce clutter. Its substance belongs in **handoff**.

**Evolution.** Added October 10 and repeatedly revised. The October 17 inspected commit explicitly records a failure: the prior 150-word cap caused PRs to collapse into a count or external file. The patch lets the answer grow by item count, requires an item link/number, evidence, user effect, and risk. A follow-up makes 'never cut items for a word count' explicit. This is unusually concrete failure-driven prompt maturation, although the commit narrative is not a comparable before/after evaluation. [Inspected patch][c16541c6] [Follow-up][cbc14437]

**Simulated argument.** A busy reviewer wants to decide each pending PR without reopening the transcript. A skeptic warns that risk boilerplate may overwhelm a simple catch-up. **Case:** summarize thirty pending PRs plus two completed changes; verify that all thirty decisions remain individually identifiable and none is represented only by a count. Include a two-item boundary case for brevity. **Decision:** strongly absorb complete, decidable user actions and live-state verification into handoff; let content, not hard word/visual counts, set length.

## 13. ketchup-video

**Mechanism and boundary.** This is ketchup with a short rendered slide video for completed/ongoing work and text for the remaining decisions. It specifies source artifacts rather than chat prose, coherent diagrams, subtitles, word-based holds, and rendered-file inspection. Useful only when a video improves a real catch-up; it is a production workflow with extra cost, not a generic status default. [Skill][ketchup-video]

**Portability and overlap.** It assumes a renderer, encoded video support, frame extraction/inspection, and inline playback, but bundles no renderer or command contract. It has no language preference. It changes ketchup's read-only posture only to permit rendering outside the repo. Rendering should not hide unavailable evidence or imply a screen capture that never existed. A **handoff** optional format can own it.

**Evolution.** Added October 23. The inspected October 27 patch adds a dedicated subtitle strip, defines a full-slide hold separately from transitions, counts changed labels/subtitles, and requires hold measurement by matching rendered frames rather than a still-frame detector. These are specific artifact-level refinements. No rendered before/after viewer study or runtime exercise was inspected. [Introduction][c3c0fdb4] [Inspected patch][cab1f702]

**Simulated argument.** A UI lead values a visual sequence showing what changed and why. A skeptic argues that a silent video is slower to scan and less searchable than text, particularly for backend decisions. **Case:** render a three-slide UI change with one long new subtitle and a fade; inspect frames and measure full holds. Then compare decision retrieval time against a screenshot-plus-text handoff. **Decision:** defer until the user requests video or an observed communication problem warrants it. Keep artifact verification as the useful lesson.

## 14. make-bot-ui

**Mechanism and boundary.** Build a local page whose server sends a secret-authenticated webhook to wake a Grok Bot routine, obtain the secret through a special UI request, probe harmlessly, and expose the page on an existing Tailscale node. Browser-side secret exclusion and treating webhook data as untrusted are sound boundaries. This is a specific integration recipe, not general frontend development. [Skill][make-bot-ui]

**Portability and overlap.** It prescribes `update_state`, `SendToUser`, routine panels, credential files, Cursor webhook headers, a macOS shortcut, Linux installation via shell, `sudo`, HTTP tailnet URLs, and an eight-second one-try request. None is established as available for the user's Windows/Codex host by this source. TS/JS or Python could implement the server; React is unnecessary. A local failure log lacks a complete replay/idempotency/acknowledgment contract. **Develop** should discover the user's actual integration if requested, rather than inherit this one.

**Evolution.** The August 27 inspected move promotes `skills/grokbot/make-bot-ui/SKILL.md` to `skills/make-bot-ui/SKILL.md` unchanged, addressing registration/discovery. Later patches change invocation metadata and align the name with its folder. Those are packaging changes, not demonstrated webhook resilience or security improvement. [Rename][c6fecddb] [Name alignment][ca968159]

**Simulated argument.** A bot operator wants buttons that wake an agent without polling or leaking keys. A platform skeptic sees an undocumented host-specific control plane plus underspecified local replay. **Case:** on a supported host, simulate an accepted-but-timed-out webhook and replay the queued payload; verify the action executes once and the secret never reaches browser assets/logs. **Decision:** reject from the general daily set. Rebuild a narrow integration-specific skill only for an actual supported service and tested delivery contract.

## 15. no-comments

**Mechanism and boundary.** A named comment-deletion agent reviews a scoped diff, keeps a small exception list, flags code that needs reshaping, and the parent fixes accepted root causes. It attempts to replace explanatory workaround comments and suppressions with enforceable structure. That intention can be useful, but default deletion under ambiguity is a strong author preference rather than a generally safe simplification policy. [Skill][no-comments] [Agent][comment-sicko]

**Portability and overlap.** The custom `comment-sicko` agent, Task semantics, how/why/architect delegation, and TS/lint suppression handling are dependencies. Python comments can carry operational constraints that neither annotations nor local tests express. Public API, legal, and external-platform comments are explicitly protected, but uncertainty about an exception still biases toward deletion. The phrase requiring interactive approval for encoding, followed by deletion when approval is absent, is especially unsuitable for preserving unknown constraints. This overlaps **simplify** and **review**.

**Evolution.** Added August 1 with its custom agent. The inspected October 12 patch fixes the Task agent identifier from a display name to `comment-sicko`, with a commit message naming Grok spawning. That is a concrete invocation compatibility repair. It does not validate deletion judgments. [Introduction][cb047069] [Inspected patch][cde2dba6]

**Simulated argument.** A maintainer wants a stale workaround removed with the code that made it necessary. A skeptic asks why uncertain historical constraints should be lost before their replacement is proven. **Case:** review a scoped diff containing redundant narration, a public contract, and an internal comment explaining a real production ordering constraint absent from local tests. Preserve the latter until its invariant is understood/enforced. **Decision:** reject the deletion persona and ambiguity rule. Absorb only evidence-based removal of comments made obsolete by the actual change.

## 16. recall

**Mechanism and boundary.** Reconstruct recent work from scoped chat history, shared issue/history/incident records, and live artifact state. Route a single-session pickup elsewhere; skip mining when the user supplies a complete capsule. It returns a compact overall capsule, tagged threads, recurring problems, and one next move. It is working-context recovery rather than a summary of the current turn. [Skill][recall]

**Portability and overlap.** The workspace-only boundary and time window are valuable, but its Unix-derived Cursor slug and transcript layout, `ls -t`, gh, sibling playbooks, and mandatory why sweep are not a universal host interface. The fixed status tags omit legitimate states such as a blocked issue without a branch or PR. No code language dependence exists. **Handoff** should own resumption; **research** can supply evidence discovery.

**Evolution.** Added June 17. The inspected September 7 patch removes explanatory repetition while preserving shared-record searching and live verification. It does not add a tested retrieval mechanism or show improved recall precision. Later effort-policy changes likewise are not retrieval-quality evidence. [Introduction][ce46364b] [Inspected patch][ce8d856f]

**Simulated argument.** An engineer resuming a reverted bug fix wants to know why the prior attempt failed, not merely where its branch lives. A skeptic worries that mandatory cross-source searches transform 'where was I?' into an expensive organization-wide investigation. **Case:** provide one stale transcript claiming a PR is open, a live merged state, and a later revert. A good capsule reflects the revert and excludes an unrelated workspace's similar issue. **Decision:** absorb evidence provenance, live-state reconciliation, and capsule-first resumption into handoff. Make external sweeps proportional to the named target and actual uncertainty.

## 17. reflect

**Mechanism and boundary.** Three lenses inspect the active transcript, a synthesizer filters durable learnings, structural mechanisms become backlog, and accepted skill edits await explicit approval. References distinguish missing guidance from execution failures and missed triggers, require target-skill reading, and treat transcripts/reviewer outputs as untrusted. It is deliberate skill maintenance, not permission to change behavior after every session. [Skill][reflect] [Judgment][reflect-judgment] [Tooling][reflect-tooling] [Divergent][reflect-divergent] [Synthesizer][reflect-synth]

**Portability and overlap.** Cursor transcript paths, fixed model roles, built-in skill authoring/evaluation, and writable mode for MCP access are host-specific. Writable mode is not inherently needed on every host. Filing every backlog item to a team tracker without waiting is an external mutation policy that cannot transfer without authorization. It touches all eight owners, but an org-wide learning pipeline is outside a small daily activity set.

**Evolution.** The October 23 inspected patch forbids editing plugin-cache copies, requires showing the intended personal/project destination, and prohibits PR/push. That addresses a concrete persistence boundary in source. Earlier multi-lens work does not establish that reviewer convergence identifies durable lessons. [Inspected patch][c7054003]

**Simulated argument.** A skill maintainer values a reviewer rejecting a duplicate rule because the actual problem was execution. A skeptic warns that three models reading one incident are still one incident, and automatically filed backlog can propagate private context. **Case:** reflect on a session with one genuine missing boundary, one already-covered ignored rule, and one private ticket. Accept only the missing boundary for user review; neither duplicate the rule nor publish the private content. **Decision:** defer a separate reflect workflow. Use explicit, case-backed maintenance in the existing owner and keep public-output and external-write authorization intact.

## 18. sharpen

**Mechanism and boundary.** Before rewriting a task, identify expert practice, the raw primary material, concrete methods/tools, and an independent correctness check. Rewrite for depth within the same scope and leave user choices open. It improves the task specification rather than performing it. [Skill][sharpen]

**Portability and overlap.** There is no host or language dependency. In TS work the raw material may be failing inputs and a diff; in Python analysis it may be original data and a reproducible query. 'Expert would do' must remain a reasoned proposal, not invented authority. This can be a requested mode of **shape** or **research**, while **simulate-discussion** can challenge the proposed expert method.

**Evolution.** Three October commits show reversals. The inspected October 19 patch removes an instruction to internally frame and then do the work, restoring an explicit prompt-rewrite deliverable with four visible questions. The title says 'return only the rewrite', but the body also says to 'say' the four findings. That is residual output ambiguity, not settled evidence of an optimal contract. [Inspected patch][c88d4751]

**Simulated argument.** A researcher wants 'review this performance claim' to become inspection of the original script, data, errors, and independent checks. A skeptic notes that the extra four answers can become a ceremony or silently expand a one-hour task. **Case:** sharpen 'compare two parsers on my existing fixtures in one hour' without adding a production observability project or deciding the winner. **Decision:** absorb primary-material and outside-check questions as optional framing. Specify whether the requested output is just a rewritten prompt or a short rationale plus prompt.

## 19. show-me-your-work

**Mechanism and boundary.** Maintain one append-only TSV of decisions, reasons, evidence pointers, and results; log pivots and checkpoints rather than every command. Run boundaries use start rows. Audit this run's rows against its transcript, supersede false entries, and ask a different-family reviewer for attention items. The bundled Bash helper sanitizes single-line cells and quotes formula-looking prefixes. Useful for unattended migrations where the diff alone cannot explain rejected choices. [Skill][show-me-your-work] [Template][decision-template] [Helper][log-helper]

**Portability and overlap.** TSV is language-neutral. Bash/date/tr and transcript paths require an adapter on Windows; model-family review and an Attention section are policy, not proof. The helper has no locking or transactional multiwriter contract, and start rows are bookkeeping rather than isolation. Evidence must survive long enough for review; a removed worktree path is a weak pointer. **Handoff** should own the artifact, with develop emitting the decision events.

**Evolution.** The inspected May 24 helper patch adds parent-directory creation, CR/tab/newline cleaning, and spreadsheet-formula prefix protection. Current source also appends rather than truncating during header creation and the September 22 helper history contains that later change. These are concrete implementation hardenings, not only prose. No helper or concurrent run was executed here. [Inspected helper patch][c11ecc12] [Current helper][log-helper] [Later helper history commit][c70b2dc8]

**Simulated argument.** A reviewer values evidence for why an attempted migration path was reverted. A skeptic worries that transcripts plus logs double paperwork and that reviewer self-consistency is not artifact correctness. **Case:** record a kept unit, a reverted approach, and an intentionally false row, then audit. The false row must be superseded with resolvable evidence, not quietly rewritten. Separately test two simultaneous appends before permitting shared logs. **Decision:** absorb a small optional decision trail for long work; prefer one writer and durable evidence, with no mandatory cross-family ritual.

## 20. swarm

**Mechanism and boundary.** Define a done predicate, partition coverage or declare a race policy, give workers standalone briefs and isolated outputs, require exact revisions/methods for measurements, reject incomplete reports, and consolidate gaps explicitly. Unlike arena it can cover independent slices without synthesizing one candidate implementation. [Skill][swarm]

**Portability and overlap.** Useful for independent TS packages or Python corpus slices. Cursor cloud execution, `cloud_base_branch`, model lines, and forced background fan-out are host-specific; cloud cannot inspect uncommitted local state merely because a brief names it. A first-pass race can bias selection toward fast shallow work unless the predicate is decisive. **Develop**, **review**, and **research** should use conditional delegation rather than require a swarm entrypoint.

**Evolution.** Added July 30. The October 2 inspected patch replaces re-running a failed worker with respawning it, a concrete fresh-context instruction. October 23 repairs misnumbering and a dangling table reference; those are coherence fixes, not task-quality evaluations. Exact-SHA/method provenance is present in current source, but this audit does not establish when it improved results. [Fresh-worker patch][c23e4138] [Reference repair][ce73df47]

**Simulated argument.** A release engineer values an explicit gap when one worker checked the wrong commit. A skeptic argues that four PASS summaries can hide four different commands and no complete coverage. **Case:** assign three packages at one SHA, with one worker returning an older SHA and another omitting the sample method. Both must be retried once or counted as gaps, never passes. **Decision:** absorb standalone briefs, revision/method provenance, isolated writes, and explicit coverage gaps as delegation mechanics. Keep parallelism optional and host-driven.

## 21. tdd

**Mechanism and boundary.** This is focused regression-first bug fixing: identify intended behavior, choose a cheap existing test path, demonstrate the intended failure, make the smallest production fix, and show the test passes. It expressly permits a targeted executable check instead of forcing costly mocks or infrastructure. Despite its name it is not a complete feature-oriented red/green/refactor methodology. [Skill][tdd]

**Portability and overlap.** Existing Vitest/Jest, React component tests, pytest, or a Python script can serve the same behavioral contract. Use the repository's runner and scope. The skill's explicit-request/cheap-obvious-bug routing is more restrained than its terse name suggests. It belongs in **debug** and **develop**, with the explicit user request deciding whether full TDD is wanted.

**Evolution.** Present at the May introduction. The inspected September 22 patch removes the explicit nearby-validation step, although the final report still mentions nearby validation performed. September 23 removes another redundant instruction in history. This is primarily instruction subtraction; the inspected evidence does not show a richer regression method or improved defect prevention. [Inspected patch][c70b2dc8] [History subtraction][cb0b9c7a]

**Simulated argument.** A bug fixer wants proof a new test catches the bug before fixing it. A skeptic worries that 'impractical' becomes an escape hatch whenever a regression is inconvenient. **Case:** a Python date-normalization bug has an existing pytest target and must fail before/pass after; a browser-only race with no reliable local test must get an honestly labeled executable/manual reproduction rather than brittle mocks. **Decision:** strongly absorb behavior-first regression evidence and justified alternatives into debug. Preserve appropriate adjacent checks when the change crosses a boundary; do not force new harnesses for tiny fixes.

## 22. teach

**Mechanism and boundary.** Compose runtime explanation from how and historical rationale from why, keep confidence wording, give the smallest complete account first, and add detail conversationally. It favors definitions and concrete mechanisms over symbol inventories, and uses progressively built diagrams. It should change understanding, not code. [Skill][teach]

**Portability and overlap.** It applies equally to TS/React rendering, Node services, and Python data flow. However it mandates sibling invocations, can trigger a large why sweep, and prescribes generated whiteboard images for spatial topics. An accurate SVG/diagram or screenshot may be cheaper and more precise; three moving parts do not always need three pictures. It overlaps **research** output and **handoff** explanation.

**Evolution.** Added July 12. The inspected September 7 patch mostly removes repetitive justifications while retaining the progressive-diagram rule and the how/why composition. It is prose refinement, not evidence of learner comprehension. The tension between 'cut hedging' and 'preserve why confidence language' remains important: evidence uncertainty must win over a style cleanup. [Introduction][c8f008c4] [Inspected patch][ce8d856f]

**Simulated argument.** An onboarding engineer wants virtualization explained through what disappears when a row scrolls out, not a tour of constants. A skeptic asks whether mandatory diagrams and a second investigation delay a simple answer. **Case:** explain one React stale-closure bug and one mixed-language queue with uncertain history. A reader must predict the next callback's value and distinguish known mechanics from inferred intent. **Decision:** absorb definition-first, mechanism-based, audience-sized explanation into research/handoff. Select visuals by explanatory value, and investigate historical why only when it affects the question.

## 23. technical-writing

**Mechanism and boundary.** Classify documentation by action/understanding and learning/work, then apply reader-focused sentences, explicit conditions, controlled terminology, and disambiguation. It calls out overloaded pronouns, misplaced only/not, long noun strings, dropped verbs, and stale paths/counts. It includes an escape clause when a rule makes the sentence worse. Useful for docs, PR descriptions, and instructions. [Skill][technical-writing]

**Portability and overlap.** Language-independent as a writing method. Its tabs-for-code policy, unconditional unslop dependency, mode purity, ban on certain punctuation, and view that opinion belongs only in explanation are author conventions, not portable necessities. Python snippets must respect the target's indentation/style. It is a shared reference for **handoff** and **research**, not a code simplification procedure. The cited external writing traditions were not independently audited as standards-conformance claims here.

**Evolution.** Added August 1. The inspected September 22 patch deletes a review checklist that restated the body; October 10 also distills prompts. This demonstrates consolidation, not verified improvement in reading accuracy or completion. [Introduction][cb047069] [Inspected patch][c70b2dc8]

**Simulated argument.** A documentation engineer values putting 'only' beside its target because a command can otherwise be applied under the wrong condition. A skeptical Python maintainer objects to a universal tab rule and splitting a coherent operational guide into many mode-pure files. **Case:** rewrite an ambiguous migration instruction containing a destructive step and condition, plus a mixed guide containing a small lookup table. Readers should identify the correct precondition without losing useful local reference. **Decision:** absorb ambiguity checks, real-symbol terminology, and truthful examples. Keep repo style and reader task above punctuation/mode dogma.

## 24. typescript-best-practices

**Mechanism and boundary.** It offers a rule table and examples for variant modeling, branded IDs, total operations, unknown external data, existing runtime schemas, exhaustiveness, derivation, named object arguments, real tests, and structured telemetry. It invokes type-system and boundary principles. This is a TS-specific reference, not language-neutral daily orchestration. [Skill][typescript-best-practices] [Examples][ts-patterns]

**Portability and overlap.** TS/TSX paths are explicit. Plain JS cannot inherit compile-time guarantees; Python needs its own NewType/union/schema/checker guidance. Repository conventions must beat mandatory `__brand`, `kind`, inline never variables, or object arguments. Source examples contain an important defect: a time range says a negative range cannot be written while `durationMs` is a plain number. Negative numbers, NaN, and infinity remain constructible. Likewise a user-defined type predicate is trusted, not proof that its asserted brand is semantically correct. React-specific verification is only an example, not a React dependency. Put a corrected reference under **develop**, reused by shape/review.

**Evolution.** July history adds constructive modeling. The inspected October 17 patch replaces a post-validation cast in `parseAgentId` with a user-defined predicate and says brands never come from casts. That removes an internal inconsistency with its cast ban, but relocates the trust assertion into a predicate; it does not create stronger runtime validation. No compile/runtime corpus was run here. [Constructive modeling][c91be0f9] [Inspected patch][c0317eb8]

**Simulated argument.** A TS maintainer likes schema-derived boundary types and discriminated state because new variants create visible compiler work. A skeptic warns that syntax purity can conceal the same assertion and that constructive-modeling examples promise more than number types enforce. **Case:** pass `durationMs: -1` through the proposed TimeRange and make a dishonest `isAgentId` predicate return true. The reference must explain why neither claim is guaranteed by TS. **Decision:** absorb selectively, correct examples, test them under the repository's strict config, and supply distinct JS/Python advice rather than relabel TS rules as universal.

## 25. unslop

**Mechanism and boundary.** This edits prose for vague attribution, unsupported flourish, filler, synonym churn, excessive hedging, dense syntax, and empty conclusions. Stable rule identifiers let other skills reference it. It is a writing policy, unlike skills of the same name that simplify code. [Skill][unslop]

**Portability and overlap.** No host/language integration is needed. Concrete source names, measured values, and stable terminology improve research and handoff. But blanket bans on words, em dashes/parenthetical substitutes, curly quotes, or domain terms such as 'primitive' can alter voice or technical accuracy. Meaning and calibrated uncertainty must survive; 'appears to' can be necessary evidence language. It overlaps **handoff** and **research**, while **simplify** should keep its code-focused contract explicit.

**Evolution.** The inspected October 11 patch removes 'Must always apply' from the description while retaining disabled model invocation. That fixes conflicting trigger posture in metadata. Other observed history adds prose-pattern rules, but an expanding prohibited-vocabulary list is not demonstrated improvement. No reader comparison was inspected. [Inspected patch][cbc697d0]

**Simulated argument.** A reviewer values replacing 'significantly improves' with the measured change and its unit. A skeptic notes that an editing model may delete the qualifier distinguishing inference from fact. **Case:** edit a cited paragraph containing one empty superlative, one legitimate term of art, and one necessary 'likely'. Remove the first, preserve/define the second, and keep the third unless new evidence changes its tier. **Decision:** absorb semantic writing checks into handoff/research. Do not transplant the author's complete vocabulary or punctuation blacklist, and do not confuse this skill with code cleanup.

## 26. why

**Mechanism and boundary.** Anchor a target in code and history, discover available evidence categories, investigate each available category, and synthesize claims as direct, supported, inferred, speculative, or unknown. The seven categories span git/PRs, issues, docs, chat, infrastructure telemetry, error tracking, and analytics. Source playbooks require real queries, source-specific leads, gaps, contradictions, and temporal caution. Before a change, findings become preserve/change/avoid/risk constraints. The confidence framework is the distinctive value. [Skill][why] [Epistemics][why-epistemics] [Investigator][why-investigator] [Source index][why-sources] [Synthesizer][why-synth]

**Portability and overlap.** Git archaeology transfers across TS/Python. Cursor Task/MCP discovery, required agent-mode semantics, model rules, gh availability, named MCP APIs, and company-shaped warehouse columns are assumptions. The Databricks reference both tells agents to probe schemas and supplies column conventions as though standard; keep probing authoritative. Calling gh/source control always available is too strong for offline/non-GitHub repositories. A full seven-category sweep for every why question is expensive and may exceed data scope. This is a reference inside **research**, supporting shape/debug/review.

**Evolution.** The long May-to-October lineage includes many model updates. The inspected October 10 patch consolidates anchor commands, spawn configuration, and coverage instructions, preserving the existing evidence-tier method. It does not show that historical answers became more correct. Source references remain substantive, but no retrieval/citation accuracy evaluation was inspected. [Inspected patch][c00b14f1] [Code archaeology][why-git] [Warehouse playbook][why-databricks]

**Simulated argument.** An incident investigator wants a retry's original failure constraint preserved instead of inferred from today's code. A skeptic asks why a small build-time decision should trigger six irrelevant data searches or receive false confidence from a tidy story. **Case:** seed a PR stating one reason, a later contradictory incident note, and absent chat access. The answer must retain both sources, mark the access gap, and avoid turning current code into author intent. **Decision:** strongly absorb confidence tiers, contradictory evidence, source-scoped queries, and planning constraints. Make the search plan proportionate and authorized; a coverage map should explain useful searches and gaps without mandating every possible integration.

## What actually looks mature, and what remains unproven

The strongest reusable methods here are consumer-first shape design, measurements that prove work happened, cross-boundary probes, regression-before-fix evidence, complete pending decisions, historical confidence tiers, exact revision/method provenance, and durable decision evidence. Their usefulness is a reasoned fit to the target user's work, not an observed performance result.

Public history supports several concrete forms of maturation: ketchup responds to a documented omission failure; interrogate changes its evidence standard; reflect fixes cache-edit persistence; make-bot-ui fixes discovery; no-comments fixes an agent identifier; log.sh hardens actual cell serialization. Other histories primarily show prose reduction, metadata cleanup, or model-default churn. None of these alone demonstrates lower defect rates, better recall, or more accurate design judgment. The user's own skills should adopt a small mechanism, exercise one realistic and one boundary case, compare against the prior owner when claiming improvement, and retain only changes that improve that activity without damaging its neighbor.

## Pinned primary sources

[snapshot]: https://github.com/cursor/plugins/tree/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack
[manifest]: https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/.cursor-plugin/plugin.json
[architect]: https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/architect/SKILL.md
[architect-runner]: https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/architect/references/runner-prompt.md
[architect-flags]: https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/architect/references/design-red-flags.md
[architect-rationale]: https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/architect/references/rationale-template.md
[arena]: https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/arena/SKILL.md
[automate-me]: https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/automate-me/SKILL.md
[benchmark-checklist]: https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/benchmark-checklist/SKILL.md
[blast-radius]: https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/blast-radius/SKILL.md
[bro]: https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/bro/SKILL.md
[correct]: https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/correct/SKILL.md
[figure-it-out]: https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/figure-it-out/SKILL.md
[how]: https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/how/SKILL.md
[how-explorer]: https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/how/references/explorer-prompt.md
[how-explainer]: https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/how/references/explainer-prompt.md
[in-your-own-words]: https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/in-your-own-words/SKILL.md
[interrogate]: https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/interrogate/SKILL.md
[ketchup]: https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/ketchup/SKILL.md
[ketchup-video]: https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/ketchup-video/SKILL.md
[make-bot-ui]: https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/make-bot-ui/SKILL.md
[no-comments]: https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/no-comments/SKILL.md
[comment-sicko]: https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/agents/comment-sicko.md
[recall]: https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/recall/SKILL.md
[reflect]: https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/reflect/SKILL.md
[reflect-judgment]: https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/reflect/references/judgment-reviewer.md
[reflect-tooling]: https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/reflect/references/tooling-reviewer.md
[reflect-divergent]: https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/reflect/references/divergent-reviewer.md
[reflect-synth]: https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/reflect/references/synthesizer.md
[sharpen]: https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/sharpen/SKILL.md
[show-me-your-work]: https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/show-me-your-work/SKILL.md
[decision-template]: https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/show-me-your-work/references/decision-log-template.tsv
[log-helper]: https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/show-me-your-work/scripts/log.sh
[swarm]: https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/swarm/SKILL.md
[tdd]: https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/tdd/SKILL.md
[teach]: https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/teach/SKILL.md
[technical-writing]: https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/technical-writing/SKILL.md
[typescript-best-practices]: https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/typescript-best-practices/SKILL.md
[ts-patterns]: https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/typescript-best-practices/references/patterns.md
[unslop]: https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/unslop/SKILL.md
[why]: https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/why/SKILL.md
[why-epistemics]: https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/why/references/epistemics.md
[why-investigator]: https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/why/references/investigator-prompt.md
[why-sources]: https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/why/references/source-playbook.md
[why-synth]: https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/why/references/synthesizer-prompt.md
[why-git]: https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/why/references/sources/code-archaeology.md
[why-databricks]: https://github.com/cursor/plugins/blob/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack/skills/why/references/sources/databricks.md
[c0fe5b8a]: https://github.com/cursor/plugins/commit/0fe5b8a
[ca586282]: https://github.com/cursor/plugins/commit/a586282
[cab1f702]: https://github.com/cursor/plugins/commit/ab1f702
[c99559f2]: https://github.com/cursor/plugins/commit/99559f2
[ce43c7ee]: https://github.com/cursor/plugins/commit/e43c7ee
[c00b14f1]: https://github.com/cursor/plugins/commit/00b14f1
[ce46364b]: https://github.com/cursor/plugins/commit/e46364b
[c70b2dc8]: https://github.com/cursor/plugins/commit/70b2dc8
[c9511e60]: https://github.com/cursor/plugins/commit/9511e60
[ce5136d8]: https://github.com/cursor/plugins/commit/e5136d8
[c35f3392]: https://github.com/cursor/plugins/commit/35f3392
[cb0b9c7a]: https://github.com/cursor/plugins/commit/b0b9c7a
[cdbf4981]: https://github.com/cursor/plugins/commit/dbf4981
[c16541c6]: https://github.com/cursor/plugins/commit/16541c6
[cbc14437]: https://github.com/cursor/plugins/commit/bc14437
[c3c0fdb4]: https://github.com/cursor/plugins/commit/3c0fdb4
[c6fecddb]: https://github.com/cursor/plugins/commit/6fecddb
[ca968159]: https://github.com/cursor/plugins/commit/a968159
[cb047069]: https://github.com/cursor/plugins/commit/b047069
[cde2dba6]: https://github.com/cursor/plugins/commit/de2dba6
[ce8d856f]: https://github.com/cursor/plugins/commit/e8d856f
[c7054003]: https://github.com/cursor/plugins/commit/7054003
[c88d4751]: https://github.com/cursor/plugins/commit/88d4751
[c11ecc12]: https://github.com/cursor/plugins/commit/11ecc12
[c23e4138]: https://github.com/cursor/plugins/commit/23e4138
[ce73df47]: https://github.com/cursor/plugins/commit/e73df47
[c8f008c4]: https://github.com/cursor/plugins/commit/8f008c4
[c91be0f9]: https://github.com/cursor/plugins/commit/91be0f9
[c0317eb8]: https://github.com/cursor/plugins/commit/0317eb8
[cbc697d0]: https://github.com/cursor/plugins/commit/bc697d0
