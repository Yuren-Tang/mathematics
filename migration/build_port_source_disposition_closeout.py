#!/usr/bin/env python3
"""Build the final portfolio source-disposition closeout artifacts."""

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
BASE = "ce577e23ea9b2493cd912af8c1335b67e8ddebec"
RELEASE = "4582185de1e0e27416e9362e0cc7943c3d2fb4fe"
REPAIRED_MULTIBLOCK = "95a2ede1d40dae41a17fe26e4fe4b491bd94e947"

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
        "state": "fixed-candidate",
        "authority": "Yuren-Tang/research-workbench#15@5081149903",
        "canonical_base": BASE,
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
            "The semantic map never upgrades theorem, assurance, publication or main-movement status.",
        ],
    }


ROOT_PREFIX = "math.graph-theory.flows.indexed-oriented-supports."
TRUST_ID = (
    "math.analytic-number-theory.prime-distribution."
    "e306-pushlinter-pnt-mertens-structural-trust-boundary"
)
FORMAL_AXIS = (
    "math.number-theory.reciprocal-representations.e306-formal-release-axis"
)
RELEASE_TRUST = (
    "math.analytic-number-theory.prime-distribution.e306-formal-trust-boundary"
)
MULTIBLOCK = (
    "math.number-theory.reciprocal-representations.multiblock-proof"
)

# The exact 23-entry theorem/scope table in ROOT_LIFT_THEORY_RETURN.md.
ROOT_DEFS = [
    ("rl-1-reference-independent-root-flow", "Reference-independent A-root flow", "Reference-edge reversal changes both incidence and root sign, so the integral A_(q-1) root-flow object is reference-independent.", "definition", "supported", "support"),
    ("rl-2-directed-support-root-equivalence", "Directed support/root-flow equivalence", "Directed indexed Eulerian q-support systems and A_(q-1) root flows are mutually inverse at support-word level.", "theorem", "supported", "support"),
    ("rl-3-circuit-decomposition-existence", "Circuit-decomposition existence boundary", "A finite root flow gives some full oriented q-cycle-double-cover only after noncanonical directed circuit decomposition.", "theorem", "supported", "support"),
    ("rl-4-full-witness-recovery-false", "Canonical full-witness recovery is false", "The four-parallel-edge example gives distinct circuit pairings with one root flow, refuting canonical recovery of a prescribed full witness.", "counterexample", "refuted-in-scope", "refute"),
    ("rl-5-support-word-retained-data", "Support-word retained-data boundary", "Multiplicity two, distinct indices, repeated indexed supports and empty indices survive at support-word level; circuit partitions and occurrence names do not.", "theorem", "supported", "support"),
    ("rl-6-binary-root-support-equivalence", "Binary root/support equivalence", "Mod-2 root flows, unordered K_q roots and indexed even supports are equivalent at the unordered support level.", "theorem", "supported", "support"),
    ("rl-7-even-q-fully-deleted-target", "Even-q fully deleted target", "For even q the nondegenerate binary target is E_I modulo the all-one radical and has dimension q-2.", "theorem", "supported", "support"),
    ("rl-8-complementary-root-boundary", "Complementary-root boundary", "At q=4 the quotient identifies complementary roots; for even q at least 6 it retains the weight-two root labels.", "theorem", "supported", "support"),
    ("rl-9-prescribed-witness-cut-criterion", "Prescribed-witness cut criterion", "A prescribed full unoriented witness has an opposite-direction sign lift exactly when its occurrence twist word is a cut.", "theorem", "supported", "support"),
    ("rl-10-support-only-canonical-obstruction-false", "Support-only canonical obstruction is false", "Without a prescribed circuit decomposition fixed-support data has no single canonical occurrence obstruction.", "claim", "refuted-in-scope", "refute"),
    ("rl-11-occurrence-class-is-omega-false", "Occurrence class is not literally omega", "The occurrence-graph class and the source-graph omega class use different cochain gauges and are not literally identical objects.", "claim", "refuted-in-scope", "refute"),
    ("rl-12-fixed-event-omega-comparison", "Fixed-event omega comparison", "For retained affine faces, opposite-direction sign lifting and omega(g)=0 describe the same fixed event, inheriting the frozen OR1 authorial assurance.", "connection", "scope-split", "qualify"),
    ("rl-13-fixed-witness-is-omega-family-false", "Fixed witness is not fixed fibre", "A generic fixed-witness obstruction is not literally the fixed-fibre Omega_f object because the family quantifier differs.", "claim", "refuted-in-scope", "refute"),
    ("rl-14-frozen-fano-fibre-omega-specialization", "Frozen Fano-fibre Omega specialization", "Within the frozen Fano package, some compatible integral sign lift exists exactly when Omega_f vanishes; this inherits frozen OR1 assurance.", "connection", "scope-split", "qualify"),
    ("rl5-1-a4-five-support-specialization", "A4 five-support specialization", "An A4 root flow specializes to a directed indexed five-support word.", "theorem", "supported", "support"),
    ("rl5-2-five-support-binary-hierarchy", "Five-support binary hierarchy", "Reduction of the A4 object gives R5, K5 and O-(4,2) unordered data, without integral signs.", "theorem", "supported", "support"),
    ("rl5-3-binary-formulations-retain-signs-false", "Binary formulations do not retain integral signs", "Quadratic, Schur, cographic and stress formulations do not retain the integral orientation signs.", "claim", "refuted-in-scope", "refute"),
    ("rl5-4-global-f5-coefficient-projection", "Global F5 coefficient projection", "A single global identification of support indices with F5 projects every A4 root flow to a nowhere-zero F5 flow.", "theorem", "supported", "support"),
    ("rl5-5-f5-converse-lift-open", "Fixed F5 converse lift problem", "An arbitrary fixed nowhere-zero F5 flow does not canonically reconstruct an oriented five-support witness; the converse is a separate lift and holonomy problem.", "question", "open", "inconclusive"),
    ("rl8-1-a7-binary-orthogonal-fano-hierarchy", "A7/binary/orthogonal/Fano hierarchy", "The exact safe hierarchy is A7 to E8 to O+(6,2) to F2^3, with no automatic reverse arrows.", "theorem", "supported", "support"),
    ("rl8-2-fano-torsor-linear-family-search", "Fano torsor linearizes family search", "The compatible-lift torsor reduces the family sign search to a linear quotient, inheriting the frozen OR1 gauge package.", "connection", "scope-split", "qualify"),
    ("rl8-3-per-lift-orientability-false", "Per-lift Fano orientability is false", "The exact frozen K4 fibre contains both orientability types, so Fano compatibility does not force each lift to orient.", "counterexample", "refuted-in-scope", "refute"),
    ("rl8-4-universal-fixed-fibre-vanishing-open", "Universal fixed-fibre vanishing", "Universal vanishing of the fixed-Fano-fibre obstruction remains open in the existing research frontier.", "question", "open", "inconclusive"),
]
ROOT_IDS = [ROOT_PREFIX + slug for slug, *_ in ROOT_DEFS]


def manifest_locator(manifest: dict, source_id: str, path: str, anchor: str, role: str) -> dict:
    source = next(s for s in manifest["sources"] if s["source_id"] == source_id)
    item = next(i for i in source["full_tree_items"] if i["path"] == path)
    return {
        "repository": item["repository"],
        "commit": item["commit"],
        "path": item["path"],
        "blob": item["blob"],
        "anchor": anchor,
        "role": role,
    }


def root_units(manifest: dict) -> list[dict]:
    table_path = "projects/affine-cdc/research/root-lift/ROOT_LIFT_THEORY_RETURN.md"
    literature = manifest_locator(
        manifest,
        "ac-root-lift",
        "projects/affine-cdc/research/root-lift/LITERATURE_AND_NOVELTY_AUDIT.md",
        "L201-L246",
        "literature",
    )
    units = []
    for offset, (slug, title, summary, form, disposition, effect) in enumerate(ROOT_DEFS):
        line = 58 + offset
        provenance = manifest_locator(
            manifest, "ac-root-lift", table_path, f"L{line}-L{line}", "development"
        )
        open_unit = disposition == "open"
        units.append(
            {
                "id": ROOT_PREFIX + slug,
                "title": title,
                "summary": summary,
                "form": form,
                "maturity": "formulated" if open_unit else "author-complete",
                "assurance": [
                    {
                        "kind": "authorial-argument",
                        "effect": effect,
                        "scope": (
                            "the exact bounded scout theorem/scope entry only; "
                            "OR1-dependent comparisons inherit AUTHORIAL / "
                            "CURATOR-INTEGRATED / NOT INDEPENDENTLY AUDITED"
                        ),
                        "provenance": provenance,
                    },
                    {
                        "kind": "literature-check",
                        "effect": "qualify",
                        "scope": (
                            "bounded terminology and antecedent search only; "
                            "supports neither novelty nor priority and is not "
                            "independent mathematical review"
                        ),
                        "provenance": literature,
                    },
                ],
                "disposition": disposition,
                "workflow": "blocked" if open_unit else "ready-for-review",
                "provenance": [provenance],
                "relations": [],
                "views": ["programme.affine-cdc", "frontier.five-cdc"],
                "notes": [
                    "Integrated at bounded authorial scout strength; no assurance upgrade.",
                    "The universal five-support and five-CDC goals remain open.",
                ],
            }
        )
    return units


def trust_unit(manifest: dict) -> dict:
    provenance = manifest_locator(
        manifest,
        "e306-pushlinter",
        "lean/RequestProject/GlobalControl/AnalyticInputs.lean",
        "L23-L51",
        "formalization",
    )
    return {
        "id": TRUST_ID,
        "title": "E306 pushlinter structural PNT/Mertens trust boundary",
        "summary": (
            "The detached pushlinter formalization assumes "
            "pnt_dyadic_prime_density for k>=5 and an eventual "
            "mertens_dyadic_window_mass.  These are a separate conditional "
            "PNT/Mertens structural variant, not a formal proof of PNT or "
            "Mertens and not the v0.0.3 Rosser–Schoenfeld interface."
        ),
        "form": "concept",
        "maturity": "assessed",
        "assurance": [
            {
                "kind": "source-fidelity-check",
                "effect": "qualify",
                "scope": (
                    "exact names and statements of the two structural axioms; "
                    "no kernel, provider-theorem or release-status upgrade"
                ),
                "provenance": provenance,
            }
        ],
        "disposition": "scope-split",
        "workflow": "integrated",
        "provenance": [provenance],
        "relations": [],
        "views": ["programme.erdos-306"],
        "notes": [
            "Scales k<5 lie outside pnt_dyadic_prime_density and require separate finite treatment if consumed.",
            "mertens_dyadic_window_mass supplies only an eventual existential threshold; no primitive provider theorem or witness is formalized here.",
            "The source README contains a stale AnalyticInputs link and stronger final/audited prose; neither controls this disposition.",
        ],
    }


def build_relations(manifest: dict) -> dict:
    table = manifest_locator(
        manifest,
        "ac-root-lift",
        "projects/affine-cdc/research/root-lift/ROOT_LIFT_THEORY_RETURN.md",
        "L54-L80",
        "development",
    )
    logical_specs = [
        ("rl2-uses-rl1", 1, 0, "uses"),
        ("rl3-uses-rl2", 2, 1, "uses"),
        ("rl6-uses-rl2", 5, 1, "uses"),
        ("rl7-qualifies-rl6", 6, 5, "qualifies"),
        ("rl8-qualifies-rl7", 7, 6, "qualifies"),
        ("rl9-uses-rl2", 8, 1, "uses"),
        ("rl10-qualifies-rl9", 9, 8, "qualifies"),
        ("rl11-qualifies-rl12", 10, 11, "qualifies"),
        ("rl13-qualifies-rl14", 12, 13, "qualifies"),
        ("rl5-1-specializes-rl2", 14, 1, "specializes"),
        ("rl5-2-specializes-rl6", 15, 5, "specializes"),
        ("rl5-3-qualifies-rl5-2", 16, 15, "qualifies"),
        ("rl5-5-qualifies-rl5-4", 18, 17, "qualifies"),
        ("rl8-1-specializes-rl6", 19, 5, "specializes"),
        ("rl8-2-uses-rl14", 20, 13, "uses"),
        ("rl8-3-qualifies-rl8-2", 21, 20, "qualifies"),
        ("pushlinter-qualifies-release-trust", 23, -1, "qualifies"),
    ]
    ids = ROOT_IDS + [TRUST_ID]
    logical = []
    for name, source_index, target_index, relation_type in logical_specs:
        source = ids[source_index]
        target = RELEASE_TRUST if target_index == -1 else ids[target_index]
        logical.append(
            {
                "id": f"rel.port-source-closeout.{name}",
                "source": source,
                "target": target,
                "plane": "logical",
                "type": relation_type,
                "scope": "exact source-disposition closeout scope; no assurance implication",
                "status": "curator-mapped",
                "provenance": [
                    {k: table[k] for k in ("repository", "commit", "path", "blob", "anchor")}
                ],
            }
        )
    return {
        "schema_version": "1.0.0",
        "batch_id": "PORT-SOURCE-DISPOSITION-CLOSEOUT",
        "logical": logical,
        "discovery": [],
        "invariants": [
            "Logical and discovery planes remain separate.",
            "No relation upgrades authorial source assurance.",
            "The trust-boundary relation is a scope qualification, not a proof-provider edge.",
        ],
    }


def canonical_consumers(paths: list[str]) -> list[dict]:
    consumers = []
    for path in paths:
        blob = subprocess.run(
            ["git", "rev-parse", f"{BASE}:{path}"],
            cwd=ROOT,
            text=True,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        ).stdout.strip()
        consumers.append(
            {
                "repository": "Yuren-Tang/mathematics",
                "commit": BASE,
                "path": path,
                "blob": blob,
                "anchor": f"blob:{blob}",
            }
        )
    return consumers


OUTER_CONSUMERS = [
    "projects/affine-cdc/reduction/outer-shell-and-binary-flow.md",
    "projects/affine-cdc/complete-cdc/foundations-expansion-and-flow.md",
    "projects/affine-cdc/complete-cdc/collapse-decomposition-and-assembly.md",
]
PAPER_CONSUMERS = [
    "projects/affine-cdc/complete-cdc/affine-compatibility-and-extraction.md",
    "projects/affine-cdc/complete-cdc/audit-a-explicitness-repairs.md",
    "projects/affine-cdc/complete-cdc/foundations-expansion-and-flow.md",
    "projects/affine-cdc/complete-cdc/collapse-decomposition-and-assembly.md",
]


def source_tree_dict(git_dir: Path, commit: str) -> dict[str, str]:
    output = git(
        git_dir,
        "ls-tree",
        "-r",
        "--format=%(objectname)%x09%(path)",
        commit,
    )
    return {path: blob for blob, path in (line.split("\t", 1) for line in output.splitlines())}


def e306_classification(
    source_id: str,
    path: str,
    blob: str,
    release_tree: dict[str, str],
    repaired_tree: dict[str, str],
) -> tuple[str, list[str], list[dict], str, str]:
    control_prefixes = (".github/",)
    lean_config = {
        "lean/lake-manifest.json",
        "lean/lakefile.toml",
        "lean/lean-toolchain",
    }
    if source_id == "e306-clear-up":
        if path.startswith("lean/") or path in lean_config:
            if release_tree.get(path) == blob:
                return "duplicate-of", [FORMAL_AXIS], [], "formal-release-duplicate", f"{RELEASE}:{path}"
            return "retained-source", [FORMAL_AXIS], [], "formal-recovery-history", "successor:e55ef359a8b98525f0bac6c7a510fcad94469bff"
        if path in {"README.md", "CITATION.cff", "LICENSE"}:
            return "projection-only", [FORMAL_AXIS], [], "public-projection-or-legal", "retained"
        return "non-mathematical-control", [], [], "repository-control", "retained"
    if source_id == "e306-pushlinter":
        if path == "lean/RequestProject/GlobalControl/AnalyticInputs.lean":
            return "new-canonical-unit", [TRUST_ID, FORMAL_AXIS], [], "conditional-structural-trust-boundary", "retained"
        if path.startswith("lean/scripts/"):
            return "non-mathematical-control", [], [], "repository-control", "retained"
        if path.startswith("lean/"):
            return "retained-source", [FORMAL_AXIS], [], "conditional-formal-source", "retained"
        if path in {
            "docs/architecture.md",
            "docs/circle-method-map.md",
            "docs/construction-redesign.md",
            "docs/global-control-map.md",
            "README.md",
            "CITATION.cff",
        }:
            return "projection-only", [TRUST_ID, FORMAL_AXIS], [], "formal-projection-or-evidence", "retained"
        if path == "LICENSE":
            return "retained-source", [], [], "legal-source", "retained"
        return "non-mathematical-control", [], [], "repository-control", "retained"
    if source_id == "e306-complete-pair-prepared":
        if path.startswith("proof-development/"):
            if repaired_tree.get(path) == blob:
                return "duplicate-of", [MULTIBLOCK], [], "absorbed-by-repaired-multiblock", f"{REPAIRED_MULTIBLOCK}:{path}"
            if path in repaired_tree:
                return "superseded-by", [MULTIBLOCK], [], "pre-repair-proof-source", f"{REPAIRED_MULTIBLOCK}:{path}"
            return "non-mathematical-control", [], [], "programme-marker", "retained"
        if path.startswith(("research/", "review/")):
            return "non-mathematical-control", [], [], "programme-marker", "retained"
        if path.startswith("lean/"):
            return "duplicate-of", [FORMAL_AXIS], [], "formal-release-base", f"{RELEASE}:{path}"
        if path in {"README.md", "CITATION.cff"}:
            return "projection-only", [FORMAL_AXIS, MULTIBLOCK], [], "public-projection", "retained"
        return "non-mathematical-control", [], [], "repository-control", "retained"
    raise ValueError(source_id)


def build_source_map(manifest: dict) -> dict:
    consumers_outer = canonical_consumers(OUTER_CONSUMERS)
    consumers_paper = canonical_consumers(PAPER_CONSUMERS)
    release_tree = source_tree_dict(E306_GIT, RELEASE)
    repaired_tree = source_tree_dict(E306_GIT, REPAIRED_MULTIBLOCK)
    root_path_groups = {
        "ROOT_LIFT_DEFINITIONS_AND_EQUIVALENCE.md": ROOT_IDS[0:5],
        "MOD2_REDUCTION_AND_FIXED_WITNESS_OBSTRUCTION.md": ROOT_IDS[5:14],
        "Q5_ORIENTED_FIVE_SUPPORT_SPECIALISATION.md": ROOT_IDS[14:19],
        "Q8_FANO_SPECIALISATION.md": ROOT_IDS[19:23],
        "LITERATURE_AND_NOVELTY_AUDIT.md": ROOT_IDS,
        "ROOT_LIFT_THEORY_RETURN.md": ROOT_IDS,
    }
    source_dispositions = {
        "ac-orientation": "SOURCE-TOPOLOGY-SUPERSEDED-BY-ROOT-LIFT / RETAINED",
        "ac-root-lift": "INTEGRATED-AUTHORIAL-SOURCE / RETAINED",
        "ac-adaptive-ordering": "MAPPED-RETAIN / UNIQUE-MATH-ZERO",
        "ac-binary-eight": "MAPPED-RETAIN / UNIQUE-MATH-ZERO",
        "ac-outer-shell": "MAPPED-RETAIN / UNIQUE-MATH-ZERO",
        "ac-outer-promotion": "MAPPED-RETAIN / UNIQUE-MATH-ZERO",
        "ac-paper-revision": "PROJECTION-MAPPED-RETAIN / NO-PUBLICATION-DISPOSITION",
        "e306-clear-up": "PUBLIC-FORMAL-RECOVERY-ANCHOR / RETAINED",
        "e306-pushlinter": "CONDITIONAL-FORMALIZATION-SOURCE / RETAINED",
        "e306-complete-pair-prepared": "ABSORBED-BY-REPAIRED-MULTIBLOCK / UNIQUE-MECHANISM-ZERO / RETAINED",
    }
    entries = []
    for source in manifest["sources"]:
        by_path = {i["path"]: i for i in source["full_tree_items"]}
        for index, path in enumerate(source["source_scope_paths"], start=1):
            loc = {k: by_path[path][k] for k in ("repository", "commit", "path", "blob", "anchor")}
            sid = source["source_id"]
            units: list[str] = []
            consumers: list[dict] = []
            note = ""
            classification = ""
            successor = "retained"
            if sid == "ac-orientation":
                disposition = "source-topology-superseded"
                units = ROOT_IDS
                classification = "orientation-authorial-source"
                successor = ROOT_LIFT
                note = "The identical blob is recoverable in the root-lift successor; assurance remains authorial and not independently audited."
            elif sid == "ac-root-lift":
                leaf = Path(path).name
                if leaf in root_path_groups:
                    disposition = "new-canonical-unit"
                    units = root_path_groups[leaf]
                    classification = "root-lift-unique-dossier"
                else:
                    disposition = "retained-source"
                    units = ROOT_IDS
                    classification = "orientation-inherited-by-root-lift"
                note = "Bounded scout theorem/scope source only; no independent-review or novelty upgrade."
            elif sid in {"ac-adaptive-ordering", "ac-binary-eight", "ac-outer-shell", "ac-outer-promotion"}:
                disposition = "map-only"
                units = [
                    "math.graph-theory.cycle-covers.root-boundary-finite-core",
                    "math.graph-theory.cycle-covers.general-multigraph-outer-shell",
                ]
                consumers = consumers_outer
                classification = "canonical-consumer-closed"
                note = "No surviving unique mathematics; exact source retained."
            elif sid == "ac-paper-revision":
                disposition = "projection-only"
                consumers = consumers_paper
                classification = "manuscript-projection-or-history"
                note = "No new mathematics; NOT A FINAL RETURN / NOT EXTERNAL-REVIEW-READY / submission NONE; no TeX is copied and no publication disposition is made."
            else:
                disposition, units, consumers, classification, successor = e306_classification(
                    sid, path, loc["blob"], release_tree, repaired_tree
                )
                note = "Exact retained E306 source mapping; no theorem, formal-kernel, release or PNT/Mertens assurance upgrade."
            entries.append(
                {
                    "item_id": f"{sid}:{index:03d}",
                    "source_id": sid,
                    "source_item": path,
                    "source_locator": loc,
                    "disposition": disposition,
                    "classification": classification,
                    "units": units,
                    "canonical_consumers": consumers,
                    "successor_or_recovery": successor,
                    "retention": "retained-not-delete-safe",
                    "notes": [note],
                }
            )
    counts_by_source = {
        source["source_id"]: sum(1 for entry in entries if entry["source_id"] == source["source_id"])
        for source in manifest["sources"]
    }
    counts_by_disposition = {
        disposition: sum(1 for entry in entries if entry["disposition"] == disposition)
        for disposition in sorted({entry["disposition"] for entry in entries})
    }
    return {
        "schema_version": "1.0.0",
        "batch_id": "PORT-SOURCE-DISPOSITION-CLOSEOUT",
        "map_type": "item-level-source-disposition",
        "source_manifest": "sources/manifests/PORT_SOURCE_DISPOSITION_CLOSEOUT_SOURCE_MANIFEST.json",
        "unit_registries": [
            "registry/units/graph-theory/flows/PORT_SOURCE_DISPOSITION_CLOSEOUT_ROOT_LIFT_UNITS.json",
            "registry/units/analytic-number-theory/prime-distribution/PORT_SOURCE_DISPOSITION_CLOSEOUT_TRUST_UNITS.json",
        ],
        "source_dispositions": source_dispositions,
        "entries": entries,
        "counts": {
            "source_refs_total": 10,
            "source_refs_classified": 10,
            "source_refs_unclassified": 0,
            "source_scope_items_total": len(entries),
            "source_scope_items_classified": len(entries),
            "source_scope_items_unclassified": 0,
            "new_canonical_units": 24,
            "by_source": counts_by_source,
            "by_disposition": counts_by_disposition,
        },
        "invariants": [
            "Every authored source-scope item has exactly one disposition.",
            "Every entry retains an immutable full-SHA/path/blob/whole-blob anchor.",
            "All ten exact refs are retained and none is deletion-safe.",
            "Negative, false, open, superseded and pre-repair material remains recoverable at source strength.",
            "Root-lift and pushlinter trust metadata are integrated without epistemic upgrade.",
            "Paper is projection/source mapping only and has no publication disposition.",
            "unclassified = 0",
        ],
    }


def attach_relation_ids(units: list[dict], relation_doc: dict) -> None:
    by_id = {unit["id"]: unit for unit in units}
    for relation in relation_doc["logical"] + relation_doc["discovery"]:
        if relation["source"] in by_id:
            by_id[relation["source"]]["relations"].append(relation["id"])


def update_views(root_ids: list[str]) -> None:
    affine_path = ROOT / "registry/views/programme.affine-cdc.json"
    affine = json.loads(affine_path.read_text())
    affine["sections"]["authorial_root_lift_scope_package"] = root_ids
    affine["status_statement"] = (
        "AffineCDC contains a substantial independently assessed local and "
        "conditional corpus, four author-complete one-atom local results, and "
        "a 23-entry authorial root-lift theorem/scope package pending "
        "independent review. The cubic and universal five-support/five-CDC "
        "goals remain open."
    )
    write_json("registry/views/programme.affine-cdc.json", affine)

    e306_path = ROOT / "registry/views/programme.erdos-306.json"
    e306 = json.loads(e306_path.read_text())
    formal = e306["sections"]["orthogonal_formal_axis"]
    if TRUST_ID not in formal:
        formal.append(TRUST_ID)
    e306["status_statement"] = (
        "E306 has three independently assured human proof routes. The "
        "v0.0.3 Lean release is conditional on exact Rosser–Schoenfeld "
        "rosser_schoenfeld_cor3 / rosser_schoenfeld_thm5 inputs; the detached "
        "pushlinter line is a separate conditional PNT/Mertens structural-"
        "axiom variant with provider and finite-small-scale boundaries. "
        "Neither formal axis upgrades human-proof assurance, and E307 remains "
        "separate/open."
    )
    write_json("registry/views/programme.erdos-306.json", e306)


def build_prose(root_docs: list[dict]) -> None:
    rows = "\n".join(
        f"| `{unit['id'].removeprefix(ROOT_PREFIX)}` | {unit['form']} | "
        f"{unit['disposition']} | authorial; ready for independent review |"
        for unit in root_docs
    )
    write(
        "math/graph-theory/flows/indexed-oriented-supports-and-root-flows.md",
        f"""# Indexed oriented supports and type-A root flows

The exact current authorial statement is an equivalence between directed
indexed Eulerian support words and integral type-A root flows.  A full circuit
witness contains more data: circuit partitions and occurrence identity are
obtained only after a generally nonunique decomposition.  The
four-parallel-edge example permanently blocks canonical full-witness recovery.

The q=5 and q=8 projections are one-way hierarchies unless a separate integral
sign lift is supplied.  OR1 comparisons remain `AUTHORIAL /
CURATOR-INTEGRATED / NOT INDEPENDENTLY AUDITED`; universal fixed-fibre
vanishing and the arbitrary fixed F5 converse lift remain open.  The bounded
literature search supports only careful synthesis/terminology, not novelty or
priority.

| Entry | Form | Disposition | Assurance |
|---|---|---|---|
{rows}
""",
    )
    write(
        "math/analytic-number-theory/prime-distribution/e306-formal-analytic-trust-boundaries.md",
        """# E306 formal analytic trust boundaries

Two scope-split conditional formal interfaces must not be conflated.

The immutable `v0.0.3` release uses the exact Rosser–Schoenfeld leaf axioms
`rosser_schoenfeld_cor3` (1962, Corollary 3) and
`rosser_schoenfeld_thm5` (1962, Theorem 5).  Lean checks the reduction under
those inputs; it does not prove the classical analytic estimates.

The detached `codex/pushlinter@e55ef359...` line instead assumes the structural
interfaces `pnt_dyadic_prime_density` and
`mertens_dyadic_window_mass`.  It is retained conditional formalization, not a
formalization of PNT or Mertens and not a replacement release.  Scales below
`k=5` are outside the first axiom; the second supplies only an eventual
existential threshold.  Primitive provider theorems and any required finite
small-scale closure remain gaps.
""",
    )
    write(
        "projects/affine-cdc/SOURCE_DISPOSITION_CLOSEOUT.md",
        """# AffineCDC retained-source disposition

Root-lift is the source-topology successor of the retained orientation packet:
all 17 orientation blobs remain exactly recoverable, while six new dossiers
carry the 23-entry authorial theorem/scope package.  Supersession here means
source topology only, never an assurance upgrade or deletion authorization.

Adaptive ordering, binary-eight, outer-shell and outer-promotion sources are
map-only retained refs with exact canonical consumers.  The paper revision is
only a projection/source map: it contributes no new mathematics, copies no
TeX, remains `NOT A FINAL RETURN / NOT EXTERNAL-REVIEW-READY`, and has
submission authorization `NONE`.
""",
    )
    write(
        "projects/erdos-306/FORMAL_TRUST_BOUNDARY_SCOPE_SPLIT.md",
        """# E306 formal trust-boundary scope split

The released and detached formal lines use different analytic interfaces.
`v0.0.3` is conditional on exact Rosser–Schoenfeld Corollary 3 and Theorem 5
axioms.  The pushlinter line is separately conditional on structural PNT and
Mertens dyadic axioms and leaves provider/small-scale boundaries explicit.

`clear-up@63801a68...` remains the public formal recovery anchor.
`complete-pair@4348421...` has no surviving unique mechanism: sixteen proof
documents are exact repaired-multiblock duplicates and three are preserved
pre-repair sources superseded by the repaired multiblock.  Every ref remains
retained and none is deletion-safe.
""",
    )


def main() -> None:
    manifest = build_manifest()
    write_json(
        "sources/manifests/PORT_SOURCE_DISPOSITION_CLOSEOUT_SOURCE_MANIFEST.json",
        manifest,
    )
    root_docs = root_units(manifest)
    trust_docs = [trust_unit(manifest)]
    relation_doc = build_relations(manifest)
    attach_relation_ids(root_docs + trust_docs, relation_doc)
    source_map = build_source_map(manifest)
    write_json(
        "registry/units/graph-theory/flows/PORT_SOURCE_DISPOSITION_CLOSEOUT_ROOT_LIFT_UNITS.json",
        {
            "schema_version": "1.0.0",
            "batch_id": "PORT-SOURCE-DISPOSITION-CLOSEOUT",
            "units": root_docs,
        },
    )
    write_json(
        "registry/units/analytic-number-theory/prime-distribution/PORT_SOURCE_DISPOSITION_CLOSEOUT_TRUST_UNITS.json",
        {
            "schema_version": "1.0.0",
            "batch_id": "PORT-SOURCE-DISPOSITION-CLOSEOUT",
            "units": trust_docs,
        },
    )
    write_json(
        "registry/relations/PORT_SOURCE_DISPOSITION_CLOSEOUT_RELATIONS.json",
        relation_doc,
    )
    write_json(
        "migration/source-to-unit-map/PORT_SOURCE_DISPOSITION_CLOSEOUT_MAP.json",
        source_map,
    )
    update_views(ROOT_IDS)
    build_prose(root_docs)
    counts = manifest["summary"]
    map_counts = source_map["counts"]
    write(
        "migration/no-loss-audits/PORT_SOURCE_DISPOSITION_CLOSEOUT_STATE.md",
        f"""# Portfolio source-disposition closeout

**State:** fixed closeout candidate; ready for independent audit

**Authority:** `Yuren-Tang/research-workbench#15@5081149903`

**Canonical base:** `mathematics:main@ce577e23ea9b2493cd912af8c1335b67e8ddebec`

The final migration batch covers ten retained exact refs.  The machine
manifest fixes all ten commit/tree identities, {counts['full_tree_items']}
recursive tree/blob items, and {counts['source_scope_items']} authored source
scope items.  All {map_counts['source_scope_items_classified']} source-scope
items have one exact disposition; `unclassified=0`.

The additive corpus delta consists of 23 bounded authorial root-lift
theorem/scope units and one E306 pushlinter structural trust-boundary unit.
Root-lift preserves the full-witness counterexample, false-claim corrections,
q=5/q=8 one-way hierarchies, open lift/vanishing questions, inherited OR1
assurance, and literature/novelty limits.  The released E306 formal boundary is
corrected to exact Rosser–Schoenfeld `rosser_schoenfeld_cor3` /
`rosser_schoenfeld_thm5`; pushlinter is a separate conditional PNT/Mertens
scope with two structural axioms and provider/small-scale gaps.

Reverse provenance closes through the item map.  Negative, false, open,
superseded and pre-repair source material remains recoverable at source
strength.  Paper material is projection/source mapping only.

No ref is deletion-safe.  This candidate does not move `main`, independently
accept a theorem, start research or formalization, copy manuscript TeX, or
authorize release, submission, DOI, or publication action.
""",
    )


if __name__ == "__main__":
    main()
