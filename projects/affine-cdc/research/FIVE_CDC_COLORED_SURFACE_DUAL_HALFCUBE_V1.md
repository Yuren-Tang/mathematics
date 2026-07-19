# Colored surfaces, dual triangulations, and the true componentwise half-cube criterion

**Programme:** `AffineCDC — Research Lead`  
**Status:** theorem-level structural checkpoint and scope correction; not canonical pending Director review and literature audit  
**Parents:** `FIVE_CDC_HALFCUBE_SUBGRAPH_CLASSIFICATION_V1.md`, `FIVE_CDC_SUPPORT_CYCLE_PIVOT_AND_FLOW_RECONFIGURATION_V1.md`, canonical `topology/README.md`

## 1. Purpose and correction

The eight-vertex theorem

\[
J\to\mathscr A_5
\iff
K_6\nsubseteq J\text{ and }K_8-C_5\nsubseteq J
\]

is correct. Its previous interpretation as the complete criterion for every five-support construction obtainable from one fixed root lift was too strong.

The graph `J_g` remembers only the eight global support indices. A root lift may have several cycle components carrying the same support index. A five-support construction is allowed to treat those components differently. The true same-embedding target is therefore not the color quotient `J_g`, but the full dual triangulation `T_g`.

This packet proves:

1. a root lift is equivalently a properly eight-face-colored cycle-face embedding, or dually a properly eight-vertex-colored closed triangular cellulation;
2. a cubic graph has a five-support cycle double cover if and only if some such dual triangulation maps to the five-dimensional half-cube `\mathscr A_5`;
3. for a fixed root lift `g`, a homomorphism `T_g\to\mathscr A_5` gives a componentwise five-support compression;
4. `J_g\to\mathscr A_5` is exactly the subclass of those maps that factor through the eight global support colors;
5. the factorization restriction is strict;
6. the thirty-vertex fixed-Fano obstruction remains valid even under the stronger componentwise criterion, by explicit `K_7` and `K_6` clique certificates in its two dual triangulations.

## 2. From a root lift to a closed surface

Let `G` be a finite loopless cubic multigraph and let

\[
g:E(G)\to E(K_8)
\]

be a root lift. Write

\[
g(e)=\{a,b\},\qquad a\ne b.
\]

For every support index `a`, put

\[
F_a:=\{e:a\in g(e)\}.
\]

At every source vertex the three incident root labels are the three edges of a target triangle. Hence every `F_a` has degree zero or two at every source vertex. Its nonempty connected components are source cycles.

Attach a polygonal disk along every cycle component of every `F_a`. Every source edge belongs to exactly two distinct supports, so it is incident with exactly two attached disks. At a cubic source vertex with local support indices `a,b,c`, the three incident source edges have labels

\[
ab,\quad ac,\quad bc.
\]

The three corresponding face corners form a disk neighbourhood of the vertex. Therefore the resulting cell complex is a closed surface, possibly nonorientable and allowing polygonal two-faces when the source is a multigraph. Its one-skeleton is `G`, and every face boundary is a source cycle.

Call this the **cycle-face embedding** `S_g`.

### Theorem 2.1 — root lifts and colored cycle-face embeddings

Root lifts of `G` with support-index set contained in an eight-set are equivalent to cycle-face embeddings of `G` together with a proper coloring of their faces by those eight indices.

Under the correspondence, the root label of a source edge is the unordered pair of colors of its two incident faces.

#### Proof

The forward construction is above. Conversely, in a cycle-face embedding with properly colored faces, label every source edge by the pair of its incident face colors. At a cubic vertex the three face incidences are pairwise adjacent around the vertex, hence have three distinct colors `a,b,c`; the incident edge labels are `ab,ac,bc`, a target triangle. Thus the edge labeling is a root lift. ∎

The active canonical topology inventory records an older embedding and gauge programme whose source bodies are absent. The theorem above is derived directly from the current root-lift definitions; it is not represented as a reconstruction of any missing historical theorem.

## 3. The dual triangulation

Let `T_g` be the cellulation dual to `S_g`.

- vertices of `T_g` are the cycle components of the supports `F_a`;
- dual edges are source edges of `G`;
- dual triangular faces are source vertices of `G`.

Every dual vertex inherits the color of its support component. Adjacent dual vertices have distinct colors, so

\[
\kappa_g:T_g^{(1)}\to K_8
\]

is a graph homomorphism, i.e. a proper eight-coloring.

Let `J_g` be the used-root graph on the eight colors. Then

\[
\boxed{
J_g
=
\text{the color-adjacency quotient of }T_g^{(1)}.
}
\]

A color pair `ab` is an edge of `J_g` exactly when some dual edge joins an `a`-colored component to a `b`-colored component.

## 4. Half-cube potentials give five supports

Let `\mathscr A_5` be the graph on `\mathbf F_2^5` whose edges join words at Hamming distance two. Its two parity components are isomorphic.

### Theorem 4.1 — dual half-cube criterion

Let `T` be the closed triangular dual of a cycle-face embedding of a cubic graph `G`. If

\[
\lambda:T^{(1)}\to\mathscr A_5
\]

is a graph homomorphism, then `G` has a five-support cycle double cover.

#### Proof

For a primal source edge `e` dual to `xy`, the difference

\[
d_e:=\lambda(x)+\lambda(y)
\]

has Hamming weight two. For `i\in\{1,\ldots,5\}`, define

\[
F_i:=\{e:i\in\operatorname{supp}(d_e)\}.
\]

Every source edge lies in exactly two of the `F_i`.

It remains to check evenness. A source vertex is dual to a triangle `xyz`. Put

\[
a=\lambda(x)+\lambda(y),\qquad
b=\lambda(x)+\lambda(z).
\]

The words `a`, `b`, and `a+b=\lambda(y)+\lambda(z)` all have weight two. Two two-subsets have symmetric difference of size two exactly when they meet in one point. Hence for distinct coordinates `p,q,r`, after relabeling,

\[
a=\{p,q\},\qquad
b=\{p,r\},\qquad
a+b=\{q,r\}.
\]

Thus each of the three coordinates `p,q,r` occurs on exactly two of the three incident source edges, and every other coordinate occurs zero times. Every `F_i` is even. ∎

### Theorem 4.2 — global equivalence

A finite loopless cubic graph has a five-support cycle double cover if and only if it has a cycle-face embedding whose dual triangular graph admits a homomorphism to `\mathscr A_5`.

#### Proof

The forward direction uses the cycle components of the five supports as faces. Color a face component of support `i` by the singleton word `e_i`, which lies in one parity component of `\mathscr A_5`; adjacent face components differ in exactly two coordinates. The reverse direction is Theorem 4.1. ∎

This gives a topological-homomorphic form of the five-support problem:

\[
\boxed{
5\text{-CDC}
\iff
\exists\text{ cycle-face embedding }S
\text{ with }T_S\to\mathscr A_5.
}
\]

## 5. Factorable versus componentwise compression

For one fixed root lift `g`, the eight-coloring factors as

\[
T_g^{(1)}\xrightarrow{\kappa_g}J_g\subseteq K_8.
\]

If

\[
\phi:J_g\to\mathscr A_5,
\]

then

\[
\lambda=\phi\circ\kappa_g
\]

is a half-cube potential on the full dual triangulation. This is the previously classified **global-index-factorable compression**.

But a general map

\[
\lambda:T_g^{(1)}\to\mathscr A_5
\]

need not be constant on all cycle components carrying the same old support index. It may split one disconnected old support into components with different target values.

Therefore:

\[
\boxed{
J_g\to\mathscr A_5
\Longrightarrow
T_g\to\mathscr A_5,
}
\]

but the converse need not hold.

The exact `K_6/K_8-C_5` theorem classifies only the left-hand, factorable condition.

## 6. Explicit strictness example

Construct a stacked planar triangulation `T` as follows. Start with `K_4` on vertices `0,1,2,3`. Insert successively:

\[
\begin{array}{c|c}
4&123\\
5&124\\
6&012\\
7&125\\
8&126\\
9&026\\
10&268\\
11&257
\end{array}
\]

where `v|abc` means insert vertex `v` in triangular face `abc` and join it to `a,b,c`.

It has the following complete proper six-coloring:

\[
\begin{array}{c|rrrrrrrrrrrr}
v&0&1&2&3&4&5&6&7&8&9&10&11\\
\hline
\kappa_6(v)&3&1&0&5&2&4&2&3&3&1&1&5.
\end{array}
\]

Every one of the fifteen unordered pairs of six colors occurs on an edge. For example witnesses are

\[
\begin{array}{c|cccccccc}
01&12&02&03&25&04&15&06&23\\
12&14&13&01&14&15&24&04
\end{array}
\]

with the remaining pairs witnessed by `03,13,23,25,34,45` on edges `02,01,04,34,57,5\,11` respectively. Direct inspection of the construction also gives the full edge list if desired.

Hence the color quotient is `K_6`, and no factorable map

\[
K_6\to\mathscr A_5
\]

exists because `\omega(\mathscr A_5)=5`.

The same triangulation has the proper four-coloring

\[
\begin{array}{c|rrrrrrrrrrrr}
v&0&1&2&3&4&5&6&7&8&9&10&11\\
\hline
\kappa_4(v)&3&1&0&2&3&2&2&3&3&1&1&1.
\end{array}
\]

A four-clique embeds in `\mathscr A_5`, so `T\to\mathscr A_5`. Taking the planar dual gives a cubic planar graph and one fixed cycle-face embedding for which global six-index factorization fails while componentwise compression succeeds, in fact to four supports.

Thus the factorization restriction is genuinely strict within the cubic cycle-cover setting.

## 7. Support pivots are vertex recolorings

Let `C` be one support-cycle component, hence one vertex `v_C` of `T_g`, with current color `c`. Its neighbouring dual vertices have precisely the leaf colors `s` occurring in root labels `cs` along `C`.

A support-cycle pivot `c\to d` is legal exactly when no neighbour of `v_C` has color `d`. Under the dual description it is simply the proper-coloring move

\[
\kappa_g(v_C)=c
\longmapsto d.
\]

The underlying cycle-face embedding and dual triangulation remain fixed. The projected Fano flow changes by `c+d` around the primal face boundary `C`.

Conversely every legal single-vertex recoloring of the dual eight-coloring is exactly a support-cycle pivot.

The unused-root update formula is therefore the color-quotient update under one vertex recoloring:

- a color adjacency `cs` disappears precisely when every `c-s` dual edge was incident with the recolored vertex;
- a color adjacency `ds` appears precisely when the recolored vertex has an `s`-colored neighbour and no other `d-s` edge was previously present.

This identifies the source-side release condition with **exclusive color adjacency** in the dual triangulation.

## 8. Gauge moves versus pivots

The two motions now have distinct geometric meanings.

1. **Support pivots / horizontal cycle switches:** preserve the cycle-face embedding and recolor one dual vertex.
2. **Gauge moves inside one fixed Fano-flow fibre:** produce another root lift, and hence may change the support-cycle decomposition, the cycle-face embedding, and the dual triangulation, while preserving the projected edge directions.

Thus the programme is naturally a moduli problem of properly colored triangular surfaces:

\[
\text{change coloring on a fixed surface}
\quad\text{and}\quad
\text{change the surface realization at fixed flow}.
\]

This is the current bridge between the active affine/gauge theory and the archived embedding programme.

## 9. Strengthened thirty-vertex fixed-flow obstruction

For the two reduced root lifts in `FIVE_CDC_FIXED_FANO_ORBIT_OBSTRUCTION_V1.md`, construct their full dual triangulations.

### Base lift

The eight supports have component counts

\[
1,1,1,1,2,1,2,2,
\]

so the dual triangulation has eleven vertices. Its simple one-skeleton contains a `K_7` formed by the support components

\[
C_0^{12},\ C_1^{16},\ C_2^{8},\ C_3^{12},\ C_4^{8},\ C_5^{9},\ C_7^{11},
\]

where the superscript is the boundary-cycle length.

### Translated lift

The support component counts are

\[
2,2,1,1,2,2,2,1,
\]

so the dual triangulation has thirteen vertices. Its simple one-skeleton contains a `K_6` formed by components of colors

\[
0,2,3,5,6,7
\]

and respective boundary lengths

\[
8,9,11,11,8,9.
\]

Since

\[
\omega(\mathscr A_5)=5,
\]

neither dual triangulation admits a homomorphism to `\mathscr A_5`. The fixed Fano flow therefore has no componentwise same-embedding five-support compression in either of its two root lifts.

This strengthens the earlier obstruction. Its former `J_g=K_8-e` proof established failure only for global-index-factorable maps; the explicit dual cliques establish failure for all componentwise half-cube potentials on those embeddings.

## 10. Corrected strategic hierarchy

The compression routes now form a strict hierarchy.

1. **Global-index-factorable route:** `J_g\to\mathscr A_5`. Completely classified by the `K_6/K_8-C_5` theorem and the two-apex/pentagon/star-core dynamics.
2. **Componentwise same-embedding route:** `T_g\to\mathscr A_5`. Strictly stronger; the correct fixed-lift target.
3. **Gauge-modified embedding route:** find another root lift above the same Fano flow whose dual maps to `\mathscr A_5`.
4. **Flow-reconfigured route:** change the downstairs Fano flow and repeat.
5. **Direct route:** construct some cycle-face embedding of `G` with dual homomorphism to `\mathscr A_5`, without factoring through the eight-support AffineCDC lift.

The previously developed finite defect-core theory remains exact and useful for Route 1. It is no longer a complete description of failure in Routes 2–5.

The next primary target should therefore be the full dual-homomorphism problem, with the quotient-factorable star-core programme retained as a tractable sufficient subroute and as a source of explicit recoloring moves.
