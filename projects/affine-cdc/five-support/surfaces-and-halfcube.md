# Cycle-face surfaces, dual triangulations, and the half-cube target

## 1. From a root lift to a surface

Let $G$ be a finite cubic loopless multigraph and let

$$
g:E(G)\to E(K_8)
$$

be a compatible root lift. At every cubic vertex the three incident roots form a triangle on three support indices. For each local support index, pair the two incident edge-sides carrying it. Across a source edge, pair equal support sides.

The resulting face-side transition system is two-regular. Its circuits are the support-cycle faces of a closed cycle-face embedding $S_g$ of $G$. The cellular dual $T_g$ is a closed triangular cellulation: source vertices become triangular faces, and support-cycle components become dual vertices.

### Theorem 1.1 — root lift/surface equivalence

A compatible root lift is equivalent to:

1. a cycle-face embedding of $G$;
2. a proper colouring of its faces by the eight support indices;
3. dually, a closed triangular cellulation $T_g$ with a proper eight-colouring of its vertices.

The graph $T_g^{(1)}$ remembers the individual support-cycle components. This distinction is essential.

## 2. The five-support target

Let $\mathscr A_5$ denote the even half-cube on five coordinates: its vertices are the even subsets of a five-set, and two are adjacent when their symmetric difference has size two.

A map

$$
\varphi:T_g^{(1)}\longrightarrow\mathscr A_5
$$

assigns a five-coordinate even word to every support-cycle face. Across a source edge the two incident dual vertices differ by a root. Reading this root on the source edge produces a root-valued $E_5$ flow and hence a five-support cover.

Conversely, a five-support cover induces such a map on every support-cycle face.

### Theorem 2.1 — componentwise half-cube criterion

For a fixed compatible root lift $g$,

$$
\boxed{
\text{$g$ yields a five-support cover}
\iff
T_g^{(1)}\to\mathscr A_5.
}
$$

This is the correct same-embedding criterion.

## 3. The global-colour quotient and its exact scope

Let $J_g\subseteq K_8$ be the graph whose vertices are the eight old support indices and whose edges are the root labels actually used by $g$. The proper eight-colouring gives a quotient map

$$
T_g^{(1)}\longrightarrow J_g.
$$

A map

$$
J_g\longrightarrow\mathscr A_5
$$

therefore gives a five-support cover whose new value is constant on every support-cycle component carrying the same old support index.

This is a strict subclass of all componentwise maps from $T_g^{(1)}$.

### Scope rule

$$
\boxed{
J_g\to\mathscr A_5
\text{ classifies global-index-factorable compression, not all fixed-lift compression.}
}
$$

Every theorem stated only for $J_g$ remains valid in this narrowed scope. It must not be promoted to the full criterion.

## 4. Exact classification of the factorable quotient

For a spanning subgraph $J\subseteq K_8$, the half-cube homomorphism problem is completely classified:

### Theorem 4.1 — eight-vertex factorable classification

$$
J\to\mathscr A_5
\iff
K_6\nsubseteq J
\quad\text{and}\quad
K_8-C_5\nsubseteq J.
$$

Equivalently, the unused-root graph $U=K_8-J$ either has a three-edge matching or belongs to the exceptional pentagon geometry.

Consequences include:

- an unused three-matching gives compression;
- sufficiently sparse used-root graphs compress;
- every root lift on a cubic graph with at most eight vertices compresses by this route;
- dense quotient obstructions are controlled by two-apex and pentagon cores.

These are exact theorems about the colour quotient. They are not complete obstructions for $T_g^{(1)}$.

## 5. Clique links and target capacity

The target $\mathscr A_5$ has clique number five. More generally, if a source graph contains a dominating clique $K_r$, its remaining vertices must map into the common neighbourhood of an $r$-clique in $\mathscr A_5$.

For $2\le r\le5$, these links are completely explicit.

### Theorem 5.1 — dominating-clique capacity

For every graph $H$ and $2\le r\le5$,

$$
\boxed{
K_r\vee H\to\mathscr A_5
\iff
\chi(H)\le5-r.
}
$$

Thus all target obstructions possessing a dominating clique of rank at least two are compressed to one chromatic threshold.

For $r=1$, the link is $J(5,2)=L(K_5)$; the problem is no longer decided by chromatic number alone. This is the first open target-capacity layer.

## 6. Beyond clique obstruction

The statement

$$
K_6\nsubseteq X
\Longrightarrow
X\to\mathscr A_5
$$

is false for arbitrary graphs. For example, if $H$ is four-chromatic with clique number at most three, then

$$
K_2\vee H
$$

is $K_6$-free but cannot map to $\mathscr A_5$, because the common-neighbour graph of any target edge is the three-colourable triangular prism.

The flower snark $J_5$ supplies a compatible realization of this deeper phenomenon. One state of a two-state root-lift fibre has a nine-vertex dual graph $D_9$ with

$$
K_2\vee W_5\subseteq D_9,
\qquad
\omega(D_9)=5,
$$

so it is $K_6$-free but still does not map to $\mathscr A_5$. The other state contains a $K_6$.

Therefore the obstruction library must include both:

1. clique-capacity cores such as $K_6$;
2. common-neighbour chromatic cores such as $K_2\vee H$.

## 7. Marked obstruction cores

A marked obstruction core is not merely an abstract subgraph of the dual. It is a finite family of exact source-edge face circuits together with its weighted dual incidence data.

For a marked family $\mathcal C$, let $Z_{\mathcal C}$ be the union of the source edges traversed by its faces and let

$$
R_{\mathcal C}=E(G)\setminus Z_{\mathcal C}
$$

be its reserve.

If $B_f$ is the reduced gauge code above the fixed Fano flow and $\beta$ is one state containing $\mathcal C$, then the same marked circuits persist precisely on

$$
\boxed{
A_{\mathcal C}
=
\beta+\left(B_f\cap\mathbf F_2^{R_{\mathcal C}}ight).
}
$$

Hence every finite marked certificate has an affine occurrence locus, and every finite obstruction library gives a finite affine-subspace arrangement in the gauge torsor.

Mixed obstruction species do not require a new nonlinear occurrence geometry. The unresolved issue is completeness of the certificate library and whether its affine arrangement covers the whole fibre.

## 8. The geometry of a visible $K_6$

Let a connected simplicial closed triangulation contain a clique on six dual vertices.

Exactly one of the following occurs:

1. the triangulation has exactly these six vertices; it is the unique six-vertex triangulation of $\mathbb{RP}^2$, and its cellular dual is the Petersen map;
2. some clique edge is externally exposed by a triangle containing a vertex outside the clique.

The externally exposed clique edges form a graph with minimum nonzero degree at least two and hence contain a cycle.

Combine this with the gauge code. For a marked $K_6$ core $X$, restrict gauge words to its face zone. If the restriction has positive rank, some admissible partial Petrial destroys the marked core. If the rank is zero, every face-zone edge is untwistable and one obtains either:

- a rigid projective Petersen core; or
- an untwistable exposed dual cycle.

This is a local escape-or-rigidity theorem for one marked core. It does not prevent destruction of one core followed by renewal of another.

## 9. Renewal and arrangement coverage

A fixed-flow fibre may exhibit three levels.

### 9.1 Rigid core

A marked certificate has exposure rank zero and persists in every gauge state.

### 9.2 Mobile renewal

Every marked certificate can be destroyed, but new certificates appear so that their occurrence cosets cover the whole torsor.

### 9.3 Arrangement escape

The union of obstruction cosets is proper; an uncovered gauge state avoids the selected library.

A sufficient escape condition is

$$
\sum_{C}2^{-r(C)}<1,
$$

where $r(C)$ is the exposure rank of a marked core. Exact Möbius inversion over the intersection lattice gives a sharper test.

The thirty-vertex laboratory realizes mobile clique renewal. Petersen has only isolated projective-plane $K_6$ states and every Fano-flow fibre contains a good state. The flower $J_5$ fibre renews between a $K_6$ core and a $K_2\vee W_5$ core.

## 10. Topological and orientability data

The cycle-face surface carries information beyond the half-cube map.

For a signed rotation-system presentation, let $s_g\in\mathbf F_2^{E(G)}$ be the edge-twist vector. A gauge/Petrial word $k\in B_f$ gives

$$
s_{g^k}=s_g+k.
$$

The orientable locus is

$$
\boxed{
\operatorname{Ori}_f(g)
=
B_f\cap\left(s_g+\operatorname{Cut}(G)ight).
}
$$

It is empty or an affine coset with direction $B_f\cap\operatorname{Cut}(G)$.

An orientable five-support cover yields a nowhere-zero $\mathbf Z_5$ flow by orienting every support component and assigning five distinct coefficients. This is a sufficient bridge toward five-flow theory, not an equivalence and not a proof of Tutte's conjecture.

## 11. Natural dependency order

$$
\boxed{
\begin{array}{c}
\text{compatible root lift }g\\
\Updownarrow\\
\text{coloured cycle-face surface }S_g\\
\Updownarrow\\
\text{coloured dual triangulation }T_g\\
\Downarrow\\
T_g^{(1)}\to\mathscr A_5\ ?\\
\Downarrow\\
\text{target links and marked obstruction cores}\\
\Downarrow\\
\text{affine occurrence arrangement over the gauge torsor.}
\end{array}
}
$$

The colour quotient $J_g$ is a useful intermediate object only after its factorability restriction is stated.

## 12. Reliability boundary

The root-lift/surface correspondence, componentwise criterion, factorable classification, dominating-clique capacity, common-neighbour obstruction, marked-core occurrence theorem, and $K_6$ escape-or-rigidity theorem are theorem-level in the public source surface.

Petersen, the thirty-vertex laboratory, and the flower $J_5$ provide exact finite classifications and certificates. They do not establish a universal obstruction list. No theorem currently proves that every non-homomorphism $T_g^{(1)}\not\to\mathscr A_5$ contains a bounded marked core from the present library, or that every resulting affine arrangement leaves an uncovered state.