# Every successful fixed-order return has a fully root-valued presentation

## Research Lead fixed-order presentation theorem v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`

**Parents:**

- the fixed-order no-sink theorem retained in `ROOT_NORMALIZED_CONTEXTUAL_TRANSFER_MASTER_V5.md` v5.3;
- `PTOLEMY_CLOSED_DEFECT_TRACK_ERASURE_V1.md`;
- `OPEN_TRACK_ROOT_STRIP_ENDPOINT_SCOPE_CORRECTION_V1.md`;
- `PERIODIC_OUTER_ENDPOINT_ROOT_SEAM_DISCHARGE_V1.md` v1.2;
- finite complete endpoint-state semantics.

**Status:** exact diagrammatic strengthening for a successful fixed-order return. Suppose a finite fixed-order contextual execution starts at a root-valued state and eventually returns a root-valued state, without an accepted route/profile/category exit. The execution may pass through one-atom states and may visit the unresolved outer endpoint finitely many times. Glue consecutive continuation episodes along their identical complete endpoint collars. Every intermediate outer contact becomes an internal seam of one nonbranching singular track. The true endpoints of every open singular component are then root-normalized birth/death cells. Closed components erase by root annuli and open components erase by the corrected root-strip theorem. Hence the complete successful execution has a boundary-equivalent fully root-valued history presentation.

This theorem does not assert abstract root/Kempe connectivity of arbitrary flows. It transforms one supplied successful contextual execution.

---

## 1. Successful fixed-order execution

Fix one labelled predecessor-order incidence universe and one original-prefix level.

Let

\[
X_0\leadsto X_1\leadsto\cdots\leadsto X_m
\]

be a finite canonical contextual execution such that:

1. every state has the same source vertex order;
2. raw `2--0/0--2` birth/death cells are absent;
3. `X_0` and `X_m` are fully root-valued;
4. every non-root state carries one normalized co-root atom after bounded local normalization;
5. no step exits through a route/profile, bounded terminal or separator/category branch.

The path may be grouped into finitely many continuation episodes separated by visits to unresolved complete outer endpoint states.

---

## 2. Glue continuation collars

Whenever one episode ends at an unresolved complete endpoint state `E` and the next episode begins from that same state, identify their short endpoint collars by the identity on the complete labelled state:

- same source topology and incidences;
- same atom edge, value and crossed resolutions;
- same support transport and side attachments;
- same cap block and route orientation.

After all such identifications, obtain one finite fixed-order lifted history complex

\[
\mathcal D.
\]

The global start and finish remain root-valued boundary histories.

### Lemma 2.1 — intermediate outer contacts are not singular endpoints

Every glued unresolved endpoint collar is an interior seam of the singular one-manifold of `D`.

### Proof

Before gluing, the incoming episode has one singular half-arc ending at the collar and the outgoing episode has the same complete singular half-arc beginning there. Pointwise equality of the labelled endpoint state identifies their germs. The resulting point has degree two in the normalized singular locus. ∎

Thus the connected singular components of `D` are:

1. closed interior tracks;
2. open tracks whose genuine endpoints occur only at local atom birth/rootification cells on the root-valued global comparison boundary.

---

## 3. Endpoint types of the remaining open tracks

At the first point of an open component, a root-valued parent move has failed and the component is born from one root resolution. Its short side is the root-normalized local cell recorded by the first-failure theorem.

At the final point, the atom is removed by:

- an alternative root NNI;
- an alternative root-valued inverse insertion already represented at fixed order;
- a horizontal rootification;
- or the final root state `X_m`.

Because accepted exits were excluded, each final short side is root-valued.

### Lemma 3.1

Every genuine endpoint of every open singular component is Type 1 or Type 2 in the classification of `OPEN_TRACK_ROOT_STRIP_ENDPOINT_SCOPE_CORRECTION_V1.md`. No Type 3 unresolved outer endpoint remains after collar gluing.

---

## 4. Remove the singular components

Choose a contextual lift of the same labelled outer boundary minimizing lexicographically:

\[
\bigl(c,s\bigr),
\]

where `c` is the number of closed singular components and `s` the total singular edge count.

### Closed components

Apply `PTOLEMY_CLOSED_DEFECT_TRACK_ERASURE_V1.md`. Constant-pivot loops rootify, odd cores are impossible and even cores have root-annulus replacements. Hence no closed component survives minimality.

### Open components

By Lemma 3.1 both endpoints are root-normalized or accepted cells. Apply the retained open-strip theorem. Its canonical root cells glue along the complete open chain, including seams which arose from glued continuation collars, because those seams are equality of the same full-labelled atom state and are not endpoints.

The root strip fixes both long histories, both root-valued short sides and every rooted attachment. Replacing one component strictly lowers `s` without creating another singular component.

Hence no open component survives minimality.

---

## 5. Main theorem

### Theorem 5.1 — root presentation of successful return

Every finite successful fixed-order contextual execution between two root-valued complete states has a boundary-equivalent fully root-valued history presentation.

The replacement:

1. remains at the same vertex order;
2. uses legal root-valued relative source movies;
3. preserves the complete labelled start and finish states;
4. preserves every exterior incidence, cap block, route and rooted attachment;
5. contains no zero or co-root edge.

### Proof

After collar gluing, Sections 2--4 remove every connected singular component from a minimal lift. ∎

---

## 6. Relation to periodic endpoint discharge

The fixed-order no-sink theorem used to obtain a successful finite execution may rely on periodic endpoint discharge: a repeated unresolved endpoint cycle is replaced by a root cylinder and cannot form a nonexit sink SCC.

There is no circular use of the present theorem:

- periodic discharge assumes one already fixed-order repeated cylinder and uses the closed-track theorem plus a root `1`-skeleton crosscut;
- the present theorem starts with a finite successful path, glues only its consecutive endpoint collars, and removes the resulting closed/open components;
- neither theorem uses variable-order bubble compression.

---

## 7. Consequence for innermost cancellation bubbles

An innermost recursive cancellation bubble contains no deeper `2--0/0--2` call. Its lower comparison is fixed-order.

If that lower branch exits, the whole contextual branch is accepted and no return compression is needed.

If it successfully returns a root state, Theorem 5.1 supplies a root-valued lower history presentation. Therefore the hypothesis of `INNERMOST_CANCELLATION_BUBBLE_RAW_INSERTION_LIFT_V1.md` is satisfied.

---

## 8. Assurance boundary

### Exact here

- collar gluing of identical complete endpoint states;
- conversion of intermediate outer contacts into internal degree-two seams;
- root-normalized classification of the true open-track endpoints;
- closed-track and open-strip elimination;
- fully root-valued presentation of a supplied successful fixed-order execution.

### Imported authorial mathematics

- fixed-order finite-state no-sink theorem;
- full-state nonbranching singular locus;
- closed-track erasure;
- normalized-endpoint open-strip replacement;
- periodic fixed-order endpoint discharge.

### Not claimed

- root connectivity of arbitrary unrelated flows;
- variable-order compression before the innermost-bubble induction;
- R2.7 closure, cap restoration or global five-support closure;
- PDL reconstruction, audit, Lean, manuscript, curation, release or publication.
