"""Run from any directory with Python 3; uses only the standard library."""
import hashlib
import json
import re
import shutil
import subprocess
import sys
import tempfile
import time
import traceback
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SERVER = ROOT / "server.py"
RESULTS = Path(__file__).resolve().parent


def digest():
    return hashlib.sha256(SERVER.read_bytes()).hexdigest()


def main():
    run = Path(tempfile.mkdtemp(prefix="run-", dir=RESULTS))
    scratch = run / "scratch-data"
    scratch.mkdir()
    evidence = {
        "started_utc": datetime.now(timezone.utc).isoformat(),
        "python": sys.version,
        "root": str(ROOT),
        "server_sha256_before": digest(),
        "fresh_directory_empty": not any(scratch.iterdir()),
        "processes": [],
        "requests": [],
        "checks": [],
    }
    process = None
    streams = []
    try:
        def start(label):
            nonlocal process, streams
            command = [sys.executable, "-u", str(SERVER),
                       "--data-dir", str(scratch), "--port", "0"]
            stdout = run / f"{label}-stdout.log"
            streams = [stdout.open("w", encoding="utf-8"),
                       (run / f"{label}-stderr.log").open("w", encoding="utf-8")]
            process = subprocess.Popen(
                command, cwd=ROOT, stdout=streams[0], stderr=streams[1],
                creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0),
            )
            evidence["processes"].append({
                "label": label, "command": command, "pid": process.pid,
                "cwd": str(ROOT), "server_sha256": digest(),
            })
            deadline = time.monotonic() + 10
            while time.monotonic() < deadline:
                if process.poll() is not None:
                    raise RuntimeError(f"Server exited before port announcement: {process.returncode}")
                match = re.search(r"^port=(\d+)$", stdout.read_text(encoding="utf-8"), re.M)
                if match:
                    port = int(match.group(1))
                    evidence["processes"][-1]["port"] = port
                    return f"http://127.0.0.1:{port}"
                time.sleep(0.05)
            raise TimeoutError("No port announcement within 10 seconds")

        def stop():
            nonlocal process, streams
            if process is not None:
                if process.poll() is None:
                    process.terminate()
                    try:
                        process.wait(timeout=5)
                    except subprocess.TimeoutExpired:
                        process.kill()
                        process.wait(timeout=5)
                evidence["processes"][-1]["exit_code_after_owned_stop"] = process.returncode
                evidence["processes"][-1]["confirmed_exited"] = process.poll() is not None
                process = None
            for stream in streams:
                stream.close()
            streams = []

        def request(base, path, payload=None):
            method = "GET" if payload is None else "POST"
            raw = None if payload is None else json.dumps(payload).encode("utf-8")
            req = urllib.request.Request(
                base + path, data=raw, method=method,
                headers={"Content-Type": "application/json"},
            )
            try:
                response = urllib.request.urlopen(req, timeout=2)
            except urllib.error.HTTPError as error:
                response = error
            with response:
                body = json.loads(response.read().decode("utf-8"))
                status = response.status
            evidence["requests"].append({
                "utc": datetime.now(timezone.utc).isoformat(),
                "method": method, "url": base + path, "input": payload,
                "status": status, "output": body,
            })
            return status, body

        def ready(base):
            deadline = time.monotonic() + 10
            while time.monotonic() < deadline:
                status, body = request(base, "/notes")
                if status == 200:
                    return body
                assert (status, body) == (503, {"error": "initializing"}), (status, body)
                time.sleep(0.1)
            raise TimeoutError("Notes were not usable within 10 seconds")

        revision = subprocess.run(
            ["git", "rev-parse", "HEAD"], cwd=ROOT,
            capture_output=True, text=True, check=True,
        )
        evidence["git_head"] = revision.stdout.strip()
        base = start("initial")
        assert request(base, "/health") == (200, {"process": "up"})
        assert ready(base) == [], "Fresh state must contain no notes"
        evidence["checks"].append("Fresh /notes became usable and returned []")
        title = "Verification note: create, list, persist"
        expected = {"id": 1, "title": title}
        assert request(base, "/notes", {"title": title}) == (201, expected)
        assert request(base, "/notes") == (200, [expected])
        disk = json.loads((scratch / "notes.json").read_text(encoding="utf-8"))
        assert disk == [expected]
        (run / "persisted-notes-snapshot.json").write_text(json.dumps(disk, indent=2) + "\n", encoding="utf-8")
        evidence["checks"].append("POST returned 201; GET and notes.json contained the same note")
        stop()
        base = start("restart")
        assert ready(base) == [expected], "Note must survive a process restart"
        evidence["checks"].append("GET after owned process restart retained the note")
        evidence["status"] = "passed"
    except BaseException:
        evidence["status"] = "failed"
        evidence["error"] = traceback.format_exc()
    finally:
        try:
            stop()
            shutil.rmtree(scratch)
        except BaseException:
            evidence["status"] = "failed"
            evidence["cleanup_error"] = traceback.format_exc()
        evidence["scratch_removed"] = not scratch.exists()
        evidence["server_sha256_after"] = digest()
        if evidence["server_sha256_after"] != evidence["server_sha256_before"]:
            evidence["status"] = "failed"
            evidence["source_changed_during_run"] = True
        evidence["finished_utc"] = datetime.now(timezone.utc).isoformat()
        (run / "evidence.json").write_text(json.dumps(evidence, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": evidence["status"], "evidence": str(run / "evidence.json")}))
    return 0 if evidence["status"] == "passed" else 1


if __name__ == "__main__":
    raise SystemExit(main())
