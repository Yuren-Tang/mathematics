#!/usr/bin/env python3
"""Build the exact artifact-level E306 source-to-unit map.

The mathematical routing below is fixed for this bounded intake. Git is used
only to resolve immutable source objects and whole-file line locators.
"""

from __future__ import annotations

import json
import os
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "sources/manifests/E306_CUR_CANONICAL_INTAKE_SOURCE_MANIFEST.json"
MAP_PATH = ROOT / "migration/source-to-unit-map/E306_CUR_CANONICAL_INTAKE_MAP.json"

ERDOS_GIT_DIR = Path(
    os.environ.get("E306_SOURCE_GIT_DIR", "/private/tmp/e306-curator-source-mirror")
)
MATH_GIT_DIR = Path(
    os.environ.get(
        "E306_MATHEMATICS_GIT_DIR",
        str(ROOT / ".git"),
    )
)

U = {
    "goal": "math.number-theory.reciprocal-representations.squarefree-semiprime-characterization",
    "necessity": "math.number-theory.reciprocal-representations.squarefree-denominator-necessity",
    "avoid": "math.number-theory.reciprocal-representations.avoiding-unit-reduction",
    "supply": "math.analytic-number-theory.prime-distribution.fixed-ratio-prime-supply",
    "family": "math.number-theory.reciprocal-representations.complete-pair-denominator-family",
    "fourier": "math.harmonic-analysis.finite-fourier.bernoulli-subset-selector",
    "rigidity": "math.combinatorics.finite-configurations.reciprocal-label-rigidity",
    "decoder": "math.harmonic-analysis.finite-fourier.anchor-fibre-decoder-observability",
    "five": "math.harmonic-analysis.finite-fourier.five-sector-positivity-budget",
    "dense": "math.number-theory.reciprocal-representations.dense-one-anchor-proof",
    "multi": "math.number-theory.reciprocal-representations.multiblock-proof",
    "sparse_core": "math.combinatorics.finite-configurations.sparse-actual-prime-sensor-core",
    "sparse": "math.number-theory.reciprocal-representations.sparse-sensor-proof",
    "weighted": "math.harmonic-analysis.finite-fourier.weighted-decoded-skeleton",
    "aft": "math.harmonic-analysis.finite-fourier.anchor-fibre-transference",
    "observe": "math.harmonic-analysis.finite-fourier.quantitative-target-observability",
    "mass": "math.combinatorics.finite-configurations.complete-family-mass",
    "aft_e306": "math.number-theory.reciprocal-representations.aft-e306-conditional-application",
    "formal": "math.number-theory.reciprocal-representations.e306-formal-release-axis",
    "trust": "math.analytic-number-theory.prime-distribution.e306-formal-trust-boundary",
    "gff": "math.harmonic-analysis.finite-fourier.small-theta-gff-candidate",
    "barrier": "math.combinatorics.finite-configurations.sampled-core-method-barriers",
    "plaquette": "math.combinatorics.finite-configurations.bipartite-plaquette-counterexample",
    "superseded": "math.number-theory.reciprocal-representations.e306-superseded-route-genealogy",
    "e307": "math.number-theory.arithmetic-derivatives.erdos-307-adjacent-open-programme",
    "frontier": "math.number-theory.reciprocal-representations.e306-future-frontier",
}


def git(git_dir: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", f"--git-dir={git_dir}", *args],
        check=True,
        text=True,
        capture_output=True,
    )
    return result.stdout


def tree_paths(git_dir: Path, commit: str, roots: list[str]) -> list[str]:
    output = git(git_dir, "ls-tree", "-r", "--name-only", commit, "--", *roots)
    return [line for line in output.splitlines() if line]


SPECS = {
    "e306-release-v0.0.3": {
        "git_dir": ERDOS_GIT_DIR,
        "commit": "4582185de1e0e27416e9362e0cc7943c3d2fb4fe",
        "roots": [
            "README.md",
            "CITATION.cff",
            "lean/RequestProject/Erdos306FormalConjectures.lean",
            "lean/RequestProject/Audit.lean",
            "lean/RequestProject/RSPrimeSums.lean",
        ],
    },
    "e306-dense-one-anchor": {
        "git_dir": ERDOS_GIT_DIR,
        "commit": "07ed8dcaff334ba9da4b9c87337455c2eca25002",
        "roots": ["proof-development"],
    },
    "e306-dense-one-anchor-audit": {
        "git_dir": ERDOS_GIT_DIR,
        "commit": "1d63273ede93e1b83abf1ab9073d91b76600c23c",
        "roots": ["review"],
    },
    "e306-multiblock-repaired": {
        "git_dir": ERDOS_GIT_DIR,
        "commit": "95a2ede1d40dae41a17fe26e4fe4b491bd94e947",
        "roots": ["proof-development"],
    },
    "e306-multiblock-audit": {
        "git_dir": ERDOS_GIT_DIR,
        "commit": "3d1451faf66830bbf38e16047b78dd08d7efa803",
        "roots": ["review"],
    },
    "e306-multiblock-repair-verification": {
        "git_dir": ERDOS_GIT_DIR,
        "commit": "5c12240e877fb10730508924d0b90ffa8f3a8973",
        "roots": ["review"],
    },
    "e306-sparse-repaired": {
        "git_dir": ERDOS_GIT_DIR,
        "commit": "3074ca46452a6f3528be588033fe414d5a0c0ef9",
        "roots": ["proof-development"],
    },
    "e306-sparse-audit": {
        "git_dir": ERDOS_GIT_DIR,
        "commit": "e9547c15b5858f5c456a9b3ffb9d30d1a0d15233",
        "roots": ["review"],
    },
    "e306-sparse-repair-verification": {
        "git_dir": ERDOS_GIT_DIR,
        "commit": "52463e45fe3ce9ac2d271cea0e0f5e93e6cd5b83",
        "roots": ["review"],
    },
    "e306-aft-authorial": {
        "git_dir": ERDOS_GIT_DIR,
        "commit": "2f49ab25c36326e9ea39e3fc0ed1d22a22b11693",
        "roots": ["research/anchor-fibre-transference"],
    },
    "e306-rl-classification": {
        "git_dir": ERDOS_GIT_DIR,
        "commit": "9bbcfae8360bce0871522e295f9aca903f64c780",
        "roots": ["research/E306_RL_BOUNDED_CURATION_HANDOFF_2026-07-24.md"],
    },
    "e306-old-curation-archival": {
        "git_dir": MATH_GIT_DIR,
        "commit": "6505b51f12de3fdaaf4976379b0ce8b0a665cfc1",
        "roots": ["projects/erdos-306"],
    },
}


def route(source_id: str, path: str) -> tuple[str, list[str]]:
    if source_id == "e306-release-v0.0.3":
        if path == "CITATION.cff":
            return "projection-only", [U["formal"]]
        if path.endswith("Audit.lean"):
            return "attached-formalization", [U["formal"], U["trust"]]
        if path.endswith("RSPrimeSums.lean"):
            return "attached-formalization", [U["trust"], U["supply"]]
        if path.endswith("Erdos306FormalConjectures.lean"):
            return "attached-formalization", [U["goal"], U["formal"]]
        return "attached-formalization", [U["goal"], U["formal"], U["trust"]]

    if source_id == "e306-dense-one-anchor":
        units = [U["dense"]]
        if "HUMAN-PROOF" in path:
            units += [
                U["goal"],
                U["necessity"],
                U["avoid"],
                U["supply"],
                U["family"],
                U["fourier"],
                U["rigidity"],
                U["decoder"],
                U["five"],
            ]
            return "attached-proof", units
        if "FAILURE-MODE" in path:
            return "attached-negative-boundary", [U["dense"], U["barrier"]]
        if "DEPENDENCY" in path or "ARCHITECTURE" in path:
            units += [U["family"], U["rigidity"], U["decoder"], U["five"]]
        return "attached-provenance", units

    if source_id == "e306-dense-one-anchor-audit":
        return "attached-independent-review", [
            U["dense"],
            U["family"],
            U["rigidity"],
            U["decoder"],
            U["five"],
        ]

    if source_id == "e306-multiblock-repaired":
        units = [U["multi"]]
        if "HUMAN-PROOF" in path:
            units += [
                U["goal"],
                U["necessity"],
                U["avoid"],
                U["supply"],
                U["family"],
                U["fourier"],
                U["rigidity"],
                U["decoder"],
                U["five"],
            ]
            return "attached-proof", units
        if "FORMAL_INFORMAL" in path:
            units += [U["formal"], U["trust"]]
        if "/units/" in path or "DEPENDENCY" in path or "DAG" in path:
            units += [U["family"], U["rigidity"], U["decoder"], U["five"]]
        return "attached-provenance", units

    if source_id in {
        "e306-multiblock-audit",
        "e306-multiblock-repair-verification",
    }:
        return "attached-independent-review", [
            U["multi"],
            U["family"],
            U["rigidity"],
            U["decoder"],
            U["five"],
        ]

    if source_id == "e306-sparse-repaired":
        units = [U["sparse"], U["sparse_core"]]
        if "HUMAN-PROOF" in path:
            units += [
                U["goal"],
                U["necessity"],
                U["avoid"],
                U["family"],
                U["fourier"],
                U["rigidity"],
                U["decoder"],
                U["five"],
            ]
            return "attached-proof", units
        if "FAILURE-MODE" in path:
            return "attached-negative-boundary", [U["sparse"], U["barrier"]]
        return "attached-provenance", units

    if source_id in {"e306-sparse-audit", "e306-sparse-repair-verification"}:
        return "attached-independent-review", [
            U["sparse"],
            U["sparse_core"],
            U["rigidity"],
            U["decoder"],
            U["five"],
        ]

    if source_id == "e306-aft-authorial":
        if path.endswith("WEIGHTED-DECODED-SKELETON-THEOREM.md"):
            return "created-new-unit", [U["weighted"]]
        if path.endswith("ANCHOR-FIBRE-FOURIER-TRANSFERENCE.md"):
            return "created-new-unit", [U["aft"]]
        if path.endswith("TARGET-SENSITIVITY-AS-OBSERVABILITY.md"):
            return "created-new-unit", [U["observe"]]
        if path.endswith("COMPLETE-FAMILY-MASS-AND-HIGHER-UNIFORMITY.md"):
            return "created-new-unit", [U["mass"]]
        if path.endswith("E306-COROLLARY-MAP.md"):
            return "attached-conditional-application", [
                U["aft_e306"],
                U["aft"],
                U["weighted"],
                U["observe"],
            ]
        if path.endswith("PROVIDER-HYPOTHESES-AND-FAILURE-MODES.md"):
            return "attached-negative-boundary", [
                U["aft"],
                U["weighted"],
                U["observe"],
                U["barrier"],
                U["plaquette"],
            ]
        return "projection-only", [
            U["aft"],
            U["weighted"],
            U["observe"],
            U["mass"],
            U["aft_e306"],
        ]

    if source_id == "e306-rl-classification":
        return "attached-source-classification", [
            U["gff"],
            U["barrier"],
            U["plaquette"],
            U["superseded"],
            U["e307"],
            U["frontier"],
            U["dense"],
            U["multi"],
            U["sparse"],
            U["aft_e306"],
        ]

    if source_id == "e306-old-curation-archival":
        units = [U["superseded"]]
        if "MASS_VARIANCE" in path or "FOURIER_POSITIVITY" in path:
            units += [U["multi"], U["family"], U["fourier"], U["five"]]
        if "ANALYTIC_INTERFACE" in path:
            units += [U["trust"], U["supply"]]
        if "OPEN_OBLIGATIONS" in path:
            units += [U["frontier"], U["gff"], U["e307"]]
        if "FINITE_CERTIFICATES" in path:
            units += [U["formal"], U["trust"]]
        return "retained-archival-source", units

    raise AssertionError((source_id, path))


def main() -> None:
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    source_by_id = {source["source_id"]: source for source in manifest["sources"]}
    assert set(source_by_id) == set(SPECS)

    items: list[dict] = []
    source_counts: dict[str, int] = {}
    for source_id, spec in SPECS.items():
        source = source_by_id[source_id]
        assert source["commit"] == spec["commit"]
        paths = tree_paths(spec["git_dir"], spec["commit"], spec["roots"])
        assert paths
        source_counts[source_id] = len(paths)
        for index, path in enumerate(paths, start=1):
            blob = git(spec["git_dir"], "rev-parse", f"{spec['commit']}:{path}").strip()
            content = git(spec["git_dir"], "show", f"{spec['commit']}:{path}")
            line_count = len(content.splitlines())
            assert line_count > 0
            disposition, units = route(source_id, path)
            items.append(
                {
                    "item_id": f"{source_id}:{index:02d}",
                    "source_id": source_id,
                    "source_item": path,
                    "disposition": disposition,
                    "units": list(dict.fromkeys(units)),
                    "source_locator": {
                        "repository": source["repository"],
                        "commit": spec["commit"],
                        "path": path,
                        "blob": blob,
                        "anchor": f"L1-L{line_count}",
                    },
                }
            )

    unit_ids = sorted({unit for item in items for unit in item["units"]})
    mapping = {
        "schema_version": "1.0.0",
        "batch_id": "E306-CUR-CANONICAL-INTAKE",
        "map_type": "artifact-to-natural-unit",
        "unit_registry": "registry/units/number-theory/reciprocal-representations/E306_CUR_CANONICAL_INTAKE_UNITS.json",
        "source_manifest": str(MANIFEST_PATH.relative_to(ROOT)),
        "items": items,
        "counts": {
            "source_packets_total": len(SPECS),
            "source_packets_classified": len(SPECS),
            "source_packets_unclassified": 0,
            "substantive_items_total": len(items),
            "substantive_items_classified": len(items),
            "substantive_items_unclassified": 0,
            "canonical_units_referenced": len(unit_ids),
        },
        "invariants": [
            "Every intake artifact has one immutable commit/path/blob/line locator.",
            "Every intake artifact maps to at least one stable natural mathematical unit.",
            "Formal, authorial and independent-review evidence remain orthogonal.",
            "Negative, failed, frontier, discovery and superseded material remains at source strength.",
            "The old curation packet is archival source only and is not a merge/base input.",
            "E307 remains separate, adjacent and open.",
            "unclassified = 0",
        ],
    }

    for source in manifest["sources"]:
        source["itemization_status"] = "complete"
        source["substantive_item_count"] = source_counts[source["source_id"]]
        source["classification_file"] = str(MAP_PATH.relative_to(ROOT))
    manifest["state"] = "fixed-candidate"
    manifest["summary"] = {
        "source_packets": len(SPECS),
        "itemized_packets": len(SPECS),
        "pending_packets": 0,
        "substantive_items": len(items),
        "classified_items": len(items),
        "unclassified_items": 0,
    }

    MAP_PATH.parent.mkdir(parents=True, exist_ok=True)
    MAP_PATH.write_text(json.dumps(mapping, indent=2) + "\n", encoding="utf-8")
    MANIFEST_PATH.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    print(
        f"E306 source map built: sources={len(SPECS)} "
        f"items={len(items)} units-referenced={len(unit_ids)} unclassified=0"
    )


if __name__ == "__main__":
    main()
