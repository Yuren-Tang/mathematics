# Periodic outer endpoints supply their own root-valued seam

## Research Lead periodic-discharge theorem v1.1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`

**Parents:**

- `CONTEXTUAL_TRANSFER_REPAIR_FRONTIER_V2.md`;
- `PTOLEMY_CLOSED_DEFECT_TRACK_ERASURE_V1.md`;
- `PETERSEN_EVEN_TRACK_ROOT_ANNULUS_REPLACEMENT_V1.md`;
- `OPEN_TRACK_ROOT_STRIP_ENDPOINT_SCOPE_CORRECTION_V1.md`;
- continuation-normalized endpoint finiteness from the full-state contextual graph.

**Correction from v1:** an arbitrary topological subdivision of a root annulus does not automatically create new source states or legal root-history edges. The root seam is instead obtained by a **marked-seam closed-track reduction** using only the explicit source-faithful constant-pivot, backtrack and `C6/C8` canonicalisation movies. Once the marked seam is root-normalized, cutting the cylinder turns the remaining singular component into an open track with root-normalized endpoints, so the corrected open-strip theorem applies.

**Status:** exact diagrammatic discharge of the periodic outer-endpoint branch isolated in `CONTEXTUAL_TRANSFER_REPAIR_FRONTIER_V2.md`. If one unresolved complete outer endpoint state returns to itself, close the intervening episode to a history cylinder and mark the return seam. Reduce the closed singular component until the marked seam is met by an explicit root section or root-annulus cell. This supplies a genuine root-valued source-history seam. Cut there and erase the remaining open track by the normalized-endpoint strip theorem. The two unresolved endpoint sides are replaced by root-normalized sides, strictly lowering the number of unresolved outer endpoint occurrences. Therefore a minimal continuation diagram has no repeated unresolved endpoint state. Since the normalized endpoint state space is finite, every continuation reaches a root/profile/route/bounded/separator exit.

This theorem closes **Target 4.1 — periodic outer-endpoint discharge** at the Research Lead authorial level, conditional only on the parent full-labelled track, source-faithful normalization, annulus and open-strip theorems. It does not by itself certify the complete R2.7 master, PDL reconstruction, audit, Lean verification, manuscript integration, release, or the global five-support theorem.

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

Consumed history words are transition data, not new state coordinates. Thus, at fixed finite `C_0`, the normalized endpoint state set

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

The identified endpoint collar determines one marked transverse seam

\[
\eta_E
\]

through the corresponding point of `\widehat\gamma_E`.

### Lemma 2.1 — collar closure is an interior marked closed track

After shrinking the endpoint collars before identification, `\widehat\gamma_E` has a two-sided annular regular neighbourhood in the history cylinder, and `\eta_E` is a marked local transverse class through that neighbourhood. Hence `\widehat\gamma_E` is an internal closed singular component in the sense of `PTOLEMY_CLOSED_DEFECT_TRACK_ERASURE_V1.md`, with one distinguished seam position.

### Proof

The complete endpoint identification matches the two one-sided local germs of the co-root track, not merely the coefficient label. Gluing the collars joins the two terminal half-edges of the singular locus into one degree-two point. The two root-valued sides also glue in order. Hence the closed component has a product neighbourhood `S^1 times (-epsilon,epsilon)`. The image of the endpoint collar supplies the marked transverse class `\eta_E`. ∎

---

## 3. Marked-seam closed-track reduction

The ordinary closed-track theorem minimizes the number and total length of closed singular components. For periodic discharge, retain the marked seam position `\eta_E` throughout that reduction.

Let

\[
\mathfrak C_\eta
\]

be the closed-track complexity of the component containing `\eta_E`, together with its number of normalized singular edges. Apply the established source-faithful reductions.

### Case 3.1 — the marked point lies in a constant-pivot run

The unique side-preserving nonpivot root section rootifies the complete run. At the marked position it gives an explicit legal root-valued history path between the two root sides. This is the required root seam.

### Case 3.2 — the marked point lies in an immediate pivot backtrack

The normalized Type-T backtrack deletion is source-faithful and fixes all exterior side attachments. Applying it to the marked `abba` unit gives an explicit root-valued local replacement across the marked position. This is the required root seam.

### Case 3.3 — a selected simple core is disjoint from the marked point

Resolve constant-pivot decorations and delete backtracks as in the closed-track theorem. Choose one shortest simple Petersen core.

- Odd `C5/C9` is impossible by the oriented cap character.
- Even `C6/C8` has the established root-annulus replacement.

If the chosen core is disjoint from `\eta_E`, perform the replacement while retaining the marked collar pointwise. The closed-track complexity strictly decreases and the marked singular point survives on the remaining component.

Repeat.

### Case 3.4 — the selected even core contains the marked point

For a `C6` cell at the marked position, both root sides are explicitly one of the root cross topology and the canonical star, and each canonicalises to the same star by at most one relative root NNI. The concatenation

\[
X^-\rightsquigarrow S^\star\leftsquigarrow X^+
\]

is therefore a genuine root-valued source-history path across the marked position.

For `C8`, use the seam-compatible two-`C6` filling; the factor containing the marked position supplies the same explicit root path while the other factor is held relative to the common rooted seam data.

This is the required root seam.

### Theorem 3.1 — marked root-seam theorem

The marked-seam reduction terminates and supplies a genuine root-valued source-history path

\[
\sigma_E
\]

across the original return seam.

### Proof

Every reduction disjoint from the marked point strictly lowers finite closed-track complexity. Therefore such reductions cannot continue indefinitely. If the marked component disappears, its final removal necessarily meets the marked point and falls under Cases 3.1, 3.2 or 3.4. Odd marked cores are impossible. In every remaining marked case, the parent local theorem supplies an explicit path made only of root-preserving relative NNIs, unique root sections and identity history steps. No artificial barycentric source state is introduced. ∎

The path `\sigma_E` fixes the complete exterior incidence, cap block, route and side-root data.

---

## 4. Cut at the root seam

Cut `\widehat{\mathcal R}_E` along the explicit root seam `\sigma_E`.

Any singular part of the original closed component not already removed becomes an open nonbranching co-root track. Its two short endpoint sides are now the two root-valued copies of `\sigma_E`. Therefore both endpoints are Type 1 root-normalized endpoints in the sense of `OPEN_TRACK_ROOT_STRIP_ENDPOINT_SCOPE_CORRECTION_V1.md`.

Apply the retained open-strip theorem. It replaces the remaining open track by a root-valued history rectangle fixing:

- the two long root histories;
- both copies of `\sigma_E`;
- every exterior source incidence;
- the cap block, route and side attachments.

The result is a finite singularity-free root-valued history rectangle

\[
\mathcal R_E^{\root}
\]

with:

1. the same two long labelled histories as the original tubular neighbourhood of `\gamma_E`;
2. two root-valued short sides supplied by `\sigma_E`;
3. the same complete exterior contextual data;
4. no zero or co-root state.

### Theorem 4.1 — close--reduce--cut--strip discharge

A repeated normalized unresolved outer endpoint state admits a source-faithful diagrammatic replacement which removes the complete intervening co-root track and replaces both endpoint occurrences by root-normalized history sides.

In particular, recurrence of the same complete endpoint state is not a terminal or neutral macro-step.

---

## 5. Strict boundary complexity

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

The close--reduce--cut--strip replacement changes no global starting or accepted terminal data and introduces no new unresolved endpoint side. It replaces two occurrences of `E` by root-valued copies of `\sigma_E`. Hence

\[
\boxed{
U(D')\le U(D)-2.
}
\]

Cell count may increase; it is irrelevant because the first coordinate strictly decreases.

### Corollary 5.1 — no periodic endpoint in a boundary-minimal lift

A contextual continuation diagram minimal in `\mathfrak B` contains no repeated normalized unresolved endpoint state.

---

## 6. Finite endpoint discharge

Consider the finite directed graph on `\mathcal E(C_0)` whose nonexit edges are finite continuation episodes.

Suppose a reachable sink strongly connected component contains no accepted exit. It contains a directed cycle. Concatenating that cycle gives a repeated endpoint episode, contrary to Corollary 5.1.

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

### Theorem 6.1 — periodic outer-endpoint discharge

The periodic branch in `CONTEXTUAL_TRANSFER_REPAIR_FRONTIER_V2.md`, Target 4.1, cannot support an unbounded continuation. Every normalized unresolved outer endpoint is discharged after finitely many episodes.

The proof uses:

- finite normalized endpoint state;
- marked-seam closed-track reduction;
- the explicit root seam supplied by the source movies;
- normalized-endpoint open-strip replacement;
- strict decrease of unresolved endpoint occurrences.

It does not use arbitrary-flow inverse weld, generic Kempe connectivity or target-order descent.

---

## 7. Consequence for the R2.7 frontier

At the Research Lead authorial level, the previously isolated unbounded endpoint is now consumed:

\[
\boxed{
\text{periodic outer endpoint}
\Longrightarrow
\text{marked root seam}
\Longrightarrow
\text{strict boundary progress}.
}
\]

A complete R2.7 theorem still requires one fresh assembly pass checking that:

1. every nonperiodic endpoint alternative is exactly one already accepted root/route/bounded/separator exit;
2. the normalized endpoint graph retains all physical source and cap data;
3. the parent closed-track, source-faithful backtrack, annulus and open-strip theorems are imported with their full hypotheses;
4. the final contextual-transfer statement does not revive any superseded cancellation shortcut.

PDL must reconstruct and independently verify the marked-seam argument before any completion classification is promoted.

---

## 8. Assurance boundary

### Exact here

- closure of a repeated complete endpoint episode to an internal marked full-state track by collar identification;
- marked-relative reduction of the closed component;
- extraction of a genuine root seam from an explicit constant-run, source-faithful backtrack or `C6/C8` canonicalisation movie;
- cutting at that seam;
- application of the corrected root-strip theorem to the residual open track;
- strict decrease of unresolved endpoint occurrences;
- exclusion of nonexit cycles in the finite normalized endpoint graph;
- authorial closure of the periodic endpoint branch.

### Imported authorial mathematics

- full-state nonbranching track identification;
- constant-pivot root sections;
- source-faithful backtrack normalization;
- odd pivot-closed exclusion;
- `C6/C8` root-annulus replacement;
- normalized-endpoint open-strip replacement;
- normalized finite endpoint-state semantics.

### Not claimed

- a completed reassembled R2.7 master theorem;
- PDL reconstruction or independent audit;
- one-cross cap restoration or global five-support closure;
- Lean verification, manuscript integration, release, arXiv, DOI, peer review or publication.
