# Every marked closed co-root track has a direct local root seam

## Research Lead source-faithful correction theorem v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`

**Parents:**

- `CONSTANT_PIVOT_FULL_STATE_CONTEXTUAL_CONSUMPTION_V1.md`;
- the source-faithful Type-T backtrack normalization;
- `PETERSEN_OPEN_TRACK_ROOT_STRIP_REPLACEMENT_V1.md`;
- `OPEN_TRACK_ROOT_STRIP_ENDPOINT_SCOPE_CORRECTION_V1.md`.

**Corrects the proof route of:**

- `PTOLEMY_CLOSED_DEFECT_TRACK_ERASURE_V1.md`;
- Section 3 of `PERIODIC_OUTER_ENDPOINT_ROOT_SEAM_DISCHARGE_V1.md`.

**Correction:** one must not take a shortest simple Petersen pivot subcycle of a longer singular circle and silently treat that coefficient subtrack as a complete physical annulus. A simple pivot subcycle may be only a proper interval of the source-level closed track. The root seam is instead constructed directly at the marked source point. Constant-pivot and backtrack points have their established source-faithful root sections. Every genuine pivot-change point has the general open-cell relative `(0,2,2)` root table, because its consecutive side roots are always distinct intersecting. Thus a genuine root seam exists locally at the mark, without extracting or replacing any pivot subcycle.

**Status:** exact authorial repair of the marked-seam interface, conditional on the listed local source theorems. It does not by itself reassemble contextual transfer.

---

## 1. Marked full-state closed track

Let

\[
\gamma
\]

be one closed nonbranching co-root track in a lifted Ptolemy history cylinder. Fix one marked point

\[
\eta\in\gamma.
\]

The complete track retains:

- the source topology at every history state;
- the co-root value and its two crossed root resolutions;
- every emitted side root;
- constant-pivot support transport;
- all exterior rooted branches;
- the ordered cap shore and physical route.

A **root seam at `eta`** is a genuine finite root-valued source-history path crossing transversely from the root-valued history on one side of `gamma` to the root-valued history on the other side while fixing every exterior incidence and all cap/route data.

---

## 2. Complete local trichotomy at the mark

After the standard one-token normalization, exactly one of the following holds at `eta`.

1. `eta` lies in the interior of a maximal constant-pivot run.
2. `eta` lies in an immediate normalized pivot backtrack.
3. `eta` lies in one genuine nonbacktracking pivot-change cell.

There is no fourth local full-state type.

The classification is source-level: constant runs and backtracks retain all side branches rather than being quotient words.

---

## 3. Constant-pivot mark

Suppose the marked state belongs to a maximal run

\[
F_t=\{s,d_t\}.
\]

The oriented cap lock selects the unique nonpivot root section

\[
r_t=d_t.
\]

This section:

- resolves every co-root state in the run;
- preserves every side-root occurrence;
- fixes every exterior rooted attachment;
- preserves the cap block and route orientation.

Restrict the section to a small marked collar of `eta`.

### Theorem 3.1 — constant-run seam

A marked point in a constant-pivot run has an explicit source-faithful root seam.

---

## 4. Backtrack mark

Suppose the marked point lies in an immediate pivot backtrack

\[
s\to t\to s.
\]

The complete forced resolution word is the source-faithful Type-T unit

\[
\boxed{t,s,s,t}.
\]

The two normalized relocations cancel while every side branch and incidence is retained.

### Theorem 4.1 — backtrack seam

A marked point in one normalized `abba` backtrack has an explicit root-valued local replacement across the marked collar and hence a root seam.

This uses the local source backtrack theorem, not the stronger and unnecessary claim that every abstract Type-T word may be deleted from an arbitrary ambient carrier.

---

## 5. Genuine pivot-change mark

Suppose the marked point lies in a genuine nonbacktracking pivot-change cell with four consecutive pivots

\[
x\to s\to t\to y,
\]

where

\[
x\ne t,
\qquad
s\ne y.
\]

Let the two consecutive side roots be

\[
z=x+t,
\qquad
w=s+y.
\]

The general open-cell theorem gives

\[
\boxed{z\ne w,
\qquad z\cap w\ne\varnothing.}
\]

Hence

\[
u=z+w\in R_5.
\]

The two already resolved turn corollas are

\[
L=(x,t,z),
\qquad
R=(s,y,w).
\]

Relative to these fixed rooted branches, the unresolved middle has branch word

\[
(z,z,w,w).
\]

Its three binary topologies are exactly:

1. one zero path;
2. one root cross path;
3. one root canonical star.

The two root topologies are joined by the unique relative root NNI fixing `L`, `R`, all six boundary incidences and every exterior source edge.

The two root-valued histories on the sides of the singular track therefore each equal the cross path or the star and canonicalise to the same star.

### Theorem 5.1 — pivot-change seam

At every genuine pivot-change marked point there is an explicit source-faithful root seam

\[
X^-
\rightsquigarrow
S^\star
\leftsquigarrow
X^+.
\]

No assumption that the surrounding pivot word is a simple cycle is required.

---

## 6. Direct marked-seam theorem

### Theorem 6.1 — every mark has a root seam

Every marked point on a closed normalized full-state co-root track admits a genuine root-valued source-history seam fixing the complete exterior data.

### Proof

Apply Theorem 3.1, 4.1 or 5.1 according to the local trichotomy of Section 2. ∎

This theorem uses only the local state at the marked point. It does not extract a shortest repeated pivot, does not classify a proper subtrack as an annulus, and does not use target-order cancellation.

---

## 7. Cutting and erasing the complete closed track

Cut the history cylinder along the root seam of Theorem 6.1. The closed singular component becomes one open co-root track whose two short endpoint sides are the two root-valued copies of the seam.

Apply `PETERSEN_OPEN_TRACK_ROOT_STRIP_REPLACEMENT_V1.md`, read through its endpoint correction. Its hypothesis is now satisfied: both short sides are root-normalized.

The strip replacement removes the complete remaining open track while fixing:

- both root seam copies;
- the two long root histories;
- every exterior source incidence;
- all side roots, support transport, cap block and route data.

### Corollary 7.1 — repaired closed-track erasure

Every closed normalized co-root track has a singularity-free root-valued cylinder replacement with the same complete labelled exterior boundary.

The proof is:

\[
\boxed{
\text{direct root seam at one marked point}
\longrightarrow
\text{cut}
\longrightarrow
\text{open root strip}.
}
\]

No simple-cycle subannulus and no equal-face cancellation is used.

---

## 8. Supersession and scope

### Retained from earlier cycle work

- Petersen pivot and side-output classification;
- constant-pivot full-state root sections;
- source-faithful backtrack normalization;
- `C6/C8` annulus constructions as valid bounded closed-cycle movies;
- odd orientation and projectivity calculations.

### No longer needed for marked seam existence

- choosing a shortest simple pivot core;
- erasing simple cores disjoint from the mark;
- proving that a proper pivot subcycle is a complete physical annulus;
- iterating closed-track complexity until the mark is reached.

### Corrected reading

`PTOLEMY_CLOSED_DEFECT_TRACK_ERASURE_V1.md` may retain its conclusion only through Corollary 7.1 of the present file, not through the unsupported use of a proper simple pivot subtrack as a full annulus.

Section 3 of `PERIODIC_OUTER_ENDPOINT_ROOT_SEAM_DISCHARGE_V1.md` is superseded by Theorem 6.1 here.

---

## 9. Assurance boundary

### Exact here

- the source-level local trichotomy at a marked co-root point;
- direct root seam in constant-pivot, backtrack and genuine pivot-change cases;
- use of the general `120/120` consecutive-side intersection theorem at pivot changes;
- cutting a closed track at a genuine root seam;
- application of the normalized-endpoint open-strip theorem to the complete residual track;
- repaired closed-track erasure without a simple-subcycle annulus assumption.

### Imported authorial mathematics

- one-token nonbranching/full-state track grammar;
- constant-pivot root section;
- source-faithful Type-T backtrack normalization;
- arbitrary open-cell relative star theorem;
- open-track root strip with normalized endpoints.

### Not claimed

- a completed reassembled R2.7 master theorem;
- PDL reconstruction or independent audit;
- cap restoration or global five-support closure;
- Lean verification, manuscript integration, release, arXiv, DOI, peer review or publication.
