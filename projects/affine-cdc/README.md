# AffineCDC

AffineCDC studies affine incidence geometry attached to nowhere-zero binary flows, its complete Cycle Double Cover consequence, and the stronger open problem of compressing compatible covers to five indexed supports.

The active current-best surface is listed in [`ACTIVE_MATHEMATICAL_SURFACE.md`](ACTIVE_MATHEMATICAL_SURFACE.md).

## 1. Complete Cycle Double Cover theorem

Programme A integrates a complete authorial paper-proof of:

> Every multigraph with finite active edge set and no singleton cut has a finite circuit double cover.

The fixed Audit A candidate is

`curation/affine-cdc-programme-a-v1@68715fb29bb4b6555e2bc3e089603c5390d01566`.

Programme B1 and B2 candidates descend from that exact ref and do not modify it.

Read the controlling Programme A proof under [`complete-cdc/`](complete-cdc/). The exact A0–A10 dossiers remain under [`proof-development/`](proof-development/) as provenance, audit, and repair surfaces.

## 2. Programme B1 — object and quantifiers

Programme B1 closes:

- five supports ↔ $R_5$ flow ↔ $K_5$ triangles;
- exact matching/four-flow data;
- fixed-$(f,W)$ component obstruction;
- fixed-flow existential plane criterion;
- root-lift/cycle-face-surface equivalence;
- fixed-lift same-embedding full-dual criterion;
- prescribed-dual holonomy;
- strict old-colour quotient scope;
- even-halfcube parity adapter.

Preferred reading:

- [`five-support/b1-object-quantifier-and-scope.md`](five-support/b1-object-quantifier-and-scope.md);
- [`PROGRAMME_B1_INTEGRATION_MAP.md`](PROGRAMME_B1_INTEGRATION_MAP.md);
- [`PROGRAMME_B1_QUANTIFIER_BOUNDARIES.md`](PROGRAMME_B1_QUANTIFIER_BOUNDARIES.md).

## 3. Programme B2 — formulations and witness hierarchy

Programme B2 extends the complete graph-level witness box to:

$$
\text{five supports}
\Longleftrightarrow
R_5\text{ flow}
\Longleftrightarrow
K_5\text{ triangles}
\Longleftrightarrow
O^-(4,2)\text{ anisotropic flow}
\Longleftrightarrow
\text{quadratic cycle solution}
\Longleftrightarrow
M(G)\to M^*(K_5)\text{ cycle-continuous edge map}.
$$

It separately classifies:

- singular and Schur descriptions as complete fixed-data lift criteria;
- relative stresses as exact dual linear obstructions;
- Fourier expansion as an exact fixed-orbit count with a separate primal-witness step.

Preferred reading:

- [`five-support/b2-formulation-and-witness-hierarchy.md`](five-support/b2-formulation-and-witness-hierarchy.md);
- [`PROGRAMME_B2_INTEGRATION_MAP.md`](PROGRAMME_B2_INTEGRATION_MAP.md);
- [`PROGRAMME_B2_WITNESS_SCOPE.md`](PROGRAMME_B2_WITNESS_SCOPE.md).

## 4. Orthogonal correction

The retired packet `FIVE_CDC_UNIVERSAL_ORTHOGONAL_ROOT_LIFT_V1.md` contains a false universal theorem and is no longer part of the active theorem family.

The controlling replacement proves:

- every additive anisotropic representation of $K_q$ with triangle addition has dimension at least $q-2$;
- the deleted permutation module attains dimension $q-2$;
- the eight-support $O^+(6,2)$ realization is exceptional because $8-2=6$;
- there is no universal $O^+(2r,2)$ hierarchy.

The packet remains recoverable only as `SUPERSEDED / FALSE THEOREM / HISTORICAL PROVENANCE`.

## 5. Wider five-support programme

The global five-support theorem remains open. The remaining dependency order is:

1. B3 surface/target correction and capacity layer;
2. B4 gauge and horizontal reconfiguration;
3. B5 cuts, four-poles, and routing;
4. B6 holonomy, defects, and atoms;
5. B7 localization consequences;
6. B8 finite certificates;
7. B9 global assembly at the genuine localization/composition frontier.

This intake consumes no B3+ moving-branch mathematics.

Read the wider corpus through [`five-support/README.md`](five-support/README.md). See [`FRONTIER_STATUS.md`](FRONTIER_STATUS.md) for the open endpoint.

## 6. Provenance and control

- [`MATHEMATICAL_ARCHITECTURE.md`](MATHEMATICAL_ARCHITECTURE.md) — project architecture;
- [`THEOREM_DEPENDENCY_MAP.md`](THEOREM_DEPENDENCY_MAP.md) — Programme A/B1/B2 DAGs;
- [`CURRENT_BEST.md`](CURRENT_BEST.md) — compact mathematical state;
- [`PROGRAMME_A_INTEGRATION_MAP.md`](PROGRAMME_A_INTEGRATION_MAP.md) — exact A0–A10 map;
- [`PROGRAMME_B1_INTEGRATION_MAP.md`](PROGRAMME_B1_INTEGRATION_MAP.md) — exact B1 map;
- [`PROGRAMME_B2_INTEGRATION_MAP.md`](PROGRAMME_B2_INTEGRATION_MAP.md) — exact B2 map;
- [`CHAPTER_PROVENANCE.md`](CHAPTER_PROVENANCE.md) — historical source provenance;
- [`RETIRED_SOURCE_CLASSIFICATION.md`](RETIRED_SOURCE_CLASSIFICATION.md) — retirement and false-theorem classification;
- [`SUPERSESSION_MAP.md`](SUPERSESSION_MAP.md) — controlling corrections;
- [`FORMAL_STATUS.md`](FORMAL_STATUS.md) — assurance boundary.

## 7. Assurance

Programme A remains fixed for Audit A. Programme B1 and B2 are Curator-integrated authorial proof-development mathematics in their stated scopes.

Neither line is end-to-end Lean verified or independently audited by this intake. Current-best inclusion does not create manuscript, peer-review, publication, release, arXiv, DOI, novelty, or timestamp status.
