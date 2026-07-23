# Every one-NNI Heawood flow has an equal-face cancellation, and trapped marks can avoid it

## Research Lead exact mixed-exit dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `7587821f4c1a9f21aa49d9b87aba2f204362ca22`.

**Parents:**

- `HEAWOOD_PRIME_KEMPE_COMPONENT_OBSTRUCTION_V1.md`;
- `HEAWOOD_ONE_PACHNER_LAYER_MIXED_RECONFIGURATION_V1.md`;
- `WELD_MARK_EQUAL_FACE_OVERLAP_V1.md`;
- `AC_PD_5CDC_EQ_RETURN_5_NESTED_STACK_ORDER.md`.

**Status:** exact positive bounded mixed-source theorem. The common one-NNI Heawood topology `H'` admits `119280` labelled root flows, and every one of them contains at least two equal-face edges. Hence a root-valued NNI from Heawood never lands in a positive-vertex cancellation-free carrier. Moreover, for every Heawood flow trapped away from the marked `B` orbit in either nonadjacent edge-pair orbit, one may choose one of the two marked-edge NNIs so that the resulting `H'` flow has an equal-face edge distinct from both marked edge objects. Thus every Heawood inherited Kempe obstruction admits a continuation-normalized source path consisting of one root NNI followed by a mark-exterior strict cancellation. This is an exact bounded certificate, not a proof of the corresponding theorem for arbitrary prime graphs.

---

## 1. Equal-face criterion

A root flow assigns to every cubic vertex one support triangle

\[
T_v\in\binom{[5]}3,
\]

whose three two-subsets are the incident edge roots.

An edge `uv` is an **equal-face edge** when

\[
\boxed{T_u=T_v.}
\]

The two incident cubic vertices then carry identical root triangles and admit the legal equal-face `2--0` cancellation.

This criterion was evaluated directly from the complete root labels at every vertex of every `H'` flow.

---

## 2. Universal equal-face existence on `H'`

Recall that all forty-two one-NNI Heawood topologies are source-isomorphic to one graph `H'`, with

\[
|V(H')|=14,
\qquad
|E(H')|=21,
\qquad
\operatorname{girth}(H')=5,
\qquad
\lambda_c(H')=5.
\]

Exact enumeration gives `119280` labelled root flows.

### Theorem 2.1 — no equal-face-free root flow

Every root flow on `H'` contains at least two equal-face edges.

The complete equal-face edge-count distribution is

\[
\boxed{
\begin{array}{c|r}
\#\text{ equal-face edges}&\#\text{ root flows}\\
\hline
2&960\\
3&4320\\
4&11040\\
5&22080\\
6&26400\\
7&15840\\
8&5760\\
9&18720\\
11&5760\\
13&8160\\
21&240.
\end{array}}
\]

No flow has zero, one, ten, twelve, or any other omitted count.

In particular:

\[
\boxed{
\min_{\lambda}\#E_{\rm eq}(\lambda)=2.}
\]

### Consequence 2.2

Any root-valued NNI from a Heawood flow reaches a graph carrying an immediate equal-face cancellation. Therefore the one-NNI topology `H'` cannot be a positive-vertex terminal of a mixed Pachner/Kempe descent.

---

## 3. Mark-exterior cancellation target

Let `e,f` be the two marked graph-edge objects whose root relation must eventually return to `B`.

After a marked-edge NNI, the active marked central edge is transported to its opposite diagonal; the other marked edge remains the same edge object. Map the resulting labelled source state to the fixed `H'` representative as in the one-layer census.

Call an equal-face edge **mark-exterior** when it is neither of the two marked edge objects.

Cancellation at such an edge:

1. preserves both marked edge objects and their ordered incidences;
2. preserves their current root labels;
3. reduces source order by two;
4. enters the PDL nested-weld stack without consuming or duplicating either marked lineage.

---

## 4. Distance-two trapped orbit

For a Heawood line-graph-distance-two marked pair there are

\[
26160
\]

root flows trapped away from `B` in their original Kempe components.

For every one of these flows, at least one of the two choices

\[
\text{NNI at }e,
\qquad
\text{NNI at }f
\]

reaches an `H'` flow with a mark-exterior equal-face edge.

This holds for all four subfamilies:

\[
\boxed{
\begin{array}{c|cc}
&\text{one-layer }B\text{ repair}&\text{one-layer }B\text{ still trapped}\\
\hline
A&9600&3120\\
C&9600&3840.
\end{array}}
\]

Thus even the `6960` flows not repaired by one Pachner layer have a mark-preserving strict cancellation exit.

---

## 5. Distance-three trapped orbit

For a distance-three pair there are

\[
11880
\]

originally trapped flows.

Again, every flow admits a choice of marked-edge NNI whose `H'` output has a mark-exterior equal-face edge, including all states which remain outside `B` after arbitrary `H'` Kempe motion:

\[
\boxed{
\begin{array}{c|cc}
&\text{one-layer }B\text{ repair}&\text{one-layer }B\text{ still trapped}\\
\hline
A&1440&2280\\
C&7200&960.
\end{array}}
\]

Hence all `3240` one-layer survivors also possess the strict cancellation exit.

---

## 6. Continuation-normalized interpretation

For every trapped Heawood marked state, choose a marked-edge root NNI and then a mark-exterior equal-face edge in the output.

The source path is

\[
\boxed{
\text{trapped inherited state}
\longrightarrow
\text{root-valued NNI state on }H'
\longrightarrow
\text{strictly smaller cancellation child}.}
\]

The NNI is a genuine parent-context source move completed before the recursive cancellation is opened. The equal-face edge is exterior to the marked weld pair.

Thus this bounded instance has exactly the continuation shape required by the abstract PDL stack theorem:

1. consume one concrete parent source step;
2. store the post-NNI parent continuation;
3. push a child of order two less;
4. retain both ordered weld-mark lineages unchanged.

The theorem does not by itself supply a universal numerical local rank, but it proves that the Heawood prime Kempe obstruction is not a counterexample to continuation normalization.

---

## 7. Why this does not close global R2.7

The argument is graph-specific and finite.

It does not prove that for every prime trapped carrier:

- one root NNI reaches a topology with an equal-face edge;
- an equal-face edge can be chosen mark-exterior;
- the selected NNI lowers the controlling equality/DDD Morse rank;
- the child return preserves the outer cap continuation;
- repeated pushes and failed weld pops cannot regenerate an equivalent parent state.

Those are the global source-rank obligations.

What is proved is narrower:

\[
\boxed{
\text{Heawood's 298 Kempe classes create no new mixed terminal.}
}
\]

---

## 8. Revised research target

### Target 8.1 — NNI-forced exterior cancellation or escape

For a complete prime inherited-flow state with one bad marked pair, prove one of:

1. a Kempe channel repairs the pair;
2. a root-valued NNI reaches `B`;
3. a root-valued NNI creates a mark-exterior equal-face edge;
4. the NNI exposes a route/profile event, bounded carrier, or accepted separator;
5. a strict equality/DDD Morse move supplies an equivalent continuation-normalized push.

The Heawood certificate establishes Alternative 3 for the first nontrivial cyclically-six-edge-connected Kempe obstruction.

---

## 9. Trust boundary

### Exact here

- complete equal-face census on all `119280` `H'` root flows;
- minimum of two equal-face edges;
- absence of an equal-face-free one-NNI Heawood flow;
- existence of a mark-exterior equal-face cancellation after a suitable marked NNI for every trapped state in both nonadjacent edge-pair orbits;
- compatibility of that cancellation with ordered marked-incidence genealogy;
- bounded continuation-normalized NNI--cancellation path for every Heawood trapped state.

### Finite/computational boundary

All universal quantifiers in this dossier range over the exhaustively enumerated Heawood and one-NNI `H'` states. No general prime-graph theorem is inferred.

### Not proved

- NNI-forced exterior cancellation in arbitrary prime graphs;
- a universal mixed-state Morse or continuation rank;
- marked-weld relative return, cancellation macro-return, R2 global return or cap restoration;
- the global five-support theorem;
- independent audit, curation, Lean verification, manuscript integration, release, arXiv, DOI, peer review or publication.
