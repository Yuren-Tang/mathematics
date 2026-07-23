# First-failure normalization is automatically category-safe

## Research dossier v1 — final contextual category cleanup

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `4797184599604b4e8bc4949eb3b70402b9e4d5d6`.

**Parents:**

- `PACHNER_HISTORY_FIRST_FAILURE_ONE_EDGE_ATOM_V1.md`;
- `PACHNER_FIRST_FAILURE_CRITICAL_OVERLAP_V1.md`;
- `FULL_DEFECT_TREE_NNI_DESCENT_V1.md`;
- `ROOT_SURGERY_AUTOMATIC_CATEGORY_SAFETY_V1.md`;
- the immediate zero-atom alternative-root theorem.

**Status:** exact category theorem for the normalization moves used in contextual inverse transfer. A persistent co-root atom and every transient bad-overlap two-co-root tree carry a nowhere-zero `E_5` flow: every edge value is a root or a co-root. Every local NNI replacement remains connected, and a bridge in an `E_5` flow must carry zero. Hence all co-root relocation and normalization moves are automatically bridgeless. A zero atom is never transported as a persistent state: its `(0,2,2)` triality has an immediate root-valued alternative, which returns the process to the nowhere-zero root layer. Therefore first-failure critical overlap has no independent separator/category outcome. Its exact outcomes are root commutation, one normalized co-root atom, route/profile terminal, or strict cancellation descent.

**Assurance boundary:** the theorem assumes the exact first-failure and critical-overlap local tables. It does not apply to an arbitrary zero-valued defect tree before the immediate root alternative is selected.

---

## 1. Structural connectivity of local NNI replacement

Let a connected bridgeless cubic graph contain two adjacent vertices. Remove them and retain the four exterior incidences. As in `ROOT_SURGERY_AUTOMATIC_CATEGORY_SAFETY_V1.md`, every component of the exterior graph contains at least two terminal incidences. Hence there are one or two exterior components.

Every two-vertex NNI topology reconnects the four terminals through two new cubic vertices joined by one central edge. Therefore every NNI output is connected, independently of its coefficient labels.

### Lemma 1.1

A local NNI performed in a connected bridgeless cubic graph always produces a connected cubic multigraph. The only possible source-category failure is a bridge, not disconnection.

---

## 2. Nowhere-zero defect states

An `E_5` flow may contain roots, co-roots, or zero values. Roots and co-roots are all nonzero.

The bridge-zero law says:

\[
\boxed{
 e\text{ bridge}
\Longrightarrow
\lambda(e)=0.}
\]

Therefore:

### Lemma 2.1 — nonzero defect flows are bridgeless

A connected cubic graph carrying an `E_5` flow whose values are all roots or co-roots is bridgeless.

This applies even though the flow is not yet root-valued.

---

## 3. Persistent co-root atom

A persistent same-order first-failure atom has one co-root central edge and roots everywhere else. Its flow is nowhere zero.

A good critical overlap either commutes the atom past a root Pachner move or relocates it to one new co-root edge. The resulting graph is connected by Lemma 1.1 and its flow remains nowhere zero.

### Theorem 3.1 — co-root relocation safety

Every one-atom co-root relocation in the contextual state graph produces another connected bridgeless cubic graph.

No separate category test is required.

---

## 4. Bad overlap and the transient two-defect tree

In the unique bad overlap, an old co-root atom `Q_i` and an adjacent root Pachner move produce one neighbouring co-root `Q_j`. Before normalization the local defect support is the three-vertex full-defect tree

\[
Q_i - Q_j
\]

with the transport root `ij` and root-valued outer leaves.

Every edge value in the complete graph is still nonzero: the only non-root values are `Q_i,Q_j`.

The full-defect local table chooses one NNI whose new central value is a root and leaves at most one co-root atom.

### Theorem 4.1 — bad-overlap normalization safety

The transient two-co-root graph and its normalized one-co-root output are connected and bridgeless.

### Proof

Connectivity of the NNI output is Lemma 1.1. Before and after normalization every edge value is a root or co-root, hence nonzero. Lemma 2.1 excludes bridges. ∎

Thus the older alternative “normalization or a separator/category exit” is redundant for the actual bad-overlap coefficient table.

---

## 5. Zero atoms are removed before transport

Suppose a first failed inverse `2--2` move produces a zero central edge. Its four-root pairing-sum pattern is `(0,2,2)`: the two other local topologies are root-valued.

Choose the alternative root topology immediately. The replacement:

1. removes the zero edge;
2. changes no exterior root value;
3. creates no second defect;
4. returns the graph to a root-valued nowhere-zero flow.

By `ROOT_SURGERY_AUTOMATIC_CATEGORY_SAFETY_V1.md`, that root NNI is connected and bridgeless.

### Theorem 5.1 — no persistent zero state

A zero atom never enters the persistent same-order relocation graph. It is consumed immediately by one category-safe root resolution.

The quadruple-equality inverse-cancellation branch belongs to the strict-order layer rather than a pure same-order flip block.

---

## 6. Corrected critical-overlap outcome

For contextual inverse transfer, the exact local outcome list is now:

1. **disjoint/root commutation:** the history moves commute root-valuedly;
2. **good co-root overlap:** one atom relocates category-safely;
3. **bad co-root overlap:** one transient two-co-root tree normalizes category-safely to one atom;
4. **zero overlap:** immediate category-safe rootification;
5. **route/profile event:** produce a cap-compatible terminal;
6. **inverse cancellation:** enter strict target-order descent.

There is no seventh separator/category outcome inside first-failure normalization.

Small-cut and bounded-category theorems remain necessary in the global graph-reconnection and initial minimal-counterexample layers, but not in the internal contextual move alphabet.

---

## 7. Consequence for the no-sink argument

After this correction, every edge of the same-order contextual state graph is one of:

- a legal root Pachner move;
- a legal co-root atom relocation;
- immediate zero removal;
- a route/profile terminal edge;
- a direct-pairing terminal edge;
- or an edge leaving to strict cancellation order.

All nonterminal same-order moves preserve connected bridgelessness automatically.

Thus the no-sink proof needs no category-return bookkeeping:

- odd Petersen cycles cannot close;
- even Petersen cycles force strict cancellation;
- a route event is handled as a cap-compatible terminal;
- direct matching is bounded;
- every other recurrence is impossible.

---

## 8. Trust boundary

### Exact here

- connectivity of every local NNI output;
- bridge exclusion for root/co-root nowhere-zero `E_5` flows;
- category safety of persistent co-root relocation;
- category safety of transient two-co-root normalization;
- immediate rootification and category safety of zero atoms;
- deletion of the separator/category branch from contextual critical-overlap normalization.

### Not claimed

- automatic category safety of an arbitrary flow containing a persistent zero edge;
- downstream proof development, curation, Lean verification, manuscript integration, release, or publication.
