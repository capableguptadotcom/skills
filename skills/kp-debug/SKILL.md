---
name: kp-debug
description: Diagnose a concrete bug, failing check, or performance regression by reproducing it and testing competing causes. Respect diagnosis-only requests.
---

# Diagnose from evidence

Identify expected behavior, actual behavior, a reproducible input, and the affected revision/environment. Follow the failing path across its actual boundaries. Keep repository facts distinct from hypotheses.

Choose a discriminating check: state what result supports a hypothesis and what result rejects it. Run the smallest useful experiment, inspect its output, and revise the explanation. Avoid changing several variables before learning which matters.

For a fix, establish a failing behavioral check first when practical, change the owner of the defect, and rerun the reproduction plus relevant regression checks. A dependency outage, missing credential, and code defect need different remedies.

For a diagnosis-only request, report the cause, evidence, remaining uncertainty, and smallest proposed correction without editing. For performance, compare the same workload and include absolute measurements; a faster wrong result is a failure.
