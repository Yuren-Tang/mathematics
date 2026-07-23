# Closed defect tracks erase from a minimal lifted Ptolemy diagram

## Research Lead diagrammatic global theorem v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Parents:**

- `PTOLEMY_CONTEXTUAL_COHERENCE_SCOPE_CORRECTION_V1.md`;
- `CONSTANT_PIVOT_FULL_STATE_CONTEXTUAL_CONSUMPTION_V1.md`;
- `FORCED_DDD_BACKBONE_BINARY_TRANSPORT_V1.md`;
- `ORIENTED_ODD_PETERSEN_SUBTRACK_EXCLUSION_V1.md`;
- `PETERSEN_EVEN_TRACK_ROOT_ANNULUS_REPLACEMENT_V1.md`;
- the first-failure nonbranching and critical-overlap theorems.

**Status:** exact closure of the global *closed-track* gap identified by the Ptolemy scope correction. A defect component in a lifted Ptolemy diagram is nonbranching. After full-state constant-pivot reduction and backtrack deletion, every closed component has a simple Petersen core of length `5,6,8,9`. Constant-pivot loops rootify; odd cores are forbidden by the oriented cap character; even cores have root-valued annular replacements. Hence every closed singular component is either impossible or removable without changing the labelled boundary of the lifted diagram.

**Scope:** this theorem eliminates internal closed defect components. It does not yet dispose of open defect arcs ending on the boundary of a history diagram. Complete contextual transfer remains open precisely at that boundary-arc interface.

---

## 1. Singular lifted diagrams

Let

\[
\mathcal D
\]

be one finite Ptolemy van Kampen diagram for a fixed marked-surface flip comparison. A **contextual lift** of `D` records at every history vertex and edge:

- the complete cubic source topology;
- root labels on every ordinary source edge;
- the ordered outer incidences and cap route;
- optionally one normalized zero/co-root first-failure atom;
- all support transport, side attachments, and resolution-sheet data.

The local involution, square, and pentagon theorems imply that the singular locus is a one-dimensional subcomplex

\[
\mathscr S(\mathcal D)
\]

with no branching after immediate defect-tree normalization.

Thus every connected component of `S(D)` is either:

1. a closed track in the interior of `D`;
2. an open arc whose endpoints lie on the boundary or at an accepted terminal/exit cell.

The present theorem concerns the first type.

---

## 2. Complexity of a lifted diagram

For a contextual lift define

\[
\mathfrak C(\mathcal D)
=
\bigl(c(\mathcal D),s(\mathcal D)\bigr),
\]

ordered lexicographically, where:

- `c(D)` is the number of closed connected components of `S(D)`;
- `s(D)` is the total number of singular track edges after local normalization.

Both are finite nonnegative integers.

A diagram is **closed-track minimal** if its labelled outer boundary is fixed and `C(D)` is minimal among all contextual lifts obtainable by the established relative root movies and local Ptolemy replacements.

---

## 3. Full-state reduction of one closed component

Let

\[
\gamma\subset\mathscr S(\mathcal D)
\]

be one closed component. Retain its full source data.

### Step 3.1 — zero cannot persist

A persistent closed component is co-root/DDD. Every zero atom either rootifies immediately or belongs to a bounded inverse-cancellation interface already recorded separately.

### Step 3.2 — resolve constant-pivot runs

Partition `gamma` into maximal constant-pivot runs and genuine pivot-change cells.

Every constant-pivot run has one unique side-preserving nonpivot root section. Applying it:

- preserves every emitted side root;
- preserves every rooted exterior attachment;
- preserves support transport and the oriented cap block;
- removes the atom from the run.

If the whole closed track has no pivot change, it disappears completely.

### Step 3.3 — delete immediate backtracks

Every immediate pivot backtrack is the established Type-T word

\[
abba.
\]

The two normalized relocations cancel without changing the exterior data. Repeatedly delete all such backtracks.

### Step 3.4 — extract a simple core

If a nonempty closed component remains, choose a shortest positive pivot-closed subtrack. Its reduced Petersen projection is one simple cycle of length

\[
\boxed{5,6,8,9.}
\]

All constant-run decorations remain as fixed rooted branches.

---

## 4. Odd cores are impossible

The original cap distinguishes one block of the fixed physical route. Forced-backbone transport preserves that block.

The crossed-resolution orientation character equals pivot-length parity. Therefore every physical pivot-closed segment must have even length.

Consequently a simple core of length

\[
5\quad\text{or}\quad9
\]

cannot occur in a valid oriented contextual lift.

This excludes odd cores before any double traversal or full-state recurrence is formed.

---

## 5. Even cores are removable

Suppose the simple core has length `6` or `8`.

By `PETERSEN_EVEN_TRACK_ROOT_ANNULUS_REPLACEMENT_V1.md`, a sufficiently small annular neighbourhood

\[
N(\gamma)
\]

has a singularity-free root-valued replacement

\[
N^\root(\gamma)
\]

with exactly the same labelled two-sided boundary history.

Replace `N(gamma)` inside `D` by `N^root(gamma)`.

The replacement:

1. removes the complete closed component `gamma`;
2. preserves every diagram cell and source incidence outside `N(gamma)`;
3. preserves all outer boundary histories;
4. introduces no zero or co-root edge;
5. preserves the cap shore, route, side roots, and all rooted decorations.

Hence

\[
\boxed{
\mathfrak C(\mathcal D')
<
\mathfrak C(\mathcal D).
}
\]

The first coordinate drops by one.

---

## 6. Closed-track erasure theorem

### Theorem 6.1 — no closed component in a minimal lift

A closed-track-minimal contextual lift of a finite Ptolemy diagram contains no internal closed singular component.

### Proof

Assume a closed component `gamma` exists.

1. If it has no pivot change, the unique constant-pivot root section removes it.
2. Otherwise delete all immediate backtracks and extract a shortest simple Petersen core.
3. An odd core is forbidden by orientation.
4. An even core has a root-annulus replacement and can be deleted.

In every possible case the alleged component is impossible or produces a lift with strictly smaller `C(D)`, contradicting minimality. ∎

---

## 7. Repair of the global Ptolemy scope correction

The earlier scope correction identified the false implication

\[
\text{every local cell is controlled}
\Longrightarrow
\text{every global closed atom track is one local }C_5/C_6.
\]

The repaired chain is now:

\[
\begin{aligned}
&\text{local cells give a nonbranching full-state track}\\
&\Downarrow\\
&\text{forced-backbone reduction gives a simple }C_5,C_6,C_8,C_9\text{ core}\\
&\Downarrow\\
&\text{odd orientation exclusion or even root-annulus replacement}\\
&\Downarrow\\
&\text{closed component erasure}.
\end{aligned}
\]

Thus global multi-cell support is no longer collapsed incorrectly to one five-leaf neighbourhood.

### Corollary 7.1 — closed contextual monodromy is diagrammatically trivial

Any internal closed first-failure component in a lifted Ptolemy comparison can be removed while fixing the complete labelled outer boundary.

This is a diagrammatic statement. It does not assert that all root flows on one graph are Kempe equivalent or that one canonical section is a single source state.

---

## 8. Why cancellation re-entry is avoided

The even-track replacement uses only root-preserving relative NNIs and identity history subdivisions. It does not cancel the equal-face dipole visible in the canonical star.

Therefore it does not create:

- a smaller graph requiring an arbitrary new root flow;
- a marked inverse-weld obligation;
- a zero/co-root re-entry after reinsertion;
- a target-order recursion edge.

The cancellation re-entry gap remains real for arguments which use cancellation, but it is bypassed for the closed-track branch.

---

## 9. Remaining open defect arcs

After Theorem 6.1, a minimal singular lift has only open arcs.

Every such arc has endpoints on:

- the two compared boundary histories;
- a route/profile escape cell;
- a bounded direct terminal;
- or another explicitly accepted boundary/category exit.

The next theorem must prove a strict boundary progress statement. A natural target is:

> choose an outermost open defect arc; the boundary interval which it cuts off is strictly shorter than the current comparison interval, and the interval admits either a root-valued replacement or one accepted endpoint discharge.

This is now the sole diagrammatic obstruction to complete same-order contextual transfer.

---

## 10. Assurance boundary

### Exact here

- definition of finite closed-track complexity;
- full-state reduction of every closed component;
- constant-pivot and backtrack consumption;
- simple Petersen core extraction;
- odd-core impossibility;
- even-core root-annulus erasure;
- absence of closed singular components in a minimal lift;
- repair of the global multi-cell gap for closed tracks.

### Imported authorial mathematics

- nonbranching first-failure grammar;
- Ptolemy-track/backbone identification;
- constant-pivot root sections;
- oriented odd-subtrack exclusion;
- even-track root-annulus replacement.

### Still open

- endpoint classification and strict descent for open defect arcs;
- conversion of closed-track erasure into complete contextual inverse transfer;
- one-cross cap restoration and global five-support closure;
- downstream proof development or independent verification;
- Lean verification, manuscript integration, release, arXiv, DOI, peer review, or publication.
