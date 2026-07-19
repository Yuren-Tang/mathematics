# Quartic nucleus transport and pairwise shell factorisation

## 1. Purpose

The quartic terminal-nucleus theorem gives a strict abstract recursion.  If all four sheets are concentrated, a quartic witness design of level `k` peels to one of level `k-1`.

This chapter identifies the exact transport structure carried by that peel.

1. The old and residual terminal nuclei are canonically isometric minus-type four-spaces.
2. The four distinguished closed-component blocks form the totally singular diagonal graph of that isometry.
3. The `D_8` route structure and the one-dimensional curvature carrier are transported without an algebraic twist.
4. For every pair of sheets, the large ribbon transition skeleton is obtained from the residual skeleton by adding one fixed two-vertex shell.  The shell contributes exactly two units of cycle rank.

Thus concentrated growth is not an arbitrary enlargement.  It is iteration of one canonical algebraic nucleus and one fixed pairwise transition-shell pattern.  The remaining difficulty is to control the scalar intervals, Kempe cycles, and original graph gluing carried by that shell.

## 2. Concentrated setup

Let

$$
(X,(\mathcal R_i),(e_i))
$$

be a concentrated quartic witness design of level `k\ge2`.  Put

$$
E=\{e_0,e_1,e_2,e_3\},
\qquad
Y=X\setminus E.
$$

For each sheet `i`, the distinguished block is

$$
D_i
=
(E\setminus\{e_i\})\cup\{y_i\},
$$

where the `y_i\in Y` are pairwise distinct.  The residual families

$$
\mathcal R_i'
=
\mathcal R_i\setminus\{D_i\}
$$

form a quartic witness design

$$
(Y,(\mathcal R_i'),(y_i))
$$

of level `k-1`.

Let

$$
E_X
=
\{x\in\mathbf F_2^X:|x|\equiv0\pmod2\},
\qquad
E_Y
=
\{x\in\mathbf F_2^Y:|x|\equiv0\pmod2\},
$$

with quadratic forms

$$
q(x)=\frac{|x|}{2}\pmod2.
$$

## 3. Old and residual terminal nuclei

The terminal nucleus of the large design is

$$
S_X
=
\langle s_0,s_1,s_2,s_3\rangle,
\qquad
s_i=1_X+e_i.
$$

The residual design has its own terminal nucleus

$$
S_Y
=
\langle t_0,t_1,t_2,t_3\rangle,
\qquad
 t_i=1_Y+y_i.
$$

Both ordered bases have Gram matrix

$$
K
=
\begin{pmatrix}
0&1&1&1\\
1&0&1&1\\
1&1&0&1\\
1&1&1&0
\end{pmatrix},
$$

and every basis vector is singular.

### Theorem 3.1 — canonical nucleus transport

There is a unique labelled quadratic isometry

$$
\boxed{
\varphi:S_X\longrightarrow S_Y,
\qquad
\varphi(s_i)=t_i.
}
$$

It sends

$$
s_\infty=s_0+s_1+s_2+s_3
$$

to

$$
t_\infty=t_0+t_1+t_2+t_3,
$$

and is equivariant under every relabelling of the four sheets.  In particular it is equivariant under the route stabiliser

$$
D_8\le S_4.
$$

#### Proof

The assignment preserves the quadratic values of the basis vectors and all pairwise polar products.  Since the `s_i` and `t_i` are bases of nondegenerate four-spaces, it extends uniquely to a quadratic isometry.  The formulas for the total sums and equivariance are immediate from the labelled definition.  ∎

## 4. Distinguished blocks as a singular diagonal

The concentrated peeling identity is

$$
1_{D_i}+s_i=t_i.
$$

Equivalently,

$$
\boxed{1_{D_i}=s_i+t_i.}
$$

Here `S_X` is orthogonal to `E_Y`, hence to `S_Y`.  Therefore the eight-dimensional space

$$
S_X\perp S_Y
$$

is the orthogonal sum of two minus-type four-spaces.

### Theorem 4.1 — diagonal gluing space

Let

$$
L
=
\langle1_{D_0},1_{D_1},1_{D_2},1_{D_3}\rangle.
$$

Then

$$
\boxed{
L
=
\{x+\varphi(x):x\in S_X\},
}
$$

so `L` is the graph of the canonical isometry `\varphi`.  It is a four-dimensional maximal totally singular subspace of

$$
S_X\perp S_Y.
$$

#### Proof

The displayed block identity gives the graph description on the basis and hence on the whole span.  For `x,x'\in S_X`,

$$
q(x+\varphi(x))
=q(x)+q(\varphi(x))
=0,
$$

and

$$
b(x+\varphi(x),x'+\varphi(x'))
=b(x,x')+b(\varphi(x),\varphi(x'))
=0.
$$

Thus `L` is totally singular.  Its dimension is four because it is the graph of an isomorphism.  The orthogonal sum of two four-dimensional minus spaces has Witt index four, so `L` is maximal totally singular.  ∎

This shows that a concentrated extension contains no hidden algebraic twist between successive nuclei.  It glues two identical minus-type geometries along the diagonal of their canonical labelled isometry.

## 5. Transport of the curvature carrier

The old and residual one-dimensional curvature carriers are

$$
\mathcal C_X
=
S_X/s_\infty^\perp,
\qquad
\mathcal C_Y
=
S_Y/t_\infty^\perp.
$$

### Corollary 5.1 — curvature transport

The isometry `\varphi` induces a canonical `D_8`-equivariant isomorphism

$$
\boxed{
\bar\varphi:
\mathcal C_X
\longrightarrow
\mathcal C_Y.
}
$$

It sends the unique nonzero parity class to the unique nonzero parity class.

#### Proof

Since `\varphi(s_\infty)=t_\infty` and `\varphi` preserves the polar form,

$$
\varphi(s_\infty^\perp)=t_\infty^\perp.
$$

Hence it descends to the quotients.  Both quotients are one-dimensional, and the induced map is nonzero.  Equivariance follows from Theorem 3.1.  ∎

This is an exact incidence-level transport theorem.  A physical peel must still prove that the side word induced on the residual terminal edges `y_i` is the transported physical curvature word, rather than merely an available labelled copy of it.

## 6. Pairwise transition skeletons

Fix distinct sheets `i,j`, and let `\ell,m` be the other two sheet indices.

Let

$$
T_{ij}(X)
$$

be the pairwise transition skeleton of the large design, and let

$$
T_{ij}(Y)
$$

be the transition skeleton of the residual design.

In `T_{ij}(Y)`, the terminal leaves are indexed by `y_i` and `y_j`.  Denote them by

$$
r_i,
\qquad
r_j.
$$

In `T_{ij}(X)`, the old terminal leaves are indexed by `e_i` and `e_j`; denote them by

$$
s_i,
\qquad
s_j.
$$

The distinguished blocks `D_i` and `D_j` are block vertices on the two bipartite sides.

### Theorem 6.1 — exact shell factorisation

The graph `T_{ij}(X)` is obtained from `T_{ij}(Y)` by the following canonical operation.

1. Identify the residual terminal vertex `r_i` with the new block vertex `D_i`.
2. Identify the residual terminal vertex `r_j` with the new block vertex `D_j`.
3. Add the two parallel edges
   $$
   e_\ell,e_m
   $$
   between `D_i` and `D_j`.
4. Add a new terminal leaf `s_i` joined to `D_j` by the edge `e_i`.
5. Add a new terminal leaf `s_j` joined to `D_i` by the edge `e_j`.

Equivalently, concentrated nucleus extension replaces the two residual terminal leaves by two degree-four block vertices, joins them by two parallel witness edges, and attaches two new terminal leaves crosswise.

#### Proof

The residual witness edges in `Y` retain exactly their old block incidences, except for `y_i` and `y_j`.

- In the residual design, `y_i` is omitted in sheet `i` and belongs to one residual `j`-block.  In the large design, it belongs to `D_i` in sheet `i` and to the same residual `j`-block.  Thus the residual terminal vertex `r_i` becomes `D_i`.
- Similarly, `r_j` becomes `D_j`.
- The old terminal point `e_i` is omitted in sheet `i` and lies in `D_j`, giving the edge `s_iD_j`.
- The old terminal point `e_j` lies in `D_i` and is omitted in sheet `j`, giving the edge `D_is_j`.
- Each of `e_\ell,e_m` belongs to both `D_i` and `D_j`, giving two parallel edges between those vertices.

No other incidence changes.  ∎

The shell is therefore the fixed labelled two-vertex graph

$$
\boxed{
\text{old terminal}
-
D_j
\mathrel{\substack{e_\ell\\[-1mm]e_m}}
D_i
-
\text{old terminal},
}
$$

with one residual terminal edge also incident at each `D`-vertex.

## 7. Exact cycle-rank increment

The residual skeleton has

$$
|V(T_{ij}(Y))|=2(k-1)+2=2k,
$$

and

$$
|E(T_{ij}(Y))|=4(k-1)+1=4k-3.
$$

The shell factorisation adds two vertices and four edges.

### Corollary 7.1 — two-cycle shell

One has

$$
\boxed{
\beta_1(T_{ij}(X))
=
\beta_1(T_{ij}(Y))+2.
}
$$

Thus every concentrated nucleus layer contributes exactly two independent cycles to each pairwise transition skeleton.

This explains recursively the formula

$$
\beta_1(T_{ij}(X))=2k.
$$

## 8. Ribbon transport

In a physical quartic core, every block vertex carries the cyclic order of its four witness edges on the corresponding scalar circuit.

Under Theorem 6.1:

- every residual block rotation is unchanged;
- all new ribbon data are concentrated at the two shell vertices `D_i,D_j`;
- the incident labels at `D_i` are
  $$
  e_j,e_\ell,e_m,y_i;
  $$
- the incident labels at `D_j` are
  $$
  e_i,e_\ell,e_m,y_j.
  $$

### Corollary 8.1 — bounded pairwise ribbon shell

The pairwise ribbon skeleton of a concentrated level-`k` core is the residual level-`k-1` ribbon skeleton plus two four-valent rotation vertices.  Up to reversal, each new vertex has only three cyclic-order types on its four labelled ports.

Hence the pairwise ribbon enlargement is finite-state.  All unbounded pairwise topology is carried recursively by the residual skeleton.

This does not yet make the shell a bounded replacement in the original four-pole.  Each rotation vertex represents a scalar closed component with four intervening non-`g` intervals, and those intervals may have unbounded graph length and side semantics.

## 9. Kempe and endpoint enrichment

The quotient Tait-phase model labels every witness `g`-edge by

$$
(q_v,q_w)
\in
(\mathbf F_2^2\setminus\{0\})^2
$$

and supplies three Kempe cycle systems relating the four sheets.

A concentrated pairwise peel therefore separates the enrichment into:

1. the complete residual enrichment on `T_{ij}(Y)`;
2. finite endpoint labels on the four old terminal edges and the two residual terminal edges incident with the shell;
3. two cyclic orders at `D_i,D_j`;
4. the four scalar intervals between successive shell ports;
5. the way the three Kempe cycle systems traverse those intervals and the two parallel shell edges.

The first three items are finite.  The only remaining unbounded shell data are the interval transports and their attachments to the residual core.

## 10. Updated physical target

The concentrated branch is now reduced to a bounded-shell transport theorem.

A sufficient theorem would prove that each four-port scalar interval admits a finite transfer state such that one of the following holds:

1. the two-vertex shell is removable and the residual quartic core inherits the transported curvature class;
2. one interval exposes a two-edge transition split or smaller cyclic separator;
3. two repeated enriched interval states give a bounded replacement;
4. incompatible shell rotations force a crossed DDD/Petersen resolution;
5. the only irreducible shell state is the physical `D_8` class.

The strict abstract measure is already available:

$$
k\longmapsto k-1.
$$

What remains is to prove that the physical shell either realises that decrease or itself yields bounded graph progress.

## 11. Reliability boundary

Proved here:

- canonical quadratic isometry between successive terminal nuclei;
- diagonal totally singular description of the four distinguished blocks;
- `D_8`-equivariant transport of the one-dimensional curvature carrier;
- exact pairwise transition-shell factorisation;
- exact cycle-rank increment by two;
- concentration of all new pairwise ribbon data at two four-valent vertices.

Not proved here:

- physical transport of the actual side word to the residual omitted edges;
- finite transfer classification of the four scalar intervals;
- simultaneous compatibility of the six pairwise shells;
- composition-safe deletion of a concentrated nucleus layer;
- identification of an irreducible shell with the physical DDD cocycle;
- the global five-support theorem.

No Lean, independent-review, peer-review, publication, release, arXiv, or DOI status is implied.
