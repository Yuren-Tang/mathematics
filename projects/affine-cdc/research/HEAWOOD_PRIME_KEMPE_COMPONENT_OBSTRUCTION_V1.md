# Heawood refutes Kempe-component two-edge flexibility even in the cyclically-six-edge-connected branch

## Research Lead exact prime obstruction dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `57c498a84c9180d7a67d46a1ff4e4f92257d4492`.

**Parents:**

- `INHERITED_TWO_EDGE_KEMPE_RECONFIGURATION_CERTIFICATE_V1.md`;
- `RELATIVE_WELD_FLOW_SELECTION_SMALL_GRAPH_OBSTRUCTIONS_V1.md`;
- `AC_PD_5CDC_EQ_RETURN_3_TWO_EDGE_CHANNEL_EVALUATION.md`;
- `AC_PD_5CDC_EQ_RETURN_4_TRIANGLE_CONTRACTION.md`.

**Status:** exact negative finite certificate. The Heawood graph is simple, bipartite, triangle-free, and has cyclic edge connectivity six, yet its labelled `R_5` root-flow Kempe graph has 298 connected components. Every pair of graph edges is globally attainable in the distinct-intersecting `B` orbit, but many nonadjacent pairs fail to meet `B` in a large fraction of Kempe components. Therefore the proposed prime theorem “every inherited root flow can reach a `B` pair by support-pair component switches after triangle and cyclic-small-cut reductions” is false. Any valid inherited-weld repair must use graph-changing root Pachner/equal-face moves, a stronger surface/source operation, or a source reduction which crosses Kempe components.

---

## 1. Exact model

Use the Heawood graph as the incidence graph of the Fano plane. It has

\[
|V|=14,
\qquad
|E|=21,
\qquad
\operatorname{girth}=6.
\]

A labelled root flow is a map

\[
\lambda:E(G)\to R_5
\]

whose incident edge roots sum to zero at every cubic vertex.

The Kempe graph `K(G)` has one vertex for every labelled root flow and one edge for every switch of one connected component of one channel

\[
F_a\triangle F_b.
\]

All data below were exhaustively generated from the exact local root constraint. No random sampling or quotient by support permutations was used.

---

## 2. Prime graph certificate

An exhaustive edge-cut search gives:

1. no cyclic edge cut of size at most five;
2. a cyclic edge cut of size six.

Hence

\[
\boxed{\lambda_c(G)=6}
\]

for cyclic edge connectivity.

Thus Heawood survives all triangle, cyclic-three-cut and cyclic-four-cut reductions contemplated by the current prime branch.

This is a finite graph certificate; no general theorem about incidence graphs is imported.

---

## 3. Root-flow and Kempe-component census

Exact root-flow enumeration gives

\[
\boxed{148320}
\]

labelled `R_5` root flows.

Their Kempe reconfiguration graph has

\[
\boxed{298}
\]

connected components, with size distribution

\[
\boxed{
8\times60
+
168\times120
+
56\times840
+
42\times960
+
24\times1680.
}
\]

The total is

\[
8\cdot60+168\cdot120+56\cdot840+42\cdot960+24\cdot1680
=148320.
\]

Therefore the inherited-flow state is highly component-sensitive even though the underlying graph is prime and highly symmetric.

---

## 4. Three edge-pair orbits

The line graph of Heawood has three distances between distinct graph edges. The 210 unordered edge pairs split as:

\[
\boxed{
42\text{ pairs at distance }1,
\quad
84\text{ at distance }2,
\quad
84\text{ at distance }3.
}
\]

Distance one means that the graph edges share a cubic vertex.

### Distance one

At a cubic root-flow vertex, the three incident roots form one root triangle. Hence every adjacent edge pair is distinct intersecting in every flow.

Exact component count:

\[
\boxed{298/298}
\]

Kempe components meet `B_(e,f)`.

### Distance two

For every one of the 84 distance-two edge pairs, exactly

\[
\boxed{193/298}
\]

Kempe components meet `B_(e,f)`.

Thus

\[
\boxed{105}
\]

components are trapped away from `B` for each such pair.

### Distance three

For every one of the 84 distance-three pairs, exactly

\[
\boxed{247/298}
\]

components meet `B_(e,f)`.

Thus

\[
\boxed{51}
\]

components are trapped away from `B` for each such pair.

Every pair is nevertheless globally `B`-attainable because the displayed component counts are positive.

---

## 5. Exact failure of the Kempe-only prime conjecture

Let `lambda` be an inherited Heawood root flow and `e,f` a distance-two marked pair. If `lambda` lies in one of the 105 trapped components, then no finite sequence of ordinary support-pair component switches changes the marked pair to distinct intersecting roots.

Likewise, distance-three pairs have 51 trapped components.

Therefore:

\[
\boxed{
G\text{ triangle-free and cyclically }5\text{-edge-connected}
\not\Rightarrow
\text{Kempe-component two-edge flexibility}.}
\]

Indeed the counterexample has cyclic edge connectivity six.

This refutes Target 8.1 of `INHERITED_TWO_EDGE_KEMPE_RECONFIGURATION_CERTIFICATE_V1.md` when “deformation” is restricted to ordinary support-pair component switches.

---

## 6. Relation sets inside trapped components

For nonadjacent marked pairs, Kempe components occur with relation sets including:

\[
\{A\},
\quad
\{C\},
\quad
\{A,B\},
\quad
\{B,C\},
\quad
\{A,B,C\}.
\]

Thus the obstruction is not one universal `A/C` parity invariant.

Some components are completely equality-locked, some completely disjoint-locked, and others permit one bad relation plus `B` without permitting the other. The relation type alone does not classify Kempe components.

The `F_2` span dimension of the five support cycles is also not constant in every component: some components contain both rank-three and rank-four support systems. Hence that coarse linear rank is not the missing invariant either.

The trapped classes retain finer cycle-decomposition, incidence or surface information.

---

## 7. Revised source frontier

The previous progression

\[
\text{triangle-free}
+
\text{no cyclic cut of size }\le4
\Longrightarrow
\text{Kempe flexibility}
\]

must be retired.

A valid repair must permit at least one operation which can cross the trapped Kempe components, such as:

1. a root-valued `2--2` Pachner flip changing the source graph;
2. an equal-face insertion/cancellation with a continuation-normalized rank;
3. a Tait/surface compression which preserves the required outer and weld boundaries;
4. a bounded source replacement whose complete boundary response is proved;
5. an explicitly enlarged mixed reconfiguration graph containing both Kempe and graph-changing moves.

The finite channel-evaluation theorem remains exact: a bad pair is Kempe-repairable precisely when one relevant channel separates the marks. Heawood proves that all relevant channels may remain locked throughout an entire prime Kempe component.

---

## 8. Corrected target

### Target 8.1 — mixed source-move two-edge flexibility

Let `G` be one prime connected cubic root-flow context, `lambda` an inherited root flow, and `e,f` two marked edge incidences. In the mixed state space generated by:

- support-pair component switches;
- category-safe root Pachner moves;
- equal-face moves with ordered-incidence genealogy;
- accepted route/profile and separator exits;

prove one of:

1. the marked pair reaches the `B` orbit;
2. the outer terminal is solved before `B` is needed;
3. a bounded or separator source reduction occurs;
4. one cancellation child is opened only after a strict continuation-normalized parent step.

The central new question is which graph-changing moves connect the trapped Heawood Kempe classes while preserving the full outer/weld context.

---

## 9. Immediate research tasks

1. Add root-valued `2--2` Pachner neighbours to the exact Heawood state census and determine whether the 298 Kempe components merge into marked-pair-flexible mixed components.
2. Identify a finite invariant of ordinary Kempe components and compute its change under one root Pachner flip.
3. Test whether a trapped marked pair forces a root-flippable edge in its causal carrier or one accepted surface compression.
4. Compare the trapped component classes with the equality/DDD Morse weights and Tait triangle-surface types.

This is now a more exact target than generic prime flow selection.

---

## 10. Trust boundary

### Exact here

- complete Heawood root-flow enumeration;
- complete Kempe-component size distribution;
- exact cyclic edge connectivity certificate;
- exact edge-pair distance orbit counts;
- exact number of components meeting `B` in every orbit;
- failure of inherited Kempe flexibility in a cyclically-six-edge-connected graph;
- insufficiency of relation type and support-span rank as complete component invariants.

### Finite/computational boundary

All graph-specific claims are exact exhaustive certificates. They do not prove a general obstruction theorem for every prime graph.

### Not proved

- mixed source-move two-edge flexibility;
- which invariant separates the Heawood Kempe classes;
- that one root Pachner move crosses every trapped class;
- continuation-normalized local rank;
- marked-weld return, cancellation macro-return, R2 global return or cap restoration;
- the global five-support theorem;
- independent audit, curation, Lean verification, manuscript integration, release, arXiv, DOI, peer review or publication.
