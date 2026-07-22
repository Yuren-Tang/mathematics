# A route-changing matching flip forces cap-profile escape

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `8527bd04cebd64419f5572e8a6754d52a99ec054`.

**Parents:**

- `THREE_RECONNECTION_FIXED_ROUTE_REDUCTION_V1.md`;
- `FOUR_POLE_CAP_LIBRARY_TEN_STATE_PROFILES_V1.md`;
- `EQUALITY_LOCK_TWO_BOUNDARY_ANNULUS_REDUCTION_V1.md`;
- `DDD_LOCK_GLOBAL_PACHNER_POTENTIAL_V1.md`;
- the exact ten-state route table.

**Status:** exact profile-level disposition of every bounded matching flip produced by equality/DDD Tait or Pachner descent. Under the three-reconnection hypotheses, blocking one cap profile `K_i` forces the complete physical four-pole profile to be `J_i` or `J_i union L_i`, and every challenge route to be the single matching `M_i`. Therefore any physically realised route change to `M_j` or `M_k` is incompatible with continued cap blocking. The complete profile must meet `K_i`, so the original cap glues root-valuedly.

**Not implied:** that every surgery history necessarily produces a matching flip, inverse transfer when all routes remain fixed, outer-route preservation after recursive first-failure resolution, global proof-DAG closure, canonical acceptance, Lean verification, manuscript integration, release, publication, or the global five-support theorem.

---

## 1. Fixed blocked cap sector

Let `P` be an ordered cubic four-pole and let

\[
M_0,M_1,M_2
\]

be its three terminal matchings.

For each index `r`, the zero-vertex direct reconnection has exact profile

\[
\boxed{J_r=\{A,B_r,C_r\}.}
\]

Fix one two-vertex cap `C_i`, whose exact profile is

\[
\boxed{K_i=\{B_j,D_j:j\ne i\}.}
\]

Assume all three zero-vertex reconnection graphs are valid smaller soluble inputs. Then the complete physical profile satisfies

\[
\Sigma(P)\cap J_r\ne\varnothing
\qquad(r=0,1,2).
\]

Assume for contradiction that the cap remains blocked:

\[
\Sigma(P)\cap K_i=\varnothing.
\]

The three-reconnection classification gives exactly:

\[
\boxed{
\Sigma(P)=J_i
\quad\text{or}\quad
\Sigma(P)=J_i\cup L_i,}
\]

where

\[
L_i=\{C_j,D_i,C_k\}
\qquad
(\{i,j,k\}=\{0,1,2\}).
\]

Moreover every complementary support-pair challenge in every state of either profile has the unique physical route

\[
\boxed{M_i.}
\]

---

## 2. Matching-flip event

A **route-changing matching flip** is any root-valued physical reconfiguration, dipole cancellation, Tait-response splice, or Pachner-history stage for which one relevant four-terminal challenge has route

\[
M_j
\quad\text{or}\quad
M_k
\]

instead of the previously forced route `M_i`.

The event may arise as:

- the Type-F complementary matching flip of a coloured Tait dipole;
- a nonlaminar component toggle;
- a root Pachner move whose scalar challenge reconnects the terminal paths;
- a crossed private-edge surgery;
- a route-changing bounded return cell.

Only the physical route change and root admissibility are used below.

---

## 3. Cap escape theorem

### Theorem 3.1 — matching flip contradicts continued blocking

Under the hypotheses of Section 1, if one physically realised challenge route is `M_j` or `M_k`, then

\[
\boxed{
\Sigma(P)\cap K_i\ne\varnothing.}
\]

### Proof

Suppose instead that the cap remains blocked. Then the complete Kempe-closed profile of `P` satisfies all hypotheses of the exact three-reconnection cap-blocking classification. Its fixed-route conclusion says that **every** relevant challenge route in **every** realised state is `M_i`.

This contradicts the physically realised route `M_j` or `M_k`.

Therefore cap blocking is impossible, and the complete profile meets `K_i`. ∎

### Corollary 3.2 — root-valued cap lift

Choose a boundary state

\[
S\in\Sigma(P)\cap K_i.
\]

By definition of the complete profiles, `S` is realised by a root flow on `P` and by a root flow on the cap `C_i`. Gluing the two flows along the four equal terminal root values gives a root-valued flow on the original closed graph.

Thus

\[
\boxed{
\text{route-changing matching flip}
\Longrightarrow
\text{successful original-cap lift}.}
\]

---

## 4. No dependence on the flip source

The theorem does not require the matching flip to be one particular local state-table transition. It uses the completeness of the physical profile.

Hence it applies uniformly to:

1. equality annulus Type-F flips;
2. negative-Euler Tait dipole flips;
3. DDD Pachner route changes;
4. Type-T/Type-H nonpolicy routes;
5. pair-changing scalar-component toggles;
6. bounded six-output return-cell escapes.

If the event is root-valued and changes one relevant route away from `M_i`, the cap glues.

---

## 5. Category boundary

The three-reconnection hypothesis requires all three direct reconnection graphs to belong to the smaller soluble category.

If one does not, the simultaneous category lemma supplies one of:

- a bridge;
- a cyclic three-/four-edge cut;
- a loop or parallel-edge bounded degeneration;
- an acyclic appendage.

Thus every application has the complete alternative:

\[
\boxed{
\text{matching flip}
\Longrightarrow
\text{cap lift or category/separator exit}.}
\]

---

## 6. Relation to physical mismatch-kernel elimination

The Type-T and Type-H physical commutation theorems prove more detailed contradictions for the four abstract minimal mismatch kernels. The present theorem is the direct consequence needed by the equality/DDD surgery programme:

- continued cap blocking implies one globally fixed route;
- one route-changing event violates that implication;
- therefore the cap profile is reached.

No separate Type-T or Type-H case split is needed once the three-reconnection classification is available.

---

## 7. Trust boundary

### Exact here

- use of the complete physical profile rather than one state;
- fixed-route consequence of blocked-cap three-reconnection forcing;
- contradiction from one physically realised alternative route;
- intersection with the cap profile `K_i`;
- root-valued gluing of the original cap;
- uniform application to every source of a matching flip.

### Still open

- proof that the inverse-transfer recursion preserves enough outer profile data to reapply the theorem after a smaller lock returns;
- complete local transfer synthesis;
- global proof-DAG assembly;
- canonical acceptance, independent audit, Lean verification, manuscript integration, release, publication, and the global five-support theorem.
