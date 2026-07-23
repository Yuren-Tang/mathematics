# Nowhere-zero root surgeries are automatically category-safe

## Research dossier v1 — global source-category simplification

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `25469bd63857ecb7aeb15b9d22b11d61fe8df06e`.

**Parents:**

- `ROOT_FLOW_TRIANGLE_COMPLEX_PACHNER_V1.md`;
- `EQUALITY_LOCK_GLOBAL_PACHNER_POTENTIAL_V1.md`;
- `DDD_LOCK_GLOBAL_PACHNER_POTENTIAL_V1.md`;
- `PETERSEN_C6_AUTOMATIC_CATEGORY_SAFETY_V1.md`;
- the standard cut-sum law for group-valued flows.

**Status:** exact category theorem for the two root-surgery moves used throughout the equality/DDD programme. On a finite connected cubic multigraph carrying a nowhere-zero `E_5` flow, every root-valued `2--2` Pachner NNI produces another connected bridgeless cubic multigraph. Every equal-face `2--0` cancellation produces a finite loopless cubic graph with two fewer vertices, possibly disconnected, and every connected component is bridgeless and inherits a nowhere-zero root flow. Therefore neither root move has a residual bridge/loop/category-failure branch. Root NNI is a same-order internal move; equal-face cancellation is unconditional strict componentwise descent.

**Assurance boundary:** the theorem applies only when the output labels are already proved root-valued. It does not make a zero/co-root triality branch category-safe, nor does it justify an arbitrary coefficient replacement before rootification.

---

## 1. Bridges in group-valued flows

Let `A` be an abelian group and let

\[
x:E(G)\to A
\]

satisfy Kirchhoff conservation at every vertex, with the usual unoriented characteristic-two convention in the present application.

### Lemma 1.1 — bridge-zero law

If `e` is a bridge of `G`, then

\[
\boxed{x(e)=0.}
\]

### Proof

Remove `e` and sum the vertex equations over one shore. Every internal edge of that shore occurs twice and cancels. The only remaining boundary term is `x(e)`, so it is zero. ∎

### Corollary 1.2 — nowhere-zero flows exclude bridges

A graph carrying a flow whose value on every edge is nonzero is componentwise bridgeless.

For a root-valued `E_5` flow, every edge value lies in

\[
R_5
\]

and is nonzero. Hence every connected component is bridgeless automatically.

---

## 2. Connectivity after deleting one adjacent pair

Let `G` be connected and bridgeless, and let adjacent cubic vertices `u,v` be removed. Retain their four noncentral incidences as labelled terminals. Let

\[
H=G-\{u,v\}.
\]

Every connected component of `H` contains at least two terminal incidences. A component with exactly one terminal incidence would be joined to the rest of `G` by one edge and would make that edge a bridge.

Since there are four terminals, `H` has either:

1. one terminal-bearing component; or
2. two components, each carrying exactly two terminals.

There is no component with no terminal incidence, because `G` was connected and every connection from such a component to `{u,v}` would itself be recorded as a terminal.

---

## 3. Root-valued `2--2` NNI

A `2--2` NNI replaces the two removed vertices by two new cubic vertices joined by one central edge and distributes the same four terminal incidences two to each new vertex.

Assume the four terminal roots and the new central value make both new cubic equations root-valued.

### Theorem 3.1 — connectivity of every NNI replacement

The NNI output graph is connected.

### Proof

If `H` is connected, attaching both new vertices and their central edge clearly preserves connectedness.

If `H` has two components with two terminals each, then either:

- each new vertex receives terminals from one exterior component, in which case the new central edge joins the two components; or
- a new vertex receives terminals from both exterior components, in which case that vertex itself joins them.

Thus every terminal pairing gives a connected graph. ∎

### Theorem 3.2 — automatic bridgelessness of root NNI

Every root-valued NNI output is a connected bridgeless cubic multigraph.

### Proof

The output is connected and cubic by construction. Every old or new edge carries a root and hence a nonzero `E_5` value. Lemma 1.1 excludes every bridge. ∎

### Corollary 3.3

The category alternatives previously attached to a **root-valued** Pachner NNI are redundant. Once root-valuedness of the selected NNI is established, no separate bridge, small-cut, loop, or acyclic-output check is required.

Parallel edges may occur and remain within the multigraph category.

---

## 4. Equal-face `2--0` cancellation

Suppose adjacent vertices carry the same support triangle and are joined along one root. The two remaining pairs of equal-labelled incidences are reconnected and the two vertices are removed.

The standard equal-face theorem gives a root-valued flow on the output and removes exactly two vertices.

### Lemma 4.1 — no loop can occur

An equal-face cancellation of a root-valued cubic flow cannot create a loop.

### Proof

A loop could arise only if the two exterior incidences to be reconnected have the same outside endpoint `w`. After reconnection, `w` would be a cubic vertex incident with the new loop and one remaining nonloop edge `h`.

In the unoriented flow equation, the loop contributes twice and hence contributes zero. Conservation at `w` would force

\[
x(h)=0,
\]

contradicting that `h` carries a root. ∎

### Theorem 4.2 — componentwise bridgeless strict descent

The equal-face cancellation output is a finite loopless cubic graph with exactly two fewer vertices. It may be connected or disconnected, but every connected component is bridgeless and carries the restricted nowhere-zero root flow.

### Proof

Cubicity and the root-valued flow are preserved by the cancellation theorem. Lemma 4.1 excludes loops. Every edge value is nonzero, so Lemma 1.1 excludes bridges in every component. ∎

### Component interpretation

If the output is disconnected, each component is already root-solved. In a cap-context problem, only the component carrying the distinguished outer cap data remains relevant to contextual induction; all other components may be retained with their inherited root flows.

The total source-vertex count decreases by exactly two in all cases.

---

## 5. Consequence for equality and DDD potentials

The full-ten-triangle equality and DDD potential theorems select only:

1. a root-valued Pachner NNI; or
2. an equal-face cancellation.

By Sections 3--4:

- a selected root NNI is always a legal same-order move in the connected bridgeless cubic category;
- a selected cancellation always gives strict componentwise target-order descent.

Therefore their forward move alphabet has no independent category-failure outcome.

### Theorem 5.1 — corrected forward descent alternative

At every nonempty equality or DDD carrier, exactly one of:

1. a route/profile event is deliberately detected and used as a cap-compatible terminal;
2. a root-valued NNI strictly lowers the relevant same-order potential;
3. an equal-face cancellation lowers total target order by two.

There is no fourth source-category alternative after root-valuedness is established.

For DDD, combine this theorem with `DDD_BOUNDED_RESIDUAL_ELIMINATION_V1.md`: no positive-vertex bounded terminal remains.

---

## 6. Consequence for contextual transfer

The repaired contextual-transfer proof may remove generic “separator/category exit” clauses from the part of the state graph generated solely by root-valued NNI and equal-face cancellation.

Category analysis remains necessary only before root-valuedness is known, for example:

- a coefficient/defect-tree replacement whose chosen central values may still be zero or co-roots;
- a graph-inductive reconnection constructed without an inherited root flow;
- a bounded non-root triality branch.

It is not needed for:

- root Pachner scheduling;
- the relative Petersen `C6` star movie;
- equality/DDD potential descent after the selected root move is identified.

### Corollary 6.1 — clean contextual measure

Within the root-valued surgery layer, the only nonterminal measures are:

\[
\boxed{
\text{same-order equality/DDD potential}
}
\]

and

\[
\boxed{
\text{strict vertex order after cancellation}.}
\]

No category-return measure is required.

---

## 7. Correction of older wording

Read any older sentence of the form

> a root Pachner flip or equal-face cancellation either stays in the category or exposes a separator/category exit

as the following sharper statement:

- if the move is only a proposed coefficient topology and has not yet been proved root-valued, retain the old category-safe alternative;
- once the move is root-valued, NNI is automatically connected and bridgeless, while cancellation is automatically componentwise bridgeless and strictly smaller.

This distinction prevents unnecessary descendant-to-original category-return obligations in the final full-channel synthesis.

---

## 8. Trust boundary

### Exact here

- bridge-zero law;
- no-singleton exterior component after deleting two adjacent vertices;
- connectivity of every two-vertex NNI topology;
- automatic bridgelessness of every root-valued NNI;
- impossibility of loops after root equal-face cancellation;
- componentwise bridgelessness after cancellation;
- exact two-vertex descent;
- removal of the category branch from root-valued equality/DDD surgery.

### Not claimed

- category safety of a non-root coefficient replacement;
- automatic transfer across a zero/co-root topology;
- downstream proof development, curation, Lean verification, manuscript integration, release, or publication.
