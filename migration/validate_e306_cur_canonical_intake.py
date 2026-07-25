#!/usr/bin/env python3
"""Independent, bounded validator for E306-CUR-CANONICAL-INTAKE."""

from __future__ import annotations

import json
import os
import re
import subprocess
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = "19a5e294e00583c930203c1eec68896ccd9d8ed2"
SOURCE_GIT = Path(os.environ.get("E306_SOURCE_GIT_DIR", "/private/tmp/e306-curator-source-mirror"))


def load(path: str):
    return json.loads((ROOT / path).read_text())


def run(*args: str) -> str:
    return subprocess.run(args, cwd=ROOT, text=True, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE, check=True).stdout.strip()


def check(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def batch_blobs(git_dir: Path, object_ids: list[str]) -> dict[str, bytes]:
    proc = subprocess.Popen(
        ["git", f"--git-dir={git_dir}", "cat-file", "--batch"],
        stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    )
    assert proc.stdin is not None and proc.stdout is not None
    for oid in object_ids:
        proc.stdin.write((oid + "\n").encode())
    proc.stdin.close()
    result: dict[str, bytes] = {}
    for expected in object_ids:
        header = proc.stdout.readline().decode().rstrip("\n")
        fields = header.split()
        check(len(fields) == 3 and fields[0] == expected and fields[1] == "blob",
              f"bad cat-file header for {expected}: {header}")
        size = int(fields[2])
        payload = proc.stdout.read(size)
        check(proc.stdout.read(1) == b"\n", f"missing batch delimiter for {expected}")
        result[expected] = payload
    stderr = proc.stderr.read().decode() if proc.stderr else ""
    check(proc.wait() == 0, f"git cat-file failed: {stderr}")
    return result


manifest = load("sources/manifests/E306_CUR_CANONICAL_INTAKE_SOURCE_MANIFEST.json")
source_map = load("migration/source-to-unit-map/E306_CUR_CANONICAL_INTAKE_MAP.json")
unit_doc = load("registry/units/number-theory/reciprocal-representations/E306_CUR_CANONICAL_INTAKE_UNITS.json")
relation_doc = load("registry/relations/E306_CUR_CANONICAL_INTAKE_RELATIONS.json")
e306_view = load("registry/views/programme.erdos-306.json")
e307_view = load("registry/views/frontier.erdos-307.json")

check(manifest["state"] == "fixed-candidate", "manifest is not fixed-candidate")
check(manifest["summary"] == {
    "source_packets": 12, "itemized_packets": 12, "pending_packets": 0,
    "substantive_items": 75, "classified_items": 75, "unclassified_items": 0,
}, "manifest counts drift")
check(source_map["counts"]["source_packets_total"] == 12, "map source count drift")
check(source_map["counts"]["substantive_items_total"] == 75, "map item count drift")
check(source_map["counts"]["substantive_items_classified"] == 75, "classified count drift")
check(source_map["counts"]["substantive_items_unclassified"] == 0, "unclassified != 0")
check(source_map["counts"]["canonical_units_referenced"] == 26, "mapped unit count drift")
check(len(source_map["items"]) == 75, "map does not have 75 item records")
check(len({item["item_id"] for item in source_map["items"]}) == 75, "duplicate item id")
check(all(item["units"] for item in source_map["items"]), "empty source-to-unit mapping")

units = unit_doc["units"]
unit_ids = {unit["id"] for unit in units}
check(len(units) == len(unit_ids) == 26, "unit count/id uniqueness drift")
mapped_ids = {uid for item in source_map["items"] for uid in item["units"]}
check(mapped_ids == unit_ids, f"map/registry unit mismatch: {mapped_ids ^ unit_ids}")

relations = relation_doc["logical"] + relation_doc["discovery"]
relation_ids = {rel["id"] for rel in relations}
check(len(relation_doc["logical"]) == 22, "logical relation count drift")
check(len(relation_doc["discovery"]) == 5, "discovery relation count drift")
check(len(relations) == len(relation_ids), "duplicate relation id")
logical_types = {"depends-on", "uses", "implies", "equivalent-to", "generalizes",
                 "specializes", "refutes", "qualifies", "supersedes"}
discovery_types = {"motivates", "suggests", "analogous-to", "arose-from"}
for rel in relations:
    check(rel["source"] in unit_ids and rel["target"] in unit_ids, f"dangling relation {rel['id']}")
    allowed = logical_types if rel["plane"] == "logical" else discovery_types
    check(rel["type"] in allowed, f"relation plane/type mismatch {rel['id']}")
    if rel["plane"] == "discovery":
        check(rel["status"] == "captured-unreviewed", f"discovery upgrade {rel['id']}")

for unit in units:
    check(set(unit["relations"]) <= relation_ids, f"dangling relation on {unit['id']}")
    check(unit["provenance"], f"missing provenance on {unit['id']}")

authorial_ids = {
    "math.harmonic-analysis.finite-fourier.weighted-decoded-skeleton",
    "math.harmonic-analysis.finite-fourier.anchor-fibre-transference",
    "math.harmonic-analysis.finite-fourier.quantitative-target-observability",
    "math.combinatorics.finite-configurations.complete-family-mass",
    "math.number-theory.reciprocal-representations.aft-e306-conditional-application",
}
for unit in units:
    if unit["id"] in authorial_ids:
        check(all(ev["kind"] == "authorial-argument" for ev in unit["assurance"]),
              f"authorial unit epistemically upgraded: {unit['id']}")
        check(unit["workflow"] == "ready-for-review", f"authorial workflow drift: {unit['id']}")

route_expectations = {
    "math.number-theory.reciprocal-representations.dense-one-anchor-proof":
        "1d63273ede93e1b83abf1ab9073d91b76600c23c",
    "math.number-theory.reciprocal-representations.multiblock-proof":
        "5c12240e877fb10730508924d0b90ffa8f3a8973",
    "math.number-theory.reciprocal-representations.sparse-sensor-proof":
        "52463e45fe3ce9ac2d271cea0e0f5e93e6cd5b83",
}
by_id = {unit["id"]: unit for unit in units}
for uid, review_commit in route_expectations.items():
    unit = by_id[uid]
    check(unit["disposition"] == "established-in-scope", f"route disposition drift: {uid}")
    check(any(ev["kind"] == "independent-mathematical-review"
              and ev["effect"] == "support"
              and ev["provenance"]["commit"] == review_commit
              for ev in unit["assurance"]), f"missing exact independent review: {uid}")

formal = by_id["math.number-theory.reciprocal-representations.e306-formal-release-axis"]
trust = by_id["math.analytic-number-theory.prime-distribution.e306-formal-trust-boundary"]
check(any(ev["kind"] == "formal-kernel-check" for ev in formal["assurance"]), "formal evidence missing")
check(trust["disposition"] == "scope-split", "formal trust boundary erased")
check("two named" in trust["summary"], "two named analytic inputs not stated")

e307_id = "math.number-theory.arithmetic-derivatives.erdos-307-adjacent-open-programme"
check(by_id[e307_id]["disposition"] == "open", "E307 not open")
check(by_id[e307_id]["workflow"] == "dormant", "E307 was activated")
check("OPEN / SEPARATE / NOT LAUNCHED" in e307_view["status_statement"], "E307 separation missing")
check(not any(rel["plane"] == "logical" and e307_id in (rel["source"], rel["target"])
              for rel in relations), "logical E306/E307 edge introduced")

check(e306_view["sections"]["preferred_human_spine"] ==
      ["math.number-theory.reciprocal-representations.dense-one-anchor-proof"],
      "preferred route drift")
check("project view references natural units" in e306_view["nonduplication_rule"].lower(),
      "project view became identity boundary")

# Validate every immutable locator used by the map, units, evidence, and relations.
locators = []
locators.extend(item["source_locator"] for item in source_map["items"])
for unit in units:
    locators.extend(unit["provenance"])
    locators.extend(ev["provenance"] for ev in unit["assurance"])
for rel in relations:
    locators.extend(rel["provenance"])

unique = {}
for loc in locators:
    key = tuple(loc[k] for k in ("repository", "commit", "path", "blob", "anchor"))
    unique[key] = loc
    check(re.fullmatch(r"[0-9a-f]{40}", loc["commit"]) is not None, "bad commit")
    check(re.fullmatch(r"[0-9a-f]{40}", loc["blob"]) is not None, "bad blob")
    check(re.fullmatch(r"L[1-9][0-9]*-L[1-9][0-9]*", loc["anchor"]) is not None, "bad anchor")

math_git = Path(run("git", "rev-parse", "--git-common-dir"))
if not math_git.is_absolute():
    math_git = (ROOT / math_git).resolve()
grouped: dict[Path, list[dict]] = defaultdict(list)
for loc in unique.values():
    git_dir = SOURCE_GIT if loc["repository"] == "Yuren-Tang/erdos-306" else math_git
    grouped[git_dir].append(loc)
for git_dir, group in grouped.items():
    check(git_dir.exists(), f"missing git store {git_dir}")
    blobs = batch_blobs(git_dir, sorted({loc["blob"] for loc in group}))
    # A commit:path resolves to the recorded blob; one batch-check process avoids
    # repeated macOS developer-tool startup overhead.
    specs = [f"{loc['commit']}:{loc['path']}" for loc in group]
    resolved = subprocess.run(
        ["git", f"--git-dir={git_dir}", "cat-file", "--batch-check=%(objectname)"],
        input="\n".join(specs) + "\n", text=True, stdout=subprocess.PIPE,
        stderr=subprocess.PIPE, check=True,
    ).stdout.splitlines()
    check(len(group) == len(resolved), f"batch-check result count drift for {git_dir}")
    for loc, actual_blob in zip(group, resolved):
        check(actual_blob == loc["blob"], f"blob mismatch {loc['commit']}:{loc['path']}")
        start, end = (int(x) for x in re.fullmatch(r"L([0-9]+)-L([0-9]+)", loc["anchor"]).groups())
        line_count = len(blobs[loc["blob"]].decode(errors="strict").splitlines())
        check(1 <= start <= end <= line_count, f"bad anchor range {loc}")

check(run("git", "merge-base", "HEAD", BASE) == BASE, "exact base is not an ancestor")
check(run("git", "branch", "--show-current") == "curation/erdos-306-current-best-v2", "wrong branch")
status = run("git", "status", "--porcelain=v1", "--untracked-files=all").splitlines()
changed_paths = [line[3:] for line in status if line]
check(not any(path.startswith("projects/affine-cdc/") for path in changed_paths),
      "AffineCDC path changed")
check(not any(path.startswith("lean/") for path in changed_paths), "Lean production changed")

try:
    import jsonschema
except ImportError:
    jsonschema = None
if jsonschema:
    unit_schema = load("registry/schema/mathematical-unit.schema.json")
    relation_schema = load("registry/schema/typed-relation.schema.json")
    for unit in units:
        jsonschema.validate(unit, unit_schema)
    for rel in relations:
        jsonschema.validate(rel, relation_schema)

print("PASS E306-CUR-CANONICAL-INTAKE")
print(f"sources=12 items=75 units={len(units)} logical={len(relation_doc['logical'])} discovery={len(relation_doc['discovery'])}")
print(f"immutable_locators={len(unique)} unclassified=0")
print("dense=preferred/independent multiblock=fallback/independent sparse=alternative/independent")
print("AFT=authorial formal=orthogonal-conditional E307=OPEN-SEPARATE-NOT-LAUNCHED")
