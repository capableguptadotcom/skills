# Design from concrete scenarios

Read representative callers, product terms, invariants and the owner of state or transactions. Resolve overloaded terms with a normal scenario and an invalid or concurrent case; do not silently rename the user's domain.

For a consequential interface choice, show materially different caller examples. Compare ease of correct use, hidden complexity, failure behavior and compatibility. Preserve the project's architecture when it fits. A single caller can justify a boundary for transactions, isolation or meaningful complexity; reuse alone does not decide the shape.

Prefer a simpler design when it meets every requirement. Do not reduce scope merely to shorten the implementation. Recommend a boundary and a caller-level check that could expose a mistake.

When one uncertainty needs an experiment, state the observation that would favor each option. Propose the cheapest prototype; build it only when the experiment is requested or already within the task. Keep disposable code and mock data out of production paths, run the experiment and report what its simplifications leave unresolved. A successful prototype does not establish production readiness.
