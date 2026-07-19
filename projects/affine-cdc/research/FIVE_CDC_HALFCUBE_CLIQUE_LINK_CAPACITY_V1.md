# Clique-link capacity in the five-dimensional half-cube

**Programme:** `AffineCDC — Research Lead`  
**Status:** theorem-level target-graph classification and obstruction hierarchy; not canonical pending Director review and literature audit  
**Parents:** `FIVE_CDC_K6_FREE_HALFCUBE_WARNING_V1.md`, `FIVE_CDC_FLOWER_J5_MIXED_CORE_OBSTRUCTION_V1.md`

## 1. Purpose

The first compatible `K_6`-free obstruction in the flower snark `J_5` contains

\[
K_2\vee W_5=K_3\vee C_5.
\]

This packet places that core and the ordinary `K_6` obstruction in one systematic target-graph hierarchy.

For a clique `Q` in the half-cube `\mathscr A_5`, define its link

\[
\operatorname{Lk}(Q)
:=
\mathscr A_5\left[\bigcap_{q\in Q}N(q)\right].
\]

If a source graph contains a join

\[
K_r\vee H,
\]

then any homomorphism to `\mathscr A_5` must map `H` into the link of the image `K_r`. The structure and chromatic capacity of those links give a nested obstruction language.

## 2. Canonical cliques

Represent vertices of `\mathscr A_5` as even subsets of

\[
[5]=\{1,2,3,4,5\},
\]

with adjacency given by symmetric difference of size two.

Every maximal clique is equivalent under translation and coordinate permutation to

\[
Q_5
=
\{\varnothing,12,13,14,15\}.
\]

For `1\le r\le5`, take the initial canonical subclique

\[
Q_r\subseteq Q_5.
\]

The link type depends only on `r`.

## 3. Exact clique-link table

### Theorem 3.1 — half-cube clique links

The links of canonical cliques are:

\[
\begin{array}{c|c|c|c}
r&|\operatorname{Lk}(Q_r)|&\operatorname{Lk}(Q_r)&\chi\\
\hline
1&10&J(5,2)=L(K_5)&5\\
2&6&K_3\square K_2&3\\
3&3&K_2\sqcup K_1&2\\
4&1&K_1&1\\
5&0&\varnothing&0.
\end{array}
\]

#### Proof

Translate the first clique vertex to `\varnothing`.

### Rank one

The neighbours of `\varnothing` are the ten two-subsets of `[5]`. Two such vertices are adjacent exactly when the corresponding two-subsets intersect in one point. This is the Johnson graph

\[
J(5,2)=L(K_5).
\]

Its chromatic number is the edge-chromatic number of `K_5`, namely five.

### Rank two

Normalize

\[
Q_2=\{\varnothing,12\}.
\]

The common neighbours are

\[
13,14,15,
\qquad
23,24,25.
\]

Each row is a triangle, and equal second coordinates give a perfect matching between the rows. Thus the link is the triangular prism and has chromatic number three.

### Rank three

Normalize

\[
Q_3=\{\varnothing,12,13\}.
\]

The common neighbours are

\[
14,\quad15,\quad23.
\]

The first two are adjacent and the third is isolated. Hence the link is `K_2\sqcup K_1`.

### Rank four

For

\[
Q_4=\{\varnothing,12,13,14\},
\]

the unique common neighbour is `15`.

### Rank five

The maximal clique `Q_5` has no common neighbour, because `\omega(\mathscr A_5)=5`. ∎

## 4. General join obstruction

### Theorem 4.1 — clique-link obstruction principle

Let `H` be any graph. If

\[
K_r\vee H
\longrightarrow
\mathscr A_5,
\]

then

\[
\boxed{
H\longrightarrow\operatorname{Lk}(Q_r).
}
\]

Consequently, any graph invariant monotone under homomorphisms gives an obstruction whenever `H` exceeds the capacity of the link.

In particular,

\[
\boxed{
\chi(H)>\chi(\operatorname{Lk}(Q_r))
\Longrightarrow
K_r\vee H\not\longrightarrow\mathscr A_5.
}
\]

#### Proof

The image of the source `K_r` is an `r`-clique, equivalent to `Q_r`. Every vertex of `H` is adjacent to every vertex of the source clique, so its image belongs to every neighbourhood of the image clique. Thus the restriction of the homomorphism to `H` lands in the link. ∎

## 5. The obstruction ladder

The clique-link table gives the following hierarchy.

### Rank five — ordinary clique obstruction

Since the link is empty, any additional joined vertex is impossible:

\[
K_5\vee K_1=K_6
\not\longrightarrow\mathscr A_5.
\]

### Rank four — independent-set capacity one

The link consists of one vertex. Therefore any `H` containing an edge gives an obstruction. The minimal case is again

\[
K_4\vee K_2=K_6.
\]

### Rank three — bipartite capacity

The link is bipartite. Hence every non-bipartite `H` gives an obstruction:

\[
\boxed{
K_3\vee C_{2k+1}
\not\longrightarrow\mathscr A_5.
}
\]

Its clique number is

\[
3+2=5,
\]

so this is an infinite `K_6`-free obstruction family.

### Rank two — three-colour capacity

The link is the three-colourable triangular prism. Hence

\[
\boxed{
\chi(H)\ge4
\Longrightarrow
K_2\vee H
\not\longrightarrow\mathscr A_5.
}
\]

If additionally `\omega(H)\le3`, the resulting obstruction is `K_6`-free.

Odd wheels give

\[
K_2\vee W_{2k+1}
\not\longrightarrow\mathscr A_5.
\]

### Rank one — five-colour link

A dominating source vertex forces the remainder into `J(5,2)`. Chromatic number alone obstructs only graphs of chromatic number at least six, but finer homomorphism invariants of `J(5,2)` may produce lower-chromatic rank-one obstructions.

## 6. The D9 obstruction has two equivalent certificates

The compatible nine-vertex graph `D_9` in the flower-snark witness contains

\[
K_2\vee W_5.
\]

Since

\[
W_5=K_1\vee C_5,
\]

it also contains

\[
\boxed{
K_3\vee C_5.
}
\]

Thus `D_9` has two nested certificates:

1. **rank-two certificate:** the odd wheel has chromatic number four, exceeding the triangular-prism link capacity three;
2. **rank-three certificate:** the odd rim `C_5` is non-bipartite, exceeding the triangle-link capacity two.

The rank-three proof is the shorter certificate. The rank-two formulation displays the larger common-neighbour geometry.

## 7. Mechanism interpretation

The obstruction library should no longer be organized as an unrelated list

\[
K_6,\quad D_9,\quad\ldots
\]

Instead, marked cores should be stratified by:

1. a dominating clique rank `r` in the source dual;
2. the residual graph `H` joined to that clique;
3. the homomorphism capacity of `\operatorname{Lk}(Q_r)`.

The two observed compatible core types occupy different levels:

\[
\begin{array}{c|c|c}
\text{core}&r&\text{link obstruction}\\
\hline
K_6&5&\text{empty link}\\
D_9\supset K_3\vee C_5&3&\text{bipartite link versus odd cycle}.
\end{array}
\]

The mixed `J_5` gauge fibre therefore renews not merely between two graphs, but between two ranks of the same clique-link obstruction ladder.

## 8. Affine occurrence loci remain type-independent

The affine marked-core occurrence theorem depends only on preserving a specified family of face circuits and their incidence data. It does not require the marked core to be a clique.

Therefore a marked `K_3\vee C_5` or `D_9` core has an affine occurrence locus

\[
A_C=\beta_C+
\bigl(B_f\cap\mathbf F_2^{R_C}\bigr)
\]

just as a marked `K_6` core does.

For a finite library of clique-link obstruction templates, the full bad locus is still a union of labelled affine subspaces. The labels now record obstruction rank and residual link type.

The one-dimensional `J_5` witness is the simplest mixed example:

\[
\mathbf F_2
=
\{\text{rank-three deep core point},
\text{rank-five clique core point}\}.
\]

## 9. Refined next targets

### 9.1 Compatible rank-three census

Search larger snark laboratories for other compatible cores containing

\[
K_3\vee H,
\qquad H\text{ non-bipartite},
\]

and classify the minimal residual graphs `H` that occur.

### 9.2 Rank-two versus rank-three minimality

Determine whether every compatible `K_2\vee H` obstruction with `\chi(H)\ge4` necessarily contains a smaller rank-three odd-cycle join, as `D_9` does, or whether genuinely rank-two cores occur.

### 9.3 Link-sensitive renewal

For a gauge move, track how the maximal dominating-clique rank of the active obstruction changes. The `J_5` atom changes rank

\[
3\longleftrightarrow5.
\]

An invariant or monotone controlling these rank changes could replace raw obstruction-graph enumeration.

### 9.4 Higher-order target capacities

Beyond chromatic number, compute homomorphism obstructions inside

\[
J(5,2),\quad K_3\square K_2,\quad K_2\sqcup K_1.
\]

This may reveal compatible cores not detectable by clique or chromatic number alone.

## 10. Trust boundary

The clique-link table and join obstruction principle are elementary theorem-level facts. The finite link orders, degree sequences, and chromatic numbers are reproduced by the private verifier.

The placement of `D_9` in both the rank-two and rank-three obstruction levels follows from the explicit compatible certificate.

No statement here classifies all graphs not mapping to `\mathscr A_5`, proves that the clique-link ladder is a complete obstruction theory, or proves the five-cycle double cover conjecture.
