# Keep properties connected to the code

Use this for a requested invariant/model check or maintenance of existing verification. Do not introduce a proof tool simply because a change is nontrivial.

State the property, the user consequence of breaking it and the exact code it concerns. For an existing check, recover its covered symbols, assumptions, bounds, tool/command and last revision confirmed to match the implementation. Run it before editing; a green result can describe stale code. If the correspondence has no recorded anchor, identify an estimated starting revision and its uncertainty rather than claiming it was validated.

Choose evidence for the question. An event-order model can apply to a system implemented in any language. A code-level verifier must support the actual language and runtime semantics. When none is available, generated-input or property-based tests must call the shipped implementation; do not substitute a handwritten copy or call those tests formal proof. Explain tool and scope limits instead of inventing a guarantee.

Inspect changes since the anchor, including moved symbols and new writers to guarded state. Trace modeled steps and assumptions to real operations. A read followed by an awaited write is not atomic merely because the model combines them. Static types do not establish runtime input validation. Integer ranges, exceptions, cancellation and external transactions must reflect the implementation where they affect the property.

Update the model or harness from the code and intended contract, before using the result to choose the answer. Change a property only with evidence of an intentional contract change; retain the old/new meanings and that evidence. Do not weaken assumptions or reduce bounds silently to obtain a pass.

Check sensitivity with a relevant deliberate violation in disposable state. For a code-level harness, confirm that it detects the corresponding implementation break. For a separate model, relate the broken transition to a possible implementation change and replay a discovered counterexample against real code where feasible. A model-only mutation shows sensitivity of the model, not a mechanical connection to product code. Restore scratch changes and rerun the clean control. Do not claim an unperformed sensitivity check or an unbounded guarantee from bounded exploration.

For each independently maintained check, report whether it matches current code, needed an update, exposes a product bug, or is blocked. Preserve overlapping outcomes when an update reveals a bug. Advance its fidelity anchor only after inspecting the relevant correspondence and running that check; keep a blocked check's old anchor even if its neighbors passed. Record which revision, coverage, bounds and assumptions the result actually supports. A successful rerun at a new revision without a correspondence review does not renew a hand model's fidelity.

Verification-only work can change the requested models, tests, harness or recipe; it does not authorize a product fix. Report a reachable implementation failure and a modeling error separately. Use existing project reporting conventions; neither a particular renderer nor a second installed skill is required to explain the counterexample.
