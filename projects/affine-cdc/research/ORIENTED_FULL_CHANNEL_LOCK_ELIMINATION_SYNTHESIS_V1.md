# Every blocked inverse-dipole cap is eliminated

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `9dee8de20865d3e7892dcb705446372b34e79788`.

**Parents:**

- `ARBITRARY_EDGE_THREE_RECONNECTION_CATEGORY_V1.md`;
- `THREE_RECONNECTION_FIXED_ROUTE_REDUCTION_V1.md`;
- `INVERSE_DIPOLE_KEMPE_RESCUE_V1.md`;
- `ORIENTED_CHANNEL_LOCK_BOUNDARY_CALIBRATION_V1.md`;
- `CONSTANT_PIVOT_ORIENTED_ROOT_SECTION_V1.md`;
- `EQUALITY_LOCK_GLOBAL_PACHNER_POTENTIAL_V1.md`;
- `DDD_LOCK_GLOBAL_PACHNER_POTENTIAL_V1.md`;
- `ROUTE_CHANGING_MATCHING_FLIP_CAP_ESCAPE_V1.md`;
- `BOUNDED_DIRECT_PAIRING_CAP_TERMINAL_V1.md`;
- `PACHNER_HISTORY_FIRST_FAILURE_ONE_EDGE_ATOM_V1.md`;
- `CONTEXTUAL_TRANSFER_TARGET_ORDER_CORRECTION_V1.md`;
- `PACHNER_FIRST_FAILURE_CRITICAL_OVERLAP_V1.md`;
- `FIVE_LEAF_PACHNER_PENTAGON_ROOT_INTERVAL_V1.md`;
- `PTOLEMY_CONTEXTUAL_COHERENCE_SCOPE_CORRECTION_V1.md`;
- `PTOLEMY_EVEN_TRACK_ROOT_TUBE_FILLING_V1.md`;
- the physical Type-T and Type-H commutation eliminations;
- cyclic three-/four-cut gluing and category-safe root surgery.

**Status:** exact synthesis theorem, using the standard Ptolemy-groupoid input already isolated in the contextual-transfer dossier. Let `P` be the complementary four-pole of one deleted cubic edge and let `C_i` be the original two-vertex cap. If all three direct reconnection closures are smaller soluble bridgeless inputs, then `P` must have a root-valued boundary state in the cap profile `K_i`. Equivalently, the original cap always lifts root-valuedly unless the graph has already exited through a proved separator or bounded category branch. Equality and DDD full-channel locks are therefore not residual inverse-dipole obstructions.

**Not implied:** the global five-support theorem before the final minimal-counterexample packaging and independent audit, canonical acceptance, Lean verification, manuscript integration, release, publication, or DOI status.

---

## 1. Four-pole and cap profiles

Let `P` be an ordered cubic four-pole with terminal matchings

\[
M_i,M_j,M_k.
\]

The three zero-vertex direct reconnections have exact profiles

\[
J_r=\{A,B_r,C_r\}
\qquad(r=i,j,k).
\]

Let `C_i` be the original two-vertex cap whose two terminal blocks define `M_i`. Its exact root profile is

\[
K_i=\{B_j,D_j:j\ne i\}.
\]

Assume the three reconnection closures are connected bridgeless smaller graphs. By minimality, each has a root-valued `E_5` flow. Cutting the two matching edges gives

\[
\boxed{
\Sigma(P)\cap J_r\ne\varnothing
\qquad(r=i,j,k).}
\]

We prove

\[
\boxed{\Sigma(P)\cap K_i\ne\varnothing.}
\]

---

## 2. Contradictory blocked-cap hypothesis

Assume

\[
\Sigma(P)\cap K_i=\varnothing.
\]

The exact three-reconnection fixed-route theorem then gives only two possible complete physical profiles:

\[
\boxed{
\Sigma(P)=J_i
\quad\text{or}\quad
\Sigma(P)=J_i\cup L_i,}
\]

where

\[
L_i=\{C_j,D_i,C_k\}.
\]

Moreover every relevant complementary support-pair challenge in every realised state has the same physical route

\[
\boxed{M_i.}
\]

Thus continued cap blocking supplies a globally fixed ordered route, not merely a coefficient restriction.

---

## 3. One cross reconnection and the inverse-lift trichotomy

Choose one cross reconnection, say `M_j`, and one root-valued flow on the closed graph

\[
G_j=P\cup M_j.
\]

Let the two reconnection edges receive roots

\[
p,q\in R_5.
\]

Reinserting the original cap forces the central value

\[
r=p+q.
\]

Exactly one of:

1. **root case:** `p,q` are distinct and intersecting;
2. **equality case:** `p=q` and `r=0`;
3. **DDD case:** `p,q` are disjoint and `r` is one co-root.

In the root case, the cap already lifts, contradicting the blocked-cap assumption. Hence only equality or DDD may remain.

---

## 4. Horizontal rescue before a lock

### Equality

If one of the six repair-channel Kempe systems separates the two marked reconnection edges, switch the component containing exactly one marked edge. Their values become distinct intersecting roots and the cap lifts.

### DDD

If one of the four crossed repair-channel systems separates the marked edges, the same one-component switch makes the two values intersect and the cap lifts.

Therefore a surviving failure is a full-channel lock:

- six-channel `K_(2,3)` in equality;
- four-channel `K_(2,2)` in DDD.

By the fixed-route conclusion of Section 2, every channel cuts open with the ordered cap route `M_i`. The deleted cap vertices distinguish its two blocks. Hence the residual is one **oriented** full-channel lock.

The DDD orientation cocycle restricts to a coboundary on this oriented transport subgroup. No independent orientation bit remains.

---

## 5. Equality current-flow descent

In the equality branch, cutting the marked equal-root edges gives a connected root-labelled four-pole with boundary

\[
r,r,r,r.
\]

The full-ten-triangle equality theorem supplies a globally monotone potential

\[
\mathcal P_{\mathrm{eq}}=(E,\Phi,|V|).
\]

Every nonempty equality carrier has either:

1. an equal-face cancellation;
2. a root Pachner flip strictly lowering `(E,Phi)`;
3. a category/separator exit.

Repeated descent terminates in one of:

- a route-changing matching flip;
- a separator or bounded degeneration;
- a zero-vertex direct-pairing terminal.

There is no equality local minimum and no adaptive projection cycle.

---

## 6. DDD current-flow descent

In the DDD branch, the four-pole boundary is, after support relabelling,

\[
12,12,34,34.
\]

The full-ten-triangle DDD theorem supplies the monotone potential

\[
\mathcal P_{\mathrm{DDD}}=(\Omega,|V|).
\]

Every nonempty DDD carrier has either:

1. an equal-face cancellation;
2. an `Omega`-lowering root Pachner flip;
3. a route/category/separator exit.

Repeated descent terminates at a matching flip, a separator/degeneration, or a bounded direct-pairing carrier. No unbounded DDD source topology survives.

---

## 7. Terminal and route-changing exits

### Matching flip

Under continued cap blocking, every relevant route is `M_i`. A physically realised route `M_j` or `M_k` contradicts that fixed-route theorem. Therefore

\[
\boxed{
\text{route-changing root state}
\Longrightarrow
\Sigma(P)\cap K_i\ne\varnothing.}
\]

The cap glues root-valuedly.

### Zero-vertex terminal

A zero-vertex four-pole is one terminal matching.

- If it equals `M_i`, closing by the cap gives two loops joined by a bridge, hence category exit.
- If it is `M_j` or `M_k`, the closure is the two-vertex theta multigraph and has the explicit root flow
  \[
  12,13,23.
  \]

Thus the bounded terminal is never a counterexample.

### Separator/category exit

Every failed root surgery records a two-, three-, or four-edge separator, loop/parallel degeneration, or acyclic appendage in the pre-move graph. These branches are consumed by the established gluing/base theorems.

---

## 8. Cover-independent inverse transfer

The forward equality/DDD descent constructs a finite history of root Pachner flips and equal-face cancellations. The root state at the terminal need not be the forward current flow, so it must be transferred back cover-independently.

The contextual-transfer programme gives the exact mechanism.

1. Reverse the history while root admissibility holds.
2. The first failed step creates exactly one zero or co-root edge atom.
3. In a pure same-order flip block, a zero atom has an immediate alternative root resolution.
4. A persistent co-root atom is transported through critical overlaps as one nonbranching forced Petersen backbone.
5. Odd closed tracks have nontrivial oriented resolution parity and cannot close.
6. Even `C6` and `C8` tracks have explicit root-valued annular tube fillings preserving every exterior side root and the ordered cap route.
7. A failure behind an actual cancellation lies in a cap-context graph with at least two fewer vertices.

Hence the inverse transfer is well founded. It reaches:

- a root-valued state on the original four-pole/cap;
- a route-changing cap lift;
- a separator/category exit;
- or the bounded terminal already consumed in Section 7.

No equality/DDD transfer loop survives.

---

## 9. Main cap-lift theorem

### Theorem 9.1 — full-channel lock elimination

Let `P` be an ordered cubic four-pole and `C_i` one two-vertex cap. Assume all three direct reconnection closures of `P` are smaller connected bridgeless cubic graphs with root-valued `E_5` flows.

Then

\[
\boxed{
\Sigma(P)\cap K_i\ne\varnothing.}
\]

Equivalently, `P` and the original cap glue to a root-valued `E_5` flow.

### Proof

Assume the cap blocked. Sections 2--4 reduce every chosen cross-cover failure to one oriented equality or DDD full-channel lock. Sections 5--7 give finite current-flow descent to cap lift, category exit, or a soluble bounded terminal. Section 8 transfers the terminal state back through the complete history without introducing a residual loop. Every outcome contradicts continued blocked-cap membership in a prime counterexample. ∎

### Corollary 9.2 — arbitrary-edge inverse-dipole lift

Let `uv` be an edge of a prime vertex-minimal counterexample. The simultaneous category theorem makes all three reconnection closures smaller soluble inputs. Applying Theorem 9.1 to the complementary four-pole gives a root-valued flow on the original graph.

Thus no prime vertex-minimal counterexample survives one arbitrary-edge cancellation.

---

## 10. Dependency and noncircularity audit

The proof order is:

1. cut/base reductions;
2. all-three-reconnection category theorem;
3. smaller-graph root covers by vertex minimality;
4. finite three-reconnection profile forcing;
5. horizontal equality/DDD rescue;
6. current-flow Pachner descent;
7. bounded terminal/matching-flip disposition;
8. cover-independent inverse transfer;
9. original-cap lift.

The current-flow descent does not invoke the global theorem. It uses only local root surgeries and finite potentials. Contextual recursion behind a cancellation invokes strictly smaller cap-target order; same-order transfer is resolved by finite critical-pair/backbone/tube theorems. Cut branches invoke only previously established gluing theorems.

Therefore Theorem 9.1 does not use its own conclusion.

---

## 11. Trust boundary

### Exact here

- three-reconnection profile hypotheses from all smaller closures;
- fixed-route consequence of cap blocking;
- complete root/equality/DDD inverse-lift table;
- horizontal rescue and oriented lock calibration;
- finite monotone equality and DDD current-flow descents;
- route-changing cap escape;
- direct-pairing terminal disposition;
- cover-independent contextual inverse transfer;
- complete full-channel lock elimination;
- arbitrary-edge cap lift in a prime minimal counterexample.

### External/topological input

The same-order contextual-transfer theorem uses the standard presentation of the marked-surface Ptolemy groupoid by involution, far commutativity, and pentagon relations, together with the explicit root lift and tube-filling calculations recorded in the branch.

### Still open

- final global minimal-counterexample theorem statement and base/cut packaging;
- independent mathematical audit of this synthesis and its imported contextual-transfer theorem;
- canonical acceptance, Lean verification, manuscript integration, release, publication;
- the global five-support theorem is not claimed in this dossier before the final packaging step.
