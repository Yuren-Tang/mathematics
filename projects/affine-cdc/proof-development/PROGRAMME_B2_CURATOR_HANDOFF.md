# CURATION-HANDOFF — AffineCDC Programme B2

**Project:** AffineCDC  
**Prepared by:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Authority basis:** research-workbench issue #37; persistent proof-development policy; AC-PDL charter  
**Live source branch:** `Yuren-Tang/mathematics:proof-development/affine-cdc-rigour-v1`  
**Immutable source checkpoint SHA:** `d62974704d6dac77aaa00275a595fedf7f70cfd2`  
**Included packet/file range:** `AC_PD_B2_1_*.md` through `AC_PD_B2_4_*.md`, `AC_PD_B2_FORMULATION_AND_WITNESS_MAP.md`, and `OBLIGATION_DAG.md` at the immutable checkpoint  
**Controlling canonical base:** `Yuren-Tang/mathematics:main@960c92b7ff231c78b387894149779083060a75eb`  
**Packet classification:** `PROOF-DEVELOPMENT / PROGRAMME-B2 / READY-FOR-CURATOR / MATHEMATICAL-CORRECTION`  
**Mathematical completeness:** complete for the formulation/witness hierarchy and the stated correction  
**Independent-review state:** not independently audited  
**Live branch may continue beyond checkpoint:** yes; all B3+ commits are excluded unless separately handed off  
**Staging authorized:** yes, on a dedicated Curator branch only  
**Merge/default-branch authority:** no

## 1. Intake objective

Integrate the exact witness hierarchy across anisotropic, singular, quadratic, Schur, cographic, stress, and Fourier formulations, and remove a false universal orthogonal-root theorem from the active theorem layer.

This intake has two inseparable parts:

1. positive theorem integration;
2. explicit mathematical correction and supersession.

## 2. Accepted theorem package

The packet proves the full graph-level equivalence among:

- five indexed even supports;
- $R_5$ root flows;
- $K_5$ triangle labellings;
- anisotropic flows in $O^-(4,2)$;
- cycle-word solutions of
  $$
  b*d=(\mathbf1+x)*(\mathbf1+y);
  $$
- cycle-continuous edge maps $M(G)\to M^*(K_5)$.

It also proves the fixed-data equivalence among:

- anisotropic lift through a singular line;
- vanishing component lift defect;
- fixed-plane colour-cut obstruction;
- existence of the eliminated cycle word $d$;
- Schur quotient condition $x*y\in\mathcal C(Q_b)$.

Finally it proves:

- exact prescribed-value Fredholm duality via relative stresses;
- exact Fourier counting of nonlinear allowed-set intersections;
- the distinction between a positive count and an exhibited primal witness.

## 3. Mandatory mathematical correction

The recovered packet `FIVE_CDC_UNIVERSAL_ORTHOGONAL_ROOT_LIFT_V1.md` contains a false theorem.

### Defects

1. Its displayed map uses `ev_a` as an element of $\Gamma^*$ for $a\in\Gamma$, which is not canonical and is type-invalid without an added self-duality.
2. No alternative $2r$-dimensional model can satisfy the asserted complete-graph triangle-addition laws for $r\geq4$.

### Proved obstruction

Any additive anisotropic-root representation of $K_q$ with

$$
r_{ab}+r_{bc}+r_{ca}=0
$$

has ambient dimension at least $q-2$. The proof reduces to the rank $q-2$ Gram matrix $J+I$.

Thus for $q=2^r$ the claimed dimension $2r$ is impossible from $r=4$ onward.

### Correct replacement

The universal module is the deleted permutation module

$$
\overline E_I
=
\left\{z\in\mathbf F_2^I:\sum_i z_i=0\right\}/\langle\mathbf1_I\rangle,
$$

of dimension $q-2$, with quadratic form $q([z])=\operatorname{wt}(z)/2\pmod2$ and roots $[\varepsilon_a+\varepsilon_b]$.

The eight-support $O^+(6,2)$ model is exceptional because $8-2=6$. It is not the first member of a universal $O^+(2r,2)$ hierarchy.

### Required classification

The affected recovered packet must remain only as historical provenance marked `SUPERSEDED / FALSE THEOREM`. It must not remain in the active theorem family with softened wording.

## 4. Witness-scope corrections

The Curator must preserve these distinctions.

- Singular quotient and Schur data are full fixed-data criteria only when the quotient flow, plane/kernel, quotient graph, and lift torsor are retained.
- A Schur boundary word alone does not reconstruct a five-support witness.
- “Cycle-continuous edge map” must be defined; no strong-map or embedding property is implied.
- Relative stresses are dual linear dependencies, not source witnesses.
- Fourier gives an exact count over a fixed affine orbit. A zero count usually yields aggregate spectral cancellation, not automatically one separating stress.
- A positive count proves existence but an explicit lift still needs a codeword and primal preimage.

## 5. Recommended destinations

Stage coherent edits to:

- `five-support/equivalent-formulations-and-proof-families.md`;
- `five-support/singular-quotient-lifting.md`;
- the active quadratic/Schur/cographic/orthogonal/Fourier chapters or sections identified by current corpus structure;
- `THEOREM_DEPENDENCY_MAP.md`;
- `MATHEMATICAL_ARCHITECTURE.md`;
- `CHAPTER_PROVENANCE.md` and retired/superseded classification records;
- proof-development provenance retaining all B2 dossiers.

Any later packet citing the false universal hierarchy must be re-audited before integration.

## 6. Exclusions

- no global five-support theorem;
- no B3+ target, reconfiguration, separator, or frontier material;
- no promotion of finite Fourier enumerators to uniform estimates;
- no formal-verification claim;
- no literature novelty claim;
- no `main`, release, manuscript, DOI, or publication action.

## 7. Curator success test

The intake succeeds when:

1. the immutable SHA remains the consumed source;
2. the complete-witness and fixed-data/dual layers are visibly separated;
3. every positive equivalence arrow has an exact reconstruction map;
4. the false $2r$ theorem is removed from the active theorem layer and marked superseded;
5. the $q-2$ lower bound and deleted permutation module replace it;
6. rank-three/eight-support exceptionality is explicit;
7. stress and Fourier witness scope is exact;
8. no B3+ delta is consumed;
9. any newly found mathematical defect returns to AC-PDL as a repair unit.

## 8. Stop conditions

Return rather than guess if integration reveals a later theorem depending essentially on the false hierarchy, an unrecorded self-duality choice, a dimension-specific orthogonal claim not covered by B2.3, a mismatch between cycle-continuity conventions, or a need to consume later branch commits.

Staging is authorized; canonical movement is not.