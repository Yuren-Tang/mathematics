# Root flows form five-coloured triangle complexes and root NNI is a Pachner flip

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Parent surface:** current equality-lock branch containing the private-matching/Tait and two-rail reductions.

**Status:** exact source-level geometric model for every root-valued `E_5` flow. A cubic root flow is the dual graph of a five-coloured triangle pseudocomplex. Two adjacent distinct root triangles admit one and only one root-valued NNI; it is the `2--2` Pachner flip across the corresponding tetrahedron. Two adjacent equal triangles admit the label-preserving two-face dipole cancellation. Thus every root-compatible two-vertex surgery in the programme is one of these two simplicial moves.

**Not implied:** that an arbitrary sequence of flips preserves the complete five-support boundary profile, that every coloured surface patch is reducible without a topological obstruction, elimination of the connected equality carrier, global proof-DAG closure, canonical acceptance, Lean verification, manuscript integration, or the global five-support theorem.

---

## 1. Roots as edges and cubic vertices as triangles

Write

\[
R_5=\{ij=e_i+e_j:1\le i<j\le5\}.
\]

Identify `ij` with the edge `{i,j}` of `K_5`.

Let

\[
x:E(G)\longrightarrow R_5
\]

be a root-valued `E_5` flow on a cubic graph or multipole.

### Lemma 1.1 — root-triangle law

At every cubic vertex `v`, the three incident roots are exactly the three edges of one unique support triangle

\[
\Delta_v=\{i,j,k\}\subset[5].
\]

### Proof

Let two incident roots be `a,b`. Since the third value is `a+b` and is again a root, `a,b` must be distinct and intersect in exactly one support index. Write

\[
a=ij,
\qquad
b=ik.
\]

Then

\[
a+b=jk.
\]

Hence the three values are

\[
ij,ik,jk,
\]

the edge set of the unique triangle on `{i,j,k}`. ∎

Thus the ten possible local root-flow states are the ten three-subsets of `[5]`.

---

## 2. The triangle pseudocomplex

For every source vertex `v`, take one abstract triangle whose vertex labels are the three support indices in `Delta_v`. Label its sides by the corresponding roots.

For every source edge

\[
e=uv,
\qquad
x(e)=ij,
\]

glue the side `ij` of `Delta_u` to the side `ij` of `Delta_v`.

For a multipole, terminal semiedges leave the corresponding triangle sides unglued.

Denote the resulting two-dimensional cell complex by

\[
\mathfrak T_x.
\]

### Theorem 2.1 — exact duality

The dual cubic graph of `mathfrak T_x` is the original source graph or multipole.

- triangle faces correspond to source vertices;
- glued triangle sides correspond to source edges;
- unglued sides correspond to terminal semiedges;
- the side label is exactly the root-flow value.

Every side of a closed source graph is glued exactly twice, so `mathfrak T_x` is a finite two-dimensional pseudomanifold. Vertex links may have several components; splitting such singular vertices gives an ordinary compact surface without changing the dual graph or any local surgery below.

### Converse 2.2

Conversely, any finite triangle pseudocomplex whose triangle vertices are labelled by distinct elements of `[5]` and whose glued sides have matching unordered endpoint labels gives a root-valued `E_5` flow on its dual cubic graph.

The flow equation at one dual vertex is the boundary identity of its labelled triangle.

---

## 3. Two adjacent triangles

Let adjacent source vertices `u,v` be joined by an edge labelled

\[
ij.
\]

Then both support triangles contain `{i,j}`.

Exactly one of two cases occurs.

### Case E — equal faces

\[
\Delta_u=\Delta_v=\{i,j,k\}.
\]

The four noncentral incidences have labels

\[
ik,jk,ik,jk.
\]

### Case T — tetrahedral pair

The triangles are distinct:

\[
\Delta_u=\{i,j,k\},
\qquad
\Delta_v=\{i,j,\ell\},
\qquad
k\ne\ell.
\]

Their union uses the four support indices

\[
\{i,j,k,\ell\}.
\]

The four exterior side labels are

\[
ik,jk,i\ell,j\ell.
\]

---

## 4. Equal faces give root-compatible dipole cancellation

In Case E, remove `u,v` and their common edge `ij`. Reconnect:

\[
ik\text{ to }ik,
\qquad
jk\text{ to }jk.
\]

### Theorem 4.1 — equal-triangle cancellation

The cancellation:

1. removes two source vertices;
2. preserves every exterior root label;
3. preserves the root-flow equations;
4. is the simplicial two-face cancellation of two equal labelled triangles.

If the resulting cubic graph leaves the connected bridgeless category, the established dipole-category lemma exposes a two-/three-edge separator, loop/parallel degeneration, or bounded appendage.

No coefficient defect is introduced.

---

## 5. Distinct faces give the unique root NNI

Assume Case T. The two old faces are

\[
ijk,
\qquad
ij\ell,
\]

glued along `ij`.

Replace them by

\[
ik\ell,
\qquad
jk\ell,
\]

glued along the opposite edge

\[
k\ell.
\]

On the dual cubic graph this removes the old edge `ij`, reconnects the four exterior incidences in the unique crossed order dictated by their root labels, and inserts the new central edge `k\ell`.

### Theorem 5.1 — root-valued Pachner NNI

The replacement is root-valued because

\[
ik+i\ell=k\ell,
\qquad
jk+j\ell=k\ell.
\]

It preserves the ordered four-root boundary

\[
ik,jk,i\ell,j\ell
\]

and gives the new local triangles

\[
ik\ell,
\qquad
jk\ell.
\]

This is exactly the coloured `2--2` Pachner flip on the boundary of the tetrahedron `{i,j,k,ell}`.

### Theorem 5.2 — uniqueness

For two adjacent distinct root triangles, the displayed Pachner flip is the unique nontrivial two-vertex NNI whose two new internal vertex equations are root-valued.

### Proof

The four exterior roots have three pairings.

1. The original pairing has common sum `ij`.
2. Pairing the two roots through `i` and the two roots through `j` has common sum `kell` and gives the displayed flip.
3. The remaining pairing has sums
   \[
   ik+j\ell,
   \qquad
   jk+i\ell,
   \]
   which are equal co-roots supported on all four indices and are not roots.

Thus exactly two topologies are root-valued: the original one and the displayed tetrahedral flip. ∎

---

## 6. Complete two-vertex root-surgery classification

### Theorem 6.1

Let two adjacent vertices of a root-valued cubic flow be regarded as a four-root interface. Exactly one of:

1. **equal support triangles:** label-preserving dipole cancellation;
2. **distinct support triangles:** unique tetrahedral `2--2` root NNI.

There is no third root-compatible local topology.

The omitted third pairing is precisely the co-root/DDD resolution of the same four-root interface.

### Corollary 6.2 — NNI and DDD triality

For distinct adjacent triangles on a four-support set, the three local pairings have central values

\[
\boxed{
\text{old root},
\quad
\text{opposite root},
\quad
\text{four-support co-root}.}
\]

Hence the root NNI and the DDD crossed resolution are the two nontrivial members of one tetrahedral triality.

---

## 7. Boundary and category behaviour

The Pachner NNI is defined at labelled incidences. Exterior attachment vertices may coincide.

The established category-safe NNI lemma therefore applies verbatim. Exactly one of:

1. the modified graph is connected and bridgeless;
2. the original graph has a two-edge separator;
3. a cyclic three-/four-edge separator is exposed;
4. a loop, parallel-edge, or bounded acyclic degeneration is exposed.

Thus failure of the geometric move to remain in the inductive category is itself a progress certificate.

---

## 8. Relation to the equality frontier

For an equality lock, the private-matching/Tait decomposition chooses one rank-two projection. Its seven branch states and three matching states are simply the ten labelled triangle faces of `mathfrak T_x`, partitioned according to whether they contain the private root.

- a branch--branch edge is one glued edge between two nonprivate faces;
- a private-root edge joins two faces containing the private edge;
- crossed private-edge surgery is one tetrahedral Pachner flip;
- aligned private-edge cancellation is the equal-face dipole move;
- DDD triality is the third, co-root pairing of the same tetrahedron.

Therefore the connected equality transfer problem may be studied as a coloured surface-patch reduction problem with only:

\[
\boxed{
2\!-\!2\text{ root flips},
\quad
2\!-\!0\text{ equal-face cancellations},
\quad
\text{small-cut/category exits}.}
\]

No separate local root-surgery alphabet remains.

---

## 9. Exact finite certificate

For the ten support triangles of the five-vertex simplex:

- there are `30` unordered adjacent distinct triangle pairs;
- every pair lies in a unique four-support tetrahedron;
- every pair has exactly one nontrivial root-valued NNI;
- the third pairing is always the four-support co-root resolution.

The equality seven-state restriction and its finer `3+12` table are recorded separately in `EQUALITY_LOCK_SEVEN_SECTION_PACHNER_DESCENT_V1.md`.

---

## 10. Trust boundary

### Exact here

- root-triangle law at every cubic vertex;
- construction of the five-coloured triangle pseudocomplex;
- exact duality with the source cubic graph;
- equal-triangle dipole cancellation;
- unique root-valued tetrahedral NNI for distinct triangles;
- identification with the `2--2` Pachner flip;
- complete root/root/co-root local triality;
- category-safe alternatives inherited from the incidence-level NNI and dipole lemmas.

### Still open

- a cover-independent theorem that arbitrary flip/cancellation sequences preserve enough of the complete five-support profile;
- topological reduction of every connected equality surface patch to the identity hexagon or a separator;
- conversion of a prime coloured annulus/Möbius patch to the already calibrated DDD classes;
- global well-founded packaging;
- canonical acceptance, independent audit, Lean verification, manuscript integration, release, publication, and the global five-support theorem.
