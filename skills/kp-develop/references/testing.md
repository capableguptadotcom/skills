# Choose evidence that can reject a wrong solution

Name the behavior, revision, environment and expected result. Confirm that the process or deployment under test serves that revision. Reuse valid evidence already collected in the task. Select the relevant case below rather than running every mode.

| Requested work | Useful evidence |
| --- | --- |
| Test-first implementation | One failing test at an observable seam, minimum implementation, then green verification and refactoring. Confirm the initial failure expresses the missing behavior rather than an import/tool error. |
| Bug fix | A reproduction or regression that distinguishes the old failure from the correction, plus relevant neighboring cases. |
| UI behavior | Exercise the actual interaction and recovery state. Match the viewport and starting state for comparisons; let asynchronous layout/font changes settle before measurement. A screenshot alone does not prove an interaction. |
| Performance | The same correct workload and conditions before and after, with absolute measurements and the limiting factor. |
| Persistence, termination or rollback | Exercise the real disposable process or database boundary. An injected exception is not process termination, and a transaction mock is not a rollback. |
| Small text/config edit | A proportionate content or command check; do not install an unrelated toolchain. |

Use the project's existing runner and public seam. Prefer representative outcomes over internal call order or mocks that hide the contract. Work one behavior at a time in TDD; do not generate a speculative full suite before implementing the first case.

Inspect the actual output. A report file, process exit code, test count or review score alone cannot establish the behavior. When a command is meant to enforce a threshold, check a known violation and a clean control before calling the gate effective. Mark targets passed, failed or untested with a reason. Keep captures local unless their publication destination is authorized; synthetic footage is not application evidence.
