# Cycle-face surfaces, target hierarchy, and half-cube capacity

## 1. Cycle-face surface and full dual

Let `G` be a finite loopless cubic multigraph and let

$$
g:E(G)\to\binom I2
$$

be a compatible root lift on an eight-element support-index set `I`. At each source vertex the three incident roots are the edges of one triangle on three distinct indices.

For every index `a`, the support

$$
F_a=\{e:a\in g(e)\}
$$

is vertex-even. Attach one face disc along every nonempty connected component of every `F_a`.

### Theorem 1.1 — root-lift/surface equivalence

Compatible root lifts are equivalent to properly face-coloured cycle-face embeddings `S_g`. Their dual cellulations `T_g` are triangular and properly vertex-coloured by the old support indices.

A vertex of `T_g` is one individual support-cycle component. Distinct components carrying the same old index remain distinct vertices.

## 2. The five-coordinate target

Put

$$
E_5=\{x\in\mathbf F_2^5:\sum_i x_i=0\},
\qquad
R_5=\{\varepsilon_i+\varepsilon_j:i<j\}.
$$

The even half-cube `\mathscr A_5` is the Cayley graph on `E_5` with difference set `R_5`.

### Theorem 2.1 — fixed-lift criterion

For a fixed compatible lift `g`, componentwise compression of the face components of the same embedding is exactly

$$
T_g^{(1)}\to\mathscr A_5.
$$

The edge differences give an `R_5`-valued flow and hence five indexed even supports.

This does not say that an arbitrary external five-support cover can be represented on the prescribed surface.

### Prescribed-surface holonomy

An external root labelling on the fixed dual integrates to a vertex potential exactly when its sum vanishes on every dual cycle. Conservation around triangular faces alone is insufficient.

## 3. Graph-level existential surface criterion

For a finite loopless cubic multigraph `G`, the following are equivalent:

1. `G` has five indexed even supports;
2. some cycle-face embedding `S` of `G` has
   $$
   T_S^{(1)}\to\mathscr A_5.
   $$

The forward construction uses the surface built from the five-support cover itself. The embedding is existentially quantified.

If `\mathscr A_5` denotes the even component, singleton words are not target vertices. Choose one odd word `t` and use `t+\varepsilon_i`; pairwise differences remain `\varepsilon_i+\varepsilon_j`.

## 4. Full dual versus old-colour quotient

Let `J_g` be the graph on the old support indices used by `g`, with an edge for every used old root. The old colouring gives a quotient

$$
T_g^{(1)}\to J_g.
$$

### Theorem 4.1 — exact factorability boundary

A map from the full dual to `\mathscr A_5` factors through `J_g` exactly when it is constant on all face components carrying the same old support index.

Therefore

$$
J_g\to\mathscr A_5
\Longrightarrow
T_g^{(1)}\to\mathscr A_5,
$$

but the converse fails in general.

Terminology:

- `componentwise same-embedding compressible`: `T_g^{(1)}\to\mathscr A_5`;
- `old-colour-factorably compressible`: `J_g\to\mathscr A_5`;
- `factorably bad`: failure of the second condition only.

Unused-root graphs, matching orbits, two-apex/pentagon cores, and ideal pivots are factorable objects unless a separate full-dual theorem is stated.

## 5. Quadratic common-link formula

Let `(E,q)` be a nondegenerate quadratic space over `\mathbf F_2`, let `\mathscr A(E,q)` have adjacency `x\sim y` when `q(x+y)=1`, and let `C` be a nonempty target clique. Choose `\alpha\in C`, put

$$
S_C=\{c+\alpha:c\in C-\{\alpha\}\},
\qquad
D_C=\operatorname{span}S_C.
$$

### Theorem 5.1

A vertex `y=\alpha+z` is adjacent to every member of `C` exactly when

$$
q(z)=1,
\qquad
B(z,d)=1\quad(d\in S_C).
$$

Hence every common link is a quadratic slice of an affine coset:

$$
\alpha+\{z\in z_0+D_C^\perp:q(z)=1\}.
$$

## 6. Exact half-cube link and capacity theorems

For an `r`-clique `Q_r` in `\mathscr A_5`:

$$
\begin{array}{c|c|c}
r&\operatorname{Lk}(Q_r)&\chi\\
\hline
1&L(K_5)&5\\
2&K_3\square K_2&3\\
3&K_2\sqcup K_1&2\\
4&K_1&1\\
5&\varnothing&0.
\end{array}
$$

### Theorem 6.1 — dominating-clique capacity

For every finite loopless graph `H` and `2\le r\le5`,

$$
K_r\vee H\to\mathscr A_5
\Longleftrightarrow
\chi(H)\le5-r.
$$

For `r=1`, the exact condition is `H\to L(K_5)`; chromatic number alone is not complete.

Consequences include `K_6\not\to\mathscr A_5` and `K_3\vee C_{2m+1}\not\to\mathscr A_5`.

## 7. Exact eight-vertex factorable classification

For every graph `J` on the eight old support indices,

$$
J\to\mathscr A_5
\Longleftrightarrow
K_6\nsubseteq J
\text{ and }
K_8-C_5\nsubseteq J.
$$

Equivalently, the unused-root graph `K_8-J` contains `3K_2`, `K_3\sqcup K_2`, or `K_4`.

This theorem completely classifies the eight-vertex old-colour-factorable target. It does not classify arbitrary full duals.

## 8. Unused matchings and factorable cores

An unused `3K_2` gives an immediate factorable compression. The action of `AGL(3,2)` on three-edge matchings has three orbits of sizes

$$
28,\qquad168,\qquad224.
$$

The correct all-parallel representative is

$$
\boxed{\{01,23,45\}}.
$$

The old display `\{05,14,23\}` has directions `5,5,1` and is not all-parallel. The orbit theorem is unchanged.

Write `U_g=K_8-J_g`. Factorable badness is exactly

$$
\tau(U_g)\le2
\quad\text{or}\quad
U_g\cong C_5.
$$

Thus the static factorable bad cores are marked two-apex cores and one pentagon core. There are exactly one hundred marked two-apex types; the reported eighty-eight unmarked isomorphism types remain computational evidence.

An ideal target pivot raises vertex-cover number by at most one. Exact two-cover cores and the pentagon admit an abstract target escape, while one-star cores are ideal one-pivot traps. This is target dynamics, not a theorem that a required source support cycle exists.

## 9. Full-dual obstruction and certificate boundary

The flower `J_5` packet supplies, conditional on its displayed finite dual certificate, a full dual containing `K_3\vee C_5`. The human target argument then proves non-homomorphism to `\mathscr A_5`.

The explicit flow, reduced fibre, dual graphs, face lengths, and neighbourhood counts remain certificate data. This example shows that `K_6` is not a complete full-dual obstruction language.

## 10. Assurance and provenance

Programme B3 source:

`proof-development/affine-cdc-rigour-v1@d806168bb579dbc13f267f44f631e07de909b706`.

State retained:

`READY-FOR-CURATOR / PROVENANCE-REPAIRED`.

The valid recovered clique-link, capacity, and eight-vertex packets remain valid theorem sources. Earlier erroneous provenance allegations in draft B3 notes are not controlling. Numerical flower and core counts keep their B8 assurance classes.

This chapter is Curator-integrated authorial mathematics. It is not independent audit, Lean verification, manuscript approval, publication, release, arXiv, or DOI status.