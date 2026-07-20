# Formalization and reliability boundary

This file separates current mathematical inclusion, authorial proof completion, independent audit, machine verification, manuscript projection, peer review, publication, release, arXiv, DOI, and novelty status.

## 1. Programme A complete theorem

Programme A proves at authorial paper-proof level:

> Every multigraph with finite active edge set and no singleton cut has a finite circuit double cover.

Exact Programme A source:

`proof-development/affine-cdc-rigour-v1@8bee16780b549f51e1f29343671a059961ec4172`.

Fixed Audit A candidate:

`curation/affine-cdc-programme-a-v1@68715fb29bb4b6555e2bc3e089603c5390d01566`.

Programme B descendants do not modify that branch or change its audit status.

## 2. Programme B1 status

Exact immutable B1 source:

`proof-development/affine-cdc-rigour-v1@778b09ac8260192e022f512f24cdef1d04871f37`.

Integrated B1 scope includes:

- root-flow/$K_5$-triangle equivalence;
- exact matching/four-flow theorem;
- fixed-flow/fixed-plane criterion;
- root-lift/surface and fixed-lift scope;
- prescribed-dual holonomy;
- old-colour quotient factorability;
- even-halfcube parity correction.

B1 is Curator-integrated authorial proof-development mathematics. It is not independently audited or machine-checked end to end.

## 3. Programme B2 status

Exact immutable B2 source:

`proof-development/affine-cdc-rigour-v1@d62974704d6dac77aaa00275a595fedf7f70cfd2`.

Integrated B2 units:

- B2.1 anisotropic, singular, quadratic, and Schur hierarchy: `COMPLETE-DRAFT`;
- B2.2 cographic cycle-continuity: `COMPLETE-DRAFT / TERMINOLOGY-BOUNDARY`;
- B2.3 orthogonal root-module correction: `COMPLETE-DRAFT / MATHEMATICAL-CORRECTION`;
- B2.4 stress/Fourier duality: `COMPLETE-DRAFT / WITNESS-SCOPE`;
- B2 aggregate: Curator-integrated authorial formulation/witness layer.

The preferred integrated chapter is [`five-support/b2-formulation-and-witness-hierarchy.md`](five-support/b2-formulation-and-witness-hierarchy.md). Exact provenance is in [`PROGRAMME_B2_INTEGRATION_MAP.md`](PROGRAMME_B2_INTEGRATION_MAP.md).

## 4. B2 theorem boundary

Complete graph-level witness equivalences:

- five indexed even supports;
- $R_5$-valued flows;
- $K_5$-triangle labellings;
- anisotropic $O^-(4,2)$ flows;
- complete quadratic cycle solutions $(b,d,x,y)$;
- exactly defined cographic cycle-continuous edge maps to $M^*(K_5)$.

Complete fixed-data equivalences, only with the quotient data and lift torsor retained:

- singular-line anisotropic lifting;
- component lift-defect vanishing;
- fixed-plane colour-cut obstruction;
- existence of the eliminated cycle word $d$;
- the Schur quotient condition.

Exact dual/counting results:

- Fredholm duality via relative stresses for a prescribed target;
- finite Fourier counting for a fixed affine orbit and allowed set.

Stress and Fourier data do not by themselves constitute graph-level source witnesses.

## 5. Mathematical correction status

The recovered packet

`FIVE_CDC_UNIVERSAL_ORTHOGONAL_ROOT_LIFT_V1.md`

is classified as:

`RETIRED / SUPERSEDED / FALSE THEOREM / HISTORICAL PROVENANCE`.

It is not part of the active theorem family.

The defects are mathematical, not merely expository:

1. its displayed evaluation map is type-invalid without an added self-duality;
2. the asserted universal $2r$-dimensional additive-root model is impossible for $r\ge4$.

The controlling replacement proves:

$$
\dim V\ge q-2
$$

for additive anisotropic roots of $K_q$ with triangle addition, and constructs the deleted permutation module of dimension $q-2$.

The eight-support $O^+(6,2)$ model remains valid and is exceptional. The five-support $O^-(4,2)$ model remains valid. No universal $O^+(2r,2)$ tower is asserted.

## 6. Machine-checked anchor

The companion checkpoint

`Yuren-Tang/affine-cdc:main@ebd7098a7a8b824e8c0a511d3c71f61705672aa8`

machine-checks substantial internal slices of the rank-three AffineCDC machinery.

It does not end-to-end verify Programme A, B1, or B2. In particular, this intake does not claim Lean verification of:

- the B2 quadratic/cographic equivalence package;
- the singular/Schur fixed-data reconstruction;
- the $q-2$ dimension lower bound or deleted permutation module;
- the stress/Fourier witness-scope statements.

No Lean repository was changed.

## 7. Independent-review status

Programme A remains fixed for Audit A. Programme B1 and B2 have not received dedicated independent line-by-line audits.

Priority B2 review targets include:

1. the coordinate isomorphism $\Phi$ and edgewise anisotropy equation;
2. the singular fibre multiplicities and lift-torsor reconstruction;
3. contraction to $Q_b$ and the Schur boundary equivalence;
4. the exact inverse-cycle convention for the cographic edge map;
5. the Gram-rank proof of the $q-2$ lower bound;
6. descent and nondegeneracy properties of the deleted permutation quadratic module;
7. Fredholm transpose identifications and endpoint-choice independence;
8. Fourier normalization, product factorization, and primal-witness recovery.

These are assurance targets, not known defects.

## 8. B3+ exclusion

This intake consumes no B3, B4, B5, or later moving-branch mathematics. It does not disposition target-capacity corrections, reconfiguration, cut/routing, defect, atom, or localization claims.

The global five-support theorem remains open.

## 9. Current source surfaces

Programme A:

- [`complete-cdc/`](complete-cdc/);
- [`PROGRAMME_A_INTEGRATION_MAP.md`](PROGRAMME_A_INTEGRATION_MAP.md);
- exact A0–A10 dossiers under `proof-development/`.

Programme B1:

- [`five-support/b1-object-quantifier-and-scope.md`](five-support/b1-object-quantifier-and-scope.md);
- [`PROGRAMME_B1_INTEGRATION_MAP.md`](PROGRAMME_B1_INTEGRATION_MAP.md);
- exact B1 dossiers under `proof-development/`.

Programme B2:

- [`five-support/b2-formulation-and-witness-hierarchy.md`](five-support/b2-formulation-and-witness-hierarchy.md);
- [`PROGRAMME_B2_INTEGRATION_MAP.md`](PROGRAMME_B2_INTEGRATION_MAP.md);
- [`PROGRAMME_B2_WITNESS_SCOPE.md`](PROGRAMME_B2_WITNESS_SCOPE.md);
- exact B2 dossiers under `proof-development/`.

## 10. Publication and release status

This intake did not:

- edit or approve a manuscript;
- establish literature novelty;
- authorize arXiv or journal submission;
- create a release or tag;
- modify a DOI or Zenodo record;
- implement a timestamp or priority-attestation workflow.

## 11. Reliability rules

1. Curator integration does not equal independent audit.
2. Natural reformulation does not inherit Lean status without checked bridges.
3. Exact finite computation does not prove a universal theorem.
4. Graph-level witnesses and fixed-data solvability criteria must not be conflated.
5. A quotient boundary word does not reconstruct the eliminated lift coordinate.
6. Relative stresses are dual dependencies, not source witnesses.
7. Positive Fourier count proves existence but does not exhibit a primal lift.
8. Zero Fourier count need not produce one separating stress.
9. The false universal orthogonal theorem may not be cited as active mathematics.
10. Current-best inclusion, Director acceptance, independent audit, Lean verification, manuscript approval, peer review, publication, release, arXiv, DOI, novelty, and timestamp status are separate axes.
