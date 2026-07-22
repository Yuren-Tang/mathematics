# Physical translation cells and route-pair difference targets

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Parent:** `projects/affine-cdc/research/PHYSICAL_TRANSLATION_WORD_STOKES_V1.md`  
**Status:** exact finite challenge-pair algebra and source-side target sharpening; physical surgery remains open.  
**Not implied:** canonical acceptance, independent audit, Lean verification, manuscript readiness, or the global five-support theorem.

---

## 1. Parallel challenge pairs

Let

\[
V\cong\mathbf F_2^3,
\qquad
0\ne g\in V,
\]

and let

\[
\Lambda_g
=
\{\lambda\in V^*: \lambda(g)=1\}
\cong AG(2,2)
\]

be the four locked challenges.

The translation space of the affine plane is

\[
g^\perp
=
\{\delta\in V^*: \delta(g)=0\}
\cong\mathbf F_2^2.
\]

For every nonzero

\[
\delta\in g^\perp,
\]

the involution

\[
\lambda\longmapsto\lambda+\delta
\]

partitions `Lambda_g` into two parallel pairs. These are one of the three perfect matchings of the four challenge points.

### Theorem 1.1 — matching/direction dictionary

The three nonzero elements of `g^perp` are naturally and bijectively the three challenge matchings.

This is the dual form of the previous quotient

\[
V/\langle g\rangle
\cong\mathbf F_2^2.
\]

The natural perfect pairing

\[
V/\langle g\rangle
\times
 g^\perp
\longrightarrow\mathbf F_2
\]

identifies a nonconstant flat word with the unique parallel-pair direction on which it is constant.

---

## 2. Scalar subgraph difference

Let

\[
c:E(Q)\to V\setminus\{0\}
\]

be the locked rank-three quotient flow, with all four terminal values equal to `g`.

For a covector `phi in V*`, define the scalar subgraph

\[
H_\phi
=
\{e\in E(Q):\phi(c(e))=1\}.
\]

For a locked challenge `lambda in Lambda_g`, `H_lambda` has all four terminals in its boundary and realises the locked terminal matching.

For `delta in g^perp`, one has `delta(g)=0`, so `H_delta` has no terminal boundary.

### Theorem 2.1 — exact parallel-pair difference

For every `lambda in Lambda_g` and `delta in g^perp`,

\[
\boxed{
H_{\lambda+\delta}
=
H_\lambda\triangle H_\delta.
}
\]

Moreover,

\[
\boxed{
\partial H_\delta=0
}
\]

at the four terminals.

### Proof

Edgewise,

\[
(\lambda+\delta)(c(e))
=
\lambda(c(e))+\delta(c(e)).
\]

Thus membership is symmetric difference. At every terminal the scalar boundary value of `H_delta` is `delta(g)=0`.

### Consequence 2.2

The two challenges in one parallel pair differ by the same closed scalar cycle system `H_delta`.

Therefore the matching class of a weight-two translation word has a canonical physical scalar object:

\[
\boxed{
\text{matching direction }\delta
\quad\longleftrightarrow\quad
\text{closed scalar subgraph }H_\delta.
}
\]

This is the first direct source-side object attached to the finite flat matching class.

---

## 3. Weight-two words and the dual direction

Let

\[
f_v(\lambda)=\lambda(v)
\]

be a nonconstant affine challenge word, with

\[
v\notin\{0,g\}.
\]

Its linear part on the affine plane `Lambda_g` is the functional

\[
\delta\longmapsto\delta(v)
\qquad(\delta\in g^\perp).
\]

There is a unique nonzero

\[
\delta_v\in g^\perp
\]

such that

\[
\delta_v(v)=0.
\]

### Theorem 3.1 — canonical matching selected by a flat word

The two points of `Lambda_g` on which `f_v` has value zero form one `delta_v`-parallel pair, and the two points on which it has value one form the other `delta_v`-parallel pair.

Thus the matching selected by `f_v` is exactly the matching whose source-side difference object is

\[
H_{\delta_v}.
\]

### Significance

The finite matching triality and the source scalar-flow triality are not merely equinumerous. They are linked by the exact formula

\[
H_{\lambda+\delta_v}
=
H_\lambda\triangle H_{\delta_v}.
\]

---

## 4. Revised weight-two physical theorem

The earlier weight-two target can now be sharpened.

Fix a nonconstant translation word `f_v` and its dual direction `delta_v`. Let

\[
Z_v:=H_{\delta_v}.
\]

Then `Z_v` is a closed binary even subgraph and toggles the two scalar route witnesses inside each matched pair of challenges.

The physical theorem should prove one of the following.

### Target 4.1 — active component escape

If a component of `Z_v` meets the two locked terminal-path systems in a way that changes their pairing or order, toggling that component gives a genuine Kempe/profile escape.

### Target 4.2 — serial confinement

If every component of `Z_v` preserves each locked route and only changes its internal side allocation, then the components are confined to serial intervals. A minimal nonexchangeable interval should yield:

- nested linkage;
- a cyclic four-cut with matching `delta_v`;
- or a smaller zero/co-root defect interface.

### Target 4.3 — common-cut obstruction

If the side allocation of `Z_v` cannot be chosen consistently across the two parallel pairs, the discrepancy is exactly a challenge-side curvature word. It returns to the common-cut/DDD branch rather than creating a new flat obstruction.

---

## 5. Constant word

The constant word

\[
1111=f_g
\]

has zero linear part on `Lambda_g`; it selects no matching direction.

It is the global-complement direction, and therefore has no nonzero `delta in g^perp` attached to it.

This algebraically separates the two physical branches:

- weight two: one canonical closed scalar subgraph `H_delta` and one terminal matching;
- constant one: simultaneous side reversal on all four challenge sheets, hence a gauge/common-cut question.

---

## 6. Strategic consequence

The weight-two composition theorem is no longer an abstract statement about a four-bit word. It is a theorem about one explicitly defined closed scalar subgraph:

\[
\boxed{
Z_v=H_{\delta_v}.
}
\]

The next source-graph step is to analyse how components of `Z_v` intersect the two locked terminal paths.

The expected dichotomy is:

\[
\boxed{
\text{pair-changing component}
\Rightarrow
\text{Kempe/profile escape},
}
\]

or

\[
\boxed{
\text{all components pair-preserving}
\Rightarrow
\text{serial/nested decomposition or smaller separator}.
}
\]

This is the most direct current route from flat translation parity to Type-T strict descent.

---

## 7. Trust boundary

### Exact here

- the duality between `V/<g>` and `g^perp`;
- the three matching directions as the three nonzero `delta in g^perp`;
- the exact scalar-subgraph identity `H_(lambda+delta)=H_lambda triangle H_delta`;
- terminal-evenness of `H_delta`;
- the unique `delta_v` selected by a nonconstant affine word;
- the exact identification of its challenge matching with the parallel-pair direction of `H_delta`.

### Still open

- the route-change criterion for a component of `H_delta`;
- proof that pair-preserving components admit serial/nested localisation;
- extraction of a cyclic four-cut or defect unit from failure of serial exchange;
- physical comparison of translation hexagons with challenge side words;
- regional torsor Stokes and the global five-support theorem.
