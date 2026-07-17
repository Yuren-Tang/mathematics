# Exact dominating-clique capacity for the half-cube target

**Programme:** `AffineCDC — Research Lead`  
**Status:** theorem-level target-graph classification; not canonical pending Director review and literature audit  
**Parents:** `FIVE_CDC_CLIQUE_LINK_CAPACITY_V1.md`, `FIVE_CDC_FLOWER_J5_MIXED_CORE_OBSTRUCTION_V1.md`

## 1. Purpose

The ordinary `K_6` obstruction and the compatible flower-snark obstruction

\[
K_3\vee C_5
\]

belong to one clique-link hierarchy. This packet strengthens that hierarchy from a one-way obstruction principle to an exact classification whenever the source has a dominating clique of rank at least two.

The central theorem is:

\[
\boxed{
K_r\vee H\longrightarrow\mathscr A_5
\iff
\chi(H)\le 5-r
\qquad(2\le r\le5).
}
\]

Thus all dominating-clique obstructions of ranks two through five are controlled by one scalar invariant. They are not an open-ended list of unrelated forbidden graphs.

## 2. Target clique links

Let `Q_r` be any `r`-clique in the even half-cube `\mathscr A_5`. Up to target automorphism its link is

\[
\operatorname{Lk}(Q_r)
=
\mathscr A_5\left[\bigcap_{q\in Q_r}N(q)\right].
\]

The exact link table is

\[
\begin{array}{c|c|c}
r&\operatorname{Lk}(Q_r)&\chi\\
\hline
1&J(5,2)=L(K_5)&5\\
2&K_3\square K_2&3\\
3&K_2\sqcup K_1&2\\
4&K_1&1\\
5&\varnothing&0.
\end{array}
\]

For every `2\le r\le5`, the link contains a clique of order `5-r`:

\[
K_{5-r}\subseteq\operatorname{Lk}(Q_r),
\]

with the convention that `K_0` is the empty graph.

Hence the link has both chromatic number and clique number equal to `5-r`.

## 3. Exact join theorem

### Theorem 3.1 — dominating-clique exact capacity

Let `H` be any finite loopless graph and let `2\le r\le5`. Then

\[
\boxed{
K_r\vee H\longrightarrow\mathscr A_5
\iff
\chi(H)\le5-r.
}
\]

#### Proof

Suppose first that

\[
K_r\vee H\longrightarrow\mathscr A_5.
\]

The source `K_r` maps injectively to an `r`-clique `Q_r`. Every vertex of `H` is adjacent to every vertex of that clique, so the restriction to `H` lands in

\[
\operatorname{Lk}(Q_r).
\]

Composing with a `(5-r)`-colouring of the link gives

\[
\chi(H)\le5-r.
\]

Conversely assume `\chi(H)\le5-r`. Then

\[
H\longrightarrow K_{5-r}.
\]

Choose a copy

\[
K_{5-r}\subseteq\operatorname{Lk}(Q_r).
\]

Map the dominating source clique to `Q_r` and map `H` into that link clique. Every cross-edge is preserved by the definition of the link, so this gives

\[
K_r\vee H\longrightarrow\mathscr A_5.
\]

∎

### Corollary 3.2 — exact obstruction threshold

For `2\le r\le5`,

\[
\boxed{
K_r\vee H\not\longrightarrow\mathscr A_5
\iff
\chi(H)\ge6-r.
}
\]

The obstruction ladder is therefore exact, not merely sufficient.

## 4. The four closed ranks

### Rank five

The remainder must have chromatic number zero, hence no vertices. Therefore

\[
K_5\vee H\to\mathscr A_5
\iff
V(H)=\varnothing.
\]

The first obstruction is

\[
K_5\vee K_1=K_6.
\]

### Rank four

The remainder must be independent:

\[
K_4\vee H\to\mathscr A_5
\iff
\chi(H)\le1.
\]

Any edge in `H` produces a `K_6` subgraph.

### Rank three

The remainder must be bipartite:

\[
\boxed{
K_3\vee H\to\mathscr A_5
\iff
H\text{ is bipartite}.
}
\]

Thus every non-bipartite graph gives an obstruction, and every such obstruction is explained by odd-cycle parity rather than by an infinite catalogue.

The compatible flower-snark core

\[
K_3\vee C_5
\]

is the smallest displayed member of this exact rank-three family.

### Rank two

The remainder must be three-colourable:

\[
\boxed{
K_2\vee H\to\mathscr A_5
\iff
\chi(H)\le3.
}
\]

The forward implication uses the three-colourability of the triangular-prism link. The reverse implication is especially simple: every three-colourable `H` maps to one triangle contained in that prism.

Hence the entire rank-two obstruction family is exactly

\[
\{K_2\vee H:\chi(H)\ge4\}.
\]

Odd wheels are one source of examples, but they are not a separate mechanism.

## 5. The first genuinely unclosed rank

For a dominating vertex,

\[
K_1\vee H\to\mathscr A_5
\iff
H\to J(5,2)=L(K_5).
\]

Chromatic number no longer decides the problem.

The link contains a `K_4` and has chromatic number five. Therefore:

\[
\chi(H)\le4
\Longrightarrow
H\to J(5,2),
\]

while

\[
\chi(H)\ge6
\Longrightarrow
H\not\to J(5,2).
\]

Only the five-chromatic layer can behave in both ways:

- `K_5` does not map to `J(5,2)` because the latter has clique number four;
- `J(5,2)` maps to itself and is five-chromatic.

Thus the first non-chromatic dominating-clique frontier is precisely

\[
\boxed{
r=1,\qquad\chi(H)=5,\qquad H\to L(K_5)?
}
\]

This is a finite-target graph-homomorphism problem, but not a single colour-threshold condition.

## 6. What has genuinely been compressed

The infinite families

\[
K_6,
\qquad
K_3\vee C_{2k+1},
\qquad
K_2\vee H\ (\chi(H)\ge4),
\]

are not three unrelated lists. They are all instances of the exact theorem

\[
\chi(H)>5-r.
\]

Therefore every compatible obstruction containing a dominating clique of rank at least two can be certified and classified without enlarging an obstruction library graph by graph.

The remaining unbounded sources of difficulty are now sharply separated:

1. compatible bad duals with no dominating clique of rank at least two;
2. the rank-one line-graph target problem;
3. global renewal among different marked cores over a gauge fibre;
4. horizontal transport among Fano flows.

## 7. Programme consequences

### 7.1 Obstruction records should store rank and remainder

For every bad compatible dual `T`, first search for a dominating clique `Q`. If `|Q|\ge2`, record

\[
(|Q|,\chi(T-Q))
\]

rather than treating the induced obstruction as a new species.

### 7.2 New species threshold

A genuinely new target-homomorphism mechanism occurs only if:

- no dominating clique of size at least two explains the obstruction; or
- the obstruction is rank one and depends on failure to map to `L(K_5)` rather than on chromatic number alone.

### 7.3 Compatible-triangulation question

The current exact laboratories have produced:

- rank-five clique cores;
- rank-three odd-cycle cores.

It remains open whether compatible cycle-face dual triangulations can realize an irreducible rank-two core, a rank-one core, or a bad core with no dominating clique.

These are now structural search targets rather than requests for more arbitrary examples.

## 8. Trust boundary

The exact equivalence for ranks two through five is an elementary theorem derived from the explicit half-cube link table and the existence of maximum cliques in those links.

The rank-one boundary statements are also elementary. No claim is made that every compatible bad dual contains a dominating clique, that the rank-one problem has a finite obstruction basis, or that the five-cycle double cover conjecture is resolved.
