# A route change on a surgery descendant is a cap-compatible terminal, not yet an original-profile state

## Research dossier v1 — scope correction and repaired interface

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `e2b22ad3a50f023d32ff7bc545ee57a0535286d1`.

**Parents:**

- `THREE_RECONNECTION_FIXED_ROUTE_REDUCTION_V1.md`;
- `ROUTE_CHANGING_MATCHING_FLIP_CAP_ESCAPE_V1.md`;
- `EQUALITY_LOCK_GLOBAL_PACHNER_POTENTIAL_V1.md`;
- `DDD_LOCK_GLOBAL_PACHNER_POTENTIAL_V1.md`;
- `PTOLEMY_EVEN_TRACK_ROOT_TUBE_FILLING_V1.md`;
- `AUTHORITATIVE_CONTEXTUAL_TRANSFER_CHAIN_V1.md`;
- `ORIENTED_FULL_CHANNEL_LOCK_ELIMINATION_SYNTHESIS_V1.md`.

**Corrects:** any reading of `ROUTE_CHANGING_MATCHING_FLIP_CAP_ESCAPE_V1.md` or Sections 7--9 of `ORIENTED_FULL_CHANNEL_LOCK_ELIMINATION_SYNTHESIS_V1.md` which applies the original four-pole profile `Sigma(P_0)` directly to a route-changing root state living on a surgery descendant `P_t`.

**Status:** exact repaired route-change interface. Before the first route-changing Kempe/matching event, internal root Pachner flips and equal-face cancellations preserve the complete ordered four-root boundary, so the descendant still carries the same support-unordered blocked-sector state `sigma in J_i` or `sigma in J_i union L_i`. The exact ten-state route table shows that any alternative route `M_j` or `M_k` from either outer fixed-route component lands in the cap profile `K_i`. Hence the descendant `P_t` has a cap-compatible root state. This is then transferred through the finite surgery history to the original four-pole `P_0` by the contextual inverse-transfer theorem. Only after this transfer may one conclude `Sigma(P_0) cap K_i != empty` and glue the original cap.

**Not implied:** independent verification of the parent route table or contextual-transfer theorem, canonical acceptance, Lean verification, manuscript integration, release, publication, or DOI status.

---

## 1. Original and descendant four-poles

Let `P_0` be the ordered four-pole obtained from the original graph by deleting one two-vertex cap `cap_i`. Its three terminal matchings are

\[
M_i,M_j,M_k.
\]

Assume all three zero-vertex reconnection closures are smaller soluble inputs and suppose, for contradiction, that the original cap is blocked:

\[
\Sigma(P_0)\cap K_i=\varnothing.
\]

The three-reconnection theorem gives

\[
\boxed{
\Sigma(P_0)=J_i
\quad\text{or}\quad
\Sigma(P_0)=J_i\cup L_i.}
\]

Every complementary support-pair challenge in every realised state of `P_0` then has the unique physical route `M_i`.

Choose one root-valued flow on a cross reconnection closure of `P_0` and perform a finite sequence of internal root Pachner flips and equal-face cancellations selected by the equality or DDD descent. Denote the successive ordered four-poles by

\[
P_0,P_1,\ldots,P_t.
\]

The graphs `P_s` need not be isomorphic. In particular,

\[
\Sigma(P_s)
\]

is not the same set as `Sigma(P_0)` merely because the outer incidences agree.

---

## 2. What internal root surgery preserves

Every root Pachner flip and equal-face cancellation in the forward descent is internal to the four-pole. It preserves:

1. the four ordered terminal incidences;
2. the root label on each terminal semiedge;
3. hence the complete ordered four-root boundary word;
4. hence its support-unordered ten-state class.

Let

\[
\sigma\in\mathcal S
\]

be the initial boundary state obtained by restricting the chosen reconnection cover to `P_0`. Under the blocked-cap hypothesis,

\[
\boxed{
\sigma\in J_i
\quad\text{or}\quad
\sigma\in L_i.}
\]

Before any boundary-changing Kempe switch, every descendant `P_s` carries the same boundary state `sigma`.

The internal surgery history may change physical linkage and therefore may change which terminal matching is realised by a given complementary support-pair challenge. That route datum is not determined solely by `sigma`.

---

## 3. Exact route table from the outer components

For fixed matching `M_i`, the ten-state route graph decomposes as

\[
\boxed{
J_i\sqcup K_i\sqcup L_i
\cong
P_3\sqcup C_4\sqcup P_3.}
\]

The route `M_i` preserves each of the two outer paths `J_i,L_i`. The exact challenge rows used in the three-reconnection classification give the stronger cross-route statement.

### Theorem 3.1 — every alternative route enters the cap profile

Let

\[
\sigma\in J_i\cup L_i
\]

and let one complementary support-pair challenge be realised with route `M_j` or `M_k`, where `{i,j,k}={0,1,2}`. Switching one of its two terminal path components produces a root-valued boundary state

\[
\tau\in K_i.
\]

### Proof

It is enough to take `i=0`. The two outer components are

\[
J_0=\{A,B_0,C_0\},
\qquad
L_0=\{C_1,D_0,C_2\},
\]

and

\[
K_0=\{B_1,B_2,D_1,D_2\}.
\]

The exact challenge rows are:

- at `A`, the three route targets are `(B_0,B_1,B_2)`;
- at `B_0`, the two rows are `(C_0,D_2,D_1)` and `(A,B_2,B_1)`;
- at `C_0`, the row is `(B_0,D_1,D_2)`;
- at `C_1`, the row is `(D_0,B_1,D_2)`;
- at `C_2`, the row is `(D_0,D_1,B_2)`;
- at `D_0`, the two rows are `(C_2,B_2,D_1)` and `(C_1,D_2,B_1)`.

In every row the `M_0` entry stays in the relevant outer component, while both other entries belong to `K_0`. Matching-index symmetry gives the result for all `i`. ∎

Thus a first physically realised route change away from `M_i` produces a cap-compatible boundary state on the current descendant.

---

## 4. The scope error in the immediate-lift reading

Suppose the first route-changing event occurs on `P_t` and gives

\[
\tau\in K_i.
\]

Then

\[
\boxed{
\tau\in\Sigma(P_t)\cap K_i.}
\]

This proves that `P_t` glues root-valuedly to `cap_i`.

It does **not** by itself prove

\[
\tau\in\Sigma(P_0),
\]

because `P_t` was obtained from `P_0` by graph-changing Pachner moves and possibly cancellations. The fixed-route theorem for the complete profile of `P_0` cannot be applied directly to a state realised only on `P_t`.

### Proposition 4.1 — corrected route-change conclusion

A route-changing event on a nontrivial surgery descendant gives a cap-compatible **terminal state for inverse transfer**, not an immediate original-profile intersection.

The old immediate conclusion remains valid only when the event occurs on `P_0` itself, before any graph-changing surgery.

---

## 5. Contextual return to the original four-pole

The forward history

\[
P_0\longrightarrow P_1\longrightarrow\cdots\longrightarrow P_t
\]

is a finite sequence of root Pachner flips and equal-face cancellations. The cap-compatible root state

\[
\tau\in\Sigma(P_t)\cap K_i
\]

is exactly an admissible terminal input for the contextual inverse-transfer theorem.

Apply that theorem while preserving:

- the ordered four terminal incidences;
- the complete terminal root word;
- the cap index `i`;
- all category exits;
- strict recursion only after an actual cancellation.

The transfer gives one of:

1. a root-valued state on `P_0` with boundary in `K_i`;
2. another cap-profile lift encountered during transfer;
3. a separator/category reduction;
4. a bounded direct-pairing completion.

The last three are already established exits. In the first case,

\[
\boxed{
\Sigma(P_0)\cap K_i\ne\varnothing.}
\]

The original cap then glues root-valuedly.

### Theorem 5.1 — route-change terminal transfer

Every first route change during an equality or DDD forward surgery history yields, after contextual inverse transfer, an original-cap lift or an established category/bounded exit.

---

## 6. Corrected full-channel order

The route-changing branch of the full-channel proof must be read in this order:

\[
\begin{aligned}
&\text{blocked original cap on }P_0\\
&\Downarrow\\
&\sigma\in J_i\cup L_i,\quad\text{initial route }M_i\\
&\Downarrow\quad\text{internal root surgery, boundary fixed}\\
&\text{first alternative route }M_j\text{ or }M_k\text{ on }P_t\\
&\Downarrow\quad\text{exact route table}\\
&\tau\in\Sigma(P_t)\cap K_i\\
&\Downarrow\quad\text{contextual inverse transfer}\\
&\Sigma(P_0)\cap K_i\ne\varnothing
\quad\text{or established exit}. 
\end{aligned}
\]

The route table supplies cap compatibility at the descendant stage. The contextual theorem supplies return to the original stage. Neither theorem replaces the other.

---

## 7. Relation to horizontal rescue

Horizontal Kempe rescue in the initial reconnection cover occurs on `P_0` before any graph-changing root surgery. In that special case the rescued intersecting-root pair expands the original cap immediately.

The correction here concerns only route changes produced **after** the forward surgery history has begun.

Thus:

- initial horizontal rescue remains an immediate original-cap lift;
- descendant route change is a cap-compatible terminal followed by contextual return.

---

## 8. Consequence for the main cap-lift theorem

Replace the route-changing paragraph of `ORIENTED_FULL_CHANNEL_LOCK_ELIMINATION_SYNTHESIS_V1.md` by the following exact statement:

> If the forward equality/DDD descent first changes the forced route, the exact ten-state table produces a `K_i` boundary state on the current descendant four-pole. Treat this as a cap-compatible terminal root state. The contextual inverse-transfer theorem returns it through the complete surgery history to the original four-pole, or exits through a proved separator/category/bounded branch.

With this replacement, the full-channel conclusion

\[
\Sigma(P_0)\cap K_i\ne\varnothing
\]

is noncircular and does not identify profiles of nonisomorphic surgery stages.

---

## 9. Trust boundary

### Exact here

- distinction between the original four-pole profile and descendant profiles;
- preservation of the complete boundary state before the first route-changing switch;
- exact route-table proof that every alternative route from `J_i union L_i` lands in `K_i`;
- classification of the route-changing descendant state as cap-compatible;
- contextual return of that state to the original cap context;
- correction of the full-channel proof order;
- preservation of immediate horizontal rescue at the initial stage.

### Imported authorial mathematics

- three-reconnection fixed-route classification;
- exact physical route table;
- equality/DDD forward descent;
- contextual inverse transfer;
- category and direct-terminal exits.

### Still outside this checkpoint

- proof-development expansion or independent verification of parent theorems;
- curation or canonical movement;
- Lean verification;
- manuscript integration;
- release, arXiv, DOI, peer review, or publication.
