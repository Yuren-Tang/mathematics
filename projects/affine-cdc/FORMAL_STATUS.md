# Formalization and reliability boundary

This file separates current mathematical inclusion, authorial proof completion, independent audit, machine verification, manuscript projection, peer review, publication, release, arXiv, and DOI status.

## 1. Programme A complete theorem

Programme A proves at authorial paper-proof level:

> Every multigraph with finite active edge set and no singleton cut has a finite circuit double cover.

Exact Programme A source:

`proof-development/affine-cdc-rigour-v1@8bee16780b549f51e1f29343671a059961ec4172`.

Fixed Audit A candidate:

`curation/affine-cdc-programme-a-v1@68715fb29bb4b6555e2bc3e089603c5390d01566`.

This B1 intake does not modify that branch or change its audit status.

## 2. Programme B1 status

Exact immutable B1 source:

`proof-development/affine-cdc-rigour-v1@778b09ac8260192e022f512f24cdef1d04871f37`.

Integrated B1 scope:

- B1.1 root-flow/$K_5$-triangle equivalence: `COMPLETE-DRAFT`;
- B1.2 exact matching/four-flow theorem: `COMPLETE-DRAFT / CORPUS-CORRECTION`;
- B1.3 fixed-flow/fixed-plane criterion: `COMPLETE-DRAFT`;
- B1.4 surface/halfcube scope: `COMPLETE-DRAFT / SCOPE-CORRECTION`;
- B1 aggregate: Curator-integrated authorial proof layer.

The preferred integrated chapter is [`five-support/b1-object-quantifier-and-scope.md`](five-support/b1-object-quantifier-and-scope.md). Exact provenance is in [`PROGRAMME_B1_INTEGRATION_MAP.md`](PROGRAMME_B1_INTEGRATION_MAP.md).

These statuses do not mean independently audited or machine-checked.

## 3. B1 theorem boundary

Programme B1 proves exact graph-level equivalences among:

- five indexed even supports;
- root-valued $E_5$ flows;
- $K_5$-triangle labellings;
- exact matching/four-flow data;
- existential Fano-flow/plane empty-profile data;
- existential cycle-face surfaces whose full dual maps to the even half-cube.

It also proves the exact fixed-data statements for:

- a fixed pair $(f,W)$;
- a fixed Fano flow with variable plane;
- a fixed compatible root lift and its same-embedding componentwise compression;
- integration of an external root flow on a prescribed dual subject to zero holonomy;
- the old-colour-factorable quotient.

The global five-support theorem for all graphs remains open.

## 4. Six B1 corrections

The active corpus now records:

1. support-coordinate inverse images are even; root-label inverse images are matchings;
2. bare matching plus four-flow is insufficient without $(B,D)$ or component $T$-join data;
3. fixed-$g$ half-cube equivalence concerns componentwise compression of the same embedding;
4. external covers require zero dual holonomy on a prescribed surface;
5. $J_g$ classifies only old-colour-factorable compression;
6. singleton words require an odd translation when the target is the even half-cube.

## 5. Boundary with B2+

This intake consumes no B2, B3, or later moving-branch mathematics.

In particular, it does not integrate or disposition:

- singular/quadratic/Schur/cographic/orthogonal/Fourier dossiers;
- later target-link or finite-certificate corrections;
- later obligation-ledger modifications;
- Programme B2/B3 handoffs.

Any broader equivalence claim remains subject to a separate exact checkpoint and Curator intake.

## 6. Machine-checked anchor

The companion checkpoint

`Yuren-Tang/affine-cdc:main@ebd7098a7a8b824e8c0a511d3c71f61705672aa8`

machine-checks substantial internal slices of the rank-three AffineCDC machinery, including local families, gluing, indexed dart supports, exact two-point coverage, and a cubic-flow CDC result.

It does not end-to-end verify Programme A or the integrated B1 graph/fixed-flow/fixed-lift package.

No Lean repository was changed by this intake.

## 7. Independent-review status

Programme A is fixed for Audit A, but this intake does not perform or complete that audit.

Programme B1 has not received a dedicated independent line-by-line audit. Priority B1 review targets include:

1. mutual inverse root-flow/support construction;
2. matching/four-flow reconstruction and the component $T$-join criterion;
3. common outside-colour parity and fixed-plane equivalence;
4. root-lift/surface construction with support-cycle components;
5. prescribed-dual path-independence/holonomy criterion;
6. full-dual versus old-colour quotient factorization;
7. even-component half-cube parity adapter.

These are assurance targets, not known defects.

## 8. Current source surfaces

Programme A:

- [`complete-cdc/`](complete-cdc/);
- [`PROGRAMME_A_INTEGRATION_MAP.md`](PROGRAMME_A_INTEGRATION_MAP.md);
- exact A0–A10 dossiers under `proof-development/`.

Programme B1:

- [`five-support/b1-object-quantifier-and-scope.md`](five-support/b1-object-quantifier-and-scope.md);
- [`five-support/root-flow-lifting.md`](five-support/root-flow-lifting.md);
- [`five-support/surfaces-and-halfcube.md`](five-support/surfaces-and-halfcube.md);
- [`five-support/equivalent-formulations-and-proof-families.md`](five-support/equivalent-formulations-and-proof-families.md);
- [`PROGRAMME_B1_QUANTIFIER_BOUNDARIES.md`](PROGRAMME_B1_QUANTIFIER_BOUNDARIES.md);
- exact B1 dossiers under `proof-development/`.

## 9. Publication and release status

This intake did not:

- edit or approve a manuscript;
- establish novelty relative to literature;
- authorize arXiv or journal submission;
- create a release or tag;
- modify a DOI or Zenodo record;
- implement a timestamp or priority-attestation workflow.

## 10. Reliability rules

1. Curator integration does not equal independent audit.
2. Natural reformulation does not inherit Lean status without checked bridges.
3. Exact finite computation does not prove a universal theorem.
4. Graph-level existential statements do not preserve fixed flow, lift, or surface data.
5. Failure for one fixed flow is not failure for the graph.
6. Same-embedding compression is not arbitrary cover existence on a prescribed surface.
7. Local triangular conservation does not imply zero global dual holonomy.
8. The old-colour quotient is not the full dual.
9. Current-best inclusion, Director acceptance, independent audit, Lean verification, manuscript approval, peer review, publication, release, and DOI status are separate axes.
