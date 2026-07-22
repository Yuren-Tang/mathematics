# AC-PD-B2.3 — additive root-module correction and source-fidelity repair

**Proof-development state:** `COMPLETE-DRAFT / MATHEMATICAL-CORRECTION / SOURCE-FIDELITY-REPAIRED`  
**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Exact initial corpus base:** `main@960c92b7ff231c78b387894149779083060a75eb`  
**Controlling repair intake:** `Yuren-Tang/research-workbench#37`, comment `5028845743`  
**Source-audit trigger:** `AC-AUDIT-B@110f014c551d4ce0f109ca5559d234ddb124d8f1`  
**Corrected attribution:** `SOURCE-UNRECONSTRUCTED / INFERRED-EXTRAPOLATION`; not a theorem of `FIVE_CDC_UNIVERSAL_ORTHOGONAL_ROOT_LIFT_V1.md`  
**Valid recovered packet:** `research/affine-cdc-five-cdc-v1@dad218dd18ed05d1b7cb730c2dc2431b4db5ec9c:projects/affine-cdc/research/FIVE_CDC_UNIVERSAL_ORTHOGONAL_ROOT_LIFT_V1.md`, blob `2043ada9d28789ecc5f4f0028e62133f37835bc1`, introduced by `a172b2acb13fc0b042ecb099a08b9631ab1db59a`  
**Depends on:** B1.1 and elementary quadratic linear algebra  
**Immediate consumers:** B2 orthogonal hierarchy; B8 assurance/source classification; Curator correction cycle  
**External mathematical inputs:** none

## 0. Corrected result and attribution boundary

This unit proves a sharp mathematical obstruction to the following **source-unreconstructed extrapolated claim**:

> for every `r`, all unordered pairs of the `2^r` points of
> `Γ=F_2^r` admit an additive anisotropic-root representation in a canonical
> quadratic space of dimension `2r`, informally written as
> `Γ⊕Γ*`, with a purported formula `d_h(a)=([a],ev_a)`, and forming a universal
> `O^+(2r,2)` tower.

No exact committed theorem source for that claim was found in the bounded source search recorded in §1. In particular, it is **not** contained in the named packet `FIVE_CDC_UNIVERSAL_ORTHOGONAL_ROOT_LIFT_V1.md`. The earlier wording of this dossier, the B2 map, and the original B2 Curator handoff incorrectly charged that valid rank-three packet with a different proposition.

The mathematical correction remains valid and unchanged:

1. the displayed formula is not canonically type-correct, because `a∈Γ` determines an element of `Γ**`, not of `Γ*`, absent an additional chosen self-duality;
2. more decisively, every additive anisotropic representation of `K_q` with the triangle law has ambient dimension at least `q-2`;
3. for `q=2^r`, a `2r`-dimensional model is impossible for every `r≥4`;
4. the correct universal additive root module is the deleted permutation module of dimension `q-2`;
5. rank three is exceptional because `2^3-2=6=2·3`.

The correction therefore targets an **inferred hierarchy or uncommitted draft**, not the recovered packet. This is a source/provenance repair, not a weakening of the `q-2` theorem or deleted permutation module.

## 1. Bounded source-forensics result

### 1.1 Exact search population

The search covered the complete committed AffineCDC source boundary relevant to the claim:

- the historical canonical/rank-hierarchy line through `main@960c92b7ff231c78b387894149779083060a75eb`, including the all-rank transgression and dual-Fano residue chapter introduced by `79e6a7ae12293c06f853e1b4f0291ea88d99a88e`;
- the complete five-support source interval from `main@749e0579581fcc838685138b3582f4de306b8e72` to `research/affine-cdc-five-cdc-v1@dad218dd18ed05d1b7cb730c2dc2431b4db5ec9c`, consisting of eighty-two source commits and seventy-eight packet files;
- the exact named packet blob `2043ada9d28789ecc5f4f0028e62133f37835bc1` and its introducing commit `a172b2acb13fc0b042ecb099a08b9631ab1db59a`;
- all plausible orthogonal, anisotropic, singular-quotient, root-flow, rank-four, universal-module, and rank-hierarchy packets identified by the source inventory;
- the Programme B2 authorial dossiers, B2 map and handoff, B8 assurance ledger, fixed Curator candidate, and Audit B claim/source ledgers;
- repository-history searches for the distinctive signatures `Γ⊕Γ*`, `d_h(a)`, `ev_a`, `2r`, `O^+(2r,2)`, “universal orthogonal”, “root module”, “rank hierarchy”, and semantically equivalent complete-graph root claims.

### 1.2 What the exact named packet proves

The named packet fixes `Γ=F_2^3` and proves:

- the even-weight eight-coordinate module `H_8`;
- the extended-Hamming kernel and moment map `μ:H_8→Γ`;
- the quotient `V_8=H_8/⟨1⟩`, a six-dimensional plus-type quadratic space;
- the Hamming Lagrangian and the exact sequence `0→L→V_8→Γ→0`;
- the twenty-eight weight-two roots as the anisotropic vectors of `O^+(6,2)`;
- the equivalence between compatible rank-three AffineCDC families and anisotropic root lifts;
- five-coordinate subspaces, their ten roots, four-dimensional minus-type geometry `O^-(4,2)`, and omitted-triple orthogonality.

It contains no arbitrary-rank `Γ⊕Γ*` model, no formula `d_h(a)=([a],ev_a)`, and no universal `O^+(2r,2)` tower.

### 1.3 What the genuine all-rank hierarchy proves

The historical all-rank transgression/residue line proves support-polynomial, degree-lowering Fano transgression, affine level-set, parity, stress, and dual-residue identities for `Γ=F_2^r`. It explicitly identifies rank three as the unique balanced quadratic-Lagrangian point. It does not encode all pairs of `2^r` support indices as anisotropic roots in dimension `2r`.

Thus “all-rank hierarchy” and “universal complete-root orthogonal tower” are different claims. Conflating them explains the inferred extrapolation but does not provide a source for it.

### 1.4 Source conclusion

No exact committed source of the arbitrary-rank tower was recovered within the complete boundary above. The first committed text located that displays the formula while treating it as a prior theorem is the Programme B2.3 correction layer itself, preserved in the original B2 checkpoint `d62974704d6dac77aaa00275a595fedf7f70cfd2`; no earlier theorem-bearing commit, path, or blob was found.

Accordingly the exact source classification is:

`SOURCE-UNRECONSTRUCTED / INFERRED-EXTRAPOLATION OR UNCOMMITTED DRAFT / MATHEMATICALLY REFUTED BY B2.3`.

This is not `BLOCKED-SOURCE`, because the controlling intake explicitly permits this classification when no committed source exists and the mathematical correction is self-contained.

## 2. Abstract additive root representation

Let `I` be a finite set of cardinality `q≥3`. An **additive root representation** of the complete graph on `I` in a quadratic space `(V,Q)` is a map

\[
r:\binom I2\longrightarrow V
\]

such that:

1. every root is anisotropic, `Q(r_{ab})=1`;
2. every target triangle satisfies
   \[
   r_{ab}+r_{bc}+r_{ca}=0
   \]
   for distinct `a,b,c∈I`.

This is exactly the structure needed to turn local `K_I` triangles into vector-flow conservation by edgewise root addition.

## 3. Triangle relations force point potentials

Fix a base point `0∈I` and define

\[
p_0=0,
\qquad
p_a=r_{0a}\quad(a\ne0).
\]

### Lemma 3.1

For every distinct `a,b∈I`,

\[
\boxed{r_{ab}=p_a+p_b.}
\]

### Proof

Apply the triangle relation to `0,a,b`:

\[
r_{0a}+r_{ab}+r_{b0}=0.
\]

Since the edge is unordered, `r_{b0}=r_{0b}`, giving the formula. ∎

Thus every additive root representation is a difference representation of `q` point potentials.

## 4. Sharp dimension lower bound

Let `B` be the polar form of `Q`. For `a≠0`,

\[
Q(p_a)=Q(r_{0a})=1.
\]

For distinct nonzero `a,b`,

\[
1=Q(r_{ab})=Q(p_a+p_b)
=Q(p_a)+Q(p_b)+B(p_a,p_b)
=B(p_a,p_b).
\]

Therefore the Gram matrix of the `q-1` vectors `(p_a)_{a≠0}` is

\[
A=J+I,
\]

with zero diagonal and one in every off-diagonal entry.

### Lemma 4.1 — rank of the off-diagonal matrix

If `q` is even, then

\[
\operatorname{rank}_{F_2}(J+I)=q-2.
\]

### Proof

Put `n=q-1`, which is odd. For `x∈F_2^n`,

\[
(J+I)x=(\sum_i x_i)\mathbf1+x.
\]

The kernel consists exactly of `0` and `1`, so it is one-dimensional and the rank is `n-1=q-2`. ∎

### Theorem 4.2 — additive root dimension bound

For even `q`, every additive root representation of `K_q` satisfies

\[
\boxed{\dim V\ge q-2.}
\]

### Proof

The rank of a Gram matrix of vectors in `V` cannot exceed `dim V`. Apply Lemma 4.1. ∎

### Corollary 4.3 — impossibility of a universal `2r` tower

For `q=2^r`, a `2r`-dimensional additive root representation can exist only if

\[
2r\ge2^r-2.
\]

This fails for every `r≥4`; already `8<14` when `r=4`. Hence no reformulation of the source-unreconstructed extrapolation can satisfy the required triangle-addition law in dimension `2r` for all ranks.

## 5. The correct deleted permutation module

Let `I` have even cardinality `q=2^r`, `r≥2`. In `F_2^I`, define

\[
E_I=\{z:\sum_{i∈I}z_i=0\},
\qquad
\overline E_I=E_I/\langle\mathbf1_I\rangle.
\]

Then

\[
\dim\overline E_I=q-2.
\]

For an even-weight representative `z`, define

\[
q_I([z])=\frac{\operatorname{wt}(z)}2\pmod2.
\]

### Lemma 5.1 — descent

The function `q_I` is a well-defined quadratic form on `\overline E_I`.

### Proof

The all-one word lies in the radical of the dot product on `E_I`. Replacing `z` by `z+1_I` complements its support, and

\[
q_I(z+\mathbf1_I)-q_I(z)
=\frac q2-\operatorname{wt}(z)\pmod2=0
\]

because `q/2` and `wt(z)` are even for `r≥2`. ∎

### Proposition 5.2 — canonical complete-graph roots

For distinct `a,b∈I`, put

\[
\rho_{ab}=[\varepsilon_a+\varepsilon_b]\in\overline E_I.
\]

Then:

1. `q_I(ρ_{ab})=1`;
2. `ρ_{ab}+ρ_{bc}+ρ_{ca}=0` for distinct `a,b,c`;
3. the roots span `\overline E_I`;
4. the dimension `q-2` attains Theorem 4.2's lower bound.

### Proof

The representative has weight two, giving anisotropy. The triangle sum cancels every coordinate twice. Basis differences span the even-weight subspace, and quotienting by `1_I` gives the claimed span. ∎

This is the correct universal additive root module for the complete graph on `2^r` support indices.

## 6. Exceptional rank three and five supports

For `q=8`,

\[
\dim\overline E_I=6=2r.
\]

The quadratic space is the plus-type six-space `O^+(6,2)`, and its twenty-eight anisotropic vectors are exactly the twenty-eight complete-graph roots. This is the exact rank-three/eight-support model proved by the historical packet.

For five support indices, the even-weight space

\[
H_5=\{z∈F_2^5:\sum z_i=0\}
\]

has dimension four. Its ten weight-two roots are the anisotropic orbit of `O^-(4,2)`. The five-support problem is therefore the exceptional orthogonal reduction

\[
O^+(6,2)\text{ root flow}
\rightsquigarrow
O^-(4,2)\text{ root flow},
\]

not the first step of a universal `O^+(2r,2)` tower.

## 7. Restored provenance of the named packet

The packet `FIVE_CDC_UNIVERSAL_ORTHOGONAL_ROOT_LIFT_V1.md` must be retained as a valid theorem-level historical source in its exact scope:

1. `H_8`, the Hamming kernel, moment map, and six-dimensional quotient;
2. rank-three AffineCDC root-lift equivalence;
3. the `O^+(6,2)` anisotropic complete-root realization;
4. five-coordinate `O^-(4,2)` slices and their singular extensions;
5. omitted-triple anisotropic-plane orthogonality;
6. the exact eight-to-five orthogonal compression formulation.

It must **not** be classified in toto as `FALSE THEOREM / HISTORICAL ONLY`, and its valid conclusions must not be prohibited from citation.

The separate source-unreconstructed extrapolation is classified as mathematically false by Theorem 4.2 and Proposition 5.2. These two classifications must remain separate.

## 8. Corrected consequences for the proof DAG

- B2.3 remains complete as a mathematical correction.
- The `q-2` lower bound and deleted permutation module remain controlling and unchanged.
- The named historical packet is restored as valid rank-three/eight-support and five-slice provenance.
- No committed parent theorem for the arbitrary-rank tower is asserted.
- The genuine all-rank transgression/residue hierarchy remains valid in its own support-polynomial and stress-residue scope.
- Any hoped-for higher-rank small-dimensional complete-root model is a new research question.
- The global five-support theorem remains open and no B9 frontier obligation changes.

## 9. Required Curator propagation repair

A replacement candidate must correct every propagated statement that:

1. attributes `Γ⊕Γ*`, `d_h(a)=([a],ev_a)`, or a universal `O^+(2r,2)` tower to the named packet;
2. classifies that packet in toto as false, superseded, or history-only;
3. suppresses its valid rank-three/eight-support or five-slice source role;
4. presents the exhaustive seventy-eight-packet disposition as source-faithful while retaining that misclassification;
5. computes the source-class partition from the misclassified packet.

The complete propagation matrix and exact destination list are supplied in `AC_PD_B2_3_SOURCE_FIDELITY_REPAIR.md` and the dedicated Curator handoff.

## 10. Completion assessment

`AC-PD-B2.3` is

`COMPLETE-DRAFT / MATHEMATICAL-CORRECTION / SOURCE-FIDELITY-REPAIRED`.

The repair changes provenance and supersession classification only. It does not modify the fixed candidate, audit branch, Curator branch, `main`, public issue #2, Lean, manuscript, release, publication, arXiv, DOI, tag, or Research Lead surfaces.