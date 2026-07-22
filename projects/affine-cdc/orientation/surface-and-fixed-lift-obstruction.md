# Retained cycle-face reconstruction and the fixed-lift orientation class

## 1. Fixed data and occurrence discipline

Let $G$ be a finite loopless cubic multigraph, possibly disconnected, let

$$
f:E(G)\longrightarrow \Gamma\setminus\{0\},
\qquad \Gamma=\mathbf F_2^3,
$$

be a nowhere-zero flow, and let

$$
g:E(G)\longrightarrow \binom{\Gamma}{2}
$$

be one compatible labelled affine/root lift. At each cubic vertex the three incident roots form the three sides of one triangle on three distinct affine indices.

For $a\in\Gamma$, put

$$
F_a=\{e\in E(G):a\in g(e)\}.
$$

The following data are retained throughout the orientation layer.

1. An empty $F_a$ remains an indexed empty support but contributes no face.
2. Distinct connected components of one $F_a$ are distinct face occurrences.
3. Equal edge supports with different indices remain different occurrences.
4. No support is flattened to a generic circuit decomposition before the cycle-face surface is constructed.

These are occurrence statements, not merely statements about sets of edge objects.

## 2. Checked dart reconstruction boundary

Let $\Delta$ be the dart set and $\sigma$ the edge-reversal involution. For a dart in the $a$-support, the checked Lean source defines the unique other same-vertex support dart

$$
\operatorname{partner}_a(d).
$$

It proves same-vertex membership, distinctness, support preservation, involutivity, and uniqueness. Define

$$
\rho_a=\operatorname{partner}_a\circ\sigma,
\qquad
\rho_a^{-1}=\sigma\circ\operatorname{partner}_a.
$$

The checked source proves that these are inverse permutations on the $a$-support. A $\rho_a$-orbit follows one directed boundary traversal; applying $\sigma$ gives the opposite traversal.

The retained Lean theorem `exists_indexed_dart_cover` therefore supplies, simultaneously:

- the support index $a$;
- $\sigma$-closure;
- exact two-support membership of every dart;
- the unique same-vertex partner;
- mutually inverse rotations $\rho_a$ and $\rho_a^{-1}$.

The graph-level theorem `Port.cubic_flow_cdc` is weaker as a reconstruction interface: it discards the returned rotation witness and invokes a generic undirected decomposition of even edge supports.

## 3. Cycle-face surface theorem

At a vertex whose local roots are $ab$, $bc$, and $ca$, take a vertex disc whose three sectors are labelled $a,b,c$ according to the partner pairings. For an edge labelled $\{a,b\}$, attach an edge band whose two long sides carry the labels $a$ and $b$. The endpoint incidences are those determined by the retained partner data. The boundary circuits are exactly the directed $\rho_a$-orbits. Cap each nonempty boundary component by its indexed face disc.

### Theorem 3.1 — retained-data reconstruction

The construction produces a closed cellular surface $S_g$, componentwise over $G$, such that:

1. the embedded one-skeleton is $G$;
2. its face occurrences are exactly the connected components of the indexed supports $F_a$;
3. its directed face boundaries are the $\rho_a$-orbits;
4. every source edge is incident with exactly the two occurrences indexed by the two elements of $g(e)$;
5. reversing a local vertex-disc cyclic order changes a signed-rotation representative but not the underlying signed-rotation class.

The cubic local triangle makes every vertex link a circle, so the ribbon complex is a surface rather than a singular two-complex.

## 4. Twist representatives

Choose an orientation on every vertex disc. For a nonloop edge $e=uv$, define

$$
w_e(g)=
\begin{cases}
0,&\text{if the endpoint attaching intervals extend over an untwisted band},\\
1,&\text{if one half-twist is required}.
\end{cases}
$$

Put

$$
C^0(G)=\mathbf F_2^{V(G)},
\qquad
C^1(G)=\mathbf F_2^{E(G)},
\qquad
(\delta x)_{uv}=x_u+x_v,
$$

and

$$
\operatorname{Cut}(G)=\operatorname{im}\delta.
$$

For a disconnected graph these spaces split over edge-bearing components and

$$
\ker\delta\cong \mathbf F_2^{\pi_0(G)}.
$$

Reversing the chosen orientation at a vertex toggles exactly the incident nonloop twist bits. Therefore

$$
w(g)\longmapsto w(g)+\delta x.
$$

The intrinsic fixed-lift orientation class is

$$
\boxed{
\omega(g)=[w(g)]\in C^1(G)/\operatorname{Cut}(G).
}
$$

It is the restriction of the first Stiefel--Whitney class of $S_g$ to the graph one-skeleton.

## 5. Fixed-lift orientation theorem

Let

$$
Z_1(G)=\operatorname{Cut}(G)^\perp
$$

be the binary cycle space under the edge dot product.

### Theorem 5.1

For one fixed compatible lift $g$, the following are equivalent.

1. $S_g$ is orientable.
2. Vertex-disc orientations can be chosen so that every edge band is untwisted.
3. $w(g)\in\operatorname{Cut}(G)$.
4. $\omega(g)=0$ in $C^1(G)/\operatorname{Cut}(G)$.
5. Every source cycle has zero twist holonomy:
   $$
   \langle w(g),z\rangle=0
   \quad\text{for all }z\in Z_1(G).
   $$
6. The retained indexed face occurrences can be oriented so that the two occurrences of each source edge traverse it in opposite directions.

Cut-cycle orthogonality gives the equivalence of (3) and (5). The surface orientation induces opposite boundary directions on the two sides of each edge band. Conversely, opposite directions on the retained face occurrences orient all face discs and edge bands; the circular cubic vertex link then extends the orientation across every vertex disc.

### Corollary 5.2 — oriented face CDC

In the compatible cubic setting, orientability of $S_g$ is equivalent to an oriented cycle double cover formed by the retained face occurrences: every undirected edge is traversed once in each direction.

This is stronger than arbitrarily orienting the circuits of a generic undirected CDC after support decomposition.

## 6. Boundaries

- **Generic support decomposition:** an arbitrary decomposition of the edge supports need not recover the retained face occurrences, partner data, or rotations, so it cannot replace Theorem 5.1.
- **Repeated supports:** repeated indexed occurrences remain distinct and may receive different face identities.
- **Empty supports:** they contribute no face or orientation condition.
- **Disconnected graphs:** the obstruction and criterion are componentwise.
- **Loops:** this chapter is loopless. Under the natural loop-dart convention, loop orientation and reinsertion are handled in `k4-and-oriented-collapse.md`.
- **Lean status:** the dart objects and inverse rotations are checked; the surface reconstruction theorem, $w(g)$, $\omega(g)$, and orientability equivalence are authorial and not end-to-end Lean formalized.
