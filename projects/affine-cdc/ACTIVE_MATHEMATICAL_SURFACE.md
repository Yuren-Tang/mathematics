# AffineCDC active mathematical surface

This file identifies the current mathematical surface on the Programme B1 curation candidate while preserving the fixed Programme A Audit A candidate.

## 1. Exact construction line

- canonical repository base: `main@960c92b7ff231c78b387894149779083060a75eb`;
- immutable Programme A source: `proof-development/affine-cdc-rigour-v1@8bee16780b549f51e1f29343671a059961ec4172`;
- fixed Programme A Audit A candidate: `curation/affine-cdc-programme-a-v1@68715fb29bb4b6555e2bc3e089603c5390d01566`;
- immutable Programme B1 source: `proof-development/affine-cdc-rigour-v1@778b09ac8260192e022f512f24cdef1d04871f37`;
- Programme B1 candidate branch: `curation/affine-cdc-programme-b1-v1`;
- exact source splice commit: `35c7a2851f070061175194eef10568c0a456cf8e`.

The splice has first parent `68715fb...` and second parent `778b09ac...`. Its tree admits exactly the five B1 dossiers and the immutable B1 checkpoint DAG from the source side.

## 2. Primary entrypoints

- [`README.md`](README.md) — project entrypoint;
- [`CURRENT_BEST.md`](CURRENT_BEST.md) — compact mathematical state;
- [`MATHEMATICAL_ARCHITECTURE.md`](MATHEMATICAL_ARCHITECTURE.md) — controlling architecture;
- [`THEOREM_DEPENDENCY_MAP.md`](THEOREM_DEPENDENCY_MAP.md) — Programme A and B1 theorem DAGs;
- [`FORMAL_STATUS.md`](FORMAL_STATUS.md) — assurance boundaries;
- [`FRONTIER_STATUS.md`](FRONTIER_STATUS.md) — open global endpoint.

## 3. Fixed Programme A surface

The complete Cycle Double Cover proof surface remains:

1. [`complete-cdc/foundations-expansion-and-flow.md`](complete-cdc/foundations-expansion-and-flow.md);
2. [`complete-cdc/affine-compatibility-and-extraction.md`](complete-cdc/affine-compatibility-and-extraction.md);
3. [`complete-cdc/collapse-decomposition-and-assembly.md`](complete-cdc/collapse-decomposition-and-assembly.md).

Programme A exact dossiers A0–A10 remain under `proof-development/`. This B1 intake changes no Programme A theorem chapter, assurance file specific to Audit A, or fixed candidate branch.

## 4. Active Programme B1 surface

The preferred integrated B1 theorem is:

- [`five-support/b1-object-quantifier-and-scope.md`](five-support/b1-object-quantifier-and-scope.md).

Synchronized B1 chapters are:

- [`five-support/root-flow-lifting.md`](five-support/root-flow-lifting.md);
- [`five-support/surfaces-and-halfcube.md`](five-support/surfaces-and-halfcube.md);
- [`five-support/equivalent-formulations-and-proof-families.md`](five-support/equivalent-formulations-and-proof-families.md);
- [`five-support/README.md`](five-support/README.md).

B1 control surfaces are:

- [`PROGRAMME_B1_INTEGRATION_MAP.md`](PROGRAMME_B1_INTEGRATION_MAP.md);
- [`PROGRAMME_B1_QUANTIFIER_BOUNDARIES.md`](PROGRAMME_B1_QUANTIFIER_BOUNDARIES.md);
- [`PROGRAMME_B1_INTEGRATION_MANIFEST.md`](PROGRAMME_B1_INTEGRATION_MANIFEST.md).

## 5. Exact B1 authorial provenance

The candidate retains exact source blobs for:

- `proof-development/AC_PD_B1_1_ROOT_FLOW_TRIANGLE_EQUIVALENCE.md`;
- `proof-development/AC_PD_B1_2_MATCHING_FOUR_FLOW_EQUIVALENCE.md`;
- `proof-development/AC_PD_B1_3_FIXED_FLOW_PLANE_CRITERION.md`;
- `proof-development/AC_PD_B1_4_SURFACE_HALFCUBE_SCOPE.md`;
- `proof-development/AC_PD_B1_EQUIVALENCE_AND_SCOPE_MAP.md`;
- the `OBLIGATION_DAG.md` at the immutable B1 checkpoint.

These dossiers are proof, audit, and repair surfaces. The integrated B1 chapter is the preferred current exposition.

## 6. B1 scope installed

The active corpus now distinguishes:

- graph-level existential five-support existence;
- fixed $(f,W)$ component obstruction;
- fixed $f$ with variable plane;
- fixed compatible lift and same-embedding componentwise compression;
- an external root flow on a prescribed dual, subject to holonomy;
- the old-colour-factorable quotient $J_g$.

It also records the exact support-coordinate/root-label distinction, the missing matching/four-flow datum, and the even-halfcube odd-translation convention.

## 7. B2+ exclusion

The candidate does not contain source-side additions for:

- `AC_PD_B2_*`;
- `AC_PD_B3_*`;
- later PDL `OBLIGATION_DAG.md` changes;
- Programme B2 or B3 handoffs;
- any moving-tip correction after `778b09ac...`.

The previously integrated five-support chapters beyond B1 remain present with their prior corpus status. Their later PDL corrections are not silently consumed or dispositioned here.

## 8. Historical research recovery

The seventy-eight discovery-order `research/FIVE_CDC_*.md` packets remain retired from the current tree after successor mapping and recoverable from the public historical checkpoint.

Existing recovery controls remain:

- [`CHAPTER_PROVENANCE.md`](CHAPTER_PROVENANCE.md);
- [`MIGRATION_LEDGER.md`](MIGRATION_LEDGER.md);
- [`RETIRED_SOURCE_CLASSIFICATION.md`](RETIRED_SOURCE_CLASSIFICATION.md);
- [`SOURCE_RECOVERY_AUDIT.md`](SOURCE_RECOVERY_AUDIT.md);
- [`SUPERSESSION_MAP.md`](SUPERSESSION_MAP.md).

## 9. Assurance boundary

Programme A remains fixed for Audit A. Programme B1 is Curator-integrated authorial proof-development mathematics and has not received dedicated independent audit.

Neither Programme A nor B1 is end-to-end Lean verified by this intake. No manuscript, peer-review, publication, release, arXiv, DOI, or timestamp status is created.
