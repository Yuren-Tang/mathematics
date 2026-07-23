# Periodic outer endpoints supply their own root-valued seam

## Research Lead periodic-discharge theorem v1.2

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`

**Parents:**

- `CONTEXTUAL_TRANSFER_REPAIR_FRONTIER_V2.md`;
- `PTOLEMY_CLOSED_DEFECT_TRACK_ERASURE_V1.md`;
- fixed-order normalization and finite complete endpoint semantics in `ROOT_NORMALIZED_CONTEXTUAL_TRANSFER_MASTER_V5.md`.

**Supersedes:** v1.0 and v1.1 of this file.

**Correction:** no arbitrary subdivision is used, and no marked point must be transported through individual reduction cores. The closed-track theorem already replaces the complete periodic singular component by a finite connected root-valued history cylinder. Its ordinary history `1`-skeleton is connected; a shortest `1`-skeleton path between the two boundary histories is a genuine root-valued crosscut made only of legal source-history edges. Cutting the cylinder along that crosscut gives the required root-valued rectangle directly. No residual open track remains.

**Status:** exact diagrammatic discharge of the periodic outer-endpoint branch. A repeated complete endpoint episode can be replaced by a fully root-valued history rectangle with the same long boundary histories and complete exterior contextual data. The replacement removes two unresolved endpoint occurrences. Hence the finite endpoint graph has no nonexit directed cycle.

This closes **Target 4.1 — periodic outer-endpoint discharge** at Research Lead authorial level, conditional on the full hypotheses of the closed-track erasure theorem and fixed-order endpoint normalization. It is not PDL acceptance, independent audit, Lean verification, manuscript integration, release or universal five-CDC status.

---

## 1. Normalized endpoint states

Fix one original context

\[
C_0
\]

with ordered cap incidences, distinguished cap block, fixed route and complete labelled exterior data.

A normalized unresolved endpoint state records:

1. the predecessor-order source topology;
2. every root label away from one co-root atom;
3. the atom position, value and two crossed resolutions;
4. support transport, side roots and rooted attachments;
5. cap block, route orientation and bounded/category flags.

History words are transition witnesses, not state coordinates. At fixed finite order the endpoint set

\[
\mathcal E(C_0)
\]

is finite.

Every continuation episode is normalized back to predecessor order before it defines an edge of the endpoint graph. In particular, any temporary forward equal-face cancellation has already been returned through the original or alternative insertion table. Thus a periodic episode is a fixed-order full-state history, not a nested lower-order object.

---

## 2. Closing one repeated episode

Let

\[
E\in\mathcal E(C_0)
\]

occur twice, and let

\[
\mathcal R_E
\]

be the finite intervening history rectangle. Its singular locus contains one nonbranching co-root arc

\[
\gamma_E
\]

joining the two short sides carrying the identical complete state `E`. The two long sides are root-valued histories.

Because the endpoint data agree pointwise, identify the two short collars. The result is a finite history cylinder

\[
\widehat{\mathcal R}_E,
\]

and `gamma_E` closes to one internal full-state singular component

\[
\widehat\gamma_E.
\]

### Lemma 2.1 — periodic closure is an internal closed track

The component `widehat gamma_E` has a two-sided annular regular neighbourhood, and its two boundary histories are exactly the two root-valued long sides of the original rectangle.

### Proof

The complete endpoint identification matches source incidences, atom edge, crossed resolutions, support transport, cap block and route orientation. It joins the two terminal half-edges of the nonbranching singular locus into one degree-two point and glues the two root-valued side germs in order. Hence the track has a product annular neighbourhood. ∎

---

## 3. Complete root-cylinder replacement

Apply `PTOLEMY_CLOSED_DEFECT_TRACK_ERASURE_V1.md` to `widehat gamma_E`.

The full-state alternatives are:

- constant-pivot root section;
- normalized backtrack deletion;
- odd `C5/C9` impossibility;
- even `C6/C8` root-annulus replacement.

Iterating the strict closed-track complexity reduction removes the complete closed singular component. We obtain a finite singularity-free root-valued history cylinder

\[
\widehat{\mathcal R}^{\root}_E
\]

with the same two labelled boundary histories and the same complete exterior source, cap, route and side data.

No equal-face cancellation, arbitrary lower-order flow, marked-weld selection or graph-order induction is used in this replacement.

---

## 4. The root crosscut lemma

Regard `widehat R_E^root` as the finite history cell complex produced by the explicit root movies.

- Every `0`-cell is a genuine root-valued source state.
- Every `1`-cell is a legal root-preserving relative NNI or identity history step.
- The two boundary histories are disjoint connected subcomplexes of the `1`-skeleton.

### Lemma 4.1 — connected root `1`-skeleton

The `1`-skeleton of `widehat R_E^root` is connected.

### Proof

A `2`-cell is attached along a connected loop in the existing `1`-skeleton and cannot join two previously disconnected `1`-skeleton components. Since the complete history cylinder is connected, its `1`-skeleton must already be connected. ∎

Choose a shortest `1`-skeleton path

\[
\sigma_E
\]

between the two boundary vertex sets.

### Lemma 4.2 — root crosscut

The path `sigma_E` is a simple proper arc joining the two boundary histories, with no other boundary vertex in its interior. Every vertex and edge of `sigma_E` is a genuine root-valued source-history state or move.

### Proof

A shortest graph path is simple. If an internal vertex lay on either boundary, the path could be shortened by beginning or ending there. Thus the interior is disjoint from both boundary components. An embedded arc joining the two boundary components of a cylinder is a crosscut. The root-history assertion follows from the definition of the `1`-skeleton. ∎

This is the required seam. No barycentric vertex or artificial source state is introduced.

---

## 5. Cut the root cylinder

Cut `widehat R_E^root` along the root crosscut `sigma_E`.

The result is a finite fully root-valued history rectangle

\[
\mathcal R_E^{\root}
\]

whose boundary consists of:

1. the same two long labelled histories as `R_E`;
2. two copies of the root history path `sigma_E` as short sides.

All exterior incidences, cap block, route orientation, support transport and side attachments are unchanged. No singular component remains.

### Theorem 5.1 — periodic endpoint rectangle replacement

A repeated normalized unresolved endpoint episode admits a source-faithful replacement by a fully root-valued history rectangle with the same long boundary data.

The two unresolved short sides labelled by `E` are replaced by root-valued short sides.

---

## 6. Strict boundary progress

For a finite continuation diagram `D`, let

\[
U(D)
\]

be the number of unresolved outer endpoint occurrences.

The root-cylinder cut replacement introduces no unresolved occurrence and removes the two copies of `E`. Therefore

\[
\boxed{U(D')\le U(D)-2.}
\]

Cell count and path length may increase; they are irrelevant because the first boundary coordinate strictly decreases.

### Corollary 6.1 — no repeated endpoint in a boundary-minimal diagram

A continuation diagram minimal in unresolved endpoint count contains no repeated complete endpoint state.

---

## 7. Finite endpoint discharge

Consider the finite directed graph on `mathcal E(C_0)` whose edges are normalized nonexit continuation episodes.

### Theorem 7.1 — periodic outer-endpoint discharge

Every reachable endpoint state has a finite path to:

\[
\boxed{
\text{cap-compatible rootification},
\quad
\text{route/profile escape},
\quad
\text{bounded or separator/category exit}.}
\]

### Proof

If a reachable sink strongly connected component had no exit, it would contain a directed cycle. Concatenating that cycle produces a repeated complete endpoint episode. Theorem 5.1 replaces it by a root-valued rectangle and strictly lowers unresolved endpoint count, contradicting boundary minimality. ∎

This proves existence of an exit path. It does not assert termination of every arbitrary nondeterministic scheduling choice.

---

## 8. Consequence and assurance boundary

At Research Lead authorial level,

\[
\boxed{
\text{periodic outer endpoint}
\Longrightarrow
\text{root cylinder}
\Longrightarrow
\text{root crosscut}
\Longrightarrow
\text{strict boundary progress}.}
\]

### Exact here

- closure of identical complete endpoint collars to an internal closed track;
- application of complete closed-track erasure;
- connectedness of the legal root-history `1`-skeleton;
- existence of a shortest root crosscut;
- cutting to a fully root-valued rectangle;
- strict decrease of unresolved endpoint occurrences;
- exclusion of nonexit endpoint cycles.

### Imported authorial mathematics

- fixed-order normalization of every continuation episode;
- full-state nonbranching track identification;
- constant-pivot and normalized backtrack consumption;
- odd pivot-closed exclusion;
- `C6/C8` root-annulus replacement;
- finite complete endpoint semantics.

### Not claimed

- PDL reconstruction or independent audit;
- global R2 assurance, cap restoration or universal five-CDC acceptance;
- Lean verification, manuscript integration, curation, release, arXiv, DOI, peer review or publication.
