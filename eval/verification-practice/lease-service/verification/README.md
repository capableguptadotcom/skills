# Lease verification correspondence

The contract is unchanged: at most one worker may receive a successful claim for the same initially free lease; failed claims return False. A duplicate success allows two workers to act as owner. The README authorizes a transport checkpoint, not a change to exclusivity.

The old model passed before editing (`python verification/model.py`), but combined the read and write into one atomic operation. Its recorded correspondence anchor was `95897e1dd5735d9446cad43fee48f6b4bee15c5e`. Reviewing `git diff 95897e1 -- lease.py` through current revision `7a18e84d099e399f80ff427a8c5962e2c0969171` shows a cached `free` read followed by `await checkpoint()` before writing `owner`. The only product writes are initialization and the assignment in `claim`; no moved claim or new owner writer was found in this fixture.

`model.py` now separates each worker's read/checkpoint from resume/write. It enumerates all six orders respecting each worker's program order, for both a free and an occupied initial state. Its results and final owner are compared against deterministic checkpoint-gated executions of the imported shipped `Lease.claim`. Read maps to `free = self.owner is None` before the await; resume maps to the cached condition, optional owner assignment, and boolean return. The main property was retained; it was not weakened to match the refactor.

Run from the repository root with Python 3.12.3:

```sh
python -B verification/model.py
python -B verification/sensitivity.py
```

Current results:

- Model/code outcomes match in all 12 bounded executions.
- Uniqueness fails in four of six free-lease schedules, so the main command exits 1.
- All six occupied-lease schedules return False to both claimants and preserve the existing owner.
- Counterexample: a reads free; b reads free; a resumes and succeeds; b resumes and also succeeds. Final owner is b, but both callers received True. This is a reachable product failure, distinct from the former modeling error.
- Sensitivity exits 0: a source-derived in-memory control moves the checkpoint before the free read and has zero violations. A deliberate mutation restores the stale-read ordering and yields four violations. The mutated source equals shipped source. Neither variant is written to the product. The final main run still fails against unchanged shipped code.

The lease correspondence anchor can advance to the inspected current revision despite the failing property: it records fidelity, not correctness. `checks.json` retains both outcomes (model needed an update and current product violates the property). The independent archive check remains blocked: `proof-runner` is not available and the external adapter/proof source is absent. Its initial-version anchor is retained; `archive.md` is unchanged.

Limits: two workers with one claim each, single event loop, normal checkpoint returns, no exceptions/cancellation, no external owner mutation, no release/reclaim cycles, no distributed or multi-process behavior. This is bounded event-order exploration with real-code replay, not unbounded proof or mechanical refinement certification.
