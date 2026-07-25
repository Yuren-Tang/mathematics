#!/usr/bin/env python3
"""Build the additive E307 adjacent natural-mathematics intake."""

from __future__ import annotations

import json
import os
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE_GIT = Path(os.environ.get("E307_SOURCE_GIT_DIR", "/private/tmp/erdos-306-e307-source.git"))
CONTENT = "6e2352eeccec3686e9c167cf2cd6c47c152e5560"
CLASSIFICATION = "9bbcfae8360bce0871522e295f9aca903f64c780"
BATCH = "E307-ADJACENT-CANONICAL-INTAKE"
MAP_PATH = ROOT / "migration/source-to-unit-map/E307_ADJACENT_CANONICAL_INTAKE_MAP.json"


def git(*args: str) -> str:
    return subprocess.run(
        ["git", f"--git-dir={SOURCE_GIT}", *args],
        text=True, capture_output=True, check=True,
    ).stdout


def write(path: str, text: str) -> None:
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text.rstrip() + "\n", encoding="utf-8")


def write_json(path: str, value: object) -> None:
    write(path, json.dumps(value, indent=2, sort_keys=False))


def locator(commit: str, path: str, role: str = "development") -> dict:
    blob = git("rev-parse", f"{commit}:{path}").strip()
    payload = git("cat-file", "-p", blob)
    lines = max(1, len(payload.splitlines()))
    return {
        "repository": "Yuren-Tang/erdos-306",
        "commit": commit,
        "path": path,
        "blob": blob,
        "anchor": f"L1-L{lines}",
        "role": role,
    }


adjacent = [
    line for line in git(
        "ls-tree", "-r", "--name-only", CONTENT, "--", "research/adjacent-problems"
    ).splitlines() if line
]
addenda = [
    "research/PROGRAMME_STATE_ADDENDUM_2026-07-23_E307_JET_PORT_AND_DIVISOR_REDUCTION.md",
    "research/PROGRAMME_STATE_ADDENDUM_2026-07-23_E307_PORT_SONDOW_NORM_SYNTHESIS.md",
    "research/PROGRAMME_STATE_ADDENDUM_2026-07-23_E307_REBOUND_BLOCK_CODE_AND_DEFECT_SPECTRUM.md",
]
paths = adjacent + addenda
assert len(adjacent) == 35 and len(paths) == 38 and len(set(paths)) == 38
class_path = "research/E306_RL_BOUNDED_CURATION_HANDOFF_2026-07-24.md"
existing_map = (
    json.loads(MAP_PATH.read_text(encoding="utf-8"))
    if MAP_PATH.exists() else {}
)
existing_by_path = {
    item["source_item"]: item["source_locator"]
    for item in existing_map.get("items", [])
}
CLASS_LOC = existing_map.get("classification_authority")
if CLASS_LOC is None:
    CLASS_LOC = locator(CLASSIFICATION, class_path, "curation")

P = "math.number-theory.arithmetic-derivatives."
H = "math.harmonic-analysis.finite-fourier."
Q = "math.number-theory.reciprocal-representations."
C = "math.combinatorics.finite-configurations."
U = {
    "problem": P+"erdos-307-existence-problem",
    "bado": P+"bado-squarefree-two-cycle-framework",
    "syndrome": P+"mutual-reciprocal-syndrome-and-union-constraints",
    "defect": P+"bilateral-defect-semigroup",
    "anti": P+"bilateral-anti-inheritance-and-terminal-port",
    "coeff": P+"prime-symbol-shift-divided-power-coefficients",
    "jettransfer": P+"semiprime-jet-transfer-and-port-involution",
    "realmod": P+"real-modular-deficit-determinant",
    "divisorport": P+"seeded-divisor-cubic-reduction",
    "residual": P+"residual-c-port-calculus",
    "wang": P+"wang-port-framework-antecedent",
    "pencil": P+"residual-port-pencils-and-block-quadratic",
    "closure": P+"block-first-two-prime-closure",
    "fourier": H+"divisor-residue-fourier-calculus",
    "split": P+"moving-quadratic-splitting-character-obstruction",
    "norm": P+"primitive-quadratic-norm-split-factor-geometry",
    "sondow": P+"paired-mu-sondow-diagonal",
    "direct": P+"direct-core30-rebound-counterexample",
    "relaycounter": P+"giuga-relay-rebound-counterexample",
    "contraction": P+"two-step-contraction-claim",
    "core30": P+"core30-residual900-port",
    "giugaport": P+"giuga-core-residual-square-port",
    "support": C+"e307-minimal-support-bounds",
    "relays": P+"positive-defect-minimal-support-relays",
    "blockcode": C+"defect-block-code-and-complement-jet",
    "lowswap": C+"defect-exchange-low-swap-rigidity",
    "spectrum": P+"defect-spectrum-and-intermediate-ladder",
    "natural66": P+"natural66-bounded-terminal-exclusion",
    "jetvalid": H+"normalized-prime-jet-valid-facets",
    "jetblocked": H+"normalized-prime-jet-flatness-transference-block",
    "phase": H+"prime-inverse-phase-provider-gap",
    "joint": H+"joint-finite-archimedean-local-limit-gap",
    "nonambient": P+"nonambient-e313-transfer-filter",
    "literature": P+"bounded-literature-attribution-facet",
    "mine": Q+"adjacent-unit-fraction-neighbourhood-mine",
    "chronology": P+"superseded-chronology-and-failed-routes",
}

R = {
    "ERDOS_307_AMBIENT_E313_COLLAPSE_AND_NONAMBIENT_TRANSFER_V1.md": ["nonambient", "wang", "problem"],
    "ERDOS_307_ARITHMETIC_DERIVATIVE_TWO_CYCLE_V1.md": ["bado", "syndrome", "chronology"],
    "ERDOS_307_BILATERAL_DEFECT_SEMIGROUP_V1.md": ["defect", "problem"],
    "ERDOS_307_BILATERAL_TERMINAL_PORT_AND_ANTI_INHERITANCE_V1.md": ["anti", "defect", "wang"],
    "ERDOS_307_BLOCK_FIRST_TWO_PRIME_CLOSURE_AND_EXACT_PENCIL_INTERSECTION_V1.md": ["closure", "pencil", "problem"],
    "ERDOS_307_COMPLEMENT_JET_CODE_AND_MEET_IN_THE_MIDDLE_V1.md": ["blockcode", "phase", "problem"],
    "ERDOS_307_CORE1722_MINIMAL_SUPPORT_RELAY_V1.md": ["support", "relays", "problem"],
    "ERDOS_307_CORE1722_NEAR_ZERO_MINIMAL_RELAY_REFINEMENT_V1.md": ["relays", "support", "problem"],
    "ERDOS_307_CORE30_RESIDUAL_900_PORT_AND_ZERO_DEFECT_V1.md": ["core30", "problem"],
    "ERDOS_307_CORE30_SUPPORT_70_AND_MINIMAL_SIGN_CROSSING_V1.md": ["support", "relays", "core30"],
    "ERDOS_307_CORE858_MINIMAL_SUPPORT_RELAY_V1.md": ["support", "relays", "problem"],
    "ERDOS_307_DEFECT900_STANDARDIZATION_AND_NO_ONE_PRIME_INHERITANCE_V1.md": ["core30", "anti", "problem"],
    "ERDOS_307_DEFECT_BLOCK_SYNDROME_GLUING_AND_HYBRID_TRANSFERENCE_V1.md": ["blockcode", "core30", "problem"],
    "ERDOS_307_DEFECT_EXCHANGE_DETERMINANT_AND_LOW_SWAP_RIGIDITY_V1.md": ["lowswap", "blockcode"],
    "ERDOS_307_DEFECT_SPECTRUM_AND_INTERMEDIATE_SONDOW_LADDER_V1.md": ["spectrum", "sondow", "problem"],
    "ERDOS_307_DIRECT_GIUGA_CORE_REBOUND_AND_TWO_LINEAR_FORMS_V1.md": ["direct", "contraction", "problem"],
    "ERDOS_307_DIVISOR_RESIDUE_FOURIER_AND_QUADRATIC_OBSTRUCTION_V1.md": ["fourier", "split", "problem"],
    "ERDOS_307_GENERAL_GIUGA_CORE_RESIDUAL_SQUARE_PORT_V1.md": ["giugaport", "support", "problem"],
    "ERDOS_307_GENERAL_RESIDUAL_PORT_TRANSFER_AND_AUTOMATIC_OUTPUT_V1.md": ["residual", "wang", "problem"],
    "ERDOS_307_GIUGA_CORE_RELAY_AND_TWO_STEP_CONTRACTION_COUNTEREXAMPLE_V1.md": ["relaycounter", "contraction", "relays"],
    "ERDOS_307_LITERATURE_ATTRIBUTION_CORRECTION_AND_BADO_INTERFACE_V1.md": ["literature", "bado", "wang"],
    "ERDOS_307_LOCAL_PORT_ORBITS_AND_CRT_DENSITY_V1.md": ["residual", "phase", "problem"],
    "ERDOS_307_MOVING_GENUS_CHARACTER_OBSTRUCTION_V1.md": ["split", "problem"],
    "ERDOS_307_NATURAL_66_CORE_COMPLETE_ONE_REPLACEMENT_EXCLUSION_V1.md": ["natural66", "support", "problem"],
    "ERDOS_307_NORMALIZED_JET_GROUP_AND_TARGET_GRAPH_FOURIER_TRANSFERENCE_V1.md": ["jetvalid", "jetblocked", "phase", "joint"],
    "ERDOS_307_PAIRED_MU_SONDOW_DIAGONAL_V1.md": ["sondow", "problem"],
    "ERDOS_307_PRIMITIVE_NORM_AND_SPLIT_FACTOR_GEOMETRY_V1.md": ["norm", "split", "problem"],
    "ERDOS_307_REAL_MODULAR_PORT_GEOMETRY_AND_DEFICIT_DETERMINANT_V1.md": ["realmod", "problem"],
    "ERDOS_307_RESIDUAL_PORT_PENCILS_BLOCK_QUADRATIC_AND_DEFECT_BRIDGE_V1.md": ["pencil", "residual", "wang"],
    "ERDOS_307_RETURN_DEFECT_STRATIFICATION_AND_TWO_STEP_CONTRACTION_FRONTIER_V1.md": ["contraction", "direct", "relaycounter", "chronology"],
    "ERDOS_307_SEEDED_DIVISOR_PORT_FACTORIZATION_V1.md": ["divisorport", "norm", "problem"],
    "ERDOS_307_SEEDED_SCALAR_PORT_COMPOSITION_V1.md": ["residual", "wang", "problem"],
    "ERDOS_307_SEMIPRIME_JET_TRANSFER_AND_MOBIUS_PORT_INVOLUTION_V1.md": ["jettransfer", "realmod", "problem"],
    "PRIME_SHIFT_HASSE_RECIPROCAL_HYPERGRAPH_CALCULUS_V1.md": ["coeff", "chronology", "problem"],
    "UNIT_FRACTION_NEIGHBOURHOOD_MINE_MAP_304_313_V1.md": ["mine", "problem"],
    "PROGRAMME_STATE_ADDENDUM_2026-07-23_E307_JET_PORT_AND_DIVISOR_REDUCTION.md": ["chronology", "jettransfer", "divisorport"],
    "PROGRAMME_STATE_ADDENDUM_2026-07-23_E307_PORT_SONDOW_NORM_SYNTHESIS.md": ["chronology", "residual", "sondow", "norm"],
    "PROGRAMME_STATE_ADDENDUM_2026-07-23_E307_REBOUND_BLOCK_CODE_AND_DEFECT_SPECTRUM.md": ["chronology", "direct", "relaycounter", "blockcode", "spectrum"],
}
assert set(R) == {Path(path).name for path in paths}

items = []
locators = {}
for index, path in enumerate(paths, 1):
    loc = existing_by_path.get(path) or locator(CONTENT, path)
    locators[Path(path).name] = loc
    basename = Path(path).name
    disposition = "mapped-to-natural-units"
    supersession = None
    if basename == "ERDOS_307_ARITHMETIC_DERIVATIVE_TWO_CYCLE_V1.md":
        disposition = "retained-superseded-source"
        supersession = "Two-cycle identity retained; novelty attribution superseded by the Bado interface."
    elif basename == "ERDOS_307_RETURN_DEFECT_STRATIFICATION_AND_TWO_STEP_CONTRACTION_FRONTIER_V1.md":
        disposition = "retained-corrected-source"
        supersession = "Contraction conjecture retracted; exact defect identity and counterexample boundary retained."
    elif basename.startswith("PROGRAMME_STATE_ADDENDUM_"):
        disposition = "retained-chronology"
        supersession = "Chronological summary only; natural units and current frontier view control navigation."
    items.append({
        "item_id": f"e307-{index:03d}",
        "source_id": "e307-adjacent-content",
        "source_item": path,
        "source_locator": loc,
        "disposition": disposition,
        "units": [U[key] for key in R[basename]],
        **({"supersession": supersession} if supersession else {}),
    })

write_json("migration/source-to-unit-map/E307_ADJACENT_CANONICAL_INTAKE_MAP.json", {
    "schema_version": "1.0.0",
    "batch_id": BATCH,
    "classification_authority": CLASS_LOC,
    "counts": {
        "source_packets_total": 2,
        "substantive_items_total": 38,
        "substantive_items_classified": 38,
        "substantive_items_unclassified": 0,
        "canonical_units_referenced": len(U),
    },
    "items": items,
})

write_json("sources/manifests/E307_ADJACENT_CANONICAL_INTAKE_SOURCE_MANIFEST.json", {
    "schema_version": "1.0.0",
    "batch_id": BATCH,
    "state": "fixed-candidate",
    "authority": {
        "control": "Yuren-Tang/research-workbench#15 comment 5080997896",
        "writer": "MATH-CUR::local:/root/e307_curator_intake",
        "branch": "curation/erdos-307-adjacent-v1",
        "base": "b047efd5f43386f71dd9d2af1c9d5d531bd03163",
    },
    "policy": {
        "mode": "additive-reversible", "wholesale_merge": False,
        "main_movement": False, "source_repo_mutation": False,
        "epistemic_upgrade": False, "e307_solved_claim": False,
        "literature_facet": "bounded-attribution-and-terminology-only",
    },
    "sources": [
        {
            "source_id": "e307-adjacent-content", "repository": "Yuren-Tang/erdos-306",
            "ref": "research/e306-frontier-v1", "commit": CONTENT, "role": "development",
            "frozen": True, "roots": ["research/adjacent-problems", *addenda],
            "itemization_status": "complete", "substantive_item_count": 38,
            "classification_file": str(MAP_PATH.relative_to(ROOT)),
        },
        {
            "source_id": "e307-rl-classification", "repository": "Yuren-Tang/erdos-306",
            "ref": "research/e306-frontier-v1", "commit": CLASSIFICATION, "role": "curation",
            "frozen": True, "roots": [class_path], "itemization_status": "classification-authority",
            "substantive_item_count": 0, "classification_file": str(MAP_PATH.relative_to(ROOT)),
        },
    ],
    "summary": {
        "source_packets": 2, "substantive_items": 38,
        "classified_items": 38, "unclassified_items": 0,
    },
})


def ploc(fragment: str, role: str = "origin") -> dict:
    matches = [item["source_locator"] for item in items if fragment in item["source_item"]]
    if len(matches) != 1:
        adjacent_matches = [
            value for value in matches if value["path"].startswith("research/adjacent-problems/")
        ]
        if len(adjacent_matches) == 1:
            matches = adjacent_matches
    assert len(matches) == 1, (fragment, len(matches))
    value = dict(matches[0])
    value["role"] = role
    return value


def ev(kind: str, effect: str, scope: str, provenance: dict, notes=None) -> dict:
    value = {"kind": kind, "effect": effect, "scope": scope, "provenance": provenance}
    if notes:
        value["notes"] = notes
    return value


specs = {
    "problem": ("Erdős 307 existence problem", "Existence of disjoint finite prime sets whose reciprocal sums multiply to one; equivalently, existence of a coprime squarefree arithmetic-derivative two-cycle.", "problem", "formulated", "open", "dormant", "ARITHMETIC_DERIVATIVE_TWO_CYCLE", "authorial-argument", "inconclusive"),
    "bado": ("Bado squarefree two-cycle framework", "The exact forcing/two-cycle identity and union-character/discriminant framework are prior art and must be attributed to Bado.", "connection", "assessed", "scope-split", "integrated", "LITERATURE_ATTRIBUTION", "literature-check", "qualify"),
    "syndrome": ("Mutual reciprocal syndromes and union constraints", "Cross-side reciprocal zero-sum, valuation, parity, union discriminant and union-character conditions necessary for a squarefree two-cycle.", "theorem", "author-complete", "supported", "ready-for-review", "LITERATURE_ATTRIBUTION", "authorial-argument", "support"),
    "defect": ("Bilateral defect semigroup", "Coupled arithmetic-derivative defect coordinates, update law and semigroup composition for partial E307 fillers.", "method", "author-complete", "supported", "ready-for-review", "BILATERAL_DEFECT_SEMIGROUP", "authorial-argument", "support"),
    "anti": ("Bilateral anti-inheritance and terminal port", "Closed cycles cannot be enlarged by naïve inheritance; exact terminal formulas expose the coupled completion boundary.", "theorem", "author-complete", "supported", "ready-for-review", "BILATERAL_TERMINAL", "authorial-argument", "support"),
    "coeff": ("Prime-symbol shift divided-power coefficients", "A prime-symbol shift generating series has Hasse-Schmidt-type multiplicative coefficients organizing reciprocal graph and hypergraph sums; it is not an iterated arithmetic derivative.", "method", "author-complete", "scope-split", "ready-for-review", "PRIME_SHIFT_HASSE", "authorial-argument", "qualify"),
    "jettransfer": ("Semiprime jet transfer and port involution", "Rational jet transfer, its inverse matrix, discriminant test and square-modulus Möbius port involution reduce local semiprime closure.", "method", "author-complete", "supported", "ready-for-review", "SEMIPRIME_JET_TRANSFER", "authorial-argument", "support"),
    "realmod": ("Real-modular deficit determinant", "One determinant controls the real completion threshold, modular partner class and derivative-transfer height.", "theorem", "author-complete", "supported", "ready-for-review", "REAL_MODULAR_PORT", "authorial-argument", "support"),
    "divisorport": ("Seeded divisor cubic reduction", "A seeded four-prime completion reduces to restricted complementary divisors of one arithmetic-derivative cubic, followed by prime-value tests.", "method", "author-complete", "supported", "ready-for-review", "SEEDED_DIVISOR", "authorial-argument", "support"),
    "residual": ("Residual-C port calculus", "Seeded E307 completion specializes/generalizes one-sided port filling to prescribed residual C, with composition and terminal formulas but unresolved global providers.", "method", "author-complete", "supported", "ready-for-review", "SEEDED_SCALAR", "authorial-argument", "support"),
    "wang": ("Wang port-framework antecedent", "Wang's one-sided primary-pseudoperfect port-filling framework is an antecedent; E307 residual-C and bilateral forms must be described as specializations/generalizations.", "connection", "assessed", "scope-split", "integrated", "GENERAL_RESIDUAL_PORT", "literature-check", "qualify"),
    "pencil": ("Residual-port pencils and block quadratic", "Residual-one blocks generate residual-C affine pencils, while block-first coordinates give a seed quadratic and exact primitivity law.", "construction", "author-complete", "supported", "ready-for-review", "RESIDUAL_PORT_PENCILS", "authorial-argument", "support"),
    "closure": ("Block-first two-prime closure", "Given one full side and a partial opposite product, divisibility gates and one quadratic recover the two missing prime candidates.", "theorem", "author-complete", "supported", "ready-for-review", "BLOCK_FIRST", "authorial-argument", "support"),
    "fourier": ("Divisor-residue Fourier calculus", "Finite group algebra and character inversion count complementary divisor orientations and isolate exact support obstructions.", "method", "author-complete", "supported", "ready-for-review", "DIVISOR_RESIDUE_FOURIER", "authorial-argument", "support"),
    "split": ("Moving quadratic splitting-character obstruction", "A moving quadratic character gives a factorization-free necessary splitting certificate for target divisors; the traditional moving-genus label is not used.", "obstruction", "author-complete", "supported", "ready-for-review", "MOVING_GENUS", "authorial-argument", "support"),
    "norm": ("Primitive quadratic norm and split-factor geometry", "The seeded cubic value is a primitive quadratic norm whose odd prime factors obey a moving splitting law; target orientation remains open.", "theorem", "author-complete", "scope-split", "ready-for-review", "PRIMITIVE_NORM", "authorial-argument", "qualify"),
    "sondow": ("Paired mu-Sondow diagonal", "E307 is a primitive paired quotient-one plus/minus-h Sondow diagonal, but existence of a paired diagonal remains open.", "theorem", "author-complete", "scope-split", "ready-for-review", "PAIRED_MU", "authorial-argument", "qualify"),
    "direct": ("Direct core-30 rebound counterexample", "An exact 60-prime descending block yields a squarefree rebound and refutes two-step contraction in its stated scope.", "counterexample", "assessed", "established-in-scope", "integrated", "DIRECT_GIUGA", "independent-reproduction", "refute"),
    "relaycounter": ("Giuga-relay rebound counterexample", "A three-arrow squarefree Giuga-core relay returns and overshoots, independently refuting the proposed contraction mechanism.", "counterexample", "assessed", "established-in-scope", "integrated", "GIUGA_CORE_RELAY", "independent-reproduction", "refute"),
    "contraction": ("Two-step contraction claim", "The proposed weak two-step contraction principle is false; both exact rebound constructions are retained as scoped refutations.", "claim", "assessed", "refuted-in-scope", "closed", "RETURN_DEFECT", "authorial-argument", "refute"),
    "core30": ("Core-30 residual-900 port", "The core-30 E307 specialization is an exact defect-900/residual-900 filling with an affine prime output; exact filling remains open.", "problem", "formulated", "open", "dormant", "CORE30_RESIDUAL", "authorial-argument", "inconclusive"),
    "giugaport": ("Giuga-core residual-square port", "Every quotient-one Giuga core gives a residual-square E307 port and support screen, without providing exact closure.", "method", "author-complete", "supported", "ready-for-review", "GENERAL_GIUGA", "authorial-argument", "support"),
    "support": ("E307 minimal-support bounds", "Exact reciprocal-mass certificates and parity give core-dependent support lower bounds; they do not prove nonexistence.", "theorem", "author-complete", "supported", "ready-for-review", "CORE30_SUPPORT", "authorial-argument", "support"),
    "relays": ("Positive-defect minimal-support relays", "Explicit core-30, core-858 and core-1722 prime reservoirs attain minimal support or near-zero positive return, but not exact zero.", "construction", "tested", "supported", "ready-for-review", "CORE1722_NEAR", "computation", "support"),
    "blockcode": ("Defect block code and complement jet", "Exact product/derivative syndromes permit distant block gluing and balanced meet-in-the-middle search; implementation and exact closure are open.", "method", "author-complete", "supported", "ready-for-review", "DEFECT_BLOCK", "authorial-argument", "support"),
    "lowswap": ("Defect exchange and low-swap rigidity", "An exact exchange determinant and bounded checks show that local low-Hamming repairs cannot close the studied relay families.", "obstruction", "tested", "established-in-scope", "integrated", "DEFECT_EXCHANGE", "computation", "support"),
    "spectrum": ("Defect spectrum and intermediate Sondow ladder", "Defect layers and moving Sondow parameters organize a ladder of near-cycles and exact-zero targets.", "concept", "author-complete", "supported", "ready-for-review", "DEFECT_SPECTRUM", "authorial-argument", "support"),
    "natural66": ("Natural-66 bounded terminal exclusion", "Exactly 66 terminal windows and 14,675 integer q values were independently reproduced with zero integral terminal pairs; this is not a general exclusion.", "computation", "assessed", "established-in-scope", "integrated", "NATURAL_66", "independent-reproduction", "support"),
    "jetvalid": ("Normalized prime-jet valid facets", "The normalized-jet homomorphism, complement inverse graph and the correctly scoped Gauss-sum cases survive the source defect.", "method", "assessed", "scope-split", "ready-for-review", "NORMALIZED_JET", "authorial-argument", "qualify"),
    "jetblocked": ("Normalized prime-jet flatness/transference block", "At k=0 with chi_l trivial and chi_H nontrivial the coefficient is l-1, not at most sqrt(l); all-nontrivial flatness, Theorem 7.1 and criterion 7.4 are NOT ESTABLISHED.", "claim", "assessed", "refuted-in-scope", "blocked", "NORMALIZED_JET", "authorial-argument", "refute"),
    "phase": ("Prime inverse-phase provider gap", "No spectral provider currently controls the moving-modulus mixed multiplicative/inverse-additive prime phases needed for target hitting.", "question", "formulated", "open", "blocked", "NORMALIZED_JET", "authorial-argument", "inconclusive"),
    "joint": ("Joint finite/Archimedean local-limit gap", "A valid provider must hit the finite inverse graph and an exact or terminally closable Archimedean residual window jointly.", "question", "formulated", "open", "blocked", "NORMALIZED_JET", "authorial-argument", "inconclusive"),
    "nonambient": ("Nonambient E313 transfer filter", "Direct ambient reuse collapses to consecutive-cycle structures; an E307 transfer must use nonambient pencil intersection.", "obstruction", "author-complete", "supported", "ready-for-review", "AMBIENT_E313", "authorial-argument", "support"),
    "literature": ("Bounded literature attribution facet", "Bado and Wang antecedents and corrected terminology are recorded; this facet does not establish comprehensive novelty, correctness or publication priority.", "connection", "assessed", "scope-split", "integrated", "LITERATURE_ATTRIBUTION", "literature-check", "qualify"),
    "mine": ("Adjacent unit-fraction neighbourhood mine", "A strategic map of E304-E313 connections and candidate consumers, retained as IDEA rather than theorem or scheduling authority.", "heuristic", "captured", "unassessed", "dormant", "UNIT_FRACTION", "authorial-argument", "inconclusive"),
    "chronology": ("Superseded chronology and failed routes", "Three programme addenda and corrected/retracted route summaries preserve development chronology without controlling present truth.", "connection", "assessed", "superseded", "closed", "PROGRAMME_STATE_ADDENDUM", "source-fidelity-check", "qualify"),
}
assert set(specs) == set(U)

units = []
for key, data in specs.items():
    title, summary, form, maturity, disposition, workflow, fragment, kind, effect = data
    provenance = CLASS_LOC if key == "chronology" else ploc(fragment)
    scope = summary
    notes = []
    if key == "direct":
        notes = ["Exact numeric construction only.", "Independent reproduction boundary is authorized by control comment 5080997896; provenance identifies the exact reproduced construction.", "Proposition 3.1 requires C even or separate l=2 parity admissibility; the core-30 instance is valid."]
    elif key == "relaycounter":
        notes = ["Exact numeric construction only; no family-level prime-production claim.", "Independent reproduction boundary is authorized by control comment 5080997896; provenance identifies the exact reproduced construction."]
    elif key == "natural66":
        notes = ["Bounded reproduction: 66 windows / 14,675 integer q values / 0 integral pairs.", "Independent reproduction boundary is authorized by control comment 5080997896; provenance identifies the exact reproduced diagnostic.", "No generalization beyond the enumerated scope."]
    elif key == "jetblocked":
        notes = ["Omitted frequency: k=0, chi_l=1, chi_H nontrivial; coefficient=l-1.", "No logical proof traversal through Theorem 5.1, Theorem 7.1 or criterion 7.4."]
    elif key in {"literature", "bado", "wang"}:
        notes = ["Bounded attribution/terminology facet only; not correctness, comprehensive novelty or publication-priority assurance."]
    assurance = [ev(kind, effect, scope, provenance, notes or None)]
    if key == "syndrome":
        assurance.append(ev(
            "literature-check", "qualify",
            "bounded attribution to the Bado union/syndrome framework only; not correctness assurance",
            provenance,
        ))
    units.append({
        "id": U[key], "title": title, "summary": summary, "form": form,
        "maturity": maturity,
        "assurance": assurance,
        "disposition": disposition, "workflow": workflow,
        "provenance": [provenance], "relations": [], "views": ["frontier.erdos-307"],
        **({"notes": notes} if notes else {}),
    })


def rel(rid, source, target, plane, typ, scope, fragment, status=None):
    value = {
        "id": "rel.e307."+rid, "source": U.get(source, source), "target": U.get(target, target),
        "plane": plane, "type": typ, "scope": scope,
        "status": status or ("curator-mapped" if plane == "logical" else "captured-unreviewed"),
        "provenance": [{k: v for k, v in ploc(fragment).items() if k != "role"}],
    }
    return value


logical_specs = [
    ("bado-qualifies-problem", "bado", "problem", "qualifies", "prior exact reformulation does not solve existence", "LITERATURE_ATTRIBUTION"),
    ("syndrome-depends-bado", "syndrome", "bado", "depends-on", "prior union and reciprocal constraints", "LITERATURE_ATTRIBUTION"),
    ("defect-uses-syndrome", "defect", "syndrome", "uses", "coupled defect coordinates", "BILATERAL_DEFECT_SEMIGROUP"),
    ("anti-uses-defect", "anti", "defect", "uses", "terminal and anti-inheritance calculations", "BILATERAL_TERMINAL"),
    ("coeff-qualifies-derivative", "coeff", "bado", "qualifies", "divided-power coefficients are not iterated arithmetic derivatives", "PRIME_SHIFT_HASSE"),
    ("jettransfer-uses-defect", "jettransfer", "defect", "uses", "local rational transfer", "SEMIPRIME_JET_TRANSFER"),
    ("realmod-generalizes-jet", "realmod", "jettransfer", "generalizes", "real/modular determinant facet", "REAL_MODULAR_PORT"),
    ("divisorport-specializes-jet", "divisorport", "jettransfer", "specializes", "seeded cubic reduction", "SEEDED_DIVISOR"),
    ("residual-generalizes-wang", "residual", "wang", "generalizes", "prescribed residual-C extension with bilateral output", "GENERAL_RESIDUAL_PORT"),
    ("residual-specializes-wang", "residual", "wang", "specializes", "one-sided port equation used inside E307", "GENERAL_RESIDUAL_PORT"),
    ("pencil-uses-residual", "pencil", "residual", "uses", "affine residual-C pencil", "RESIDUAL_PORT_PENCILS"),
    ("closure-uses-pencil", "closure", "pencil", "uses", "exact seed-curve/pencil intersection", "BLOCK_FIRST"),
    ("fourier-uses-syndrome", "fourier", "syndrome", "uses", "divisor orientation character count", "DIVISOR_RESIDUE_FOURIER"),
    ("split-specializes-fourier", "split", "fourier", "specializes", "quadratic splitting certificate", "MOVING_GENUS"),
    ("norm-uses-divisorport", "norm", "divisorport", "uses", "primitive norm interpretation", "PRIMITIVE_NORM"),
    ("split-qualifies-norm", "split", "norm", "qualifies", "necessary factor orientation only", "MOVING_GENUS"),
    ("sondow-qualifies-problem", "sondow", "problem", "qualifies", "paired diagonal reformulation remains open", "PAIRED_MU"),
    ("direct-refutes-contraction", "direct", "contraction", "refutes", "exact direct rebound", "DIRECT_GIUGA"),
    ("relay-refutes-contraction", "relaycounter", "contraction", "refutes", "exact three-arrow relay rebound", "GIUGA_CORE_RELAY"),
    ("core30-specializes-problem", "core30", "problem", "specializes", "residual-900 existence slice", "CORE30_RESIDUAL"),
    ("giugaport-generalizes-core30", "giugaport", "core30", "generalizes", "quotient-one Giuga-core residual-square family", "GENERAL_GIUGA"),
    ("support-qualifies-core30", "support", "core30", "qualifies", "support lower bound, not nonexistence", "CORE30_SUPPORT"),
    ("relays-use-support", "relays", "support", "uses", "minimal-support positive-return reservoirs", "CORE1722_MINIMAL"),
    ("blockcode-uses-core30", "blockcode", "core30", "uses", "defect/product syndrome gluing", "DEFECT_BLOCK"),
    ("lowswap-qualifies-blockcode", "lowswap", "blockcode", "qualifies", "local repairs blocked only in checked families", "DEFECT_EXCHANGE"),
    ("spectrum-generalizes-core30", "spectrum", "core30", "generalizes", "moving defect layers", "DEFECT_SPECTRUM"),
    ("natural66-qualifies-support", "natural66", "support", "qualifies", "bounded diagnostic only", "NATURAL_66"),
    ("jetvalid-uses-blockcode", "jetvalid", "blockcode", "uses", "valid normalized homomorphism and inverse target graph", "NORMALIZED_JET"),
    ("jetblocked-qualifies-jetvalid", "jetblocked", "jetvalid", "qualifies", "flatness/transference is blocked but local facets survive", "NORMALIZED_JET"),
    ("phase-depends-jetvalid", "phase", "jetvalid", "depends-on", "moving prime inverse-phase estimate", "NORMALIZED_JET"),
    ("joint-depends-phase", "joint", "phase", "depends-on", "finite target plus Archimedean closure", "NORMALIZED_JET"),
    ("nonambient-qualifies-pencil", "nonambient", "pencil", "qualifies", "ambient reuse collapses", "AMBIENT_E313"),
    ("literature-qualifies-bado", "literature", "bado", "qualifies", "bounded audit facet", "LITERATURE_ATTRIBUTION"),
    ("literature-qualifies-wang", "literature", "wang", "qualifies", "bounded antecedent facet", "LITERATURE_ATTRIBUTION"),
    ("chronology-superseded-bado", "bado", "chronology", "supersedes", "novelty label corrected", "LITERATURE_ATTRIBUTION"),
]
logical = [rel(r, s, t, "logical", ty, sc, f) for r, s, t, ty, sc, f in logical_specs]
discovery_specs = [
    ("e306-suggests-e307", Q+"squarefree-semiprime-characterization", "problem", "suggests", "adjacent question only; no proof transfer", "UNIT_FRACTION"),
    ("mine-motivates-problem", "mine", "problem", "motivates", "strategic neighbourhood map", "UNIT_FRACTION"),
    ("relays-suggest-blockcode", "relays", "blockcode", "suggests", "prime reservoirs for distant collision search", "CORE1722_NEAR"),
    ("spectrum-suggests-joint", "spectrum", "joint", "suggests", "defect layers as Archimedean coordinate", "DEFECT_SPECTRUM"),
    ("norm-suggests-split", "norm", "split", "suggests", "moving-family factor orientation", "PRIMITIVE_NORM"),
    ("counter-suggests-core30", "direct", "core30", "suggests", "sign flexibility redirects search to exact zero", "DIRECT_GIUGA"),
    ("pencil-suggests-nonambient", "pencil", "nonambient", "suggests", "nonambient intersection search", "AMBIENT_E313"),
    ("coeff-analogous-jet", "coeff", "jetvalid", "analogous-to", "multiplicative coefficient and normalized-jet packages", "PRIME_SHIFT_HASSE"),
]
discovery = [rel(r, s, t, "discovery", ty, sc, f) for r, s, t, ty, sc, f in discovery_specs]
by_id = {unit["id"]: unit for unit in units}
for relation in logical + discovery:
    for endpoint in (relation["source"], relation["target"]):
        if endpoint in by_id:
            by_id[endpoint]["relations"].append(relation["id"])

write_json("registry/units/number-theory/arithmetic-derivatives/E307_ADJACENT_CANONICAL_INTAKE_UNITS.json", {
    "schema_version": "1.1.0", "batch_id": BATCH,
    "item_schema": "registry/schema/mathematical-unit.schema.json", "units": units,
})
write_json("registry/relations/E307_ADJACENT_CANONICAL_INTAKE_RELATIONS.json", {
    "schema_version": "1.1.0", "batch_id": BATCH,
    "item_schema": "registry/schema/typed-relation.schema.json",
    "logical": logical, "discovery": discovery,
})
write_json("registry/views/frontier.erdos-307.json", {
    "view_id": "frontier.erdos-307", "title": "Erdős 307 adjacent frontier",
    "view_type": "frontier",
    "registry_source": "registry/units/number-theory/arithmetic-derivatives/E307_ADJACENT_CANONICAL_INTAKE_UNITS.json",
    "relation_source": "registry/relations/E307_ADJACENT_CANONICAL_INTAKE_RELATIONS.json",
    "compatibility_entrypoints": [
        "projects/erdos-307/README.md", "projects/erdos-307/FRONTIER_AND_ASSURANCE.md",
        "registry/assurance/E307_ADJACENT_ASSURANCE_AND_ATTRIBUTION_MAP.json",
        "math/number-theory/arithmetic-derivatives/e307-two-cycles-and-syndromes.md",
        "math/number-theory/arithmetic-derivatives/e307-ports-jets-and-closure.md",
        "math/number-theory/arithmetic-derivatives/e307-negative-knowledge-and-open-frontier.md",
    ],
    "sections": {
        "headline_open_problem": [U["problem"]],
        "prior_art_must_attribute": [U["bado"], U["syndrome"]],
        "authorial_mechanisms_novelty_unresolved": [
            U[k] for k in ("defect", "anti", "coeff", "jettransfer", "realmod", "divisorport",
                           "residual", "pencil", "closure", "fourier", "split", "norm", "sondow")
        ],
        "antecedent": [U["wang"]],
        "independently_reproduced_counterexamples": [U["direct"], U["relaycounter"]],
        "bounded_independently_reproduced_diagnostic": [U["natural66"]],
        "blocked_not_established": [U["jetblocked"]],
        "open_providers": [U["phase"], U["joint"]],
        "negative_and_finite_knowledge": [
            U[k] for k in ("contraction", "support", "relays", "blockcode", "lowswap", "spectrum")
        ],
        "idea_and_chronology": [U["mine"], U["chronology"]],
    },
    "status_statement": "OPEN / SEPARATE / NOT SOLVED / RESEARCH NOT LAUNCHED. Legacy separation remains OPEN / SEPARATE / NOT LAUNCHED. No E306 proof status transfers to E307.",
    "forbidden_traversal": [
        "The blocked normalized-jet Theorem 5.1 all-nontrivial flatness, Theorem 7.1 and criterion 7.4 cannot support a proof edge.",
        "Counterexamples refute two-step contraction only; they neither establish nor refute E307 existence.",
        "Bounded computation and literature facets do not establish the headline.",
    ],
    "remaining_gaps": [
        "existence or nonexistence",
        "repaired target-graph transference",
        "moving-modulus prime inverse-phase provider",
        "joint finite/Archimedean local limit",
        "exact residual closure",
        "affine/quadratic prime outputs",
    ],
    "nonduplication_rule": "This frontier view references natural units; it is not a project-owned mathematical ontology.",
})
write_json("registry/assurance/E307_ADJACENT_ASSURANCE_AND_ATTRIBUTION_MAP.json", {
    "schema_version": "1.0.0",
    "batch_id": BATCH,
    "registry_source": "registry/units/number-theory/arithmetic-derivatives/E307_ADJACENT_CANONICAL_INTAKE_UNITS.json",
    "control": "Yuren-Tang/research-workbench#15 comment 5080997896",
    "attribution": {
        "prior_art_must_attribute": [U["bado"], U["syndrome"]],
        "port_framework_antecedent": [U["wang"]],
        "terminology": {
            "moving_genus_replacement": "moving quadratic splitting-character obstruction",
            "hasse_replacement": "prime-symbol shift divided-power / Hasse-Schmidt-type multiplicative coefficients",
        },
        "mechanism_novelty": "unresolved",
        "literature_effect": "bounded attribution/terminology only; no correctness, comprehensive novelty, peer-review or publication-priority assurance",
    },
    "independent_reproduction": {
        "exact_numeric_counterexamples_only": [U["direct"], U["relaycounter"]],
        "bounded_diagnostic_only": {
            "unit": U["natural66"], "windows": 66, "integer_q_values": 14675,
            "integral_pairs": 0, "general_exclusion": False,
        },
    },
    "blocked": {
        "unit": U["jetblocked"],
        "omitted_frequency": "k=0, chi_l=1, chi_H nontrivial",
        "coefficient": "l-1",
        "not_established": ["Theorem 5.1 all-nontrivial flatness", "Theorem 7.1", "criterion 7.4"],
        "forbidden_as_logical_provider": True,
    },
    "open": {
        "headline": U["problem"],
        "prime_inverse_phase_provider": U["phase"],
        "joint_finite_archimedean_local_limit": U["joint"],
    },
})

write("math/number-theory/arithmetic-derivatives/e307-two-cycles-and-syndromes.md", """
# Squarefree arithmetic-derivative two-cycles and E307

Erdős 307 asks for disjoint finite prime sets whose reciprocal sums have product one.  In
squarefree product notation this is the open existence question

```text
D(X)=Y,  D(Y)=X,  gcd(X,Y)=1.
```

The exact forcing identity, two-cycle formulation, valuation and reciprocal-syndrome
conditions, union discriminant and union quadratic-character model are prior work of Idriss
Olivier Bado and must be attributed as such.  This corpus records an independent
reconstruction, not a novelty claim and not a solution.

The internally developed bilateral-defect semigroup, anti-inheritance formulas, paired
mu-Sondow diagonal and prime-symbol shift divided-power coefficients are status-honest
authorial mechanisms.  The last term denotes Hasse-Schmidt-type multiplicative
coefficients in a prime-symbol shift generating series; they are not iterated arithmetic
derivatives.  Their novelty remains unresolved.
""")
write("math/number-theory/arithmetic-derivatives/e307-ports-jets-and-closure.md", """
# Residual ports, arithmetic jets and quadratic closure

The E307 completion problem has several exact but presently incomplete coordinates:

- bilateral defects and rational semiprime jet transfer;
- a real-modular deficit determinant and Möbius port involution;
- seeded reduction to restricted divisors of one arithmetic-derivative cubic;
- residual-C port composition, affine pencils and block-first quadratic closure;
- divisor-residue Fourier inversion, primitive quadratic norms and a moving quadratic
  splitting-character obstruction.

Han Wang's one-sided primary-pseudoperfect port-filling framework is an antecedent.
The residual-C and bilateral E307 forms are specializations/generalizations of that
framework, not unqualified independent inventions.

Block-first closure removes a coordinate-induced final-output test but leaves correlated
divisibility, quadratic splitting and prime-output conditions.  Direct ambient E313 reuse
collapses to consecutive-cycle structures, so any transfer must use nonambient pencil
intersection.  None of these reductions supplies E307 existence.
""")
write("math/number-theory/arithmetic-derivatives/e307-negative-knowledge-and-open-frontier.md", """
# E307 negative knowledge, computations and open frontier

Two exact squarefree rebound constructions were independently reproduced in their numeric
scope.  They refute the proposed two-step contraction mechanism; they do not solve E307.
Core-dependent support certificates, positive-defect relays, low-swap rigidity and the
Natural-66 diagnostic are retained as scoped knowledge.  Natural-66 means exactly 66
terminal windows, 14,675 tested integer q values and zero integral terminal pairs; it has
no general exclusion force.

The normalized-jet source has a decisive omitted frequency:

```text
k=0, chi_l=1, chi_H nontrivial,
target coefficient = l-1.
```

Consequently its claimed all-nontrivial square-root flatness (Theorem 5.1), Theorem 7.1
and criterion 7.4 are **BLOCKED / NOT ESTABLISHED** and cannot be traversed as proof.
The normalized-jet homomorphism, complement inverse graph and the other correctly scoped
Gauss-sum cases remain useful facets.

E307 is **OPEN / SEPARATE / NOT SOLVED**.  Remaining gates include existence or
nonexistence, repaired target-graph transference, a moving-modulus prime inverse-phase
provider, a joint finite/Archimedean local limit, exact residual closure and correlated
affine/quadratic prime outputs.
""")
write("projects/erdos-307/README.md", """
# Erdős 307 frontier view

This is a compatibility/project view over stable natural units in
`registry/units/number-theory/arithmetic-derivatives/`.  It does not own the mathematics.

**Headline:** `OPEN / SEPARATE / NOT SOLVED`.

Read `registry/views/frontier.erdos-307.json` for the typed current view and
`FRONTIER_AND_ASSURANCE.md` for the assurance boundary.
""")
write("projects/erdos-307/FRONTIER_AND_ASSURANCE.md", """
# E307 frontier and assurance

- Bado's two-cycle and union-character framework is prior art and must be attributed.
- Wang's one-sided port-filling framework is an antecedent to residual-C and bilateral
  specializations/generalizations.
- Internally derived mechanisms are authorial and have unresolved novelty unless an exact
  evidence item says otherwise.
- The two rebound constructions are independently reproduced only in exact numeric scope.
- Natural-66 is independently reproduced only as `66 windows / 14,675 q / 0 integral pairs`.
- The normalized-jet all-frequency flatness/transference chain is blocked at the omitted
  `k=0, chi_l=1, chi_H nontrivial` frequency.
- Literature evidence here is bounded attribution/terminology only, not correctness,
  comprehensive novelty, peer review or publication priority.
""")
write("registry/discovery/E307_ADJACENT_CANONICAL_INTAKE_DISCOVERY_ADDENDUM.md", """
# E307 adjacent intake — discovery addendum

These low-strength links arose during no-loss organization and are not proof edges:

- minimal-support positive relays may be reservoirs for distant complement-jet collisions;
- defect spectra suggest an Archimedean coordinate for a future joint local limit;
- primitive norm values suggest moving splitting-character orientation filters;
- prime-symbol shift coefficients are analogous to, but not identical with, normalized
  arithmetic-jet packages;
- E306 suggests the adjacent E307 question only on the discovery plane.

Each observation remains `captured-unreviewed`; no research line is launched here.
""")
write("migration/no-loss-audits/E307_ADJACENT_CANONICAL_INTAKE_FINAL_VALIDATION.md", f"""
# E307 adjacent canonical intake — final validation packet

**Base:** `b047efd5f43386f71dd9d2af1c9d5d531bd03163`
**Source:** `Yuren-Tang/erdos-306@{CONTENT}`
**Classification:** `Yuren-Tang/erdos-306@{CLASSIFICATION}`
**Control:** `Yuren-Tang/research-workbench#15` comment `5080997896`

The generated source map classifies all 38 items with `unclassified=0`.  Every item has an
immutable repository/full-SHA/path/blob/anchor locator.  The registry has {len(U)} natural
units, {len(logical)} logical relations and {len(discovery)} discovery relations.

No source is silently lost and no assurance is upgraded.  Negative, failed, blocked,
counterexample, bounded-computation, superseded, chronology, IDEA and open-frontier
material remains visible.  E307 is `OPEN / SEPARATE / NOT SOLVED`.

The independent reception audit must recompute all locators and specifically retest the
normalized-jet forbidden traversal, direct-rebound parity qualification, bounded
Natural-66 reproduction, attribution terminology and additive isolation.
""")

print(f"BUILT {BATCH}: items=38 units={len(U)} logical={len(logical)} discovery={len(discovery)}")
