# R2.6 exact source-replacement handoff

## Research Lead packet for PDL reconstruction v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`

**Receiver:** `AffineCDC — Proof Development Lead` (`AC-PDL`)

**Consumes the PDL outputs:**

- `AC_PD_5CDC_R2_4_FULL_STATE_FORCED_BACKBONE.md`;
- `AC_PD_5CDC_R2_5_ORIENTED_ODD_EXCLUSION.md`;
- `AC_PD_5CDC_R2_7_FIXED_ORDER_CONSUMER_COMPATIBILITY.md`.

**Research sources to reconstruct independently:**

- `PETERSEN_C6_CANONICAL_STAR_SECTION_V1.md`;
- `PETERSEN_C6_RELATIVE_STAR_MOVIE_DESCENT_V1.md`, only for its relative `(0,2,2)` and overlap calculations;
- `PETERSEN_EVEN_TRACK_ROOT_ANNULUS_REPLACEMENT_V1.md`, controlling for closed even tracks;
- `PETERSEN_C8_TWO_C6_HISTORY_FILLING_REDUCTION_V1.md`;
- `PETERSEN_OPEN_TRACK_ROOT_STRIP_REPLACEMENT_V1.md` read through
  `OPEN_TRACK_ROOT_STRIP_ENDPOINT_SCOPE_CORRECTION_V1.md`;
- `PERIODIC_OUTER_ENDPOINT_ROOT_SEAM_DISCHARGE_V1.md` v1.2;
- `ROOT_NORMALIZED_CONTEXTUAL_TRANSFER_MASTER_V6_1_ADDENDUM.md`.

**Target classification:** after independent line-by-line reconstruction, this packet should yield

`AC-PD-5CDC R2.6 — COMPLETE-DRAFT`

for the source-level even-core annulus, normalized open strip and periodic endpoint seam. It does not by itself complete R2.7 or five-CDC.

---

## 1. Input from R2.4--R2.5

Work in one normalized fixed-order lifted comparison.

R2.4 supplies one nonbranching physical Petersen pivot track with:

- every maximal constant-pivot run already rootified as a fixed rooted carrier;
- every immediate Type-T backtrack removed diagrammatically;
- one transported crossed sheet;
- all emitted side roots and exterior rooted attachments retained;
- the distinguished cap block and route orientation fixed;
- one shortest simple pivot-closed core of length `5,6,8,9`.

R2.5 excludes the odd cores `C5,C9` before double traversal.

Thus R2.6 receives exactly one of:

\[
\boxed{C_6\quad\text{or}\quad C_8}
\]

with complete full-labelled decorations.

The fixed-order consumer normal form is essential:

- internal persistent cells are root-NNI/Ptolemy cells;
- raw support-switch corrections do not occur inside the core;
- switch--pop collars may occur only at open-track endpoints.

---

## 2. Primitive `C6` coordinates

Let

\[
p_0,p_1,\ldots,p_5,p_0
\]

be a simple Petersen six-cycle. Let `z_i` be the third Petersen neighbour of `p_i` outside the cycle.

The identity-hexagon theorem gives

\[
(z_0,z_1,z_2,z_3,z_4,z_5)=(a,b,c,a,b,c),
\qquad a+b+c=0.
\]

At two consecutive pivots use the ordered six-port boundary

\[
B_i=(p_i,p_{i-1},z_i\mid z_{i+1},p_{i+1},p_{i+2}).
\]

The two turn equations are

\[
p_{i-1}+p_{i+1}=z_i,
\qquad
p_i+p_{i+2}=z_{i+1}.
\]

The adjacent resolved constant-pivot carriers determine fixed root corollas

\[
R_i=(p_{i-1},p_{i+1},z_i),
\qquad
R_{i+1}=(p_i,p_{i+2},z_{i+1}).
\]

Treat these corollas as rooted exterior branches.

---

## 3. Relative `(0,2,2)` cell theorem

After contracting the fixed turn corollas to their outgoing roots, the unresolved middle has four branch values

\[
(z_i,z_i,z_{i+1},z_{i+1}).
\]

Its three binary topologies are exactly:

1. one equality path with central value zero;
2. one root cross path;
3. one root canonical star.

Let

\[
u_i=z_i+z_{i+1}=z_{i+2}.
\]

The canonical star has:

- turn spokes `z_i,z_{i+1}`;
- side cherry `(z_i,z_{i+1})` with spoke `u_i`;
- central root triangle `(z_i,z_{i+1},u_i)`.

### Lemma 3.1 — two root states only

Relative to the fixed turn corollas, every root-valued restriction is either the cross path or the canonical star.

### Lemma 3.2 — unique root exchange

The cross path and canonical star are joined by one unique root-preserving relative NNI fixing:

- both turn corollas pointwise;
- all six boundary incidences;
- every exterior source edge and root label.

The third NNI direction is the zero path and is not used.

---

## 4. Common canonical target around `C6`

The canonical star in Cell `i` induces the two turn corollas

\[
R_i,
\qquad
R_{i+1}.
\]

Consecutive cells induce literally the same labelled shared corolla. The relative NNI support lies only in the middle two vertices and treats every turn corolla as an exterior rooted branch.

Therefore the six local canonicalisations glue cyclically.

Let

\[
\mathcal T_{C_6}^\star
\]

be the resulting canonical section complex.

### Theorem 4.1 — one-sided `C6` canonicalisation

Every root-valued annular boundary history of a decorated `C6` track admits a root-valued relative movie

\[
\partial N(\gamma)\rightsquigarrow \mathcal T_{C_6}^\star
\]

fixing the complete exterior data.

This is a two-dimensional history section complex. It is not one simultaneous cubic source graph containing all six star interiors.

---

## 5. `C6` root annulus

Let `N(gamma)` be a sufficiently small annular neighbourhood of the closed `C6` singular track. Its two boundary circles

\[
\partial_-N(\gamma),
\qquad
\partial_+N(\gamma)
\]

lie in the root-valued part of the lifted history.

Apply Theorem 4.1 to both sides. The canonical target is determined only by the labelled six-port cells and fixed turn corollas, so it is the same on both sides:

\[
\partial_-N(\gamma)
\rightsquigarrow
\mathcal T_{C_6}^\star
\leftsquigarrow
\partial_+N(\gamma).
\]

Reverse the plus-side movie and concatenate.

### Theorem 5.1 — `C6` root-cylinder replacement

A closed decorated `C6` track has a singularity-free root-valued annular replacement with:

- the same two labelled boundary histories;
- every constant-run carrier retained;
- every side-root incidence retained;
- the same crossed sheet, cap block and route orientation;
- no zero or co-root edge;
- no equal-face cancellation and no lower-order call.

This root-cylinder theorem, not the older strict-cancellation corollary, is controlling for R2.6 closed-track erasure.

---

## 6. `C8` reduction and seam

Let `C` be a simple Petersen eight-cycle. Its two omitted vertices `r,r'` are adjacent.

Choose `r`. Let `a,b` be its two neighbours on `C`; the two `a`--`b` arcs in `C` have length four. Adding the shared path

\[
a-r-b
\]

to each arc gives two simple six-cycles

\[
H_+,
\qquad
H_-.
\]

They satisfy

\[
E(C)=E(H_+)\triangle E(H_-)
\]

and share exactly the two-edge path `a-r-b`.

The side-root seam data are:

1. away from `a,b`, the `H_\pm` emissions equal the original `C8` emissions;
2. at `r`, both six-cycles emit the same root `r'`;
3. at `a` and `b`, the two six-cycle emissions and the original eight-cycle emission form one root triangle.

### Theorem 6.1 — seam-compatible `C8` annulus

Apply the `C6` root-cylinder theorem to `H_+` and `H_-` relative to:

- the shared pivot path `a-r-b`;
- the common middle root `r'`;
- the two endpoint root-triangle seam vertices;
- all exterior `C8` side roots.

The two cylinders glue to a singularity-free root-valued annulus for the decorated `C8` track, preserving its complete labelled exterior history.

No separate primitive `C8` local movie is required.

---

## 7. Unified closed even-core theorem

### Theorem 7.1 — R2.6 closed-track replacement

Let a full-state recurrent component have reduced core `C6` or `C8`. Then a regular annular neighbourhood of that component has a root-valued replacement fixing its complete labelled boundary.

Replacing the neighbourhood:

- removes the entire closed singular component;
- introduces no new singular edge;
- preserves every exterior rooted decoration, side output, cap block, route and crossed sheet;
- uses no graph-order descent.

Together with R2.4--R2.5, this proves that a singular-component-minimal fixed-order lifted comparison has no internal closed component.

---

## 8. Open-track local theorem

Let

\[
x,s,t,y
\]

be four consecutive pivots on a reduced nonbacktracking Petersen path. Let `z` be the third neighbour of `s` and `w` the third neighbour of `t`.

Normalize the central Petersen edge to

\[
s=12,
\qquad
 t=34.
\]

Then

\[
\{x,z\}=\{35,45\},
\qquad
\{y,w\}=\{15,25\}.
\]

Hence

\[
\boxed{z\ne w,\qquad |z\cap w|=1.}
\]

Equivalently, all 120 ordered nonbacktracking four-pivot paths satisfy the same relation.

Therefore every open pivot-change cell again has the relative branch word

\[
(z,z,w,w)
\]

with one equality topology and exactly two root topologies, cross and canonical star.

---

## 9. Normalized open strip

Let an open co-root track have pivot-change cells

\[
B_1,\ldots,B_k.
\]

After constant-run and backtrack normalization, choose a rectangular neighbourhood. Its two long sides lie in root-valued histories.

Assume both short endpoint sides are:

1. root-normalized local cells;
2. switch--pop collars with root-valued/discharged short sides; or
3. accepted route/bounded/separator cells.

Canonicalise every root-valued cell restriction on both long sides to the same star strip

\[
\mathcal T_\gamma^\star.
\]

Adjacent cells share fixed turn corollas, so the movies glue linearly.

### Theorem 9.1 — normalized-endpoint root strip

Under the endpoint hypothesis above, the complete open track has a singularity-free root-valued rectangular replacement fixing all four labelled sides and all exterior contextual data.

### Scope prohibition

Do not apply this theorem when one short side is the unresolved original outer cap endpoint carrying a co-root atom. Interior canonicalisation alone does not rootify that short side.

---

## 10. Periodic unresolved endpoint

After witnessed variable-order compression and normalized FOC, suppose the same complete unresolved outer endpoint state occurs twice in a fixed-order history rectangle.

Identify the two equal short collars. The open singular arc becomes one internal closed full-state component in a history cylinder.

Apply the complete closed-track theorem:

- constant runs rootify;
- Type-T bigons disappear;
- odd cores are impossible;
- even cores use Theorem 7.1.

The result is a finite connected fully root-valued history cylinder with the same two boundary histories.

Its ordinary history `1`-skeleton is connected. Choose a shortest path between the two boundary vertex sets. This path is:

- simple;
- interior-disjoint from both boundaries;
- made entirely of genuine root-valued source states and legal root-history edges.

It is therefore a root crosscut.

Cut the cylinder along the crosscut.

### Theorem 10.1 — periodic root rectangle

A repeated normalized unresolved endpoint episode has a fully root-valued rectangular replacement with the same long boundary histories and complete exterior contextual data. The two unresolved endpoint occurrences are removed.

No artificial barycentric state, marked-point transport or residual open-track argument is used.

---

## 11. Exact PDL reconstruction obligations

A PDL R2.6 dossier must independently verify:

1. the `C6` side-word identity and all turn equations;
2. the relative `(0,2,2)` table;
3. uniqueness of the root cross--star NNI;
4. literal overlap of adjacent turn corollas;
5. coherent canonicalisation of each annular side;
6. equality of the two canonical targets;
7. construction of the root cylinder without treating all cells as one source time slice;
8. the complete `C8=C6 triangle C6` seam and side-root formulas;
9. category-safe exits for every local NNI/gluing degeneration;
10. the 120/120 open side-root intersection theorem;
11. the root-strip theorem with the corrected endpoint scope;
12. switch--pop collars as endpoint cells, never internal Ptolemy cells;
13. periodic closure only after normalized fixed-order compression;
14. connectedness of the legal root-history `1`-skeleton and shortest crosscut;
15. preservation of cap block, route, crossed sheet, side roots, rooted carriers and suspended ancestor marks throughout.

---

## 12. Forbidden shortcuts

Do not use:

- the six canonical stars as one simultaneous cubic graph;
- abstract support monodromy in place of physical rooted carriers;
- equality dipole cancellation as the controlling closed `C6` erasure;
- raw support-switch corrections as internal Ptolemy cells;
- an open strip at an unresolved co-root endpoint;
- endpoint order restoration as proof that a variable-order episode was fixed-order;
- arbitrary subdivision to invent source-history vertices;
- child/parent prefix identification;
- arbitrary terminal recolouring.

---

## 13. Handoff boundary

### Supplied by this packet

- exact theorem spine for `C6`, `C8`, open strip and periodic seam;
- source-level gluing data;
- endpoint and cell-alphabet scope;
- complete downstream interface to R2.7.

### Still PDL-owned

- independent ordinary-proof reconstruction;
- source checks for every imported local theorem;
- final R2.4--R2.7 synthesis;
- return of any contradiction or missing cap/route hypothesis.

### Not implied

- independent audit;
- cap-restoration assurance;
- global five-support or five-CDC acceptance;
- Lean, manuscript, curation, release or publication status.
