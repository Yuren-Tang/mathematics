#!/usr/bin/env python3
"""Build the E306 natural-unit registry, typed relations, views, and prose entrypoints."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MAP_PATH = ROOT / "migration/source-to-unit-map/E306_CUR_CANONICAL_INTAKE_MAP.json"
ITEMS = json.loads(MAP_PATH.read_text())["items"]
BATCH = "E306-CUR-CANONICAL-INTAKE"


def write(path: str, text: str) -> None:
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text.rstrip() + "\n")


def write_json(path: str, value: object) -> None:
    write(path, json.dumps(value, indent=2, sort_keys=False))


def locator(source_id: str, fragment: str, role: str | None = None) -> dict:
    matches = [
        item for item in ITEMS
        if item["source_id"] == source_id and fragment in item["source_item"]
    ]
    if len(matches) != 1:
        raise ValueError(f"locator {source_id=} {fragment=} matched {len(matches)}")
    result = dict(matches[0]["source_locator"])
    if role is not None:
        result["role"] = role
    return result


def evidence(kind: str, effect: str, scope: str, loc: dict, notes: list[str] | None = None) -> dict:
    value = {"kind": kind, "effect": effect, "scope": scope, "provenance": loc}
    if notes:
        value["notes"] = notes
    return value


P = {
    "release_readme": locator("e306-release-v0.0.3", "README.md", "formalization"),
    "formal_statement": locator("e306-release-v0.0.3", "Erdos306FormalConjectures.lean", "formalization"),
    "formal_audit": locator("e306-release-v0.0.3", "Audit.lean", "formalization"),
    "formal_inputs": locator("e306-release-v0.0.3", "RSPrimeSums.lean", "formalization"),
    "dense": locator("e306-dense-one-anchor", "ONE-ANCHOR-HUMAN-PROOF.md", "development"),
    "dense_ledger": locator("e306-dense-one-anchor", "ONE-ANCHOR-DEPENDENCY-AND-PARAMETER-LEDGER.md", "development"),
    "dense_review": locator("e306-dense-one-anchor-audit", "E306-OA-AUDIT-01-REPORT.md", "review"),
    "dense_gate": locator("e306-dense-one-anchor-audit", "E306-OA-AUDIT-01-CURATOR-GATE.md", "review"),
    "multi": locator("e306-multiblock-repaired", "PAPER-FIRST-HUMAN-PROOF.md", "development"),
    "multi_ledger": locator("e306-multiblock-repaired", "PAPER-FIRST-DEPENDENCY-AND-PARAMETER-LEDGER.md", "development"),
    "multi_review": locator("e306-multiblock-audit", "E306-PF-AUDIT-01-REPORT.md", "review"),
    "multi_repair": locator("e306-multiblock-repair-verification", "E306-PF-REPAIR-VERIFY-01-REPORT.md", "review"),
    "sparse": locator("e306-sparse-repaired", "SPARSE-ANCHOR-HUMAN-PROOF.md", "development"),
    "sparse_ledger": locator("e306-sparse-repaired", "SPARSE-ANCHOR-DEPENDENCY-AND-PARAMETER-LEDGER.md", "development"),
    "sparse_review": locator("e306-sparse-audit", "E306-SAS-AUDIT-01-REPORT.md", "review"),
    "sparse_repair": locator("e306-sparse-repair-verification", "E306-SAS-REPAIR-VERIFY-01-REPORT.md", "review"),
    "aft": locator("e306-aft-authorial", "ANCHOR-FIBRE-FOURIER-TRANSFERENCE.md", "development"),
    "weighted": locator("e306-aft-authorial", "WEIGHTED-DECODED-SKELETON-THEOREM.md", "development"),
    "observability": locator("e306-aft-authorial", "TARGET-SENSITIVITY-AS-OBSERVABILITY.md", "development"),
    "mass": locator("e306-aft-authorial", "COMPLETE-FAMILY-MASS-AND-HIGHER-UNIFORMITY.md", "development"),
    "aft_e306": locator("e306-aft-authorial", "E306-COROLLARY-MAP.md", "development"),
    "failures": locator("e306-aft-authorial", "PROVIDER-HYPOTHESES-AND-FAILURE-MODES.md", "development"),
    "publication": locator("e306-aft-authorial", "PUBLICATION-LEVEL-DECISION.md", "development"),
    "rl": locator("e306-rl-classification", "E306_RL_BOUNDED_CURATION_HANDOFF", "curation"),
    "old": locator("e306-old-curation-archival", "SOURCE_PROVENANCE_AND_SUPERSESSION.md", "superseded-source"),
}

DENSE_REVIEW = evidence(
    "independent-mathematical-review", "support",
    "the complete dense one-anchor E306 route, subject to the audit gate's exact range, branch, normalization, partition, decoder, error-sector, and parameter-order conditions",
    P["dense_review"],
)
MULTI_REVIEW = evidence(
    "independent-mathematical-review", "support",
    "the repaired multiblock E306 route, including the bounded size-range, R=0, class-sum, and empty-set wording repairs",
    P["multi_repair"],
)
SPARSE_REVIEW = evidence(
    "independent-mathematical-review", "support",
    "the repaired sparse actual-prime sensor route, including the exact cold-label range and decoder/error bookkeeping",
    P["sparse_repair"],
)

unit_defs = [
    ("math.number-theory.reciprocal-representations.squarefree-semiprime-characterization",
     "Squarefree-semiprime reciprocal characterization",
     "A positive rational in lowest terms is a finite sum of distinct reciprocals of squarefree semiprimes exactly when its denominator is squarefree.",
     "theorem", "assessed", "established-in-scope", "integrated", "dense", [DENSE_REVIEW]),
    ("math.number-theory.reciprocal-representations.squarefree-denominator-necessity",
     "Squarefree denominator necessity",
     "Any finite sum of reciprocals of squarefree integers has squarefree reduced denominator; this supplies the necessity direction.",
     "theorem", "assessed", "established-in-scope", "integrated", "dense", [DENSE_REVIEW]),
    ("math.number-theory.reciprocal-representations.avoiding-unit-reduction",
     "Avoiding-unit reduction",
     "The sufficiency problem is reduced to constructing a representation that avoids a prescribed finite set while respecting the numerator induction and the b=1,2 base reductions.",
     "method", "assessed", "established-in-scope", "integrated", "dense", [DENSE_REVIEW]),
    ("math.analytic-number-theory.prime-distribution.fixed-ratio-prime-supply",
     "Fixed-ratio prime supply",
     "The E306 routes use primes in fixed-ratio intervals and a target-prime auxiliary denominator supply as their analytic interface.",
     "method", "assessed", "established-in-scope", "integrated", "dense_ledger", [DENSE_REVIEW]),
    ("math.number-theory.reciprocal-representations.complete-pair-denominator-family",
     "Complete-pair denominator family",
     "A complete bipartite pair family between a prime block and the top block supplies squarefree-semiprime denominators and a full top partition.",
     "construction", "assessed", "established-in-scope", "integrated", "dense", [DENSE_REVIEW]),
    ("math.harmonic-analysis.finite-fourier.bernoulli-subset-selector",
     "Finite-Fourier Bernoulli subset selector",
     "A Fourier inversion over independently sampled denominator labels turns modular target selection into a main term plus controlled nontrivial characters.",
     "method", "assessed", "established-in-scope", "integrated", "dense", [DENSE_REVIEW]),
    ("math.combinatorics.finite-configurations.reciprocal-label-rigidity",
     "Reciprocal-label rigidity",
     "The reciprocal labels attached to the complete denominator family obey the exact rigidity and row-code separation needed by the decoder.",
     "theorem", "assessed", "established-in-scope", "integrated", "dense", [DENSE_REVIEW]),
    ("math.harmonic-analysis.finite-fourier.anchor-fibre-decoder-observability",
     "Anchor-fibre decoder observability",
     "Nontrivial characters are divided by whether a target-prime fibre is coherent, decoder-visible, or relegated to a separately bounded sector.",
     "method", "assessed", "established-in-scope", "integrated", "dense", [DENSE_REVIEW]),
    ("math.harmonic-analysis.finite-fourier.five-sector-positivity-budget",
     "Five-sector positivity budget",
     "The Fourier remainder is exhausted through five explicit character sectors, with no-wrap and positivity obtained after the prescribed constant-then-scale parameter order.",
     "proof", "assessed", "established-in-scope", "integrated", "dense", [DENSE_REVIEW]),
    ("math.number-theory.reciprocal-representations.dense-one-anchor-proof",
     "Dense one-anchor E306 proof",
     "The preferred human spine: one dense anchor family, complete top partition, reciprocal rigidity, target decoder, and five-sector Fourier positivity.",
     "proof", "assessed", "established-in-scope", "integrated", "dense", [DENSE_REVIEW]),
    ("math.number-theory.reciprocal-representations.multiblock-proof",
     "Repaired multiblock E306 proof",
     "An independently assured fallback using multiple control blocks, fingerprint entropy, propagation, global coding, and localization.",
     "proof", "assessed", "established-in-scope", "integrated", "multi", [MULTI_REVIEW]),
    ("math.combinatorics.finite-configurations.sparse-actual-prime-sensor-core",
     "Sparse actual-prime sensor core",
     "A sparse sample of actual prime labels, with exact cold-label cutoff and target decoder ranges, replaces the complete dense anchor family.",
     "construction", "assessed", "established-in-scope", "integrated", "sparse", [SPARSE_REVIEW]),
    ("math.number-theory.reciprocal-representations.sparse-sensor-proof",
     "Repaired sparse-sensor E306 proof",
     "An independently assured alternative whose hierarchy is cleaner but whose total analytic burden remains comparable to the dense route.",
     "proof", "assessed", "established-in-scope", "integrated", "sparse", [SPARSE_REVIEW]),
    ("math.harmonic-analysis.finite-fourier.weighted-decoded-skeleton",
     "Weighted decoded skeleton",
     "An authorial weighted Fourier skeleton separates complete-family mass, decoder visibility, higher uniformity, and positivity closure.",
     "method", "author-complete", "supported", "ready-for-review", "weighted", [
         evidence("authorial-argument", "support", "the stated weighted decoded skeleton only; no independent E306 assurance", P["weighted"])
     ]),
    ("math.harmonic-analysis.finite-fourier.anchor-fibre-transference",
     "Anchor-fibre Fourier transference",
     "An authorial general mechanism intended to transfer complete-family mass and fibre observability into a decoded Fourier positivity conclusion.",
     "method", "author-complete", "supported", "ready-for-review", "aft", [
         evidence("authorial-argument", "support", "the general AFT mechanism as written; not independently reviewed", P["aft"])
     ]),
    ("math.harmonic-analysis.finite-fourier.quantitative-target-observability",
     "Quantitative target observability",
     "An authorial interface quantifies when the target residue is visible through an anchor fibre and its decoder.",
     "concept", "author-complete", "supported", "ready-for-review", "observability", [
         evidence("authorial-argument", "support", "the observability interface as formulated", P["observability"])
     ]),
    ("math.combinatorics.finite-configurations.complete-family-mass",
     "Complete-family mass and higher uniformity",
     "An authorial provider package relates complete-family mass, higher-order uniformity, and the error terms consumed by AFT.",
     "method", "author-complete", "supported", "ready-for-review", "mass", [
         evidence("authorial-argument", "support", "the provider package as formulated", P["mass"])
     ]),
    ("math.number-theory.reciprocal-representations.aft-e306-conditional-application",
     "Conditional AFT application to E306",
     "A provider map records how E306 could instantiate AFT, but it is not an independently assured fourth proof and is not the canonical proof route.",
     "connection", "author-complete", "supported", "ready-for-review", "aft_e306", [
         evidence("authorial-argument", "qualify", "conditional provider map only; no proof-status upgrade", P["aft_e306"])
     ]),
    ("math.number-theory.reciprocal-representations.e306-formal-release-axis",
     "E306 v0.0.3 formal/release axis",
     "The tagged Lean release formalizes the exact characterization and its conditional analytic interface; this axis is orthogonal to human proof-route assurance.",
     "proof", "assessed", "established-in-scope", "integrated", "formal_statement", [
         evidence("formal-kernel-check", "support", "Lean theorem statements and proofs at release v0.0.3, under the named analytic inputs", P["formal_audit"])
     ]),
    ("math.analytic-number-theory.prime-distribution.e306-formal-trust-boundary",
     "E306 formal analytic trust boundary",
     "The v0.0.3 formal theorem consumes the exact Rosser–Schoenfeld inputs rosser_schoenfeld_cor3 and rosser_schoenfeld_thm5; kernel checking verifies the reduction but does not independently prove those analytic inputs.",
     "concept", "assessed", "scope-split", "integrated", "formal_inputs", [
         evidence("formal-kernel-check", "qualify", "v0.0.3 formal reduction conditional on Rosser–Schoenfeld (1962) Corollary 3 via rosser_schoenfeld_cor3 and Theorem 5 via rosser_schoenfeld_thm5", P["formal_inputs"])
     ]),
    ("math.harmonic-analysis.finite-fourier.small-theta-gff-candidate",
     "Small-theta GFF candidate",
     "A captured authorial candidate for a non-enumerative Gaussian-free-field-style route beyond the present E306 proof families.",
     "heuristic", "captured", "open", "dormant", "rl", [
         evidence("authorial-argument", "inconclusive", "frontier candidate only", P["rl"])
     ]),
    ("math.combinatorics.finite-configurations.sampled-core-method-barriers",
     "Sampled-core method barriers",
     "The curation handoff records method-level barriers showing why several naïve sampled-core or purely local-control routes cannot by themselves replace global decoding.",
     "obstruction", "assessed", "established-in-scope", "integrated", "failures", [
         evidence("authorial-argument", "support", "the stated provider failures and method barriers", P["failures"])
     ]),
    ("math.combinatorics.finite-configurations.bipartite-plaquette-counterexample",
     "Bipartite plaquette counterexample",
     "A permanent negative example blocks an overstrong inference from local plaquette control to the required global decoded uniformity.",
     "counterexample", "assessed", "refuted-in-scope", "integrated", "failures", [
         evidence("authorial-argument", "refute", "the overstrong local-to-global inference only", P["failures"])
     ]),
    ("math.number-theory.reciprocal-representations.e306-superseded-route-genealogy",
     "E306 superseded-route genealogy",
     "Historical curation and superseded proof attempts remain auditable as genealogy; none is a base or whole-branch merge source for this intake.",
     "connection", "assessed", "superseded", "closed", "old", [
         evidence("source-fidelity-check", "qualify", "archival genealogy and supersession only", P["old"])
     ]),
    ("math.number-theory.arithmetic-derivatives.erdos-307-adjacent-open-programme",
     "Erdős 307 adjacent open programme",
     "E307 is an adjacent but distinct open programme concerning arithmetic derivatives; E306 developments may suggest questions but do not launch or solve it.",
     "problem", "formulated", "open", "dormant", "rl", [
         evidence("source-fidelity-check", "qualify", "separate/open status in the bounded curation handoff", P["rl"])
     ]),
    ("math.number-theory.reciprocal-representations.e306-future-frontier",
     "E306 future mathematical frontier",
     "Post-proof questions include simplification, provider abstraction, publication architecture, and genuinely new consequences; they remain open and unlaunched.",
     "question", "formulated", "open", "dormant", "publication", [
         evidence("authorial-argument", "inconclusive", "frontier and publication-level decision only", P["publication"])
     ]),
]

units = []
for uid, title, summary, form, maturity, disposition, workflow, primary, assurance in unit_defs:
    units.append({
        "id": uid,
        "title": title,
        "summary": summary,
        "form": form,
        "maturity": maturity,
        "assurance": assurance,
        "disposition": disposition,
        "workflow": workflow,
        "provenance": [P[primary]],
        "relations": [],
        "views": ["programme.erdos-306"],
    })


def relation(rid: str, source: str, target: str, plane: str, rtype: str,
             scope: str, provenance: dict, status: str = "curator-mapped") -> dict:
    return {
        "id": rid, "source": source, "target": target, "plane": plane,
        "type": rtype, "scope": scope, "status": status,
        "provenance": [{k: provenance[k] for k in ("repository", "commit", "path", "blob", "anchor")}],
    }


N = "math.number-theory.reciprocal-representations."
H = "math.harmonic-analysis.finite-fourier."
C = "math.combinatorics.finite-configurations."
A = "math.analytic-number-theory.prime-distribution."
E307 = "math.number-theory.arithmetic-derivatives.erdos-307-adjacent-open-programme"

logical_specs = [
    ("rel.e306.characterization-uses-necessity", N+"squarefree-semiprime-characterization", N+"squarefree-denominator-necessity", "uses", "necessity direction", P["dense"]),
    ("rel.e306.characterization-uses-avoiding", N+"squarefree-semiprime-characterization", N+"avoiding-unit-reduction", "uses", "sufficiency direction", P["dense"]),
    ("rel.e306.dense-uses-prime-supply", N+"dense-one-anchor-proof", A+"fixed-ratio-prime-supply", "uses", "fixed-ratio prime blocks and target-prime supply", P["dense_ledger"]),
    ("rel.e306.dense-uses-complete-pairs", N+"dense-one-anchor-proof", N+"complete-pair-denominator-family", "uses", "canonical denominator family", P["dense"]),
    ("rel.e306.dense-uses-selector", N+"dense-one-anchor-proof", H+"bernoulli-subset-selector", "uses", "finite Fourier target selection", P["dense"]),
    ("rel.e306.dense-uses-rigidity", N+"dense-one-anchor-proof", C+"reciprocal-label-rigidity", "uses", "row-code and reciprocal-label separation", P["dense"]),
    ("rel.e306.dense-uses-decoder", N+"dense-one-anchor-proof", H+"anchor-fibre-decoder-observability", "uses", "target-prime fibre decoder", P["dense"]),
    ("rel.e306.dense-uses-five-sector", N+"dense-one-anchor-proof", H+"five-sector-positivity-budget", "uses", "exhaustive error partition and positivity", P["dense_review"]),
    ("rel.e306.dense-implies-characterization", N+"dense-one-anchor-proof", N+"squarefree-semiprime-characterization", "implies", "together with the necessity lemma", P["dense_review"]),
    ("rel.e306.multiblock-implies-characterization", N+"multiblock-proof", N+"squarefree-semiprime-characterization", "implies", "repaired independently assured fallback", P["multi_repair"]),
    ("rel.e306.sparse-uses-sensor", N+"sparse-sensor-proof", C+"sparse-actual-prime-sensor-core", "uses", "actual-prime sparse sensor family", P["sparse"]),
    ("rel.e306.sparse-uses-decoder", N+"sparse-sensor-proof", H+"anchor-fibre-decoder-observability", "uses", "exact target decoder and cold-label ranges", P["sparse_repair"]),
    ("rel.e306.sparse-implies-characterization", N+"sparse-sensor-proof", N+"squarefree-semiprime-characterization", "implies", "repaired independently assured alternative", P["sparse_repair"]),
    ("rel.e306.aft-uses-weighted-skeleton", H+"anchor-fibre-transference", H+"weighted-decoded-skeleton", "uses", "authorial structural skeleton", P["aft"]),
    ("rel.e306.aft-uses-observability", H+"anchor-fibre-transference", H+"quantitative-target-observability", "uses", "target visibility provider", P["observability"]),
    ("rel.e306.aft-uses-complete-mass", H+"anchor-fibre-transference", C+"complete-family-mass", "uses", "mass and higher-uniformity provider", P["mass"]),
    ("rel.e306.aft-e306-specializes-aft", N+"aft-e306-conditional-application", H+"anchor-fibre-transference", "specializes", "conditional authorial provider map only", P["aft_e306"]),
    ("rel.e306.barriers-qualify-aft", C+"sampled-core-method-barriers", H+"anchor-fibre-transference", "qualifies", "provider failures that any AFT instantiation must avoid", P["failures"]),
    ("rel.e306.plaquette-refutes-local-global", C+"bipartite-plaquette-counterexample", C+"complete-family-mass", "qualifies", "refutes an overstrong local-control implication, not the provider package as stated", P["failures"]),
    ("rel.e306.formal-specializes-characterization", N+"e306-formal-release-axis", N+"squarefree-semiprime-characterization", "specializes", "formal theorem at v0.0.3 under named analytic inputs", P["formal_statement"]),
    ("rel.e306.trust-qualifies-formal", A+"e306-formal-trust-boundary", N+"e306-formal-release-axis", "qualifies", "kernel assurance is conditional on two analytic inputs", P["formal_inputs"]),
    ("rel.e306.dense-supersedes-genealogy", N+"dense-one-anchor-proof", N+"e306-superseded-route-genealogy", "supersedes", "current intake replaces archival curation as navigation, without rewriting history", P["old"]),
]
discovery_specs = [
    ("rel.e306.aft-arose-from-decoder", H+"anchor-fibre-transference", H+"anchor-fibre-decoder-observability", "arose-from", "general mechanism abstracted from decoded E306 routes", P["aft"]),
    ("rel.e306.gff-motivated-by-barriers", C+"sampled-core-method-barriers", H+"small-theta-gff-candidate", "motivates", "method barriers motivate a non-enumerative candidate", P["rl"]),
    ("rel.e306.dense-suggests-frontier", N+"dense-one-anchor-proof", N+"e306-future-frontier", "suggests", "post-proof simplification and provider questions", P["publication"]),
    ("rel.e306.aft-suggests-frontier", H+"anchor-fibre-transference", N+"e306-future-frontier", "suggests", "possible abstraction and reuse questions", P["publication"]),
    ("rel.e306.e306-suggests-e307", N+"squarefree-semiprime-characterization", E307, "suggests", "adjacent question only; no logical implication, launch, or solved claim", P["rl"]),
]

logical = [relation(r, s, t, "logical", ty, sc, pv) for r, s, t, ty, sc, pv in logical_specs]
discovery = [relation(r, s, t, "discovery", ty, sc, pv, "captured-unreviewed") for r, s, t, ty, sc, pv in discovery_specs]
for rel in logical + discovery:
    for unit in units:
        if unit["id"] in (rel["source"], rel["target"]):
            unit["relations"].append(rel["id"])
    if rel["source"] == E307 or rel["target"] == E307:
        for unit in units:
            if unit["id"] == E307:
                unit["views"].append("frontier.erdos-307")

write_json("registry/units/number-theory/reciprocal-representations/E306_CUR_CANONICAL_INTAKE_UNITS.json", {
    "schema_version": "1.1.0",
    "batch_id": BATCH,
    "item_schema": "registry/schema/mathematical-unit.schema.json",
    "units": units,
})
write_json("registry/relations/E306_CUR_CANONICAL_INTAKE_RELATIONS.json", {
    "schema_version": "1.1.0",
    "batch_id": BATCH,
    "item_schema": "registry/schema/typed-relation.schema.json",
    "logical": logical,
    "discovery": discovery,
})

write_json("registry/views/programme.erdos-306.json", {
    "view_id": "programme.erdos-306",
    "title": "Erdős 306 programme view",
    "view_type": "programme",
    "registry_source": "registry/units/number-theory/reciprocal-representations/E306_CUR_CANONICAL_INTAKE_UNITS.json",
    "relation_source": "registry/relations/E306_CUR_CANONICAL_INTAKE_RELATIONS.json",
    "compatibility_entrypoints": [
        "projects/erdos-306/README.md",
        "projects/erdos-306/CURRENT_BEST.md",
        "projects/erdos-306/ASSURANCE_AND_SOURCE_MAP.md",
        "projects/erdos-306/FRONTIER_AND_E307_SEPARATION.md",
    ],
    "sections": {
        "theorem": [N+"squarefree-semiprime-characterization"],
        "preferred_human_spine": [N+"dense-one-anchor-proof"],
        "independently_assured_fallback": [N+"multiblock-proof"],
        "independently_assured_alternative": [N+"sparse-sensor-proof"],
        "authorial_generalization_pending_review": [
            H+"anchor-fibre-transference", N+"aft-e306-conditional-application"
        ],
        "orthogonal_formal_axis": [N+"e306-formal-release-axis", A+"e306-formal-trust-boundary"],
        "negative_and_method_boundaries": [
            C+"sampled-core-method-barriers", C+"bipartite-plaquette-counterexample"
        ],
        "open_unlaunched_frontier": [N+"e306-future-frontier", E307],
    },
    "status_statement": "E306 has three independently assured human proof routes with the dense one-anchor route preferred for exposition. AFT is authorial, the Lean release is an orthogonal conditional formal axis, and E307 remains separate/open.",
    "nonduplication_rule": "This project view references natural units; it does not own or duplicate mathematical truth.",
})
write_json("registry/views/frontier.erdos-307.json", {
    "view_id": "frontier.erdos-307",
    "title": "Erdős 307 adjacent frontier",
    "view_type": "frontier",
    "registry_source": "registry/units/number-theory/reciprocal-representations/E306_CUR_CANONICAL_INTAKE_UNITS.json",
    "relation_source": "registry/relations/E306_CUR_CANONICAL_INTAKE_RELATIONS.json",
    "sections": {"open_separate": [E307], "discovery_only_antecedent": [N+"squarefree-semiprime-characterization"]},
    "status_statement": "OPEN / SEPARATE / NOT LAUNCHED. The E306 connection is discovery-plane only.",
    "nonduplication_rule": "No E306 proof status transfers to E307.",
})

write("math/number-theory/reciprocal-representations/squarefree-semiprime-characterization.md", f"""
# Squarefree-semiprime reciprocal characterization

## Statement

For a positive rational number \(a/b\) in lowest terms, the following are equivalent:

1. \(b\) is squarefree;
2. \(a/b\) is a finite sum of distinct reciprocals of squarefree semiprimes.

The necessity direction is the squarefree-denominator lemma.  The sufficiency direction is organized as an avoiding-unit construction, so numerator induction can forbid all denominators already used.

## Preferred human spine

The preferred exposition is the independently audited dense one-anchor route.  It chooses a prime block \(P=[X,X^3)\), a top block \(B=[Z/2,Z)\), and the complete pair family \(P\\times B\).  Reciprocal-label rigidity gives row-code separation; a target-prime fibre supplies the decoder; finite Fourier inversion then separates five explicit character sectors.  The proof closes only after the exact audit-gate ranges, the \(R=0\) branch, normalization factors, full top partition, decoder ranges, actual-family cubic remainder, no-wrap estimate, and parameter order \(C\) then \(X\) are retained.

## Other assured routes

The repaired multiblock proof is an independently assured fallback.  The repaired sparse actual-prime sensor proof is an independently assured alternative.  They prove the same characterization but are not merged into a synthetic unaudited fourth proof.

Registry unit: `{N}squarefree-semiprime-characterization`.
""")

write("math/number-theory/reciprocal-representations/complete-pair-fourier-selection.md", f"""
# Complete-pair Fourier selection

The E306 dense route uses squarefree semiprime denominators \(pq\) from a complete pair family.  A full partition of the top prime block prevents hidden overlap, while reciprocal-label rigidity makes different rows distinguishable to the target decoder.

Finite Fourier inversion evaluates the probability that a Bernoulli-selected subfamily reaches the desired residue.  The main term is positive.  Every nontrivial character belongs to one of five audited sectors: coherent decoder-visible fibres, noncoherent fibres, nondecoder characters, and the remaining large/small control regimes recorded by the route.  The estimates are a single package: deleting a range, normalization factor, decoder endpoint, or actual-family remainder invalidates the assurance attribution.

Natural units: `{N}complete-pair-denominator-family`, `{H}bernoulli-subset-selector`, `{C}reciprocal-label-rigidity`, `{H}five-sector-positivity-budget`.
""")

write("math/harmonic-analysis/finite-fourier/anchor-fibre-decoding.md", f"""
# Anchor-fibre decoding

An anchor fibre is a family of labels sharing a target-prime coordinate.  Its row code exposes whether a character is coherent and whether the target residue is observable.  This is the structural bridge between modular Fourier inversion and arithmetic denominator selection.

In the audited E306 proofs the decoder is route-specific and established only with its exact label ranges.  The later anchor-fibre transference packet abstracts a weighted decoded skeleton and quantitative observability interface, but that abstraction is authorial and still awaits independent review.  It must not be cited as an independently assured E306 proof.

Natural units: `{H}anchor-fibre-decoder-observability`, `{H}weighted-decoded-skeleton`, `{H}quantitative-target-observability`, `{H}anchor-fibre-transference`.
""")

write("math/combinatorics/finite-configurations/anchor-fibre-transference.md", f"""
# Complete families, sparse sensors, and transference

Three independently assured E306 routes instantiate different finite configurations:

- the preferred dense route uses a complete pair family;
- the fallback uses multiple blocks, fingerprints, propagation, coding, and localization;
- the sparse alternative samples actual prime sensors with the exact cold-label cutoff.

The authorial AFT programme asks for a reusable theorem whose providers are complete-family mass, higher uniformity, and target observability.  Provider-failure analysis and the bipartite plaquette counterexample show that purely local control is insufficient for the desired global decoded conclusion.  These are reusable structural observations, not permission to upgrade AFT or to splice proof routes.
""")

write("math/number-theory/reciprocal-representations/frontiers-and-method-barriers.md", f"""
# E306 frontiers and method barriers

The characterization itself is established in the three audited human routes.  Remaining E306 work concerns exposition, publication, simplification, provider abstraction, and possible consequences.  The small-theta GFF idea is a captured frontier candidate, not an active or assured route.

Historical failed or superseded attempts remain in the source manifest and genealogy.  They are negative knowledge rather than merge bases.

Erdős 307 is adjacent only in the discovery plane.  It is a separate open programme, not launched here, and no E306 theorem implies that E307 is solved.
""")

write("projects/erdos-306/README.md", """
# Erdős 306 project view

This directory is a compatibility and navigation view over natural mathematical units.  It does not own a separate copy of mathematical truth.

- `CURRENT_BEST.md`: theorem and proof-family disposition.
- `ASSURANCE_AND_SOURCE_MAP.md`: exact assurance strata and immutable source map.
- `FRONTIER_AND_E307_SEPARATION.md`: open work and the E307 boundary.
- `registry/views/programme.erdos-306.json`: machine-readable project view.
- `migration/source-to-unit-map/E306_CUR_CANONICAL_INTAKE_MAP.json`: all 75 source artifacts mapped to stable units.
""")

write("projects/erdos-306/CURRENT_BEST.md", f"""
# E306 current best

## Mathematical result

The squarefree-semiprime reciprocal characterization is established in scope.

## Human proof disposition

1. **Preferred:** dense one-anchor proof.
2. **Fallback:** repaired multiblock proof.
3. **Alternative:** repaired sparse actual-prime sensor proof.

All three have independent mathematical review in their exact route scopes.  They are kept distinct; no unaudited hybrid proof is asserted.

## Separate axes

- Anchor-fibre transference is an authorial general mechanism pending independent review.
- Lean release v0.0.3 is kernel-checked under two named analytic inputs; it is orthogonal to human proof-family assurance.
- Earlier mathematics curation at `6505b51f12de3fdaaf4976379b0ce8b0a665cfc1` is archival genealogy only.
""")

write("projects/erdos-306/ASSURANCE_AND_SOURCE_MAP.md", """
# E306 assurance and source map

| Surface | Disposition | Assurance boundary |
|---|---|---|
| Dense one-anchor | preferred human spine | independent mathematical review; exact audit gate applies |
| Repaired multiblock | fallback | independent audit plus bounded repair verification |
| Repaired sparse sensor | alternative | independent audit plus exact cold-label repair verification |
| Anchor-fibre transference | reusable authorial mechanism | no independent review; no E306 proof upgrade |
| Lean v0.0.3 | formal/release axis | kernel-checked conditional reduction; two analytic inputs remain the trust boundary |
| Historical curation | genealogy | archival only; no whole-branch merge and no base status |

The immutable manifest names 12 frozen source packets.  The source-to-unit map contains 75 artifact-level locators, each with repository, 40-hex commit, path, blob, and line anchor.  Every item maps to at least one of 26 stable natural units; unclassified count is zero.
""")

write("projects/erdos-306/FRONTIER_AND_E307_SEPARATION.md", """
# E306 frontier and E307 separation

E306's theorem is established, but publication, exposition, proof simplification, provider abstraction, and new consequences remain possible future work.  The GFF-style route is captured but unlaunched.

E307 is **OPEN / SEPARATE / NOT LAUNCHED**.  Its only relation to E306 in this intake is a discovery-plane `suggests` edge.  There is no logical implication and no solved claim.
""")

write("registry/discovery/E306_CUR_CANONICAL_INTAKE_DISCOVERY_ADDENDUM.md", """
# E306 intake discovery addendum

The intake itself exposed several potentially useful observations without activating research:

1. The dense, multiblock, and sparse routes share decoder and positivity interfaces but have genuinely different provider geometries; preserving all three may be more valuable than forcing a synthetic proof.
2. Anchor-fibre transference is the natural abstraction candidate, while provider failures show that local plaquette control alone cannot supply global decoded uniformity.
3. The formal axis isolates the exact analytic trust boundary and can inform later interface design without deciding the preferred human proof.
4. The E306→E307 adjacency may inspire questions, but remains unreviewed discovery context only.

All four observations are captured-unreviewed.  They carry no proof-status upgrade or work-launch authority.
""")

print(f"E306 knowledge plane built: units={len(units)} logical={len(logical)} discovery={len(discovery)}")
