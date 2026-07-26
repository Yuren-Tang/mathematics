#!/usr/bin/env python3
"""Build the final portfolio source-disposition closeout artifacts.

The first checkpoint deliberately persists the exact ten-ref tree/blob
inventory before the semantic map is completed.  Later phases extend this
generator with the natural units, typed relations, and no-loss disposition
map; the inventory itself remains the immutable input.
"""

from __future__ import annotations

import json
import os
import subprocess
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MATH_GIT = Path(
    subprocess.run(
        ["git", "rev-parse", "--git-common-dir"],
        cwd=ROOT,
        text=True,
        check=True,
        stdout=subprocess.PIPE,
    ).stdout.strip()
)
if not MATH_GIT.is_absolute():
    MATH_GIT = (ROOT / MATH_GIT).resolve()

PAPER_GIT = Path(
    os.environ.get(
        "PORT_CLOSEOUT_PAPER_GIT_DIR",
        "/private/tmp/portfolio-source-disposition-ac-paper-mirror",
    )
)
E306_GIT = Path(
    os.environ.get(
        "PORT_CLOSEOUT_E306_GIT_DIR",
        "/private/tmp/e306-curator-source-mirror",
    )
)


@dataclass(frozen=True)
class Source:
    source_id: str
    repository: str
    commit: str
    git_dir: Path
    role: str
    scope_mode: str
    scope_base: str | None = None
    scope_paths: tuple[str, ...] = ()


ORIENTATION = "e6af5645107d0f21ac6c262c63a1db5dab8f0fd1"
ROOT_LIFT = "81da79782da348fac629b42882e447f95e4c9d3a"

SOURCES = [
    Source(
        "ac-orientation",
        "Yuren-Tang/mathematics",
        ORIENTATION,
        MATH_GIT,
        "superseded-source",
        "diff",
        "ec765cd03271abd3588ec36faec3d53d0f8aa03b",
    ),
    Source(
        "ac-root-lift",
        "Yuren-Tang/mathematics",
        ROOT_LIFT,
        MATH_GIT,
        "development",
        "orientation-plus-diff",
        ORIENTATION,
    ),
    Source(
        "ac-adaptive-ordering",
        "Yuren-Tang/mathematics",
        "04f9a37052406f760a31b725945cfa52dce6c2d8",
        MATH_GIT,
        "development",
        "explicit",
        scope_paths=(
            "projects/affine-cdc/research/ADAPTIVE_CYCLIC_ORDERING_V1.md",
        ),
    ),
    Source(
        "ac-binary-eight",
        "Yuren-Tang/mathematics",
        "8b17ebb4077b5bb00a96ddb83a5f46c799489fdb",
        MATH_GIT,
        "development",
        "explicit",
        scope_paths=(
            "projects/affine-cdc/research/BINARY_EIGHT_FLOW_AUDIT_V1.md",
            "projects/affine-cdc/research/M2_WORKSTREAM_REPORT.md",
        ),
    ),
    Source(
        "ac-outer-shell",
        "Yuren-Tang/mathematics",
        "3f79773e6ddb7d3a816a1a47120fa0696a7d0b52",
        MATH_GIT,
        "development",
        "explicit",
        scope_paths=(
            "projects/affine-cdc/research/M1_WORKSTREAM_REPORT.md",
            "projects/affine-cdc/research/OUTER_SHELL_RESEARCH_V1.md",
        ),
    ),
    Source(
        "ac-outer-promotion",
        "Yuren-Tang/mathematics",
        "eb6f184d38caa4b16b157f7c1b236bd374a68455",
        MATH_GIT,
        "development",
        "explicit",
        scope_paths=(
            "projects/affine-cdc/reduction/outer-shell-and-binary-flow.md",
            "projects/affine-cdc/research/MP1_OUTER_SHELL_PROMOTION_REPORT.md",
        ),
    ),
    Source(
        "ac-paper-revision",
        "Yuren-Tang/affine-cdc-workbench",
        "278fb45ef65601e6b5b9917d20219b3a60bc2ee7",
        PAPER_GIT,
        "manuscript",
        "diff",
        "f8f072e86d28960150fa166cc9e23e5775ce30fe",
    ),
    Source(
        "e306-clear-up",
        "Yuren-Tang/erdos-306",
        "63801a68fb6b9f4e0f0509687960d159a278503e",
        E306_GIT,
        "formalization",
        "all",
    ),
    Source(
        "e306-pushlinter",
        "Yuren-Tang/erdos-306",
        "e55ef359a8b98525f0bac6c7a510fcad94469bff",
        E306_GIT,
        "formalization",
        "all",
    ),
    Source(
        "e306-complete-pair-prepared",
        "Yuren-Tang/erdos-306",
        "4348421af6830b99a233c021c1761d485481ddf6",
        E306_GIT,
        "development",
        "all",
    ),
]


def git(git_dir: Path, *args: str, input_text: str | None = None) -> str:
    return subprocess.run(
        ["git", f"--git-dir={git_dir}", *args],
        text=True,
        input=input_text,
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    ).stdout


def tree_items(source: Source) -> list[dict]:
    output = git(
        source.git_dir,
        "ls-tree",
        "-r",
        "--format=%(objectmode)%x09%(objecttype)%x09%(objectname)%x09%(path)",
        source.commit,
    )
    items = []
    for line in output.splitlines():
        mode, object_type, blob, path = line.split("\t", 3)
        if object_type != "blob":
            raise ValueError(f"non-blob recursive tree entry: {source.source_id} {path}")
        items.append(
            {
                "repository": source.repository,
                "commit": source.commit,
                "path": path,
                "blob": blob,
                "anchor": f"blob:{blob}",
                "object_mode": mode,
            }
        )
    return items


def diff_paths(source: Source, base: str) -> list[str]:
    return [
        line
        for line in git(
            source.git_dir,
            "diff",
            "--name-only",
            "--diff-filter=ACMRT",
            base,
            source.commit,
        ).splitlines()
        if line
    ]


def source_scope(source: Source, all_paths: list[str], orientation_paths: list[str]) -> list[str]:
    if source.scope_mode == "all":
        return all_paths
    if source.scope_mode == "explicit":
        return list(source.scope_paths)
    if source.scope_mode == "diff":
        assert source.scope_base is not None
        return diff_paths(source, source.scope_base)
    if source.scope_mode == "orientation-plus-diff":
        assert source.scope_base is not None
        return sorted(set(orientation_paths + diff_paths(source, source.scope_base)))
    raise ValueError(f"unknown scope mode {source.scope_mode}")


def write_json(path: str, value: object) -> None:
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(value, indent=2, sort_keys=False) + "\n")


def write(path: str, value: str) -> None:
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(value.rstrip() + "\n")


def build_manifest() -> dict:
    documents = []
    orientation_paths: list[str] = []
    for source in SOURCES:
        if not source.git_dir.exists():
            raise FileNotFoundError(f"missing read-only git store: {source.git_dir}")
        resolved = git(source.git_dir, "rev-parse", f"{source.commit}^{{commit}}").strip()
        if resolved != source.commit:
            raise ValueError(f"commit did not resolve exactly: {source.source_id}")
        tree = git(source.git_dir, "rev-parse", f"{source.commit}^{{tree}}").strip()
        items = tree_items(source)
        paths = [item["path"] for item in items]
        scope = source_scope(source, paths, orientation_paths)
        if source.source_id == "ac-orientation":
            orientation_paths = scope
        missing = sorted(set(scope) - set(paths))
        if missing:
            raise ValueError(f"scope path missing from tree {source.source_id}: {missing}")
        documents.append(
            {
                "source_id": source.source_id,
                "repository": source.repository,
                "commit": source.commit,
                "tree": tree,
                "role": source.role,
                "frozen": True,
                "retention": "retained-not-delete-safe",
                "full_tree_item_count": len(items),
                "source_scope_item_count": len(scope),
                "source_scope_paths": scope,
                "full_tree_items": items,
            }
        )
    return {
        "schema_version": "1.0.0",
        "batch_id": "PORT-SOURCE-DISPOSITION-CLOSEOUT",
        "state": "inventory-checkpoint",
        "authority": "Yuren-Tang/research-workbench#15@5081149903",
        "canonical_base": "ce577e23ea9b2493cd912af8c1335b67e8ddebec",
        "sources": documents,
        "summary": {
            "source_refs": len(documents),
            "full_tree_items": sum(d["full_tree_item_count"] for d in documents),
            "source_scope_items": sum(d["source_scope_item_count"] for d in documents),
            "unresolved_refs": 0,
            "delete_safe_refs": 0,
        },
        "invariants": [
            "Every exact ref resolves to its recorded commit and tree.",
            "Every full recursive tree entry records commit, path, blob and whole-blob anchor.",
            "Source scope distinguishes authored intake content from inherited repository files.",
            "All ten refs are retained; none is deletion-safe.",
            "This inventory checkpoint makes no theorem, assurance, publication or main-movement disposition.",
        ],
    }


def main() -> None:
    manifest = build_manifest()
    write_json(
        "sources/manifests/PORT_SOURCE_DISPOSITION_CLOSEOUT_SOURCE_MANIFEST.json",
        manifest,
    )
    counts = manifest["summary"]
    write(
        "migration/no-loss-audits/PORT_SOURCE_DISPOSITION_CLOSEOUT_STATE.md",
        f"""# Portfolio source-disposition closeout

**State:** inventory checkpoint; semantic disposition in progress

**Authority:** `Yuren-Tang/research-workbench#15@5081149903`

**Canonical base:** `mathematics:main@ce577e23ea9b2493cd912af8c1335b67e8ddebec`

The final migration batch covers ten retained exact refs.  The machine
manifest fixes all ten commit/tree identities, {counts['full_tree_items']}
recursive tree/blob items, and {counts['source_scope_items']} authored source
scope items.  Exact source-to-unit/disposition mapping, reverse provenance,
negative completeness, and epistemic no-upgrade checks are the remaining work
of this same branch.

No ref is deletion-safe.  This checkpoint does not move `main`, accept a
theorem, start research or formalization, copy manuscript TeX, or authorize
release, submission, DOI, or publication action.
""",
    )


if __name__ == "__main__":
    main()
