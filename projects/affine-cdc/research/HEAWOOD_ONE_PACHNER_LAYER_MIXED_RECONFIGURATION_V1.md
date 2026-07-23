# One marked Pachner layer crosses most but not all Heawood Kempe traps

## Research Lead exact mixed-reconfiguration dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `ae8d9c407caa72db69c52e4f64c094e8b6ba5463`.

**Parents:**

- `HEAWOOD_PRIME_KEMPE_COMPONENT_OBSTRUCTION_V1.md`;
- `INHERITED_TWO_EDGE_KEMPE_RECONFIGURATION_CERTIFICATE_V1.md`;
- `MARKED_WELD_PACHNER_OVERLAP_SCOPE_V1.md`;
- `WELD_RELATION_FIRST_EXIT_V1.md`.

**Status:** exact finite mixed-state certificate. Every root-valued `2--2` move from Heawood reaches one common isomorphism type `H'`, a fourteen-vertex cubic graph of girth five and cyclic edge connectivity five. The labelled root-flow Kempe graph of `H'` was exhaustively enumerated. Allowing one root-valued NNI on either marked edge, followed by an arbitrary sequence of Kempe component switches on `H'`, repairs most trapped Heawood marked pairs but leaves nonempty trapped classes in both nonadjacent edge-pair orbits. Thus root Pachner moves genuinely cross ordinary Kempe-component obstructions, but a single Pachner layer does not prove inherited two-edge flexibility. The live theorem needs a multi-layer source rank or an adaptive Morse/source reduction.

---

## 1. One-NNI Heawood topology

For every Heawood edge there are two unlabelled NNI reconnections of its four exterior branches. Across all

\[
21\times2=42
\]

choices, the resulting graphs are mutually isomorphic.

Denote their common isomorphism type by

\[
H'.
\]

Exact graph data:

\[
\boxed{
|V(H')|=14,
\qquad
|E(H')|=21,
\qquad
\operatorname{girth}(H')=5,
\qquad
\lambda_c(H')=5.
}
\]

Here `lambda_c` is cyclic edge connectivity, verified by exhaustive finite cut search.

Thus one NNI leaves the accepted triangle-free/cyclically-five-edge-connected prime layer.

For any particular root flow and central edge, exactly one of the two NNI reconnections is root-valued. The new central root is the unique root-valued opposite diagonal.

---

## 2. Root flows on `H'`

Exact labelled root-flow enumeration gives

\[
\boxed{119280}
\]

root flows on one fixed labelled representative of `H'`.

Its ordinary Kempe reconfiguration graph has

\[
\boxed{129}
\]

connected components, with size distribution

\[
\boxed{
\begin{aligned}
&1\times48480
+1\times35040
+1\times9120
+1\times5280
+1\times1920\\
&\quad+4\times600
+8\times360
+8\times240
+100\times120
+4\times60.
\end{aligned}}
\]

The sum is `119280`.

Every one of the forty-two labelled NNI target graphs was mapped source-isomorphically to this representative, retaining:

- the complete root flow;
- the two marked edge objects;
- which marked edge was the active diagonal;
- all support labels.

Consequently one `H'` census suffices for every Heawood marked-edge NNI.

---

## 3. Mixed repair operation tested

Fix a Heawood root flow `lambda` and marked edges `e,f` whose roots are not in the weld-admissible `B` relation.

The tested operation is:

1. choose either `e` or `f` as the central edge;
2. perform its unique root-valued NNI;
3. enter the corresponding `H'` flow;
4. perform an arbitrary finite sequence of ordinary support-pair component switches on `H'`;
5. ask whether the marked pair reaches `B`.

This operation retains the marked central-edge lineage by transporting it to the opposite diagonal, as in the mobile-envelope theorem.

A state is counted as repaired if either choice of marked central edge succeeds.

---

## 4. Heawood distance-two orbit

For one, hence every, line-graph-distance-two pair, the original Heawood Kempe graph has

\[
\boxed{105}
\]

trapped components and

\[
\boxed{26160}
\]

trapped root flows.

Their relation census is

\[
\boxed{
12720\text{ equality states}
+
13440\text{ disjoint states}.}
\]

After one marked NNI and arbitrary `H'` Kempe motion:

\[
\boxed{
\begin{array}{c|cc}
\text{initial relation}&\text{repaired}&\text{still trapped}\\
\hline
A&9600&3120\\
C&9600&3840
\end{array}}
\]

Therefore

\[
\boxed{
19200/26160\text{ trapped flows are repaired},
\qquad
6960/26160\text{ survive}.}
\]

At the original-component level:

- equality components: 27 are entirely repaired, 18 entirely survive, 4 are mixed;
- disjoint components: 24 are entirely repaired, 32 entirely survive.

---

## 5. Heawood distance-three orbit

For one, hence every, line-graph-distance-three pair, the original Kempe graph has

\[
\boxed{51}
\]

trapped components and

\[
\boxed{11880}
\]

trapped flows.

Their relation census is

\[
\boxed{
3720\text{ equality states}
+
8160\text{ disjoint states}.}
\]

After one marked NNI and arbitrary `H'` Kempe motion:

\[
\boxed{
\begin{array}{c|cc}
\text{initial relation}&\text{repaired}&\text{still trapped}\\
\hline
A&1440&2280\\
C&7200&960
\end{array}}
\]

Thus

\[
\boxed{
8640/11880\text{ are repaired},
\qquad
3240/11880\text{ survive}.}
\]

At the component level:

- equality: 8 components entirely repaired, 16 entirely survive, 1 mixed;
- disjoint: 18 entirely repaired, 8 entirely survive.

---

## 6. Local interpretation

A marked-edge root NNI acts on relation type as follows.

### Equality input

If the marked roots are equal `p,p`, moving one central root replaces it by a root disjoint from `p`. Hence one NNI changes

\[
A\longrightarrow C,
\]

never directly to `B`.

Any equality repair in this dossier therefore genuinely uses subsequent `H'` Kempe motion.

### Disjoint input

If the roots are disjoint `p,q`, the opposite diagonal to `p` is one of the three roots disjoint from `p`.

- If it equals `q`, the relation becomes `A`.
- If it is one of the other two, it intersects `q`, and the move gives `B` immediately.

This explains why the DDD/disjoint sector is substantially more responsive to one Pachner layer than equality, especially in the distance-three orbit.

---

## 7. Exact conclusion

The Heawood obstruction is not invariant under root Pachner moves:

\[
\boxed{
\text{one NNI layer repairs a strict majority of trapped states}.}
\]

But neither is one Pachner layer sufficient:

\[
\boxed{
6960\text{ distance-two states}
+
3240\text{ distance-three states}
}
\]

remain trapped in the tested mixed neighbourhood.

Therefore the following shortcuts are both false:

1. ordinary Kempe motion alone resolves every prime full lock;
2. one marked root NNI followed by arbitrary Kempe motion resolves every prime full lock.

---

## 8. Revised mixed target

### Target 8.1 — multi-layer Pachner/Kempe source descent

For a trapped marked pair in one complete inherited-flow context, permit alternating blocks of:

- Kempe component switches;
- category-safe root `2--2` moves;
- equality/DDD Morse-selected moves;
- equal-face moves governed by the continuation stack;
- route/profile and separator exits.

Prove that every nonterminal mixed component has one of:

1. a `B` state;
2. an outer terminal;
3. a bounded/separator source reduction;
4. a cancellation push preceded by strict continuation progress.

The rank cannot be “number of Kempe components crossed” or “one Pachner layer”. It must use a source-level Morse, enclosure, or finite mixed-component order.

---

## 9. Next finite experiments

1. Enumerate a second NNI layer only for the surviving `H'` components rather than the full state space.
2. Compare surviving states with equality/DDD Morse weights and root-triangle adjacency types.
3. Test whether every survivor has an equal-face cancellation, a route event, or an NNI to a topology with a triangle/cyclic-small-cut reduction.
4. Search for a finite invariant which decreases under the actual Morse-selected NNI, not under every NNI.

---

## 10. Trust boundary

### Exact here

- uniqueness of the one-NNI Heawood isomorphism type;
- exact graph parameters of `H'`;
- complete `H'` root-flow enumeration and Kempe-component distribution;
- source-isomorphic mapping of all forty-two labelled NNI targets;
- exact repair/survival counts for both nonadjacent Heawood pair orbits;
- proof that one Pachner layer crosses many but not all ordinary Kempe traps.

### Finite/computational boundary

All conclusions concern the explicitly enumerated Heawood/`H'` mixed neighbourhood. They do not prove termination for arbitrary prime graphs.

### Not proved

- multi-layer mixed source descent;
- a strict Morse rank on the surviving components;
- continuation-normalized local rank;
- marked-weld return, cancellation macro-return, R2 global return or cap restoration;
- the global five-support theorem;
- independent audit, curation, Lean verification, manuscript integration, release, arXiv, DOI, peer review or publication.
