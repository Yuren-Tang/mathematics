# AC-PD-5CDC-R2.5 — even-track cylinder erasure

**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Programme:** compressed five-support proof, global return repair  
**Classification:** `COMPLETE-DRAFT / CO-ROOT RECURRENCE REPAIRED / EQUALITY-CANCELLATION RETURN OPEN`.

This dossier strengthens the even-core consumer. The existing relative Petersen `C6` movie is used to remove a closed co-root track at the same cap-target order. The internal equal-face cancellation in the canonical star is not needed for this purpose.

Controlling inputs:

- the full-labelled forced-backbone annulus;
- `PETERSEN_C6_CANONICAL_STAR_SECTION_V1.md`;
- `PETERSEN_C6_RELATIVE_STAR_MOVIE_DESCENT_V1.md`;
- `PETERSEN_C8_TWO_C6_HISTORY_FILLING_REDUCTION_V1.md`;
- fixed turn-corolla and side-root overlap data.

---

## 1. Relative annular input

Let `A` be a sufficiently small regular neighbourhood of one closed persistent co-root track in a lifted history diagram. Assume its reduced Petersen core is a simple `C6`.

The annulus has two root-valued boundary lifts

\[
\partial_-A,
\qquad
\partial_+A.
\]

At every pivot-change cell `i`, both boundary restrictions retain the same two resolved turn corollas

\[
R_i,
\qquad
R_{i+1},
\]

and the same two emitted side roots. Relative to these fixed rooted branches, the local boundary topology is one of exactly two root states:

\[
P_i^\times,
\qquad
S_i^\star.
\]

The unique root NNI

\[
P_i^\times\leftrightarrow S_i^\star
\]

fixes both turn corollas and every exterior incidence.

---

## 2. Canonicalisation of each boundary circle

Apply the unique relative NNI at every cell whose boundary restriction is `P_i^times`; do nothing at a cell already equal to `S_i^star`.

Adjacent moves are compatible because their common turn corolla is treated as a pointwise fixed rooted branch. Their middle NNI supports are disjoint after the standard annular cell subdivision, and sequential execution leaves every later move unchanged.

Thus each boundary lift admits a root-valued relative movie

\[
\partial_\pm A
\rightsquigarrow
\mathcal S_{C_6},
\]

where `S_(C6)` is the cyclic canonical section complex formed from the six `S_i^star`.

### Lemma 2.1 — uniqueness of the canonical endpoint

The canonical endpoint is the same on the two boundary circles, with identical:

- turn-corolla incidences;
- pivot and side roots;
- cyclic order;
- distinguished route block;
- exterior attachment labels.

### Proof

For one fixed Petersen `C6`, each `S_i^star` is uniquely determined by the labelled pivot quadruple and the repeated side-root triangle. Consecutive sections agree literally on their common `R_(i+1)`, and the cyclic closing overlap agrees as well. Both annular boundaries inherit these same rooted data from the one full-labelled track. Hence their canonicalisations have one common labelled endpoint complex. ∎

Orientation of the two boundary circles as topological boundaries is opposite, but this merely reverses the parameterisation of the same labelled cyclic complex; it does not exchange the distinguished route block or alter any root label.

---

## 3. The identity root cylinder

Between two identical copies of `S_(C6)` place the product cylinder

\[
\mathcal S_{C_6}\times[0,1]
\]

with constant source topology and constant root labels. It contains no singular edge and no co-root transition.

Concatenate:

1. the root canonicalisation movie on `partial_- A`;
2. the identity root cylinder;
3. the reverse canonicalisation movie on `partial_+ A`.

Every stage is root-valued, fixes the complete outer side word, and preserves the ordered cap route.

### Theorem 3.1 — relative `C6` cylinder erasure

The original annular history neighbourhood `A` may be replaced, relative to its complete exterior boundary data, by a root-valued annulus containing no co-root track.

The replacement:

- leaves the two outside histories unchanged;
- changes no exterior source edge or attachment;
- retains every ordered incidence and root label on `partial A`;
- retains the distinguished cap matching and block;
- preserves cap-target vertex order;
- strictly decreases the number of singular/co-root track cells in the history diagram.

### Proof

The two relative canonicalisation strips are legal root NNI histories by the two-state `(0,2,2)` theorem and overlap lemma. Their canonical endpoints agree by Lemma 2.1. Gluing them to the identity cylinder gives a root-valued replacement with the same labelled boundary map as `A`. The old annulus contained the closed co-root track; the replacement does not. ∎

---

## 4. `C8` reduction

Let the reduced core be a simple Petersen `C8`. The omitted Petersen edge gives two simple `C6` cells sharing a two-edge pivot path. Their side-root data:

- agree with the `C8` away from the two seam endpoints;
- have equal middle emissions on the common path;
- form root triangles with the original `C8` emission at each seam endpoint.

Canonicalise and erase the two `C6` annuli using Theorem 3.1. The shared middle roots are identified, and the two endpoint root-triangle seams preserve all exterior labels.

### Theorem 4.1 — relative `C8` cylinder erasure

Every full-labelled simple `C8` co-root track has a same-order root-valued replacement preserving its complete exterior context and strictly reducing singular-track complexity.

No equal-face cancellation and no target-order recursion is required.

---

## 5. Repaired no-recurrence conclusion

Choose, among all lifted history diagrams realising one same-order contextual recurrence, one with the minimum number of singular track cells.

The forced-backbone theorem produces a shortest pivot-closed subtrack.

- Under `O+`, odd `C5/C9` subtracks are impossible.
- An even `C6/C8` subtrack is erased by Theorem 3.1 or 4.1, giving a diagram with the same exterior recurrence and fewer singular cells.

This contradicts minimality.

### Corollary 5.1 — co-root no-sink theorem without cancellation recursion

Subject to the full-labelled forced-backbone theorem and `O+`, no nonterminal recurrent SCC of persistent co-root states exists.

The even-core hypothesis may be stated as:

\[
\boxed{
E_{\rm cyl}:
\text{every even primitive track admits same-order relative root-cylinder erasure}.}
\]

This is stronger and cleaner than the old hypothesis

\[
E_{\rm cancel}:
\text{every even primitive track exits through an equal-face cancellation}.
\]

---

## 6. Consequence for the master theorem

For persistent co-root first failures, the global return argument now needs no appeal to:

- target-order descent;
- componentwise recursion after the star cancellation;
- an arbitrary root flow on a smaller graph;
- inverse restoration of the cancelled dipole.

Finite condensation plus diagram-complexity minimality gives a same-order route to rootification or a cap/category terminal.

---

## 7. Remaining equality interface

This repair does **not** by itself close inverse-cancellation quadruple equality.

If the first failed inverse step is an equal-face insertion with boundary

\[
r,r,r,r,
\]

all three local pairing sums are zero. There is no immediate root NNI and no co-root Petersen track. A separate theorem must show that the equality return process reaches:

1. a cap/route root terminal;
2. a same-order rootification;
3. or a recursive obligation with a genuinely decreasing complete contextual measure.

Thus after the cylinder repair the unique unresolved global-return interface is:

\[
\boxed{
\text{cover-independent return across a failed inverse equal-face cancellation}.}
\]

The shortest final proof should isolate that theorem rather than retain a broad cancellation-recursion assumption.