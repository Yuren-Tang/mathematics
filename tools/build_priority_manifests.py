#!/usr/bin/env python3
"""Create canonical priority manifests for content-changing commits."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path
from typing import Any

CONTENT_ROOTS = ("projects", "unfiled")


def git(*args: str, text: bool = True, check: bool = True) -> str | bytes:
    result = subprocess.run(
        ["git", *args],
        check=check,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=text,
    )
    return result.stdout


def exists(spec: str) -> bool:
    return subprocess.run(
        ["git", "cat-file", "-e", spec],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    ).returncode == 0


def blob(commit: str | None, path: str) -> dict[str, Any] | None:
    if not commit:
        return None
    spec = f"{commit}:{path}"
    if not exists(spec):
        return None
    content = bytes(git("show", spec, text=False))
    return {
        "path": path,
        "git_blob": str(git("rev-parse", spec)).strip(),
        "sha256": hashlib.sha256(content).hexdigest(),
        "size_bytes": len(content),
    }


def first_parent(commit: str) -> str | None:
    raw = str(git("show", "-s", "--format=%P", commit)).strip()
    return raw.split()[0] if raw else None


def changes(commit: str, parent: str | None) -> list[dict[str, Any]]:
    if parent:
        raw = str(git(
            "diff", "--name-status", "-M", parent, commit, "--", *CONTENT_ROOTS
        ))
    else:
        raw = str(git(
            "diff-tree", "--root", "--no-commit-id", "--name-status",
            "-r", "-M", commit, "--", *CONTENT_ROOTS
        ))

    records: list[dict[str, Any]] = []
    for line in raw.splitlines():
        if not line.strip():
            continue
        parts = line.split("\t")
        status = parts[0]
        kind = status[0]

        if kind == "R":
            old_path, new_path = parts[1], parts[2]
            records.append({
                "status": "renamed",
                "similarity": int(status[1:]) if status[1:] else None,
                "before": blob(parent, old_path),
                "after": blob(commit, new_path),
            })
        elif kind == "D":
            records.append({
                "status": "deleted",
                "before": blob(parent, parts[1]),
                "after": None,
            })
        else:
            labels = {
                "A": "added",
                "M": "modified",
                "C": "copied",
                "T": "type-changed",
            }
            records.append({
                "status": labels.get(kind, status),
                "before": blob(parent, parts[1]),
                "after": blob(commit, parts[-1]),
            })
    return records


def commits_in_push(before: str, after: str) -> list[str]:
    zero = "0" * 40
    after = str(git("rev-parse", f"{after}^{{commit}}" )).strip()
    if before and before != zero and exists(f"{before}^{{commit}}"):
        raw = str(git("rev-list", "--reverse", f"{before}..{after}")).strip()
        return raw.splitlines() if raw else []
    return [after]


def build(repository: str, commit: str) -> dict[str, Any] | None:
    parent = first_parent(commit)
    changed = changes(commit, parent)
    if not changed:
        return None

    commit_object = bytes(git("cat-file", "commit", commit, text=False))
    return {
        "schema": "working-mathematics-priority-manifest/v1",
        "repository": repository,
        "commit": commit,
        "tree": str(git("rev-parse", f"{commit}^{{tree}}" )).strip(),
        "parents": str(git("show", "-s", "--format=%P", commit)).strip().split(),
        "commit_object_sha256": hashlib.sha256(commit_object).hexdigest(),
        "content_roots": list(CONTENT_ROOTS),
        "changes": changed,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--before", required=True)
    parser.add_argument("--after", required=True)
    parser.add_argument("--repository", required=True)
    parser.add_argument("--output-dir", required=True)
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    written = 0

    for commit in commits_in_push(args.before, args.after):
        manifest = build(args.repository, commit)
        if manifest is None:
            continue
        path = output_dir / f"{commit}.json"
        path.write_text(
            json.dumps(manifest, ensure_ascii=False, sort_keys=True, indent=2)
            + "\n",
            encoding="utf-8",
        )
        written += 1

    if written == 0:
        raise SystemExit("No content-changing commits found.")


if __name__ == "__main__":
    main()
