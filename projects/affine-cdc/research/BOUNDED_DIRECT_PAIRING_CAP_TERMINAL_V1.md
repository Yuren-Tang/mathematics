# The zero-vertex direct-pairing terminal is a bridge or the soluble theta graph

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `276e221f31b4bbf4808739ccc3456d3509f8099d`.

**Parents:**

- `EQUALITY_LOCK_GLOBAL_PACHNER_POTENTIAL_V1.md`;
- `DDD_LOCK_GLOBAL_PACHNER_POTENTIAL_V1.md`;
- `THREE_RECONNECTION_FIXED_ROUTE_REDUCTION_V1.md`;
- the loop/parallel-edge conventions of the cubic multigraph category.

**Status:** exact bounded-terminal disposition. A zero-vertex cubic four-pole is one perfect matching of its four terminals. Closing it by one two-vertex cubic cap produces exactly one of two closed cubic multigraphs. If the matching equals the cap-block matching, the closure is two loops joined by one bridge and is outside the bridgeless category. If the matching is one of the two cross matchings, the closure is the two-vertex theta multigraph with three parallel edges and has an explicit three-support root flow. Hence the zero-vertex terminal of an equality or DDD Pachner descent is never a counterexample.

**Not implied:** transfer through a nonterminal surgery history, automatic preservation of an outer route during recursive returns, global proof-DAG closure, canonical acceptance, Lean verification, manuscript integration, release, publication, or the global five-support theorem.

---

## 1. Ordered cap

Let the four ordered terminal incidences be

\[
1,2,3,4.
\]

The two-vertex cap has vertices `x,y`, central edge `xy`, and cap blocks

\[
\boxed{M_i=12\mid34,}
\]

meaning that terminals `1,2` attach to `x` and terminals `3,4` attach to `y`.

The two cross matchings are

\[
M_j=13\mid24,
\qquad
M_k=14\mid23.
\]

A zero-vertex four-pole consists of two ordinary edges joining the terminal pairs of one matching

\[
M\in\{M_i,M_j,M_k\}.
\]

Close it by the cap.

---

## 2. Same matching gives a bridge

Assume

\[
M=M_i=12\mid34.
\]

The edge joining terminals `1,2` becomes a loop at `x`. The edge joining `3,4` becomes a loop at `y`. The cap central edge remains the single nonloop edge joining `x` and `y`.

### Theorem 2.1 — same-matching closure

The closure is exactly:

\[
\boxed{
\text{one loop at }x
+
\text{one loop at }y
+
\text{the edge }xy.}
\]

The edge `xy` is a bridge. Therefore this closure is not a connected bridgeless cubic counterexample.

It enters the established singleton-cut / loop-deletion-and-reinsertion branch.

---

## 3. Cross matching gives the theta multigraph

Assume

\[
M=M_j
\]

or

\[
M=M_k.
\]

Each of the two matching edges joins one terminal at `x` to one terminal at `y`. Together with the cap central edge, all three ordinary edges join the same two vertices.

### Theorem 3.1 — cross-matching closure

The closure is the cubic theta multigraph

\[
\Theta_3
\]

with two vertices and three parallel edges.

It is connected and bridgeless.

### Theorem 3.2 — explicit root flow

Choose any support triangle, for example

\[
12,
\qquad
13,
\qquad
23.
\]

Assign these three distinct roots to the three parallel edges. At both vertices

\[
12+13+23=0.
\]

Hence

\[
\boxed{
\Theta_3\text{ has a root-valued }E_5\text{ flow}.}
\]

Indeed it already has a three-support cycle double cover.

---

## 4. Complete bounded-terminal theorem

### Theorem 4.1

Let a root-surgery reduction of an equality or DDD four-pole terminate with no source vertices, so the remaining four-pole is one direct terminal matching `M`. Closing by the original two-vertex cap gives exactly one of:

1. `M` is the cap-block matching: a bridge plus two loops, hence category/separator exit;
2. `M` is a cross matching: the explicitly root-soluble theta multigraph.

Thus

\[
\boxed{
\text{zero-vertex direct-pairing terminal}
\Longrightarrow
\text{category exit or immediate root solution}.}
\]

There is no third bounded graph and no residual terminal profile problem.

---

## 5. Equality and DDD interpretations

### Equality

All four current terminal roots may be equal, so every terminal matching is coefficient-compatible on the reduced side. The graph closure theorem above, not the current terminal coefficient word, decides the endpoint:

- same matching exposes the bridge;
- cross matching gives `Theta_3`, which may be recoloured by the explicit root triangle.

### DDD

For a fixed current word `p,p,q,q` with `p,q` disjoint, only the matching pairing equal values can be represented by two direct edges. Relative to the target co-root cap, this is a cross matching, so the closed source graph is `Theta_3`.

The current DDD word itself would force the central co-root; the theorem instead uses the complete closed graph and supplies a different root flow on the same theta multigraph. This is exactly the cover-independent terminal state needed by inverse transfer.

---

## 6. Trust boundary

### Exact here

- complete three-matching graph census;
- same-matching loop/bridge closure;
- cross-matching theta closure;
- explicit root flow on the theta multigraph;
- terminal consumption for equality and DDD current-flow reductions.

### Still open

- inverse transfer from the soluble theta terminal through an arbitrary surgery history;
- outer-route preservation after recursive first-failure resolution;
- complete local transfer synthesis;
- global proof-DAG assembly;
- canonical acceptance, independent audit, Lean verification, manuscript integration, release, publication, and the global five-support theorem.
