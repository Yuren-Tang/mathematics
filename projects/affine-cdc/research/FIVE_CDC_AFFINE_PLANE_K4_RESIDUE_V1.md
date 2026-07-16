# Affine-plane `K_4` compression and the seven plane residues

**Programme:** `AffineCDC — Research Lead`  
**Status:** theorem-level structural checkpoint; not canonical pending Director review and literature audit  
**Parents:** `FIVE_CDC_HALFCUBE_SUBGRAPH_CLASSIFICATION_V1.md`, `FIVE_CDC_GAUGE_AS_PIECEWISE_ROOT_TRANSLATION_V1.md`, canonical `core/rank-three-fano-compatibility.md`

## 1. Purpose

The exact half-cube classification says that a root lift compresses to five
supports whenever its unused-root graph contains a `K_4`. Among the two affine
types of four-point subsets of `F_2^3`, an affine plane is especially natural:
its six internal roots are controlled by one linear functional and the canonical
Fano characteristic vector.

This packet isolates an exact gauge-invariant residue for each of the seven
linear planes `W<=F_2^3`. The residue vanishes exactly when one of the two affine
planes parallel to `W` can be made an unused `K_4` by changing the compatible
root lift while keeping the projected Fano flow fixed.

Thus every nowhere-zero Fano flow carries seven plane-slice tests. Vanishing of
any one gives a five-support cover.

## 2. Plane-side bit of a root

Put

\[
\Gamma=\mathbf F_2^3.
\]

Fix a two-dimensional linear plane

\[
W\leq\Gamma
\]

and let

\[
\ell_W:\Gamma\to\mathbf F_2
\]

be the unique nonzero linear functional with kernel `W`. Its two affine fibres
are

\[
P_0=W,
\qquad
P_1=a+W
\]

for any `a` with `\ell_W(a)=1`.

Let

\[
f:E(G)\to\Gamma\setminus\{0\}
\]

be a nowhere-zero flow on a finite loopless cubic multigraph and let

\[
g:E(G)\to\mathcal R_8
\]

be a root lift. If `e` has direction

\[
h=f(e)\in W\setminus\{0\}
\]

and

\[
g(e)=r_{s,s+h},
\]

define

\[
\eta_e^W(g):=\ell_W(s).
\]

This is well defined because `\ell_W(h)=0`, so the two endpoints of the root have
the same `\ell_W`-value.

A root of direction `h\in W` lies internally in `P_\varepsilon` exactly when

\[
\eta_e^W(g)=\varepsilon.
\]

Roots whose directions lie outside `W` cross between `P_0` and `P_1` and are
internal to neither affine plane.

## 3. Relation with the canonical characteristic vector

For `0\neq h\in W`, let

\[
\kappa_{W,h}\in Q_h
\]

be the canonical component of the local Fano characteristic vector: it is the
common class modulo `h` of the other two nonzero elements of `W`.

### Proposition 3.1 — plane side is a characteristic pairing

For every `x\in\Gamma`,

\[
\boxed{
B_h(\kappa_{W,h},[x]_h)=\ell_W(x).}
\]

Consequently, if `g(e)` has fibre coordinate `q_e(g)=[s]_h`, then

\[
\boxed{
\eta_e^W(g)=B_h(\kappa_{W,h},q_e(g)).}
\]

#### Proof

Choose `u\in W` independent of `h`. Then `\kappa_{W,h}=[u]_h`, and the canonical
polar form is

\[
B_h([u],[x])=\omega(h,u,x).
\]

The functional `\omega(h,u,-)` is nonzero and has kernel `W`; hence it is the
unique functional `\ell_W`. ∎

Thus the plane-side observable is already present in the canonical quadratic
package. It is the linear characteristic covector attached to the plane `W`.

## 4. The degree-one/degree-three subgraph

Define

\[
G_W:=(V(G),E_W),
\qquad
E_W:=\{e:f(e)\in W\}.
\]

At a cubic vertex `v`, the three incident flow values are the nonzero elements of
a two-dimensional local plane `U_v`. Since two planes in `F_2^3` meet in a line,

\[
\deg_{G_W}(v)
=
\begin{cases}
3,&U_v=W,\\
1,&U_v\neq W.
\end{cases}
\]

Hence every component of `G_W` is a degree-one/degree-three graph.

### Lemma 4.1 — component constancy

The bit `\eta_e^W(g)` is constant on all edges of each connected component of
`G_W`.

#### Proof

At a degree-three vertex one has `U_v=W`. The local root triangle has its three
support indices in one affine coset of `W`. Therefore all three incident
`W`-direction roots lie inside the same affine plane `P_0` or `P_1`, so their
plane-side bits agree.

A degree-one vertex imposes no comparison and can occur only as a leaf of a
component. Equality therefore propagates through every connected component. ∎

Let

\[
\mathscr K_W:=\pi_0(G_W)
\]

and write

\[
\eta_W(g)\in\mathbf F_2^{\mathscr K_W}
\]

for the resulting component-bit vector.

## 5. Gauge action on plane components

Let

\[
H_f^0
=
\{k:V(G)\to\Gamma:
 k_u+k_v\in\langle f(e)\rangle\text{ for every }e=uv\}
\]

be the admissible vertex-translation space.

For `k\in H_f^0` and an edge `e=uv\in E_W`,

\[
k_u+k_v\in\langle f(e)\rangle\subseteq W,
\]

so

\[
\ell_W(k_u)=\ell_W(k_v).
\]

Thus `\ell_W(k_v)` is constant on each component `K\in\mathscr K_W`. Define

\[
\tau_W:H_f^0\to\mathbf F_2^{\mathscr K_W},
\qquad
(\tau_Wk)_K:=\ell_W(k_v)\quad(v\in K),
\]

and put

\[
T_W:=\operatorname{im}\tau_W.
\]

### Lemma 5.1 — component toggle law

For every admissible translation field `k`,

\[
\boxed{
\eta_W(g^k)=\eta_W(g)+\tau_W(k).}
\]

#### Proof

Translation sends the root pair `{s,s+h}` to `{s+k_v,s+h+k_v}` at either endpoint.
Applying `\ell_W` changes the plane-side bit by `\ell_W(k_v)`, which is constant
on the component. ∎

A constant field `k_v=a` with `\ell_W(a)=1` is admissible and maps to the all-one
component vector. Therefore

\[
\boxed{\mathbf1\in T_W.}
\]

## 6. The affine-plane residue

Define the **plane residue**

\[
\boxed{
R_W(f):=[\eta_W(g)]
\in
\mathbf F_2^{\mathscr K_W}/T_W.}
\]

Lemma 5.1 shows that this class is independent of the chosen root lift `g` of the
fixed Fano flow `f`.

### Theorem 6.1 — affine-plane `K_4` compression criterion

The following are equivalent.

1. `R_W(f)=0`.
2. Some root lift of `f` uses no root internal to `P_0`.
3. Some root lift of `f` uses no root internal to `P_1`.
4. Some root lift of `f` has an unused affine-plane `K_4` parallel to `W`.

Whenever these conditions hold, `G` has a five-support double cover obtained by
source-dependent half-cube compression.

#### Proof

For a translated lift `g^k`, the affine plane `P_\varepsilon` is unused exactly
when every `W`-direction edge lies in the opposite plane, namely when

\[
\eta_W(g^k)=(1-\varepsilon)\mathbf1.
\]

By Lemma 5.1 this is solvable exactly when

\[
\eta_W(g)\in T_W+\langle\mathbf1\rangle.
\]

Since `\mathbf1\in T_W`, this is simply `\eta_W(g)\in T_W`, or `R_W(f)=0`.
The two choices of `\varepsilon` are equivalent by global translation.

If `P_\varepsilon` is unused, the unused-root graph contains the six edges of the
`K_4` induced by its four support indices. The exact half-cube classification
then gives a five-support compression. ∎

## 7. Dual directional stress certificate

Choose one representative vertex `v_K` in every component `K\in\mathscr K_W`.
For

\[
y=(y_K)\in(\mathbf F_2^{\mathscr K_W})^*,
\]

define a vertex covector field supported on the representatives by

\[
\alpha_y(v_K):=y_K\ell_W,
\qquad
\alpha_y(v):=0\text{ otherwise}.
\]

### Theorem 7.1 — plane residue/stress duality

One has

\[
\boxed{
y\in T_W^\perp
\iff
\alpha_y\in\operatorname{im}\delta_f^*.}
\]

Consequently,

\[
R_W(f)\neq0
\]

if and only if there exists a relative equilibrium stress represented by edge
covectors

\[
\psi_e\in\operatorname{Ann}(f(e))
\]

whose divergence is `\alpha_y` for some `y` satisfying

\[
\boxed{y(\eta_W(g))=1.}
\]

#### Proof

The map `\tau_W` is the composition of restriction to the selected vertices with
application of the functional `\ell_W`. Its adjoint sends `y` to `\alpha_y`.
Apply the vertex controllability/stress duality

\[
(\operatorname{im}H_f^0)^\perp=\operatorname{im}\delta_f^*.
\]

The phase condition is ordinary separation of a nonzero quotient class by its
dual. ∎

Thus failure of affine-plane compression is certified by a directional stress,
not merely by a dense used-label graph.

## 8. The seven-slice problem

There are seven two-dimensional linear planes `W<=F_2^3`, equivalently seven
nonzero functionals `\ell_W`. Every fixed Fano flow therefore has seven residues

\[
\boxed{
R_W(f)
\in
\mathbf F_2^{\pi_0(G_W)}/T_W.}
\]

The affine-plane route to five supports succeeds if at least one of them vanishes.
A fixed-flow obstruction to this route must supply seven nonzero directional
stress certificates simultaneously.

This gives a sharply defined next problem:

\[
\boxed{
\text{Can all seven plane residues of a nowhere-zero cubic Fano flow be nonzero?}}
\]

If not, affine-plane `K_4` compression proves the five-support conclusion. If yes,
the smallest simultaneous-residue example will expose the missing higher-order
mechanism and leave the other target templates available.

## 9. Relation to the explicit `K_6` gauge escape

In the explicit `K_6` example, the translated compressible lift leaves unused the
affine plane

\[
\{2,3,4,5\},
\]

whose direction plane is

\[
W=\{0,1,6,7\}.
\]

Hence the corresponding residue `R_W(f)` vanishes. The transformed used-label
graph nevertheless uses at least two roots in every Fano direction. Therefore
this affine-plane `K_4` mechanism is strictly more flexible than the simpler
criterion that one direction use only a single root and leave three parallel
roots unused.

## 10. Strategic relation to quadratic transgression

Proposition 3.1 identifies the plane-side functional with the canonical local
characteristic components. The seven residues are therefore not external
colouring invariants attached after AffineCDC. They are seven linear slices of
the same characteristic-torsor geometry used in the rank-three compatibility
proof.

The immediate structural target is to determine whether the Fano quadratic
transgression, global handshaking identity, or Hamming self-duality imposes a
relation among the seven classes `R_W(f)` strong enough to force a zero.

No such simultaneous-vanishing theorem is claimed here.
