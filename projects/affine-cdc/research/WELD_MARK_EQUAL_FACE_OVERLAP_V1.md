# Ordered weld incidences transport canonically through equal-face moves

## Research Lead `2--0` overlap dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `ca4442a89f553df6cc05d0b51f434021285e4eb5`.

**Parents:**

- `WELD_RELATION_FIRST_EXIT_V1.md`;
- `MARKED_WELD_RELATIVE_CONTEXTUAL_RETURN_TARGET_V1.md`;
- the equal-face cancellation rule;
- `PACHNER_HISTORY_FIRST_FAILURE_ONE_EDGE_ATOM_V1.md`.

**Status:** exact completion of the bounded local transition table for a mobile inverse-weld boundary. The correct primitive marks are four ordered edge incidences, grouped into two reconnecting pairs, rather than two indivisible edge identities. Under an equal-face cancellation, external marked incidences reconnect canonically; under inverse insertion they split canonically. A weld-admissible pair using the two distinct external label classes remains distinct intersecting. The intended inverse weld succeeds root-valuedly. The only mark-destroying `2--0` overlap is a marked central edge of the cancelled equal-face pair; that move is itself a strict order-lowering cancellation and must be handled as a nested mark-consuming frame, not as a new coefficient failure.

---

## 1. Equal-face coordinates

Let two adjacent cubic vertices carry the same root triangle

\[
\boxed{(p,q,r),
\qquad r=p+q,}
\]

where `p,q,r` are three distinct roots.

Let the central edge between the vertices carry `r`. The four external incidences are

\[
p_L,q_L,p_R,q_R,
\]

with root values

\[
p,q,p,q.
\]

Forward equal-face cancellation deletes the two vertices and the central `r` edge, and reconnects

\[
\boxed{
p_L\sim p_R,
\qquad
q_L\sim q_R.
}
\]

The two output edges carry roots `p,q`.

---

## 2. Incidence marks, not indivisible edge marks

A marked weld boundary consists of four ordered incidences

\[
\boxed{
P_1,P_2,Q_1,Q_2
}
\]

grouped into two reconnecting pairs, together with current pair roots

\[
p,q.
\]

When one edge is split by inverse insertion, its two endpoint incidences continue uniquely to the two half-edges. When two equal-root half-edges are reconnected by cancellation, their ordered endpoint incidences continue uniquely to the output edge.

Thus splitting and reconnecting do not create an ambiguity in incidence lineage.

The earlier apparent “one marked edge branches into two” problem was an artefact of treating an edge as one atomic mark rather than retaining its two ordered incidences.

---

## 3. Forward cancellation overlap classes

### Class I — disjoint

If no marked incidence belongs to the equal-face support, the marks are unchanged.

### Class II — one external label class

Suppose marked incidences lie on one or both of `p_L,p_R`. Cancellation reconnects them through the output `p` edge. Their root value remains `p`.

The same holds for the `q` class.

### Class III — one mark from each external label class

Suppose the two weld roots are represented by one marked incidence pair in the `p` class and one in the `q` class. After cancellation they become the two output edges with roots

\[
\boxed{p,q.}
\]

Because `(p,q,r)` is a root triangle,

\[
\boxed{p\ne q,
\qquad
|p\cap q|=1.}
\]

Hence the mobile weld remains in the `B` orbit.

### Class IV — central marked edge

If the central `r` edge itself carries marked incidences, forward cancellation deletes that edge and both of its incidences.

There is no pointwise descendant mark of the same type. This is not an `A/C` coefficient failure: the entire marked central edge has been consumed by a genuine order-lowering `2--0` move.

It must be recorded as:

\[
\boxed{
\text{strict cancellation}
+
\text{one fewer active marked edge lineage}.}
\]

---

## 4. A `B` pair cannot be the equal external pair

The two external edges with the same label class have equal roots:

\[
p_L=p_R=p,
\]

or

\[
q_L=q_R=q.
\]

Therefore they form the `A` orbit, not the weld-admissible `B` orbit.

Consequently an admissible two-edge weld pair meeting an equal-face support in both coordinates must use different label classes `p` and `q`. By Class III it survives the cancellation in `B`.

### Theorem 4.1 — no `A/C` first exit from an external `2--0` overlap

A forward equal-face cancellation which does not delete a marked central edge preserves every external weld-admissible pair in the `B` orbit.

No external `2--0` overlap changes a `B` pair to equal or disjoint.

---

## 5. Reverse insertion

Start from the two output edges with roots `p,q` and their four ordered endpoint incidences.

Inverse equal-face insertion splits both edges, inserts two cubic vertices, and forces the central value

\[
\boxed{r=p+q.}
\]

### Theorem 5.1 — intended inverse weld

If the output pair lies in `B`, then `r` is a root and inverse insertion succeeds canonically. The inserted vertices both carry the root triangle

\[
(p,q,p+q).
\]

All four marked incidences retain their order and root classes.

This is exactly the marked-boundary inverse-weld theorem, now phrased in incidence-lineage form.

### Partial overlap

If only one output edge is marked, inverse insertion splits its two endpoint incidences onto the two corresponding external half-edges. The lineage remains canonical. No coefficient relation is asserted until a second marked root is specified.

---

## 6. Complete local transition alphabet

Combining the present theorem with the prior two dossiers gives the following complete local behaviour of a weld-admissible pair.

### Root `2--2` flip

- four of six one-coordinate moves retain `B`;
- two of six enter `C`;
- no move enters `A`.

### Support-pair switch

- both/neither marked edges switched: retain `B`;
- exactly one switched: enter `A` or `C`.

### Equal-face `2--0`

- disjoint/external incidences: retain `B`;
- intended reverse weld: root success;
- central marked edge cancelled: strict mark-consuming order descent.

### Corollary 6.1

There is no additional local coefficient alphabet beyond:

\[
\boxed{
B\text{ transport},
\quad
A\text{ zero atom},
\quad
C\text{ co-root atom}.}
\]

The only non-coefficient event is deletion of a marked central edge by a genuine cancellation.

---

## 7. Consequence for a nested return rank

A finite relative return can now be scanned until the first event among:

1. complete `B` transport and successful inverse weld;
2. first `A/C` exit, producing one ordinary zero/co-root atom on a strict history prefix;
3. cancellation of a marked central edge, producing a lower-order frame with fewer active mark lineages.

Every local step has an exact disposition. The remaining problem is no longer local overlap classification.

It is to prove that a stack of lower-order frames, shorter-prefix `A/C` returns, and mark-consuming cancellations admits one well-founded global order.

---

## 8. Exact next theorem

### Target 8.1 — nested weld-return stack rank

Define a return frame recording:

- target vertex order;
- remaining finite history prefix;
- number and ordered incidence data of active weld marks;
- complete one-token/cap/route state.

Prove that:

1. entering a recursive cancellation frame strictly lowers target order;
2. an `A/C` pop returns to the parent at a strict shorter prefix;
3. cancellation of a central marked edge strictly lowers the active mark count at the lower-order frame;
4. no transition increases an earlier coordinate of the stack order.

A successful theorem would turn the local first-exit results into a complete cancellation macro-return without requiring pointwise `MWR`.

---

## 9. Trust boundary

### Exact here

- ordered-incidence formulation of weld marks;
- canonical split/reconnection lineage under `2--0` moves;
- preservation of `B` by all external equal-face cancellations;
- impossibility for a `B` pair to use the two equal external label copies;
- root-valued intended inverse weld;
- central-mark deletion as a strict mark-consuming cancellation;
- completion of the finite local transition alphabet.

### Not proved

- the nested weld-return stack rank;
- global handling of repeated central-mark cancellations;
- repaired contextual return or cancellation macro-return;
- R2 global return, cap restoration, or global five-support closure;
- independent audit, curation, Lean verification, manuscript integration, release, arXiv, DOI, peer review, or publication.
