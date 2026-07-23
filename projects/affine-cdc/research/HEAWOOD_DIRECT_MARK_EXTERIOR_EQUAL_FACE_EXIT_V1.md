# Every Heawood root flow already has a mark-exterior equal-face cancellation

## Research Lead shortening and supersession dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `252cc8f9e48488709235369aeb60519659135ce5`.

**Supersedes for Heawood disposition:** the use of the NNI detour in `HEAWOOD_PACHNER_FORCED_EQUAL_FACE_EXIT_V1.md`.

**Retains:** every exact enumeration in `HEAWOOD_PRIME_KEMPE_COMPONENT_OBSTRUCTION_V1.md`, `HEAWOOD_ONE_PACHNER_LAYER_MIXED_RECONFIGURATION_V1.md`, and `HEAWOOD_PACHNER_FORCED_EQUAL_FACE_EXIT_V1.md` as finite reconfiguration data.

**Status:** exact stronger bounded theorem. Every labelled `R_5` root flow on the Heawood graph already contains at least three equal-face edges before any Kempe or Pachner move. Therefore, for any two marked edge objects, at least one equal-face edge is distinct from both marks. Every inherited Heawood marked-pair state has an immediate mark-exterior strict cancellation. The 298 ordinary Kempe components are real but irrelevant as terminal obstructions to mixed source descent.

---

## 1. Equal-face census on Heawood

For one root flow `lambda`, let

\[
T_v\in\binom{[5]}3
\]

be the support triangle determined by the three roots incident with vertex `v`.

An edge `uv` is equal-face when

\[
T_u=T_v.
\]

Exact evaluation over all

\[
\boxed{148320}
\]

labelled Heawood root flows gives:

\[
\boxed{
\begin{array}{c|r}
\#\text{ equal-face edges}&\#\text{ root flows}\\
\hline
3&6720\\
5&20160\\
6&40320\\
9&60480\\
13&20160\\
21&480.
\end{array}}
\]

The counts sum to `148320`.

Hence:

\[
\boxed{
\min_{\lambda}\#E_{\rm eq}(\lambda)=3.}
\]

No Heawood root flow is equal-face-free.

---

## 2. Two marked edges cannot block all cancellations

Let `e,f` be any two distinct marked graph-edge objects.

At most two equal-face edges belong to the marked set

\[
\{e,f\}.
\]

Since every flow has at least three equal-face edges, there exists

\[
g\in E_{\rm eq}(\lambda)\setminus\{e,f\}.
\]

### Theorem 2.1 — direct mark-exterior cancellation

Every Heawood root flow and every marked edge pair admit an equal-face cancellation at an edge `g` distinct from both marks.

The cancellation:

1. removes two source vertices;
2. preserves both marked edge objects;
3. preserves all four ordered marked incidences;
4. preserves both marked root values;
5. produces a lower-order root flow on the cancellation output;
6. creates no local coefficient defect for the inherited flow.

Thus it is a direct mark-exterior child push in the nested return framework.

---

## 3. Consequence for Kempe traps

`HEAWOOD_PRIME_KEMPE_COMPONENT_OBSTRUCTION_V1.md` proves that many nonadjacent marked pairs are trapped away from `B` inside their ordinary Kempe components.

The present theorem shows:

\[
\boxed{
\text{ordinary Kempe trap}
\not\Rightarrow
\text{mixed source terminal}.}
\]

Every such state has an immediate strict cancellation independent of:

- which of the 298 Kempe components contains the inherited flow;
- whether the marked relation is equality or disjointness;
- the line-graph distance between the marked edges;
- whether a marked NNI would repair the pair.

The ordinary Kempe-component obstruction is therefore bypassed by the graph-changing source grammar at once.

---

## 4. Relation to the NNI-layer dossiers

The following finite statements remain exact and useful:

1. every one-NNI Heawood topology is isomorphic to `H'`;
2. `H'` has `119280` root flows and `129` Kempe components;
3. one marked NNI plus `H'` Kempe motion repairs most but not all Heawood trapped states;
4. every `H'` flow also has at least two equal-face edges;
5. every trapped Heawood state has a marked NNI whose output has a mark-exterior equal-face edge.

However, none is needed for the shortest Heawood source disposition, because the equal-face edge already exists before the NNI.

Read the controlling bounded path as

\[
\boxed{
\text{Heawood inherited state}
\longrightarrow
\text{mark-exterior equal-face cancellation}.}
\]

The NNI path is a supplementary mixed-reconfiguration certificate.

---

## 5. Continuation-rank significance

This theorem supplies a strict lower-order child edge, but it does not alone prove the global continuation-normalization condition.

The unresolved issue remains:

- how the lower-order child returns while preserving or transporting the two marked weld incidences;
- how a failed inverse weld is compared with the stored parent continuation;
- why repeated direct cancellations cannot reset an equally large parent frame.

Thus the theorem removes Heawood as a positive-vertex full-lock source obstruction; it does not close cancellation re-entry.

---

## 6. Revised source target

The next general source theorem should not ask first whether a prime full lock is Kempe-flexible.

It should ask:

> Does every prime inherited bad-pair state admit either a mark-exterior equal-face cancellation, a strictly Morse-lowering root Pachner move, a route/profile exit, or an accepted separator/bounded reduction?

Heawood satisfies the first alternative uniformly.

Only equal-face-free prime root states can support a genuinely new full-lock source obstruction.

This narrows the global search to:

\[
\boxed{
\text{prime}
+
\text{equal-face-free}
+
\text{marked full-channel lock}.}
\]

---

## 7. Trust boundary

### Exact here

- complete Heawood equal-face census;
- minimum of three equal-face edges in every root flow;
- existence of a mark-exterior equal-face edge for every two marked edges;
- immediate strict cancellation disposition of every Heawood inherited Kempe trap;
- supersession of the NNI detour as the shortest Heawood argument.

### Finite/computational boundary

The universal statements concern the exhaustively enumerated Heawood graph only.

### Not proved

- the corresponding equal-face-or-Morse theorem for arbitrary prime graphs;
- continuation-normalized cancellation re-entry;
- marked-weld relative return, R2 global return or cap restoration;
- the global five-support theorem;
- independent audit, curation, Lean verification, manuscript integration, release, arXiv, DOI, peer review or publication.
