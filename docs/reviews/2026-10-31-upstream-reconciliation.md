# Daily upstream reconciliation — 31 October 2026

Eleven public sources and the separate authorized private baseline were checked. Four public sources changed relative to the open proposal's previous observation; seven did not. The catalog now contains **816 entrypoints**. The private baseline has no delta and is not reproduced here.

This report uses simulated Practitioner, Skeptic and Evaluator perspectives. They are curation arguments, not independent experiments or claims by the authors. Changed instructions and support code were inspected as data; no upstream installer, helper or benchmark was executed. The owned 20-skill pack remains unchanged.

## Observed changes

| Source | Previous observation | New observation | Scope |
| --- | --- | --- | --- |
| Matt Pocock | `a496f5513d4a4cf889bc48e189e579f4b0bdf6aa` | `4ae2317ddb22b046e26455e4f9c9b3aaaf62212d` | One new in-progress skill with six files, coordinator instructions, and release notes |
| Addy Osmani | `eb07f19f52c2669f2364897aaa293e2aaddd7b1c` | `8bfcc1f9916f2eea55494d8c1fa7f4bde867dd9e` | Eight entrypoint edits plus scanner gates, references, a hook, evaluation fixtures/runner and release manifests |
| David Ondrej | `d5c727c82e55df04374888c1d708a1a65354d2ba` | `8e90e9d634983e76e66154e6b36a11d735fd19da` | ADR filename convention guidance |
| ibelick | `59193a75432e5f41c6980f53b9e6a7bd56919947` | `b88b130b87af0570d46692fa9806ccbcbd5afec2` | Directory/site implementation and metadata; no bundled skill-directory, package, plugin or license diff |

The exact added/changed path list is in [upstream-changes.json](../upstream-changes.json). No tracked license change was found. Existing copyright and package terms still apply; this report adds summaries, not vendored upstream bodies.

## Matt: software-factory and coordinator procedures

The new [software-factory entrypoint](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/in-progress/software-factory/SKILL.md) defines tasks, triggers, runs and service roles, with bounded trigger/review loops and questions about duplicate work. Its example tasks are useful design prompts. The slot surveys explicitly require current product verification; their vendor-specific claims were not verified here.

- **Practitioner:** The state-owner, trigger, human-entry and duplicate-delivery questions could sharpen a concrete factory design without building another orchestration framework.
- **Skeptic:** The glossary is prescriptive, runner state is assumed disposable, and runs never wait for people. Those are design choices, not universal requirements. More immediately, the unquoted description contains a colon followed by a space, and the actual entrypoint fails PyYAML parsing with `mapping values are not allowed here`.
- **Evaluator:** Require valid frontmatter and clean-install discovery first. Then use a real design with retries, duplicate tickets and human review to see whether the vocabulary clarifies ownership without erasing accepted product terms.
- **Consensus:** **Defer installation and active adoption.** Keep a source reference under the domain-model/design activity until metadata is corrected and a matching project case is evaluated.

The changed [chief-of-staff entrypoint](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/in-progress/chief-of-staff/SKILL.md) now prefers an existing shared wiki and calls retrospective/spec/ticket/implementation procedures.

- **Practitioner:** Shared notes can reduce competing stores of project memory.
- **Skeptic:** Its literal relative paths resolve under `skills/in-progress`, while the four procedure directories exist under `skills/engineering`. A flattened installed layout may make those links valid; the source-tree check alone does not prove an installed bundle is broken. The new procedure also prescribes publishing tracker artifacts and pursuing retrospective candidates, which need task scope and authority.
- **Evaluator:** Compare a raw checkout, a single-skill install and a complete flattened bundle; missing peers must be reported rather than silently installed or invoked. Test that design-only work does not publish or implement.
- **Consensus:** **Remain deferred.** Validate dependency closure and scope before reconsidering the raw coordinator. The personal router continues to use available peers without assuming a complete imported suite.

## Addy: eight changed entrypoints

All links in this section refer to [the pinned source](https://github.com/addyosmani/agent-skills/tree/8bfcc1f9916f2eea55494d8c1fa7f4bde867dd9e). These are delta reviews against the previously assessed entrypoints, with inspection depth recorded in `reviews.json`; they are not fresh full-body or end-to-end audits of every package.

| Skill | Practitioner: useful change | Skeptic: remaining limit | Evaluator: proposed falsification | Consensus |
| --- | --- | --- | --- | --- |
| browser-testing-with-devtools | Settle fonts and resize observers before layout measurement. | A delay alone cannot establish the expected rendered state. | Delayed-font/viewport case with observed stable layout. | Optional browser profile; no universal wait duration. |
| constraint-driven-development | Enforce scanner-report severity and test the actual CI command with positive/negative controls. | New JSON schemas, severity mappings and POSIX shell examples need the project's real scanner versions. | Clean, blocking, below-threshold, malformed report and scanner-error controls. | Adapt the enforcement principle; helper stays unexecuted and unpromoted. |
| context-engineering | Replace an unsupported fixed percentage with a host-aware compaction margin. | Occupancy may be unavailable and no optimal threshold is demonstrated. | Long-session retention of accepted decisions at the actual host limit. | Retain the context/handoff principle, without a universal number. |
| doubt-driven-development | Preserve contradictory callers, guards and tests when withholding the author's reasoning. | Adversarial framing still can produce unsupported findings. | A claimed defect contradicted by a reachable caller guard. | Retain counterevidence in bounded review. |
| git-workflow-and-versioning | Scan matching staged file names without printing secret values; include pasted commit-message requests. | Keyword scans are incomplete; text generation does not authorize Git mutations. | Fake credential sentinel plus a commit-message-only request. | Reference, not another broad default workflow. |
| security-and-hardening | Name session cookies and use non-value-printing shared secret-check examples. | Broad triggers and keyword limitations remain. | Concrete cookie boundary plus fake staged credential, with no secret echo. | Optional security profile with project-specific evidence. |
| shipping-and-launch | Type the React boundary's children in the example. | Type correctness does not prove recovery, rollout readiness or deployment authority. | Type-check children and observe a real fallback in a matching project. | Optional rollout profile. |
| test-driven-development | Distinguish real process termination/database rollback from injected exceptions or transaction mocks. | Real-boundary fixtures can be expensive and were not executed here. | Terminate a disposable process or force a real test-database rollback; read state separately. | Retain the behavioral-seam principle; no owned TDD change yet. |

Supporting changes were also examined:

- The new 45-line quality gate parses Semgrep/axe reports, distinguishes blocking findings from unusable input, and rejects unknown severity, incomplete scans and non-HTTP(S) pages. Static inspection does not establish compatibility with every scanner output or correctness of the page being scanned.
- The shared accessibility checklist corrects its large-text units and says not to round a failing ratio up. The security references use filename-only staged-diff matching. No separate conformance or legal conclusion is implied by these source edits.
- The simplify hook changes protected-block recovery, quoting and lock cleanup. It can restore or rewrite files, so it remains a host-specific operational dependency; it was not installed or run.
- The evaluation runner gains a single behavioral-case selector, validation for missing/unknown/duplicate IDs and diagnostics for top-k matches that are not first. Lexical ranking remains different from actual host selection and task quality.
- Added scanner tests, hook tests, secret-output tests, persistence fixtures and CI wiring demonstrate intended coverage in source, not a reproduced benchmark. Their presence alone does not prove the procedures work in this environment.

## David: ADR naming

The [changed ADR entrypoint](https://github.com/davidondrej/skills/blob/8e90e9d634983e76e66154e6b36a11d735fd19da/skills/thinking-and-docs/adr-verbatim/SKILL.md) now reads directory instructions before choosing a filename and accepts timestamp-style IDs.

- **Practitioner:** Preserves an established ADR convention rather than forcing the next sequential number.
- **Skeptic:** The existing activity still needs an approved decision and must not invent rationale or acceptance.
- **Evaluator:** Supply timestamp naming rules and an approved decision; check the filename and heading without adding unapproved content.
- **Consensus:** Keep the documentation adaptation candidate. The owned docs skill already follows the project's established home; no active wording change is justified.

## ibelick: site-only update

The tracked changes add a design-system directory and update site data, routes and tests. A scoped Git diff for `skills/`, license files, package and plugin manifests is empty. This is distinct from a changed bundled skill. Resources consumed dynamically by a profile may still change through a website, so the site update is not treated as evidence that every remote dependency is stable. No new active profile is recommended.

## Review anchors and validation

Eleven candidate assessments were updated: one new entrypoint, two complete-entrypoint reviews and eight explicit delta reviews. Prior assessed hashes and decisions for updated entries are retained in their `review_history`; unchanged entries keep their previous review anchors. Conservative source-wide fingerprints leave 124 other entries marked for renewed impact assessment rather than silently treating them as re-reviewed.

The owned 20 skills and all private material are unchanged. Structural/provenance validation passes for the 816-entry catalog. The update publisher passed the existing 14 tracker/proposal tests; the final candidate is checked again before publication. No comparative skill-quality or live integration result is claimed. The upstream YAML parse failure is a deferred candidate finding, not a failure of the owned skill pack.
