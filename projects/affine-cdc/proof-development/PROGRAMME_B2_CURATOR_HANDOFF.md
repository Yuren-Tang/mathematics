# CURATION-HANDOFF — AffineCDC Programme B2

**Project:** AffineCDC  
**Prepared by:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Authority basis:** research-workbench issue #37; persistent proof-development policy; AC-PDL charter; source-fidelity repair intake comment `5028845743`  
**Live source branch:** `Yuren-Tang/mathematics:proof-development/affine-cdc-rigour-v1`  
**Original immutable B2 checkpoint:** `d62974704d6dac77aaa00275a595fedf7f70cfd2`  
**Current controlling source:** the later source-fidelity repair checkpoint named by the dedicated B2/B8 Curator handoff  
**Included range:** B2.1–B2.4, `AC_PD_B2_FORMULATION_AND_WITNESS_MAP.md`, `AC_PD_B2_3_SOURCE_FIDELITY_REPAIR.md`, and the corrected DAG  
**Controlling canonical base:** `Yuren-Tang/mathematics:main@960c92b7ff231c78b387894149779083060a75eb`  
**Packet classification:** `PROOF-DEVELOPMENT / PROGRAMME-B2 / READY-FOR-CURATOR / MATHEMATICAL-CORRECTION / SOURCE-FIDELITY-REPAIRED`  
**Mathematical completeness:** complete for the formulation/witness hierarchy and additive-root correction  
**Independent-review state:** Audit B verified the theorem layer but found the repaired source-fidelity defect; this authorial checkpoint awaits bounded B2/B8 re-audit after Curator replacement  
**Live branch may continue:** yes  
**Staging authority:** dedicated Curator branch only after AC-DIR branch/base supplement  
**Merge/default-branch authority:** none

## 1. Intake objective

Integrate the exact witness hierarchy across anisotropic, singular, quadratic, Schur, cographic, stress, and Fourier formulations; retain the sharp additive-root correction; and repair the historical-source classification found defective by Audit B.

The intake has three inseparable parts:

1. positive theorem integration;
2. mathematical refutation of the source-unreconstructed arbitrary-rank extrapolation;
3. restoration of the named historical packet's valid rank-three/eight-support and five-slice provenance.

## 2. Accepted theorem package

The packet proves the graph-level equivalence among:

- five indexed even supports;
- `R_5` root flows;
- `K_5` triangle labellings;
- anisotropic flows in `O^-(4,2)`;
- cycle-word solutions of
  \[
  b*d=(\mathbf1+x)*(\mathbf1+y);
  \]
- cycle-continuous edge maps `M(G)→M^*(K_5)`.

It also proves the fixed-data equivalence among:

- anisotropic lift through a singular line;
- vanishing component lift defect;
- fixed-plane colour-cut obstruction;
- existence of the eliminated cycle word `d`;
- Schur quotient condition `x*y∈C(Q_b)`.

Finally it proves:

- exact prescribed-value Fredholm duality via relative stresses;
- exact Fourier counting of nonlinear allowed-set intersections;
- the distinction between a positive count and an exhibited primal witness.

These theorem and witness-scope results are unchanged by the source repair.

## 3. Mathematical correction retained

For an additive anisotropic-root representation of `K_q` satisfying

\[
r_{ab}+r_{bc}+r_{ca}=0,
\]

point potentials give `r_{ab}=p_a+p_b`, and the Gram matrix of the `q-1` nonbase potentials is `J+I`, of rank `q-2`. Hence

\[
\boxed{\dim V\ge q-2.}
\]

For `q=2^r`, dimension `2r` is impossible for every `r≥4`.

The correct universal module is

\[
\overline E_I
=
\{z∈F_2^I:\sum_i z_i=0\}/\langle\mathbf1_I\rangle,
\]

of dimension `q-2`, with quadratic form `q([z])=wt(z)/2 mod 2` and roots `[ε_a+ε_b]`.

Eight supports are exceptional because `8-2=6=2·3`.

## 4. Source-fidelity correction

### 4.1 Attribution retracted

No exact committed source was found for the arbitrary-rank claim described by

\[
V=\Gamma\oplus\Gamma^*,
\qquad
d_h(a)=([a],\operatorname{ev}_a),
\qquad
O^+(2r,2).
\]

It must be classified as:

`SOURCE-UNRECONSTRUCTED / INFERRED-EXTRAPOLATION OR UNCOMMITTED DRAFT`.

It must not be attributed to `FIVE_CDC_UNIVERSAL_ORTHOGONAL_ROOT_LIFT_V1.md`.

### 4.2 Valid packet restored

The exact historical packet at blob `2043ada9d28789ecc5f4f0028e62133f37835bc1`, introduced by `a172b2acb13fc0b042ecb099a08b9631ab1db59a`, is valid provenance for:

- the even-weight `H_8` module on `F_2^3`;
- the Hamming kernel and moment map;
- the Hamming Lagrangian quotient;
- the plus-type six-space `O^+(6,2)`;
- its twenty-eight anisotropic roots;
- rank-three AffineCDC compatible root lifts;
- five-coordinate `O^-(4,2)` slices and omitted-triple orthogonality.

The packet is not to be classified in toto as `SUPERSEDED / FALSE THEOREM / HISTORICAL ONLY`.

### 4.3 Genuine all-rank hierarchy retained separately

The historical all-rank transgression and dual-Fano residue chapter remains valid for support-polynomial, Fano transgression, level-set, parity, stress, and residue identities. It explicitly distinguishes higher rank from the unique rank-three quadratic-Lagrangian case. It is not a parent theorem for the false complete-root tower.

## 5. Exact search and propagation ledger

The complete source boundary, exact inspected refs, source conclusion, and downstream propagation matrix are in:

`projects/affine-cdc/proof-development/AC_PD_B2_3_SOURCE_FIDELITY_REPAIR.md`.

The search covered the historical rank-hierarchy line, all eighty-two commits and seventy-eight five-support packets in the fixed source interval, the exact named packet blob and introducing commit, all plausible orthogonal/root/rank packets, the original PDL/Curator propagation, and Audit B's complete claim/source matrix.

## 6. Witness-scope requirements

Curator must preserve:

- singular quotient and Schur data as fixed-data criteria only when quotient flow, plane/kernel, quotient graph, and lift torsor are retained;
- a Schur boundary word as an obstruction projection, not a graph-level witness;
- “cycle-continuous edge map” with its exact inverse-cycle definition;
- relative stresses as dual dependencies, not source witnesses;
- Fourier as an exact count over a fixed affine orbit;
- positive count versus explicit lift reconstruction.

## 7. Required replacement-candidate edits

After AC-DIR issues the exact replacement branch/base supplement, Curator must correct:

1. the B2 formulation/witness chapter;
2. root-flow lifting and equivalent-proof-family chapters;
3. `CHAPTER_PROVENANCE.md`;
4. `MIGRATION_LEDGER.md`;
5. `RETIRED_SOURCE_CLASSIFICATION.md`;
6. `SUPERSESSION_MAP.md`;
7. `SOURCE_RECOVERY_AUDIT.md`;
8. any Programme B2 integration/final-audit map carrying the false attribution;
9. dependency, architecture, active-surface, current-best, formal-status, assurance, and unified status surfaces;
10. the seventy-eight-packet class partition.

The source-unreconstructed extrapolation is not one of the seventy-eight recovered packets and must not be counted as such. The named packet remains within the seventy-eight and must be classified according to its valid exact contents.

## 8. Exclusions

- no global five-support theorem;
- no change to B1 or B3–B9 mathematics;
- no promotion of finite Fourier enumerators to uniform estimates;
- no formal-verification or literature-novelty claim;
- no fixed candidate, audit branch, Curator branch, `main`, public issue #2, Research Lead, Lean, manuscript, release, publication, arXiv, DOI, or tag mutation.

## 9. Curator success test

The replacement intake succeeds when:

1. the exact authorial repair checkpoint remains recoverable;
2. the complete-witness and fixed-data/dual layers remain visibly separated;
3. every positive equivalence arrow retains its reconstruction map;
4. the false tower is attributed only to the source-unreconstructed extrapolation;
5. the `q-2` lower bound and deleted permutation module remain controlling;
6. the historical packet's exact valid roles are restored;
7. the all-rank transgression hierarchy remains distinct;
8. the seventy-eight-packet disposition and class equation are recomputed;
9. all propagated provenance/supersession/assurance surfaces agree;
10. the candidate returns for a narrowly bounded B2/B8 source-fidelity re-audit;
11. no B3+ or public/canonical surface is moved without separate authority.

## 10. Stop conditions

Return rather than guess if replacement integration reveals:

- a newly found exact committed source contradicting this classification;
- a later theorem depending essentially on the disputed `2r` tower;
- a dimension-specific orthogonal claim not covered by B2.3;
- a need to consume Research Lead or other unauthorized branch commits;
- an accounting ambiguity that cannot be resolved from the seventy-eight exact packets.

The PDL source repair itself is `READY-FOR-CURATOR`; staging and candidate creation remain subject to the pending AC-DIR supplement.