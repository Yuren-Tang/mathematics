# Generic two-edge and simultaneous weld-flow selection already fail on small cubic graphs

## Research Lead SAT obstruction dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `3260543eb488c871050ff5832caad021774a3d61`.

**Parents:**

- `CANCELLATION_EXIT_REENTRY_WELL_FOUNDEDNESS_GAP_V1.md`;
- `MARKED_WELD_RELATIVE_CONTEXTUAL_RETURN_TARGET_V1.md`;
- `WELD_B_ORBIT_SWITCH_AND_MOBILE_MARK_GRAPH_V1.md`.

**Status:** exact small-graph negative certificate. A naive Repair C asserting that every distinguished edge pair outside a two-edge cut can be made distinct intersecting by some root flow is false already on `K_4`. A stronger generic intersection principle asserting simultaneous attainability of individually attainable `B` constraints is false on both the triangular prism and `K_(3,3)`. Therefore inverse-weld flow selection cannot be repaired by a graph-independent pair-selection or Helly theorem. Any valid theorem must use the inherited canonical weld flow, the particular return history, outer cap/route data, or additional source structure.

---

## 1. Flow model and SAT certificate

For a connected cubic graph `G`, assign five Boolean coordinates to every edge. Impose:

1. exactly two coordinates are one on every edge;
2. at every vertex, each coordinate has even incident parity.

The first condition says every edge value is one root of

\[
R_5=\binom{[5]}2.
\]

The second is exactly the `E_5` flow equation. Thus the SAT solutions are precisely all root-valued `E_5` flows, with support labels retained.

For two distinguished edges `e,f`, classify their values as:

\[
A:\lambda(e)=\lambda(f),
\]

\[
B:\lambda(e),\lambda(f)\text{ distinct and intersecting},
\]

\[
C:\lambda(e),\lambda(f)\text{ disjoint}.
\]

The SAT enumeration is complete, not random sampling.

---

## 2. `K_4`: non-two-cut does not imply `B` attainability

The complete SAT enumeration gives

\[
\boxed{180}
\]

root-valued flows on labelled `K_4`.

Among its fifteen unordered edge pairs, exactly three never occur in the `B` relation. They are the three pairs of opposite edges:

\[
\boxed{
(01,23),
\qquad
(02,13),
\qquad
(03,12).
}
\]

Across all root flows, each such pair occurs only in states `A` or `C`.

`K_4` is three-edge-connected. In particular none of these pairs is a two-edge cut.

### Theorem 2.1

The implication

\[
\boxed{
\{e,f\}\text{ is not a two-edge cut}
\Longrightarrow
\exists\lambda:\ (\lambda(e),\lambda(f))\in B
}
\]

is false.

Thus the cut-sum equality obstruction is not the only possible obstruction to `B` selection.

---

## 3. Triangular prism

For the labelled triangular prism with edges

\[
01,02,03,12,14,25,34,35,45,
\]

complete SAT enumeration gives

\[
\boxed{540}
\]

root-valued flows.

Of the thirty-six unordered edge pairs:

\[
\boxed{30}
\]

are individually `B`-attainable, while

\[
\boxed{6}
\]

never occur in `B`.

More importantly, among pairs of individually `B`-attainable edge-pair constraints, there are

\[
\boxed{18}
\]

unordered pairs of constraints for which no single root flow realizes both in `B` simultaneously.

### Consequence

Even when a proposed weld pair and a second boundary pair are each separately root-successful, their complete physical profile sets need not intersect.

---

## 4. `K_(3,3)`

For labelled `K_(3,3)`, complete SAT enumeration gives

\[
\boxed{840}
\]

root-valued flows.

Every one of its thirty-six unordered edge pairs is individually `B`-attainable:

\[
\boxed{36/36.}
\]

Nevertheless there are

\[
\boxed{81}
\]

unordered pairs of individually attainable `B` constraints which cannot be realized simultaneously by any root flow.

### Theorem 4.1 — no generic two-constraint Helly property

The family of root-flow boundary-profile subsets does not satisfy the implication

\[
\boxed{
\Sigma_B(P)\ne\varnothing,
\quad
\Sigma_B(Q)\ne\varnothing
\Longrightarrow
\Sigma_B(P)\cap\Sigma_B(Q)\ne\varnothing.
}
\]

This fails even on the highly symmetric three-edge-connected graph `K_(3,3)`.

---

## 5. Exact census table

\[
\boxed{
\begin{array}{c|c|c|c}
G&\#\text{ root flows}&\#\text{ edge pairs with no }B&
\#\text{ individually }B\text{ but jointly impossible constraint pairs}\\
\hline
K_4&180&3&0\\
\text{triangular prism}&540&6&18\\
K_{3,3}&840&0&81
\end{array}}
\]

The final column ranges over unordered pairs of unordered edge-pair constraints.

---

## 6. What this does and does not refute

The canonical `C6/C8` cancellation output already carries one inherited root flow in which its reconnecting edges have roots `z,w` with

\[
(z,w)\in B.
\]

Therefore the present certificate does **not** say that the actual weld pair lacks a `B` flow.

It refutes the proposed shortcut:

> discard the inherited flow, apply a generic lower-order root-flow existence theorem, and then select another flow satisfying the weld relation and the outer terminal independently.

The two requirements may have disjoint profile sets even when each is nonempty.

Hence a valid repair must exploit at least one of:

1. history-coherent deformation of the inherited `B` flow;
2. a special route/cap theorem for the canonical weld geometry;
3. first-`B`-exit localisation with a strict causal rank;
4. a source-specific profile identity stronger than generic nonemptiness;
5. an explicitly computed finite relative state game.

---

## 7. Consequence for the repair queue

### Retire as generic statements

- “non-two-cut edge pairs always admit a `B` root flow”;
- “individually attainable boundary constraints are jointly attainable”;
- “ordinary lower-order root solvability can be upgraded to inverse-weld solvability by a support permutation.”

Support permutations preserve `A/B/C` relation type and cannot repair a missing profile intersection.

### Retain as live

- the inherited canonical `B` flow;
- weld-relation first-exit along a specific finite return history;
- route-aware and source-aware relative selection;
- the nested history-stack or finite-game approach.

---

## 8. Exact next theorem

### Target 8.1 — inherited-flow relative path theorem

Starting from the inherited lower-order `B` flow produced by a canonical cancellation, deform it toward an outer cap-compatible terminal through a specified root-surgery/Kempe history. Prove one of:

1. the `B` relation survives and inverse weld succeeds;
2. the first `B` exit gives the shorter-prefix zero/co-root atom of `WELD_RELATION_FIRST_EXIT_V1.md`;
3. a route/profile event solves the outer cap before the weld constraint is lost;
4. a source separator isolates the two constraints so that support permutations become componentwise independent.

No theorem based only on separate nonemptiness of the two profile conditions can suffice.

---

## 9. Trust boundary

### Exact here

- complete SAT root-flow enumerations for `K_4`, the triangular prism and `K_(3,3)`;
- the three opposite-edge `K_4` obstructions;
- failure of the non-two-cut criterion;
- exact individual `B`-attainability counts;
- exact simultaneous-incompatibility counts;
- failure of a generic two-constraint profile-intersection principle.

### Not proved

- the inherited-flow relative path theorem;
- a counterexample to the canonical weld repair;
- cancellation macro-return or contextual transfer;
- R2 global return, cap restoration, or global five-support closure;
- independent audit, curation, Lean verification, manuscript integration, release, arXiv, DOI, peer review, or publication.
