# Pointwise marked-weld return fails exactly at active Pachner diagonals

## Research Lead local-overlap dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `0ec14b9219c09b271b2b032806a9cf362611eed2`.

**Parents:**

- `MARKED_WELD_RELATIVE_CONTEXTUAL_RETURN_TARGET_V1.md`;
- `ROOT_FLOW_TRIANGLE_COMPLEX_PACHNER_V1.md`;
- `PACHNER_FIRST_FAILURE_CRITICAL_OVERLAP_V1.md`;
- `PETERSEN_C6_RELATIVE_STAR_MOVIE_DESCENT_V1.md`.

**Status:** exact local scope theorem. A marked root incidence is preserved pointwise by every disjoint move and by every local move for which it is an exterior branch. It cannot be preserved pointwise when its edge is the active central diagonal of a root-valued `2--2` Pachner flip: the old central root and the new central root are disjoint. The smallest invariant object across such an overlap is the complete ordered four-port envelope of the flip, not the old two-incidence edge mark. Consequently the unrestricted pointwise form of marked-weld relative return is false for arbitrary histories. The live repair is either a causal side-enclosure theorem proving that the canonical `C6/C8` weld edges never become active diagonals in the remaining return history, or a mobile-envelope return theorem.

---

## 1. Root-valued flip coordinates

Let two adjacent root triangles be

\[
T=\{a,b,c\},
\qquad
U=\{a,b,d\},
\]

with four distinct support indices `a,b,c,d`. Their common central root is

\[
\boxed{r=ab.}
\]

The root-valued opposite `2--2` topology has triangles

\[
\{a,c,d\},
\qquad
\{b,c,d\},
\]

and central root

\[
\boxed{s=cd.}
\]

The complete exterior branch word is

\[
\boxed{
B=(ac,bc,ad,bd).
}
\]

Hence

\[
\boxed{r\cap s=\varnothing.}
\]

The old and new diagonals are the two disjoint roots whose union is the active four-support set.

---

## 2. Exact finite certificate

Exhaustive enumeration over the ten root triangles gives:

\[
\boxed{15}
\]

unordered root-valued flip involutions.

For all fifteen:

1. the old and new central roots are disjoint;
2. the central-root pairs are exactly the fifteen Petersen edges of `KG(5,2)`;
3. each of the ten roots occurs as a central diagonal in exactly three involutions;
4. the unordered exterior set
   \[
   \{ac,bc,ad,bd\}
   \]
   uniquely determines the two diagonal roots `ab,cd`.

A standard representative is

\[
12\longleftrightarrow34
\]

with exterior word

\[
13,14,23,24.
\]

Thus a central-edge crossing is precisely one Petersen projectivity step.

---

## 3. Three overlap classes for one marked edge

Let `e` be one root-valued marked edge with its two ordered incidences and prescribed value `z`.

### Class I — disjoint support

If the local surgery support is disjoint from `e` and its endpoints, strict source commutation applies. The edge, both incidences, and value `z` remain unchanged.

### Class II — exterior-branch contact

If `e` is one of the four exterior branches of the local surgery, the move fixes that branch pointwise by definition. Its incidence identity and root value remain unchanged.

The local critical-overlap theorem also preserves every exterior root label. Therefore zero/co-root normalization is relative to any marked branch which remains exterior to the active two-vertex support.

### Class III — active central diagonal

If `e` is the old central edge `ab`, the flipped graph contains no edge with those two incidences. Its new central edge is `cd`, and

\[
ab\perp cd.
\]

Therefore no pointwise relative version can simultaneously require:

- the same marked edge;
- the same two incidences;
- the same root value `ab`;
- and performance of the root-valued flip.

This is a literal topological and coefficient incompatibility, not missing bookkeeping.

---

## 4. Minimal invariant across a central overlap

Although the two-incidence diagonal mark is not preserved, the ordered four-port envelope

\[
\boxed{B=(ac,bc,ad,bd)}
\]

is preserved exactly.

It determines both possible root diagonals:

\[
\boxed{ab\quad\text{and}\quad cd.}
\]

Thus the minimal relative object across an active central flip is not a frozen edge but a **mobile Pachner envelope**:

\[
(B;\text{chosen diagonal sheet}).
\]

Crossing the flip changes only the sheet

\[
ab\leftrightarrow cd,
\]

which is one Petersen edge.

For a weld word with two marked edges

\[
W=(z,z,w,w),
\]

each edge independently has one of:

1. strict preservation as a disjoint/exterior branch;
2. inflation to its four-port Pachner envelope when it becomes active.

Repeated active crossings can therefore enlarge the relative interface unless an enclosure theorem prevents them.

---

## 5. Consequence for the proposed `MWR`

The unrestricted statement

> every arbitrary lower-order contextual history can be performed while fixing the internal weld edges pointwise

is false whenever that history contains a root flip whose central diagonal is one of the weld edges.

Accordingly, `MARKED_WELD_RELATIVE_CONTEXTUAL_RETURN_TARGET_V1.md` must be read conditionally in one of two forms.

### Form A — side-enclosed `MWR`

Prove that, for the particular weld produced by a canonical `C6/C8` star cancellation, both reconnecting edges remain exterior branches or disjoint from every active move in the remaining return history.

Then the existing strict commutation and relative local-overlap theorems preserve

\[
W=(z,z,w,w)
\]

pointwise, and the inverse weld succeeds.

### Form B — mobile-envelope return

Allow a marked edge to become a four-port envelope when crossed by an active flip. Record:

- the ordered four exterior incidences;
- both possible diagonal roots;
- the current diagonal sheet;
- cap and route data.

Prove termination and final recovery of the original weld word under this enlarged finite local grammar.

Form B is substantially stronger and reintroduces projectivity transport. It should not be attempted before Form A is tested.

---

## 6. Exact next theorem

### Target 6.1 — canonical-weld side enclosure

Let one canonical `C6` or seam-compatible `C8` star cell be cancelled, producing reconnecting edges `e_z,e_w`. Relative to the remaining contextual return history, prove one of:

1. `e_z,e_w` are never active central diagonals and hence remain pointwise frozen;
2. the first active-diagonal overlap yields immediate cap/profile escape or a strict separator;
3. the first overlap admits a bounded mobile-envelope replacement with a strictly smaller causal interval.

Only Alternative 1 gives the currently proposed `MWR` without further machinery.

---

## 7. Trust boundary

### Exact here

- all fifteen root-valued Pachner flip involutions;
- disjointness of old and new central roots;
- three central involutions through each root;
- uniqueness of the two diagonals from the exterior four-port word;
- strict preservation for disjoint and exterior-branch marks;
- impossibility of pointwise preservation for an active central mark;
- the mobile four-port envelope as the minimal local invariant.

### Not proved

- canonical-weld side enclosure;
- mobile-envelope global return;
- pointwise `MWR` for the actual `C6/C8` cancellation history;
- repaired cancellation macro-return;
- R2 global return, cap restoration, or the global five-support theorem;
- independent audit, curation, Lean verification, manuscript integration, release, arXiv, DOI, peer review, or publication.
