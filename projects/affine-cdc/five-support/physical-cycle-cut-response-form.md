# The physical cycle--cut response form

## 1. Purpose

The natural-transversal exact sequence identifies the full cocycle space of the line-graph transition matroid as an extension

$$
0
\longrightarrow
\operatorname{Cut}(G)
\longrightarrow
\mathscr C^*_{\tau}(\mathcal L(G))
\longrightarrow
\operatorname{Cycle}(G)
\longrightarrow
0,
$$

where `G=\widehat Q` in the route-capped application.

This chapter identifies the extension datum exactly.

At every edge `e` of `G`, fix the local transition and label the two cross transitions as `x_e^0,x_e^1`.  Every cocycle meets the transition triple in even cardinality, so its local word has the form

$$
(z_e,a_e,z_e+a_e).
$$

The full cocycle space therefore becomes a subspace of

$$
\mathbf F_2^{E(G)}\oplus\mathbf F_2^{E(G)}.
$$

This subspace is Lagrangian for the standard symplectic form.  Its projection to the first factor is the physical cycle space and its kernel is the physical cut space.  Consequently the extension is controlled by a symmetric bilinear response form

$$
\mathcal B_G:
\operatorname{Cycle}(G)\times\operatorname{Cycle}(G)
\longrightarrow
\mathbf F_2.
$$

A pair `(z,a)` is a full transition-matroid cocycle exactly when `z` is a physical cycle and the edge word `a`, modulo cuts, represents the functional

$$
z'\longmapsto\mathcal B_G(z,z').
$$

Thus the residual prime cap obstruction is a support-minimal word in a physical Lagrangian cycle--cut code, not an arbitrary isotropic cocircuit.

## 2. Even transition coordinates

Let

$$
F=\mathcal L(G),
\qquad
m=|E(G)|=|V(F)|.
$$

At the line vertex `v_e`, denote the transition triple by

$$
\{\ell_e,x_e^0,x_e^1\},
$$

where `\ell_e` is the canonical local transition and the two cross transitions are given an arbitrary order.

Every cocycle meets this triple in zero or two elements.  Therefore its three indicator bits satisfy

$$
\ell_e+x_e^0+x_e^1=0.
$$

Define coordinates

$$
z_e=1_{\ell_e\in D},
\qquad
a_e=1_{x_e^0\in D}.
$$

Then automatically

$$
1_{x_e^1\in D}=z_e+a_e.
$$

Hence every cocycle `D` has one coordinate pair

$$
(z(D),a(D))
\in
\mathbf F_2^{E(G)}\oplus\mathbf F_2^{E(G)}.
$$

The active physical edge set of the cocycle is

$$
L(D)
=
\operatorname{supp}z(D)
\cup
\operatorname{supp}a(D).
$$

Indeed the transition triple is zero exactly when `(z_e,a_e)=(0,0)`; every other pair gives one of the three weight-two words.

## 3. The ambient symplectic form

On

$$
\mathbf F_2^{E(G)}\oplus\mathbf F_2^{E(G)}
$$

define

$$
\omega((z,a),(z',a'))
=
z\cdot a'+a\cdot z'.
$$

### Theorem 3.1 — Lagrangian cocycle code

The image

$$
\mathscr L_G
$$

of the full transition-matroid cocycle space in `(z,a)` coordinates is a Lagrangian subspace:

$$
\boxed{
\omega|_{\mathscr L_G}=0,
\qquad
\dim\mathscr L_G=m.
}
$$

#### Proof

Choose any Euler system of `F` and an `IAS` representation

$$
IAS(H)=(I\mid A\mid I+A),
$$

where `A` is the symmetric interlacement matrix.  In the corresponding vertex coordinates a row-space word has the form

$$
(y,yA,y+yA).
$$

Using the first two coordinates as a pair gives

$$
(y,yA).
$$

For two row vectors `y,y'`,

$$
\omega((y,yA),(y',y'A))
=
yAy'+yAy'
=0,
$$

because `A=A^T` and the field has characteristic two.

At one vertex, replacing the `IAS` transition labels by the physically fixed local transition and an ordering of the two cross transitions applies a permutation of the three nonzero vectors of `\mathbf F_2^2`.  Every such permutation is an element of

$$
GL(2,2)=Sp(2,2)
$$

and preserves the alternating form.  Hence isotropy survives the local relabelling at all vertices.

The transition matroid has rank `m`, so its cocycle space and hence `\mathscr L_G` have dimension `m`, exactly half the ambient dimension.  Thus the isotropic subspace is Lagrangian. ∎

## 4. Projection and kernel

Let

$$
Z(G)=\operatorname{Cycle}(G),
\qquad
B(G)=\operatorname{Cut}(G).
$$

The natural-transversal exact sequence gives:

$$
\operatorname{pr}_1(\mathscr L_G)=Z(G),
$$

and

$$
\ker(\operatorname{pr}_1|_{\mathscr L_G})
=
\{0\}\oplus B(G).
$$

Here a cut word `b` corresponds to the cocycle with both cross transitions on every edge of `\operatorname{supp}b`.

The ordinary edge dot product has

$$
B(G)=Z(G)^\perp.
$$

Therefore an edge word `a`, modulo the cut space, defines a linear functional on `Z(G)` by

$$
z'\longmapsto a\cdot z'.
$$

## 5. Definition of the response form

Let `z\in Z(G)`.  Choose any cocycle coordinate pair

$$
(z,a)\in\mathscr L_G.
$$

For `z'\in Z(G)`, define

$$
\boxed{
\mathcal B_G(z,z')
=
a\cdot z'.
}
$$

### Lemma 5.1 — well-definedness

The value is independent of the chosen cocycle lift `(z,a)`.

#### Proof

Two lifts differ by an element of the kernel:

$$
(z,a')+(z,a)=(0,b)
$$

with `b\in B(G)`.  Since every cut is orthogonal to every cycle,

$$
(a'+a)\cdot z'=b\cdot z'=0.
$$

Thus `a'\cdot z'=a\cdot z'`. ∎

### Theorem 5.2 — symmetric physical response

The map

$$
\mathcal B_G:
Z(G)\times Z(G)
\longrightarrow
\mathbf F_2
$$

is bilinear and symmetric:

$$
\boxed{
\mathcal B_G(z,z')
=
\mathcal B_G(z',z).
}
$$

#### Proof

Linearity follows from linearity of the cocycle space and the dot product.

Choose lifts `(z,a)` and `(z',a')`.  Since `\mathscr L_G` is isotropic,

$$
0
=
\omega((z,a),(z',a'))
=
z\cdot a'+a\cdot z'.
$$

The two terms are precisely

$$
\mathcal B_G(z',z)
\quad\text{and}\quad
\mathcal B_G(z,z').
$$

Hence they are equal. ∎

## 6. Exact characterization of full cocycles

### Theorem 6.1 — response-form membership criterion

A coordinate pair

$$
(z,a)
\in
\mathbf F_2^{E(G)}\oplus\mathbf F_2^{E(G)}
$$

belongs to the full transition-matroid cocycle code `\mathscr L_G` if and only if:

1. `z\in Z(G)`;
2. for every `z'\in Z(G)`,
   $$
   \boxed{
   a\cdot z'
   =
   \mathcal B_G(z,z').
   }
   $$

Equivalently, the coset of `a` in

$$
\mathbf F_2^{E(G)}/B(G)
$$

is exactly the functional `\mathcal B_G(z,-)`.

#### Proof

Necessity is the definition of the response form.

Conversely, choose one cocycle lift `(z,a_0)\in\mathscr L_G`, which exists because the natural projection is onto `Z(G)`.  The displayed equations imply

$$
(a+a_0)\cdot z'=0
$$

for every cycle `z'`.  Hence

$$
a+a_0\in Z(G)^\perp=B(G).
$$

Therefore `(0,a+a_0)` lies in the kernel of the exact sequence, and

$$
(z,a)
=
(z,a_0)+(0,a+a_0)
\in
\mathscr L_G.
$$

∎

Thus the full cocycle code is reconstructed from the pair

$$
(Z(G),\mathcal B_G).
$$

## 7. Gauge under cross-transition relabelling

At one edge `e`, swapping the names of the two cross transitions replaces

$$
a_e
\longmapsto
a_e+z_e.
$$

For a set `T\subseteq E(G)` of such swaps, put `t=1_T`.  Then

$$
a
\longmapsto
a+t\odot z,
$$

where `\odot` is coordinatewise product.

The response form changes by

$$
\boxed{
\mathcal B_G(z,z')
\longmapsto
\mathcal B_G(z,z')
+
\sum_{e\in T}z_ez'_e.
}
$$

Hence the cross-label-independent object is the diagonal-gauge class of `\mathcal B_G` under addition of coordinate diagonal forms.

The local transition, the cycle projection, the cut kernel, and the exact sequence are completely canonical.  Only the ordering of the two physical cross transitions produces this diagonal gauge.

## 8. Cap residue as boundary conditions

Return to the capped four-pole `G=\widehat Q`, with cap edges

$$
z_{12},z_{34}.
$$

For a cocycle coordinate `(z,a)`:

- `z_{rs}=1` means the local transition is present at cap `rs`;
- `z_{rs}=0` means it is absent;
- the two cross indicators are
  $$
  a_{rs},
  \qquad
  z_{rs}+a_{rs}.
  $$

A prescribed residue transition therefore imposes one affine coordinate condition on `(z,a)` at each cap.  The full cap-completion problem is now:

$$
\boxed{
\begin{array}{c}
z\in Z(\widehat Q),\
 a\cdot z'=\mathcal B_{\widehat Q}(z,z')\quad
 \forall z'\in Z(\widehat Q),\
\text{two prescribed cap cross coordinates},\
\text{transition-support minimality}.
\end{array}
}
$$

The cap word is simply

$$
(z_{12},z_{34}).
$$

The zero-cycle case `z=0` is exactly the physical cut-kernel branch already reduced to bonds.  The residual branch has `z\ne0`.

## 9. A necessary negative boundary

Cocircuit minimality does **not** force the physical cycle projection `z` to be one connected graph circuit.

An exact finite check on the cubic cube graph exhibits full transition-matroid cocircuits whose natural projection is the disjoint union of two four-cycles.  Thus one cannot reduce the prime branch by replacing `z` with a single physical cycle without additional use of the response form or the flow labels.

The correct irreducible object is therefore a support-minimal word of the Lagrangian response code, potentially with several physical cycle components coupled through the cross-coordinate functional `\mathcal B_G(z,-)`.

This finite statement is a negative boundary only; the general theory above does not depend on it.

## 10. Mechanism consequence

The nonflat full-rank frontier has now become a physical code problem.

### Closed branch

$$
z=0
\Longrightarrow
\text{physical bond and separator}.
$$

### Residual branch

$$
\boxed{
 z\ne0,
 \qquad
 a\bmod B(G)=\mathcal B_G(z,-),
}
$$

with two prescribed cap cross coordinates and cocircuit minimality.

The next theorem should exploit special constraints on the response form arising from:

- the common `\mathbf F_2^3` flow;
- the four affine scalar sheets;
- the three quotient Kempe systems;
- the fixed terminal route;
- aligned/crossed endpoint selectors;
- the physical `g`-component quotient `\Gamma_g`.

A successful theorem should show that a nonzero response word yields:

1. a proper cycle--cut decomposition or transition two-sum;
2. a crossed four-terminal projection breaking route-lock;
3. a bounded replacement or horizontal switch;
4. or one uniquely constrained prime response class comparable with the physical DDD support-label cocycle.

This is the current shortest mechanism path.  Abstract isotropic connectivity alone does not encode the response-form restrictions supplied by the flow.

## 11. Reliability boundary

Proved here:

- even-pair coordinates `(z,a,z+a)` for full cocycles;
- the Lagrangian property of the full cocycle code;
- the physical cycle image and cut kernel;
- the well-defined symmetric response form on the graph cycle space;
- the exact response-form membership criterion;
- diagonal gauge under cross-transition relabelling;
- cap residue as two affine boundary conditions.

Finite negative boundary:

- a cocircuit projection need not be a single connected graph circuit.

Not proved here:

- a closed formula for `\mathcal B_G` directly from the flow labels;
- decomposition of every multi-component cycle projection;
- physical composition for all nonzero response words;
- identification of a unique prime response class with DDD;
- the global five-support theorem.

No Lean, independent-review, peer-review, publication, release, arXiv, DOI, or merge status is implied.
