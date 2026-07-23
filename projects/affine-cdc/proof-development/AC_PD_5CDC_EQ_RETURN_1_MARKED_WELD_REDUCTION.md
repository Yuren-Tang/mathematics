# AC-PD-5CDC EQ-RETURN 1 — marked-weld reduction and finite obstruction scout

**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Research target consumed:** `MARKED_WELD_RELATIVE_CONTEXTUAL_RETURN_TARGET_V1.md`  
**State:** `ACTIVE / EXACT REDUCTIONS / PRIME FLEXIBILITY OPEN`.

---

## 1. Canonical marked weld

After cancelling one canonical equal-face pair with root triangle

\[
\{z,w,u\},\qquad u=z+w,
\]

the two reconnected edges carry roots `z` and `w`. Cutting their interiors exposes

\[
W=(z,z,w,w),
\qquad z\ne w,
\qquad |z\cap w|=1.
\]

If a lower-order contextual return preserves this word, inverse insertion is canonical and root-valued.

The exact labels are stronger than necessary. The ordered orbit of `W` under one global support permutation is sufficient: `S_5` is transitive on ordered pairs of distinct intersecting roots. Thus a returned word

\[
W'=(z',z',w',w'),
\qquad z'\ne w',
\qquad |z'\cap w'|=1,
\]

may be globally relabelled to `W`, together with all outer cap and route data, before inverse insertion.

Hence the essential invariant is the **intersecting-pair orbit**, not the literal names `z,w`.

---

## 2. Disconnected cancellation output

Suppose the cancelled graph has distinct connected components containing the two marked edges. Each component may be relabelled by an independent element of `S_5` before taking their disjoint union. Given arbitrary nonzero root labels on the two edges, choose the two component permutations so that the labels become any prescribed ordered pair of distinct intersecting roots.

Therefore cancellation re-entry is automatic in the split-component case.

### Proposition 2.1

If the two marked reconnecting edges lie in different connected components of the cancellation output, the equal-face pair can be reinserted root-valuedly after componentwise return.

The remaining marked-weld obstruction lies in one connected continuing component containing both marked edges.

---

## 3. Relative local-move lemma

Cut the two marked edges and regard the four half-edges as frozen semiedges.

For a root-valued `2--2` move or first-failure normalization whose central edge is internal:

1. if its support is disjoint from every frozen semiedge, the move commutes strictly with the marking;
2. if a frozen semiedge is one of the four exterior branches, its incidence and root value are unchanged by the move;
3. the local pairing-sum and first-failure classifications are unchanged, because they depend only on the four branch roots;
4. category safety of a root-valued NNI remains valid with frozen exterior branches.

Thus ordinary root flips, inverse-flip zero normalization and bounded co-root critical-overlap normalization are already relative to `W` whenever the marked branches remain exterior.

### New collision types

The only genuinely new local interfaces are:

- a proposed transition whose central edge is one of the two marked reconnecting edges before cutting;
- a Kempe/route switch whose switched component meets the marked boundary and changes its orbit type;
- a terminal normalization which identifies or redistributes marked incidences;
- a component split which places the four marks in a nontrivial genealogy.

This is a much smaller attack surface than a full reconstruction of every local theorem.

---

## 4. Unrestricted inverse-weld flow selection is false

A tempting repair is:

> for every root-soluble bridgeless cubic graph and every two specified edges, some root flow makes their values distinct and intersecting.

Exact labelled-flow enumeration disproves this without prime/bounded qualifications.

### `K_4`

There are `180` labelled `R_5` root flows. For each pair of opposite edges, the realised relation types are exactly

\[
\{\text{equal},\text{disjoint}\};
\]

no flow gives an intersecting pair.

### Triangular prism

There are `540` labelled root flows. Six specified edge pairs likewise realise only equal or disjoint labels and never an intersecting pair.

Both graphs belong to the bounded/small-structure layer, so this does not refute a prime-context theorem. It proves that Repair C must explicitly retain bounded and separator exits.

The census was independently evaluated by a cycle-space enumeration: choose five binary cycle-space vectors and retain exactly those assignments for which every edge has coordinate weight two.

---

## 5. Prime small-graph scout

A Boolean exact-satisfiability census was run for every unordered edge pair in the following connected cubic graphs:

- Petersen graph;
- Möbius--Kantor graph;
- Heawood graph;
- Pappus graph;
- Desargues graph.

For every tested pair, a root flow with distinct intersecting values exists. No bad pair occurs in these five cyclically robust examples.

This is finite evidence only. It supports the following precise research target.

### Target 5.1 — prime two-edge flexibility

Let `H` be a connected root-soluble cubic graph in the prime branch after the accepted bounded and small-cut reductions. For any two distinguished nonloop edges `e,f`, either:

1. there is an `R_5` root flow with `lambda(e),lambda(f)` distinct and intersecting; or
2. `H,e,f` exposes an accepted bounded or separator configuration.

Target 5.1 would imply the marked-weld flow-selection repair after cancellation, because the cancellation output is strictly smaller and already root-soluble.

No proof of Target 5.1 is presently known.

---

## 6. Kempe formulation of the prime target

For a root flow with indexed even supports `(F_1,...,F_5)`, a support-pair Kempe switch is performed on one cycle component of

\[
F_a\triangle F_b.
\]

If the marked edge values are equal, six support-pair systems can change one edge without the other. If they are disjoint, four crossed support-pair systems do so. A separating Kempe component immediately changes the marked pair to the intersecting orbit.

The only obstruction is therefore a **two-edge full-channel lock**: in every relevant channel, the two marked edges lie in the same cycle component. The prime flexibility problem is equivalent to proving that such a lock gives:

- a further root/co-root flexible cycle correction;
- a bounded rigid label geometry;
- or a small separator.

This isolates the remaining mathematics without invoking the original same-order cap-extension theorem.

---

## 7. Current repair split

The marked-weld return problem now decomposes as follows.

1. **Different components:** closed by independent `S_5` alignment.
2. **Ordinary local root moves with marks exterior:** closed by the relative local-move lemma.
3. **Bounded graphs:** require explicit finite terminals; unrestricted pair selection is false.
4. **One prime connected component:** open two-edge full-channel flexibility / marked route preservation.
5. **Terminal and component genealogy:** remains to be checked after the prime flexibility theorem is chosen.

---

## 8. Trust boundary

### Exact here

- preservation up to the ordered intersecting-pair `S_5` orbit is sufficient;
- split-component marked welds are solvable by independent support relabelling;
- disjoint and exterior-branch local moves are automatically relative;
- the exact new collision list;
- counterexamples to unrestricted two-edge selection on `K_4` and the triangular prism;
- exact positive finite evidence on five prime small graphs.

### Open

- Target 5.1 in arbitrary prime graphs;
- classification of a two-edge full-channel lock;
- marked route-switch and terminal normalization;
- complete `MWR`;
- repaired contextual return and global five-support closure.