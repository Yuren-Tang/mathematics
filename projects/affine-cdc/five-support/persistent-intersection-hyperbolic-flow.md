# Persistent intersections as hyperbolic flow norms

## 1. Purpose

Let

$$
f:E(G)\longrightarrow\Gamma\setminus\{0\},
\qquad
\Gamma\cong\mathbf F_2^3,
$$

be the fixed nowhere-zero Fano flow and let

$$
\mathcal B_f
$$

be its reduced gauge code.

The gauge-radicalisation theorem shows that failure to move a response cycle `z` into the ribbon-intersection radical is certified by another physical cycle `z'` satisfying

$$
\mathcal B(z,z')=1,
\qquad
w:=z\odot z'\in\mathcal B_f^\perp.
$$

The active Schur-duality theorem gives

$$
\mathcal B_f^\perp
=
\mathcal C(G)*\mathcal F_f,
$$

where `\mathcal C(G)` is the binary cycle code and `\mathcal F_f` is the coordinate code of the Fano flow.

This chapter gives a coordinate-free interpretation of that Schur space.

Every word in `\mathcal B_f^\perp` is the diagonal pairing

$$
w_e=\langle u(e),f(e)\rangle
$$

of `f` with an auxiliary dual-valued flow

$$
u:E(G)\longrightarrow\Gamma^*.
$$

Equivalently, if

$$
H=\Gamma\oplus\Gamma^*
$$

has hyperbolic quadratic form

$$
q(x,\xi)=\xi(x),
$$

then

$$
h(e)=(f(e),u(e))
$$

is an `H`-valued flow and `w` is its quadratic norm word.

The rank of `u` gives a new exact hierarchy for the persistent-intersection obstruction.

## 2. The coordinate flow code

Let

$$
\mathcal F_f
=
\{\alpha\circ f:\alpha\in\Gamma^*\}
\le
\mathbf F_2^{E(G)}.
$$

Because `f` spans `\Gamma` at the full-rank endpoint, the map

$$
\Gamma^*\longrightarrow\mathcal F_f
$$

is an isomorphism.

The Schur product space is

$$
\mathcal C(G)*\mathcal F_f
=
\left\langle
c*(\alpha\circ f):
 c\in\mathcal C(G),
 \alpha\in\Gamma^*
\right\rangle.
$$

## 3. Dual-flow representation

Let

$$
\operatorname{Flow}(G;\Gamma^*)
$$

denote the space of `\Gamma^*`-valued flows: at every vertex, the incident covectors sum to zero.

For such a flow `u`, define

$$
N_f(u)_e
=
\langle u(e),f(e)\rangle.
$$

### Theorem 3.1 — Schur space equals the norm image

$$
\boxed{
\mathcal C(G)*\mathcal F_f
=
\{N_f(u):u\in\operatorname{Flow}(G;\Gamma^*)\}.
}
$$

#### Proof

Choose a basis

$$
\alpha_1,\alpha_2,\alpha_3
$$

of `\Gamma^*`.

Let

$$
u:E(G)\to\Gamma^*
$$

be a dual-valued flow and write

$$
u(e)=c_1(e)\alpha_1+c_2(e)\alpha_2+c_3(e)\alpha_3.
$$

The flow equation for `u` holds coordinatewise, so each

$$
c_i\in\mathcal C(G).
$$

Then

$$
\begin{aligned}
N_f(u)_e
&=
\sum_i c_i(e)\alpha_i(f(e))\\
&=
\sum_i
\bigl(c_i*(\alpha_i\circ f)\bigr)_e.
\end{aligned}
$$

Hence `N_f(u)` lies in the Schur product space.

Conversely, every Schur expression

$$
w
=
\sum_i c_i*(\alpha_i\circ f)
$$

defines

$$
u(e)=\sum_i c_i(e)\alpha_i.
$$

Each `c_i` is a binary flow, so `u` is a `\Gamma^*`-valued flow, and the same calculation gives `N_f(u)=w`. ∎

Combining with the active gauge duality gives

$$
\boxed{
\mathcal B_f^\perp
=
N_f\bigl(\operatorname{Flow}(G;\Gamma^*)\bigr).
}
$$

## 4. Hyperbolic flow form

Put

$$
H=\Gamma\oplus\Gamma^*.
$$

Define

$$
q(x,\xi)=\xi(x)
$$

and polar form

$$
b\bigl((x,\xi),(y,\eta)\bigr)
=
\xi(y)+\eta(x).
$$

For a dual flow `u`, let

$$
h=(f,u):E(G)\to H.
$$

Both coordinates satisfy the flow equation, so `h` is an `H`-valued flow.

### Corollary 4.1 — persistent word as quadratic norm

$$
\boxed{
w_e=q(h(e)).}
$$

Thus a gauge-invisible common-edge word is the anisotropic support of a hyperbolic flow lying above the fixed Fano flow.

## 5. Local boundary identity

Let a cubic vertex have incident edges `e_1,e_2,e_3`.  Put

$$
f_i=f(e_i),
\qquad
u_i=u(e_i),
\qquad
h_i=(f_i,u_i).
$$

Flow conservation gives

$$
f_3=f_1+f_2,
\qquad
u_3=u_1+u_2.
$$

### Theorem 5.1 — norm-boundary identity

At every cubic vertex,

$$
\boxed{
w_{e_1}+w_{e_2}+w_{e_3}
=
b(h_1,h_2).}
$$

#### Proof

Expand:

$$
\begin{aligned}
w_1+w_2+w_3
&=u_1(f_1)+u_2(f_2)+(u_1+u_2)(f_1+f_2)\\
&=u_1(f_2)+u_2(f_1)\\
&=b(h_1,h_2).
\end{aligned}
$$

∎

The right side is independent of which two incident edges are chosen because `h_1+h_2+h_3=0`.

## 6. Intersection of two cubic cycles

Let

$$
z,z'\in\mathcal C(G)
$$

and put

$$
w=z\odot z'.
$$

At a cubic vertex, a nonzero binary cycle uses exactly two of the three incident edges.

### Lemma 6.1 — local overlap types

At a vertex, the restriction of `w` has exactly one of the following forms.

1. weight `0`: at least one of `z,z'` avoids the vertex;
2. weight `2`: `z,z'` use the same local pair;
3. weight `1`: they use different local pairs.

In particular, local weight three is impossible.

### Corollary 6.2 — edge-disjoint cycles do not intersect

If

$$
z\odot z'=0,
$$

then the supports of `z,z'` are vertex-disjoint.  Consequently they have zero mod-two intersection in every ribbon thickening of `G`:

$$
\boxed{
\mathcal B(z,z')=0.
}
$$

#### Proof

If two nonzero cubic cycle germs meet one vertex, each uses a two-element subset of a three-element star, and the two subsets must share an edge.  Hence edge-disjoint cycles are vertex-disjoint.  Their ribbon representatives lie in disjoint vertex discs and edge bands, so they have zero intersection. ∎

Therefore every persistent odd-intersection pair has

$$
\boxed{w=z\odot z'\ne0.}
$$

There is always a genuine shared-edge carrier.

Combining Lemma 6.1 with Theorem 5.1, the vertices at which `z,z'` use different transition pairs are exactly the odd-degree vertices of the norm support `w`, and their parity is measured by the hyperbolic polar interaction of the incident flow values.

## 7. Dual-rank hierarchy

For a word

$$
w\in\mathcal B_f^\perp,
$$

define its **dual-flow rank** by

$$
\operatorname{drk}_f(w)
=
\min
\left\{
\dim\langle u(E)\rangle:
 u\in\operatorname{Flow}(G;\Gamma^*),
 N_f(u)=w
\right\}.
$$

Since `\dim\Gamma^*=3`,

$$
0\le\operatorname{drk}_f(w)\le3.
$$

For a persistent odd-intersection word, `w\ne0`, so the rank is `1`, `2`, or `3`.

### Theorem 7.1 — rank-one normal form

The following are equivalent.

1. `\operatorname{drk}_f(w)=1`.
2. There exist a nonzero covector `\alpha\in\Gamma^*` and a binary cycle `c` such that
   $$
   \boxed{
w=c*(\alpha\circ f).}
   $$

Equivalently, if

$$
H_\alpha
=
\{e:\alpha(f(e))=1\}
$$

is the scalar even subgraph of the Fano flow, then

$$
\boxed{
\operatorname{supp}w
=
\operatorname{supp}c
\cap
H_\alpha.
}
$$

#### Proof

A rank-one dual flow has the form

$$
u(e)=c(e)\alpha
$$

for one nonzero `\alpha`.  The flow equation for `u` is exactly the binary cycle equation for `c`.  The norm formula gives the displayed expression.  The converse is immediate. ∎

Thus the first persistent obstruction layer is the intersection of one physical binary cycle with one scalar sheet of the fixed Fano flow.

### Theorem 7.2 — rank-two normal form

The condition

$$
\operatorname{drk}_f(w)\le2
$$

is equivalent to the existence of independent covectors `\alpha,\beta` and binary cycles `c,d` such that

$$
\boxed{
w
=c*(\alpha\circ f)
+d*(\beta\circ f).}
$$

The rank-three branch is the residual case in which no such two-scalar-sheet expression exists.

These forms are basis-independent statements about the span of the auxiliary dual flow.

## 8. Self-intersection subcase

For a gauge-invisible one-sided cycle, one has

$$
z'=z,
\qquad
w=z\odot z=z.
$$

Hence

$$
\boxed{
z\in\mathcal B_f^\perp}
$$

and there is a dual flow `u` with

$$
\boxed{
z_e=\langle u(e),f(e)\rangle.}
$$

The one-sided response cycle itself is therefore a hyperbolic-flow norm support.  Its dual rank supplies an exact rank-one/two/three hierarchy for nonorientability persistent under all admissible gauges.

## 9. Updated mechanism target

The gauge-rigid positive-genus branch now has data

$$
\boxed{
\begin{array}{c}
z,z'\in\mathcal C(G),\\
\mathcal B(z,z')=1,\\
w=z\odot z'\ne0,\\
h=(f,u)\in\operatorname{Flow}(G;\Gamma\oplus\Gamma^*),\\
q(h)=w.
\end{array}}
$$

The next proof order is:

1. localise the rank-one case
   $$
w=c*H_\alpha$$
   using scalar-component and marked-transition theory;
2. reduce rank two by the interaction of two scalar sheets and their Kempe difference;
3. reserve the full-rank hyperbolic branch for comparison with the DDD support-label geometry.

A successful theorem should turn the norm support into a proper component region, separator, bounded handle, horizontal flow switch, or the final DDD class.

## 10. Reliability boundary

Proved here:

- coordinate-free dual-flow representation of `\mathcal B_f^\perp`;
- hyperbolic-flow norm interpretation;
- local norm-boundary identity;
- nonvanishing of the common-edge word for an odd intersection pair on a cubic graph;
- dual-rank hierarchy and rank-one/two normal forms.

Open:

- composition of every rank-one persistent word;
- reduction of rank two by Kempe geometry;
- classification of full dual rank three;
- compatibility of the response ribbon realization with every route-capped active gauge state;
- comparison with DDD;
- the global five-support theorem.

No Lean, independent-review, peer-review, publication, release, arXiv, DOI, or merge status is implied.
