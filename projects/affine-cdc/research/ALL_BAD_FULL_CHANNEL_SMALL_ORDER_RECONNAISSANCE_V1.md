# All-bad and full-channel lock are disjoint through order eight

## Research Lead finite reconnaissance v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Parent frontier:** `CONTEXTUAL_TRANSFER_REPAIR_FRONTIER_V2.md`.

**Status:** exact exhaustive small-order evidence for the sole periodic outer-endpoint obstruction. For every connected simple cubic graph of orders `4,6,8`, every labelled root flow and every unordered pair of edges carrying disjoint roots were examined. No incidence is simultaneously:

1. **all-bad:** all four endpoints use the co-root missing index, so both marked edges join equal support triangles; and
2. **full-channel locked:** for each of the four crossed support pairs, the corresponding even-subgraph component contains both marked edges.

All-bad incidences occur only in the cube and Wagner graph, and every one of them has a one-component Kempe switch containing exactly one marked edge and moving the pair directly into the intersecting `B` orbit.

This is finite reconnaissance, not a proof of the general separator/escape theorem.

---

## 1. Definitions

Let two marked edges carry disjoint roots

\[
a,b\in R_5,
\qquad a\cap b=\varnothing,
\]

and let `i` be the unique missing support index:

\[
[5]=a\sqcup b\sqcup\{i\}.
\]

### All-bad endpoint profile

At an endpoint of the `a`-edge, borrowing the adjacent root triangle is missing-index bad exactly when that triangle is

\[
a\cup\{i\}.
\]

Similarly an endpoint of the `b`-edge is bad exactly when its triangle is

\[
b\cup\{i\}.
\]

The marked pair is **all-bad** when this holds at all four endpoints.

Equivalently:

- the `a`-edge joins two equal support triangles `a union {i}`;
- the `b`-edge joins two equal support triangles `b union {i}`.

Thus both marked edges are equal-face dipole edges in the returned root flow.

### Full crossed-channel lock

For each

\[
x\in a,
\qquad y\in b,
\]

consider the even subgraph

\[
H_{xy}=F_x\triangle F_y.
\]

The pair is **full-channel locked** when, for all four crossed pairs `(x,y)`, the two marked edges belong to the same connected component of `H_(xy)`.

If one crossed channel separates them, switching the component containing exactly one marked edge changes the marked pair from disjoint to intersecting and gives the standard horizontal DDD rescue.

---

## 2. Exhaustive range and method

All connected simple cubic graph isomorphism classes on

\[
4,6,8
\]

vertices were generated. Their counts are

\[
1,2,5.
\]

For each graph:

1. compute the binary cycle space;
2. enumerate all ordered five-tuples of even subgraphs in which every graph edge occurs exactly twice;
3. interpret each tuple as a fully labelled root-valued `E_5` flow;
4. enumerate every unordered edge pair with disjoint root values;
5. test all four endpoint triangles for the missing index;
6. test connected-component membership in all four crossed support channels;
7. build the complete componentwise support-Kempe graph when an all-bad incidence occurs.

---

## 3. Complete census

The counts below are labelled `(root flow, marked edge pair)` incidences.

| graph class | labelled root flows | all-bad incidences | full-lock incidences | all-bad and full-lock |
|---|---:|---:|---:|---:|
| `K_4` | 180 | 0 | 360 | 0 |
| triangular prism | 540 | 0 | 2880 | 0 |
| `K_{3,3}` | 840 | 0 | 4320 | 0 |
| order-8, edge-connectivity 2 class | 3240 | 0 | 18720 | 0 |
| cube | 3960 | 720 | 14400 | 0 |
| Wagner graph / Möbius ladder `M_4` | 3300 | 240 | 21600 | 0 |
| order-8 class with two triangles | 1620 | 0 | 15720 | 0 |
| order-8 class with one triangle | 2520 | 0 | 25200 | 0 |

Therefore:

\[
\boxed{
\text{all-bad}\cap\text{full-lock}=\varnothing
}
\]

through order eight.

---

## 4. Exact shape of the first all-bad examples

Normalize

\[
a=12,
\qquad b=34,
\qquad i=5.
\]

Every all-bad example has endpoint triangles

\[
125,125
\]

on the `12` edge and

\[
345,345
\]

on the `34` edge, up to support permutation.

Thus the two marked edges are complementary equal-face dipoles with the same missing support.

### Cube representative

A representative cube flow has marked roots such as

\[
03
\qquad\text{and}\qquad12
\]

with missing support `4`; the four endpoint triangles are two copies each of

\[
034
\qquad\text{and}\qquad124.
\]

### Wagner representative

A representative Wagner flow has marked roots such as

\[
04
\qquad\text{and}\qquad12
\]

with missing support `3`; the endpoint triangles are two copies each of

\[
034
\qquad\text{and}\qquad123.
\]

No smaller simple cubic graph supports this four-endpoint pattern.

---

## 5. Every small all-bad incidence has one-switch rescue

For every one of the

\[
720+240=960
\]

all-bad incidences, compute its complete labelled root-flow Kempe component.

### Cube

The cube root-flow Kempe graph is connected with `3960` vertices. Every one of its `720` all-bad incidences is distance exactly one from a flow in which the marked pair lies in `B`.

### Wagner graph

All `240` all-bad incidences lie in the Kempe component of size `1380`. Every one is distance exactly one from a `B`-flow for the same marked edge pair.

Thus:

### Theorem 5.1 — small all-bad rescue

Every all-bad incidence through order eight has a crossed support-pair component containing exactly one marked edge. Switching that component sends the marked roots to a distinct intersecting pair.

In particular, none is a full-channel lock.

---

## 6. Why this is the correct remaining structural target

The local borrowing dichotomy says:

- if at least one endpoint is not missing-index bad, the inverse weld rootifies by a direct alternative insertion;
- if all four are bad, both marked edges are equal-face dipoles.

The full-channel theorem says:

- if one crossed channel separates the marked edges, horizontal rescue gives the cap lift;
- only four simultaneous crossed locks survive.

The finite census shows that these two worst conditions do not coexist at small order.

Hence the remaining periodic endpoint must satisfy the rigid conjunction:

\[
\boxed{
\begin{array}{c}
\text{two complementary equal-face marked dipoles}\
+\\
\text{all four crossed channels connect them}\
+\\
\text{one fixed oriented cap route}.
\end{array}}
\]

This is substantially narrower than an arbitrary co-root track.

---

## 7. Exact next theorem

### Target 7.1 — all-bad locked-pair structural escape

Let a connected loopless bridgeless cubic root flow contain two marked edges with disjoint roots `a,b` and common missing support `i`. Assume:

1. both endpoints of the `a`-edge have support triangle `a union {i}`;
2. both endpoints of the `b`-edge have support triangle `b union {i}`;
3. every crossed channel `H_(xy)`, `x in a`, `y in b`, contains both marked edges in one component;
4. the four components carry the same oriented cap route.

Prove one of:

1. a two-, three-, or four-edge separator;
2. a strictly smaller all-bad locked carrier after equal-face peeling;
3. a componentwise support switch or finite switch sequence entering `B`;
4. a bounded identity/cube/Wagner-type carrier with an explicit root-valued cap replacement;
5. contradiction with the oriented projectivity character.

A proof of Target 7.1 discharges the sole periodic outer endpoint in `CONTEXTUAL_TRANSFER_REPAIR_FRONTIER_V2.md`.

---

## 8. Assurance boundary

### Exact here

- complete labelled root-flow enumeration through order eight;
- exact all-bad and full-lock definitions;
- zero intersection of the two conditions in that range;
- identification of cube and Wagner as the first all-bad graph classes;
- one-switch `B` rescue for all `960` all-bad incidences;
- isolation of Target 7.1.

### Not proved

- general incompatibility of all-bad and full-lock;
- separator extraction or peeling beyond order eight;
- periodic outer-endpoint discharge;
- complete contextual transfer, cap restoration, or global five-support closure;
- PDL reconstruction, independent audit, Lean verification, manuscript integration, release, arXiv, DOI, peer review, or publication.
