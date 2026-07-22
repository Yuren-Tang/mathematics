# DDD four-poles admit a globally monotone Pachner descent

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent:** `0e7f405476311e406f0c152a7d7e13096b0631e6`.  

**Parents:**

- `ROOT_FLOW_TRIANGLE_COMPLEX_PACHNER_V1.md`;
- `PACHNER_HISTORY_FIRST_FAILURE_ONE_EDGE_ATOM_V1.md`;
- `ORIENTED_CHANNEL_LOCK_BOUNDARY_CALIBRATION_V1.md`;
- `INVERSE_DIPOLE_KEMPE_RESCUE_V1.md`;
- the category-safe root NNI and equal-face cancellation lemmas.

**Status:** exact full-ten-triangle descent theorem for the disjoint-root/DDD four-port boundary. After normalising the four boundary roots to `12,12,34,34`, one explicit nonnegative triangle weight orients all fifteen tetrahedral flip involutions without ties. Every nonempty connected root-labelled cubic four-pole with that boundary contains either an equal-face cancellation or a strictly weight-lowering root Pachner flip. Hence an oriented DDD full-channel lock has no unbounded current-flow local minimum and admits finite root-surgery reduction to a route change, separator/category exit, or bounded direct-pairing terminal.

**Not implied:** cover-independent inverse transfer through the reduction history, elimination of a same-order DDD first failure produced while reversing a Pachner flip, proof that every bounded DDD terminal lifts the original cap, global proof-DAG closure, canonical acceptance, Lean verification, manuscript integration, release, publication, or the global five-support theorem.

---

## 1. DDD boundary normalisation

Let the two marked reconnection edges carry disjoint roots. By `S_5` symmetry normalise them to

\[
p=12,
\qquad
q=34.
\]

Cutting the marked edges gives a four-pole whose ordered boundary multiset is

\[
\boxed{12,12,34,34.}
\]

The exact terminal ordering and cap-oriented route are retained, but the local descent theorem below uses only the root labels and the fact that no other root occurs on the boundary.

Every cubic source vertex is one of the ten support triangles

\[
\binom{[5]}3.
\]

Distinct adjacent triangles admit the unique root-valued tetrahedral `2--2` Pachner flip; equal adjacent triangles admit two-face cancellation.

---

## 2. One explicit DDD triangle weight

Define

\[
\omega:\binom{[5]}3\to\mathbf Z_{\ge0}
\]

by

\[
\boxed{
\begin{array}{c|cccccccccc}
T&123&124&125&134&135&145&234&235&245&345\\
\hline
\omega(T)&3&0&1&3&0&1&1&3&3&3.
\end{array}}
\]

For a root-labelled source region `R`, put

\[
\boxed{
\Omega(R)=\sum_{v\in V(R)}\omega(\Delta_v).}
\]

For an adjacent distinct pair `T,U`, let `T',U'` be the opposite pair in the same four-support tetrahedron. Orient the root Pachner flip from `T,U` to `T',U'` exactly when

\[
\omega(T')+\omega(U')
<
\omega(T)+\omega(U).
\]

### Theorem 2.1 — exact `15/15` orientation

Among the thirty unordered adjacent distinct triangle pairs:

\[
\boxed{15\text{ admit a strictly }\Omega\text{-decreasing flip},}
\]

\[
\boxed{15\text{ lie on the lower side of their flip},}
\]

and there is no tie.

An independent exact Wolfram enumeration verifies the census

\[
30=15+15+0.
\]

---

## 3. Complete nondecreasing adjacency table

Assume an adjacent distinct pair does not admit an `Omega`-decreasing flip. The complete list, grouped by the common root label, is

\[
\boxed{
\begin{array}{c|l}
\text{root}&\text{nondecreasing adjacent pairs}\\
\hline
12&123\!-\!124,\ 124\!-\!125\\
13&123\!-\!135,\ 134\!-\!135\\
14&124\!-\!134,\ 124\!-\!145\\
15&125\!-\!135,\ 125\!-\!145,\ 135\!-\!145\\
23&234\!-\!235\\
24&124\!-\!234,\ 234\!-\!245\\
25&\varnothing\\
34&234\!-\!345\\
35&135\!-\!235,\ 135\!-\!345\\
45&\varnothing.
\end{array}}
\]

Equal adjacent types are omitted because they admit two-face cancellation.

This table is the complete finite certificate needed for the human exclusion proof.

---

## 4. No nonempty DDD local minimum

### Theorem 4.1 — full ten-triangle DDD descent

Let `R` be a nonempty connected cubic multipole with a root-valued `E_5` flow such that its only boundary semiedges have root multiset

\[
12,12,34,34.
\]

Then `R` contains at least one of:

1. an edge joining equal support triangles, hence an equal-face cancellation;
2. an adjacent distinct pair whose root Pachner flip strictly lowers `Omega`.

### Proof

Assume neither move exists. Every internal edge must therefore use one of the nondecreasing pairs in Section 3.

#### Step 1 — eliminate the `25` and `45` sectors

The `25` row is empty and root `25` is not a boundary label. Therefore no triangle containing root `25` can occur:

\[
125,\ 235,\ 245
\]

are absent.

The `45` row is empty and root `45` is not a boundary label. Hence

\[
145,\ 245,\ 345
\]

are absent.

Thus

\[
125,145,235,245,345
\]

are all excluded.

#### Step 2 — eliminate the `23` sector

The only nondecreasing `23` pair is

\[
234-235.
\]

Since `235` is absent, neither `123` nor `234` can satisfy an internal `23` incidence. Root `23` is not a boundary label. Therefore

\[
123,\ 234
\]

are absent.

#### Step 3 — eliminate the `35` and `13` sectors

The only nondecreasing `35` pairs use

\[
135
\]

with `235` or `345`, both already absent. Hence `135` is absent.

The remaining triangle `134` has an internal `13` incidence. The nondecreasing `13` pairs are

\[
123-135,
\qquad
134-135.
\]

Both possible neighbours are absent, so `134` is absent.

#### Step 4 — eliminate the last active type

Only `124` remains. Its nonboundary incidences have roots `14` and `24`.

- the nondecreasing `14` neighbours of `124` are `134` and `145`;
- the nondecreasing `24` neighbour alternatives use `234`.

All are absent. Hence `124` is absent.

No source vertex remains, contradicting nonemptiness and the four prescribed boundary semiedges. ∎

---

## 5. Global DDD surgery measure

Define

\[
\boxed{
\mathcal P_{\mathrm{DDD}}(R)
=igl(\Omega(R),|V(R)|\bigr)}
\]

lexicographically.

### Theorem 5.1 — every selected move lowers `P_DDD`

1. A selected root Pachner flip leaves vertex count unchanged and strictly lowers `Omega`.
2. An equal-face cancellation removes two vertices. Since `omega` is nonnegative, it either lowers `Omega` or preserves `Omega` and lowers `|V|` by two. In particular the zero-weight types `124` and `135` are still strictly reduced by the second coordinate.

Thus an adaptive DDD root-surgery sequence cannot cycle.

### Corollary 5.2 — finite current-flow reduction

Repeatedly apply Theorem 4.1 while the graph remains in the connected bridgeless cubic category. Because `P_DDD` is well founded, after finitely many steps one obtains one of:

1. a local root surgery that changes the cap-oriented route/profile;
2. a two-, three-, or four-edge separator;
3. a bounded loop, parallel-edge, or acyclic degeneration;
4. a zero-vertex four-port direct matching;
5. a bounded residual carrier at which the marked DDD route can be inspected explicitly.

No unbounded root-labelled DDD carrier survives merely through local Pachner irreducibility.

---

## 6. Interaction with horizontal DDD rescue

The inverse-dipole rescue theorem gives the first dichotomy before root surgery:

1. one cross-channel Kempe system separates the marked edges, giving an immediate root lift;
2. all four cross channels lock the edges together, giving the oriented DDD full-channel lock.

The present theorem applies to the second branch. It does not by itself produce the separating Kempe component, but it proves that the locked source region has a finite monotone root-surgery descent.

If a selected Pachner/cancellation move changes one of the four physical channel routes, the fixed-route outer profile escapes. If all routes are retained, the process reaches a bounded direct-pairing carrier or a category exit.

Therefore the remaining DDD issue is transfer through a finite history, not existence of a new unbounded DDD topology.

---

## 7. Relation to the earlier Petersen/backbone programme

The forced-backbone and Petersen-cycle dossiers reduced an oriented DDD lock to:

- constant-pivot rank-two runs;
- Type-T backtracks;
- one binary resolution local system;
- bounded identity-hexagon or DDD-octagon carriers.

The current theorem is an independent source-level reduction. It does not use a pivot word and permits all ten root triangles. Its conclusion is compatible with the previous finite alphabet:

\[
\boxed{
\text{no unbounded DDD local minimum}
\quad+\quad
\text{no unbounded Petersen obstruction species}.}
\]

The two routes now meet at the same bounded transfer frontier.

---

## 8. Revised DDD frontier

### Closed here

- an explicit global triangle potential for the disjoint-root boundary;
- exact `15/15` orientation with no ties;
- complete nondecreasing adjacency table;
- exclusion of every nonempty ten-triangle local minimum;
- finite current-flow descent of every oriented DDD carrier;
- exclusion of adaptive Pachner cycles and unbounded DDD source topology.

### Still open

- cover-independent inverse transfer through the finite DDD history;
- disposition of a same-order co-root first failure when reversing a root Pachner flip;
- transfer from the bounded direct-pairing DDD terminal;
- integration with equality recursion and horizontal route bookkeeping;
- final proof-DAG assembly;
- canonical acceptance, independent audit, Lean verification, manuscript integration, release, publication;
- the global five-support theorem.