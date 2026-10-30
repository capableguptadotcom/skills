"""Fetch candidates in an isolated worktree and publish one reusable update PR."""

import argparse
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import uuid

from upstreams import ROOT, git

BRANCH_PREFIX = "automation/upstream-skills"
FILES = ["upstream.lock.json", "catalog.json", "docs/catalog.md", "docs/upstream-changes.json"]


def run(args, cwd):
    return subprocess.check_output(args, cwd=cwd, text=True, encoding="utf-8").strip()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--publish", action="store_true", help="Push candidate data and create/update the PR")
    args = parser.parse_args()
    if git(ROOT, "remote", "get-url", "origin") not in (
        "https://github.com/capableguptadotcom/skills.git", "git@github.com:capableguptadotcom/skills.git"
    ):
        raise SystemExit("Unexpected origin; refusing to publish")
    git(ROOT, "fetch", "origin", "main")
    prs = json.loads(run(["gh", "pr", "list", "--repo", "capableguptadotcom/skills",
                          "--state", "open", "--limit", "100", "--json", "headRefName,url"], ROOT))
    proposal = next((p for p in prs if p["headRefName"].startswith(BRANCH_PREFIX)), None)
    branch = proposal["headRefName"] if proposal else f"{BRANCH_PREFIX}-{uuid.uuid4().hex[:8]}"
    base = "origin/main"
    if proposal:
        git(ROOT, "fetch", "origin", branch)
        base = "FETCH_HEAD"
    # Never checkout, stage or commit the user's working tree. A linear push
    # preserves an existing proposal; concurrent updates fail without force.
    with tempfile.TemporaryDirectory(prefix="kp-skills-update-") as tmp:
        workspace = Path(tmp) / "checkout"
        git(ROOT, "worktree", "add", "--detach", str(workspace), base)
        try:
            if base == "FETCH_HEAD":
                git(workspace, "merge", "--no-edit", "origin/main")
            run([sys.executable, "scripts/upstreams.py", "--refresh", "--write"], workspace)
            run([sys.executable, "scripts/validate.py"], workspace)
            run([sys.executable, "-m", "unittest", "discover", "-s", "tests", "-v"], workspace)
            git(workspace, "diff", "--check")
            if not git(workspace, "status", "--porcelain", "--", *FILES):
                print("No upstream changes; no commit or PR needed.")
                return
            if not args.publish:
                print(git(workspace, "diff", "--stat"))
                print("Preview only. Run with --publish to propose the verified candidate data.")
                return
            git(workspace, "add", "--", *FILES)
            git(workspace, "commit", "-m", "chore: refresh upstream skill candidates")
            git(workspace, "push", "origin", f"HEAD:refs/heads/{branch}")
            body = Path(tmp) / "body.md"
            body.write_text(
                "Upstream files changed since the previous observation. This updates pinned candidate metadata, "
                "file hashes, and the catalog; active skills and reviewed decisions are preserved.\n\n"
                "Review docs/upstream-changes.json for added, removed, and changed files, including scripts, "
                "references, licenses and assets. Changed tracked source files invalidate previous review status. "
                "Reassess affected dependencies and compare candidate behavior before promoting wording into skills/.\n\n"
                "Validation: structural/provenance checks, tracker unit tests, and git diff --check. "
                "These checks do not demonstrate behavioral uplift.\n", encoding="utf-8"
            )
            found = run(["gh", "pr", "list", "--repo", "capableguptadotcom/skills", "--head", branch,
                         "--state", "open", "--json", "url", "--jq", ".[0].url // empty"], workspace)
            if found:
                run(["gh", "pr", "edit", found, "--body-file", str(body)], workspace)
                print(found)
            else:
                print(run(["gh", "pr", "create", "--repo", "capableguptadotcom/skills", "--head", branch,
                           "--base", "main", "--draft", "--title", "Review upstream skill updates", "--body-file", str(body)], workspace))
        finally:
            # workspace is created above inside this tool-owned absolute temp root.
            # Git removes this exact registered worktree; no recursive shell delete.
            if workspace.resolve().parent != Path(tmp).resolve():
                raise RuntimeError("Unexpected temporary worktree target")
            git(ROOT, "worktree", "remove", "--force", str(workspace))


if __name__ == "__main__":
    main()
