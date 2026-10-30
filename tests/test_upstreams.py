import copy
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from upstreams import build_catalog, diff_files, inventory_source


class ChangeTrackingTests(unittest.TestCase):
    def test_changes_include_runtime_and_license_files(self):
        old = {"SKILL.md": "a", "scripts/run.py": "b", "LICENSE": "c", "old.md": "d"}
        new = {"SKILL.md": "a", "scripts/run.py": "new", "LICENSE": "new", "references/new.md": "e"}
        self.assertEqual(diff_files(old, new), {
            "added": ["references/new.md"], "removed": ["old.md"],
            "changed": ["LICENSE", "scripts/run.py"],
        })

    def test_changed_instructions_invalidate_review_without_mutating_it(self):
        row = {"source": "x", "path": "skills/foo/SKILL.md", "id": "x:foo", "name": "foo", "blob": "new"}
        review = {"source": "x", "path": row["path"], "reviewed_blob": "old", "disposition": "adapt", "evidence_level": "source-review"}
        saved = copy.deepcopy(review)
        result = build_catalog([row], [review])[0]
        self.assertEqual(result["disposition"], "defer")
        self.assertEqual(result["evidence_level"], "changed-since-source-review")
        self.assertEqual(review, saved)

    def test_same_version_preserves_review(self):
        row = {"source": "x", "path": "skills/foo/SKILL.md", "id": "x:foo", "name": "foo", "blob": "same"}
        review = {"source": "x", "path": row["path"], "reviewed_blob": "same", "disposition": "adapt", "evidence_level": "source-review"}
        self.assertEqual(build_catalog([row], [review])[0]["disposition"], "adapt")

    def test_new_candidate_is_not_auto_promoted(self):
        row = {"source": "x", "path": "skills/new/SKILL.md", "id": "x:new", "name": "new", "blob": "a"}
        result = build_catalog([row], [])[0]
        self.assertEqual(result["disposition"], "defer")
        self.assertEqual(result["evidence_level"], "metadata-inventory")

    def test_changed_helper_invalidates_a_review_even_with_same_skill_blob(self):
        row = {"source": "x", "path": "skills/foo/SKILL.md", "id": "x:foo", "name": "foo", "blob": "same", "source_tree_sha256": "new-helper"}
        review = {"source": "x", "path": row["path"], "reviewed_blob": "same", "reviewed_source_sha256": "old-helper", "disposition": "adapt", "evidence_level": "source-review"}
        self.assertEqual(build_catalog([row], [review])[0]["disposition"], "defer")

    def test_copied_old_catalog_row_cannot_overwrite_current_provenance(self):
        current = {"source": "x", "path": "skills/foo/SKILL.md", "id": "x:foo", "name": "foo", "blob": "same", "commit": "new", "source_tree_sha256": "new-helper"}
        review = {**current, "source_tree_sha256": "old-helper", "commit": "old", "reviewed_blob": "same", "reviewed_source_sha256": "old-helper", "disposition": "adapt", "evidence_level": "source-review"}
        result = build_catalog([current], [review])[0]
        self.assertEqual(result["source_tree_sha256"], "new-helper")
        self.assertEqual(result["commit"], "new")
        self.assertEqual(result["disposition"], "defer")

    def test_inventory_ignores_mirrors_but_tracks_helper_deletions(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            def git(*args):
                subprocess.run(["git", "-C", tmp, *args], check=True, capture_output=True)
            git("init")
            for folder in ("skills/foo", "generated/foo"):
                (root / folder).mkdir(parents=True)
                (root / folder / "SKILL.md").write_text("---\nname: foo\ndescription: Test fixture\n---\n", encoding="utf-8")
            (root / "skills/foo/helper.py").write_text("pass\n")
            (root / "references").mkdir()
            (root / "references/rules.md").write_text("Keep the agreed behavior.\n")
            (root / "LICENSE").write_text("Test license\n")
            git("add", ".")
            git("-c", "user.name=Test", "-c", "user.email=test@example.invalid", "commit", "-m", "fixture")
            source = {"id": "test", "repository": "test/test", "scope": "", "skill_roots": ["skills/"]}
            before, rows = inventory_source(source, root)
            self.assertEqual(len(rows), 1)
            self.assertIn("skills/foo/helper.py", before["files"])
            self.assertIn("references/rules.md", before["files"])
            self.assertIn("LICENSE", before["files"])
            (root / "skills/foo/helper.py").unlink()
            (root / "references/rules.md").write_text("Contradict the agreed behavior.\n")
            git("add", ".")
            git("-c", "user.name=Test", "-c", "user.email=test@example.invalid", "commit", "-m", "remove helper")
            after, _ = inventory_source(source, root)
            self.assertEqual(diff_files(before["files"], after["files"])["removed"], ["skills/foo/helper.py"])
            self.assertEqual(diff_files(before["files"], after["files"])["changed"], ["references/rules.md"])
            self.assertNotEqual(before["tree_sha256"], after["tree_sha256"])


if __name__ == "__main__":
    unittest.main()
