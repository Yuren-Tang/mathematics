# Support-pair switches lift through one weld insertion with at most one atom

## Research Lead innermost-bubble local theorem v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`

**Parents:**

- `WELD_RELATION_FIRST_EXIT_V1.md`;
- `WELD_MARK_EQUAL_FACE_OVERLAP_V1.md`;
- `ROOT_VALUED_ALTERNATIVE_INVERSE_CANCELLATION_INSERTION_V1.md`;
- the support-pair identity `A_h=F_i triangle F_j`.

**Status:** exact source-level lift of one ordinary support-pair component switch through an inserted equal-face weld. If the switch changes neither marked output edge, it commutes. If it changes one marked edge and the other is not eligible for that channel, the switch lifts root-valuedly by routing the channel through the inserted central edge. If both marked roots are eligible, simultaneous switching lifts root-valuedly; one-sided switching lifts to a predecessor-order `E_5` flow with exactly one non-root central edge, zero or co-root according to the known equality/DDD table. No second defect occurs.

---

## 1. Inserted weld and channel parity

Let two edges of a root-valued lower-order graph carry a weld-admissible pair

\[
p,q\in R_5,
\qquad
p\ne q,
\qquad
p+q=r\in R_5.
\]

Insert two equal root triangles

\[
(p,q,r)
\]

on the two edges. Denote the expanded graph by `I(H)`.

Fix a root switch direction

\[
h=ij.
\]

For a root `x`, write

\[
\epsilon_h(x)=1
\]

when

\[
x+h\in R_5,
\]

equivalently when `x` contains exactly one endpoint of `h`.

This is linear mod two on support indicators, so

\[
\boxed{
\epsilon_h(r)=\epsilon_h(p)+\epsilon_h(q)\pmod2.
}
\]

At each inserted cubic vertex the eligible-edge degree is therefore even.

---

## 2. Neither marked edge switched

Let `Z` be one component of the lower-order channel graph

\[
A_h(H)=F_i\triangle F_j.
\]

If neither marked edge lies in `Z`, the same component is present unchanged in `I(H)` and is disjoint from the inserted pair.

Switching `Z` commutes strictly with insertion.

---

## 3. Exactly one marked edge eligible

Assume the `p` edge lies in `Z` and

\[
\epsilon_h(p)=1,
\qquad
\epsilon_h(q)=0.
\]

Then

\[
\epsilon_h(r)=1.
\]

In the expanded graph, replace the occurrence of the lower-order `p` edge in `Z` by the three-edge path

\[
p_L-r-p_R
\]

through the two inserted vertices. Let the resulting edge set be `widehat Z`.

### Lemma 3.1

`widehat Z` is one component of the expanded channel graph `A_h(I(H))`.

### Proof

Every old vertex has the same channel degree as in `Z`. At each inserted vertex exactly the incident `p` half-edge and the central `r` edge are eligible, so the path continues uniquely through the insertion. The `q` half-edges are not eligible. ∎

Switching `widehat Z` changes

\[
p\mapsto p+h,
\qquad
r\mapsto r+h,
\]

and leaves `q` fixed. All three values

\[
p+h,\ q,\ r+h
\]

are roots and satisfy

\[
(p+h)+q=r+h.
\]

Thus both inserted vertices remain equal root triangles.

### Theorem 3.2 — one-eligible root lift

A lower-order component switch containing exactly one marked edge, while the other marked root is not channel-eligible, lifts to one ordinary root-valued support-pair switch on the expanded graph.

The transported marked pair remains in the `B` orbit.

---

## 4. Both marked roots eligible

Assume

\[
\epsilon_h(p)=\epsilon_h(q)=1.
\]

Then

\[
\epsilon_h(r)=0.
\]

At each inserted vertex the two eligible external half-edges are the `p` and `q` half-edges; the central `r` edge is not in the root channel.

### 4.1 Both marked edges in one lower component

If one lower-order component `Z` contains both marked edges, remove those two edge interiors. Its remaining portions reconnect at the inserted vertices by pairing the eligible `p` and `q` half-edges.

The inherited edge set in `I(H)` is an even union of one or two root-channel circuits. Switch every resulting circuit. Then

\[
p\mapsto p+h,
\qquad
q\mapsto q+h,
\qquad
r\mapsto r.
\]

The inserted triangles remain root-valued because

\[
(p+h)+(q+h)=p+q=r.
\]

### 4.2 Marked edges in different components, both switched

Let `Z_p,Z_q` be the two lower components. Their inherited expanded edge union is even: at each inserted vertex one `p` and one `q` half-edge occur. Switch its circuit components. The same root-valued formula results.

### Theorem 4.1 — simultaneous root lift

Whenever a lower-order switch changes both channel-eligible marked edges, the switch lifts root-valuedly through the insertion, even if expansion merges or splits their channel components.

The weld pair remains in `B`.

---

## 5. One-sided switch with both marked roots eligible

Assume `p,q` are both eligible but lie in different lower-order channel components. Switch only the component `Z_p` containing the `p` edge.

In the expanded graph form `widetilde Z_p` by:

1. retaining every inherited edge of `Z_p`;
2. retaining both split `p` half-edges;
3. adding the central edge of value `r`;
4. retaining no `q` half-edge.

At every old vertex `widetilde Z_p` has even degree. At each inserted vertex it contains exactly the `p` half-edge and the central edge. Thus it is an even source subgraph.

Add `h` to every edge of `widetilde Z_p`.

### Theorem 5.1 — one-atom one-sided lift

The resulting assignment is an `E_5` flow on the same predecessor-order source graph. Every edge remains root-valued except possibly the inserted central edge, whose value becomes

\[
\boxed{r+h.}
\]

The marked values become

\[
(p+h,q).
\]

At each inserted vertex conservation is

\[
(p+h)+q+(r+h)=0.
\]

### Exact non-root type

For a weld triangle `p,q,r=p+q`, the common eligible channels for `p,q` are:

- `h=r`, giving
  \[
  r+h=0;
  \]
- two roots disjoint from `r`, giving
  \[
  r+h=Q_k
  \]
  for one co-root.

Therefore the one-sided lift produces exactly the known equality or doubled-disjoint first-exit atom. It creates no second defect.

The symmetric statement holds when only the `q` component is switched.

---

## 6. Complete switch-lift table

For one lower-order support-pair component switch relative to one inserted weld:

\[
\begin{array}{c|c}
\text{marked interaction}&\text{predecessor-order lift}\\
\hline
\text{neither marked edge}&\text{strict root commutation}\\
\text{one eligible, other ineligible}&\text{root switch through the central edge}\\
\text{both eligible, both switched}&\text{root simultaneous lift}\\
\text{both eligible, one switched}&\text{one zero/co-root central atom}.
\end{array}
\]

There is no additional source or coefficient branch.

---

## 7. Relation to the first-`B`-exit theorem

The coefficient theorem `WELD_RELATION_FIRST_EXIT_V1.md` states that one-sided common-channel switching changes a `B` pair to `A` or `C`.

The present theorem supplies its missing source realisation:

- the expanded predecessor-order graph is unchanged topologically;
- the lower switched component lifts together with the inserted central edge;
- the only failed root is the central insertion edge;
- its value is exactly the zero/co-root forced by the returned marked pair.

Thus a first `B`-exit caused by a support-pair switch is a genuine one-atom history cell, not merely a coefficient comparison.

---

## 8. Consequence for one innermost bubble

For an innermost lower-order history consisting of root-valued `2--2` moves and support-pair component switches:

- disjoint/exterior flips lift strictly;
- generic active-diagonal flips lift by the central source movies;
- adjacent active-diagonal flips lift in three root NNIs;
- support-pair switches lift root-valuedly or with one first-exit atom.

The remaining burden is global assembly of these local lifts into one predecessor-order strip and disposition of any first atom relative to the rest of the lower-order history.

---

## 9. Assurance boundary

### Exact here

- channel-parity identity at the inserted vertices;
- strict root lift when neither mark or only one eligible mark is involved;
- simultaneous root lift when both eligible marks switch;
- explicit even correction subgraph for a one-sided common-channel switch;
- exactly one zero/co-root central atom;
- complete support-switch source-lift table.

### Not claimed

- root/Kempe connectivity of arbitrary flows;
- complete innermost-bubble strip assembly;
- nested variable-order episode compression;
- R2.7 closure, cap restoration or global five-support closure;
- PDL reconstruction, audit, Lean, manuscript, curation, release or publication.
