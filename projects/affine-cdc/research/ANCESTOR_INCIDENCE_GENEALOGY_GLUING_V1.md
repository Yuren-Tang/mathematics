# Ancestor incidence genealogy glues by a labelled frame stack

## Research Lead witnessed-history interface v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`

**PDL interface:** `AC-PD-5CDC-HW2`.

**Parents:**

- `FINITE_COMPLETE_STATE_NO_HIDDEN_GENEALOGY_V1.md`;
- `NESTED_CANCELLATION_BUBBLE_COMPRESSION_V1.md`;
- `WELD_MARK_EQUAL_FACE_OVERLAP_V1.md`;
- the complete raw-insertion root-NNI and support-switch lift table;
- `CHILD_CONTEXT_FIDELITY_AFTER_ROOT_CANCELLATION_V1.md`.

**Status:** exact ancestor-incidence and contextual-data gluing theorem. Every recursive cancellation frame stores an ordered source interface, not merely two root values. Root NNIs, support switches, one-atom movies and alternative-insertion macros act relative to labelled exterior darts. A returned insertion must consume the stored interface. Proper nesting makes the partial incidence maps composable and prevents a deleted mark from being recreated by a later equality of root labels. Outer cap blocks, terminal order, route sheet and side attachments therefore survive concatenation as literal labelled data until an explicitly declared route/category exit.

---

## 1. Labelled contextual universes

At each frame level `r`, fix a finite labelled dart universe

\[
\mathscr D_r
\]

with:

- labelled cubic vertex slots;
- two darts for every internal edge;
- ordered outer semiedge darts;
- the distinguished cap block and route sheet;
- labels on every rooted side attachment.

A source topology is an involution pairing appropriate darts together with their vertex incidences.

The four global outer semiedges and their cap-block order use persistent labels shared by every descendant frame. Internal vertices and darts created or removed by one frame receive labels local to that frame.

---

## 2. One cancellation frame

Let a parent equal-face pair have vertices `u,v`, central edge `c`, and four noncentral incident darts

\[
(a_0,a_1;b_0,b_1)
\]

in the exact ordered incidence convention supplied by the source state.

The root-valued cancellation pairs these darts into two output edges. Store a frame record

\[
\boxed{
\mathfrak f=(u,v,c;\ a_0,a_1,b_0,b_1;\ \pi;\ \mathcal C,\mathcal R)
}
\]

where:

- `pi` is the ordered pairing producing the two child output edge lineages;
- `mathcal C` is the inherited cap/terminal record;
- `mathcal R` is the inherited route sheet and side-attachment record.

The child dart universe is obtained by deleting the six darts at `u,v` and pairing the four surviving outside half-darts according to `pi`.

### Lemma 2.1 — push map

There is a canonical partial ancestor map

\[
\iota_{\mathfrak f}:\mathscr D_{r+1}\longrightarrow\mathscr D_r
\]

which is the identity on every surviving dart and records each child output edge as the ordered pair of its two parent outside half-darts.

No root label is used to define `iota_f` after the frame is created.

---

## 3. Local generator genealogy

### Root NNI

A labelled `2--2` move fixes its four exterior branch darts pointwise and replaces only one active central pairing. Every passive dart lineage is the identity. If a stored marked output edge is active, the explicit central-overlap movie records the replacement diagonal sheet; it does not identify the new edge with the old edge by value alone.

### Support-pair switch

A support switch changes only coefficient labels on an explicitly selected even edge set. The topology and every dart lineage are the identity.

### Bounded one-atom movies

Every split-system movie fixes the listed exterior branch darts pointwise. Intermediate central edges have local movie labels and disappear when the movie ends. The endpoint genealogy is the displayed ordinary topology map, independent of whether the central value is root, zero or co-root.

### Alternative insertion

The equality/good-disjoint five-leaf path restores the two parent vertex slots using the stored five exterior incidences. The alternative topology differs from the original insertion, but all exterior dart identities are literal and the local NNI path supplies the unique genealogy between them.

### Lemma 3.1 — generator functoriality

Every declared fixed-order generator supplies a finite labelled correspondence which:

1. is identity on all exterior darts outside its support;
2. retains ordered outer terminals, cap block and side attachments;
3. records every active-edge replacement explicitly;
4. never infers ancestry from equality of root labels.

---

## 4. Pop consumes the stored interface

A successful child return reaches the two stored output edge lineages of `mathfrak f` with current root values. Raw insertion splits those exact edge objects and restores the local parent vertex slots.

The pop may end as:

- original root insertion;
- alternative root insertion;
- missing-index one-atom insertion;
- bounded/category exit.

In every nonexit case the insertion endpoint is connected to the stored parent topology by the explicit local source movie.

### Theorem 4.1 — no silent interface recreation

A pop operation is legal only relative to the top frame record `mathfrak f`. It may not select another pair of equal-valued child edges or reconstruct a pairing from current coefficient labels.

If a descendant cancellation consumes one marked output edge, its frame transition records deletion of that lineage and the new ordered outputs. A later pop cannot recreate the consumed edge except through the explicit inverse of that descendant frame.

---

## 5. Proper nesting and composition

Recursive calls are last-in-first-out. Hence frame intervals form a properly nested family

\[
\mathfrak f_0\supset\mathfrak f_1\supset\cdots.
\]

At any moment the live genealogy map from the current child universe to an ancestor universe is the ordered composition

\[
\iota_{\mathfrak f_0}\circ\iota_{\mathfrak f_1}\circ\cdots
\]

together with the finite active-diagonal correspondences of intervening fixed-order generators.

### Lemma 5.1 — composability

Every map is defined on the surviving labelled darts expected by the next outer map. A child pop removes only the top frame and restores exactly its parent universe. Therefore the composite ancestor map is well typed throughout the execution.

### Theorem 5.2 — ancestor genealogy theorem

Concatenating witnessed child histories and innermost-bubble replacements yields one labelled ancestor history in which:

- every surviving dart has a unique ancestor;
- every deleted dart has a unique consuming frame;
- every restored parent dart is supplied by the matching top frame;
- no two unrelated lineages are merged because they happen to carry the same root.

---

## 6. Cap block, route sheet and side attachments

### Outer cap data

All surgeries in the current-flow programme are relative to the four ordered outer semiedges. Their dart labels and distinguished cap block are fixed at every generator and copied into every child frame.

### Route sheet

At a route-preserving move, the current physical route sheet is recomputed on the same labelled terminal system and stored in the child record. If the physical route first changes, the route-change theorem declares a cap-compatible terminal and no further fixed-route child is formed.

Thus no generator silently changes the route sheet while claiming identity.

### Side attachments

Constant-pivot runs, Petersen cells and raw insertion movies retain every emitted side root and rooted exterior branch as a labelled attachment. Relative source movies are glued only when these labels agree pointwise.

### Theorem 6.1 — contextual genealogy fidelity

At every nonexit concatenation, ordered terminals, cap block, route sheet and rooted side attachments agree literally across the gluing collar. A route/category change is explicit terminal data, not an unrecorded mutation.

---

## 7. Component and separator tags

If a child cancellation output splits, each component is recorded by its labelled surviving vertex/dart set. The parent small-cut shore constructed from it is therefore canonical.

If a lower child later exposes a separator, the exit record contains:

- the child shore dart set;
- ordered cut semiedges;
- its composite ancestor map;
- all enclosing frame interfaces.

This record is sufficient for a separate separator-persistence or componentwise-gluing theorem. The present genealogy theorem does not claim that the numerical cut size is invariant under reinsertion.

Indeed local cut calculus shows that reinserting one two-vertex interface can increase a cut by two when the two stored output edges lie internally on opposite shores. This is why separator disposition must use the stored genealogy rather than a bare cut-size assertion.

---

## 8. `HW2` audit

The PDL obligation asks that concatenation retain all ancestor ordered incidences, cap blocks, route sheets and side attachments, and that a mark-consuming cancellation not silently recreate its mark.

These requirements are closed by:

1. labelled dart universes;
2. ordered frame records at every push;
3. relative generator correspondences;
4. top-frame-only pop semantics;
5. proper nesting and composition;
6. explicit route/side records;
7. tagged component/separator exits.

### Classification

\[
\boxed{
\texttt{HW2 ANCESTOR INCIDENCE GENEALOGY CLOSED}
}
\]

The numerical disposition of a tagged separator after all ancestor insertions is a cut/gluing consumer question, not a failure of genealogy.

---

## 9. Assurance boundary

### Exact here

- canonical push interface;
- local generator ancestry;
- top-frame-only pop;
- mark consumption without silent recreation;
- proper nested composition;
- literal cap/route/side gluing;
- canonical component and separator tags;
- warning that cut size need not be ancestor-invariant.

### Imported authorial mathematics

- ordered-incidence cancellation rule;
- central/adjacent raw insertion movies;
- universal support-switch lift;
- route-change terminal theorem;
- witnessed bubble compression.

### Not claimed

- `HW3` fixed-order consumer compatibility;
- a theorem that every child separator remains a cut of size at most four in every ancestor;
- unconditional PDL R2.7 or global cap restoration;
- independent audit, Lean verification, manuscript integration, curation, release or publication.
