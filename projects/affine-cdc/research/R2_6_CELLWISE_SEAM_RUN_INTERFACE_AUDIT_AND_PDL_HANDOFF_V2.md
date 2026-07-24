# R2.6 cellwise seam/run interface audit and PDL handoff

## Research Lead packet v2

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `71a10f9ba86c1d2b8b7885e78fa9baa303c77818`  
**Receiver:** `AffineCDC — Proof Development Lead` (`AC-PDL`)

**Controls together with:**

- `CELLWISE_ROOT_SEAM_AND_CONSTANT_RUN_TRACK_ERASURE_V1.md`;
- `ROOT_NORMALIZED_CONTEXTUAL_TRANSFER_MASTER_V6.md`;
- `ROOT_NORMALIZED_CONTEXTUAL_TRANSFER_MASTER_V6_1_ADDENDUM.md`.

**Supersedes as the PDL R2.6 packet:**

- `R2_6_EVEN_TRACK_SOURCE_REPLACEMENT_PDL_HANDOFF_V1.md`;
- every instruction to reconstruct a global canonical `C6` history section, a simultaneous six-star state, or the two-`C6` `C8` annulus as a prerequisite for R2.6.

**Status after adversarial interface audit:** the cellwise theorem remains closed at Research Lead authorial level, but one implication used in its first statement must be read through the explicit two-sided identity-strip lemma below. A one-dimensional canonical root section is not, by terminology alone, a relative two-dimensional strip. The missing implication is supplied by uniqueness: both root-valued long-side histories of a constant-pivot neighbourhood must literally be the same nonpivot full-state history, so their relative replacement is its identity product.

This packet gives the exact reconstruction target. It does not assert PDL completion, independent assurance, cap restoration, or a global five-CDC theorem.

---

## 1. Normalized local geometry

Let `N(gamma)` be a sufficiently small regular neighbourhood of one finite normalized nonbranching co-root track.

The complete state on every slice records:

- source graph topology and ordered dart slots;
- every root label and the unique co-root atom when present;
- both crossed resolutions of that atom;
- all emitted side roots and rooted exterior attachments;
- support transport;
- cap block and route orientation;
- surviving or suspended ancestor marks.

The two long sides of `N(gamma)` lie in legal root-valued histories. Short sides lie in root-normalized or accepted endpoint collars, except for the explicitly retained unresolved outer endpoint case.

Interior raw support switches have already been removed from the recurrent alphabet. A switch--pop event is an endpoint collar, not a Ptolemy cell.

---

## 2. Two-sided constant-run identity-strip lemma

Consider one maximal constant-pivot interval

\[
F_j=\{s,d_j\},\qquad j=a,\ldots,b,
\]

with emitted side root `z_j` on the transition

\[
\{s,d_{j-1}\}\longrightarrow\{s,d_j\}.
\]

The exact transition equation is

\[
d_{j-1}+d_j+z_j=0.
\]

Let

\[
H^-,H^+
\]

be the two root-valued long-side restrictions of a regular neighbourhood of this interval. They have the same exterior source topology, side-root word, cap block, route, support transport, and mark data, because those data are fixed on the boundary of the neighbourhood.

### Lemma 2.1 — uniqueness on each long side

At every genuine transition, any root-valued restriction preserving the emitted root `z_j` must choose

\[
r_{j-1}=d_{j-1},\qquad r_j=d_j.
\]

The pivot choice `s,s` gives `z_j` rather than zero, and the mixed choices contain disjoint roots and give a co-root. Hence the nonpivot pair is the unique root-admissible choice.

Consequently both `H^-` and `H^+` choose `d_j` at every state.

### Lemma 2.2 — literal full-state equality

The neighbourhood fixes all noncentral source data. Since the central root choice is unique at every slice, `H^-` and `H^+` agree literally on:

- every source vertex and dart slot;
- every root label;
- the selected crossed-resolution block;
- every side-root occurrence and rooted attachment;
- support transport;
- cap block, route orientation, and surviving/suspended marks.

Thus

\[
\boxed{H^-=H^+}
\]

as complete labelled histories, not merely as coefficient words.

### Theorem 2.3 — relative constant-run strip

The product of this common root history with an interval,

\[
H^-\times[0,1],
\]

is a legal root-valued identity strip fixing the complete rectangular boundary. It replaces the constant-pivot co-root neighbourhood without introducing any source move, zero edge, co-root edge, or cancellation.

This is the exact two-dimensional consequence needed by the cellwise theorem.

### Degenerate intervals

- A run with one state and no transition is handled by the same unique endpoint root and an identity rectangle.
- A zero-width piece created only by separating adjacent collars is already root-valued and may be retained as an identity slice or omitted from the list of nontrivial intervals.
- A closed constant-pivot track has identical initial and terminal complete states; the same identity product closes to a root cylinder.

---

## 3. Pivot-change seam endpoints match the unique run sections

Consider a genuine nonbacktracking pivot-change cell

\[
x\to s\to t\to y
\]

with side roots

\[
z=x+t,\qquad w=s+y.
\]

The shared DDD state at the pivot change is

\[
F=\{s,t\}.
\]

The constant-pivot run on the left has pivot `s` and therefore forces the nonpivot endpoint root `t`. The run on the right has pivot `t` and forces the nonpivot endpoint root `s`.

The local `(0,2,2)` seam theorem fixes the two turn corollas

\[
L=(x,t,z),\qquad R=(s,y,w)
\]

pointwise. Therefore the seam exposes exactly:

- root `t` on the left run side;
- root `s` on the right run side.

These are not chosen after the fact. They are the roots already present in the fixed turn corollas of the local source cell.

### Lemma 3.1 — literal seam/run endpoint equality

At each cut copy of a pivot-change seam, the adjoining constant-run identity strip and the seam collar agree literally on:

- the shared source dart slots;
- the endpoint root `t` or `s`;
- the crossed-resolution block selected by the oriented cap lock;
- side roots and support transport;
- cap block and route orientation;
- every surviving or suspended ancestor mark.

Hence the gluing is by identity of complete endpoint states. No coefficient-only identification and no star-centre identification is used.

---

## 4. Adjacent pivot changes and backtracks

Two pivot-change occurrences may share one history vertex. Their local seam movies must not be superposed in one source cell.

Insert an identity subdivision of the history parameter at the common complete state. This means replacing one time vertex by two copies joined by an identity interval carrying the same complete root-labelled state. It is a subdivision of the history complex, not a new graph move and not a new element of the move alphabet.

Choose one seam collar in the interior of each adjacent source cell. Their interiors are then disjoint.

### Lemma 4.1 — source-category safety of identity subdivision

Identity subdivision:

- changes no source graph;
- changes no root or atom label;
- changes no cap, route, support, side-output, genealogy, or mark datum;
- creates no cancellation or support switch;
- creates no new singular branch.

Thus it may be inserted and removed freely in a relative history proof.

### Immediate backtrack

For

\[
s\to t\to s,
\]

one may either:

1. apply the established source-faithful `abba` deletion; or
2. place disjoint seams at the two pivot-change occurrences and treat the intervening single-state/identity piece by Theorem 2.3.

The second description does not invoke free reduction of an abstract pivot word.

---

## 5. Endpoint collars

A switch--pop birth/death collar is included as a separate bounded endpoint block.

Its root short side is the predecessor-order `B` insertion boundary `X^-`. One must not identify `X^-` directly with the nonpivot endpoint root of the first constant run. Instead:

1. retain the whole switch--pop collar;
2. place the open-track short side on `X^-`;
3. let the singular half-track leave the opposite side of the collar;
4. begin the seam/run decomposition only after the collar, where the first atom and its two root-valued long-side restrictions are defined.

The collar fixes all ordered incidences, inserted vertex slots, cap/route data, side roots, rooted attachments, and surviving/suspended marks. The first constant-run or pivot-change replacement therefore glues to the collar on its ordinary long-side boundary, while the root short side remains fixed.

The reverse statement holds for a death collar.

If the other endpoint is unresolved at the original outer cap, only the completed interior pieces are consumed; the final incident component remains the exact outer-endpoint obligation.

---

## 6. Closed and open assembly

Place a disjoint local root seam at every genuine pivot-change occurrence. Cut the track at all seam copies.

Every remaining nontrivial singular interval has no pivot change and is therefore constant-pivot. Replace it by the identity strip of Theorem 2.3. Glue every strip to the adjacent seam collars by Lemma 3.1.

### Theorem 6.1 — repaired closed assembly

Every finite closed normalized full-state co-root track has a source-faithful root-valued cylinder replacement fixing its complete labelled exterior boundary.

No global canonical-star section, simple `C6/C8` subannulus, simultaneous six-star source state, support-switch interior cell, equal-face cancellation, or graph-order descent is used.

### Theorem 6.2 — repaired normalized open assembly

Every finite open normalized full-state co-root track whose two short sides are root-normalized or accepted has a source-faithful root-valued rectangle replacement fixing all four complete labelled sides.

If one short side is the unresolved original outer endpoint, all completed cells and runs are removed while that endpoint continuation is retained exactly.

---

## 7. Periodic endpoint crosscut

Assume variable-order calls have already been compressed and the same complete unresolved endpoint state occurs twice at one fixed order. Identify the two equal endpoint collars. The intervening history becomes a finite root-boundary cylinder after Theorem 6.1.

### Lemma 7.1 — connected legal `1`-skeleton

A connected finite history cylinder is a finite CW complex whose cells attach along their boundary histories. Different components of its `1`-skeleton cannot be joined by a higher cell, because the attaching circle of each cell lies in one `1`-skeleton component. Hence its legal history `1`-skeleton is connected.

Every vertex and edge of this `1`-skeleton belongs to the root-valued replacement history.

### Lemma 7.2 — embedded root crosscut

Choose a shortest edge path in the legal `1`-skeleton joining the two disjoint boundary subcomplexes.

- A shortest path is simple.
- Its interior cannot meet either boundary subcomplex; otherwise truncate it at the first or last such meeting.
- A small regular neighbourhood is therefore an embedded transverse band joining the two boundary circles.

All states and history edges on the path are root-valued and source-legal.

Cutting the cylinder along this band gives a root-valued rectangle with the two repeated endpoint collars separated. This is the exact periodic endpoint discharge used by the resolved-call SCC argument.

---

## 8. Exact PDL reconstruction obligations

PDL should reconstruct the following, in this order.

1. **Local seam table.** Recompute the 120 nonbacktracking four-pivot cases, the branch word `(z,z,w,w)`, the two root topologies, and the unique zero/one relative root NNI with fixed turn corollas.
2. **Two-sided uniqueness.** Prove Lemmas 2.1--2.2 from the root-triangle equation and complete boundary data; do not infer a strip from the word `section` alone.
3. **Identity strip.** Build Theorem 2.3 as a literal product of one complete root history.
4. **Endpoint matching.** Check that `L=(x,t,z)` and `R=(s,y,w)` expose exactly the nonpivot roots demanded by the adjacent runs, including crossed-resolution, cap, route, support, and mark fields.
5. **Disjoint collars.** Treat consecutive changes, zero-width pieces, and `abba` backtracks using source-neutral identity subdivision.
6. **Switch--pop endpoints.** Keep the collar as a separate block; do not equate its short side with the first run state.
7. **Closed/open assembly.** Glue only on literal complete states.
8. **Periodic crosscut.** Verify the connected-`1`-skeleton and minimal-crosscut lemmas in the actual history complex.
9. **Final consumer.** Replace the old R2.6 annulus/open-strip dependency in the v6/v6.1 synthesis by Theorems 6.1--7.2 above.
10. **Terminal semantics.** Audit every accepted endpoint against an explicit route/profile, bounded direct/theta, small-cut, separator, or terminal-unwind theorem.

PDL should return either:

- `AC-PD-5CDC R2.6 — COMPLETE-DRAFT`, with exact dependency citations and no old canonical-star gluing; or
- one precise counterexample/interface failure, returned to AC-RL.

---

## 9. Classification and trust boundary

### Closed at Research Lead authorial level

- local root seams at every pivot-change occurrence;
- pairwise-disjoint source-cell collars after identity subdivision;
- two-sided constant-run uniqueness;
- identity-product strip realization;
- literal seam/run endpoint matching;
- switch--pop endpoint scope;
- closed and normalized-open track erasure;
- periodic root crosscut.

### Required before promotion

- independent PDL reconstruction;
- final v6/v6.1 synthesis;
- literal cap/route consumer audit;
- independent audit of the full dependency DAG.

### Not claimed

- PDL completion;
- independently assured R2.7;
- accepted cap restoration or R1;
- universal five-support/five-CDC theorem;
- Lean, manuscript, curation, release, arXiv, DOI, peer review, or publication status.
