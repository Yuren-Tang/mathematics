# Periodic outer endpoints supply their own root-valued seam

## Research Lead periodic-discharge theorem v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`

**Parents:**

- `CONTEXTUAL_TRANSFER_REPAIR_FRONTIER_V2.md`;
- `PTOLEMY_CLOSED_DEFECT_TRACK_ERASURE_V1.md`;
- `PETERSEN_EVEN_TRACK_ROOT_ANNULUS_REPLACEMENT_V1.md`;
- `OPEN_TRACK_ROOT_STRIP_ENDPOINT_SCOPE_CORRECTION_V1.md`;
- continuation-normalized endpoint finiteness from the full-state contextual graph.

**Status:** exact diagrammatic discharge of the periodic outer-endpoint branch isolated in `CONTEXTUAL_TRANSFER_REPAIR_FRONTIER_V2.md`. If one unresolved complete outer endpoint state returns to itself, close the intervening episode to a history cylinder, erase its closed singular component by the established root-annulus theorem, and cut the resulting root cylinder along the original return seam. The cut is a genuine root-valued history meridian. It replaces the two unresolved endpoint sides by root-normalized sides and strictly lowers the number of unresolved outer endpoint occurrences. Therefore a minimal continuation diagram has no repeated unresolved endpoint state. Since the normalized endpoint state space is finite, every continuation reaches a root/profile/route/bounded/separator exit.

This theorem closes **Target 4.1 — periodic outer-endpoint discharge** at the Research Lead authorial level, conditional only on the parent full-labelled track and annulus theorems. It does not by itself certify the complete R2.7 master, PDL reconstruction, audit, Lean verification, manuscript integration, release, or the global five-support theorem.

---

## 1. Normalized outer endpoint states

Fix the original target context

\[
C_0
\]

with its ordered cap incidences, distinguished cap block, fixed physical route and complete root-labelled exterior data.

A **normalized unresolved outer endpoint state** records:

1. the source topology at `C_0`;
2. every current root label away from one co-root atom;
3. the atom value and position;
4. both crossed root resolutions;
5. support transport and side-root data;
6. the ordered cap shore and route orientation;
7. all bounded category flags needed by the next finite equality/DDD episode.

Consumed history words are not retained as new state coordinates. They are transition data. Thus, at fixed finite `C_0`, the normalized endpoint state set

\[
\mathcal E(C_0)
\]

is finite.

A nonexit endpoint launches one finite continuation episode. Its next outcome is exactly one of:

- root/cap lift;
- route or profile escape;
- bounded or separator/category exit;
- another state of `\mathcal E(C_0)`.

The only unbounded possibility is therefore an infinite path in the finite directed endpoint graph, hence a repeated endpoint state.

---

## 2. One periodic endpoint episode

Let

\[
E\in\mathcal E(C_0)
\]

occur twice, with no earlier repetition between the two occurrences. Let

\[
\mathcal R_E
\]

be the finite contextual history rectangle carried by the intervening episode.

Its singular locus contains one nonbranching co-root arc

\[
\gamma_E
\]

joining the two short endpoint sides labelled by the same complete state `E`. All ordinary history immediately on the two sides of `\gamma_E` is root-valued.

Because the two endpoint states agree in the complete labelled sense, their small endpoint collars agree pointwise:

- same source incidences;
- same co-root edge and crossed resolutions;
- same support transport;
- same cap block and route orientation.

Identify the two short collars by this equality. The result is a finite history cylinder

\[
\widehat{\mathcal R}_E.
\]

The identified arc becomes one closed nonbranching full-state singular component

\[
\widehat\gamma_E.
\]

### Lemma 2.1 — collar closure is an interior closed track

After shrinking the endpoint collars before identification, `\widehat\gamma_E` has a two-sided annular regular neighbourhood in the history cylinder. It is therefore an internal closed singular component in the sense of `PTOLEMY_CLOSED_DEFECT_TRACK_ERASURE_V1.md`.

### Proof

The complete endpoint identification matches the two one-sided local germs of the co-root track, not merely the coefficient label. Gluing the collars joins the two terminal half-edges of the singular locus into one degree-two point. The two root-valued sides also glue in order. Hence the closed component has a product neighbourhood `S^1 times (-epsilon,epsilon)` after the standard cell subdivision. ∎

---

## 3. Erasing the periodic closed component

Apply the closed-track theorem to `\widehat\gamma_E`.

The full-state reduction gives exactly the established alternatives:

1. no pivot change: the unique side-preserving root section removes the component;
2. immediate pivot backtracks: source-faithful normalized deletion;
3. odd reduced core `C5/C9`: impossible by the oriented cap character;
4. even reduced core `C6/C8`: root-annulus replacement.

Iterating the strict closed-track complexity reduction removes the complete component. We obtain a singularity-free root-valued history cylinder

\[
\widehat{\mathcal R}^{\root}_E
\]

with the same labelled two-sided exterior history as `\widehat{\mathcal R}_E`.

No equal-face cancellation, arbitrary lower-order flow choice or inverse-weld selection is used.

---

## 4. Root meridians in a root history cylinder

The root-annulus replacement is not merely an abstract homotopy class. It is assembled from finitely many root-preserving relative NNIs and identity history subdivisions.

### Lemma 4.1 — root seam lemma

After a finite cellular subdivision, the homotopy class of the original endpoint-identification seam contains a transverse edge path

\[
\sigma_E
\]

joining the two boundary histories of `\widehat{\mathcal R}^{\root}_E`, such that every source state and every history edge along `\sigma_E` is root-valued.

The path fixes the complete exterior incidence, cap-block, route and side-root data.

### Proof

The constructed replacement is a finite root-valued history cylinder. Subdivide each root NNI cell so that a chosen transverse meridian lies in the one-skeleton. Every vertex of the subdivided cylinder is one of the source states in the root canonicalisation movies, and every edge is a root-preserving NNI or identity step. Exterior data are fixed cellwise by the parent annulus theorem. ∎

This lemma does **not** assert that all canonical charts form one simultaneous cubic source graph. `\sigma_E` is a one-dimensional history path through the two-dimensional cylinder.

---

## 5. Close--erase--cut

Cut `\widehat{\mathcal R}^{\root}_E` along `\sigma_E`.

The cut cylinder is a finite root-valued history rectangle

\[
\mathcal R_E^{\root}
\]

with:

1. the same two long labelled histories as the original tubular neighbourhood of `\gamma_E`;
2. two copies of the root-valued meridian `\sigma_E` as its short sides;
3. the same exterior source incidences, cap block, route and side attachments;
4. no zero or co-root state.

Thus the periodic co-root episode is replaced by a root-valued rectangle. The original unresolved short sides labelled by `E` are absent.

### Theorem 5.1 — periodic endpoint root-seam discharge

A repeated normalized unresolved outer endpoint state admits a source-faithful diagrammatic replacement which removes the complete intervening co-root track and replaces both endpoint occurrences by root-normalized history sides.

In particular, recurrence of the same complete endpoint state is not a terminal or neutral macro-step.

---

## 6. Strict boundary complexity

For a finite contextual continuation diagram `D`, let

\[
U(D)
\]

be the number of short boundary sides carrying unresolved outer co-root endpoint states. Refine, if needed, by

\[
\mathfrak B(D)=\bigl(U(D),s(D),A(D)\bigr),
\]

ordered lexicographically, where:

- `s(D)` is the number of normalized singular-track edges;
- `A(D)` is the number of history cells.

The close--erase--cut replacement changes no global starting or accepted terminal data and introduces no new unresolved endpoint side. It replaces two occurrences of `E` by root-valued copies of `\sigma_E`. Hence

\[
\boxed{
U(D')\le U(D)-2.
}
\]

Cell count may increase; it is irrelevant because the first coordinate strictly decreases.

### Corollary 6.1 — no periodic endpoint in a boundary-minimal lift

A contextual continuation diagram minimal in `\mathfrak B` contains no repeated normalized unresolved endpoint state.

---

## 7. Finite endpoint discharge

Consider the finite directed graph on `\mathcal E(C_0)` whose nonexit edges are finite continuation episodes.

Suppose a reachable sink strongly connected component contains no accepted exit. It contains a directed cycle. Concatenating that cycle gives a repeated endpoint episode, contrary to Corollary 6.1.

Therefore every reachable endpoint state has a finite path to one of:

\[
\boxed{
\text{cap-compatible rootification},
\quad
\text{route/profile escape},
\quad
\text{bounded or separator/category exit}.
}
\]

### Theorem 7.1 — periodic outer-endpoint discharge

The periodic branch in `CONTEXTUAL_TRANSFER_REPAIR_FRONTIER_V2.md`, Target 4.1, cannot support an unbounded continuation. Every normalized unresolved outer endpoint is discharged after finitely many episodes.

The proof uses:

- finite normalized endpoint state;
- closed-track root-annulus erasure;
- the root seam lemma;
- strict decrease of unresolved endpoint occurrences.

It does not use arbitrary-flow inverse weld, generic Kempe connectivity or target-order descent.

---

## 8. Consequence for the R2.7 frontier

At the Research Lead authorial level, the previously isolated unbounded endpoint is now consumed:

\[
\boxed{
\text{periodic outer endpoint}
\Longrightarrow
\text{root seam}
\Longrightarrow
\text{strict boundary progress}.
}
\]

A complete R2.7 theorem still requires one fresh assembly pass checking that:

1. every nonperiodic endpoint alternative is exactly one already accepted root/route/bounded/separator exit;
2. the normalized endpoint graph retains all physical source and cap data;
3. the parent closed-track and annulus theorems are imported with their full hypotheses;
4. the final contextual-transfer statement does not revive any superseded cancellation shortcut.

PDL must reconstruct and independently verify the close--erase--cut seam argument before any completion classification is promoted.

---

## 9. Assurance boundary

### Exact here

- closure of a repeated complete endpoint episode to an internal full-state track by collar identification;
- applicability of closed-track erasure to the resulting cylinder;
- existence of a root-valued transverse meridian in the constructed root history cylinder;
- cutting the cylinder to a root-valued rectangle;
- strict decrease of unresolved endpoint occurrences;
- exclusion of nonexit cycles in the finite normalized endpoint graph;
- authorial closure of the periodic endpoint branch.

### Imported authorial mathematics

- full-state nonbranching track identification;
- constant-pivot and source-faithful backtrack normalization;
- odd pivot-closed exclusion;
- `C6/C8` root-annulus replacement;
- normalized finite endpoint-state semantics.

### Not claimed

- a completed reassembled R2.7 master theorem;
- PDL reconstruction or independent audit;
- one-cross cap restoration or global five-support closure;
- Lean verification, manuscript integration, release, arXiv, DOI, peer review or publication.
