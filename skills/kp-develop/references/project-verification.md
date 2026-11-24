# Make a project's real behavior repeatable

Use this when the task asks for a reusable verification recipe or maintenance of one. An ordinary change does not need a new skill or feature inventory. Prefer the project's existing tests, harness and documentation home; create a project-local skill only when that is the requested artifact.

Inspect how the project starts, what a user drives, required data/authentication, observable results and how concurrent runs isolate state. Use actual repository commands and available host tools. A Python API, JavaScript CLI and browser UI need different driving instructions, even when their evidence requirements are the same.

Record only the recipe's needed details:

- How to start an owned disposable instance and confirm its revision and usable state. An answering port does not establish that migrations, seeds or authentication finished.
- How to exercise the public path with the required preconditions and check its visible result and relevant persistent side effects.
- Where to retain the input/action, output and supporting captures. A final screenshot alone cannot establish an interaction.
- How to stop the processes and remove the scratch state this run created while preserving its evidence. Clean failed attempts too, at their actual lifetime; do not tear down a shared instance between features that still need it.

Follow the recipe once before presenting it as runnable. Inspect the evidence after cleanup. If a stand-in supplied prerequisites absent on the intended target, identify what remains untested there. Missing seed data or an inaccessible feature is a coverage gap, not a reason to weaken the promised behavior.

For maintenance, compare the requested coverage with source changes and drive the affected paths. A requested full-map audit needs every mapped feature accounted for; a narrow change does not imply that audit. After surprising behavior, recheck instance identity/readiness and reset the affected state before continuing.

Separate an outdated description, a broken driving helper, a product regression and an unmet prerequisite. Correct only the artifacts in the authorized scope. Re-drive a changed helper before claiming it works; report product defects separately when product edits were not requested. Delegation, external publication and scheduling depend on the current task and host, not this recipe.
