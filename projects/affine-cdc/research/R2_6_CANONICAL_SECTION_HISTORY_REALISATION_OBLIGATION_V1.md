# R2.6 load-bearing obligation: the canonical `C6` section must be a legal history

## Research Lead scope guard v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`

**Historical PDL files:**

- `AC_PD_5CDC_R2_5_EVEN_TRACK_CYLINDER_ERASURE.md`;
- `AC_PD_5CDC_R2_5A_PRE_CANCELLATION_SCOPE_CORRECTION.md`.

**Current Research sources:**

- `PETERSEN_C6_CANONICAL_STAR_SECTION_V1.md`;
- `PETERSEN_C6_RELATIVE_STAR_MOVIE_DESCENT_V1.md`;
- `PETERSEN_EVEN_TRACK_ROOT_ANNULUS_REPLACEMENT_V1.md`;
- `R2_6_EVEN_TRACK_SOURCE_REPLACEMENT_PDL_HANDOFF_V1.md`.

**Status:** exact reconstruction obligation. The old PDL correction rightly rejects treating all six canonical star charts as one simultaneous cubic source state. The later Research Lead annulus theorem intends a different object: a one-dimensional root-valued **history section** through the subdivided annular history complex. To reconstruct R2.6, PDL must prove that this section is a legal source history, not merely a static collection of compatible local charts.

Static equality of shared turn corollas is necessary but not sufficient by itself.

---

## 1. The forbidden simultaneous state

Let `R_i` be the rooted turn corolla shared by neighbouring identity-hexagon cells.

In the canonical star of Cell `i`, the root spoke from `R_i` leads to one star centre. In the canonical star of Cell `i-1`, the same rooted interface leads to a different star centre.

Placing both interiors on the same side of one physical `R_i` in one cubic graph would either:

- give excessive degree at the shared corolla; or
- force centre identifications around the cycle and violate cubicity.

Therefore:

\[
\boxed{
\text{six compatible canonical charts}
\ne
\text{one simultaneous cubic source graph}.}
\]

No R2.6 proof may use such a state.

---

## 2. The intended history-section object

The annular neighbourhood is a two-dimensional history cell complex. Each longitudinal cell corresponds to one local Ptolemy comparison, and adjacent cells meet along complete rooted history interfaces.

A **canonical history section** is a one-dimensional subcomplex

\[
\mathcal T_{C_6}^\star
\]

which runs once around the annulus and satisfies:

1. every section vertex is one complete root-valued cubic source state;
2. every section edge is one legal root-preserving NNI or identity history move;
3. inside Cell `i`, the section uses the canonical star local restriction;
4. at the interface of Cells `i-1,i`, the terminal complete state from one side is literally the initial complete state from the other;
5. no source state contains both neighbouring star interiors simultaneously;
6. all exterior incidence, side-root, cap, route and rooted-carrier data agree.

The section is a sequence of states through history time, not a union of all local star interiors in physical source space.

---

## 3. What the local `(0,2,2)` theorem supplies

For each cell and each annular boundary side:

- the local root restriction is cross or canonical star;
- cross reaches star by one relative root NNI;
- the NNI fixes both turn corollas and every exterior incidence.

Thus every individual cell has a legal root path to its canonical local restriction.

This gives the local vertical edges of a canonicalisation strip.

It does not by itself identify the longitudinal inner boundary of all six strips as a legal history cycle.

---

## 4. Required cellular construction

PDL must give an explicit finite subdivision of the annular history neighbourhood with:

### Cellwise strips

For each longitudinal cell `i`, attach a root-valued strip implementing either:

- the identity if the boundary restriction is already canonical; or
- the unique relative root NNI from cross to star.

Every new strip vertex must be an existing endpoint state of that NNI; no barycentric source state is invented.

### Interface gluing

At every shared turn interface:

- the two cellwise strips fix the same complete rooted corolla pointwise;
- their complete endpoint source states agree on the whole overlap, not only on root values;
- the two strips are attached on opposite history-cell sides, never as two simultaneous source subgraphs.

### Inner boundary

After gluing all six strips, identify the inner boundary cycle explicitly. List its complete source states and legal history edges.

This inner boundary is the object denoted

\[
\mathcal T_{C_6}^\star.
\]

### Theorem target

Prove that `T_C6^star` is a genuine closed root-valued history and that both annular boundary histories admit root-valued homotopies to it relative to all exterior data.

---

## 5. The root cylinder

Only after Section 4 is proved may one concatenate

\[
\partial_-N(\gamma)
\rightsquigarrow
\mathcal T_{C_6}^\star
\leftsquigarrow
\partial_+N(\gamma).
\]

The middle identity is the product of a **history cycle** with an interval:

- source topology may vary along the longitudinal history coordinate;
- each longitudinal state is held constant only in the transverse product direction.

It is not a cylinder on one globally constant source graph.

This distinction resolves the old PDL scope correction.

---

## 6. Minimal acceptance test

A valid PDL R2.6 proof must answer yes, with explicit source data, to all of:

1. Is every vertex of `T_C6^star` one complete cubic source state?
2. Is every edge one root-preserving history move?
3. Are adjacent cell endpoints literally equal as complete states?
4. Is each shared corolla used only once in each source state?
5. Are the six chart interiors separated in history time?
6. Is the cyclic closing seam source-faithful?
7. Are cap block, route, crossed sheet, side roots and rooted carriers preserved?
8. Does the construction avoid equal-face cancellation and lower-order recursion?

If any item is supplied only by static local-chart compatibility, R2.6 remains open.

---

## 7. Relation to `C8`, open strips and periodic seams

The same dimensional discipline is required downstream.

### `C8`

The two `C6` history cylinders must be glued along a legal shared history seam, not by placing two complete hexagon interiors in one state.

### Open strip

The common canonical star strip must be a legal longitudinal history; switch--pop collars occur only at its short boundary.

### Periodic seam

The root crosscut is taken in the legal `1`-skeleton of the already constructed root history cylinder. It cannot repair a missing legal `C6` history section retroactively.

---

## 8. Assurance boundary

### Exact here

- rejection of the simultaneous-star source state;
- distinction between a source graph and a history section;
- exact cellular data required to realise the section;
- correct interpretation of the middle product cylinder;
- acceptance tests for PDL R2.6.

### Not claimed here

- that the required section has already been independently reconstructed;
- PDL R2.6 completion;
- R2.7 or global five-support assurance;
- Lean, manuscript, curation, release or publication status.
