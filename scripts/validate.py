"""Validate pack structure and provenance, without claiming behavioral quality."""

from pathlib import Path
import re

from upstreams import ROOT, frontmatter, read_json


def validate(root=ROOT):
    errors = []
    names = set()
    for path in sorted((root / "skills").glob("*/SKILL.md")):
        try:
            meta = frontmatter(path.read_text(encoding="utf-8"))
            name = meta["name"]
            if name != path.parent.name or not re.fullmatch(r"kp-[a-z0-9-]{1,60}", name):
                errors.append(f"Invalid/mismatched skill name: {path}")
            if name in names:
                errors.append(f"Duplicate skill name: {name}")
            names.add(name)
            if not isinstance(meta.get("description"), str) or not meta["description"].strip():
                errors.append(f"Missing description: {path}")
            for link in re.findall(r"\]\(([^)]+)\)", path.read_text(encoding="utf-8")):
                if not re.match(r"[a-z]+://|#", link) and not (path.parent / link.split("#")[0]).exists():
                    errors.append(f"Broken skill reference: {path}: {link}")
        except (KeyError, ValueError, TypeError) as exc:
            errors.append(f"Invalid frontmatter: {path}: {exc}")
    if not names:
        errors.append("No discoverable skills")
    sources = read_json(root / "sources.json")["sources"]
    source_ids = [s["id"] for s in sources]
    if len(set(source_ids)) != len(source_ids):
        errors.append("Duplicate source IDs")
    lock = read_json(root / "upstream.lock.json")
    catalog = read_json(root / "catalog.json")
    seen = set()
    for row in catalog:
        if row["id"] in seen:
            errors.append(f"Duplicate catalog identity: {row['id']}")
        seen.add(row["id"])
        snapshot = lock["sources"].get(row["source"])
        if not snapshot or row["path"] not in snapshot["files"]:
            errors.append(f"Missing snapshot: {row['id']}")
            continue
        if row["blob"] != snapshot["files"][row["path"]]["sha"] or row["commit"] != snapshot["commit"]:
            errors.append(f"Catalog/snapshot drift: {row['id']}")
        if row["source_tree_sha256"] != snapshot["tree_sha256"]:
            errors.append(f"Source tree/catalog drift: {row['id']}")
        if row["evidence_level"] == "source-review" and (row.get("reviewed_blob") != row["blob"] or row.get("reviewed_source_sha256") != row["source_tree_sha256"]):
            errors.append(f"Stale review presented as current: {row['id']}")
        for field in ("one_liner", "practitioner", "skeptic", "evaluator", "consensus"):
            if not row.get(field):
                errors.append(f"Missing {field}: {row['id']}")
    if set(source_ids) != set(lock["sources"]):
        errors.append("Source registry/snapshot mismatch")
    return errors, len(names), len(catalog)


if __name__ == "__main__":
    errors, skills, candidates = validate()
    for error in errors:
        print(error)
    print(f"{skills} active skills; {candidates} upstream entries; {len(errors)} structural errors.")
    raise SystemExit(bool(errors))
