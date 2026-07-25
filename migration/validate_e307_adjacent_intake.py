#!/usr/bin/env python3
"""Bounded validator for E307-ADJACENT-CANONICAL-INTAKE."""

from __future__ import annotations

import json
import os
import re
import subprocess
from collections import defaultdict, deque
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = "b047efd5f43386f71dd9d2af1c9d5d531bd03163"
SOURCE_GIT = Path(os.environ.get("E307_SOURCE_GIT_DIR", "/private/tmp/erdos-306-e307-source.git"))


def load(path: str):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def run(*args: str) -> str:
    return subprocess.run(args, cwd=ROOT, text=True, capture_output=True, check=True).stdout.strip()


def check(value: bool, message: str) -> None:
    if not value:
        raise AssertionError(message)


manifest = load("sources/manifests/E307_ADJACENT_CANONICAL_INTAKE_SOURCE_MANIFEST.json")
source_map = load("migration/source-to-unit-map/E307_ADJACENT_CANONICAL_INTAKE_MAP.json")
unit_doc = load("registry/units/number-theory/arithmetic-derivatives/E307_ADJACENT_CANONICAL_INTAKE_UNITS.json")
relation_doc = load("registry/relations/E307_ADJACENT_CANONICAL_INTAKE_RELATIONS.json")
view = load("registry/views/frontier.erdos-307.json")
assurance_map = load("registry/assurance/E307_ADJACENT_ASSURANCE_AND_ATTRIBUTION_MAP.json")
units = unit_doc["units"]
unit_ids = {unit["id"] for unit in units}
relations = relation_doc["logical"] + relation_doc["discovery"]

check(manifest["state"] == "fixed-candidate", "manifest is not fixed")
check(manifest["summary"] == {
    "source_packets": 2, "substantive_items": 38,
    "classified_items": 38, "unclassified_items": 0,
}, "manifest counts drift")
check(source_map["counts"]["substantive_items_total"] == 38, "map item count drift")
check(source_map["counts"]["substantive_items_classified"] == 38, "classified count drift")
check(source_map["counts"]["substantive_items_unclassified"] == 0, "unclassified != 0")
check(len(source_map["items"]) == 38, "not 38 item records")
check(len({item["item_id"] for item in source_map["items"]}) == 38, "duplicate item id")
check(all(item["units"] for item in source_map["items"]), "empty item mapping")
check(len(units) == len(unit_ids) == source_map["counts"]["canonical_units_referenced"] == 36,
      "unit count/id drift")
check({uid for item in source_map["items"] for uid in item["units"]} == unit_ids,
      "source map does not cover every new unit")
check(len(relation_doc["logical"]) == 35 and len(relation_doc["discovery"]) == 8,
      "relation count drift")
check(len({rel["id"] for rel in relations}) == len(relations), "duplicate relation id")

forms = {"concept", "definition", "problem", "question", "conjecture", "claim", "theorem",
         "construction", "method", "proof", "example", "counterexample", "obstruction",
         "heuristic", "experiment", "computation", "connection"}
maturities = {"captured", "formulated", "tested", "proof-sketch", "author-complete", "assessed"}
dispositions = {"unassessed", "open", "supported", "established-in-scope", "refuted-in-scope",
                "scope-split", "conflicted", "superseded"}
workflows = {"captured", "active", "blocked", "ready-for-review", "ready-for-integration",
             "integrated", "dormant", "closed"}
evidence_kinds = {"authorial-argument", "computation", "independent-reproduction",
                  "independent-mathematical-review", "formal-kernel-check",
                  "source-fidelity-check", "literature-check", "external-review"}
evidence_effects = {"support", "refute", "qualify", "inconclusive"}
for unit in units:
    check(re.fullmatch(r"math\.[a-z0-9]+(?:[.-][a-z0-9]+)*", unit["id"]) is not None,
          f"unit id schema violation {unit['id']}")
    check(unit["form"] in forms and unit["maturity"] in maturities and
          unit["disposition"] in dispositions and unit["workflow"] in workflows,
          f"unit enum schema violation {unit['id']}")
    check(unit["provenance"], f"empty provenance {unit['id']}")
    for evidence in unit["assurance"]:
        check(evidence["kind"] in evidence_kinds and evidence["effect"] in evidence_effects
              and evidence["scope"], f"evidence schema violation {unit['id']}")

logical_types = {"depends-on", "uses", "implies", "equivalent-to", "generalizes",
                 "specializes", "refutes", "qualifies", "supersedes"}
discovery_types = {"motivates", "suggests", "analogous-to", "arose-from"}
external = {"math.number-theory.reciprocal-representations.squarefree-semiprime-characterization"}
for relation in relations:
    check(re.fullmatch(r"rel\.[a-z0-9]+(?:[.-][a-z0-9]+)*", relation["id"]) is not None,
          f"relation id schema violation {relation['id']}")
    check(relation["source"] in unit_ids | external and relation["target"] in unit_ids | external,
          f"dangling relation {relation['id']}")
    allowed = logical_types if relation["plane"] == "logical" else discovery_types
    check(relation["type"] in allowed, f"plane/type mismatch {relation['id']}")
    if relation["plane"] == "discovery":
        check(relation["status"] == "captured-unreviewed", f"discovery upgrade {relation['id']}")

by_id = {unit["id"]: unit for unit in units}
problem = "math.number-theory.arithmetic-derivatives.erdos-307-existence-problem"
blocked = "math.harmonic-analysis.finite-fourier.normalized-prime-jet-flatness-transference-block"
contraction = "math.number-theory.arithmetic-derivatives.two-step-contraction-claim"
direct = "math.number-theory.arithmetic-derivatives.direct-core30-rebound-counterexample"
relay = "math.number-theory.arithmetic-derivatives.giuga-relay-rebound-counterexample"
natural = "math.number-theory.arithmetic-derivatives.natural66-bounded-terminal-exclusion"

check(by_id[problem]["disposition"] == "open" and by_id[problem]["workflow"] == "dormant",
      "E307 was solved/launched")
check(view["status_statement"].startswith("OPEN / SEPARATE / NOT SOLVED"), "headline drift")
check(by_id[blocked]["disposition"] == "refuted-in-scope" and by_id[blocked]["workflow"] == "blocked",
      "normalized-jet block erased")
blocked_text = by_id[blocked]["summary"] + " " + " ".join(by_id[blocked].get("notes", []))
for token in ("k=0", "chi_l", "chi_H", "l-1", "Theorem 7.1", "criterion 7.4"):
    check(token in blocked_text, f"missing exact normalized-jet defect token {token}")
check(not any(rel["source"] == blocked and rel["type"] in
              {"implies", "equivalent-to", "generalizes", "specializes"}
              for rel in relation_doc["logical"]), "blocked claim traverses as proof")
check(by_id[contraction]["disposition"] == "refuted-in-scope", "contraction not refuted")
for counter in (direct, relay):
    check(any(rel["source"] == counter and rel["target"] == contraction and rel["type"] == "refutes"
              for rel in relation_doc["logical"]), f"counterexample scope drift {counter}")
    check(not any(rel["source"] == counter and rel["target"] == problem and rel["type"] == "refutes"
                  for rel in relation_doc["logical"]), f"counterexample overgeneralized {counter}")
check("C even" in " ".join(by_id[direct]["notes"]) and "l=2" in " ".join(by_id[direct]["notes"]),
      "direct rebound parity qualification missing")
natural_text = by_id[natural]["summary"] + " ".join(by_id[natural]["notes"])
for token in ("66 windows", "14,675", "0 integral"):
    check(token in natural_text, f"Natural-66 bounded scope missing {token}")

bado = by_id["math.number-theory.arithmetic-derivatives.bado-squarefree-two-cycle-framework"]
wang = by_id["math.number-theory.arithmetic-derivatives.wang-port-framework-antecedent"]
split = by_id["math.number-theory.arithmetic-derivatives.moving-quadratic-splitting-character-obstruction"]
coeff = by_id["math.number-theory.arithmetic-derivatives.prime-symbol-shift-divided-power-coefficients"]
literature = by_id["math.number-theory.arithmetic-derivatives.bounded-literature-attribution-facet"]
check("prior art" in bado["summary"].lower() and "must be attributed" in bado["summary"].lower(),
      "Bado attribution drift")
check("antecedent" in wang["summary"].lower() and
      "specializations/generalizations" in wang["summary"], "Wang boundary drift")
check("moving quadratic splitting-character obstruction" in split["title"].lower(),
      "moving splitting terminology drift")
check("prime-symbol shift divided-power" in coeff["title"].lower() and
      "Hasse-Schmidt-type" in coeff["summary"], "coefficient terminology drift")
check("does not establish comprehensive novelty, correctness or publication priority" in
      literature["summary"], "literature facet overreach")
check(any("prime inverse-phase provider" in gap for gap in view["remaining_gaps"]),
      "prime inverse-phase provider not open")
check(assurance_map["attribution"]["mechanism_novelty"] == "unresolved",
      "mechanism novelty upgraded")
check(assurance_map["independent_reproduction"]["bounded_diagnostic_only"] == {
    "unit": natural, "windows": 66, "integer_q_values": 14675,
    "integral_pairs": 0, "general_exclusion": False,
}, "bounded reproduction map drift")
check(assurance_map["blocked"]["forbidden_as_logical_provider"] is True,
      "blocked provider not forbidden")

# Resolve every immutable item locator and all registry/relation provenance.
locators = [item["source_locator"] for item in source_map["items"]]
locators.append(source_map["classification_authority"])
for unit in units:
    locators += unit["provenance"]
    locators += [evidence["provenance"] for evidence in unit["assurance"]]
for relation in relations:
    locators += relation["provenance"]
unique = {}
for loc in locators:
    key = tuple(loc[k] for k in ("repository", "commit", "path", "blob", "anchor"))
    unique[key] = loc
    check(re.fullmatch(r"[0-9a-f]{40}", loc["commit"]) is not None, "bad commit")
    check(re.fullmatch(r"[0-9a-f]{40}", loc["blob"]) is not None, "bad blob")
    match = re.fullmatch(r"L([1-9][0-9]*)-L([1-9][0-9]*)", loc["anchor"])
    check(match is not None, "bad anchor")
ordered = list(unique.values())
specs = [f"{loc['commit']}:{loc['path']}" for loc in ordered]
actual_blobs = subprocess.run(
    ["git", f"--git-dir={SOURCE_GIT}", "cat-file", "--batch-check=%(objectname)"],
    input="\n".join(specs) + "\n", text=True, capture_output=True, check=True,
).stdout.splitlines()
check(len(actual_blobs) == len(ordered), "batch locator count drift")

object_ids = sorted({loc["blob"] for loc in ordered})
proc = subprocess.Popen(
    ["git", f"--git-dir={SOURCE_GIT}", "cat-file", "--batch"],
    stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
)
assert proc.stdin is not None and proc.stdout is not None
for object_id in object_ids:
    proc.stdin.write((object_id + "\n").encode())
proc.stdin.close()
line_counts = {}
for expected in object_ids:
    header = proc.stdout.readline().decode().rstrip("\n").split()
    check(len(header) == 3 and header[0] == expected and header[1] == "blob",
          f"bad batch header {expected}: {header}")
    payload = proc.stdout.read(int(header[2]))
    check(proc.stdout.read(1) == b"\n", f"missing batch delimiter {expected}")
    line_counts[expected] = len(payload.decode(errors="strict").splitlines())
stderr = proc.stderr.read().decode() if proc.stderr else ""
check(proc.wait() == 0, f"batch blob read failed: {stderr}")

for loc, actual in zip(ordered, actual_blobs):
    check(actual == loc["blob"], f"blob mismatch {loc['path']}")
    start, end = (int(value) for value in re.fullmatch(
        r"L([1-9][0-9]*)-L([1-9][0-9]*)", loc["anchor"]).groups())
    check(1 <= start <= end <= line_counts[loc["blob"]],
          f"anchor out of range {loc['path']}")

check(run("git", "merge-base", "HEAD", BASE) == BASE, "wrong ancestry")
check(run("git", "branch", "--show-current") == "curation/erdos-307-adjacent-v1", "wrong branch")
status = run("git", "status", "--porcelain=v1", "--untracked-files=all").splitlines()
changed = set(run("git", "diff", "--name-only", BASE).splitlines())
changed |= {line[3:] for line in status if line}
for forbidden in ("projects/affine-cdc/", "registry/units/number-theory/reciprocal-representations/",
                  "projects/erdos-306/", "lean/"):
    check(not any(path.startswith(forbidden) for path in changed), f"forbidden path delta {forbidden}")

try:
    import jsonschema
except ImportError:
    jsonschema = None
if jsonschema:
    unit_schema = load("registry/schema/mathematical-unit.schema.json")
    relation_schema = load("registry/schema/typed-relation.schema.json")
    for unit in units:
        jsonschema.validate(unit, unit_schema)
    for relation in relations:
        jsonschema.validate(relation, relation_schema)

print("PASS E307-ADJACENT-CANONICAL-INTAKE")
print(f"items=38 units={len(units)} logical=35 discovery=8 unclassified=0")
print(f"immutable_provenance_objects={len(unique)} E307=OPEN-SEPARATE-NOT-SOLVED")
print("normalized-jet=BLOCKED direct-parity=QUALIFIED Natural66=BOUNDED")
print("literature=BOUNDED-ATTRIBUTION-TERMINOLOGY-ONLY")
