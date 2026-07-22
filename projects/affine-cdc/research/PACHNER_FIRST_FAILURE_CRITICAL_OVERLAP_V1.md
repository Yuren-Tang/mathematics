# First-failure atoms have only one bounded Pachner critical overlap

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Parent surface:** branch head containing `EQUALITY_IDENTITY_HEXAGON_EXACT_CENSUS_V1.md`.

**Parents:**

- `PACHNER_HISTORY_FIRST_FAILURE_ONE_EDGE_ATOM_V1.md`;
- `ROOT_FLOW_TRIANGLE_COMPLEX_PACHNER_V1.md`;
- `FULL_DEFECT_TREE_NNI_DESCENT_V1.md`;
- `DDD_RECURSION_VERTEX_DESCENT_V1.md`;
- the root/co-root shift criteria in `CONNECTED_CYCLE_CORRECTION_RIGIDITY_V1.md`.

**Status:** exact critical-overlap theorem. A first failed inverse transfer carries exactly one zero or co-root edge. A root Pachner move disjoint from that edge commutes with the defect insertion. If the move uses one root edge adjacent to the defect, the complete local coefficient table has only three outcomes: a zero defect remains one zero defect; a co-root defect either remains one co-root defect, or creates one additional adjacent co-root edge. The latter two-edge defect support is exactly a three-vertex full-defect tree and therefore immediately admits the established category-safe root-lowering NNI. Hence a first-failure atom cannot interact with a root-surgery history by producing an unbounded defect cloud or a new critical-pair alphabet.

**Not implied:** complete outer-route preservation, a global confluence theorem for arbitrary Pachner histories, proof that every recursive return strictly lowers the outer equality/DDD potential, final proof-DAG closure, canonical acceptance, Lean verification, manuscript integration, release, publication, or the global five-support theorem.

---

## 1. One-edge first-failure state

Let

\[
x:E(G)\longrightarrow E_5
\]

be an `E_5`-flow on a cubic graph or multipole such that exactly one edge

\[
c=uv
\]

has non-root value. By the first-failure theorem,

\[
\boxed{x(c)=0\quad\text{or}\quad x(c)=Q_i}
\]

for one co-root

\[
Q_i=\sum_{h\ne i}e_h,
\]

and every other edge of `G` is root-valued.

At the endpoint `u`, let the other two incident roots be

\[
a,b\in R_5.
\]

Conservation gives

\[
\boxed{x(c)=a+b.}
\]

Thus:

1. if `x(c)=0`, then
   \[
   a=b;
   \]
2. if `x(c)=Q_i`, then `a,b` are disjoint roots whose four support indices are exactly `[5]\setminus\{i\}`.

In the co-root case, both `a` and `b` avoid the missing index `i`.

---

## 2. A root Pachner move adjacent to the defect

Let the root edge `a` join `u` to a second vertex `w`. Let the other two root values at `w` be

\[
d,e\in R_5.
\]

Since `w` is root-valued,

\[
\boxed{a=d+e,}
\]

and `d,e` are distinct intersecting roots.

Removing the two vertices around `a` exposes the four branch values

\[
x(c),\ b,\ d,\ e.
\]

Their total sum is zero. Besides the current central value `a`, the two NNI central values are

\[
\boxed{q=x(c)+d=b+e}
\]

and

\[
\boxed{r=x(c)+e=b+d.}
\]

These are the complete two alternatives.

---

## 3. Zero atom: no defect proliferation

Assume

\[
x(c)=0.
\]

Then `a=b`, and the two alternative central values are

\[
q=d,
\qquad
r=e.
\]

Both are roots.

### Theorem 3.1 — zero-overlap propagation

A root Pachner move on any root edge adjacent to a zero first-failure atom has two root-valued NNI alternatives. After either move:

1. the old zero edge `c` remains the unique non-root edge;
2. the new central edge is root-valued;
3. no second defect is created;
4. all exterior root labels are unchanged.

Thus a zero atom may change one endpoint under a neighbouring Pachner move, but it cannot branch or increase the defect count.

---

## 4. Co-root atom: the missing-index dichotomy

Assume

\[
x(c)=Q_i.
\]

Since the adjacent root `a` avoids `i` and

\[
a=d+e,
\]

the `i`-coordinates of `d,e` agree:

\[
\boxed{d_i=e_i.}
\]

Hence exactly one of two cases occurs.

### Case 4.1 — both neighbouring roots avoid `i`

Assume

\[
i\notin d,
\qquad
i\notin e.
\]

The co-root shift criterion gives

\[
Q_i+d\in R_5,
\qquad
Q_i+e\in R_5.
\]

Therefore both NNI central values `q,r` are roots.

### Theorem 4.1 — good co-root overlap

If the triangle on the far side of the adjacent root edge avoids the missing index of the co-root defect, either Pachner alternative remains root-valued. The old edge `c` remains the unique co-root defect, and no new defect is created.

### Case 4.2 — both neighbouring roots contain `i`

Assume

\[
i\in d,
\qquad
i\in e.
\]

Since `d,e` are distinct intersecting roots and both contain `i`, write

\[
d=ij,
\qquad
e=ik,
\qquad j\ne k.
\]

Then

\[
a=d+e=jk.
\]

The two NNI values are

\[
Q_i+d=Q_j,
\qquad
Q_i+e=Q_k.
\]

Thus neither alternative is a root; each is another co-root.

Choose, for example, the first NNI. Its new central edge has value `Q_j`. At the new vertex incident with the old defect edge, the local state is

\[
\boxed{(Q_i,Q_j,ij).}
\]

This is exactly the degree-two co-root transport state of the full-defect-tree grammar.

The defect support now consists of exactly two adjacent co-root edges:

\[
Q_i\text{ --- }Q_j.
\]

Because the original flow had only one defect edge, this component has exactly three source vertices: the two outer defect leaves and the shared transport vertex.

### Theorem 4.2 — bad co-root overlap is one three-vertex defect tree

If the far triangle contains the missing index `i`, an adjacent root Pachner move creates exactly one additional co-root edge and no other non-root value. The complete defect component is a three-vertex full-defect tree with one transport vertex.

No larger defect component and no new local coefficient type occurs.

---

## 5. Immediate normalization of the bad overlap

The full-defect-tree NNI theorem applies to every full-defect component with at least three vertices. Therefore the component from Theorem 4.2 has an internal NNI whose new central value is a root and whose defect energy drops by one.

Since the component has exactly two defect edges, the normalized outcome has at most one defect edge.

The category-safe NNI alternative gives exactly one of:

1. a connected bridgeless graph with a flow carrying at most one zero/co-root defect;
2. a two-edge separator in the pre-move graph;
3. a bounded acyclic or parallel-edge degeneration.

### Theorem 5.1 — normalized co-root critical pair

A co-root first-failure atom and one adjacent root Pachner move compose, after at most one defect-tree normalization, to:

\[
\boxed{
\text{root flow}
\quad\text{or}\quad
\text{one zero/co-root atom}
\quad\text{or}\quad
\text{separator/category exit}.}
\]

The defect count never needs to exceed two transiently and is at most one after normalization.

---

## 6. Disjoint surgery commutation

Let `S_1,S_2` be two local source surgeries, each supported on two adjacent cubic vertices. Assume their support vertices and boundary incidences are disjoint.

Then replacing the two local topologies in either order produces canonically the same cubic multigraph with the same exterior incidence identification.

If one operation is a first-failure insertion and the other is a root-valued Pachner flip or equal-face cancellation, the edge-value assignments also agree away from the two disjoint supports.

### Theorem 6.1 — disjoint critical moves commute

A first-failure atom commutes strictly with every root-surgery move whose local support is disjoint from the atom neighbourhood.

Consequently a genuinely noncommuting first-failure/Pachner pair must share one endpoint of the defect edge and is covered by Sections 2--5.

---

## 7. Complete local critical-overlap theorem

### Theorem 7.1

Let one inverse-transfer history have a first failed step, producing one zero or co-root edge atom. Let one root-compatible Pachner move from the surrounding equality/DDD descent meet that failed step.

Exactly one of the following holds.

1. **Disjoint supports.**  
   The moves commute exactly.

2. **Zero overlap.**  
   The zero atom remains one zero atom and the neighbouring move stays root-valued.

3. **Good co-root overlap.**  
   The co-root atom remains one co-root atom and the neighbouring move stays root-valued.

4. **Bad co-root overlap.**  
   One transient adjacent co-root is created, giving a three-vertex full-defect tree; one established root-lowering NNI returns the system to at most one atom or exposes a separator/category exit.

There is no fifth overlap type.

In particular, a first-failure atom cannot generate:

- an unbounded defect tree;
- an independent second co-root direction persisting after normalization;
- a new Pachner critical-pair alphabet;
- or a history-level defect cloud.

---

## 8. Consequence for the final transfer bridge

The remaining contextual-transfer problem can now be separated into two tasks.

### Local task — closed here

When a smaller equality/DDD recursive return is commuted through an outer root-surgery history:

- disjoint moves commute;
- every overlapping move is bounded by Theorem 7.1;
- after immediate normalization, at most one first-failure atom survives.

Thus recursive return cannot reset the outer history by creating uncontrolled non-root support.

### Global task — still open

One must still choose and order the commutations so that one of the established well-founded quantities decreases globally:

\[
|V(\text{target})|,
\qquad
\mathcal P_{\mathrm{eq}},
\qquad
\mathcal P_{\mathrm{DDD}},
\qquad
\text{remaining history depth},
\]

or else the physical route changes and the cap-escape theorem applies.

Equivalently, the last missing theorem is now a global scheduling statement for one nonbranching defect token, not a new local algebra or graph carrier theorem.

---

## 9. Trust boundary

### Exact here

- complete local coefficient formula for an atom adjacent to a root Pachner edge;
- zero atom never proliferates;
- missing-index dichotomy for a co-root atom;
- exact identities `Q_i+ij=Q_j` and `Q_i+ik=Q_k` in the bad overlap;
- identification of the transient state with the degree-two transport grammar `(Q_i,Q_j,ij)`;
- reduction of the transient two-edge defect component by the full-defect-tree theorem;
- disjoint surgery commutation;
- complete four-case critical-overlap classification;
- exclusion of every unbounded local critical-pair alphabet.

### Still open

- one globally monotone scheduling rule for repeated critical-overlap commutations;
- proof that a surviving single atom either reaches a strictly smaller recursive target or changes the outer route;
- complete contextual-transfer synthesis;
- final proof-DAG audit and well-founded packaging;
- canonical acceptance, independent audit, Lean verification, manuscript integration, release, publication;
- the global five-support theorem.
