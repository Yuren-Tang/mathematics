# Face-transition systems and affine obstruction arrangements

**Programme:** `AffineCDC — Research Lead`  
**Status:** theorem-level structural checkpoint; not canonical pending Director review and literature audit  
**Parents:** `FIVE_CDC_COLORED_SURFACE_DUAL_HALFCUBE_V1.md`, `FIVE_CDC_GAUGE_PARTIAL_PETRIAL_CORRESPONDENCE_V1.md`, `FIVE_CDC_AFFINE_SUBSPACE_ARRANGEMENT_SIEVE_V1.md`

## 1. Purpose

For a fixed nowhere-zero Fano flow, the reduced gauge code parametrizes a finite family of cycle-face embeddings related by code-filtered partial Petrials. The corrected five-support target is a graph homomorphism

\[
T_g\longrightarrow \mathscr A_5
\]

from the full dual triangulation, not merely from its eight-colour quotient.

This packet gives an exact transition model for the faces and proves that every fixed marked dual obstruction core occurs on an affine subspace of the gauge torsor. In particular, the locus carrying a marked dual `K_6` is affine, and the entire `K_6`-bad region is a finite affine-subspace arrangement.

The result reconnects the new surface/Petrial programme to the existing stress, Fourier, intersection-lattice, and Möbius-sieve machinery.

## 2. The fixed face-side set

Let

\[
g:E(G)\to E(K_8)
\]

be a root lift of a cubic loopless multigraph. At a source vertex `v`, the three incident roots form the three edges of a target triangle on three local support indices.

Define the set of **face-side darts**

\[
\mathcal D_g
:=
\{(v,e,a):v\in e,\ a\in g(e)\}.
\]

There are two fixed-point-free involutions on this set.

### Vertex transition

For a local support index `a` at `v`, exactly two of the three incident source edges have root labels containing `a`. Pair the two corresponding darts. Denote the resulting involution by

\[
\nu.
\]

### Edge transition

For a source edge `e=uv` with

\[
g(e)=\{a,b\},
\]

the untwisted edge transition is

\[
\epsilon_0:(u,e,a)\leftrightarrow(v,e,a),
\qquad
(u,e,b)\leftrightarrow(v,e,b).
\]

Let `k` be an admissible gauge field, and write

\[
k_u+k_v=\lambda_e(a+b),
\qquad \lambda_e\in\mathbf F_2.
\]

The corresponding edge transition is

\[
\epsilon_\lambda=
\begin{cases}
\epsilon_0,&\lambda_e=0,\\
(u,e,a)\leftrightarrow(v,e,b),\ (u,e,b)\leftrightarrow(v,e,a),&\lambda_e=1.
\end{cases}
\]

Thus `\lambda_e=1` is exactly the face-side swap of the partial Petrial theorem.

### Theorem 2.1 — face-transition model

The face cycles of the embedding `S_{g^k}` are exactly the connected components of the two-regular graph on `\mathcal D_g` whose edge set is the union of the matchings `\nu` and `\epsilon_\lambda`.

Equivalently, they are the orbits of the permutation

\[
\nu\epsilon_\lambda.
\]

#### Proof

A face boundary alternates between two operations:

1. at a source vertex it continues through the other incident source edge carrying the same local support index, which is `\nu`;
2. across a source edge it follows the face-side identification prescribed by the embedding, which is `\epsilon_\lambda`.

Every dart has one transition of each kind, so the union is two-regular and its connected components are precisely the face-boundary circuits. The local gauge admissibility equation guarantees that the translated support colour is constant along each circuit. ∎

This model keeps the face-side set fixed while the gauge code changes only the edge matching.

## 3. Pointwise persistence of marked faces

Fix one gauge state `\beta` and let `F` be one face cycle in its transition system. Let

\[
Z(F)\subseteq E(G)
\]

be the set of source edges traversed by `F`. For a finite marked family of distinct faces

\[
\mathcal F=\{F_1,\ldots,F_m\},
\]

put

\[
Z(\mathcal F):=\bigcup_i Z(F_i).
\]

Let `B_f` be the reduced gauge code of the fixed projected Fano flow. For a difference word

\[
\lambda\in B_f,
\]

denote its coordinate restriction by

\[
\rho_{\mathcal F}(\lambda)
:=
\lambda|_{Z(\mathcal F)}.
\]

### Theorem 3.1 — marked-face stabilizer

Starting from the gauge state `\beta`, the same face-side dart sets

\[
F_1,\ldots,F_m
\]

remain face cycles after adding `\lambda` if and only if

\[
\boxed{\rho_{\mathcal F}(\lambda)=0.}
\]

#### Proof

If `\lambda` vanishes on every source edge traversed by the marked faces, all edge transitions used by those face cycles remain unchanged, so every marked dart circuit persists.

Conversely, suppose `\lambda_e=1` for an edge traversed by a marked face `F_i`. At `e`, the old edge transition from a dart of `F_i` is replaced by the crossed transition to the dart that belonged to the other old incident face. Hence the dart set of `F_i` is not invariant under the new transition system and cannot remain the same face cycle. ∎

### Corollary 3.2 — affine occurrence locus

The set of gauge states in which one fixed marked family of face-side circuits occurs is the affine subspace

\[
\boxed{
\beta+\ker\rho_{\mathcal F}
\subseteq B_f.
}
\]

If

\[
r(\mathcal F):=\operatorname{rank}\rho_{\mathcal F},
\]

then the marked family occurs in exactly

\[
2^{\dim B_f-r(\mathcal F)}
\]

gauge states.

Call `r(\mathcal F)` the **exposure rank** of the marked face system.

- `r=0`: the system is pointwise rigid throughout the whole gauge orbit;
- `r>0`: some admissible partial Petrial destroys the marked system;
- larger rank means a smaller stabilizer and fewer states carrying that exact system.

In dual-code language, `r=0` precisely when every coordinate functional supported on `Z(\mathcal F)` vanishes on `B_f`; equivalently, every unit coordinate vector of that zone belongs to `B_f^\perp`.

## 4. Marked obstruction cores

Let `H` be a finite graph with

\[
H\not\longrightarrow\mathscr A_5.
\]

A **marked `H`-core** in a gauge state is a marked family of face cycles whose dual adjacency graph contains a specified copy of `H`.

If the same face-side circuits persist pointwise, all source edges witnessing their dual adjacencies also persist, so the same marked `H` remains present.

### Theorem 4.1 — obstruction-core locus

For every fixed marked `H`-core `C`, its occurrence locus in the gauge torsor is an affine subspace

\[
\boxed{
A_C=\beta_C+\ker\rho_C.
}
\]

Every state in `A_C` is componentwise bad because its dual triangulation contains a graph that does not map to `\mathscr A_5`.

The theorem applies in particular to:

- `H=K_6`, by the clique-number bound `\omega(\mathscr A_5)=5`;
- any marked copy of the `K_6`-free Mycielski obstruction `M(K_5)`;
- any later finite library of certified half-cube homomorphism obstructions.

## 5. The `K_6` arrangement

Let

\[
\mathfrak K_f
\]

be the finite set of all marked `K_6` face systems that occur in at least one gauge state above the fixed Fano flow. Then the locus of gauge states whose dual triangulation contains a marked `K_6` is

\[
\boxed{
\mathcal K_f
=
\bigcup_{C\in\mathfrak K_f}A_C.
}
\]

Thus the first visible componentwise obstruction is a finite affine-subspace arrangement in `B_f`.

### Corollary 5.1 — union-bound escape criterion

If

\[
\sum_{C\in\mathfrak K_f}2^{-r(C)}<1,
\]

then

\[
\mathcal K_f\ne B_f,
\]

so some gauge state has a `K_6`-free dual triangulation.

#### Proof

Each `A_C` has relative density `2^{-r(C)}` in `B_f`. The union bound shows that their union has density strictly less than one. ∎

This criterion is only sufficient. Exact avoidance may instead be tested by the intersection lattice and Möbius inversion already developed for affine-subspace arrangements.

A `K_6`-free state need not yet map to `\mathscr A_5`; the Mycielski warning shows that deeper graph-homomorphism cores exist in general. The same arrangement construction applies to any finite obstruction library once compatible cores are identified.

## 6. Topology of a visible `K_6`

The following geometric lemma applies to a connected simplicial closed triangulation `T` containing a clique on a six-set `X`.

Call a clique edge `xy` **externally exposed** when one of its incident triangular faces is

\[
xyz
\]

with `z` outside `X`.

### Proposition 6.1 — projective core or exposed edge

Exactly one of the following holds.

1. `V(T)=X`, so the one-skeleton is `K_6`; then
   \[
   E=15,\qquad F=10,\qquad\chi(T)=6-15+10=1,
   \]
   and `T` is the six-vertex triangulation of the real projective plane. Its cellular dual is the Petersen graph in its six-pentagon projective-plane embedding.
2. Some clique edge is externally exposed.

#### Proof

If `T` has a vertex outside `X`, connectedness gives a clique vertex `x` with an outside neighbour. The link of `x` is a cycle containing all five other clique vertices and at least one outside vertex. At a transition in this cyclic link between an inside and an outside neighbour, there is a triangular face `xyz` with `y\in X` and `z\notin X`; hence the clique edge `xy` is externally exposed.

If no outside vertex exists, the simplicial one-skeleton is exactly `K_6`. The displayed Euler count gives a closed surface of Euler characteristic one, hence the real projective plane. The six-vertex triangulation is unique up to combinatorial isomorphism, and its dual is the hemi-dodecahedral Petersen map. ∎

The uniqueness of the six-vertex triangulation of `\mathbb{RP}^2` is standard; it is noted, for example, in A. Gaifullin, *634 vertex-transitive and more than 10^103 non-vertex-transitive 27-vertex triangulations of manifolds like the octonionic projective plane* (2022). Independently, it is verified here by the finite fact that the ten triangular faces form, up to `S_6`, the unique `2-(6,3,2)` design.

### Proposition 6.2 — exposed-edge cycle

If `T` has more than six vertices, form a graph `H_X` on `X` from the externally exposed clique edges. Every nonisolated vertex of `H_X` has degree at least two. Consequently `H_X` contains a cycle.

#### Proof

At a clique vertex `x` with outside neighbours, inspect the cyclic link of `x`. The five other clique vertices occur in one or more runs separated by outside vertices. If there is one run, its two distinct endpoints are exposed; if there are several runs, their boundary vertices include at least two distinct clique neighbours. Each corresponding edge from `x` is externally exposed. Thus the nonisolated part of `H_X` has minimum degree at least two and therefore contains a cycle. ∎

This exposed cycle is a natural geometric candidate on which an admissible Petrial word may act. Its existence does not by itself prove that the required word lies in the gauge code.

## 7. The thirty-vertex fixed-flow obstruction revisited

For the fixed obstruction with one-dimensional reduced gauge code:

- the base dual has eleven vertices and contains one `K_7`, hence exactly seven marked `K_6` subcliques inside that `K_7`;
- the other reduced lift has thirteen dual vertices and exactly two marked `K_6` cliques;
- the unique nonzero gauge word is supported on source edges
  \[
  \{1,3,14,16,40,41\};
  \]
- this word meets the face zone of every one of the seven base cliques and both cliques in the other lift.

Hence every marked clique has exposure rank one: the nontrivial Petrial destroys every old marked `K_6`. Nevertheless, the other state creates replacement `K_6` cliques, and the two-state gauge orbit remains entirely componentwise bad.

This is the first exact example of a **clique-renewal obstruction**:

\[
\boxed{
\text{no individual }K_6\text{ is rigid, but the }K_6\text{ arrangement covers the whole gauge torsor.}
}
\]

The calculation is reproduced by the private verifier

`verify_face_transition_k6_arrangement.py`.

## 8. Revised mechanism and next target

The visible obstruction theory now has three distinct levels.

1. **Rigid core.** A marked obstruction has exposure rank zero and survives every gauge move. This gives a direct dual-code certificate.
2. **Mobile renewal.** Every marked core can be destroyed, but the affine obstruction arrangement still covers the torsor because new cores appear elsewhere.
3. **Arrangement escape.** The obstruction subspaces fail to cover `B_f`; then a state avoiding the selected finite obstruction library exists.

The next theorem-level tasks are therefore:

- compute or bound exposure ranks from the gauge/stress presentation without enumerating the whole torsor;
- describe intersections of marked-clique subspaces and apply the existing Möbius arrangement sieve;
- classify the clique-renewal mechanism in the one-dimensional certificate and search for higher-dimensional analogues;
- enlarge the obstruction library beyond `K_6`, while respecting the distinction between arbitrary graphs and compatible closed dual triangulations.

No statement here proves that every gauge fibre has a `K_6`-free state, that every `K_6`-free compatible dual maps to `\mathscr A_5`, or that every cubic graph has a five-support cycle double cover.
