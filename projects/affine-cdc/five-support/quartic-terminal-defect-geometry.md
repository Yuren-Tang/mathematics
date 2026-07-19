# Quartic terminal splits and bounded `K_6` defect geometry

## 1. Purpose

The quartic terminal-nucleus theorem assigns to every closed-component block in one scalar sheet a vector in the canonical minus-type four-space

$$
S\cong O^-(4,2).
$$

A block containing one or two of the other omitted terminal points has anisotropic projection, so a nonconcentrated sheet exposes roots of the intrinsic `E_5/K_5` geometry.  This chapter identifies the complete local conservation law carried by those projections.

The three terminal-distribution types

$$
3,\qquad 2+1,\qquad 1+1+1
$$

are exactly the coefficient shadows of:

1. a co-root equality wire;
2. one `K_6` perfect-matching vertex;
3. one `K_6` perfect-matching vertex followed by one root-triangle vertex.

Thus every root-exposed quartic sheet already carries a bounded defect gadget with at most two cubic vertices.  The remaining open problem is not coefficient classification.  It is to lift this bounded gadget through the actual scalar circuits, quotient Kempe systems, and four-pole composition semantics.

## 2. The intrinsic `K_6` completion of the terminal nucleus

Let

$$
I=\{0,1,2,3\},
$$

and let

$$
s_0,s_1,s_2,s_3,s_\infty
$$

be the five nonzero singular vectors of the canonical terminal nucleus, where

$$
s_\infty=s_0+s_1+s_2+s_3.
$$

Put

$$
A=I\sqcup\{\infty\},
$$

and adjoin one formal symbol `\ast` carrying the zero vector.

For `a\in A`, define the co-root

$$
c_a=s_a,
$$

represented by the `K_6` edge

$$
\{\ast,a\}.
$$

For distinct `a,b\in A`, define the root

$$
r_{ab}=s_a+s_b,
$$

represented by the `K_6` edge

$$
\{a,b\}.
$$

The five co-roots and ten roots exhaust the fifteen nonzero vectors of `S`.  Three distinct nonzero vectors sum to zero exactly when their `K_6` edges form either:

1. a triangle; or
2. a perfect matching.

This is the same local `K_6` geometry used by the canonical defect flow, now realized intrinsically inside the quartic incidence nucleus.

## 3. Sheet conservation after nucleus projection

Fix one sheet `i\in I`.  Let

$$
\mathcal R_i
$$

be its four-element closed-component blocks, and let

$$
p(B)=\operatorname{pr}_S(1_B)
$$

be the orthogonal projection of a block vector to the terminal nucleus.

The whole-sheet sum is

$$
\sum_{B\in\mathcal R_i}1_B=s_i.
$$

Applying the linear projection gives:

### Theorem 3.1 — projected sheet conservation

For every sheet `i`,

$$
\boxed{
 c_i
 +
 \sum_{B\in\mathcal R_i}p(B)
 =0.
}
$$

Blocks containing none of the other three omitted points have projection zero.  Hence only the one, two, or three terminal-bearing blocks participate in this conservation law.

#### Proof

Since `s_i\in S`, its orthogonal projection is itself.  Therefore

$$
\sum_{B\in\mathcal R_i}p(B)
=
\operatorname{pr}_S\left(
\sum_{B\in\mathcal R_i}1_B
\right)
=
\operatorname{pr}_S(s_i)
=s_i
=c_i.
$$

Over `\mathbf F_2`, this is equivalent to the displayed zero-sum relation.  ∎

## 4. Concentrated distribution: co-root equality transport

Suppose the three other omitted points all lie in one block `D_i`.  Then

$$
J(D_i)=I\setminus\{i\},
$$

and the terminal-block projection table gives

$$
p(D_i)=s_i=c_i.
$$

Thus projected sheet conservation is

$$
\boxed{c_i+c_i=0.}
$$

### Proposition 4.1 — concentrated equality wire

A concentrated sheet carries the coefficient geometry of a co-root equality wire: the terminal co-root `c_i` is transported unchanged to the unique terminal-bearing closed component.

This is the coefficient-level origin of the canonical nucleus peel.  It is not yet a physical equality-wire replacement in the original four-pole; the distinguished scalar circuit may contain four unbounded intervening intervals.

## 5. Distribution `2+1`: one perfect-matching vertex

Suppose

$$
I\setminus\{i\}=\{j,\ell,m\},
$$

and the terminal-bearing blocks have distributions

$$
\{j,\ell\}
\qquad\text{and}\qquad
\{m\}.
$$

Their projections are

$$
p_{j\ell}=r_{j\ell}=s_j+s_\ell
$$

and

$$
p_m=r_{m\infty}=s_m+s_\infty.
$$

### Theorem 5.1 — split sheet as a one-factor vertex

One has

$$
\boxed{
 c_i+r_{j\ell}+r_{m\infty}=0.
}
$$

Under the intrinsic `K_6` edge model, the three values correspond to

$$
\{\ast,i\},
\qquad
\{j,\ell\},
\qquad
\{m,\infty\},
$$

which form a perfect matching of the six vertices

$$
\{\ast,0,1,2,3,\infty\}.
$$

#### Proof

Using

$$
s_\infty=s_i+s_j+s_\ell+s_m,
$$

one obtains

$$
\begin{aligned}
c_i+r_{j\ell}+r_{m\infty}
&=s_i+(s_j+s_\ell)+(s_m+s_\infty)\\
&=s_i+s_j+s_\ell+s_m+s_\infty\\
&=0.
\end{aligned}
$$

The three displayed `K_6` edges are pairwise disjoint and cover all six vertices, so they form a perfect matching.  ∎

### Corollary 5.2

Every `2+1` terminal split exposes exactly one bounded one-factor defect vertex: one incident co-root and two incident roots.

No further coefficient obstruction remains in this branch.

## 6. Distribution `1+1+1`: a two-vertex defect tree

Suppose again

$$
I\setminus\{i\}=\{j,\ell,m\},
$$

but now the three terminal-bearing blocks contain `j`, `\ell`, and `m` separately.  Their projections are

$$
r_{j\infty},
\qquad
r_{\ell\infty},
\qquad
r_{m\infty}.
$$

Projected sheet conservation is the four-term relation

$$
 c_i
 +r_{j\infty}
 +r_{\ell\infty}
 +r_{m\infty}
 =0.
$$

Choose one of `j,\ell,m` to be distinguished; write it as `j`, leaving the pair `\ell,m`.  Introduce the auxiliary root

$$
a=r_{\ell m}=s_\ell+s_m.
$$

### Theorem 6.1 — fully split sheet factorisation

The four-term conservation law factors into two cubic `K_6` relations:

$$
\boxed{
 c_i+r_{j\infty}+a=0,
}
$$

and

$$
\boxed{
 a+r_{\ell\infty}+r_{m\infty}=0.
}
$$

The first triple is the perfect matching

$$
\{\ast,i\},
\qquad
\{j,\infty\},
\qquad
\{\ell,m\},
$$

and the second triple is the root triangle on

$$
\{\ell,m,\infty\}.
$$

#### Proof

For the first relation,

$$
\begin{aligned}
c_i+r_{j\infty}+a
&=s_i+(s_j+s_\infty)+(s_\ell+s_m)\\
&=s_i+s_j+s_\ell+s_m+s_\infty\\
&=0.
\end{aligned}
$$

The corresponding `K_6` edges are pairwise disjoint and cover all six vertices.

For the second relation,

$$
\begin{aligned}
a+r_{\ell\infty}+r_{m\infty}
&=(s_\ell+s_m)+(s_\ell+s_\infty)+(s_m+s_\infty)\\
&=0.
\end{aligned}
$$

The corresponding root edges are the three sides of the triangle with vertices `\ell,m,\infty`.  Adding the two cubic relations cancels the auxiliary root `a` and recovers the projected four-term conservation law.  ∎

There are three possible choices of the distinguished singleton `j`.  They are permuted transitively by the stabiliser of the unordered triple `\{j,\ell,m\}`.  Hence the coefficient gadget is canonical up to the expected local support symmetry.

### Corollary 6.2

Every `1+1+1` terminal split is represented by a bounded two-vertex defect tree:

1. one perfect-matching vertex incident with the terminal co-root;
2. one adjacent root-triangle vertex;
3. one internal auxiliary root joining them.

## 7. Complete terminal-defect trichotomy

Combining the three cases gives:

### Theorem 7.1 — bounded terminal-defect classification

For every sheet of a quartic witness design, the terminal-bearing block projections admit a coefficient realization of one of the following forms:

$$
\begin{array}{c|c|c}
\text{distribution}&\text{coefficient gadget}&\text{size}\\
\hline
3&\text{co-root equality wire}&0\text{ cubic vertices}\\
2+1&\text{one }K_6\text{ perfect-matching vertex}&1\text{ cubic vertex}\\
1+1+1&\text{perfect-matching vertex + root triangle}&2\text{ cubic vertices}.
\end{array}
$$

Thus every root-exposed quartic sheet has a bounded coefficient defect factor.  There is no unbounded algebraic terminal gadget.

### Corollary 7.2 — refined split-or-peel frontier

The abstract quartic branch now has the form

$$
\boxed{
\begin{cases}
\text{bounded }K_6\text{ defect factor},&
\text{if some sheet is split};\\
\text{canonical }D_8\text{ nucleus peel }k\mapsto k-1,&
\text{if every sheet is concentrated}.
\end{cases}
}
$$

This places both branches directly in the coefficient geometry already used by the defect-forest programme.

## 8. Relation to defect forests and Petersen atoms

In the canonical `E_5` defect flow:

- a zero edge creates an equality wire;
- a perfect-matching vertex is a one-factor defect vertex;
- co-root paths connect such vertices;
- root triangles are ordinary root-valued cubic vertices;
- a single co-root edge between two one-factor vertices is the elementary Petersen/DDD atom.

The terminal-defect classification shows that the root-exposed quartic branch is not a new coefficient species.  It lands exactly in this established local vocabulary.

However, the projection

$$
1_B\longmapsto p(B)\in S
$$

lives in the incidence coefficient space.  A closed scalar component `B` is not itself an edge of the original four-pole, and the auxiliary root in the fully split factorisation is not yet a physical graph edge.  Therefore the classification does not by itself produce an `E_5` flow or a valid graph replacement.

## 9. Updated physical target

The remaining root-exposed theorem is a lifting/composition statement.

Given one split scalar sheet, prove that its one or two terminal-defect vertices can be realised by the actual scalar intervals and quotient-phase data so that one obtains at least one of:

1. a composition-safe one-factor leaf or Petersen endpoint;
2. a two-edge scalar transition interval;
3. a bounded DDD/Petersen atom;
4. a transition-matroid two-sum;
5. a smaller cyclic separator;
6. a ten-state four-pole transfer.

A useful intermediate object should record, for each terminal-bearing closed scalar component:

- its four cyclically ordered witness edges;
- the quotient defect colour at every endpoint;
- the binary phase along each intervening interval;
- the three Kempe-cycle traversals;
- the induced root or co-root projection in the terminal nucleus.

The coefficient theorem says that the target local relation has at most two vertices.  The only remaining complexity lies in transporting the physical intervals to that bounded relation.

## 10. Reliability boundary

Proved here:

- projected sheet conservation in the canonical terminal nucleus;
- concentrated sheets give co-root equality transport;
- every `2+1` split is exactly one `K_6` perfect-matching relation;
- every `1+1+1` split factors through one perfect-matching relation and one root triangle;
- every root-exposed sheet has a bounded coefficient defect gadget with at most two cubic vertices.

Not proved here:

- that block projections lift to an actual `E_5` flow on the original four-pole;
- that the auxiliary root in the fully split gadget has a physical path realisation;
- composition-safe replacement of the scalar intervals;
- a Petersen/DDD factor in the original incidence graph;
- the global five-support theorem.

No Lean, independent-review, peer-review, publication, release, arXiv, or DOI status is implied.
