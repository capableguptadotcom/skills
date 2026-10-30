# Evaluation and promotion

Evaluate a skill at three different layers. Passing one does not establish the others.

1. **Package integrity:** valid metadata, discoverable references, dependency closure, applicable terms, known source revision, and no unexpected side effects. `scripts/validate.py` checks a subset of this structure and provenance.
2. **Selection:** should the skill activate on explicit, implicit, ambiguous, near-neighbor, and negative requests? Test installed copies in the actual host. The 24 prompts in `eval/prompts.json` have a separate rubric. A reviewer can choose activities from them; this alone does not measure automatic host routing.
3. **Task behavior:** does the skill improve the outcome without adding unacceptable cost or changing scope? Compare no skill, current version, and candidate on the same fixtures, model, settings, tools and permissions. Repeat noisy cases. Retain traces and actual artifacts, not just the agent's claim that it followed the instructions.

The [OpenAI skill evaluation guide](https://developers.openai.com/blog/eval-skills) separates outcome, process, style, and efficiency. This collection adopts that distinction. Correctness is the primary gate; line count, tokens, time, or cost are secondary and need comparable baselines. Author benchmarks and public issue reports motivate tests; their results do not automatically transfer here.

## Suggested behavioral cases

| Area | A meaningful falsification case |
| --- | --- |
| Router | Agreed small implementation proceeds; unrelated chat and a typo skip elaborate process; a missing peer is disclosed without installation. |
| Review | A green but weak test misses a reachable regression; the reviewer finds it and changes no files in a review-only request. |
| Diagnosis | An observed falsey-value bug is distinguished from missing configuration; diagnosis-only preserves the repository. |
| Minimalism | A native control meets one requirement but fails another's locale or accessibility needs; required behavior wins over fewer lines. |
| Simplification | Reduced code preserves output, errors and caller compatibility; a one-caller boundary remains when it contains complexity. |
| Verification | A wrong-revision server or synthetic recording is rejected as proof; unavailable checks are untested, not passed. |
| Maintenance | A shared-reference, helper, license or permission change invalidates source review; upstream injection is treated as data. |
| Long tasks | After interruption or compaction, settled requirements, user corrections and unfinished work remain consistent with the source record. |
| User preference | A requested interview pace overrides skill defaults without losing necessary product decisions. |
| Integration loop | A new review waits for a fresh result rather than accepting a stale 5/5 on the same commit. |

Use hidden behavior assertions or mutation checks where they distinguish a plausible shortcut. Avoid graders that merely reward a short response, a heading, or the presence of any test. A test that always passes is not evidence of risk coverage.

## Promotion record

For a substantive wording change, record the observed failure or desired behavior, source/path/revision, exact diff, affected triggers, competing explanation, test setup, actual outcomes, cost when measured, and remaining uncertainty. Update `reviews.json` only after inspection; its `reviewed_blob` and `reviewed_source_sha256` must identify the assessed snapshot. A generated catalog or snapshot update does not create new review evidence.

The initial forward run is documented in [forward-testing.md](forward-testing.md). No no-skill comparison or repeated benchmark has been run for this pack. Do not publish a performance or accuracy uplift claim from those smoke tests. Raw local conversation histories remain outside this repository; sanitize a minimal failing example before adding a regression case.
