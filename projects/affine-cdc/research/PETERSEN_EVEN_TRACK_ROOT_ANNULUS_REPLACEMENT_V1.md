# Petersen even tracks admit a root-valued annulus replacement

## Research Lead diagrammatic repair theorem v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Parents:**

- `PETERSEN_C6_CANONICAL_STAR_SECTION_V1.md`;
- `PETERSEN_C6_RELATIVE_STAR_MOVIE_DESCENT_V1.md`;
- `PETERSEN_C8_TWO_C6_HISTORY_FILLING_REDUCTION_V1.md`;
- `CONSTANT_PIVOT_FULL_STATE_CONTEXTUAL_CONSUMPTION_V1.md`;
- `PRE_CANCELLATION_C6_MOVIE_AND_MIXED_SCC_SCOPE_CORRECTION_V1.md`.

**Status:** exact diagrammatic theorem extracted from the already proved relative local movies. A closed decorated Petersen `C6` or `C8` defect track has an annular regular neighbourhood whose two boundary histories are root-valued. Each boundary restriction of every primitive `C6` cell is either the canonical star or the unique root cross-path one NNI away from it. Both annular sides therefore canonicalise to the same unique star-section complex. Concatenating the two canonicalisations gives a root-valued cylinder between the two boundary histories. The singular track can be replaced diagrammatically without using equal-face cancellation or target-order induction.

**Important scope:** the cylinder is a two-dimensional history replacement. It is not one simultaneous cubic source graph, not a single contextual state, and not by itself a terminal or strict-order exit. It therefore does not contradict the pre-cancellation scope correction.

---

## 1. Annular neighbourhood of one closed track

Let

\[
\gamma
\]

be one closed nonbranching co-root first-failure track in a lifted Ptolemy history diagram. Let

\[
N(\gamma)
\]

be a sufficiently small regular annular neighbourhood of the track.

Its two boundary circles are denoted

\[
\partial_-N(\gamma),
\qquad
\partial_+N(\gamma).
\]

By construction they lie in the root-valued part of the lifted history. The singular co-root states lie between them.

Resolve every maximal constant-pivot run by its unique side-preserving nonpivot root section. Treat the resulting carriers, side outputs, support transport, cap block, and route orientation as fixed rooted branches at the remaining pivot-change cells.

Assume first that the reduced pivot core of `gamma` is one simple Petersen six-cycle

\[
p_0,p_1,\ldots,p_5,p_0.
\]

---

## 2. The same primitive cell on both annular sides

At the `i`-th pivot-change cell, the fixed two-turn six-port boundary is

\[
B_i=
(p_i,p_{i-1},z_i
\mid
z_{i+1},p_{i+1},p_{i+2}).
\]

The fixed turn corollas are

\[
R_i=(p_{i-1},p_{i+1},z_i),
\qquad
R_{i+1}=(p_i,p_{i+2},z_{i+1}).
\]

Both annular boundary restrictions have exactly this same ordered six-port word and the same rooted turn corollas. They differ only in which root-valued resolution of the relative middle interface is used.

Relative to the four rooted branches with values

\[
(z,z,w,w),
\]

the complete topology table is

\[
\boxed{
\text{one zero path}
+
\text{one root cross path}
+
\text{one root canonical star}.
}
\]

Hence each root-valued boundary restriction is exactly one of

\[
P_i^\times,
\qquad
S_i^\star.
\]

The root cross path and canonical star are joined by the unique relative root-preserving NNI fixing both turn corollas and every exterior incidence.

---

## 3. Both sides canonicalise to the same section

For a sign

\[
\epsilon\in\{-,+\},
\]

let

\[
X_i^\epsilon
\]

be the restriction of `partial_epsilon N(gamma)` to Cell `i`.

Define a path

\[
X_i^\epsilon
\rightsquigarrow
S_i^\star
\]

as follows:

- if `X_i^epsilon=S_i^star`, use the empty path;
- if `X_i^epsilon=P_i^times`, use the unique relative root NNI.

The target `S_i^star` is determined solely by the labelled boundary `B_i` and the fixed turn corollas. Therefore the canonical target is the same for the minus and plus sides.

### Lemma 3.1 — two-sided common canonical target

For every cell `i`, both annular boundary restrictions admit root-valued relative paths to one and the same canonical star:

\[
\boxed{
X_i^-
\rightsquigarrow
S_i^\star
\leftsquigarrow
X_i^+.
}
\]

No support relabelling, root reselection, or change of exterior incidence is used.

---

## 4. Gluing around the hexagon

Consecutive cells share one completely rooted turn corolla:

\[
R_{i+1}^{(i)}=R_{i+1}^{(i+1)}.
\]

Every relative NNI treats this corolla as a fixed exterior branch. Its support contains only the two middle vertices of the relative four-branch interface.

Therefore the six local canonicalisation paths on either annular side:

1. agree on every shared source incidence;
2. preserve all root labels on shared corollas;
3. may be scheduled sequentially or after the standard cell subdivision;
4. introduce no zero or co-root edge;
5. preserve the complete exterior side-root word and cap-route data.

Let

\[
\mathcal T_{C_6}^\star
\]

be the resulting canonical section complex.

### Theorem 4.1 — one-sided canonicalisation

Each annular boundary history admits a root-valued relative history movie to the same canonical section complex:

\[
\partial_-N(\gamma)
\rightsquigarrow
\mathcal T_{C_6}^\star,
\]

and

\[
\partial_+N(\gamma)
\rightsquigarrow
\mathcal T_{C_6}^\star.
\]

The two movies have identical fixed exterior data.

---

## 5. Root-valued cylinder replacement

Reverse the plus-side canonicalisation and concatenate:

\[
\partial_-N(\gamma)
\rightsquigarrow
\mathcal T_{C_6}^\star
\leftsquigarrow
\partial_+N(\gamma).
\]

Every history edge in this concatenation is a root-preserving relative NNI or an identity step. Every history vertex is fully root-valued.

### Theorem 5.1 — `C6` root-annulus replacement

A closed decorated Petersen `C6` track has a singularity-free root-valued annular replacement with the same two boundary histories and the same complete exterior rooted data.

Equivalently, inside a larger lifted Ptolemy diagram one may replace

\[
N(\gamma)
\]

by a root-valued cylinder

\[
N^\root(\gamma)
\]

such that

\[
\partial N^\root(\gamma)
=
\partial N(\gamma)
\]

as labelled history data.

The replacement removes the closed co-root track and creates no new singular track.

---

## 6. Why this is not a forbidden simultaneous time slice

The canonical section complex contains one canonical chart for each history cell. Adjacent charts share rooted interfaces, but their interiors live in different cells of the subdivided history cylinder.

The theorem does **not** identify all six star interiors inside one cubic graph. In particular it does not require one turn corolla to be simultaneously incident with two star centres.

Thus:

\[
\boxed{
\text{root-valued history cylinder}
\ne
\text{one simultaneous source time slice}.
}
\]

This is exactly why the theorem is compatible with `PRE_CANCELLATION_C6_MOVIE_AND_MIXED_SCC_SCOPE_CORRECTION_V1.md`.

---

## 7. Extension to `C8`

Let the reduced pivot core be one simple Petersen eight-cycle. Choose one omitted Petersen vertex and write the canonical decomposition

\[
C_8=H_+\triangle H_-,
\]

where `H_+,H_-` are two simple `C6` cycles sharing a two-edge path.

The seam theorem gives:

- unchanged side-root data away from the seam;
- one identical internal seam root at the shared middle vertex;
- one root-triangle seam at each endpoint;
- complete exterior identity after gluing.

The relative `C6` canonicalisation fixes every side and seam corolla. Apply Theorem 5.1 to each factor while retaining the common seam data, then glue the two root cylinders.

### Theorem 7.1 — `C8` root-annulus replacement

Every closed decorated Petersen `C8` track has a singularity-free root-valued annular replacement preserving its complete labelled exterior history.

No equal-face cancellation or lower-order graph is required.

---

## 8. Unified even-track theorem

### Theorem 8.1 — even closed tracks are diagrammatically removable

Let `gamma` be a closed nonbranching first-failure track whose full-state reduction has simple Petersen core `C6` or `C8`. Retain:

- every constant-pivot rooted carrier;
- every emitted side root;
- every support-transport label;
- the ordered cap shore and route orientation;
- all source incidences outside `N(gamma)`.

Then `N(gamma)` may be replaced by a root-valued history cylinder with the same boundary data. The number of closed singular-track components decreases by one and no new singular edge is introduced.

---

## 9. Relation to the cancellation repair queue

This theorem supplies a new repair mechanism:

### Repair E — diagrammatic track erasure

Use a two-dimensional root homotopy to remove a closed even defect track before any canonical-star dipole is cancelled.

It does not require:

- marked-weld relative return;
- flow selection on the cancelled graph;
- a cancel--solve--reinsert rank;
- one global Kempe class of root flows.

It also does not yet prove complete contextual transfer. One must still show that a minimal lifted Ptolemy diagram has no other closed-track type and that the remaining open defect arcs give strict boundary/history progress.

---

## 10. Assurance boundary

### Exact here

- both annular sides of one primitive `C6` cell have the same fixed six-port data;
- each root-valued restriction is cross or canonical star;
- both restrictions root-canonicalise to the same unique star;
- adjacent canonicalisations glue through fixed rooted turn corollas;
- the resulting two-sided root-valued `C6` cylinder;
- seam-compatible extension to `C8`;
- deletion of one closed even singular-track component without cancellation.

### Imported authorial mathematics

- annular regular-neighbourhood description;
- unique constant-pivot root sections;
- relative `(0,2,2)` cell theorem;
- canonical star uniqueness and overlap compatibility;
- exact `C8=C6 triangle C6` seam theorem.

### Not proved here

- elimination of odd tracks, except as an imported orientation theorem;
- conversion of every recurrent contextual cycle into an embedded closed track with root-valued two-sided boundary;
- strict progress for open defect arcs;
- repaired contextual transfer, cap restoration, or global five-support closure;
- independent audit, Lean verification, manuscript integration, release, arXiv, DOI, peer review, or publication.
