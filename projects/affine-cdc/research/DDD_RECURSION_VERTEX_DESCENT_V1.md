# Recursive DDD failure also occurs only after strict target-vertex descent

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Parent surface:** branch head containing `DDD_LOCK_GLOBAL_PACHNER_POTENTIAL_V1.md` and `EQUALITY_RECURSION_VERTEX_DESCENT_V1.md`.

**Parents:**

- `DDD_LOCK_GLOBAL_PACHNER_POTENTIAL_V1.md`;
- `EQUALITY_RECURSION_VERTEX_DESCENT_V1.md`;
- `PACHNER_HISTORY_FIRST_FAILURE_ONE_EDGE_ATOM_V1.md`;
- `ROOT_FLOW_TRIANGLE_COMPLEX_PACHNER_V1.md`;
- the equality/DDD inverse-expansion grammar.

**Status:** exact well-foundedness theorem for DDD inverse-transfer recursion. A co-root first failure may occur at a `2--2` inverse Pachner step or a `2--0` inverse cancellation, but in either case its target graph is one stage of the surgery history inside the graph obtained after deleting the outer two-vertex cap. Hence its target order is at least two smaller than the DDD problem that generated the history. An equality first failure at an inverse cancellation has the same strict order decrease. Together with the equality-recursion theorem, every equality/DDD recursive call strictly lowers one common target-vertex coordinate.

**Not implied:** automatic consumption of the bounded direct-pairing terminal, complete horizontal/profile bookkeeping after a recursive return, category preservation at every surgery, final proof-DAG assembly, canonical acceptance, Lean verification, manuscript integration, release, publication, or the global five-support theorem.

---

## 1. Outer DDD inverse-expansion problem

Let

\[
\widehat G
\]

be the target graph of one two-vertex DDD inverse expansion. Deleting the two target vertices and reconnecting their four exterior incidences gives the reduced graph

\[
G_0,
\qquad
|V(\widehat G)|=|V(G_0)|+2.
\]

Assume a root-valued flow on `G_0` gives disjoint roots on the two reconnection edges and that all ordinary separating-channel rescues fail, so the complementary four-pole is in the oriented DDD full-channel branch.

Apply the globally monotone DDD root-surgery reduction inside that four-pole:

\[
G_0\longrightarrow G_1\longrightarrow\cdots\longrightarrow G_m.
\]

Every step is one of:

1. a root-valued `2--2` Pachner flip, preserving vertex number;
2. an equal-face `2--0` cancellation, removing two vertices.

Therefore

\[
\boxed{|V(G_j)|\le |V(G_0)|=|V(\widehat G)|-2}
\]

for every stage `j`.

The cap orientation and the ordered four external incidences are retained throughout.

---

## 2. First-failure localisation

Start from any cap-compatible root state at a route-changing or bounded terminal stage and reverse the surgery history only while the inverse local move remains root-valued.

If the complete inverse transfer fails, let

\[
G_j\longrightarrow G_{j-1}
\]

be the first failed inverse step.

The first-failure theorem gives exactly one non-root central edge in `G_(j-1)`, with value:

\[
0
\qquad\text{or}\qquad
Q_i.
\]

Every other edge is root-valued, and the ordered local four-root boundary and the outer DDD route orientation are retained.

---

## 3. Inverse Pachner failure

Suppose the failed step reverses a root-valued `2--2` Pachner flip.

### Zero branch

The restored old central value is zero. The current topology is root-valued, so the four outer roots have the form

\[
a,a,b,b
\]

with `a,b` distinct and intersecting. Hence this is the nonsingular doubled-intersecting branch and has the other root NNI topology. It is not equality recursion and not DDD recursion.

### Co-root branch

The restored old central value is a co-root. The old topology is therefore one oriented DDD inverse-expansion problem whose target graph is

\[
G_{j-1}.
\]

Since `G_(j-1)` is a stage inside the reduced graph,

\[
|V(G_{j-1})|\le |V(G_0)|=|V(\widehat G)|-2.
\]

### Theorem 3.1 — inverse-flip DDD descent

A recursive DDD problem created by an inverse Pachner flip has target order at least two below the outer DDD target:

\[
\boxed{
|V(\text{new DDD target})|
\le
|V(\widehat G)|-2.}
\]

The phrase “same-order co-root failure” is correct only relative to the adjacent stages `G_j,G_(j-1)` of the reduced history. It is not same-order relative to the outer inverse-expansion target `widehat G`.

---

## 4. Inverse cancellation failure

Suppose the failed step reverses an equal-face cancellation. Let the two reconnected edges of `G_j` carry roots

\[
a,b.
\]

Restoring the two vertices forces the central value

\[
x=a+b.
\]

Exactly three cases occur.

### Root success

If `a,b` are distinct and intersecting, the inverse cancellation is root-valued.

### Equality recurrence

If

\[
a=b,
\]

then `x=0` and the new target `G_(j-1)` is a quadruple-equality inverse-expansion problem.

### DDD recurrence

If `a,b` are disjoint, then `x` is a co-root and the new target `G_(j-1)` is the doubled-disjoint DDD/Type-T inverse-expansion problem.

In both recursive branches,

\[
|V(G_{j-1})|\le |V(G_0)|=|V(\widehat G)|-2.
\]

### Theorem 4.1 — inverse-cancellation target descent

Every equality or DDD recursive problem created while reversing a DDD reduction history has target order at least two smaller than the outer DDD target.

---

## 5. Mutual equality--DDD recursion measure

For either an equality or DDD inverse-expansion problem `P`, let

\[
N(P)
\]

be the vertex number of its target graph, including the two vertices whose inverse expansion is under consideration.

The equality-recursion theorem proves:

\[
P_{\mathrm{eq}}\longrightarrow P'_{\mathrm{eq}}
\quad\Longrightarrow\quad
N(P'_{\mathrm{eq}})\le N(P_{\mathrm{eq}})-2.
\]

Theorems 3.1 and 4.1 prove:

\[
P_{\mathrm{DDD}}\longrightarrow P'_{\mathrm{DDD}}
\quad\Longrightarrow\quad
N(P'_{\mathrm{DDD}})\le N(P_{\mathrm{DDD}})-2,
\]

and

\[
P_{\mathrm{DDD}}\longrightarrow P'_{\mathrm{eq}}
\quad\Longrightarrow\quad
N(P'_{\mathrm{eq}})\le N(P_{\mathrm{DDD}})-2.
\]

An equality history may also fail into a DDD atom; that new DDD target is likewise one stage inside the equality reduced graph and therefore satisfies the same order bound.

### Theorem 5.1 — common well-founded recursion

Every recursive edge in the mutual equality/DDD transfer graph strictly lowers

\[
\boxed{N=|V(\text{target graph})|}
\]

by at least two.

Hence:

\[
\boxed{
\text{no equality/DDD recursion cycle and no infinite alternating recursion exist}.}
\]

This is independent of which local triangle potential is used inside one fixed target order.

---

## 6. Full lexicographic measure

Inside one equality problem use

\[
\mathcal P_{\mathrm{eq}}=(E,\Phi,|V(R)|).
\]

Inside one DDD problem use

\[
\mathcal P_{\mathrm{DDD}}=(\Omega,|V(R)|).
\]

Define the tagged measure

\[
\boxed{
\mathfrak M(P)=
\bigl(
N(P),
\operatorname{tag}(P),
\mathcal P_{\operatorname{tag}(P)}
\bigr),}
\]

where the tag merely selects the appropriate finite local potential and is not used before the leading coordinate.

Then:

1. current-flow Pachner/cancellation moves within one problem strictly lower its local suffix;
2. any recursive equality/DDD call strictly lowers `N`;
3. nonsingular zero and route-changing branches leave the recursion graph;
4. category failure leaves the recursion graph through a separator or bounded degeneration.

Thus the entire equality--DDD descent is well founded.

---

## 7. Revised transfer frontier

After this theorem there is no remaining unbounded or cyclic recursion mechanism in either singular fibre.

The unresolved work is finite/compositional:

1. consume a bounded zero-vertex direct-pairing terminal;
2. identify a route-changing matching flip with cap/profile escape;
3. resume an outer inverse-transfer history after a smaller recursive problem returns;
4. package the returns without losing the ordered outer terminal route;
5. assemble the global proof DAG.

No same-order DDD recursion remains.

---

## 8. Trust boundary

### Exact here

- target-order comparison between an outer DDD problem and every stage of its reduced surgery history;
- strict order decrease for inverse-flip DDD recurrence;
- strict order decrease for inverse-cancellation equality recurrence;
- strict order decrease for inverse-cancellation DDD recurrence;
- mutual equality--DDD recursion graph is acyclic and well founded;
- one combined leading target-order measure.

### Still open

- bounded direct-pairing terminal consumption;
- route-changing matching-flip disposition;
- outer-route preservation across recursive returns;
- complete local transfer synthesis;
- global proof-DAG assembly;
- canonical acceptance, independent audit, Lean verification, manuscript integration, release, publication, and the global five-support theorem.
