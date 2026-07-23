# The relative Petersen `C6` descent is automatically category-safe

## Research dossier v1 — removal of the even-track category branch

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `c11ca04b68e95fd0223f41b3722fbcf8441ba494`.

**Parents:**

- `PETERSEN_C6_CANONICAL_STAR_SECTION_V1.md`;
- `PETERSEN_C6_RELATIVE_STAR_MOVIE_DESCENT_V1.md`;
- `ROOT_FLOW_TRIANGLE_COMPLEX_PACHNER_V1.md`;
- `BRIDGELESS_ROOT_STAR_REPLACEMENT_V1.md`;
- the standard cut-sum law for `E_5` flows.

**Status:** exact source-category strengthening of the primitive even-track descent. In the relative four-branch interface of one Petersen identity-hexagon cell, the two fixed turn branches and the two exterior side branches have values `(z,w,z,w)` with `z,w` distinct intersecting roots. The canonical NNI pairs one `z` branch with one `w` branch on each side. Such a pair cannot be the complete two-terminal boundary of one exterior connected component, because flow conservation on that component would force `z+w=0`. Therefore the new central edge cannot be a bridge. The replacement is connected and root-valued, so the canonical NNI remains in the connected bridgeless cubic category. The subsequent equal-face cancellation leaves a root-valued cubic graph with two fewer vertices; every output component is bridgeless because a bridge in a group-valued flow must carry zero, whereas every edge carries a root. Hence the `C6` exit is always strict order descent, possibly accompanied by harmless component decomposition, and never requires a separate category-terminal return.

**Assurance boundary:** this theorem assumes the relative-cell incidence model and root movie of `PETERSEN_C6_RELATIVE_STAR_MOVIE_DESCENT_V1.md`. It does not independently verify that model or confer downstream assurance status.

---

## 1. Component cut-sum law

Let `H` be a graph or multipole carrying an `E_5` flow on all internal edges, with root-valued terminal incidences. Let `C` be one connected component of the internal graph after a local region is removed. Sum the vertex equations over all vertices of `C`. Every internal edge of `C` occurs twice and cancels in characteristic two. Therefore:

### Lemma 1.1 — boundary sum of one exterior component

If the terminal incidences of `C` carry values

\[
r_1,\ldots,r_k,
\]

then

\[
\boxed{r_1+\cdots+r_k=0.}
\]

In particular, if `C` has exactly two terminal incidences with values `r,s`, then

\[
\boxed{r=s.}
\]

This remains true when the two incidences meet the same exterior vertex; they are still two distinct edge incidences in the cut sum.

---

## 2. Relative four-branch interface

For one primitive Petersen `C6` cell, the fixed turn corollas are

\[
L=(x,t,z),
\qquad
R=(s,y,w),
\]

and the two side incidences carry roots `z,w`. Relative to `L,R`, the unresolved four branches are therefore:

\[
L_z,\quad Z,\quad W,\quad R_w
\]

with values

\[
\boxed{z,z,w,w.}
\]

Here `z,w` are distinct members of the repeated side-root triangle, so

\[
\boxed{z\ne w,\qquad z+w=u\in R_5.}
\]

The current root cross path and the canonical star are the two root-valued resolutions of the `(0,2,2)` triality.

In the canonical resolution, each side of the new central edge receives exactly one `z` branch and one `w` branch. Equivalently, the two paired branch sets are

\[
\boxed{\{L_z,W\},\qquad\{Z,R_w\}}
\]

up to exchanging `Z,W` according to the chosen cyclic orientation. In either convention, both pairs have boundary values `{z,w}`.

---

## 3. The canonical NNI cannot create a bridge

Remove the two middle vertices of the relative interface and let the four terminal incidences be partitioned by the connected components of the exterior graph.

For a two-vertex NNI replacement, the new central edge is a bridge exactly when one of the two paired terminal sets is itself a complete two-incidence exterior component block. This is the four-terminal instance of the internal bridge criterion.

### Theorem 3.1 — no canonical bridge block

Neither canonical pair `{z,w}` can be a two-terminal exterior component block.

### Proof

If one pair were the complete boundary of an exterior component, Lemma 1.1 would give

\[
z+w=0.
\]

But `z,w` are distinct roots and `z+w` is the third nonzero root of their support triangle. Contradiction. ∎

### Corollary 3.2 — bridgeless canonical NNI

The canonical root-preserving NNI

\[
P_i^\times\longrightarrow S_i^\star
\]

produces a connected bridgeless cubic multigraph.

### Proof

The two new middle vertices are joined by the central edge, so the replacement connects all exterior components incident with the four terminals. Every terminal edge remains nonbridging because its exterior component has at least one other terminal incidence in the original bridgeless graph. The central edge is nonbridging by Theorem 3.1. All unchanged old edges remain nonbridging: if deleting one separated a component with no terminal incidence, it was already a bridge before the local replacement; if both shores contain terminals, the connected two-vertex replacement reconnects them unless the central edge gives precisely a forbidden two-terminal block, already excluded. ∎

Thus the relative movie does not need the weaker alternative “NNI or category exit”. Its NNI step is category-safe unconditionally in the identity-hexagon setting.

---

## 4. Equal-face cancellation and nonzero-flow bridgelessness

In the canonical star, the central vertex and the side-cherry vertex are equal root triangles joined along the third root `u=z+w`. Cancel this equal-face dipole and reconnect equal-labelled incidences.

The resulting graph `G'` has:

1. exactly two fewer vertices;
2. the same exterior root labels;
3. a root-valued `E_5` flow on every edge;
4. cubic degree at every remaining vertex.

It may a priori be connected or split into several components.

### Lemma 4.1 — a bridge in a flow has value zero

Let an edge `e` be a bridge of a graph carrying a flow over any abelian group. Sum the vertex equations over one shore of `G-e`. Every internal edge cancels, leaving only the value on `e`. Hence

\[
\boxed{x(e)=0.}
\]

### Theorem 4.2 — output components are bridgeless

Every connected component of `G'` is bridgeless.

### Proof

Every edge of `G'` carries a root of `R_5`, hence a nonzero value. Lemma 4.1 excludes bridges. ∎

If `G'` is disconnected, each component is a finite bridgeless cubic multigraph already carrying the restricted root flow. No unresolved component is created.

---

## 5. Strict contextual descent

Let the cap-context target before the cancellation have `N` source vertices. After cancellation the total number of source vertices is

\[
\boxed{N-2.}
\]

The ordered exterior four-port word and cap shore are unchanged. If the graph remains connected, this is one ordinary lower-order cap-context target. If it splits, the component containing the distinguished outer cap data has fewer than `N` vertices, while every other component is already root-solved by restriction of the current flow.

### Theorem 5.1 — unconditional strict-order exit

Every primitive Petersen `C6` track reaches a cap-context problem of strictly smaller total vertex order. No separator/category terminal is needed.

The same conclusion holds for a `C8` after choosing one of its two `C6` factors and applying the seam-preserving relative movie there.

### Consequence

The even-track branch of contextual transfer has the exact disposition

\[
\boxed{
C_6,C_8
\Longrightarrow
\text{strict target-order descent}.}
\]

It no longer carries an auxiliary category alternative.

---

## 6. Correction to the repaired authority chain

Read `PETERSEN_C6_RELATIVE_STAR_MOVIE_DESCENT_V1.md` and `CONTEXTUAL_TRANSFER_REPAIRED_AUTHORITY_V2.md` with the following strengthening:

- the relative canonical NNI is automatically connected and bridgeless;
- the equal-face cancellation output is componentwise bridgeless by nonzero-flow conservation;
- the total target order drops by exactly two;
- disconnected output components require no new theorem, since they inherit root flows and only the distinguished component continues the contextual problem.

Therefore even-track consumption contributes a strict induction edge, not a category-terminal edge.

---

## 7. Trust boundary

### Exact here

- boundary-sum law for each exterior component;
- impossibility of a two-terminal `{z,w}` block with `z\ne w`;
- automatic bridgelessness of the canonical relative NNI;
- bridge-zero lemma for group-valued flows;
- componentwise bridgelessness after equal-face cancellation;
- exact two-vertex target-order drop;
- removal of the category branch from primitive even-track consumption.

### Imported authorial mathematics

- the relative `(0,2,2)` cell model;
- canonical star section and overlap compatibility;
- equal-face cancellation preserving the exterior word;
- `C8` decomposition into seam-compatible `C6` factors.

### Not claimed

- downstream proof development or independent reconstruction;
- canonical acceptance;
- Lean verification;
- manuscript integration;
- release, arXiv, DOI, peer review, or publication.
