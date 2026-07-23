# No positive-vertex bounded DDD residual survives the global Pachner potential

## Research dossier v1 — authorial correction and closure

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `011fec1029cdb332a57b6d81c364752574be8357`.

**Parents:**

- `DDD_LOCK_GLOBAL_PACHNER_POTENTIAL_V1.md`;
- `BOUNDED_DIRECT_PAIRING_CAP_TERMINAL_V1.md`;
- `ROUTE_CHANGING_MATCHING_FLIP_CAP_ESCAPE_V1.md`;
- the category-safe root NNI and equal-face cancellation theorems;
- `ORIENTED_FULL_CHANNEL_LOCK_ELIMINATION_SYNTHESIS_V1.md`.

**Corrects:** the extra alternative “a bounded residual carrier at which the marked DDD route can be inspected explicitly” in Corollary 5.2 of `DDD_LOCK_GLOBAL_PACHNER_POTENTIAL_V1.md`.

**Status:** exact consequence of the already proved full-ten-triangle DDD descent and its well-founded potential. A nonempty DDD four-pole always admits either an equal-face cancellation or a strictly `Omega`-lowering root Pachner flip. If the selected move changes the ordered cap route, the cap lifts; if it leaves the connected bridgeless cubic category, a separator or bounded degeneration is exposed; otherwise the lexicographic potential strictly decreases. Hence an internal DDD descent cannot terminate at a positive-vertex bounded carrier. Its only non-exit terminal is the zero-vertex direct matching, already classified as bridge or soluble theta.

**Not implied:** cover-independent inverse transfer through the finite history, independent verification of the parent potential theorem, canonical acceptance, Lean verification, manuscript integration, release, publication, or DOI status.

---

## 1. DDD state and potential

Normalize the DDD boundary roots to

\[
12,12,34,34.
\]

Let `R` be a connected root-labelled cubic four-pole with this ordered boundary and with the fixed cap-oriented route retained.

The full-ten-triangle DDD theorem defines

\[
\Omega(R)=\sum_{v\in V(R)}\omega(\Delta_v)
\]

for an explicit nonnegative triangle weight `omega`, and the lexicographic potential

\[
\boxed{
\mathcal P_{\mathrm{DDD}}(R)
=(\Omega(R),|V(R)|).}
\]

Its two exact local conclusions are:

1. if `R` is nonempty, then some internal edge joins equal support triangles or some distinct adjacent pair admits a strictly `Omega`-lowering root Pachner flip;
2. an equal-face cancellation removes two vertices and strictly lowers `P_DDD`, while a selected Pachner flip preserves vertex number and strictly lowers `Omega`.

Therefore every selected category-safe, route-preserving move strictly lowers `P_DDD`.

---

## 2. Complete disposition of one selected move

At a nonempty DDD carrier, choose one move guaranteed by the parent descent theorem. Exactly one of the following occurs.

### Route/profile change

The modified root state changes the distinguished cap route or reaches a boundary state in the original cap profile. Then the route-changing matching-flip theorem gives cap-profile escape and the original cap lifts root-valuedly.

### Category failure

The local replacement does not remain a connected bridgeless cubic four-pole in the inductive category. The category-safe surgery theorem then exposes one of:

- a two-edge separator;
- a cyclic three- or four-edge separator;
- a loop or parallel-edge degeneration;
- a bounded acyclic appendage.

These are established exits from the prime DDD branch.

### Internal continuation

The move preserves the ordered DDD boundary, fixed route, connectedness, bridgelessness, and cubic category. Then the resulting carrier `R'` satisfies

\[
\boxed{
\mathcal P_{\mathrm{DDD}}(R')
<
\mathcal P_{\mathrm{DDD}}(R).}
\]

There is no fourth response.

---

## 3. Positive-vertex bounded residuals are impossible

### Theorem 3.1 — no positive-vertex DDD terminal

A finite route-preserving DDD descent which has not exited through cap lift or category failure cannot terminate at a carrier with at least one source vertex.

### Proof

Suppose a terminal carrier `R` has

\[
|V(R)|>0.
\]

Then `R` is nonempty. The full-ten-triangle DDD descent theorem supplies an equal-face cancellation or an `Omega`-lowering Pachner flip.

- If that move changes the route, `R` was not terminal: it exits through cap lift.
- If it fails the category conditions, `R` was not an unresolved terminal: it exits through a separator or bounded degeneration.
- Otherwise the move remains internal and strictly lowers `P_DDD`, contradicting terminality.

Thus no positive-vertex carrier can be an internal terminal. ∎

### Corollary 3.2 — boundedness is irrelevant

The conclusion does not require an order bound or finite census of residual carriers. Every finite positive-vertex residual, however small, still contains a guaranteed move or an established exit.

Hence the phrase “bounded residual carrier at which the marked DDD route can be inspected explicitly” is unnecessary and must not be treated as an additional proof obligation or allowed endpoint.

---

## 4. The only internal endpoint

If a descent has no route or category exit, repeated strict decrease of the nonnegative integer pair

\[
(\Omega,|V|)
\]

must terminate. By Theorem 3.1 the terminal carrier has

\[
|V|=0.
\]

A zero-vertex cubic four-pole is exactly one of the three terminal matchings of its four boundary incidences.

Closing it by the original two-vertex cap gives:

1. the cap-block matching: two loops joined by a bridge, hence category exit;
2. either cross matching: the two-vertex theta multigraph, with explicit root flow `12,13,23`.

Therefore:

### Theorem 4.1 — complete DDD current-flow endpoint

Every oriented DDD current-flow descent reaches, after finitely many moves, exactly one of:

\[
\boxed{
\text{cap-profile/route escape},
\quad
\text{separator or bounded category exit},
\quad
\text{zero-vertex direct matching}.}
\]

The last case is itself bridge or immediately root-soluble. No generic bounded DDD residual remains.

---

## 5. Correction to the earlier corollary

Corollary 5.2 of `DDD_LOCK_GLOBAL_PACHNER_POTENTIAL_V1.md` listed five possible outcomes, including:

> a bounded residual carrier at which the marked DDD route can be inspected explicitly.

This was a cautious frontier placeholder rather than a consequence required by the main potential theorem. Read the corollary henceforth with that alternative deleted.

The exact corrected outcome list is:

1. route/profile change and cap escape;
2. two-, three-, or four-edge separator;
3. loop, parallel-edge, or acyclic category degeneration;
4. zero-vertex direct matching.

The apparent equality/DDD asymmetry is therefore removed: both forward descents terminate at the same three classes of endpoint—route escape, category exit, or direct matching.

---

## 6. Interface with contextual inverse transfer

The current theorem concerns the forward current-flow history. It does not assert that the terminal theta recolouring equals the forward terminal root state.

The complete proof uses:

1. forward equality or DDD descent to route/category/direct-matching endpoint;
2. cover-independent recolouring at the soluble endpoint when necessary;
3. first-failure localisation during inverse transfer;
4. same-order Ptolemy/Petersen track disposition and root-tube filling;
5. strict cap-target order descent after an actual cancellation.

Thus eliminating the spurious bounded residual does not bypass contextual transfer. It ensures that contextual transfer has only the already declared endpoint sources and no hidden finite DDD family.

---

## 7. Consequence for the full-channel theorem

Under a blocked original cap, horizontal rescue reduces the DDD branch to one oriented full-channel lock. Apply the corrected current-flow descent.

- Route change contradicts fixed-route blocking and lifts the cap.
- Category failure discharges the prime branch.
- Direct matching is bridge or soluble theta.
- The terminal solution transfers back through the established contextual inverse-transfer theorem.

Therefore the DDD half of the full-channel synthesis no longer contains any implicit bounded-census assumption.

---

## 8. Trust boundary

### Exact here

- complete disposition of every move guaranteed by the DDD potential theorem;
- impossibility of a positive-vertex internal terminal;
- deletion of the generic bounded-residual alternative;
- reduction of all non-exit DDD descents to the zero-vertex direct matching;
- exact agreement of equality and DDD forward endpoint classes;
- removal of one hidden finite-exception reading from the full-channel synthesis.

### Imported authorial mathematics

- the explicit DDD weight and no-local-minimum theorem;
- category-safe root surgery;
- route-changing cap escape;
- bridge/theta direct-terminal classification;
- contextual inverse transfer.

### Still outside this checkpoint

- proof-development expansion or independent verification of the parent theorems;
- curation or canonical movement;
- Lean verification;
- manuscript integration;
- release, arXiv, DOI, peer review, or publication.
