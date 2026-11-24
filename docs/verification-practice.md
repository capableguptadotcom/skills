# Verification wording: observed behavior and limits

31 October 2026. These are targeted smoke tests of the two conditional verification references added to `kp-develop`, not an evaluation of all pstack skills or a comparison with a baseline. The fixtures were authored for this pass. Their deliberate defects are not findings in the user's products. Raw private sessions were not used.

## Method and exact instructions

One fresh agent received three realistic requests and raw fixture repositories. A separate fresh agent received the runtime-recipe request. Both were explicitly pointed to `kp-develop`; neither was given the intended defect, expected answer, prior research conclusions or scoring rules. They could write verification artifacts in their fixture only, with no product edits, installations, commits or publication. The first three tasks shared one agent session and are not independent replicates.

The actual instruction-file SHA-256 values are preserved in [instruction-hashes.json](../eval/verification-practice/instruction-hashes.json). The entrypoint and references were unchanged while these exercises ran. Agents reported which references they read. The first read testing/properties, while the runtime task read testing/project-verification. This is limited evidence of conditional reading during explicit invocation, not evidence of automatic skill discovery or long-session retention.

## Outcomes inspected

| Request | Actual observation | Boundary and limitation |
| --- | --- | --- |
| Reconcile a Python lease model after a refactor; verification artifacts only. | The old atomic model passed. The current implementation cached a free-owner read before an await. The agent updated the model, replayed six event orders against the shipped method in two initial states, and found duplicate successful claims in four initially-free schedules. | It kept the property and product code unchanged, labeled model drift separately from the exposed bug, and distinguished bounded correspondence from unbounded proof. It advanced only the inspected check's fidelity anchor. |
| Account for a second, unavailable check in that profile. | The archive runner and external proof were unavailable. The record retained its old anchor and marked the check blocked/untested. | This fixture deliberately included the missing dependency. It is not a runtime failure in the skills repository. A neighboring successful check did not erase that gap. |
| Create repeatable verification for a shipped JavaScript integer-range function. | Tests imported the actual module and exposed lexical sorting. Example: `(2, 10)` produced `[10, 2]`. Four contract groups failed, totaling 1,245 failures across 5,276 sampled pairs. The groups can overlap. | The report called this bounded/generated testing, not formal proof. The library remained unchanged. An initial sensitivity expectation was wrong and was corrected from three mismatches to two; that verification error was recorded separately. |
| Describe checks for an agreed single log-label edit, answer only. | The agent recommended exact-diff/config checks and an optional readily available log exercise. | It did not propose a new model, harness or dependency. No actual label edit was made, so this is a response-boundary observation only. |
| Create and prove a reusable recipe for a Python Notes API. | From an empty owned data directory, health answered 200 while the usable list still answered 503. The recipe waited, created a note through HTTP, checked list and disk state, restarted the owned process, and observed persistence. | Both child processes stopped, scratch data was removed and evidence survived. The source hash stayed unchanged. Only one sequential path was exercised; failure-cleanup branches and concurrent writes were not fault-injected. |

The parent inspected the produced code, coverage records and evidence, then reran the Python model and sensitivity commands, JavaScript tests and Notes recipe. The same contract failures and successful controls were observed. A parent rerun is a reproducibility check of the generated artifact, not another independent agent trial. Both Notes runs retained HTTP exchanges, matching source hashes, exited-child records and absent scratch state.

See [the first agent's structured observations](../eval/verification-practice/observations.json), [runtime observations](../eval/verification-practice/notes-api/observations.json), [agent runtime evidence](../eval/verification-practice/notes-api/run-k5ulf_80-evidence.json) and [parent runtime evidence](../eval/verification-practice/notes-api/run-42y4jbqg-evidence.json). Workstation paths in saved records are replaced with descriptive placeholders. Fixture Git anchors identify the original disposable history, not revisions in this public repository. The Python baseline and current implementation are preserved so that the semantic change can be inspected without those Git objects.

## Repeat the artifact checks

The [synthetic fixtures](../eval/verification-practice/) preserve product inputs, generated verification code and the runtime recipe. From each named directory:

```sh
# eval/verification-practice/lease-service
python -B verification/model.py
# Expected exit 1: the unchanged fixture violates uniqueness.
python -B verification/sensitivity.py
# Expected exit 0: clean control passes and the deliberate violation is detected.

# eval/verification-practice/range-library
node --test verification/range.test.mjs
# Expected exit 1: four contract groups expose the unchanged fixture defect.

# eval/verification-practice/notes-api
python verification-results/verify_notes.py
# Expected exit 0: creates disposable loopback instances and retains evidence locally.
```

Python 3.12.3 and Node 22.14.0 were used. The runtime helper also reads the enclosing Git revision and source hash. It uses Python assertions; do not invoke it with optimization enabled. Retained run directories are local evidence, not files to commit automatically. These deliberately failing product fixtures are separate from the repository's package validation suite.

## What this does not establish

There is no old-wording/no-skill comparison, repeated model-family experiment, automatic-selection test or sustained daily-use result. The requests were synthetic, short and explicitly invoked. No actual TLC/proof-assistant toolchain, pstack helper, renderer, remote deployment, cancellation path or multiprocess race was run. The observations support keeping these references as a provisional proposal; they do not establish improved correctness, an optimal eight-skill composition, or why Claude and Codex select skills differently.
