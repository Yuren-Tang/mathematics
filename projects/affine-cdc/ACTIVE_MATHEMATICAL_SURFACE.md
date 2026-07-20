# AffineCDC active mathematical surface

This file identifies the current mathematical surface on the Programme B2 curation candidate while preserving the fixed Programme A Audit A candidate and the accepted B1 ancestor.

## 1. Exact construction line

- canonical repository base: `main@960c92b7ff231c78b387894149779083060a75eb`;
- fixed Programme A Audit A candidate: `curation/affine-cdc-programme-a-v1@68715fb29bb4b6555e2bc3e089603c5390d01566`;
- Programme B1 integration base: `curation/affine-cdc-programme-b1-v1@4d7b9c74ea4377a58e219a7c6c3cb569a8229276`;
- immutable Programme B2 source: `proof-development/affine-cdc-rigour-v1@d62974704d6dac77aaa00275a595fedf7f70cfd2`;
- Programme B2 candidate branch: `curation/affine-cdc-programme-b2-v1`;
- exact B2 source splice: `9799d8a657cb43ed5d896d53ef16c50fc79c4e1e`.

The splice has first parent `4d7b9c74...` and second parent `d6297470...`. Its tree imports exactly the five B2 dossiers and the immutable B2 checkpoint DAG from the source side.

## 2. Primary entrypoints

- [`README.md`](README.md) — project entrypoint;
- [`CURRENT_BEST.md`](CURRENT_BEST.md) — compact mathematical state;
- [`MATHEMATICAL_ARCHITECTURE.md`](MATHEMATICAL_ARCHITECTURE.md) — controlling architecture;
- [`THEOREM_DEPENDENCY_MAP.md`](THEOREM_DEPENDENCY_MAP.md) — Programme A/B1/B2 theorem DAG;
- [`FORMAL_STATUS.md`](FORMAL_STATUS.md) — assurance and correction boundaries;
- [`FRONTIER_STATUS.md`](FRONTIER_STATUS.md) — open global endpoint.

## 3. Fixed Programme A surface

The complete Cycle Double Cover proof surface remains:

1. [`complete-cdc/foundations-expansion-and-flow.md`](complete-cdc/foundations-expansion-and-flow.md);
2. [`complete-cdc/affine-compatibility-and-extraction.md`](complete-cdc/affine-compatibility-and-extraction.md);
3. [`complete-cdc/collapse-decomposition-and-assembly.md`](complete-cdc/collapse-decomposition-and-assembly.md).

Programme A exact dossiers A0–A10 remain under `proof-development/`. The B2 intake changes no Programme A theorem chapter, Audit A-specific assurance file, or fixed candidate branch.

## 4. Active Programme B1 surface

Preferred B1 theorem:

- [`five-support/b1-object-quantifier-and-scope.md`](five-support/b1-object-quantifier-and-scope.md).

B1 controls:

- graph-level root/matching/Fano-plane/surface equivalences;
- fixed $(f,W)$ and fixed-$f$ criteria;
- fixed-lift same-embedding compression;
- prescribed-dual holonomy;
- old-colour factorability;
- even-halfcube parity.

Control files:

- [`PROGRAMME_B1_INTEGRATION_MAP.md`](PROGRAMME_B1_INTEGRATION_MAP.md);
- [`PROGRAMME_B1_QUANTIFIER_BOUNDARIES.md`](PROGRAMME_B1_QUANTIFIER_BOUNDARIES.md).

## 5. Active Programme B2 surface

Preferred B2 theorem:

- [`five-support/b2-formulation-and-witness-hierarchy.md`](five-support/b2-formulation-and-witness-hierarchy.md).

Synchronized chapters:

- [`five-support/root-flow-lifting.md`](five-support/root-flow-lifting.md);
- [`five-support/equivalent-formulations-and-proof-families.md`](five-support/equivalent-formulations-and-proof-families.md);
- [`five-support/README.md`](five-support/README.md).

B2 control files:

- [`PROGRAMME_B2_INTEGRATION_MAP.md`](PROGRAMME_B2_INTEGRATION_MAP.md);
- [`PROGRAMME_B2_WITNESS_SCOPE.md`](PROGRAMME_B2_WITNESS_SCOPE.md);
- [`PROGRAMME_B2_INTEGRATION_MANIFEST.md`](PROGRAMME_B2_INTEGRATION_MANIFEST.md).

## 6. Exact B2 authorial provenance

The candidate retains exact source blobs for:

- `proof-development/AC_PD_B2_1_SINGULAR_QUADRATIC_SCHUR_EQUIVALENCE.md`;
- `proof-development/AC_PD_B2_2_COGRAPHIC_CYCLE_CONTINUITY.md`;
- `proof-development/AC_PD_B2_3_ORTHOGONAL_ROOT_MODULE_CORRECTION.md`;
- `proof-development/AC_PD_B2_4_FOURIER_STRESS_DUALITY.md`;
- `proof-development/AC_PD_B2_FORMULATION_AND_WITNESS_MAP.md`;
- the `OBLIGATION_DAG.md` at the immutable B2 checkpoint.

The integrated chapters are the preferred reading surface; the dossiers remain proof, audit, and repair surfaces.

## 7. Witness hierarchy installed

The active corpus separates:

- complete graph-level witnesses: five supports, roots, triangles, anisotropic flow, quadratic solution, and cographic edge map;
- fixed-data criteria: singular lifting, component defect, colour-cut parity, eliminated coordinate, and Schur quotient;
- dual/counting layers: relative stresses and exact Fourier intersection counts;
- target models: $O^-(4,2)$, exceptional $O^+(6,2)$, and the universal deleted permutation module.

Every full-witness arrow has an explicit reconstruction map.

## 8. Mathematical correction installed

`FIVE_CDC_UNIVERSAL_ORTHOGONAL_ROOT_LIFT_V1.md` is no longer a controlling theorem source. It is classified as:

`RETIRED / SUPERSEDED / FALSE THEOREM / HISTORICAL PROVENANCE`.

The active replacement is:

- dimension lower bound $\dim V\ge q-2$;
- deleted permutation module of dimension $q-2$;
- exceptional rank-three/eight-support $O^+(6,2)$ realization;
- no universal $O^+(2r,2)$ hierarchy.

## 9. B3+ exclusion

The candidate does not import:

- `AC_PD_B3_*`;
- `AC_PD_B4_*`;
- `AC_PD_B5_*` or later dossiers;
- later PDL `OBLIGATION_DAG.md` changes;
- Programme B2/B3/B4/B5 handoffs as mathematical source;
- any moving-tip commit after `d6297470...`.

The wider previously integrated five-support corpus remains present with its prior status, but later PDL corrections are not silently consumed.

## 10. Historical research recovery

The seventy-eight discovery-order `research/FIVE_CDC_*.md` packets remain retired from the current tree and recoverable from the public historical checkpoint.

Current controls:

- [`CHAPTER_PROVENANCE.md`](CHAPTER_PROVENANCE.md);
- [`MIGRATION_LEDGER.md`](MIGRATION_LEDGER.md);
- [`RETIRED_SOURCE_CLASSIFICATION.md`](RETIRED_SOURCE_CLASSIFICATION.md);
- [`SOURCE_RECOVERY_AUDIT.md`](SOURCE_RECOVERY_AUDIT.md);
- [`SUPERSESSION_MAP.md`](SUPERSESSION_MAP.md).

## 11. Assurance boundary

Programme A remains fixed for Audit A. Programme B1 and B2 are Curator-integrated authorial proof-development mathematics in their stated scopes.

Neither B1 nor B2 has received dedicated independent audit or end-to-end Lean verification. No manuscript, peer-review, publication, release, arXiv, DOI, novelty, or timestamp status is created.
