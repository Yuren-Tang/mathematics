# Type-X projective profiles and crossed `g`-edge selector charts

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `47cb732c6f340fc26db8b7d2ffa0e95148ccda13`  
**Parents:**

- `projects/affine-cdc/research/PETERSEN_RELATIVE_CHANNEL_PROFILE_CALIBRATION_V1.md`;
- `projects/affine-cdc/research/PETERSEN_IDENTITY_HEXAGON_TRANSVERSE_CHANNEL_TRANSVERSAL_V1.md`;
- `projects/affine-cdc/five-support/route-locked-quotient-phase.md`;
- `projects/affine-cdc/research/DDD_ROUTE_ORIENTATION_COVER_V1.md`.

**Status:** exact local comparison theorem. A crossed physical `g`-edge provides a complete affine coordinate chart on the four locked challenges, and its three sheet-difference signatures agree exactly with the three channel-triality translations of the projective Type-X profile plane. An aligned `g`-edge has rank one and leaves one constant endpoint-twist bit.  
**Not implied:** existence of a crossed `g`-edge in every irreducible region, global compatibility of charts on several edges, aligned-edge serial contraction, bounded twist localisation, canonical acceptance, Lean verification, manuscript readiness, or the global five-support theorem.

---

## 1. Projective Type-X coordinates

Fix an ordered active root

\[
r=uv
\]

and write

\[
W=\{x,y,z\}.
\]

A Type-X channel profile chooses one channel from each pair

\[
P_w=\{uw,vw\}.
\]

Choose the orientation convention

\[
\epsilon_w(T)=1
\quad\Longleftrightarrow\quad
vw\in T.
\]

Thus an oriented transversal is encoded by

\[
\epsilon(T)=(\epsilon_x,\epsilon_y,\epsilon_z)
\in\mathbf F_2^3.
\]

Full complement adds

\[
111,
\]

so the projective Type-X profile is the class of `epsilon` modulo `<111>`.

### Definition 1.1 — complement-invariant chart

Define

\[
\boxed{
\chi_{x,y\mid z}([T])
=
(\epsilon_x+\epsilon_z,
 \epsilon_y+\epsilon_z)
\in\mathbf F_2^2.
}
\]

### Theorem 1.2 — affine chart

The map

\[
\boxed{
\chi_{x,y\mid z}:
\overline{\mathcal T}_r
\xrightarrow{\sim}
\mathbf F_2^2
}
\]

is a bijection from the four complement-pairs of Type-X transversals to the affine plane `F2^2`.

### Proof

Adding `111` changes both terms by

\[
(1+1,1+1)=(0,0),
\]

so the chart is complement-invariant. The eight oriented words give the four values

\[
00,01,10,11,
\]

each twice, once for each complementary lift. ∎

---

## 2. Channel-triality translations in the chart

The three nonzero channel-cohomology directions are represented by the four-cycles

\[
\Gamma_{xy},
\qquad
\Gamma_{xz},
\qquad
\Gamma_{yz}.
\]

On the oriented transversal word they toggle respectively

\[
110,
\qquad
101,
\qquad
011.
\]

### Theorem 2.1 — exact switch signatures

Under `chi_(x,y|z)`, the three triality directions act by translation through

\[
\boxed{
\Gamma_{xy}\longmapsto(1,1),
}
\]

\[
\boxed{
\Gamma_{xz}\longmapsto(0,1),
}
\]

and

\[
\boxed{
\Gamma_{yz}\longmapsto(1,0).
}
\]

### Proof

For a toggle word `d=(d_x,d_y,d_z)`, the chart changes by

\[
(d_x+d_z,d_y+d_z).
\]

Substitution of `110,101,011` gives the three displayed values. ∎

### Corollary 2.2

The projective Type-X plane is the regular affine translation representation of

\[
H^1(K_{2,3};\mathbf F_2)
\cong\mathbf F_2^2.
\]

There is no nontrivial stabiliser and no fourth translation direction.

---

## 3. Physical selector chart on a `g`-edge

Let

\[
c:E(Q)\to V\setminus\{0\},
\qquad
V=\langle g\rangle\oplus U,
\qquad
U\cong\mathbf F_2^2,
\]

be a full-rank route-locked quotient flow.

The four scalar sheets are indexed by

\[
\phi\in U^*,
\]

or equivalently by

\[
\lambda_\phi=\alpha+\phi\circ\pi
\in\Lambda_g.
\]

Let `e=ab` be an internal `g`-edge. At its two endpoints the common non-`g` quotient colours are

\[
q_a,q_b\in U\setminus\{0\}.
\]

After ordering the two continuation edges at each endpoint, the physical selector bits are

\[
s_a(\phi)=\varepsilon_a+\phi(q_a),
\]

\[
s_b(\phi)=\varepsilon_b+\phi(q_b).
\]

Define

\[
\boxed{
\sigma_e(\phi)
=(s_a(\phi),s_b(\phi))
\in\mathbf F_2^2.
}
\]

---

## 4. Crossed edge gives a complete affine comparison

Assume

\[
q_a\ne q_b.
\]

Then `q_a,q_b` are linearly independent in the two-dimensional space `U`.

### Theorem 4.1 — crossed selector chart

The map

\[
\boxed{
\sigma_e:U^*\xrightarrow{\sim}\mathbf F_2^2
}
\]

is an affine bijection.

Its linear part is

\[
\phi\longmapsto(\phi(q_a),\phi(q_b)).
\]

### Proof

Evaluation on the ordered basis `(q_a,q_b)` is a linear isomorphism

\[
U^*\to\mathbf F_2^2.
\]

Adding the constant vector `(epsilon_a,epsilon_b)` gives an affine bijection. ∎

### Theorem 4.2 — physical three-switch signatures

For the three nonzero sheet differences `delta in U*`, the selector changes are exactly

\[
\boxed{
(0,1),
\qquad
(1,0),
\qquad
(1,1).
}
\]

More precisely:

- the unique nonzero `delta` annihilating `q_a` gives `(0,1)`;
- the unique nonzero `delta` annihilating `q_b` gives `(1,0)`;
- the third nonzero `delta` gives `(1,1)`.

This is the crossed-signature theorem of the quotient-phase corpus.

---

## 5. Canonical local challenge/profile map

Match the three nonzero sheet differences with the three channel directions by equal selector signature:

\[
\begin{array}{c|c}
\text{channel direction}&\text{physical selector change}\\
\hline
\Gamma_{xy}&(1,1)\\
\Gamma_{xz}&(0,1)\\
\Gamma_{yz}&(1,0).
\end{array}
\]

This defines a unique linear triality isomorphism

\[
\phi_e:
H^1(K_r;\mathbf F_2)
\xrightarrow{\sim}
U^*.
\]

### Theorem 5.1 — crossed-edge comparison isomorphism

There is a unique affine bijection

\[
\boxed{
J_e:
\Lambda_g
\xrightarrow{\sim}
\overline{\mathcal T}_r
}
\]

such that

\[
\boxed{
\chi_{x,y\mid z}(J_e(\lambda_\phi))
=
\sigma_e(\phi).
}
\]

Its linear part identifies the three physical sheet-difference directions with the three DDD/channel-triality directions.

### Proof

Both `chi_(x,y|z)` and `sigma_e` are affine bijections to `F2^2`. Define

\[
J_e
=
\chi_{x,y\mid z}^{-1}\circ\sigma_e.
\]

Theorem 2.1 and Theorem 4.2 identify their three nonzero translation signatures term by term. ∎

### Consequence 5.2 — no free basepoint remains at a crossed edge

The selector constants

\[
(\varepsilon_a,\varepsilon_b)
\]

supply the affine origin. The three-switch signatures supply the linear part. Therefore a crossed `g`-edge calibrates all four locked challenges against all four projective Type-X profiles at once.

No eight-state check and no separately chosen challenge/profile basepoint is required.

### Coordinate covariance

Changing:

- the reference vertex `z`;
- the ordering of `x,y,z`;
- the ordering of the two endpoints of `e`;
- either continuation-edge orientation convention;

postcomposes the two charts by affine automorphisms of `F2^2`. The existence and affine-equivariance of `J_e` are unchanged. The displayed direction labels change coherently.

---

## 6. Aligned edge is exactly rank one

Assume

\[
q_a=q_b=q.
\]

Then

\[
\sigma_e(\phi)
=
(\varepsilon_a+\phi(q),
 \varepsilon_b+\phi(q)).
\]

### Theorem 6.1 — aligned selector rank

The selector map has affine image of size two and linear rank one.

Its three nonzero sheet-difference signatures are

\[
\boxed{
(0,0),
\qquad
(1,1),
\qquad
(1,1)
}
\]

in some order.

### Proof

The linear part is

\[
\phi\longmapsto(\phi(q),\phi(q)),
\]

whose image is the diagonal line

\[
\{00,11\}.
\]

Exactly one nonzero functional annihilates `q`; the other two evaluate to one. ∎

### Definition 6.2 — aligned endpoint twist

The selector difference

\[
\boxed{
\tau_e
=s_a(\phi)+s_b(\phi)
=\varepsilon_a+\varepsilon_b
}
\]

is independent of the challenge `phi`.

Thus an aligned edge retains exactly:

1. one observed matching direction `q`;
2. one constant endpoint twist `tau_e`;
3. one nonzero sheet-difference direction invisible to the selector pair.

### Corollary 6.3 — no new finite comparison type

Failure of a `g`-edge to provide the full Type-X affine comparison is exactly the aligned rank-one degeneration. It introduces no new finite selector alphabet beyond one direction and one binary twist.

Whether a family of aligned edges is serialisable, separates, or carries nontrivial twist holonomy is a graph-level question.

---

## 7. Revised regional frontier

### Closed here

- the four projective Type-X profiles have an explicit complement-invariant `F2^2` chart;
- the three channel triality directions act by all three nonzero translations;
- a crossed `g`-edge has the identical three-switch representation;
- crossed selector constants canonically fix the affine origin;
- therefore one crossed `g`-edge gives a complete local challenge/profile comparison;
- an aligned edge is precisely a rank-one degeneration with one constant twist.

### Still open

1. Prove that every irreducible Type-X return region contains a crossed `g`-edge, **or** reduce the all-aligned region.
2. In the all-aligned branch, choose composition-compatible endpoint orientation conventions and determine whether the bits `tau_e` form:
   - a coboundary, yielding an oriented serial/gauge reduction;
   - a nontrivial cycle class, yielding bounded Type-H/DDD holonomy;
   - or a separator/common-cut witness.
3. Transport the local comparison through contracted non-`g` components and preserve the four external route ports.
4. Convert the resulting calibrated profile change into a route escape, four-pole split, bounded DDD/defect atom, or strict serial contraction.
5. Assemble horizontal/global induction.