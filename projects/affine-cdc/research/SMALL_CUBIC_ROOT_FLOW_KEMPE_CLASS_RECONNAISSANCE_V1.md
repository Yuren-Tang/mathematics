# Small-cubic root-flow Kempe-class reconnaissance

## Research Lead finite reconnaissance v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Parent frontier:** cancellation re-entry and history-coherent terminal selection.

**Status:** exact finite counterevidence to the proposed shortcut that any terminal root flow can be transformed to the history-inherited root flow by componentwise support-Kempe switches. The full labelled root-flow Kempe graph is disconnected already for `K_4`, the triangular prism, and `K_{3,3}`. Among all connected simple cubic graph classes of orders `4,6,8`, only the cube has a connected root-flow Kempe graph.

This is computational reconnaissance. It does not classify Kempe components in general.

---

## 1. Componentwise support switches

Write a root flow as five even subgraphs

\[
F_1,\ldots,F_5
\]

such that every source edge belongs to exactly two `F_i`.

For support indices `a,b`, the symmetric difference

\[
F_a\triangle F_b
\]

is an even subgraph and hence a disjoint union of cycle components. On one connected component `C`, interchange the two support coordinates:

\[
F_a\mapsto F_a\triangle C,
\qquad
F_b\mapsto F_b\triangle C.
\]

This is the physical support-Kempe switch on `C`. It preserves the root condition on every edge and the flow equation at every vertex.

Define the **labelled root-flow Kempe graph**:

- vertices are all root-valued `E_5` flows with support coordinates `1,...,5` retained;
- edges are single componentwise support-Kempe switches.

Global `S_5` support permutations lie inside Kempe components, since a global transposition is the product of the switches on all components of `F_a triangle F_b`.

---

## 2. Exact enumeration method

For each connected simple cubic graph of orders `4,6,8`:

1. compute its binary cycle space;
2. enumerate all ordered five-tuples of cycle-space vectors in which every graph edge occurs exactly twice;
3. retain support-coordinate labels, so no `S_5` quotient is taken;
4. generate every componentwise support switch;
5. compute the connected components of the resulting finite graph.

The graph census contains exactly

\[
1,2,5
\]

isomorphism classes in orders `4,6,8`.

---

## 3. Complete small-order census

| graph class | labelled root flows | Kempe-component sizes |
|---|---:|---|
| `K_4` | 180 | `120, 60` |
| triangular prism | 540 | `240, 120, 120, 60` |
| `K_{3,3}` | 840 | `120,120,120,120,120,120,60,60` |
| order-8 class of edge-connectivity 2 | 3240 | `1440,720,720,360` |
| cube | 3960 | `3960` |
| order-8 triangle-free nonbipartite class | 3300 | `1440,1380,120,120,120,120` |
| order-8 class with two triangles | 1620 | `480,240,240,240,120,120,120,60` |
| order-8 class with one triangle | 2520 | `240` six times, `120` eight times, `60` twice |

Thus seven of the eight graph classes have more than one Kempe class.

---

## 4. Minimal obstruction on `K_4`

The two Kempe components on `K_4` admit a simple support-cycle description.

For one component of size `120`, the multiset of sizes of the five support even subgraphs is

\[
\boxed{(0,3,3,3,3).}
\]

For the other component of size `60`, it is

\[
\boxed{(0,0,4,4,4).}
\]

Every componentwise support switch on `K_4` stays inside the corresponding class.

This proves directly that not all root flows on the same three-edge-connected cubic graph are Kempe equivalent.

---

## 5. Consequence for history-coherent terminal selection

Let

\[
\rho_{\mathrm{inh}}
\]

be the root flow inherited from the forward surgery history at a descendant graph, and let

\[
\rho_{\mathrm{term}}
\]

be an arbitrary cap-compatible terminal flow on the same graph.

The tempting shortcut was:

\[
\rho_{\mathrm{term}}
\xrightarrow{\text{support-Kempe switches}}
\rho_{\mathrm{inh}},
\]

followed by exact reversal of the constructing history.

The finite census shows that the first arrow need not exist. The two flows may lie in distinct Kempe components even before any cap-boundary or route constraint is imposed.

Therefore componentwise Kempe connectivity cannot replace contextual inverse transfer.

---

## 6. Stronger relative versions are not rescued automatically

The negative result concerns unrestricted closed-graph Kempe connectivity. A relative version preserving:

- one cap-compatible terminal condition;
- an outer ordered boundary;
- a marked weld pair;
- or a distinguished physical route

is strictly stronger and cannot follow from general connectivity.

The cube's connected Kempe graph is an exceptional positive datum, not evidence for the universal theorem.

---

## 7. Strategic disposition

### Quarantined

- universal Kempe connectivity of root flows;
- transformation of an arbitrary terminal flow to the inherited flow by support switches;
- using global `S_5` symmetry as if it implied local Kempe equivalence.

### Retained

- individual support-Kempe switch formulas;
- exact horizontal rescue when a suitable separating component exists;
- route-table consequences of a physically realised switch;
- finite Kempe-class data as a possible invariant source.

### Preferred next direction

The remaining repair should use the actual Ptolemy history and defect-track geometry. In particular, the relative `C6/C8` source movies may yield a root-valued annular replacement and a diagrammatic rank, without requiring different root flows on one fixed graph to be Kempe equivalent.

---

## 8. Assurance boundary

### Exact here

- complete labelled root-flow enumeration for every connected simple cubic graph class of orders `4,6,8`;
- complete componentwise support-Kempe graph in that range;
- explicit disconnectedness on seven of the eight classes;
- exact two-component support-size invariant on `K_4`;
- invalidity of the universal terminal-to-inherited Kempe shortcut.

### Not proved

- a general invariant classifying Kempe components;
- root-annulus replacement;
- diagrammatic termination;
- repaired contextual transfer;
- one-cross cap restoration or the global five-support theorem;
- independent audit, Lean verification, manuscript integration, release, arXiv, DOI, peer review, or publication.
