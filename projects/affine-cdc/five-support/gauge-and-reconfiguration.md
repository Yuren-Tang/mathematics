# Gauge torsors, partial Petrials, and connected flow reconfiguration

## 1. Two-level state space

For a finite loopless cubic multigraph `G`, a five-support state consists of a nowhere-zero Fano flow `f` together with a compatible root lift `g` above it.

There are two distinct motions.

1. **Vertical:** keep `f` fixed and move inside its compatible-lift fibre.
2. **Horizontal:** change `f` by one connected-cycle switch and solve or construct a lift in the new fibre.

A support-cycle pivot is a special horizontal edge with an explicit root-level lift. It is not a gauge move.

## 2. Exact vertical torsor

For fixed `f:E(G)\to\Gamma\setminus\{0\}`, define

$$
H_f^0=
\{k:V(G)\to\Gamma:
 k_u+k_v\in\langle f(e)\rangle
 \text{ for every }e=uv\}.
$$

For `k\in H_f^0`, endpoint translation defines another root lift `g^k`. Every labelled root lift above `f` is uniquely obtained this way.

### Theorem 2.1

The labelled root-lift fibre above `f` is a torsor under `H_f^0`.

If `\Lambda_f(k)=\lambda` is defined by

$$
k_u+k_v=\lambda_e f(e),
$$

then the gauge code is `\mathcal B_f=\operatorname{im}\Lambda_f`. On a disconnected graph,

$$
\mathcal B_f\cong H_f^0/\Gamma^{\pi_0(G)},
$$

where `\pi_0(G)` means edge-bearing components. The connected quotient `H_f^0/\Gamma` must not be applied unchanged to disconnected graphs.

## 3. Gauge / partial-Petrial correspondence

A gauge bit records whether the two support-face sides are exchanged across an edge.

### Theorem 3.1

For every admissible field `k`,

$$
S_{g^k}=S_g^{\tau(\operatorname{supp}\lambda(k))}.
$$

Thus `\mathcal B_f` is exactly the code of partial Petrials accessible while the projected Fano flow is fixed.

A vertical move preserves the source graph, edge objects, projected flow, local root equations, and exact edge double coverage. It may change the surface, face components, full dual, old-colour quotient, orientability, and both factorable and full-dual compressibility.

## 4. Connected horizontal switches

For a binary cycle word `z` and `0\ne a\in\Gamma`, put

$$
f^{z,a}=f+az.
$$

This is nowhere zero exactly when `\operatorname{supp}z` avoids the colour class `E_a=f^{-1}(a)`.

In a cubic graph, every connected component of a nonempty cycle-word support is a source circuit. If

$$
z=\mathbf1_{C_1}+\cdots+\mathbf1_{C_m},
$$

then switching the `C_i` in any order gives a commuting path of `m` nowhere-zero connected-cycle moves.

### Exact adjacency boundary

- `m=1`: one horizontal reconfiguration edge;
- `m>1`: a commuting path, not one edge.

Conversely, two exponent-two flows that agree outside one connected source cycle differ by one constant nonzero direction on that cycle.

## 5. Support-cycle pivots

Let `C` be one connected component of old support `F_c`. Suppose root `cd` is absent from `C`. Replacing each label `\{c,s_e\}` on `C` by `\{d,s_e\}` produces a compatible root lift of

$$
f+(c+d)\mathbf1_C.
$$

### Theorem 5.1

A support-cycle pivot:

- is one connected horizontal switch;
- preserves the uncoloured cycle-face embedding and full dual;
- recolours one face component;
- changes the projected flow and generally the old-colour quotient and gauge code.

Not every connected switch is directly pivotable above a prescribed old lift.

If `R_C` is the set of old roots whose every occurrence lies on `C` and `A_{C,d}` is the set of previously unused roots introduced on `C`, then

$$
U_{g'}=(U_g\cup R_C)\setminus A_{C,d}.
$$

This is an exact factorable-quotient update. The full dual remains unchanged by the bare pivot.

## 6. The new fibre is not transported

After a connected switch from `f` to `f'`, the edge-line constraints on the switched cycle change from `\langle f(e)\rangle` to `\langle f'(e)\rangle`.

There is no general invariance of

$$
\dim H_f^0,
\qquad
\mathcal B_f,
\qquad
\text{or the Petrial orbit}.
$$

A support pivot gives one distinguished lift above `f'`. The remainder of the new fibre must be solved from `H_{f'}^0`.

## 7. Internal fixed-plane correction

Fix `W=\ker b` and write `f=(b,x,y)`. For an internal direction `t\in W`, choose coordinates with `t` the `x`-direction. A switch word `z` gives

$$
f'=(b,x+z,y).
$$

The plane subgraph and quotient `Q_W` remain fixed, and

$$
d_W(f')+d_W(f)=\partial_{Q_W}(y*z).
$$

For all composite same-direction endpoints, the exact correction image is

$$
\operatorname{Im}\Delta^{\mathrm{comp}}_{W,t}
=
q_*\bigl(\mathsf B(R_1)\cap\mathsf B(R_0)\bigr)
=
\sigma_q\mathcal C(\mathscr I_{W,t}).
$$

The dual obstructions are fibre-constant cuts of the component-incidence graph.

### Connectedness correction

The connected-neighbour image is only the subset obtained from one connected source cycle. It need not be a vector subspace. The linear image classifies endpoints reachable by a commuting same-direction path.

## 8. External reslicing

For `t\notin W`, write

$$
f=(b,x,y),
\qquad
f'=(b+z,x,y).
$$

The Schur word `p=x*y` and zero matching `M=f^{-1}(t)` remain fixed, while the contracted quotient changes:

$$
d_W(f')=\partial_{Q_{b+z}}(p).
$$

As `z` ranges over all cycle words avoiding `M`, the composite endpoints correspond exactly to even supports `B'\supseteq M`. Such an endpoint is good precisely when

$$
|M\cap\delta_G(K)|\equiv0\pmod2
$$

for every component `K` of `G-B'`.

Again, one adjacency additionally requires `B+B'` to be one connected source cycle.

## 9. Exact motion table

| Motion | Projected flow | Uncoloured embedding | Fibre action |
|---|---|---|---|
| gauge / Petrial | fixed | may change | one `H_f^0` translation |
| support pivot | changes | fixed | one explicit lift in new fibre |
| general connected switch | changes | not canonically transported | solve new affine fibre |
| disconnected switch | sequence | sequence | commuting path through successive fibres |

## 10. Certificate boundary

In the thirty-vertex laboratory:

- `7737` counts all nonzero admissible pairs `(a,z)`;
- `2801` have connected support and are genuine one-edge neighbours;
- the remaining `4936` describe multi-component paths.

The corresponding outcome tables are different finite populations and retain their B8 assurance class. Fibre ranks, surface counts, and neighbour success counts are not universal motion invariants.

## 11. Open global transport

B4 does not prove:

- every fixed-flow fibre contains a good lift;
- every reconfiguration component reaches a good flow;
- every factorably bad core has a source-realizable escape;
- connected-neighbour correction always kills some plane defect;
- a monotone compression potential exists.

These are genuine source/global questions, not missing linear algebra.

## 12. Provenance and assurance

Programme B4 source:

`proof-development/affine-cdc-rigour-v1@345074690b7a8658c1208ae84f10d709f8b74bcf`.

State retained:

`READY-FOR-CURATOR / FRONTIER-EXPLICIT`.

The motion laws are Curator-integrated authorial proofs. They have not received independent audit or end-to-end Lean verification and create no manuscript, publication, release, arXiv, or DOI status.