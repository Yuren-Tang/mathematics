# Petersen backtracks, the Type-T `abba` word, and the bounded Type-H core

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `2bcd25e8f56886610fd52cbc293a528ccb662efe`  
**Parent:** `projects/affine-cdc/research/PETERSEN_PIVOT_RESOLUTION_V1.md`  
**Status:** exact coefficient-side Type-T/backtrack theorem and finite reduced-cycle dichotomy; graph-side serial contraction and DDD holonomy identification remain open.  
**Not implied:** canonical acceptance, independent audit, Lean verification, manuscript readiness, or the global five-support theorem.

---

## 1. Pivot skeleton as an oriented edge path

Let

\[
s_0,F_1,s_1,F_2,\ldots,F_k,s_k
\]

be the pivot skeleton of an enriched co-root strip, where

\[
F_j=\{s_{j-1},s_j\}\in E(P)
\]

is the DDD/Petersen-edge switch state between two consecutive constant-pivot runs.

Although `P` is undirected, the traversal gives each occurrence of `F_j` an orientation

\[
s_{j-1}\longrightarrow s_j.
\]

An **immediate backtrack** is a subpath

\[
\boxed{s\xrightarrow{F}t\xrightarrow{F}s}
\]

using the same Petersen edge `F={s,t}` in opposite directions.

---

## 2. The exact `abba` word

Consider three consecutive pivot runs with pivots

\[
s,\qquad t,\qquad s.
\]

The two switch states are both

\[
F=\{s,t\}.
\]

### Theorem 2.1 — Petersen backtrack gives Type T

Across the two switch interfaces, the forced root resolutions are

\[
\boxed{t,\ s,\ s,\ t.}
\]

Thus every pivot backtrack carries the exact Type-T serial word

\[
\boxed{abba}
\]

with `a=t` and `b=s`.

### Proof

At the first switch `s\to t`, the left `s`-pivot run forces the non-`s` endpoint `t`, while the right `t`-pivot run forces the non-`t` endpoint `s`.

At the second switch `t\to s`, the left `t`-pivot run again forces `s`, while the right `s`-pivot run forces `t`.

Reading the four forced shore resolutions gives

\[
t,s,s,t.
\]

The middle `t`-pivot run is root-resolvable in the rank-two plane `W_t`, so no additional coefficient obstruction lies between the two equal middle letters. ∎

### Corollary 2.2 — physical meaning of the old `abba` target

The Type-T word is not being inferred from a support-unordered potential pattern. It arises directly from the two actual Petersen root-resolution endpoints demanded by a physical co-root transport skeleton.

The remaining issue is composition, not identification of the word.

---

## 3. Backtrack cancellation

Delete one immediate backtrack

\[
s\to t\to s
\]

from the pivot skeleton and merge the two adjacent `s`-pivot runs at coefficient level.

This operation is called **formal Type-T cancellation**. It records one `abba` unit but does not yet assert that the corresponding source subgraph may be contracted.

### Theorem 3.1 — unique reduced pivot path

Repeated formal Type-T cancellation terminates and produces the unique reduced oriented edge path obtained by the standard stack reduction:

- traverse the pivot skeleton from left to right;
- if the next oriented Petersen edge is the inverse of the current stack top, cancel the pair;
- otherwise push it.

The final reduced path has no immediate backtrack.

### Proof

This is ordinary free reduction in the edge-path groupoid of a graph. Each cancellation lowers the edge count by two. The deterministic stack algorithm gives a unique result for the given oriented path. ∎

### Definition 3.2 — reduced pivot length

Let

\[
\ell_{\mathrm{red}}(R)
\]

be the number of oriented Petersen edges in the reduced pivot path of the interval or strip `R`.

It is a coefficient-side complexity measure. A graph-side descent theorem must still prove that deleting a recorded `abba` unit is composition-safe before using `\ell_red` as a genuine induction parameter.

---

## 4. Closed-skeleton dichotomy

Assume the pivot skeleton is closed:

\[
s_k=s_0.
\]

### Theorem 4.1 — Type T or reduced Petersen core

Exactly one of the following holds.

1. **Type-T null branch.** The reduced pivot path is empty. Then the complete coefficient skeleton is a concatenation of Petersen backtracks and therefore of exact Type-T `abba` units.

2. **Reduced-cycle branch.** The reduced pivot path is nonempty. Then it is a cyclically reduced closed walk in the Petersen graph and contains a simple Petersen cycle.

### Proof

If stack reduction deletes every edge, the original edge word is a product of adjacent inverse pairs; Theorem 2.1 turns every deleted pair into one `abba` unit.

Otherwise the reduced word is a nonempty closed edge path with no adjacent inverse pair. Any nonempty closed walk contains a simple cycle: choose two equal pivot occurrences at minimum positive distance. Minimality removes repeated internal pivots, and the absence of immediate backtracking excludes the two-edge return. ∎

### Corollary 4.2 — bounded Type-H candidate core

Every nonempty reduced closed pivot skeleton contains a simple cycle on at most ten Petersen vertices.

Therefore its coefficient obstruction localises to a bounded DDD switch core. The unbounded remainder consists only of rank-two constant-pivot runs and formally cancellable Type-T backtracks.

The theorem does not yet identify the simple-cycle core with the physical nontrivial `D_8` cohomology class; it gives the exact finite object on which that identification must be proved.

---

## 5. Open-skeleton localisation

Let the reduced pivot path be open.

### Theorem 5.1 — long reduced path exposes a bounded cycle

If the reduced path contains more than nine edges, then some pivot repeats. A shortest repeated-pivot subpath is a simple Petersen cycle, because the reduced path has no immediate backtrack.

Hence every open pivot skeleton admits the coefficient-side alternative:

1. after Type-T cancellation it has at most nine DDD switch states; or
2. it contains a bounded simple Petersen-cycle core.

### Proof

The Petersen graph has ten vertices. A path with more than nine edges has more than ten pivot occurrences, so some pivot repeats. Choose a repeated pair at minimum positive distance. The interior pivots are distinct. Since the path is reduced, the segment is not a two-edge backtrack; therefore it is a simple cycle. ∎

---

## 6. Coefficient-side Type T / Type H normal form

Combine the constant-pivot resolution theorem with the backtrack reduction.

### Theorem 6.1 — normal form

Every enriched co-root strip has the following coefficient-side normal form:

\[
\boxed{
\text{rank-two root runs}
+
\text{Type-T `abba` backtrack units}
+
\text{one reduced Petersen path/cycle skeleton}.
}
\]

For a closed strip, the reduced skeleton is either empty or contains a bounded simple Petersen cycle.

No third coefficient mechanism exists.

### Significance

This gives an exact version of the intended Type T / Type H dichotomy:

- **Type T:** reversible pivot excursions, detected by the actual physical root-resolution word `abba`;
- **Type H / DDD candidate:** cyclically reduced motion in the Petersen pivot graph.

The distinction is now intrinsic to the co-root transducer, not imposed from an external routing analogy.

---

## 7. Revised composition targets

The mathematical frontier separates into two explicit transfer lemmas.

### Target 7.1 — Type-T cancellation transfer

For a laminar four-port interval containing a pivot backtrack, prove that its `abba` unit yields one of:

1. a serial contraction;
2. a smaller cyclic separator/four-pole;
3. a root-admissible profile escape;
4. a bounded zero/co-root defect atom.

The proof must retain the external side-root attachments of the middle rank-two run.

### Target 7.2 — reduced-cycle holonomy

For a bounded simple Petersen-cycle skeleton, compute the induced full-frame/side-root holonomy and prove that it is:

1. the physical nontrivial DDD `D_8` class;
2. root-resolvable after a bounded route change;
3. or a bounded separator/defect unit.

These are finite tasks. The remaining unbounded issue is how the laminar external attachments compose with them.

---

## 8. Trust boundary

### Exact here

- a pivot backtrack forces the resolution word `t,s,s,t`;
- this word is the coefficient-side Type-T `abba` pattern;
- deterministic backtrack reduction and uniqueness of the reduced pivot path;
- the closed-skeleton empty/nonempty dichotomy;
- existence of a bounded simple Petersen cycle in every nonempty reduced closed skeleton;
- the nine-edge bound for an open reduced path without a repeated pivot;
- the coefficient-side normal form into rank-two runs, Type-T units, and a reduced Petersen skeleton.

### Still open

- source-graph contraction of an `abba` unit;
- preservation of external side-root semantics under cancellation;
- four-pole transfer for the crossed atom resolutions;
- identification of bounded reduced cycles with the physical `D_8` class;
- strict global descent, horizontal induction, and the global five-support theorem.
