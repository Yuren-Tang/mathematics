# Cocircuit carriers, local sets, and the cut-rank mechanism

## 1. Purpose

The bounded nonflat residue has one selected transition at each of the two route-cap vertices.  After local loop/parallel/twin/pendant degenerations are removed, an inclusion-minimal full cocycle completion is either:

1. one cocircuit coupling the two caps; or
2. two disjoint cocircuits, one carrying each cap.

This chapter identifies the exact graph-connectivity parameter carried by each such cocircuit.

Let

$$
M=M[IAS(G)],
\qquad
IAS(G)=(I\mid A\mid I+A),
$$

where `G` is an interlacement graph of the route-capped `4`-regular carrier.  If `D` is a cocircuit, let

$$
L(D)
=
\{v\in V(G):D\cap\tau(v)\ne\varnothing\}
$$

be its vertex support.

The main theorem is

$$
\boxed{
 r_M(D)=|L(D)|+\rho_G(L(D)),
}
$$

where

$$
\rho_G(L)
=
\operatorname{rank}_{\mathbf F_2}A[L,V\setminus L]
$$

is the cut-rank of `L`.

Consequently the nullity and matroid connectivity of a cocircuit are explicit:

$$
\boxed{
 n_M(D)=|L(D)|-\rho_G(L(D)),
}
$$

and

$$
\boxed{
 \lambda_M(D)=|L(D)|+\rho_G(L(D))-1.
}
$$

This gives the exact split-or-prime mechanism needed for the coupled cap branch.

## 2. Vertex-triple support of a cocycle

For a row coefficient vector

$$
y\in\mathbf F_2^{V(G)},
$$

the corresponding cocycle is

$$
c(y)=y\,IAS(G).
$$

At a vertex `v` its three coordinates are

$$
\bigl(y_v,(yA)_v,y_v+(yA)_v\bigr).
$$

Hence the triple is either zero or has weight two.  If

$$
S=\operatorname{supp}y,
$$

then the set of active triples is

$$
\boxed{
L(c(y))=S\cup\operatorname{Odd}_G(S),
}
$$

where

$$
\operatorname{Odd}_G(S)
=
\{v:|N(v)\cap S|\equiv1\pmod2\}.
$$

Thus every cocircuit carrier is a local set in the standard graph-state sense.

## 3. The span of an active cocycle

At every active vertex `v`, the cocycle contains exactly two of

$$
\phi_v,
\qquad
\chi_v,
\qquad
\psi_v,
$$

and these satisfy

$$
\phi_v+\chi_v+\psi_v=0.
$$

### Lemma 3.1 — triple-span saturation

For every nonzero cocycle `D`,

$$
\boxed{
\operatorname{span}_M D
=
\operatorname{span}_M\tau(L(D)),
}
$$

where

$$
\tau(L)=\bigcup_{v\in L}\tau(v).
$$

#### Proof

The inclusion from left to right is immediate.  Conversely, for every `v\in L(D)`, the two transition columns in `D\cap\tau(v)` span the third because their sum is the third.  Hence all three columns of every active vertex triple lie in `\operatorname{span}D`. ∎

This is special to the binary three-element vertex triples.  It says that the rank of a cocycle depends only on which vertices it reaches, not on which of the three transition pairs it uses there.

## 4. Rank of a union of vertex triples

For `L\subseteq V(G)`, the columns of `\tau(L)` span the same space as

$$
\{e_v:v\in L\}
\cup
\{A_v:v\in L\},
$$

because the `I+A` columns are sums of the corresponding `I` and `A` columns.

### Theorem 4.1 — triple-union rank formula

For every `L\subseteq V(G)`,

$$
\boxed{
 r_M(\tau(L))
 =
 |L|+\rho_G(L).
}
$$

#### Proof

The identity columns `e_v`, `v\in L`, span the whole coordinate subspace supported on `L`, contributing rank `|L|`.

Quotient the ambient row space by this coordinate subspace.  The adjacency columns `A_v`, `v\in L`, then retain only their coordinates on `V\setminus L`.  Their quotient matrix is exactly

$$
A[V\setminus L,L].
$$

Its rank is the cut-rank `\rho_G(L)`.  The two contributions are independent, giving the formula. ∎

### Corollary 4.2 — cocycle rank and nullity

For every nonzero cocycle `D`,

$$
\boxed{
 r_M(D)
 =
 |L(D)|+\rho_G(L(D)).
}
$$

Since `D` has exactly two elements in each active triple,

$$
|D|=2|L(D)|,
$$

and therefore

$$
\boxed{
 n_M(D)
 =
 |D|-r_M(D)
 =
 |L(D)|-\rho_G(L(D)).
}
$$

The local-set deficiency `|L|-\rho(L)` is exactly the matroid nullity of the cocycle support.

## 5. Connectivity value of a cocircuit

The isotropic matroid has rank `|V(G)|` because the identity block is present.  If `D` is a cocircuit, its complement is a hyperplane, so

$$
r_M(E\setminus D)=|V(G)|-1.
$$

### Theorem 5.1 — cocircuit connectivity formula

For every cocircuit `D`,

$$
\boxed{
\lambda_M(D)
=
|L(D)|+\rho_G(L(D))-1.
}
$$

#### Proof

By definition,

$$
\lambda_M(D)
=
r_M(D)+r_M(E\setminus D)-r(M).
$$

Insert Corollary 4.2, `r(E\setminus D)=|V|-1`, and `r(M)=|V|`. ∎

This formula is not itself a low-order separation theorem: `D` contains two transition elements at every vertex of `L`, so `\lambda_M(D)` grows with `|L|`.  Its value lies instead in recovering the graph cut-rank exactly from the cocircuit support.

## 6. Split-or-prime trichotomy

Let `D` be a cap cocircuit and put

$$
L=L(D).
$$

The cross adjacency between `L` and `V\setminus L` has rank `\rho_G(L)`.

### Theorem 6.1 — cut-rank mechanism

Assume both shores contain at least two vertices.

1. If
   $$
   \rho_G(L)=0,
   $$
   then there are no interlacement edges across the partition.  The carrier is disconnected across `L\mid V\setminus L`.
2. If
   $$
   \rho_G(L)=1,
   $$
   then the cross-adjacency matrix has rank one, so the partition is a Cunningham split of the interlacement graph.
3. If
   $$
   \rho_G(L)\ge2,
   $$
   then this cocircuit support does not expose a graph split.  It is a prime-side carrier for the next physical analysis.

#### Proof

Rank zero means the cross matrix vanishes.  Over `\mathbf F_2`, a nonzero matrix has rank one exactly when all nonzero rows are equal, equivalently when the cross edges form the complete bipartite graph between two nonempty boundary subsets; this is the graph split condition.  The final case is the negation. ∎

Small shores `|L|=1` or `|V\setminus L|=1` recover the already isolated pendant/twin/local cases rather than a proper split.

## 7. Application to the separated completion

Suppose a minimal cap completion is

$$
C=D_p\sqcup D_q,
$$

with disjoint cocircuits and disjoint vertex supports

$$
L_p=L(D_p),
\qquad
L_q=L(D_q).
$$

Then each one-cap certificate has its own cut-rank

$$
\rho_G(L_p),
\qquad
\rho_G(L_q).
$$

The branch now divides exactly:

- if either cut-rank is at most one, a disconnected shore or graph split is already visible;
- if both are at least two, the two cap certificates occupy disjoint prime-side local sets.

The remaining physical theorem must show that two disjoint prime-side one-cap carriers cannot coexist under one route-locked cubic flow without producing a separator in `\Gamma_g`, an alternate route, or a smaller defect factor.

This is substantially narrower than analysing arbitrary disjoint cocircuits.

## 8. Application to the coupled completion

Suppose one cocircuit `D` contains both cap residues.

- `\rho_G(L(D))\le1` gives an interlacement disconnection or split and should feed the standard transition-matroid decomposition machinery.
- `\rho_G(L(D))\ge2` is the only genuinely prime coupled branch.

Therefore the irreducible nonflat candidate has now been reduced to:

$$
\boxed{
\text{one cap-to-cap cocircuit}
+
\text{one prime local carrier }L
+
\rho_G(L)\ge2.
}
$$

Any comparison with the DDD support-label class need only be constructed on this branch.  The coefficient-space curvature bit, terminal cap residue, and support-label DDD cocycle remain three separate data until such a map is proved.

## 9. Relation to physical composition

A split of an interlacement graph corresponds to a low-connectivity decomposition of the isotropic/transition carrier.  The remaining project-specific step is to transport that decomposition through:

1. the route-capped line graph `F=\mathcal L(\widehat Q)`;
2. the original cubic four-pole `Q`;
3. the physical `g`-component quotient `\Gamma_g`;
4. the five-support boundary profiles and gluing semantics.

The exact cut-lifting theorem on `\Gamma_g` remains the preferred endpoint: once a terminal-even quotient cut is produced, it lifts verbatim to the original four-pole.

## 10. Reliability boundary

Proved here:

- cocycle vertex support as `S\cup\operatorname{Odd}(S)`;
- triple-span saturation;
- `r(\tau(L))=|L|+\rho_G(L)`;
- cocycle rank and nullity formulas;
- cocircuit connectivity formula;
- exact cut-rank split-or-prime trichotomy.

Not proved here:

- that every interlacement split projects to a composition-safe split of `Q` or `\Gamma_g`;
- elimination of two disjoint prime-side one-cap carriers;
- classification of the prime coupled cap cocircuit;
- comparison with the DDD support-label cocycle;
- the global five-support theorem.

No Lean, independent-review, peer-review, publication, release, arXiv, DOI, or merge status is implied.
