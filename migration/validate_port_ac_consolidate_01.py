#!/usr/bin/env python3
"""Validate the additive PORT-AC-CONSOLIDATE-01 registry batch.

This validator checks registry identity, source-map completeness, relation typing,
view reconstruction, and the epistemic invariant unclassified == 0. It performs
no network access and mutates no files.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
UNIT_ID = re.compile(r"^math\.[a-z0-9]+(?:[.-][a-z0-9]+)*$")
SHA = re.compile(r"^[0-9a-f]{40}$")
LOGICAL = {"depends-on", "uses", "implies", "equivalent-to", "generalizes", "specializes", "refutes", "qualifies", "supersedes"}
DISCOVERY = {"motivates", "suggests", "analogous-to", "arose-from"}


def load(path: str) -> dict:
    with (ROOT / path).open("r", encoding="utf-8") as handle:
        return json.load(handle)


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
    assert counts["canonical_units"] == 33

    units = registry["units"]
    ids = [unit["id"] for unit in units]
    assert registry["count"] == 33 == len(units)
    assert len(ids) == len(set(ids))
    assert all(UNIT_ID.fullmatch(unit_id) for unit_id in ids)
    unit_ids = set(ids)

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
    assert manifest["policy"]["delete_or_move_existing_paths"] is False
    assert manifest["policy"]["wholesale_merge"] is False
    assert manifest["policy"]["main_movement"] is False
    assert manifest["policy"]["new_observation_default"] == "captured/unreviewed"

    print("PORT-AC-CONSOLIDATE-01 validation: PASS")
    print("sources=6 items=80 units=33 logical_relations=%d discovery_relations=%d unclassified=0" % (len(logical), len(discovery)))


if __name__ == "__main__":
    main()
