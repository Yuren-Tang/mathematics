# Cellwise root seams and constant-run sections erase a complete normalized track

## Research Lead R2.6 replacement theorem v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`

**Parents:**

- `MARKED_CLOSED_TRACK_DIRECT_ROOT_SEAM_V1.md`, Theorems 3.1--6.1 only;
- `CONSTANT_PIVOT_FULL_STATE_CONTEXTUAL_CONSUMPTION_V1.md`;
- source-faithful Type-T/backtrack normalization;
- the general nonbacktracking open-cell `(0,2,2)` theorem;
- first-failure nonbranching and complete full-state track classification;
- `SWITCH_POP_COLLAR_ROOT_SHORT_SIDE_V1.md` for normalized support-switch endpoints.

**Supersedes as the controlling R2.6 route:**

- the unproved global canonical `C6` history section;
- `PETERSEN_EVEN_TRACK_ROOT_ANNULUS_REPLACEMENT_V1.md` as a required input;
- the global gluing claim in `PETERSEN_OPEN_TRACK_ROOT_STRIP_REPLACEMENT_V1.md`;
- Corollary 7.1 of `MARKED_CLOSED_TRACK_DIRECT_ROOT_SEAM_V1.md` insofar as it invoked that global open-strip theorem;
- the R2.6 dependence on simultaneous/alternating six-star states.

**Status:** exact source-level track-erasure theorem. A finite normalized nonbranching co-root track is partitioned into maximal constant-pivot runs and genuine pivot-change cells. Put one explicit local root seam in every pivot-change cell. These collars are disjoint after harmless identity subdivision. Cutting at all seams leaves only open constant-pivot intervals. Each interval has the unique side-preserving nonpivot root section, relative to the root-valued seam copies at its ends. Gluing the local seams and run sections gives a singularity-free root-valued replacement of the whole track. No global canonical star section, `C6/C8` annulus, support-switch interior cell, equal-face cancellation or lower-order call is used.

This repairs the legal-history realisation gap isolated by `R2_6_LEGAL_HISTORY_SECTION_SCOPE_CORRECTION_V1.md`.

---

## 1. Normalized full-state track

Let

\[
\gamma
\]

be one connected component of the singular locus in a finite lifted fixed-order comparison.

Assume the normalized fixed-order alphabet:

- every persistent singular edge is one co-root/DDD atom;
- the locus is nonbranching;
- raw support-switch corrections occur only in terminal switch--pop collars, not in the interior;
- every current history state retains complete source topology, root labels, crossed resolutions, side outputs, support transport, cap block, route and ancestor-mark data.

Thus `gamma` is either:

1. a closed circle; or
2. an open interval whose endpoints lie at normalized/accepted/outer boundary collars.

Along `gamma`, partition the finite history into maximal constant-pivot runs and genuine pivot-change cells.

---

## 2. Local root seam at every pivot change

Consider one genuine nonbacktracking pivot-change cell with four consecutive pivots

\[
x\to s\to t\to y.
\]

Its consecutive side roots are

\[
z=x+t,
\qquad
w=s+y.
\]

The exact 120-case theorem gives

\[
z\ne w,
\qquad
|z\cap w|=1.
\]

Relative to the two resolved turn corollas, the middle branch word is

\[
(z,z,w,w).
\]

The two root-valued side restrictions are cross or canonical star, and both reach the same star by zero or one relative root NNI:

\[
X^-
\rightsquigarrow
S^\star
\leftsquigarrow
X^+.
\]

The path fixes:

- both turn corollas;
- all ordered local boundary incidences;
- every exterior source edge;
- side roots, support transport, cap block, route and surviving/suspended marks.

### Lemma 2.1 — pivot-change cut seam

Every genuine pivot-change cell contains a root-valued transverse seam which cuts the singular track at that cell.

This is a local statement about one complete source cell. It does not require a neighbouring canonical star.

---

## 3. Disjoint collar choice

The track has finitely many pivot-change cells. Choose a small closed collar

\[
N_i
\]

inside each such cell around the local seam of Lemma 2.1.

### Lemma 3.1 — pairwise disjoint seam collars

After inserting identity history subdivisions where two pivot-change cells are consecutive, the collars `N_i` may be chosen with disjoint interiors.

### Proof

Distinct pivot-change occurrences are distinct cells or distinct marked occurrences in the finite history complex. Shrink inside cell interiors. If two occurrences share a boundary history vertex, replace that vertex by a finite identity interval and assign one collar to each side. Identity states and edges are root-valued and preserve all complete data. ∎

No collar contains two canonical star interiors.

---

## 4. Cutting the complete track

Replace every collar by its local root seam, or equivalently cut the history neighbourhood along all seam paths.

Every genuine pivot change has been removed from the singular locus. Therefore each remaining singular component has constant pivot throughout.

### Lemma 4.1 — remaining components are constant-pivot intervals

After all cuts, the remaining singular locus is a finite disjoint union of open intervals

\[
I_1,\ldots,I_k
\]

such that:

- each `I_j` lies in one maximal constant-pivot run;
- every finite endpoint short side is a root-valued seam copy or a normalized/accepted endpoint collar;
- no `I_j` contains a pivot-change cell.

For a closed original track with at least one pivot change, every endpoint is a seam copy.

If the original closed track has no pivot change, it is one closed constant-pivot run and is treated directly in Section 5.

---

## 5. Rootifying constant-pivot pieces

Let one remaining interval have states

\[
F_t=\{s,d_t\},
\qquad t=a,\ldots,b,
\]

with fixed pivot `s`.

The oriented cap lock selects the unique nonpivot root section

\[
r_t=d_t.
\]

`CONSTANT_PIVOT_FULL_STATE_CONTEXTUAL_CONSUMPTION_V1.md` proves that this section:

1. resolves every co-root state in the run;
2. preserves every emitted side-root occurrence;
3. preserves every exterior rooted attachment and incidence order;
4. preserves support transport and the distinguished cap block;
5. matches the actual root endpoint resolutions at both ends.

### Theorem 5.1 — relative constant-run strip

Every constant-pivot interval with root-normalized/accepted endpoint short sides has a root-valued relative strip replacement fixing its complete rectangular boundary.

### Closed constant-pivot case

If a closed track has no pivot change, the same nonpivot section closes because the complete endpoint state is identical. It rootifies the whole circle directly.

---

## 6. Gluing

For each cut seam, the adjacent constant-run replacement uses exactly the root state furnished by that seam on its endpoint short side.

The local seam and run section agree literally on:

- source vertex/dart slots;
- all edge roots;
- crossed-resolution choice;
- side-root and support-transport data;
- cap block, route orientation and surviving marks.

Thus they glue by identity, not merely by equal coefficient labels.

### Theorem 6.1 — closed-track cellwise erasure

Every finite closed normalized full-state co-root track has a singularity-free root-valued cylinder replacement with the same complete labelled exterior boundary.

### Proof

- If there is no pivot change, use the closed constant-run section.
- Otherwise place disjoint seams at every pivot-change cell, cut, rootify each constant-pivot interval, and glue all pieces along the seam copies.

Every replacement piece is source-faithful and root-valued. The finite gluing restores a cylinder and contains no singular edge. ∎

This proof is independent of simple-cycle length, `C6/C8` classification and global star matching.

---

## 7. Open tracks

Let `gamma` be open.

### Both endpoints normalized or accepted

Include their root-valued/discharged short sides, place seams at every interior pivot-change cell, and rootify every remaining constant-pivot interval.

### Theorem 7.1 — open-track cellwise erasure

If both endpoints are root-normalized or accepted boundary collars, the complete open track has a root-valued rectangular replacement fixing all four labelled sides.

Switch--pop birth/death collars satisfy the normalized endpoint hypothesis by `SWITCH_POP_COLLAR_ROOT_SHORT_SIDE_V1.md`.

### One unresolved outer endpoint

The interior pivot changes and all completed constant-pivot intervals may still be consumed. The final component incident with the unresolved outer co-root side is not declared rootified. It remains the exact outer-endpoint obligation.

Thus the endpoint scope correction is preserved.

---

## 8. Periodic outer endpoint

Suppose a normalized variable-order episode has already been compressed to fixed order and the same complete unresolved endpoint state repeats.

Identify the two equal endpoint collars. The open track becomes a finite closed normalized full-state track in a history cylinder.

Apply Theorem 6.1 to obtain a connected root-valued history cylinder with the same boundary histories.

Its legal history `1`-skeleton is connected. A shortest path between the two boundary vertex sets is a root-valued crosscut. Cutting along it gives a root rectangle and removes the repeated endpoint occurrences.

### Theorem 8.1 — periodic endpoint discharge, repaired R2.6 input

The periodic outer-endpoint theorem is valid using cellwise track erasure, without a global `C6/C8` canonical section or open-star strip.

---

## 9. Type-T/backtrack occurrences

An immediate pivot backtrack may be handled in either of two equivalent ways:

1. use the established source-faithful local `abba` deletion before the seam decomposition; or
2. regard its two genuine pivot-change occurrences as seam sites, after which the intervening constant-pivot interval rootifies.

No abstract free-word deletion is required.

---

## 10. Why the simultaneous-star obstruction disappears

The failed global approach tried to place or longitudinally connect canonical stars from neighbouring cells.

The present proof never does this.

- Each canonical star appears only inside its own small seam collar.
- Distinct collars have disjoint interiors.
- Between collars lies a physical constant-pivot run, replaced by its own root section.
- Gluing occurs at complete root seam states, not at shared star centres.

Therefore `TURN_COROLLA_POINTWISE_MATCHING_CHANGE_OBSTRUCTION_V1.md` is respected rather than evaded.

The naked twenty-three-NNI alternating-carrier certificate is no longer required for R2.6, though it remains a valid finite root-connectivity result for the abstract carrier.

---

## 11. Impact on the proof DAG

### R2.6 closed at Research Lead authorial level

The exact R2.6 source statement is now:

\[
\boxed{
\text{local seams at every pivot change}
+
\text{constant-run root sections}
\Longrightarrow
\text{closed/open normalized track erasure}.}
\]

### Reactivated conditional consumers

With independent reconstruction of this theorem, the following can again be consumed:

- fixed-order no-neutral-recurrence;
- periodic endpoint discharge;
- variable-order episode compression;
- resolved-call macro rank;
- contextual transfer v6/v6.1;
- the R2-to-R1 cap-restoration interface.

### No dependence on

- a simultaneous six-star source state;
- a legal global `C6` canonical history section;
- a `C8=C6 triangle C6` annulus;
- whole-track support-switch cells;
- equal-face cancellation or graph-order descent inside R2.6.

---

## 12. Assurance boundary

### Exact here

- finite all-pivot-change seam placement;
- disjoint collar construction;
- decomposition into constant-pivot intervals;
- endpoint-relative constant-run rootification;
- literal full-state seam/run gluing;
- closed-track cylinder replacement;
- normalized-endpoint open rectangle;
- repaired periodic endpoint consumer;
- avoidance of the global history-section obstruction.

### Imported exact local mathematics

- local root seam at constant-run/backtrack/pivot-change marks;
- unique side-preserving constant-pivot root section;
- one-token nonbranching;
- switch--pop root endpoint collars.

### Required downstream

- PDL independent reconstruction;
- final R2.7 synthesis and terminal-result audit;
- independent assurance.

### Not claimed

- present PDL completion;
- global five-CDC acceptance;
- Lean, manuscript, curation, release or publication status.
