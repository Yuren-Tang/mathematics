# Ribbon intersection geometry of the physical response form

## 1. Purpose

The natural-transversal theorem associates to a cubic multigraph `G` the line-graph transition carrier

$$
F=\mathcal L(G)
$$

and the physical cycle--cut exact sequence

$$
0
\longrightarrow
\operatorname{Cut}(G)
\longrightarrow
\operatorname{Cocycle}(M_\tau(F))
\longrightarrow
\operatorname{Cycle}(G)
\longrightarrow
0.
$$

After ordering the two cross transitions at every edge, the full cocycle code has coordinates

$$
(z,a,z+a)
$$

and is controlled by a symmetric response form

$$
\mathcal B_G:
\operatorname{Cycle}(G)^2
\longrightarrow
\mathbf F_2.
$$

This chapter identifies the geometry behind that form.

The canonical local circuit partition of `F` has one circuit for every vertex of `G`.  Thicken these circuits to vertex discs and replace every line vertex `v_e` by an edge band.  The two cross transitions at `v_e` are exactly the two possible band attachments relative to chosen orientations of the incident vertex circuits.  A choice of one cross transition at every edge therefore produces a signed ribbon realization

$$
\mathfrak R
$$

with spine `G`.

The full transition-cocycle code is the topological `L`-space of this ribbon graph, and the response form is the mod-two intersection pairing on

$$
H_1(\mathfrak R;\mathbf F_2)
\cong
\operatorname{Cycle}(G).
$$

Consequently:

- the radical is the boundary-cycle space;
- the rank is the Euler genus;
- the form is alternating exactly in the orientable case;
- a partial Petrial at an edge adds the corresponding coordinate diagonal form.

This is the exact bridge from the new cap-response frontier back to the established gauge/Petrial surface architecture.

## 2. Signed ribbon realization of the natural partition

Let

$$
P_{\mathrm{loc}}
$$

be the circuit partition of `F=\mathcal L(G)` which uses the local transition at every line vertex.  Its circuits are

$$
\Delta_x,
\qquad x\in V(G),
$$

the vertex triangles of `G`.

Choose an orientation of every circuit `\Delta_x`.  At a line vertex `v_e`, the local transition pairs the two half-edges belonging to each endpoint circuit.  The other two transitions pair the endpoint sides across `e`.

Fix an ordering

$$
x_e^0,
\qquad
x_e^1
$$

of those two cross transitions.

Construct a ribbon surface `\mathfrak R` as follows.

1. Replace every oriented circuit `\Delta_x` by an oriented vertex disc whose attaching intervals occur in the cyclic order inherited from `\Delta_x`.
2. For every edge `e`, attach one rectangular band between its two attaching intervals.
3. Use the attachment encoded by `x_e^0`; the alternative `x_e^1` is obtained by inserting one half-twist in that band.

The resulting surface with boundary deformation-retracts onto `G`.  Reversing the auxiliary orientation of a vertex circuit gives the usual signed-rotation vertex switch and does not alter the ribbon graph up to the standard equivalence.

Thus a cross-transition ordering determines a signed ribbon realization, with the expected vertex-switch redundancy.

## 3. Topological edge coordinates

Remove a small open disc from the interior of every vertex disc of `\mathfrak R`; denote the punctured surface by

$$
\widehat{\mathfrak R}.
$$

For each edge band `e`, choose two relative arcs:

- `\alpha_e`, a co-core crossing the band from one side to the other;
- `\beta_e`, a longitudinal arc following the band between the puncture boundaries at its ends.

For an absolute mod-two cycle

$$
\gamma\in H_1(\widehat{\mathfrak R};\mathbf F_2),
$$

define

$$
\Phi_{\mathfrak R}(\gamma)
=
\left(
(\gamma\cdot\alpha_e)_{e\in E(G)},
(\gamma\cdot\beta_e)_{e\in E(G)}
\right)
\in
\mathbf F_2^{E(G)}\oplus\mathbf F_2^{E(G)}.
$$

The first coordinate records which edge bands the cycle traverses.  Hence

$$
(\gamma\cdot\alpha_e)_e
\in
\operatorname{Cycle}(G).
$$

The second coordinate records the side response of the cycle to the signed band attachments.

The outer boundary of each connected component maps to zero, so the image has dimension `|E(G)|`, equal to half the ambient dimension.

## 4. Transition cocycles equal the ribbon `L`-space

Let

$$
\mathscr L_G
\subseteq
\mathbf F_2^{E(G)}\oplus\mathbf F_2^{E(G)}
$$

be the full transition-matroid cocycle code in the local/cross coordinates `(z,a)`.

### Theorem 4.1 — topological realization of the cocycle code

Under the above signed ribbon realization,

$$
\boxed{
\mathscr L_G
=
\operatorname{im}\Phi_{\mathfrak R}.
}
$$

#### Proof

At one edge band there are four local possibilities for an absolute cycle after mod-two simplification:

1. it avoids the band;
2. it crosses the co-core but not the longitudinal arc;
3. it meets the longitudinal arc but not the co-core;
4. it meets both.

The corresponding transition words are respectively

$$
(0,0,0),
\qquad
(1,0,1),
\qquad
(0,1,1),
\qquad
(1,1,0),
$$

which are exactly the zero word and the three even weight-two words on the transition triple

$$
\{\ell_e,x_e^0,x_e^1\}.
$$

Following a topological cycle through the vertex discs imposes precisely the row-space compatibility condition of the transition matroid: the local words concatenate around the circuits of the natural partition.  Thus

$$
\operatorname{im}\Phi_{\mathfrak R}
\subseteq
\mathscr L_G.
$$

Both spaces have dimension `|E(G)|`.  The image of `\Phi_{\mathfrak R}` has this dimension because the punctured ribbon graph has first homology dimension `|E(G)|+c(G)` and its `c(G)` outer boundary classes form exactly the kernel.  The transition cocycle space has dimension `|E(G)|`, the rank of `M_\tau(F)`.  Hence the inclusion is equality. ∎

This is the line-graph instance of the general ribbon-graph `L`-space construction.

## 5. Response equals mod-two intersection

The surface intersection pairing on absolute homology is

$$
I_{\mathfrak R}:
H_1(\mathfrak R;\mathbf F_2)^2
\longrightarrow
\mathbf F_2.
$$

Use the deformation retraction to identify

$$
H_1(\mathfrak R;\mathbf F_2)
\cong
\operatorname{Cycle}(G).
$$

### Theorem 5.1 — ribbon-intersection response theorem

For all physical cycles

$$
z,z'\in\operatorname{Cycle}(G),
$$

one has

$$
\boxed{
\mathcal B_G(z,z')
=
I_{\mathfrak R}(z,z').
}
$$

#### Proof

Choose topological representatives `\gamma,\gamma'` with

$$
\Phi_{\mathfrak R}(\gamma)=(z,a),
\qquad
\Phi_{\mathfrak R}(\gamma')=(z',a').
$$

Push `\gamma` slightly toward the longitudinal side of every band and keep `\gamma'` on the spine side.  Intersections may then be localized band by band.  In band `e`, an intersection occurs exactly when `\gamma` meets `\beta_e` and `\gamma'` crosses the co-core `\alpha_e`.  Therefore

$$
I_{\mathfrak R}(\gamma,\gamma')
=
\sum_e a_ez'_e
=
a\cdot z'.
$$

By definition of the physical response form,

$$
a\cdot z'
=
\mathcal B_G(z,z').
$$

The symmetric equality with `a'\cdot z` is the symmetry of surface intersection over `\mathbf F_2`, equivalently the Lagrangian identity for `\mathscr L_G`. ∎

Thus the apparently algebraic extension form is the ordinary intersection form of a signed ribbon embedding of the physical cubic graph.

## 6. Radical and boundary cycles

Let

$$
b(\mathfrak R)
$$

be the number of boundary components and let

$$
c(G)
$$

be the number of connected components.

The inclusion of the boundary induces

$$
H_1(\partial\mathfrak R;\mathbf F_2)
\longrightarrow
H_1(\mathfrak R;\mathbf F_2).
$$

### Theorem 6.1 — boundary-radical theorem

The radical of the response form is exactly the image of the boundary homology:

$$
\boxed{
\operatorname{rad}\mathcal B_G
=
\operatorname{im}
\bigl(
H_1(\partial\mathfrak R;\mathbf F_2)
\to
H_1(\mathfrak R;\mathbf F_2)
\bigr).
}
$$

Moreover,

$$
\boxed{
\dim\operatorname{rad}\mathcal B_G
=
b(\mathfrak R)-c(G).
}
$$

#### Proof

The absolute intersection map factors as

$$
H_1(\mathfrak R)
\longrightarrow
H_1(\mathfrak R,\partial\mathfrak R)
\xrightarrow{\mathrm{PD}}
H^1(\mathfrak R),
$$

where Poincaré--Lefschetz duality over `\mathbf F_2` is nondegenerate for orientable and nonorientable surfaces alike.  Hence the radical is the kernel of the first arrow.

The long exact sequence of the pair identifies this kernel with the image of `H_1(\partial\mathfrak R)`.  On each connected component, the sum of all boundary classes is zero and this is the only relation.  Therefore the image has dimension one less than the number of boundary components on that connected component.  Summing over components gives `b(\mathfrak R)-c(G)`. ∎

A response cycle lies in the radical exactly when it is homologous to a sum of boundary components of the ribbon surface.

## 7. Rank, Euler genus, and orientability

Let

$$
\gamma(\mathfrak R)
$$

be the total Euler genus: twice the orientable genus on orientable components and the nonorientable genus on nonorientable components.

Because `\mathfrak R` retracts onto `G`,

$$
\dim H_1(\mathfrak R)
=
|E(G)|-|V(G)|+c(G).
$$

Euler's formula for a surface with boundary gives

$$
|V(G)|-|E(G)|
=
2c(G)-\gamma(\mathfrak R)-b(\mathfrak R).
$$

### Corollary 7.1 — genus-rank theorem

$$
\boxed{
\operatorname{rank}\mathcal B_G
=
\gamma(\mathfrak R).
}
$$

#### Proof

Subtract the radical dimension from the homology dimension:

$$
\begin{aligned}
\operatorname{rank}\mathcal B_G
&=
\bigl(|E|-|V|+c\bigr)-\bigl(b-c\bigr)\\
&=
|E|-|V|+2c-b\\
&=
\gamma(\mathfrak R).
\end{aligned}
$$

∎

### Corollary 7.2 — orientability criterion

The response form is alternating,

$$
\mathcal B_G(z,z)=0
\quad\text{for all }z,
$$

if and only if every component of `\mathfrak R` is orientable.

#### Proof

On an orientable surface every mod-two one-cycle has zero self-intersection.  A nonorientable component contains a one-sided simple closed curve, whose mod-two self-intersection is one. ∎

Thus response rank measures Euler genus and the diagonal detects orientability.

## 8. Partial Petrials and diagonal response

Let

$$
T\subseteq E(G).
$$

Form the partial Petrial

$$
\mathfrak R^{\tau(T)}
$$

by inserting one half-twist in every band of `T`.

### Theorem 8.1 — Petrial response law

For all cycles `z,z'`,

$$
\boxed{
I_{\mathfrak R^{\tau(T)}}(z,z')
=
I_{\mathfrak R}(z,z')
+
\sum_{e\in T}z_ez'_e.
}
$$

Equivalently,

$$
\boxed{
\mathcal B_G^{\tau(T)}
=
\mathcal B_G
+
\sum_{e\in T}z_ez'_e.
}
$$

#### Proof

A half-twist in band `e` changes the local intersection of two traversing cycles by one exactly when both cycles use that band.  Its contribution is therefore `z_ez'_e`.  Different bands are disjoint, so their contributions add. ∎

This is precisely the diagonal-gauge law obtained algebraically by swapping the two cross-transition labels.

## 9. Interface with the AffineCDC gauge code

For one fixed Fano flow, the active gauge theorem identifies a reduced gauge word

$$
\lambda\in B_f
$$

with an admissible partial Petrial: `\lambda_e=1` swaps the two face-side identifications across edge `e`.

Whenever the route-capped response coordinates are chosen from the same side-identification data, Theorem 8.1 gives the exact vertical action

$$
\boxed{
\mathcal B_{g+\lambda}(z,z')
=
\mathcal B_g(z,z')
+
\sum_e\lambda_ez_ez'_e.
}
$$

The off-diagonal ribbon-intersection geometry is fixed by the underlying signed rotation structure; admissible gauge motion changes the response by the diagonal forms allowed by `B_f`.

This statement is an interface theorem, not yet a proof that every abstract response coordinate choice arises from one compatible root lift.  The required compatibility is that the cross-transition labels and the root-lift face-side identifications describe the same edge bands.

## 10. Consequence for the cap-response frontier

Write a cap cocircuit as

$$
(z,a,z+a),
$$

with

$$
a\bmod\operatorname{Cut}(G)
=
\mathcal B_G(z,-).
$$

The residual nonzero branch now has a topological dichotomy.

### Boundary/radical branch

If

$$
z\in\operatorname{rad}\mathcal B_G,
$$

then `z` is a boundary-homology class.  The response functional vanishes, so

$$
a\in\operatorname{Cut}(G).
$$

Adding the corresponding kernel cocycle gives an equivalent lift

$$
(z,0,z).
$$

The remaining task is to turn support-minimal boundary classes into a physical boundary component, separator, serial interface, or bounded replacement.

### Genuine genus branch

If

$$
z\notin\operatorname{rad}\mathcal B_G,
$$

then some physical cycle `z'` has

$$
\mathcal B_G(z,z')=1.
$$

The cap cocircuit therefore occupies a positive-Euler-genus carrier.  Its irreducible content lies in the nondegenerate quotient

$$
H_1(\mathfrak R)/\operatorname{rad}\mathcal B_G,
$$

whose dimension is exactly `\gamma(\mathfrak R)`.

Hence the former prime-response problem refines to:

$$
\boxed{
\text{boundary response}
\quad\text{or}\quad
\text{positive-genus response core}.
}
$$

## 11. Updated mechanism target

The next theorem should exploit the four AffineCDC scalar sheets and admissible Petrial code to prove one of:

1. a radical cap response contains a proper boundary component yielding a separator or serial interface;
2. an admissible gauge word reduces the Euler genus or moves the cap response into the radical;
3. a positive-genus response has a bounded symplectic or orthogonal handle supporting a local switch/replacement;
4. the only gauge-minimal positive-genus cap carrier is the physical DDD support-label class.

This target directly joins the current route-locked obstruction to the established vertical gauge and surface programme.  Pure incidence and pure isotropic connectivity are no longer the controlling layers.

## 12. Reliability boundary

Proved here:

- construction of a signed ribbon realization from the natural partition and cross choices;
- equality of the full transition cocycle code with the ribbon `L`-space;
- identification of the response form with mod-two surface intersection;
- radical as boundary homology;
- rank as Euler genus;
- alternating form exactly in the orientable case;
- partial Petrial diagonal law;
- the exact conditional interface with the active AffineCDC gauge code.

Open:

- a canonical response ribbon realization independent of auxiliary signed-rotation choices;
- proof that the route-capped response coordinates of every active endpoint coincide with one fixed root-lift surface without additional closure choices;
- boundary-component localisation for a support-minimal cap cocircuit;
- genus-reducing admissible gauge theorem;
- comparison of the residual positive-genus class with DDD;
- the global five-support theorem.

No Lean, independent-review, peer-review, publication, release, arXiv, DOI, or merge status is implied.
