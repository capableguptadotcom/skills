"""Exercise proposal Git operations with local remotes and fake service boundaries.

The fake producer supplies candidate files; it does not test upstream inventory.
Validation and a small fixture unittest suite run as real subprocesses. GitHub
state is simulated, while staging, commits, merges, pushes, and cleanup are real.
"""

import contextlib
import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import propose_update


def local_git(path, *args):
    return subprocess.check_output(
        ["git", "-C", str(path), *args], text=True, encoding="utf-8",
        stderr=subprocess.PIPE,
    ).strip()


class ProposalIntegrationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="kp-proposal-test-")
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.root = self.base / "primary"
        self.remote = self.base / "origin.git"
        self.root.mkdir()
        self.remote.mkdir()
        local_git(self.remote, "init", "--bare", "--initial-branch=main")
        local_git(self.root, "init", "-b", "main")
        for key, value in (
            ("user.name", "Proposal Test"), ("user.email", "test@example.invalid"),
            ("commit.gpgsign", "false"), ("core.autocrlf", "false"),
            ("core.longpaths", "true"), ("core.hooksPath", str(self.base / "no-hooks")),
        ):
            local_git(self.root, "config", key, value)
        (self.root / "scripts").mkdir()
        (self.root / "tests").mkdir()
        (self.root / "skills").mkdir()
        (self.root / "skills/keep.md").write_text("Curated wording stays owned.\n", encoding="utf-8")
        (self.root / "decisions.json").write_text('{"reviewed": true}\n', encoding="utf-8")
        (self.root / ".gitattributes").write_text("*.json text eol=lf\n*.md text eol=lf\n", encoding="utf-8")
        (self.root / "unrelated.txt").write_text("Committed unrelated work.\n", encoding="utf-8")
        (self.root / "scripts/validate.py").write_text(
            "import json\nfrom pathlib import Path\n"
            "for name in ('upstream.lock.json', 'catalog.json', 'docs/upstream-changes.json'):\n"
            "    value = json.loads(Path(name).read_text(encoding='utf-8'))\n"
            "    assert isinstance(value['generation'], int)\n", encoding="utf-8",
        )
        (self.root / "tests/test_candidate.py").write_text(
            "import json\nfrom pathlib import Path\nimport unittest\n\n"
            "class CandidateTests(unittest.TestCase):\n"
            "    def test_candidate_outputs_agree(self):\n"
            "        names = ('upstream.lock.json', 'catalog.json', 'docs/upstream-changes.json')\n"
            "        values = [json.loads(Path(n).read_text())['generation'] for n in names]\n"
            "        self.assertEqual(len(set(values)), 1)\n"
            "        self.assertEqual(Path('docs/catalog.md').read_text().strip(), f'Candidate {values[0]}')\n"
            "        self.assertFalse(Path('tests/fail.marker').exists())\n",
            encoding="utf-8",
        )
        self.generation = 0
        self.crlf = False
        self.failure = None
        self.write_candidate(self.root)
        local_git(self.root, "add", ".")
        local_git(self.root, "commit", "-m", "seed fixture")
        local_git(self.root, "remote", "add", "origin", str(self.remote))
        local_git(self.root, "push", "-u", "origin", "main")
        local_git(self.root, "switch", "-c", "user-work")
        self.prs = []
        self.github_events = []
        self.workspaces = []
        self.real_run = propose_update.run

    def write_candidate(self, workspace):
        for name in propose_update.FILES:
            path = workspace / name
            path.parent.mkdir(parents=True, exist_ok=True)
            text = f"Candidate {self.generation}\n" if name.endswith(".md") else json.dumps({"generation": self.generation}) + "\n"
            path.write_bytes(text.replace("\n", "\r\n").encode() if self.crlf else text.encode())

    def fake_run(self, argv, cwd):
        workspace = Path(cwd)
        if argv[:2] == [sys.executable, "scripts/upstreams.py"]:
            if self.failure == "producer":
                raise RuntimeError("Fixture producer failed")
            self.write_candidate(workspace)
            if self.failure == "validation":
                (workspace / "catalog.json").write_text("invalid JSON", encoding="utf-8")
            if self.failure == "tests":
                (workspace / "tests/fail.marker").touch()
            return "Fixture candidate produced"
        if argv[0] != "gh":
            return self.real_run(argv, cwd)
        action = argv[2]
        if action == "list":
            open_prs = [p for p in self.prs if p["state"] == "open"]
            if "--head" in argv:
                branch = argv[argv.index("--head") + 1]
                return next((p["url"] for p in open_prs if p["headRefName"] == branch), "")
            return json.dumps([{k: p[k] for k in ("headRefName", "url")} for p in open_prs])
        body = Path(argv[argv.index("--body-file") + 1]).read_text(encoding="utf-8")
        self.assertIn("active skills and reviewed decisions are preserved", body)
        if action == "create":
            branch = argv[argv.index("--head") + 1]
            # A PR cannot be created until its branch actually reached the remote.
            published = local_git(self.remote, "rev-parse", f"refs/heads/{branch}")
            pr = {"headRefName": branch, "url": f"https://example.invalid/pr/{len(self.prs) + 1}",
                  "state": "open", "draft": "--draft" in argv, "published_head": published,
                  "base": argv[argv.index("--base") + 1], "body": body}
            self.prs.append(pr)
            self.github_events.append(("create", pr["url"]))
            return pr["url"]
        if action == "edit":
            pr = next(p for p in self.prs if p["url"] == argv[3] and p["state"] == "open")
            pr["body"] = body
            pr["published_head"] = local_git(self.remote, "rev-parse", f"refs/heads/{pr['headRefName']}")
            self.github_events.append(("edit", pr["url"]))
            return ""
        raise AssertionError(f"Unexpected GitHub action: {argv}")

    def checked_git(self, path, *args):
        if Path(path) == self.root and args == ("remote", "get-url", "origin"):
            # Only the identity check is faked. All fetches/pushes target the
            # fixture's local bare origin, never GitHub or another network URL.
            return "https://github.com/capableguptadotcom/skills.git"
        result = local_git(path, *args)
        if args[:2] == ("worktree", "add"):
            self.workspaces.append(Path(args[-2]))
        return result

    def snapshot_primary(self):
        files = {str(p.relative_to(self.root)): p.read_bytes() for p in self.root.rglob("*")
                 if p.is_file() and ".git" not in p.relative_to(self.root).parts}
        return {
            "files": files,
            "head": local_git(self.root, "rev-parse", "HEAD"),
            "branch": local_git(self.root, "symbolic-ref", "--short", "HEAD"),
            "status": local_git(self.root, "status", "--porcelain=v1", "--untracked-files=all"),
            "staged": local_git(self.root, "diff", "--cached", "--binary"),
            "unstaged": local_git(self.root, "diff", "--binary"),
        }

    def remote_refs(self):
        return local_git(self.remote, "show-ref")

    def invoke(self, publish=True):
        before = self.snapshot_primary()
        argv = ["propose_update.py"] + (["--publish"] if publish else [])
        try:
            with patch.object(propose_update, "ROOT", self.root), \
                 patch.object(propose_update, "git", self.checked_git), \
                 patch.object(propose_update, "run", self.fake_run), \
                 patch.object(sys, "argv", argv), contextlib.redirect_stdout(io.StringIO()):
                propose_update.main()
        finally:
            self.assertEqual(self.snapshot_primary(), before, "The user's checkout changed")
            listed = local_git(self.root, "worktree", "list", "--porcelain")
            registered = [Path(line.removeprefix("worktree ")).resolve()
                          for line in listed.splitlines() if line.startswith("worktree ")]
            self.assertEqual(registered, [self.root.resolve()])
            self.assertTrue(self.workspaces, "No real temporary worktree was exercised")
            self.assertTrue(all(not p.exists() for p in self.workspaces))

    def remote_generation(self, branch, name="catalog.json"):
        return json.loads(local_git(self.remote, "show", f"{branch}:{name}"))["generation"]

    def test_line_ending_only_candidate_creates_no_commit_or_pr(self):
        self.crlf = True
        refs = self.remote_refs()
        commits = local_git(self.root, "rev-list", "--all", "--count")
        self.invoke()
        self.assertEqual(self.remote_refs(), refs)
        self.assertEqual(local_git(self.root, "rev-list", "--all", "--count"), commits)
        self.assertEqual(self.prs, [])
        self.assertEqual(self.github_events, [])

    def test_first_changed_candidate_is_committed_pushed_and_drafted(self):
        self.generation = 1
        self.invoke()
        self.assertEqual(len(self.prs), 1)
        pr = self.prs[0]
        self.assertTrue(pr["draft"])
        self.assertEqual(pr["base"], "main")
        self.assertEqual(self.remote_generation(pr["headRefName"]), 1)
        changed = local_git(self.remote, "diff", "--name-only", "main", pr["headRefName"]).splitlines()
        self.assertEqual(set(changed), set(propose_update.FILES))
        self.assertEqual(local_git(self.remote, "show", f"{pr['headRefName']}:skills/keep.md"), "Curated wording stays owned.")
        self.assertEqual(local_git(self.remote, "show", f"{pr['headRefName']}:decisions.json"), '{"reviewed": true}')

    def test_next_candidate_reuses_open_proposal_and_merges_new_main(self):
        self.generation = 1
        self.invoke()
        first = self.prs[0].copy()
        updater = self.base / "main-writer"
        local_git(self.base, "clone", str(self.remote), str(updater))
        (updater / "main-note.txt").write_text("New main work survives.\n", encoding="utf-8")
        local_git(updater, "add", "main-note.txt")
        local_git(updater, "-c", "user.name=Test", "-c", "user.email=test@example.invalid",
                  "-c", "commit.gpgsign=false", "commit", "-m", "advance main")
        local_git(updater, "push", "origin", "main")
        self.generation = 2
        self.invoke()
        self.assertEqual(len(self.prs), 1)
        current = self.prs[0]
        self.assertEqual(current["headRefName"], first["headRefName"])
        self.assertEqual(current["url"], first["url"])
        self.assertEqual(self.github_events, [("create", first["url"]), ("edit", first["url"])])
        self.assertEqual(self.remote_generation(current["headRefName"]), 2)
        self.assertNotEqual(current["published_head"], first["published_head"])
        local_git(self.remote, "merge-base", "--is-ancestor", first["published_head"], current["published_head"])
        self.assertEqual(local_git(self.remote, "show", f"{current['headRefName']}:main-note.txt"), "New main work survives.")
        self.assertTrue(local_git(self.remote, "rev-list", "--merges", f"{first['published_head']}..{current['published_head']}"))

    def test_closed_proposal_starts_fresh_branch_without_changing_old_branch(self):
        self.generation = 1
        self.invoke()
        self.prs[0]["state"] = "closed"
        closed = self.prs[0].copy()
        self.generation = 2
        self.invoke()
        self.assertEqual(len(self.prs), 2)
        fresh = self.prs[1]
        self.assertNotEqual(fresh["headRefName"], closed["headRefName"])
        self.assertTrue(fresh["draft"])
        self.assertEqual(local_git(self.remote, "rev-parse", closed["headRefName"]), closed["published_head"])
        self.assertEqual(self.remote_generation(fresh["headRefName"]), 2)
        self.assertEqual(self.remote_generation(closed["headRefName"]), 1)

    def test_publish_preserves_staged_unstaged_and_untracked_primary_work(self):
        unrelated = self.root / "unrelated.txt"
        unrelated.write_text("User staged this.\n", encoding="utf-8")
        local_git(self.root, "add", "unrelated.txt")
        unrelated.write_text("User then made an unstaged edit.\n", encoding="utf-8")
        (self.root / "private-note.txt").write_text("Untracked user content.\n", encoding="utf-8")
        self.generation = 1
        self.invoke()
        self.assertEqual(len(self.prs), 1)
        self.assertEqual(local_git(self.remote, "show", f"{self.prs[0]['headRefName']}:unrelated.txt"), "Committed unrelated work.")
        remote_files = local_git(self.remote, "ls-tree", "-r", "--name-only", self.prs[0]["headRefName"]).splitlines()
        self.assertNotIn("private-note.txt", remote_files)

    def test_preview_leaves_remote_unchanged_and_cleans_worktree(self):
        refs = self.remote_refs()
        self.generation = 1
        self.invoke(publish=False)
        self.assertEqual(self.remote_refs(), refs)
        self.assertEqual(self.github_events, [])

    def test_failed_producer_or_check_cleans_worktree_without_publishing(self):
        refs = self.remote_refs()
        self.generation = 1
        for failure in ("producer", "validation", "tests"):
            with self.subTest(failure=failure):
                self.failure = failure
                error = RuntimeError if failure == "producer" else subprocess.CalledProcessError
                with self.assertRaises(error):
                    self.invoke()
                self.assertEqual(self.remote_refs(), refs)
                self.assertEqual(self.github_events, [])


if __name__ == "__main__":
    unittest.main()
