# Every simple cubic edge is five-support reducible

## Research Lead headline mechanism v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `95c2fafef5fb0ceb531dcbe98dbdc31023e25dbe`.

**Parents:**

- `ONE_CROSS_RECONNECTION_EXISTENCE_V1.md`;
- `ONE_CROSS_CAP_RESTORATION_THEOREM_V1.md`;
- `SINGULAR_ROOT_TRIALITY_CONFLUENCE_MASTER_THEOREM_V2.md`.

**Purpose:** state the complete cubic proof as one local reducibility theorem plus the theta base. This is the natural headline architecture for proof development and exposition.

**Status:** compressed authorial theorem conditional on the concrete cap-restoration/confluence package. It adds no independent assurance.

---

## 1. Reduction at one simple edge

Let `G` be a finite connected loopless bridgeless cubic multigraph and let

\[
e=uv
\]

be a simple edge.

Delete `u,v`. The four remaining incidences admit two cross pairings. Let the corresponding cross closures be

\[
G_	imes^{(1)},
\qquad
G_	imes^{(2)}.
\]

### Structural half

At least one cross closure, denoted `G/e`, is:

- connected;
- loopless;
- bridgeless;
- cubic;
- smaller by exactly two vertices.

Thus

\[
|V(G/e)|=|V(G)|-2.
\]

The notation `G/e` denotes a selected cross reduction, not ordinary graph contraction.

---

## 2. Extension across the deleted edge

### Extension half

Assume `G/e` has a root-valued `E_5` flow. Then `G` has a root-valued `E_5` flow.

The extension mechanism is:

1. inspect the two root values on the cross edges;
2. if they intersect, restore `u,v,e` immediately;
3. if they are equal or disjoint, obtain one zero/co-root singular insertion;
4. the blocked-cap route rows orient the unique surviving repair lock;
5. a positive singular-carrier Morse function gives finite forward reduction;
6. singular contextual confluence returns a cap-compatible terminal;
7. restore `u,v,e` root-valuedly.

The root flow on `G/e` is arbitrary. The extension theorem does not require choosing a reduction-compatible cover in advance.

---

## 3. Simple-edge reducibility theorem

### Theorem 3.1

For every simple edge `e` of a finite connected loopless bridgeless cubic multigraph `G`, there exists a cross reduction `G/e` satisfying:

\[
\boxed{
G/e\text{ root-soluble}
\Longrightarrow
G\text{ root-soluble}.
}
\]

Moreover `G/e` is a connected loopless bridgeless cubic multigraph with two fewer vertices.

Thus every simple edge is reducible for the five-support property.

---

## 4. The unique irreducible base shape

### Lemma 4.1

A connected loopless cubic multigraph with no simple edge is the two-vertex theta multigraph with three parallel edges.

### Proof

At any vertex, if its three incident edges do not include a simple edge, all neighbours must be joined with multiplicity at least two. Cubic degree then permits only one neighbour joined by three parallel edges. Connectedness gives the theta graph. ∎

Theta has the explicit root flow

\[
12,13,23.
\]

---

## 5. Cubic theorem as pure induction

### Theorem 5.1 — recursive cubic closure

Every finite connected loopless bridgeless cubic multigraph has a root-valued `E_5` flow.

### Proof

Induct on vertex number.

- The no-simple-edge case is theta and is explicit.
- Otherwise choose any simple edge `e`.
- Theorem 3.1 supplies a smaller connected loopless bridgeless cubic cross reduction `G/e`.
- By induction `G/e` has a root flow.
- The extension half of Theorem 3.1 gives a root flow on `G`.

∎

No preliminary edge-connectivity normal form is required.

---

## 6. Recursive construction viewpoint

The proof is not merely a contradiction architecture. Subject to effective finite certificates for the local tables and confluence moves, it describes a recursive construction:

1. if the graph is theta, output the root triangle;
2. choose a simple edge;
3. test the two cross closures and select a valid one;
4. recurse on the smaller closure;
5. restore the edge using the singular-cap algorithm.

The recursion depth is at most

\[
|V(G)|/2-1.
\]

The restoration phase may require finite local surgery search; no polynomial complexity claim is made.

---

## 7. Conceptual meaning

The five-support theorem becomes analogous to a reducibility theorem in colouring theory:

- graph structure guarantees a smaller admissible reduction;
- finite boundary algebra classifies failure of naive extension;
- singular confluence proves every apparent extension obstruction is removable.

The hard theorem is not global existence in one step. It is:

\[
\boxed{
\text{root flows extend across every simple-edge cross reduction}.}
\]

Petersen and Ptolemy structures belong entirely to the proof of this extension property.

---

## 8. Preferred exposition order

A future proof should be organised as:

1. root-flow formulation;
2. structural cross-reduction lemma;
3. simple-edge extension theorem;
4. theta base and induction;
5. general-graph outer shell.

Inside the extension theorem:

1. root triality;
2. six blocked route rows;
3. singular carrier Morse descent;
4. one-token confluence;
5. odd-orientation exclusion and even source movie.

This order reveals the theorem before its technical proof.

---

## 9. PDL and audit focus

The complete cubic candidate now has two load-bearing local propositions.

### R1 — structural reducibility

One cross reduction at a simple edge stays in the bridgeless cubic category.

### R2 — flow extension

Every root flow on that reduction extends to the original graph.

An independent failure of either R1 or R2 destroys the compressed proof. Every other main-line statement is a lemma supporting these two propositions or the final outer shell.

---

## 10. Trust boundary

### Exact authorial synthesis

- the cubic candidate is equivalent to universal simple-edge reducibility plus the theta base;
- the prior minimal-counterexample architecture can be expressed as direct induction;
- the full technical corpus is localised inside the edge-extension theorem.

### Not claimed

- PDL reconstruction of R1 or R2;
- algorithmic efficiency;
- canonical acceptance, Lean verification, manuscript integration, release, peer review, publication, or established truth of 5-CDC.
