"""Inventory pinned upstream sources as data; never install or execute them."""

from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import subprocess

import yaml

ROOT = Path(__file__).resolve().parents[1]


def git(path, *args):
    return subprocess.check_output(
        ["git", "-C", str(path), *args], text=True, encoding="utf-8"
    ).strip()


def read_json(path, default=None):
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else default


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def frontmatter(text):
    match = re.match(r"\A---\s*\n(.*?)\n---(?:\s*\n|$)", text, re.S)
    if not match:
        raise ValueError("Missing frontmatter")
    result = yaml.safe_load(match[1])
    if not isinstance(result, dict):
        raise ValueError("Frontmatter must be a mapping")
    return result


def inventory_source(source, path):
    commit = git(path, "rev-parse", "HEAD")
    # ls-tree includes scripts, assets, references and license changes even when
    # sparse checkout materializes only Markdown and licensing files.
    files = {}
    skills = []
    for line in git(path, "ls-tree", "-r", "HEAD").splitlines():
        info, name = line.split("\t", 1)
        mode, kind, blob = info.split()
        root_provenance = "/" not in name and (name.upper().startswith(("LICENSE", "NOTICE", "COPYING")) or name == "README.md")
        support_file = any(name.startswith(p) for p in source.get("support_roots", []))
        if not name.startswith(source["scope"]) and not root_provenance and not support_file:
            continue
        files[name] = {"sha": blob, "mode": mode, "kind": kind}
        if name.endswith("/SKILL.md") and any(name.startswith(p) for p in source["skill_roots"]):
            if mode != "100644" and mode != "100755":
                raise ValueError(f"Skill entrypoint must be a regular file: {name}")
            raw = git(path, "show", f"HEAD:{name}").lstrip("\ufeff")
            try:
                meta = frontmatter(raw)
                declared_name = str(meta.get("name") or Path(name).parent.name)
                error = None
            except (ValueError, yaml.YAMLError) as exc:
                declared_name = Path(name).parent.name
                error = str(exc).splitlines()[0]
            skills.append({
                "id": f"{source['id']}:{name}", "source": source["id"],
                "path": name, "name": declared_name, "blob": blob,
                "body_sha256": hashlib.sha256(raw.encode()).hexdigest(),
                "commit": commit,
                "url": f"https://github.com/{source['repository']}/blob/{commit}/{name}",
                "frontmatter_error": error,
            })
    tree_hash = hashlib.sha256(json.dumps(files, sort_keys=True).encode()).hexdigest()
    for row in skills:
        row["source_tree_sha256"] = tree_hash
    return {"commit": commit, "tree_sha256": tree_hash, "files": files}, skills


def prepare(source, refresh):
    path = ROOT / ".cache" / "upstreams" / source["id"]
    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run([
            "git", "clone", "--depth", "1", "--filter=blob:none", "--sparse",
            "--branch", source["branch"],
            f"https://github.com/{source['repository']}.git", str(path),
        ], check=True, capture_output=True)
    expected = f"https://github.com/{source['repository']}.git"
    if git(path, "remote", "get-url", "origin") != expected:
        raise ValueError(f"Unexpected cache origin: {source['id']}")
    if git(path, "status", "--porcelain"):
        raise ValueError(f"Refusing to change dirty cache: {source['id']}")
    if refresh:
        git(path, "fetch", "--depth", "1", "origin", source["branch"])
        git(path, "checkout", "--detach", "FETCH_HEAD")
    git(path, "sparse-checkout", "set", "--no-cone", "**/SKILL.md", "**/LICENSE*", "**/README.md", "**/AGENTS.md", "**/references/**", "**/agents/*.yaml", "**/plugin.json")
    return path


def diff_files(before, after):
    return {
        "added": sorted(after.keys() - before.keys()),
        "removed": sorted(before.keys() - after.keys()),
        "changed": sorted(p for p in before.keys() & after.keys() if before[p] != after[p]),
    }


def inferred_summary(row):
    """A conservative name-based label for candidates not substantively reviewed."""
    parts = row["path"].split("/")
    group = parts[1] if row["source"] == "openai-plugins" else row["source"]
    subject = row["name"].replace("-", " ").replace("_", " ")
    return f"Handle {subject} work within {group}; assess against a concrete task before use."


def build_catalog(skills, reviews):
    decisions = {(r["source"], r["path"]): r for r in reviews}
    assessment_fields = {
        "one_liner", "disposition", "canonical_target", "practitioner", "skeptic", "evaluator",
        "consensus", "overlaps", "dependencies", "evidence_level", "reviewed_blob", "reviewed_source_sha256",
        "inspection_depth", "lifecycle", "license", "license_source",
    }
    catalog = []
    for row in sorted(skills, key=lambda r: r["id"]):
        decision = decisions.get((row["source"], row["path"]))
        if decision:
            row.update({k: v for k, v in decision.items() if k in assessment_fields})
            row["reviewed_blob"] = decision.get("reviewed_blob")
            if row["reviewed_blob"] != row["blob"] or decision.get("reviewed_source_sha256") != row.get("source_tree_sha256"):
                row["previous_disposition"] = row.get("disposition")
                row["disposition"] = "defer"
                row["evidence_level"] = "changed-since-source-review"
                row["consensus"] = "Upstream source files changed; inspect the delta and affected dependencies before promotion."
        else:
            row.update({
                "one_liner": inferred_summary(row),
                "disposition": "reference" if row["source"] == "openai-skills" else "defer",
                "canonical_target": None,
                "evidence_level": "metadata-inventory",
                "practitioner": "May supply specialized procedures when this named capability is needed.",
                "skeptic": "No substantive source assessment or demonstrated local benefit for this candidate.",
                "evaluator": "Inspect instructions, dependencies and terms; compare a representative task with a no-skill baseline.",
                "consensus": "Keep discoverable in the catalog; do not add to the active pack without a relevant use case and review.",
                "overlaps": [], "dependencies": ["Inspect upstream package and host requirements"],
            })
        catalog.append(row)
    return catalog


def render(catalog, lock):
    lines = ["# Upstream skill catalog", "", "Generated from pinned source trees. This is an inventory, not an installation list.", "",
             "`source-review` means a written assessment, not a behavioral benchmark; see inspection depth and the source reports. `description-review` summarizes name/description only and gives a provisional decision; bodies and dependencies were not substantively audited. `metadata-inventory` means a new, unassessed entry with a name-derived label. Changed tracked source files invalidate previous decisions. Simulated role comments are hypotheses, not independent empirical results.", ""]
    counts = Counter(r["source"] for r in catalog)
    lines += ["| Source | Skills | Pinned commit |", "| --- | ---: | --- |"]
    for source, count in sorted(counts.items()):
        lines.append(f"| {source} | {count} | `{lock['sources'][source]['commit']}` |")
    for source in counts:
        lines += ["", f"## {source}", "", "| Skill | One-line use | Decision | Coverage |", "| --- | --- | --- | --- |"]
        for row in (r for r in catalog if r["source"] == source):
            summary = row["one_liner"].replace("|", "\\|").replace("\n", " ")
            lines.append(f"| [{row['name']}]({row['url']}) | {summary} | {row['disposition']} | {row['evidence_level']} |")
    (ROOT / "docs" / "catalog.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--refresh", action="store_true", help="Fetch current configured branches into disposable caches")
    parser.add_argument("--write", action="store_true", help="Write observed snapshots and catalog; never edits skills/")
    args = parser.parse_args()
    sources = read_json(ROOT / "sources.json")["sources"]
    previous = read_json(ROOT / "upstream.lock.json", {"sources": {}})
    lock = {"schema_version": 1, "sources": {}}
    all_skills, changes = [], []
    for source in sources:
        snapshot, skills = inventory_source(source, prepare(source, args.refresh))
        lock["sources"][source["id"]] = snapshot
        all_skills.extend(skills)
        old = previous["sources"].get(source["id"], {})
        diff = diff_files(old.get("files", {}), snapshot["files"])
        if any(diff.values()):
            changes.append({"source": source["id"], "before": old.get("commit"), "after": snapshot["commit"], **diff})
        print(f"{source['id']}: {len(skills)} skills at {snapshot['commit'][:12]}")
    if args.write:
        (ROOT / "docs").mkdir(exist_ok=True)
        write_json(ROOT / "upstream.lock.json", lock)
        catalog = build_catalog(all_skills, read_json(ROOT / "reviews.json", []))
        write_json(ROOT / "catalog.json", catalog)
        render(catalog, lock)
        # Preserve the last actual delta on no-op runs so reruns are idempotent.
        if changes:
            write_json(ROOT / "docs" / "upstream-changes.json", changes)
    print(f"Total: {len(all_skills)} skills; {len(changes)} sources have file changes.")


if __name__ == "__main__":
    main()
