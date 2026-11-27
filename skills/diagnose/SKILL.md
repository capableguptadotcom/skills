---
name: diagnose
description: Use first for any bug - an error, a failing or flaky test, a wrong result, a crash or a slowdown - including when the user already names a suspected cause. Reproduces before fixing, tests competing causes, and fixes the code that owns the defect without hiding the symptom.
---

# Diagnose from evidence

This skill does one thing: it finds the cause of a concrete failure and proves it. A diagnosis-only request ends with the report, not a fix.

1. **Pin the failure.** Record expected behavior, actual behavior, a reproducible input and the revision and environment. Check: you can trigger the failure on demand, or you state why you cannot.
2. **Follow the failing path** across its real boundaries: process, network, database, queue, configuration. Keep repository facts separate from hypotheses.
3. **Rank competing causes.** For each, name a check whose result would reject it. A dependency outage, a missing credential and a code defect need different checks and different remedies.
4. **Run the cheapest discriminating check first.** Change one variable at a time. Inspect the output and revise the ranking.
5. **For a performance problem,** read [performance](references/performance.md) before measuring.
6. **Report** with [the diagnosis template](assets/diagnosis.md): cause, evidence, rejected causes, remaining uncertainty and the smallest correction.
7. **Fix only when asked.** Write a failing check for the defect first when practical, change the code that owns the defect, then rerun the reproduction and the relevant regression checks. A guard or retry that hides the symptom is not a fix unless the state it handles is legitimate.
