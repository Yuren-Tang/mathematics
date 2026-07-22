# AC-PD-B2 — formulation and witness hierarchy

**Proof-development state:** `READY-FOR-CURATOR / MATHEMATICAL-CORRECTION / SOURCE-FIDELITY-REPAIRED`  
**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Exact initial corpus base:** `main@960c92b7ff231c78b387894149779083060a75eb`  
**Constituent units:** B2.1–B2.4 plus B2.3 source-fidelity repair  
**External mathematical inputs:** none  
**Assurance:** complete authorial proofs for the stated equivalences and correction; source attribution repaired after Audit B; not independent audit and not formal verification

## 0. Purpose and corrected source boundary

Programme B2 classifies the singular, quadratic, Schur, cographic, orthogonal, stress, and Fourier descriptions by the amount of witness data they retain. It also refutes a source-unreconstructed extrapolated `2r`-dimensional orthogonal-root tower and replaces it with a sharp dimension bound and the correct deleted permutation module.

The extrapolated tower is **not** a theorem of `FIVE_CDC_UNIVERSAL_ORTHOGONAL_ROOT_LIFT_V1.md`. That exact packet is a valid source for the rank-three/eight-support `O^+(6,2)` model and five-coordinate `O^-(4,2)` slices. The complete source classification and search boundary are in `AC_PD_B2_3_SOURCE_FIDELITY_REPAIR.md`.

The central rule is:

> two formulations belong in one equivalence box only when their fixed data and reconstruction maps are explicit.

A quotient residue, boundary word, dual annihilator, or Fourier spectrum may decide a fixed solvability problem without itself being a graph-level five-support witness.

## 1. Complete graph-level witness equivalences

For a finite loopless cubic multigraph `G`, the following are equivalent.

1. An indexed five-support even double cover.
2. An `R_5`-valued flow in
   \[
   H_5=\{z\in F_2^5:\sum_i z_i=0\}.
   \]
3. A `K_5`-triangle edge labelling.
4. An anisotropic flow in the minus-type four-space `(H_5,q_5)`, where
   \[
   q_5(z)=\sum_{i<j}z_iz_j.
   \]
5. Cycle words `b,d,x,y∈C(G)` satisfying
   \[
   b*d=(\mathbf1+x)*(\mathbf1+y).
   \]
6. A cycle-continuous edge map
   \[
   M(G)\longrightarrow M^*(K_5),
   \]
   meaning an arbitrary ground-set map whose inverse image sends every target binary cycle, equivalently every cut of `K_5`, to a source binary cycle.

The reconstruction maps are explicit:

- supports are the five coordinate words;
- anisotropic values are exactly the weight-two roots;
- the coordinate isomorphism is
  \[
  \Phi(b,d,x,y)=(b,d,b+d+y,b+d+x,b+d+x+y);
  \]
- the cographic edge map records the unordered pair of support indices containing each source edge.

Thus

\[
\boxed{
\text{five supports}
\Longleftrightarrow R_5\text{-flow}
\Longleftrightarrow K_5\text{ triangles}
\Longleftrightarrow O^-(4,2)\text{ anisotropic flow}
\Longleftrightarrow \text{quadratic cycle solution}
\Longleftrightarrow M(G)\to M^*(K_5)\text{ cycle-continuous}.}
\]

No injectivity, strong-map, quotient, or matroid-embedding property is included in the last formulation.

## 2. Fixed singular-quotient solvability equivalences

Let `(H,q)` be a four-dimensional minus-type quadratic space, let `0≠k∈H` be singular, and put

\[
\Gamma=H/\langle k\rangle,
\qquad
W_k=k^\perp/\langle k\rangle.
\]

Fix a nowhere-zero Fano flow `f:E(G)→Γ\setminus{0}`. The following are equivalent.

1. `f` admits an anisotropic `H`-flow lift.
2. The component sums of the kernel-line lift defects vanish on every component of the plane subgraph `G_{W_k}`.
3. The corresponding fixed-plane forbidden-three-colour obstruction vanishes.
4. In coordinates `f=(b,x,y)`, there exists a cycle word `d` satisfying
   \[
   b*d=(\mathbf1+x)*(\mathbf1+y).
   \]
5. After contracting the `b=0` components, the Schur word satisfies
   \[
   x*y\in C(Q_b).
   \]

When nonempty, the anisotropic lift set is a torsor under `C(G_{W_k})`, and the coordinate `d`-solution set is the same torsor in one chart.

These are complete **fixed-data** equivalences only when the quotient flow, singular kernel line or plane, contracted quotient, and lift torsor are retained. The Schur boundary word alone is an obstruction projection, not a five-support witness.

## 3. One obstruction in four resolutions

For one fixed singular quotient, the following componentwise bits are identical.

1. The sum of vertex lift defects in the kernel line.
2. The forbidden-three-colour local-family obstruction.
3. The parity of one, hence every, outside colour on the plane-component cut.
4. The quotient boundary of the Schur product `x*y`.

Accordingly, singular, fixed-plane, and Schur arguments are invariant, local, and eliminated-coordinate resolutions of one incidence obstruction.

## 4. Stress duality

For the quotient differential

\[
\delta_f:\Gamma^{V(G)}\to\bigoplus_eQ_e,
\]

its transpose is the equilibrium-stress divergence operator

\[
(\delta_f^*\psi)_v=\sum_{e\ni v}\psi_e.
\]

For any selected vertex or fibre evaluation map, the orthogonal complement of its attainable image is exactly the space of relative stresses whose divergence is supported on the selected interface.

A prescribed target vector is attainable if and only if every relative stress annihilates its displacement from the base lift. When attainable, a primal preimage reconstructs the translated lift.

The stress space by itself records linear dependencies. It does not specify the base flow, base lift, target vector, or primal preimage and is therefore not a graph-level five-support witness.

## 5. Fourier duality

For a fibre-evaluation code `C_F≤Q_F` and an allowed set `A⊆Q_F`,

\[
|C_F\cap A|
=
\frac{|C_F|}{|Q_F|}
\sum_{y\in C_F^\perp}\widehat{\mathbf1_A}(y).
\]

The nonzero frequencies are precisely relative stresses. The zero frequency is the exact uniform main term; it is not an independence assumption.

This is an exact existence/counting criterion for one fixed orbit. If the count is zero, the complete spectrum gives a structured cancellation identity; a single separating stress need not exist for a nonlinear product set. A positive count proves existence, but a full witness still requires one codeword, a primal preimage, the fixed base lift, and root/support reconstruction.

Thus Fourier duality is a complete dual count, not an independent constructive equivalence.

## 6. Orthogonal correction with repaired provenance

### 6.1 Exact source classification

No committed source was found for the extrapolated arbitrary-rank claim

\[
V=\Gamma\oplus\Gamma^*,
\qquad
\dim V=2r,
\qquad
O^+(2r,2),
\]

or for the formula `d_h(a)=([a],ev_a)`. It is classified as

`SOURCE-UNRECONSTRUCTED / INFERRED-EXTRAPOLATION OR UNCOMMITTED DRAFT`.

The exact packet formerly blamed for it instead proves the valid rank-three/eight-support and five-slice theorems listed in §6.4.

### 6.2 Sharp lower bound

For any even set `I` of cardinality `q`, suppose roots `r_{ab}` satisfy

\[
Q(r_{ab})=1,
\qquad
r_{ab}+r_{bc}+r_{ca}=0.
\]

Fixing a base point gives `r_{ab}=p_a+p_b`. The Gram matrix of the `q-1` vectors `p_a` is `J+I`, of rank `q-2`. Hence

\[
\boxed{\dim V\ge q-2.}
\]

For `q=2^r`, dimension `2r` is impossible from `r=4` onward.

### 6.3 Correct universal module

The deleted permutation module

\[
\overline E_I
=
\{z\in F_2^I:\sum_i z_i=0\}/\langle\mathbf1_I\rangle
\]

has dimension `q-2` and quadratic form

\[
q_I([z])=\frac{\operatorname{wt}(z)}2\pmod2.
\]

The roots `[ε_a+ε_b]` are anisotropic and satisfy every triangle relation. This attains the lower bound.

### 6.4 Restored historical packet

`FIVE_CDC_UNIVERSAL_ORTHOGONAL_ROOT_LIFT_V1.md` remains valid provenance for:

- `H_8`, the Hamming kernel and moment map;
- the Hamming Lagrangian quotient;
- the exceptional six-dimensional plus space `O^+(6,2)`;
- its twenty-eight complete-graph roots;
- rank-three AffineCDC compatible root lifts;
- five-coordinate `O^-(4,2)` slices and singular extensions;
- omitted-triple orthogonality.

It is not classified in toto as a false theorem or history-only packet.

### 6.5 Exceptional dimensions

- Five supports use `O^-(4,2)`.
- Eight supports use `O^+(6,2)` because `8-2=6=2·3`.
- The eight-support realization is exceptional; it is not the first case of a universal `O^+(2r,2)` tower.

The source-unreconstructed extrapolation is mathematically refuted, while the named packet's exact theorems remain available.

## 7. Exact classification table

| Formulation | Scope | Retains full witness? | Reconstruction requirement |
|---|---|---:|---|
| five indexed supports | graph-level | yes | none |
| `R_5` root flow / `K_5` triangles | graph-level | yes | coordinate supports |
| anisotropic `O^-(4,2)` flow | graph-level | yes | identify roots with support pairs |
| quadratic equation `(b,d,x,y)` | graph-level | yes | apply `Φ` |
| cographic cycle-continuous edge map | graph-level | yes | target-star preimages |
| singular quotient | fixed flow and kernel line | no, until lifted | solve incidence equation and retain torsor |
| Schur quotient | fixed coordinate quotient | no, until lifted | solve for `d` |
| component obstruction | fixed quotient | no | incidence/`T`-join solve |
| relative stress space | fixed evaluation map | no | primal target and preimage |
| Fourier spectrum/count | fixed orbit and allowed set | existence/count only | exhibit codeword and preimage |
| deleted permutation root module | universal target model | target data, not source witness | choose root-valued source flow |
| historical `O^+(6,2)` packet | fixed rank-three/eight-index model | target and lift data | retain moment map and Hamming quotient |

## 8. Required corpus repair

Before a replacement candidate is accepted, Curator must:

1. preserve the complete-witness versus fixed-data/dual distinction;
2. retain anisotropic flow as the mother object and singular/Schur/stress/Fourier layers in their stated scopes;
3. replace the false packet attribution with the exact extrapolation classification;
4. retain the `q-2` lower bound and deleted permutation module;
5. restore the named packet's valid rank-three/eight-support and five-slice provenance;
6. recompute the seventy-eight-packet classification without counting the uncommitted extrapolation as a packet;
7. repair all migration, supersession, provenance, dependency, assurance, and status surfaces enumerated in `AC_PD_B2_3_SOURCE_FIDELITY_REPAIR.md`;
8. preserve finite evidence as evidence rather than universal estimates.

## 9. Remaining frontier

B2 does not prove that every bridgeless cubic graph has an anisotropic `O^-(4,2)` flow. It supplies exact equivalent witnesses, fixed-data lift criteria, dual obstruction languages, and the corrected universal target dimension.

The global unresolved step remains a source theorem guaranteeing successful data or eliminating all obstructions. B9 and the six AC-RL obligations remain unchanged.

## 10. Completion assessment

`AC-PD-B2` is

`READY-FOR-CURATOR / MATHEMATICAL-CORRECTION / SOURCE-FIDELITY-REPAIRED`.

No fixed candidate, audit, Curator, `main`, public issue #2, Lean, manuscript, release, publication, arXiv, DOI, tag, or Research Lead surface is modified by this authorial repair.