# Notes API verification recipe

From the Notes API directory, run:

```powershell
python verification-results/verify_notes.py
```

Requires Python 3 and Git already available on PATH. Uses the project's actual server and Python standard-library HTTP client; installs nothing and contacts only loopback. Run without Python's optimization flags because the behavioral checks use assertions.

The script creates a unique run directory here and an initially empty scratch data directory. It launches its own `server.py` on port 0 and reads that child's announced port. Evidence records the exact launch arguments, PID, working directory, Git HEAD, Python version, and server source SHA-256 before and after the run. The source hash identifies the actual file used even if the checkout contains uncommitted changes.

Success requires these observations in order:

1. GET `/health` returns 200. GET `/notes` is separately polled until 200, accepting only the documented initializing response (503) while waiting. Health alone does not establish storage readiness.
2. The usable fresh list is empty. POST `/notes` with the recorded title returns 201 and note ID 1. GET `/notes` returns that note.
3. The real `notes.json` contains the same list. A retained snapshot records that side effect.
4. Stop the owned process, restart with the same scratch directory, and wait for `/notes` readiness again. The note survives restart.
5. Stop only the child processes this script created, remove their scratch data, and preserve requests, logs, snapshot, and final evidence. Cleanup also runs after a failed attempt.

The printed JSON points to `run-*/evidence.json`. Inspect its actual request inputs/outputs, checks, source hashes, `confirmed_exited`, and `scratch_removed`, together with both process logs and the saved disk snapshot. A zero exit alone is insufficient evidence. A failed run exits nonzero and retains its traceback and logs. If cleanup reports failure, use the recorded PID and scratch path to investigate ownership before taking further action.

This is one sequential create/read/durability path. It does not test concurrent writers, malformed payloads, validation, deletion, authorization, remote deployment, or behavior after forced interruption during a write. No external prerequisites or stand-ins are used.
