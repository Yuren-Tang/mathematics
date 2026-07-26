#!/usr/bin/env python3
"""Independent validator for PORT-SOURCE-DISPOSITION-CLOSEOUT."""

from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import tempfile
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BASE = "ce577e23ea9b2493cd912af8c1335b67e8ddebec"
ORIENTATION = "e6af5645107d0f21ac6c262c63a1db5dab8f0fd1"
ROOT_LIFT = "81da79782da348fac629b42882e447f95e4c9d3a"
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
E307_GIT = Path(
    os.environ.get(
        "E307_SOURCE_GIT_DIR",
        "/private/tmp/erdos-306-e307-source.git",
    )
)


def load(path: str):
    return json.loads((ROOT / path).read_text())


def run(*args: str, cwd: Path = ROOT, env: dict | None = None) -> str:
    return subprocess.run(
        args,
        cwd=cwd,
        text=True,
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        env=env,
    ).stdout.strip()


def check(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def git_tree(git_dir: Path, commit: str) -> tuple[str, dict[str, tuple[str, str]]]:
    resolved = run("git", f"--git-dir={git_dir}", "rev-parse", f"{commit}^{{commit}}")
    check(resolved == commit, f"commit resolution drift: {commit}")
    tree = run("git", f"--git-dir={git_dir}", "rev-parse", f"{commit}^{{tree}}")
    output = run(
        "git",
        f"--git-dir={git_dir}",
        "ls-tree",
        "-r",
        "--format=%(objectmode)%x09%(objectname)%x09%(path)",
        commit,
    )
    items = {}
    for line in output.splitlines():
        mode, blob, path = line.split("\t", 2)
        items[path] = (mode, blob)
    return tree, items


def batch_blob_payloads(git_dir: Path, blob_ids: list[str]) -> dict[str, bytes]:
    ids = sorted(set(blob_ids))
    proc = subprocess.Popen(
        ["git", f"--git-dir={git_dir}", "cat-file", "--batch"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    assert proc.stdin is not None and proc.stdout is not None
    proc.stdin.write(("\n".join(ids) + "\n").encode())
    proc.stdin.close()
    payloads = {}
    for expected in ids:
        header = proc.stdout.readline().decode().rstrip("\n")
        fields = header.split()
        check(
            len(fields) == 3 and fields[0] == expected and fields[1] == "blob",
            f"bad blob header {expected}: {header}",
        )
        size = int(fields[2])
        payloads[expected] = proc.stdout.read(size)
        check(proc.stdout.read(1) == b"\n", f"missing blob delimiter: {expected}")
    stderr = proc.stderr.read().decode() if proc.stderr else ""
    check(proc.wait() == 0, f"cat-file batch failed: {stderr}")
    return payloads


manifest = load("sources/manifests/PORT_SOURCE_DISPOSITION_CLOSEOUT_SOURCE_MANIFEST.json")
source_map = load("migration/source-to-unit-map/PORT_SOURCE_DISPOSITION_CLOSEOUT_MAP.json")
root_doc = load(
    "registry/units/graph-theory/flows/"
    "PORT_SOURCE_DISPOSITION_CLOSEOUT_ROOT_LIFT_UNITS.json"
)
trust_doc = load(
    "registry/units/analytic-number-theory/prime-distribution/"
    "PORT_SOURCE_DISPOSITION_CLOSEOUT_TRUST_UNITS.json"
)
relation_doc = load("registry/relations/PORT_SOURCE_DISPOSITION_CLOSEOUT_RELATIONS.json")
affine_view = load("registry/views/programme.affine-cdc.json")
e306_view = load("registry/views/programme.erdos-306.json")
e306_units = load(
    "registry/units/number-theory/reciprocal-representations/"
    "E306_CUR_CANONICAL_INTAKE_UNITS.json"
)

check(manifest["state"] == "fixed-candidate", "manifest is not fixed-candidate")
check(manifest["canonical_base"] == BASE, "manifest base drift")
check(manifest["summary"] == {
    "source_refs": 10,
    "full_tree_items": 848,
    "source_scope_items": 498,
    "unresolved_refs": 0,
    "delete_safe_refs": 0,
}, "manifest summary drift")
check(len(manifest["sources"]) == 10, "ten-ref manifest drift")
check(
    all(source["retention"] == "retained-not-delete-safe" for source in manifest["sources"]),
    "a source was marked deletion-safe",
)

math_git = Path(run("git", "rev-parse", "--git-common-dir"))
if not math_git.is_absolute():
    math_git = (ROOT / math_git).resolve()
repository_git = {
    "Yuren-Tang/mathematics": math_git,
    "Yuren-Tang/affine-cdc-workbench": PAPER_GIT,
    "Yuren-Tang/erdos-306": E306_GIT,
}
tree_cache: dict[tuple[Path, str], tuple[str, dict[str, tuple[str, str]]]] = {}
manifest_items: dict[tuple[str, str], dict] = {}
grouped_blobs: dict[Path, list[str]] = defaultdict(list)
expected_scope_counts = [17, 23, 1, 2, 2, 2, 45, 110, 169, 127]
for source, expected_scope in zip(manifest["sources"], expected_scope_counts):
    git_dir = repository_git[source["repository"]]
    check(git_dir.exists(), f"missing source git store: {git_dir}")
    tree, actual = git_tree(git_dir, source["commit"])
    tree_cache[(git_dir, source["commit"])] = (tree, actual)
    check(tree == source["tree"], f"tree hash drift: {source['source_id']}")
    check(len(actual) == source["full_tree_item_count"], f"tree item count drift: {source['source_id']}")
    check(source["source_scope_item_count"] == expected_scope, f"scope count drift: {source['source_id']}")
    check(len(source["source_scope_paths"]) == len(set(source["source_scope_paths"])) == expected_scope,
          f"scope path uniqueness drift: {source['source_id']}")
    check(set(source["source_scope_paths"]) <= set(actual), f"scope path missing: {source['source_id']}")
    recorded = source["full_tree_items"]
    check(len(recorded) == len(actual), f"recorded tree length drift: {source['source_id']}")
    for item in recorded:
        key = (source["source_id"], item["path"])
        check(key not in manifest_items, f"duplicate manifest path: {key}")
        manifest_items[key] = item
        check(actual[item["path"]] == (item["object_mode"], item["blob"]), f"tree/blob mismatch: {key}")
        check(item["commit"] == source["commit"], f"locator commit drift: {key}")
        check(item["repository"] == source["repository"], f"locator repo drift: {key}")
        check(item["anchor"] == f"blob:{item['blob']}", f"whole-blob anchor drift: {key}")
        check(re.fullmatch(r"[0-9a-f]{40}", item["blob"]) is not None, f"bad blob hash: {key}")
        grouped_blobs[git_dir].append(item["blob"])

for git_dir, blobs in grouped_blobs.items():
    batch_blob_payloads(git_dir, blobs)

orientation = next(s for s in manifest["sources"] if s["source_id"] == "ac-orientation")
root_lift = next(s for s in manifest["sources"] if s["source_id"] == "ac-root-lift")
check(run("git", f"--git-dir={math_git}", "merge-base", ORIENTATION, ROOT_LIFT) == ORIENTATION,
      "root-lift is not exact orientation successor")
orientation_blobs = {
    path: manifest_items[("ac-orientation", path)]["blob"]
    for path in orientation["source_scope_paths"]
}
root_lift_blobs = {
    path: manifest_items[("ac-root-lift", path)]["blob"]
    for path in root_lift["source_scope_paths"]
}
check(all(root_lift_blobs.get(path) == blob for path, blob in orientation_blobs.items()),
      "17 orientation blobs are not exactly recovered by root-lift")
check(len(set(root_lift["source_scope_paths"]) - set(orientation["source_scope_paths"])) == 6,
      "root-lift unique dossier count drift")

counts = source_map["counts"]
check(counts["source_refs_total"] == counts["source_refs_classified"] == 10, "source ref classification drift")
check(counts["source_refs_unclassified"] == 0, "unclassified source ref")
check(counts["source_scope_items_total"] == counts["source_scope_items_classified"] == 498,
      "source item classification drift")
check(counts["source_scope_items_unclassified"] == 0, "unclassified source item")
entries = source_map["entries"]
check(len(entries) == 498, "map length drift")
check(len({entry["item_id"] for entry in entries}) == 498, "duplicate map item id")
map_keys = {(entry["source_id"], entry["source_item"]) for entry in entries}
scope_keys = {
    (source["source_id"], path)
    for source in manifest["sources"]
    for path in source["source_scope_paths"]
}
check(map_keys == scope_keys, f"map/scope mismatch: {map_keys ^ scope_keys}")
allowed_dispositions = {
    "duplicate-of", "map-only", "new-canonical-unit", "non-mathematical-control",
    "projection-only", "retained-source", "source-topology-superseded",
    "superseded-by",
}
for entry in entries:
    check(entry["disposition"] in allowed_dispositions, f"unclassified disposition: {entry['item_id']}")
    check(entry["retention"] == "retained-not-delete-safe", f"delete-safe map entry: {entry['item_id']}")
    item = manifest_items[(entry["source_id"], entry["source_item"])]
    for key in ("repository", "commit", "path", "blob", "anchor"):
        check(entry["source_locator"][key] == item[key], f"map locator drift: {entry['item_id']} {key}")
    check(entry["units"] or entry["canonical_consumers"] or
          entry["disposition"] in {"non-mathematical-control", "retained-source"},
          f"mapped item has no unit/consumer/terminal reason: {entry['item_id']}")

by_source_class = Counter((e["source_id"], e["classification"]) for e in entries)
expected_e306 = {
    ("e306-clear-up", "formal-release-duplicate"): 94,
    ("e306-clear-up", "formal-recovery-history"): 10,
    ("e306-clear-up", "public-projection-or-legal"): 3,
    ("e306-clear-up", "repository-control"): 3,
    ("e306-pushlinter", "conditional-formal-source"): 153,
    ("e306-pushlinter", "conditional-structural-trust-boundary"): 1,
    ("e306-pushlinter", "formal-projection-or-evidence"): 6,
    ("e306-pushlinter", "legal-source"): 1,
    ("e306-pushlinter", "repository-control"): 8,
    ("e306-complete-pair-prepared", "formal-release-base"): 101,
    ("e306-complete-pair-prepared", "absorbed-by-repaired-multiblock"): 16,
    ("e306-complete-pair-prepared", "pre-repair-proof-source"): 3,
    ("e306-complete-pair-prepared", "public-projection"): 2,
    ("e306-complete-pair-prepared", "programme-marker"): 2,
    ("e306-complete-pair-prepared", "repository-control"): 3,
}
for key, expected in expected_e306.items():
    check(by_source_class[key] == expected, f"E306 disposition count drift: {key}")

for source_id in {
    "ac-adaptive-ordering", "ac-binary-eight", "ac-outer-shell", "ac-outer-promotion"
}:
    check(all(e["disposition"] == "map-only" for e in entries if e["source_id"] == source_id),
          f"AC map-only source drift: {source_id}")
    for entry in (e for e in entries if e["source_id"] == source_id):
        for consumer in entry["canonical_consumers"]:
            actual = run("git", "rev-parse", f"{consumer['commit']}:{consumer['path']}")
            check(actual == consumer["blob"], f"AC canonical consumer drift: {entry['item_id']}")

paper_entries = [e for e in entries if e["source_id"] == "ac-paper-revision"]
check(len(paper_entries) == 45 and all(e["disposition"] == "projection-only" for e in paper_entries),
      "paper projection map drift")
paper_text = json.dumps(paper_entries)
for phrase in ("NOT A FINAL RETURN", "NOT EXTERNAL-REVIEW-READY", "submission NONE"):
    check(phrase in paper_text, f"paper boundary missing: {phrase}")

units = root_doc["units"] + trust_doc["units"]
unit_ids = {unit["id"] for unit in units}
check(len(root_doc["units"]) == 23, "root-lift unit count drift")
check(len(trust_doc["units"]) == 1, "trust unit count drift")
check(len(unit_ids) == 24, "new unit ID uniqueness drift")
all_registry_ids = set()
for path in (ROOT / "registry/units").rglob("*.json"):
    all_registry_ids.update(unit["id"] for unit in json.loads(path.read_text())["units"])
check(unit_ids <= all_registry_ids, "new units missing from registry")

forms = {
    "concept", "definition", "problem", "question", "conjecture", "claim",
    "theorem", "construction", "method", "proof", "example", "counterexample",
    "obstruction", "heuristic", "experiment", "computation", "connection",
}
maturities = {"captured", "formulated", "tested", "proof-sketch", "author-complete", "assessed"}
dispositions = {
    "unassessed", "open", "supported", "established-in-scope",
    "refuted-in-scope", "scope-split", "conflicted", "superseded",
}
workflows = {
    "captured", "active", "blocked", "ready-for-review",
    "ready-for-integration", "integrated", "dormant", "closed",
}
map_locator_keys = {
    (e["source_locator"]["repository"], e["source_locator"]["commit"],
     e["source_locator"]["path"], e["source_locator"]["blob"])
    for e in entries
}
for unit in units:
    check(unit["form"] in forms and unit["maturity"] in maturities, f"unit form/maturity drift: {unit['id']}")
    check(unit["disposition"] in dispositions and unit["workflow"] in workflows,
          f"unit disposition/workflow drift: {unit['id']}")
    check(unit["provenance"], f"unit provenance missing: {unit['id']}")
    for provenance in unit["provenance"]:
        key = tuple(provenance[k] for k in ("repository", "commit", "path", "blob"))
        check(key in map_locator_keys, f"reverse provenance not closed: {unit['id']}")

root_ids = {u["id"] for u in root_doc["units"]}
expected_negative_suffixes = {
    "rl-4-full-witness-recovery-false",
    "rl-10-support-only-canonical-obstruction-false",
    "rl-11-occurrence-class-is-omega-false",
    "rl-13-fixed-witness-is-omega-family-false",
    "rl5-3-binary-formulations-retain-signs-false",
    "rl8-3-per-lift-orientability-false",
}
negative_ids = {
    unit["id"] for unit in root_doc["units"] if unit["disposition"] == "refuted-in-scope"
}
check(negative_ids == {"math.graph-theory.flows.indexed-oriented-supports." + x
                       for x in expected_negative_suffixes},
      "root-lift negative completeness drift")
open_ids = {unit["id"] for unit in root_doc["units"] if unit["disposition"] == "open"}
check(open_ids == {
    "math.graph-theory.flows.indexed-oriented-supports.rl5-5-f5-converse-lift-open",
    "math.graph-theory.flows.indexed-oriented-supports.rl8-4-universal-fixed-fibre-vanishing-open",
}, "root-lift open-boundary drift")
for unit in root_doc["units"]:
    kinds = {ev["kind"] for ev in unit["assurance"]}
    check(kinds == {"authorial-argument", "literature-check"}, f"root assurance upgrade: {unit['id']}")
    check(not kinds & {"independent-mathematical-review", "formal-kernel-check"},
          f"root assurance upgrade: {unit['id']}")
    literature_scopes = " ".join(ev["scope"] for ev in unit["assurance"] if ev["kind"] == "literature-check")
    check("neither novelty nor priority" in literature_scopes, f"literature boundary drift: {unit['id']}")

trust = trust_doc["units"][0]
check(trust["id"].endswith("e306-pushlinter-pnt-mertens-structural-trust-boundary"),
      "pushlinter trust ID drift")
trust_text = json.dumps(trust)
for phrase in (
    "pnt_dyadic_prime_density", "mertens_dyadic_window_mass",
    "Scales k<5", "primitive provider theorem",
):
    check(phrase in trust_text, f"pushlinter trust boundary missing: {phrase}")
check({ev["kind"] for ev in trust["assurance"]} == {"source-fidelity-check"},
      "pushlinter formal/kernel assurance upgrade")

release_trust = next(
    unit for unit in e306_units["units"] if unit["id"] ==
    "math.analytic-number-theory.prime-distribution.e306-formal-trust-boundary"
)
release_text = json.dumps(release_trust)
for phrase in ("rosser_schoenfeld_cor3", "rosser_schoenfeld_thm5", "Rosser"):
    check(phrase in release_text, f"release trust attribution missing: {phrase}")
check("Ramar" not in release_text and "Saias" not in release_text,
      "obsolete Ramaré–Saias attribution remains")

relations = relation_doc["logical"] + relation_doc["discovery"]
check(len(relation_doc["logical"]) == 17 and len(relation_doc["discovery"]) == 0,
      "relation count drift")
check(len({relation["id"] for relation in relations}) == len(relations), "duplicate relation ID")
logical_types = {
    "depends-on", "uses", "implies", "equivalent-to", "generalizes",
    "specializes", "refutes", "qualifies", "supersedes",
}
discovery_types = {"motivates", "suggests", "analogous-to", "arose-from"}
for relation in relations:
    check(relation["source"] in all_registry_ids and relation["target"] in all_registry_ids,
          f"dangling relation: {relation['id']}")
    allowed = logical_types if relation["plane"] == "logical" else discovery_types
    check(relation["type"] in allowed, f"relation plane/type drift: {relation['id']}")
    check(relation["type"] != "implies", f"forbidden proof traversal introduced: {relation['id']}")

check(affine_view["sections"]["authorial_root_lift_scope_package"] ==
      [unit["id"] for unit in root_doc["units"]], "Affine view reconstruction drift")
check("remain open" in affine_view["status_statement"], "five-CDC open boundary missing")
check(trust["id"] in e306_view["sections"]["orthogonal_formal_axis"],
      "pushlinter trust scope missing from E306 view")
check("Rosser" in e306_view["status_statement"] and "separate conditional PNT/Mertens" in e306_view["status_statement"],
      "E306 view trust scope drift")

check(run("git", "branch", "--show-current") == "curation/portfolio-source-disposition-v1",
      "wrong closeout branch")
check(run("git", "merge-base", "HEAD", BASE) == BASE, "exact base is not ancestor")
changed = set(run("git", "diff", "--name-only", BASE).splitlines())
allowed_prefixes = (
    "registry/", "sources/manifests/", "migration/", "math/graph-theory/flows/",
    "math/analytic-number-theory/prime-distribution/", "projects/affine-cdc/",
    "projects/erdos-306/",
)
check(all(path.startswith(allowed_prefixes) for path in changed), "out-of-scope changed path")
check(not any(path.endswith(".tex") or path.endswith(".lean") for path in changed),
      "Lean or manuscript production path changed")
check(not any(path.startswith(("projects/erdos-307/", "registry/units/number-theory/arithmetic-derivatives/"))
              for path in changed), "E307 truth/view surface changed")
check(run("git", "diff", "--check", BASE) == "", "git diff --check failed")

# Schemas are usable even when the optional jsonschema package is unavailable:
# validate all required keys/enums above, then use jsonschema when installed.
try:
    import jsonschema
except ImportError:
    jsonschema = None
if jsonschema is not None:
    unit_schema = load("registry/schema/mathematical-unit.schema.json")
    relation_schema = load("registry/schema/typed-relation.schema.json")
    for unit in units:
        jsonschema.validate(unit, unit_schema)
    for relation in relations:
        jsonschema.validate(relation, relation_schema)

if os.environ.get("PORT_CLOSEOUT_SKIP_REPRO") != "1":
    with tempfile.TemporaryDirectory(
        prefix="port-source-disposition-repro-", dir="/private/tmp"
    ) as tmp:
        tmp_path = Path(tmp)
        run("git", "clone", "--shared", "--quiet", str(ROOT), str(tmp_path))
        head = run("git", "rev-parse", "HEAD")
        run("git", "checkout", "--quiet", head, cwd=tmp_path)
        env = dict(os.environ)
        env.update({
            "PORT_CLOSEOUT_PAPER_GIT_DIR": str(PAPER_GIT),
            "PORT_CLOSEOUT_E306_GIT_DIR": str(E306_GIT),
            "E307_SOURCE_GIT_DIR": str(E307_GIT),
        })
        run("python3", "migration/build_e306_knowledge_plane.py", cwd=tmp_path, env=env)
        run("python3", "migration/build_e307_adjacent_intake.py", cwd=tmp_path, env=env)
        run("python3", "migration/build_port_source_disposition_closeout.py", cwd=tmp_path, env=env)
        check(run("git", "status", "--porcelain=v1", "--untracked-files=all", cwd=tmp_path) == "",
              "generator reconstruction is not reproducible")

print("PASS PORT-SOURCE-DISPOSITION-CLOSEOUT")
print("refs=10 full_tree_items=848 source_scope_items=498 unclassified=0")
print("new_units=24 root_lift=23 trust_scope_split=1 logical=17 discovery=0")
print("orientation_recovered=17 root_unique_dossiers=6 all_refs=retained-not-delete-safe")
print("E306 clear_up=94dup+10history pushlinter=153formal+1trust complete_pair=117dup+3superseded")
print("paper=projection-only/no-publication main=unchanged E307=unchanged")
