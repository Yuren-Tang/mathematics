#!/usr/bin/env python3
"""Validate the additive PORT-AC-CONSOLIDATE-01 registry batch.

This validator checks registry identity, source-map completeness, relation typing,
view reconstruction, and the epistemic invariant unclassified == 0. It performs
no network access and mutates no files.
"""

from __future__ import annotations

import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
UNIT_ID = re.compile(r"^math\.[a-z0-9]+(?:[.-][a-z0-9]+)*$")
SHA = re.compile(r"^[0-9a-f]{40}$")
ANCHOR = re.compile(r"^L([1-9][0-9]*)-L([1-9][0-9]*)$")
LOGICAL = {"depends-on", "uses", "implies", "equivalent-to", "generalizes", "specializes", "refutes", "qualifies", "supersedes"}
DISCOVERY = {"motivates", "suggests", "analogous-to", "arose-from"}
CUBIC_GOAL = "math.graph-theory.cycle-covers.cubic-five-support-goal"
GENERAL_GOAL = "math.graph-theory.cycle-covers.five-support-goal"
REJECTED_CANDIDATE = "math.graph-theory.cycle-covers.v741-proof-candidate"
LATER_RL_AUTHORIAL = {
    "math.graph-theory.cycle-covers.one-atom-identical-support-endpoint",
    "math.graph-theory.cycle-covers.one-atom-shared-vertex-macro",
    "math.graph-theory.cycle-covers.one-atom-conditional-disjoint-commutation",
    "math.graph-theory.cycle-covers.supplied-comparison-run-seam-coherence",
}


def load(path: str) -> dict:
    with (ROOT / path).open("r", encoding="utf-8") as handle:
        return json.load(handle)


_source_cache: dict[tuple[str, str], tuple[str, int]] = {}


def immutable_source_object(commit: str, path: str) -> tuple[str, int]:
    """Return the exact blob SHA and line count for a frozen source object."""

    key = (commit, path)
    if key not in _source_cache:
        blob_result = subprocess.run(
            ["git", "rev-parse", f"{commit}:{path}"],
            cwd=ROOT,
            check=True,
            text=True,
            capture_output=True,
        )
        content_result = subprocess.run(
            ["git", "show", f"{commit}:{path}"],
            cwd=ROOT,
            check=True,
            text=True,
            capture_output=True,
        )
        _source_cache[key] = (
            blob_result.stdout.strip(),
            len(content_result.stdout.splitlines()),
        )
    return _source_cache[key]


def validate_provenance(provenance: dict, *, expected_commit: str | None = None) -> None:
    """Require an immutable source object and a resolvable exact line locator."""

    assert provenance["repository"] == "Yuren-Tang/mathematics"
    assert SHA.fullmatch(provenance["commit"])
    if expected_commit is not None:
        assert provenance["commit"] == expected_commit
    assert provenance["path"]
    assert SHA.fullmatch(provenance["blob"])
    anchor_match = ANCHOR.fullmatch(provenance["anchor"])
    assert anchor_match
    start, end = map(int, anchor_match.groups())
    assert start <= end
    actual_blob, line_count = immutable_source_object(
        provenance["commit"], provenance["path"]
    )
    assert provenance["blob"] == actual_blob
    assert end <= line_count


def main() -> None:
    manifest = load("sources/manifests/PORT_AC_CONSOLIDATE_01_SOURCE_MANIFEST.json")
    mapping = load("migration/source-to-unit-map/PORT_AC_CONSOLIDATE_01_MAP.json")
    registry = load("registry/units/graph-theory/cycle-covers/PORT_AC_CONSOLIDATE_01_UNITS.json")
    relations = load("registry/relations/PORT_AC_CONSOLIDATE_01_RELATIONS.json")
    ac_view = load("registry/views/programme.affine-cdc.json")
    five_view = load("registry/views/frontier.five-cdc.json")

    assert manifest["summary"]["source_packets"] == 6
    assert manifest["summary"]["pending_packets"] == 0
    assert manifest["summary"]["substantive_items"] == 80
    assert manifest["summary"]["classified_items"] == 80
    assert manifest["summary"]["unclassified_items"] == 0

    sources = manifest["sources"]
    assert len(sources) == 6
    assert len({source["source_id"] for source in sources}) == 6
    for source in sources:
        assert SHA.fullmatch(source["commit"])
        assert source["frozen"] is True
        assert source["itemization_status"] == "complete"
        assert source["substantive_item_count"] > 0
        assert (ROOT / source["classification_file"]).is_file()

    counts = mapping["counts"]
    assert counts["source_packets_total"] == 6
    assert counts["source_packets_classified"] == 6
    assert counts["source_packets_unclassified"] == 0
    assert counts["substantive_items_total"] == 80
    assert counts["substantive_items_classified"] == 80
    assert counts["substantive_items_unclassified"] == 0
    assert counts["canonical_units"] == 34

    units = registry["units"]
    ids = [unit["id"] for unit in units]
    assert registry["count"] == 34 == len(units)
    assert len(ids) == len(set(ids))
    assert all(UNIT_ID.fullmatch(unit_id) for unit_id in ids)
    unit_ids = set(ids)
    assert CUBIC_GOAL in unit_ids
    assert GENERAL_GOAL in unit_ids

    for unit in units:
        for provenance in unit["provenance"]:
            validate_provenance(provenance)
        for evidence in unit["assurance"]:
            validate_provenance(evidence["provenance"])

    batch_total = 0
    for entry in mapping["entries"]:
        assert entry["status"] == "classified"
        batch = load(entry["classification_file"])
        assert batch["source_id"] == entry["source_id"]
        assert batch["counts"]["unclassified"] == 0
        assert batch["counts"]["classified"] == batch["counts"]["substantive_items"]
        assert batch["counts"]["substantive_items"] == entry["item_count"]
        batch_total += entry["item_count"]
        for item in batch["items"]:
            validate_provenance(
                item["source_locator"], expected_commit=entry["source_commit"]
            )
            for unit_id in item["units"]:
                assert unit_id in unit_ids, (entry["source_id"], unit_id)
    assert batch_total == 80

    logical = relations["logical"]
    discovery = relations["discovery"]
    assert relations["counts"] == {"logical": len(logical), "discovery": len(discovery), "total": len(logical) + len(discovery)}
    relation_ids = set()
    for relation in logical + discovery:
        assert relation["id"] not in relation_ids
        relation_ids.add(relation["id"])
        assert relation["source"] in unit_ids
        assert relation["target"] in unit_ids
        if relation["plane"] == "logical":
            assert relation["type"] in LOGICAL
        else:
            assert relation["plane"] == "discovery"
            assert relation["type"] in DISCOVERY
        for provenance in relation["provenance"]:
            validate_provenance(provenance)

    assert not any(
        relation["source"] == REJECTED_CANDIDATE
        and relation["type"] == "implies"
        for relation in logical
    )
    cubic_outer_shell = [
        relation
        for relation in logical
        if relation["source"] == CUBIC_GOAL
        and relation["target"] == GENERAL_GOAL
        and relation["type"] == "implies"
    ]
    assert len(cubic_outer_shell) == 1
    assert not any(
        relation["source"]
        == "math.graph-theory.cycle-covers.general-multigraph-outer-shell"
        and relation["target"] == GENERAL_GOAL
        for relation in logical
    )
    application_scope_relations = {
        relation["id"]: relation
        for relation in logical
        if relation["id"]
        in {
            "rel.ac.co-root-qualifies-exact-two-application",
            "rel.ac.zero-qualifies-exact-two-application",
        }
    }
    assert set(application_scope_relations) == {
        "rel.ac.co-root-qualifies-exact-two-application",
        "rel.ac.zero-qualifies-exact-two-application",
    }
    assert all(
        relation["type"] == "qualifies"
        and "premise" in relation["scope"]
        and "application carrier" in relation["scope"]
        for relation in application_scope_relations.values()
    )

    unit_by_id = {unit["id"]: unit for unit in units}
    for unit_id in LATER_RL_AUTHORIAL:
        unit = unit_by_id[unit_id]
        assert unit["maturity"] == "author-complete"
        assert unit["disposition"] == "supported"
        assert unit["workflow"] == "ready-for-review"
        assert any(
            evidence["kind"] == "authorial-argument"
            and evidence["effect"] == "support"
            for evidence in unit["assurance"]
        )
        assert not any(
            evidence["kind"] == "independent-mathematical-review"
            for evidence in unit["assurance"]
        )
    scheduler = unit_by_id[
        "math.graph-theory.cycle-covers.one-atom-prefix-scheduler"
    ]
    assert scheduler["disposition"] == "refuted-in-scope"
    assert any(
        evidence["effect"] == "refute" for evidence in scheduler["assurance"]
    )

    def walk_unit_ids(value: object) -> None:
        if isinstance(value, str) and value.startswith("math."):
            assert value in unit_ids, value
        elif isinstance(value, list):
            for item in value:
                walk_unit_ids(item)
        elif isinstance(value, dict):
            for item in value.values():
                walk_unit_ids(item)

    walk_unit_ids(ac_view)
    walk_unit_ids(five_view)

    assert five_view["status"] == "OPEN / NO ACCEPTED PROOF"
    assert five_view["cubic_goal_unit"] == CUBIC_GOAL
    assert set(ac_view["sections"]["authorial_pending_independent_review"]) == LATER_RL_AUTHORIAL
    assert not (
        set(ac_view["sections"]["independently_established_in_scope"])
        & LATER_RL_AUTHORIAL
    )
    assert manifest["policy"]["delete_or_move_existing_paths"] is False
    assert manifest["policy"]["wholesale_merge"] is False
    assert manifest["policy"]["main_movement"] is False
    assert manifest["policy"]["new_observation_default"] == "captured/unreviewed"

    print("PORT-AC-CONSOLIDATE-01 validation: PASS")
    print(
        "sources=6 items=80 units=34 logical_relations=%d discovery_relations=%d unclassified=0"
        % (len(logical), len(discovery))
    )
    print(
        "immutable_item_locators=80 provenance_objects=%d rejected_candidate_proof_edges=0"
        % (
            sum(
                len(unit["provenance"]) + len(unit["assurance"])
                for unit in units
            )
            + sum(
                len(relation["provenance"])
                for relation in logical + discovery
            )
        )
    )


if __name__ == "__main__":
    main()
