# Root-valued flows and the five-support lifting problem

## 1. The strengthening beyond ordinary cycle double covers

An indexed five-support cycle double cover of a finite cubic graph $G$ is a family

$$
(F_1,\ldots,F_5)
$$

of even edge sets such that every edge of $G$ lies in exactly two of the $F_i$. Empty supports and repeated support components are allowed. Minimal circuit decomposition is postponed; the natural object is the indexed even cover.

Put

$$
E_5=\left\{x\in\mathbf F_2^5:\sum_i x_i=0\right\}
$$

and let

$$
R_5=\{e_i+e_j:1\le i<j\le5\}
$$

be its ten weight-two roots.

For an edge contained in supports $F_i,F_j$, assign the root $e_i+e_j$. Coordinatewise evenness is precisely Kirchhoff conservation. Conversely, every root-valued $E_5$-flow recovers the five supports from its coordinates.

### Theorem 1.1 — root-flow equivalence

Indexed five-support cycle double covers of $G$ are equivalent to nowhere-zero flows

$$
\lambda:E(G)\longrightarrow R_5\subset E_5.
$$

At every cubic vertex the three incident roots are

$$
e_i+e_j,\qquad e_j+e_k,\qquad e_k+e_i
$$

for one three-set $\{i,j,k\}\subset[5]$; equivalently, they form a triangle of $K_5$.

This is the intrinsic five-support object. The global open problem is not ordinary binary-flow existence in a rank-four group, but the requirement that every nonzero value lie in the ten-root orbit $R_5$.

## 2. Relation to the AffineCDC compatibility theorem

Let

$$
f:E(G)\to\Gamma\setminus\{0\},
\qquad \Gamma\cong\mathbf F_2^3,
$$

be a nowhere-zero Fano flow on a finite cubic graph. The rank-three affine compatibility theorem produces a compatible root lift

$$
g:E(G)\to E(K_8),
$$

where the eight support indices are naturally the points of $\Gamma$ and a root over direction $h\ne0$ is an affine edge

$$
\{s,s+h\}.
$$

This is the plus-type six-dimensional orthogonal model. Invariantly, the compatible lift is a nowhere-zero anisotropic flow in a quadratic space of type $O^+(6,2)$.

A five-support cover asks for a stronger confinement: after an appropriate five-coordinate identification, the same graph should carry a root-valued flow in the minus-type four-dimensional space $(E_5,q_5)$.

Thus the strengthening is naturally

$$
\boxed{
O^+(6,2)\text{ anisotropic root lift}
\longrightarrow
O^-(4,2)\text{ root-valued lift}.
}
$$

It is not a request to delete three arbitrary supports from one fixed eight-support witness. One may change the Fano flow, the compatible lift, the embedding, and the support identification.

## 3. Equivalent global formulations

The root-valued $E_5$ flow has several exact coordinate-free presentations. They are equivalent descriptions of one object, not competing conjectures.

### 3.1 Triangle labelling in $K_5$

Identify the ten roots with the ten edges of $K_5$. Then a five-support cover is a labelling of every graph edge by an edge of $K_5$ such that every cubic vertex receives the three edges of a triangle.

### 3.2 Cographic map

The triangle condition says that every source vertex circuit is sent to a target triangle circuit. Hence the root labelling defines a cycle-continuous map

$$
M(G)\longrightarrow M^*(K_5),
$$

or, equivalently, a cographic representation of the local support triangles.

### 3.3 Matching plus a four-flow

Choose one support coordinate as distinguished. Roots incident with that coordinate form a matching, because the same root coordinate cannot occur twice at a cubic vertex without forcing a zero third value. Removing that matching leaves a degree-two system carrying the three nonzero values of $\mathbf F_2^2$.

Conversely, a matching together with a nowhere-zero $\mathbf F_2^2$ flow on its complement reconstructs the local $K_5$ triangles.

### Theorem 3.1 — matching/four-flow equivalence

A cubic graph has an indexed five-support cover if and only if it admits a matching $M$ such that $G-M$ carries the appropriate nowhere-zero four-flow with the prescribed terminal behaviour.

### 3.4 Quadratic cycle equation

After choosing coordinates, the root condition can be expressed by a quadratic equation on binary cycles. The Schur product of two cycle coordinates must have zero boundary in the relevant quotient. This is the same obstruction seen in the matching-complement description.

### 3.5 Singular quotient lifting

For a permutation or quotient map $Q$ on $E_5$, each allowed quotient value has a finite root fibre. A root-valued lift is a global section of these edge fibres satisfying the cubic vertex relations. This local-system presentation becomes decisive in the rainbow-holonomy branch.

## 4. Fixed Fano flow and a five-coordinate slice

Fix a plane

$$
W\le\Gamma,
\qquad \dim W=2.
$$

Let $G_W$ be the spanning subgraph whose edges have flow values in $W$. Every nonisolated vertex of $G_W$ has degree one or three. A five-coordinate slice parallel to $W$ exists precisely when a component obstruction vanishes on every connected component of $G_W$.

Choose $a\notin W$ and write

$$
f(e)=w_e+b_ea,
\qquad w_e\in W,\quad b_e\in\mathbf F_2.
$$

At a degree-one vertex of $G_W$, the two outside-$W$ edges determine one binary boundary contribution. Summing over a component gives the obstruction bit.

### Theorem 4.1 — component-parity criterion

For each component $K$ of $G_W$, the following four parities are equal:

$$
\left|
\{e\in\delta_G(K):f(e)=c\}
\right|\pmod2,
\qquad c\in\Gamma\setminus W.
$$

Call the common value $\chi_W(K)$. A compatible five-coordinate lift with direction plane $W$ exists if and only if

$$
\chi_W(K)=0
$$

for every component $K$ of $G_W$.

Equivalently, after contracting the $G_W$ components, every outside-colour class is Eulerian in the quotient graph.

### Proof synthesis

Summing the flow equations over $K$ cancels internal edges and gives a linear relation among the four outside colours. Those four colours form an affine $W$-plane and possess one nontrivial binary relation, their total sum. Therefore their boundary parity vector is either $0000$ or $1111$. The local affine-lift obstruction counts one chosen outside colour, so it equals this common parity.

This is the coordinate-free form of the original affine component obstruction.

## 5. Singular-line, Schur, stress, and colour-cut presentations

The fixed-plane obstruction has several useful presentations.

### 5.1 Singular-line quotient

Quotient the local root fibres by the singular direction associated with $W$. The local choices become affine lines. The only obstruction to choosing a compatible section is the parity around each connected quotient component. This yields exactly $\chi_W(K)$.

### 5.2 Schur boundary

Choose two binary cycle coordinates $x,y$ for the quotient four-flow. Then

$$
\partial(x*y)
$$

is the same component obstruction. The five-support slice exists exactly when the Schur word is a cycle after passage to the relevant quotient.

### 5.3 Dual stress

The obstruction vanishes if and only if it pairs trivially with every relative equilibrium stress. The dual certificates are harmonic functions constant on the appropriate quotient components.

### 5.4 Fourier and Möbius formulations

Fourier expansion over the affine choice space separates the uniform orbit average from nonuniform stress characters. Möbius inversion over the arrangement of bad affine subspaces gives a Fourier-free equivalent. These are proof-family tools for controllability and counting; they do not define a different five-support object.

## 6. A complete fixed-plane criterion and its limits

For a fixed Fano flow $f$, define

$$
\mathfrak O_f(W)
=
\{K\in\pi_0(G_W):\chi_W(K)=1\}.
$$

Then

$$
\boxed{
\text{$f$ has a five-coordinate compatible lift}
\iff
\exists W\le\Gamma,\ \dim W=2,
\quad \mathfrak O_f(W)=\varnothing.
}
$$

This is a complete criterion for the specified five-coordinate lifting route above the fixed flow.

It is not the complete graph-level five-support criterion. The graph-level problem may choose another Fano flow, and the surface/dual formulation permits componentwise support identifications that do not factor through one global five-coordinate quotient.

## 7. The cube certificate and the fixed-flow negative boundary

There is an explicit cube Fano flow for which every plane $W$ has an obstructed component. In colour-cut form, for every one of the seven planes there is a component whose four outside colours cross its boundary oddly.

Consequently:

$$
\boxed{
\text{not every fixed nowhere-zero Fano flow admits a five-support lift.}
}
$$

The certificate requires six indexed supports in that fixed-flow fibre. It does not refute the graph-level five-support conjecture, because another Fano flow or a non-factorable componentwise lift may succeed.

## 8. Strong sufficient templates

Several useful sufficient conditions sit strictly inside the complete criterion.

### 8.1 Rank-two flow

If all values of $f$ lie in one plane $W$, then $G_W=G$ and the boundary is empty. This recovers the immediate consequence of a nowhere-zero $\mathbf F_2^2$ flow, equivalently a Tait three-edge-colouring.

### 8.2 Unused matching

For an eight-support root lift, suppose three pairwise disjoint root labels are unused. Identifying the endpoints of each unused pair maps the used-label graph into a five-clique of the half-cube, producing a five-support cover.

The $420$ three-edge matchings of $K_8$ form exactly three $AGL(3,2)$ orbits:

1. three parallel directions;
2. exactly two parallel directions;
3. three independent directions.

These are three restricted lifting templates, not three exhaustive obstruction types.

### 8.3 Seven affine-plane residues

For each linear plane $W\le\Gamma$, one can define a gauge-invariant residue measuring whether one of the two affine planes parallel to $W$ can become an unused $K_4$. Vanishing of any residue gives five supports.

These seven tests are strong fixed-template sufficient conditions. They are not equivalent to the complete componentwise surface criterion.

## 9. Proof architecture

The natural logical order is:

$$
\boxed{
\begin{array}{c}
\text{five indexed even supports}\\
\Updownarrow\\
\text{root-valued }E_5\text{ flow}\\
\Updownarrow\\
\text{$K_5$ triangle / matching--four-flow / quadratic-cycle data}\\
\Downarrow\\
\text{choose a Fano projection and compatible eight-support lift}\\
\Downarrow\\
\text{fixed-plane singular quotient and component obstruction}\\
\Downarrow\\
\text{vary the lift, the surface, and finally the Fano flow.}
\end{array}
}
$$

The first three lines are global equivalences. The fixed-plane criterion is a complete theorem only after the projection and plane are fixed. The final variation is the unresolved global mechanism.

## 10. Reliability boundary

The following are theorem-level within the public checkpoint:

- root-flow equivalence;
- local $K_5$ triangle law;
- matching/four-flow, quadratic-cycle, cographic, and singular-quotient equivalences;
- universal eight-support root-lift existence above a cubic Fano flow;
- fixed-plane component-parity and colour-cut criteria;
- dual stress and Schur-boundary formulations;
- unused-matching compression and its three affine orbit types.

Exact finite computation supports the cube certificate and selected coordinate tables. The global five-support theorem, universal success of any plane template, and universal escape from all fixed-flow obstructions remain open. None of these statements acquires Lean, independent-review, peer-review, or publication status through this reconstruction.