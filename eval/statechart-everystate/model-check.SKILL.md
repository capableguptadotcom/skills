---
name: model-check
description: Model-checks a small TLA+ model of steps that can interleave, repeat or fail (double submits, retries, leases, locks, state machines) with everystate, and retells any bug as numbered steps in the product's words. Use when asked whether steps can happen in a bad order. Runs `npx everystate`, so it needs Node.
disable-model-invocation: true
---

# Check a flow's states

A test checks the orders someone wrote down. A model checker checks every order of steps in a small model. Use it when the answer depends on how requests, retries or workers interleave.

1. **Name the promise.** One sentence the code must keep, the harm when it breaks, and the lines that keep it: "an order is charged at most once" in `checkout.ts`. Check: you can point at those lines.
2. **Model the steps.** Keep the model out of the product code, in a new `.model/` folder at the project root; tell the user it can be deleted, or keep it if they want the check. One variable per piece of state that matters, one action per step that can interleave with another. A read and a later write are two actions unless a lock or a transaction makes them one, and every `await` between them is a point where another request can run. Include the failures the code handles or ignores: a timeout whose request still arrived, a crash between two writes, a retry. Name each action after what happens and put the function it stands for in a comment. Check: every action maps to a line range.
3. **Bound it and state the rules.** Small constants in the `.cfg`: two requests or workers, at most three retries. A type invariant first, then the promise as an `INVARIANT`. Check: the model is finite.
4. **Run it.** From the project root, without `cd`: `npx --yes everystate@0.4.1 -json .model/Spec.tla > .model/result.json` (it reads `.model/Spec.cfg`). Exit 0: every reachable state holds the rules. 11 deadlock, 12 a rule breaks, 13 a liveness property breaks, 150/151 the spec or `.cfg` does not parse, 255 another error such as a failed `Assert`. Check: `result.json` holds one JSON line.
5. **Retell it in the product's words.** Read the `trace` in `result.json` and write the bug path as numbered steps: what happens at each step, in words the reader uses, not TLA+ names. Check: no step is a TLA+ name or a variable dump.
6. **Connect it to the code.** On a broken rule, replay the path against the real code where that is cheap (a test that forces the same interleaving), or say it was not replayed. On a pass, break the model the way the code could break (drop the guard, split the atomic step) and confirm the checker catches it. Check: one replay or one deliberate break, or a stated reason.
7. **Report.** The verdict, the path, the fix it points to, the bounds and what the model leaves out. A pass covers the model at those bounds, not the code. Do not change product code unless asked.
