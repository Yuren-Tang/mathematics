# Quartic witness designs: abstract existence and symplectic form

## 1. Purpose

The nonflat common-cut localisation theorem leaves one unbounded incidence pattern.  A residual witness has size

$$
|\eta|=4k+1
$$

and carries four near-resolutions by four-element closed-component blocks.  The complete set of `4k` block vectors is a basis of the even-weight space on `\eta`.

This chapter answers the first purely combinatorial question about that endpoint:

> do the near-resolution and basis axioms themselves force `k=1`, or at least bound `k`?

They do not.  Quartic witness designs exist for every `k\ge1`.  Therefore no argument using only common-cut parity, block sizes, omitted points, and binary rank can eliminate the unbounded branch.  Any further reduction must use physical data coming from one route-locked `\mathbf F_2^3` flow.

## 2. Abstract quartic witness designs

Let `X` be a set of size `4k+1`.  A quartic witness design consists of four families

$$
\mathcal R_i
\qquad(i\in\{0,1,2,3\})
$$

and four pairwise distinct omitted points `e_i\in X` such that:

1. `\mathcal R_i` partitions `X\setminus\{e_i\}` into `k` four-element blocks;
2. the `4k` block incidence vectors form a basis of
   $$
   E_X
   =
   \left\{x\in\mathbf F_2^X:\sum_{u\in X}x_u=0\right\};
   $$
3. the four omitted points are decorated by an odd terminal-side word.

The side word is independent of the incidence-rank axioms, so one may prescribe any odd word once the block system is constructed.

## 3. A quartic ladder in every size

### Theorem 3.1 — unbounded abstract quartic cores

For every integer `k\ge1`, there exists a quartic witness design on `4k+1` points.

### Construction

Put

$$
X_k
=
\{z\}
\sqcup
\{x_{j,i}:0\le j\le k-1,\ 0\le i\le3\}.
$$

Thus `|X_k|=4k+1`.  For sheet `i`, omit

$$
e_i=x_{0,i}.
$$

For `0\le j\le k-2`, define

$$
B_{i,j}
=
\{x_{j,h}:h\ne i\}
\cup
\{x_{j+1,i}\},
$$

and define the final block

$$
B_{i,k-1}
=
\{x_{k-1,h}:h\ne i\}
\cup
\{z\}.
$$

Let

$$
\mathcal R_i
=
\{B_{i,0},\ldots,B_{i,k-1}\}.
$$

Each block has four elements.

### Lemma 3.2 — near-resolution property

For every `i`, the blocks in `\mathcal R_i` partition `X_k\setminus\{e_i\}`.

#### Proof

In the initial layer `j=0`, the block `B_{i,0}` contains the three points `x_{0,h}` with `h\ne i`; the omitted point is `x_{0,i}`.

For an intermediate layer `1\le j\le k-1`, the point `x_{j,i}` occurs in the preceding block `B_{i,j-1}`, while the three points `x_{j,h}` with `h\ne i` occur in `B_{i,j}`.  Hence every layer point other than `e_i` occurs exactly once.  The point `z` occurs exactly once, in `B_{i,k-1}`.  Therefore the blocks are pairwise disjoint and cover precisely `X_k\setminus\{e_i\}`.  ∎

### Lemma 3.3 — independence of all block vectors

The `4k` vectors

$$
1_{B_{i,j}}
\qquad
(0\le i\le3,\ 0\le j\le k-1)
$$

are linearly independent over `\mathbf F_2`.

#### Proof

Suppose

$$
\sum_{i=0}^3\sum_{j=0}^{k-1}
\alpha_{i,j}1_{B_{i,j}}
=0.
$$

Consider first the coordinates `x_{0,s}`.  The point `x_{0,s}` occurs in `B_{i,0}` exactly when `i\ne s`, so

$$
\sum_{i\ne s}\alpha_{i,0}=0
\qquad(s=0,1,2,3).
$$

Let

$$
T_0=\sum_i\alpha_{i,0}.
$$

Then the displayed equations give `\alpha_{s,0}=T_0` for every `s`.  Hence

$$
T_0
=
\sum_s\alpha_{s,0}
=
4T_0
=0,
$$

so all `\alpha_{i,0}` vanish.

Proceed inductively.  Suppose all coefficients in levels below `j` vanish.  In the coordinate `x_{j,s}`, the only possible contribution from level `j-1` is `\alpha_{s,j-1}`, already zero, and the level-`j` contribution is

$$
\sum_{i\ne s}\alpha_{i,j}.
$$

The same four-equation argument forces every `\alpha_{i,j}` to vanish.  Induction through `j=k-1` proves that all coefficients are zero.  ∎

### Completion of the proof of Theorem 3.1

Every block has even weight, so all `4k` block vectors lie in `E_{X_k}`.  By Lemma 3.3 they are independent.  Since

$$
\dim E_{X_k}
=
|X_k|-1
=
4k,
$$

they form a basis.  Choose any odd terminal-side word on the four omitted points.  This gives a quartic witness design for every `k\ge1`.  ∎

## 4. The first examples

For `k=1`, the point set is

$$
\{x_{0,0},x_{0,1},x_{0,2},x_{0,3},z\},
$$

and sheet `i` has the single block

$$
X_1\setminus\{x_{0,i}\}.
$$

This is the five-point quartic core.

For `k=2`, write the points as

$$
a_0,a_1,a_2,a_3,
\quad
b_0,b_1,b_2,b_3,
\quad
z.
$$

Sheet `i` has blocks

$$
\{a_h:h\ne i\}\cup\{b_i\},
$$

and

$$
\{b_h:h\ne i\}\cup\{z\}.
$$

Thus a nine-point quartic design already satisfies the full binary basis condition.

## 5. Symplectic reformulation

The standard dot product restricts to a nondegenerate alternating form on `E_X` when `|X|` is odd.  Indeed, every even-weight vector satisfies

$$
x\cdot x=0,
$$

and

$$
E_X^\perp=\langle1_X\rangle,
$$

while `1_X\notin E_X` for odd `|X|`.

For a quartic witness design, let

$$
U_i
=
\operatorname{span}\{1_B:B\in\mathcal R_i\}.
$$

The blocks within one near-resolution are pairwise disjoint and have even size.  Hence `U_i` is a `k`-dimensional totally isotropic subspace.  Since all `4k` block vectors form a basis, one has the direct-sum decomposition

$$
\boxed{
E_X
=
U_0\oplus U_1\oplus U_2\oplus U_3.
}
$$

### Theorem 5.1 — nonsingular cross-intersection form

Order the `4k` blocks by sheet and let

$$
G_{BC}=|B\cap C|\pmod2
$$

be their Gram matrix.  Then:

1. `G` is alternating;
2. its four diagonal `k\times k` blocks are zero;
3. its off-diagonal blocks record cross-sheet intersection parity;
4. `G` is nonsingular over `\mathbf F_2`.

#### Proof

The block vectors are a basis of the nondegenerate alternating space `E_X`.  Therefore their Gram matrix is the matrix of a nondegenerate bilinear form in a basis and is nonsingular.  Disjointness within one sheet gives the zero diagonal blocks.  ∎

This gives a useful exact invariant for any physical quartic core: its four closed-component block spaces form a four-way totally isotropic decomposition of the even-weight symplectic space, and the complete cross-sheet parity matrix must be invertible.

## 6. Consequences for the AffineCDC frontier

### Corollary 6.1 — parity has been exhausted

There is no universal bound on `k` derivable from the following data alone:

- four near-resolutions;
- four distinct omitted points;
- four-element closed-component blocks;
- independence of all block incidence rows;
- odd terminal-side parity.

All of these conditions hold in the quartic ladder for every `k\ge1`.

### Corollary 6.2 — the missing input is physical compatibility

To eliminate, bound, or identify the quartic core, a proof must use information absent from the abstract design, such as:

- the cyclic order of the four witness edges on each closed scalar circuit;
- the two complementary endpoint colours at every witness `g`-edge;
- the fact that the four sheets arise from one nowhere-zero `\mathbf F_2^3` flow;
- the intervening non-`g` path systems;
- composition semantics for crossed root resolutions;
- compatibility with the ten-state four-pole boundary language.

The correct next object is therefore an **enriched quartic design** carrying cyclic orders, endpoint complementary-pair labels, and the induced cross-sheet transition data.

## 7. Reliability boundary

Proved here:

- abstract quartic witness designs exist for every `k\ge1`;
- the explicit quartic ladder satisfies all near-resolution and basis axioms;
- the block spaces give a direct sum of four totally isotropic `k`-spaces;
- the cross-intersection Gram matrix is nonsingular.

Not proved here:

- that any quartic ladder is realised by a route-locked full-rank `\mathbf F_2^3` flow;
- that a physical quartic core exists for any `k`;
- that physical compatibility bounds `k` or forces the DDD `D_8` class;
- any singleton, transition-interval, defect-forest, or four-pole composition theorem;
- the global five-support theorem.

No Lean, independent-review, peer-review, publication, release, arXiv, or DOI status is implied.