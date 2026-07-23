# Marked-weld relative contextual return would repair cancellation re-entry

## Research Lead exact frontier dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `cce33855cd7c21acfe3b490f07151a7e5bc1356b`.

**Parents:**

- `CANCELLATION_EXIT_REENTRY_WELL_FOUNDEDNESS_GAP_V1.md`;
- `PRE_CANCELLATION_C6_MOVIE_AND_MIXED_SCC_SCOPE_CORRECTION_V1.md`;
- `PETERSEN_C6_RELATIVE_STAR_MOVIE_DESCENT_V1.md`;
- `PETERSEN_C6_AUTOMATIC_CATEGORY_SAFETY_V1.md`;
- `CONTEXTUAL_TRANSFER_TARGET_ORDER_CORRECTION_V1.md`.

**Status:** precise sufficient repair theorem. It is not proved here. It replaces the vague phrase “componentwise recursion after genuine cancellation” by an exact relative boundary-preservation obligation.

---

## 1. The canonical weld boundary

In one canonical Petersen `C6` star cell, let the side-root triangle be

\[
\{z,w,u\},
\qquad
u=z+w.
\]

The equal-face dipole consists of two vertices carrying the same triangle

\[
(z,w,u)
\]

and joined along `u`.

Cancelling the pair reconnects:

- the two `z` incidences into one edge `e_z` of value `z`;
- the two `w` incidences into one edge `e_w` of value `w`.

Cut the interiors of `e_z,e_w`. This exposes an ordered marked weld boundary

\[
\boxed{
W=(z,z,w,w),
\qquad z\ne w,
\qquad z+w=u\in R_5.
}
\]

The lower-order graph or multipole already carries an inherited root flow realizing this boundary.

---

## 2. Why preservation of `W` is sufficient

Suppose a lower-order contextual return produces a root flow on the required lower-order predecessor while preserving the four marked incidences and their values `W`.

Reconnect the equal pairs to recover edges `e_z,e_w`, then insert the two equal root triangles with central edge `u=z+w`.

At both inserted vertices the incident roots are

\[
(z,w,u),
\]

so the inverse weld is root-valued.

### Theorem 2.1 — marked-boundary inverse weld

A lower-order return preserving the ordered word

\[
(z,z,w,w)
\]

lifts canonically through the cancelled equal-face pair. No zero or co-root first-failure atom is created.

### Proof

The forced central value is `z+w=u`, a root because `z,w` are distinct intersecting members of one root triangle. Every other edge value is unchanged. ∎

Thus the cancellation re-entry problem is entirely a boundary-preservation problem.

---

## 3. Required strengthened induction statement

Let a **multiply relative cap context** consist of:

1. the usual ordered outer cap boundary and distinguished cap block;
2. a finite list of additional frozen ordered semiedge boundaries;
3. one prescribed root word on each frozen boundary;
4. a source history whose allowed internal moves fix all frozen rooted branches pointwise.

### Target 3.1 — marked-weld relative contextual return (`MWR`)

For every target order below `N`, every cap-compatible terminal root state on such a context transfers to the required predecessor context while preserving:

- every frozen incidence;
- every frozen root value;
- the ordering of all marked boundaries;
- the outer cap block and route data;

or exits through an independently accepted separator/bounded branch which preserves the same marked data on every continuing component.

The theorem must allow the marked word

\[
(z,z,w,w)
\]

created by a `C6/C8` equal-face cancellation.

---

## 4. Conditional repair of the no-sink theorem

### Theorem 4.1 — cancellation exit under `MWR`

Assume `MWR` for every target order below `N`. Then a canonical `C6/C8` equal-face cancellation at order `N` is a genuine completed lower-order exit.

### Proof

1. Cancel the canonical equal-face dipole and cut the two reconnecting edges, recording the marked word `W=(z,z,w,w)`.
2. The total number of source vertices decreases by two.
3. Apply lower-order `MWR` to the continuing component(s), retaining `W` pointwise.
4. Reinsert the equal-face pair by Theorem 2.1.
5. The reinserted order-`N` state is root-valued; no singular re-entry occurs. ∎

Consequently the finite same-order SCC argument may treat the cancellation as an exit **only after** `MWR` is established.

---

## 5. Why the existing contextual theorem does not imply `MWR`

The existing context records the outer ordered four-port word and cap route. The weld boundary is internal to the source graph at the moment before cancellation.

Promoting it to an exterior frozen boundary requires all remaining history moves to admit a relative realization fixing those four rooted branches. The current dossiers do not prove:

1. that the weld boundary has a coherent trace through every earlier history state;
2. that every critical overlap can be normalized without moving or relabelling it;
3. that route-changing Kempe switches avoid the marked edges;
4. that direct/theta terminal normalization preserves `W`;
5. that component decomposition keeps both copies of each marked pair in a controlled continuing context.

Therefore the general slogan “all exterior data are preserved” cannot be applied until the internal weld is actually externalized throughout the recursive history.

---

## 6. Two possible proofs of `MWR`

### Route I — weld-boundary extrusion

Construct a coherent trace of the two reconnecting edges backward through the remaining Ptolemy history. Prove local commutation/extrusion rules for:

- disjoint root flips;
- one-cell critical overlaps;
- route switches;
- constant-pivot normalization;
- direct terminal conversion.

At every stage the four marked rooted incidences must remain outside the support of the active move.

### Route II — simultaneous stronger induction

Rebuild contextual return from the outset for arbitrary finite frozen boundaries. Every local theorem must be proved relative to an arbitrary collection of fixed rooted branches. Then the weld boundary can be added at a cancellation and removed after the successful inverse weld.

Route II is conceptually cleaner but potentially requires broad reconstruction of R2.4--R2.7.

---

## 7. Finite local attack surface

The new mathematics is concentrated at overlaps between one marked weld edge and one allowed contextual transition.

For each transition type, prove one of:

1. the move is disjoint and commutes with marking;
2. the move has a relative version fixing the marked branch;
3. the overlap gives immediate root transfer;
4. the overlap gives a separator/category exit;
5. the overlap replaces `W` by another marked root-triangle weld boundary at the same or lower strict rank.

Because the root alphabet and critical neighbourhoods are finite, the genuinely local overlap table is a candidate for Wolfram enumeration. What is not finite purely locally is the global component/route genealogy.

---

## 8. Relation to the prior repair list

`MWR` is a precise implementation of:

- Repair B, if the marked-boundary trace carries a strict macro rank;
- Repair C, because preservation of `z,w` selects a root-success inverse weld;
- part of Repair A, if terminal switches can be chosen relative to `W`.

Repair D alone is not available from the current pre-cancellation `C6` movie.

---

## 9. PDL target

After reconstructing R2.4--R2.6, PDL should test whether every local theorem has a version relative to one additional frozen root-triangle weld boundary.

A successful dossier must explicitly include:

1. definition of multiply relative contextual states;
2. finite-state proof with marked incidences;
3. all local overlap cases;
4. route and direct-terminal preservation;
5. componentwise handling;
6. Theorem 2.1 as the final inverse-weld step;
7. a noncircular target-order induction.

Until then R2.7 remains `BLOCKED-FRONTIER`.

---

## 10. Trust boundary

### Exact here

- canonical weld word `(z,z,w,w)`;
- root-valued inverse insertion under preservation of that word;
- `MWR` as a sufficient repair theorem;
- exact distinction between outer-boundary preservation and internal-weld extrusion;
- finite list of local transition interfaces requiring reconstruction.

### Not proved

- `MWR`;
- coherent weld-boundary extrusion;
- route/direct terminal preservation relative to `W`;
- repaired finite condensation;
- cap restoration, simple-edge extension, global five-support closure;
- independent audit, Lean verification, manuscript integration, release, arXiv, DOI, peer review or publication.