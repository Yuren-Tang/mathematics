# Direct single-defect augmentation — exact boundary and genuine bypass targets

## Research Lead mechanism audit v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `a48f554ff6084fdb3299aca3ead9a0080fad7a82`.

**Purpose:** determine whether the current cover-independent surgery-history theorem can be replaced by the informal argument “choose a defect-minimal flow and eliminate its single defect”.

**Status:** exact scope diagnosis. The existing defect-minimality and local-NNI theorems do not by themselves imply a root flow on the original source graph. A genuine history-free bypass would require one of two new theorems identified below.

---

## 1. The tempting shortcut

Restoring one deleted cubic edge from a root-valued cross reduction produces an `E_5` flow on the original graph with at most one non-root edge:

\[
0
\qquad\text{or}\qquad
Q_i.
\]

The full-defect-tree theorem proves that every defect component with at least three vertices admits a defect-lowering NNI. First-failure localisation is stronger still: the restoration problem already begins at the one-edge normal form.

It is therefore tempting to argue:

> choose a defect-minimal flow; perform a root-valued NNI that removes the remaining defect; conclude that the original graph is root-soluble.

The last implication is invalid.

---

## 2. Topology-change obstruction

A root NNI replaces one source pairing of four exterior incidences by the opposite root-valued pairing. It changes the source graph:

\[
G\longmapsto G'.
\]

The inherited flow may be root-valued on `G'`, but the desired theorem concerns `G`.

### Proposition 2.1 — local defect removal is not fixed-graph repair

Let a one-edge zero/co-root defect in `G` admit a root-valued alternative NNI. Then the NNI proves root-solubility of the modified local topology `G'`; it does not supply a root-valued flow on the original topology `G`.

To return an arbitrary root flow on `G'` through the inverse NNI, the old central value is again one of:

\[
\text{root},\qquad 0,\qquad Q_i.
\]

Hence inverse return may recreate exactly one defect edge.

### Consequence 2.2

The implication

\[
\delta(G')=0
\Longrightarrow
\delta(G)=0
\]

is precisely the missing contextual-transfer statement; it cannot be assumed as part of defect minimality.

This explains why the secondary defect-minimality theorem stops at the one-edge normal form rather than completing the original graph.

---

## 3. Defect-minimality has already reached its ceiling

First-failure localisation gives exactly one defect edge before any large defect network forms. The full-defect-tree theorem gives the same normal form after arbitrary forest descent.

Thus applying the large-defect theorem to the current one-cross proof adds no new order decrease:

\[
\boxed{
\text{first-failure atom}
=
\text{final defect-minimal normal form}.}
\]

A further appeal to “minimise the number of defects” is circular unless accompanied by an invariant that compares the original and NNI-modified source topologies.

---

## 4. Ordinary Kempe augmentation is also insufficient

For an equality defect, every relevant repair root belongs to the six-channel `K_{2,3}` system. For a DDD defect, the relevant roots form the four-channel `K_{2,2}` system.

If one channel separates the two marked cross edges, one component switch repairs the cap. The residual case is exactly the oriented full-channel lock:

- both marked edges lie in one component of every repair system;
- every such component cuts open with the original cap route;
- switching a locked component remains inside the corresponding outer route sector.

### Proposition 4.1 — no one-switch bypass in a full lock

A residual oriented equality or DDD lock is, by definition, closed under every single relevant component augmentation that remains root-admissible. Therefore ordinary one-component Kempe rescue cannot be promoted into a universal direct theorem.

A history-free proof would need either a genuinely global simultaneous switch or a theorem selecting a different root-flow orbit.

---

## 5. The two genuine bypass targets

There are exactly two conceptually different ways to remove the contextual-history package.

### Target F — fixed-topology simulation

Prove that every root-valued Pachner NNI used by the singular Morse descent has a simulation on the **original** four-pole by a finite sequence of root-admissible support transformations, preserving the ordered exterior cap context.

Schematically:

\[
\text{root NNI on }G'
\quad\rightsquigarrow\quad
\text{root-flow transformation on fixed }G.
\]

Such a theorem would turn graph-changing descent into an ordinary augmentation algorithm and would make inverse transfer unnecessary.

No current dossier proves this. Ptolemy history comparison proves contextual return through graph-changing moves; it is not a fixed-graph simulation theorem.

### Target O — orbit selection

Weaken the extension theorem from

\[
\text{every root flow on the selected cross reduction extends}
\]

to the existential statement actually needed by induction:

\[
\boxed{
\text{some root flow on some valid cross reduction extends}.}
\]

A direct proof would have to show that the root-flow space of the smaller cross closure contains a boundary state in the original cap profile, or at least an orbit escaping the equality/DDD outer lock.

Possible forms include:

1. a counting or parity identity among boundary-state partition functions;
2. a global Kempe-orbit transitivity theorem;
3. a two-cross comparison theorem forcing one intersecting-root boundary state;
4. a positivity theorem for a four-terminal tensor/connection matrix.

No present finite profile theorem implies this: the abstract boundary algebra permits the equality outer path and the DDD outer path as closed fixed-route sectors.

---

## 6. What would constitute a real simplification

The following statements would be genuine proof shortening:

\[
\boxed{
\text{fixed-topology root-NNI simulation}
}
\]

or

\[
\boxed{
\text{existence of an extendable cross-flow orbit}.}
\]

By contrast, the following are only restatements of the current obligation:

- minimise defect count;
- choose a lowering NNI;
- solve the NNI-modified graph;
- say that the solution “returns” to the original graph.

The fourth step is the contextual-confluence theorem itself.

---

## 7. Safe architectural simplification still available

Although the history cannot presently be removed mathematically, its well-founded bookkeeping can be compressed.

For one fixed finite forward history and one target order, form the complete finite contextual state graph containing:

- all history prefixes;
- root states;
- one-token first-failure states;
- physical route and distinguished-block data;
- successful inverse edges;
- token relocation edges;
- cap terminals and cancellation exits.

If every sink strongly connected component has a terminal or strict-order exit, the condensation graph supplies a canonical finite rank. One then needs induction only on target order, not an additional hand-written induction on history length.

This is an expository and proof-DAG simplification that does not assume a nonexistent fixed-graph repair.

---

## 8. Research conclusion

### Controlling conclusion

The one-cross candidate cannot currently discard singular contextual confluence by citing defect minimality alone.

### Exact remaining choice

1. retain confluence, but package it by the finite sink-SCC principle; or
2. discover and prove Target F or Target O.

Until one of those new theorems exists, cover-independent contextual return remains a genuinely load-bearing part of R2.

---

## 9. Assurance boundary

### Established as a scope diagnosis

- local defect removal changes source topology;
- inverse NNI may recreate one defect;
- defect-tree minimality already terminates at the present one-edge frontier;
- one-component Kempe rescue is exhausted by the definition of a full lock;
- fixed-topology simulation and orbit selection are the two genuine bypass targets.

### Not claimed

- impossibility of every future direct augmentation theorem;
- nonexistence of a counting/partition-function proof of Target O;
- independent verification of the current confluence package;
- PDL acceptance, Lean verification, manuscript integration, release, peer review, publication, or established truth of five-CDC.
