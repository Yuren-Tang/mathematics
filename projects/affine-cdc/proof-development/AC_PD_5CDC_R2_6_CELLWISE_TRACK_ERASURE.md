# AC-PD-5CDC R2.6 — cellwise seam and constant-run track erasure

**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Programme:** compressed five-support proof, fixed-order singular-history unit `R2.6`  
**Frozen Research Lead input:** `research/affine-cdc-five-cdc-v1@71a10f9ba86c1d2b8b7885e78fa9baa303c77818`  
**Classification:** `COMPLETE-DRAFT / R2.6 SOURCE-LEVEL CLOSED / CELLWISE ROUTE SUPERSEDES GLOBAL C6-C8 SECTION`.

This dossier independently reconstructs
`CELLWISE_ROOT_SEAM_AND_CONSTANT_RUN_TRACK_ERASURE_V1.md` and narrows its
consumer statement to exactly what is needed by contextual transfer.

The proof does **not** construct one simultaneous six-star source state, does
not identify a proper Petersen subcycle with a complete physical annulus, and
does not use a raw support-switch correction as an interior Ptolemy cell.
It works one source cell at a time.

---

## 1. Fixed-order normalized input

Work in one finite labelled fixed-order history complex.  Every state records:

- the complete cubic source topology and ordered dart slots;
- every root label;
- at most one normalized co-root atom;
- both crossed root resolutions of that atom;
- all emitted side roots and exterior rooted attachments;
- support transport;
- the distinguished cap block and route orientation;
- every surviving or suspended ancestor mark.

Immediate zero rows, raw doubled-disjoint insertions and transient two-co-root
trees are internal to bounded normalization macros and are not state vertices.
By `AC_PD_5CDC_R2_7_FIXED_ORDER_CONSUMER_COMPATIBILITY.md`, raw support-switch
corrections occur only inside terminal switch--pop collars and never as
interior cells of a closed singular component.

The persistent singular locus is therefore a finite nonbranching one-manifold.
Each connected component is either a circle or an interval.

---

## 2. Petersen notation along one component

A standard co-root atom has two disjoint root resolutions.  Write its Petersen
edge as

\[
F_j=\{s_{j-1},s_j\}.
\]

A maximal constant-pivot run has the form

\[
F_t=\{s,d_t\}
\]

with fixed pivot `s`.  A **genuine pivot change** is a nonbacktracking local
word

\[
x\longrightarrow s\longrightarrow t\longrightarrow y
\]

with

\[
x\ne t,
\qquad
s\ne y.
\]

Before the cellwise construction, remove every immediate pivot backtrack by
the source-faithful labelled bigon replacement of
`AC_PD_5CDC_R2_4_FULL_STATE_FORCED_BACKBONE.md`, Theorem 6.1.  Thus every
remaining change cell is genuine in the above sense.

This preliminary step fixes the complete outer history and all rooted
attachments; it is not abstract word cancellation.

---

## 3. Exact algebra at a genuine pivot change

Let roots be two-subsets of `[5]`, with Petersen adjacency given by
disjointness.  For one nonbacktracking Petersen path

\[
x-s-t-y
\]

define the two side roots

\[
z=x+t,
\qquad
w=s+y,
\]

where addition is symmetric difference in `E_5`.

### Lemma 3.1 — side-root intersection

The vectors `z,w` are distinct roots and

\[
|z\cap w|=1.
\]

### Proof

Use one global support permutation to put

\[
s=12,
\qquad
t=34.
\]

The nonbacktracking neighbours of `s` other than `t` are

\[
x\in\{35,45\},
\]

and the nonbacktracking neighbours of `t` other than `s` are

\[
y\in\{15,25\}.
\]

Consequently

\[
z=x+t\in\{35,45\},
\qquad
w=s+y\in\{15,25\},
\]

with the complementary member chosen in each displayed pair.  Both contain
support index `5`; their other indices lie in disjoint sets `{3,4}` and
`{1,2}`.  Hence they are distinct and meet exactly in `5`. ∎

### Finite certificate

There are

\[
10\cdot3\cdot2\cdot2=120
\]

ordered nonbacktracking four-pivot words.  Direct enumeration gives `120/120`
instances satisfying Lemma 3.1 and no exception.  The normal-form proof above,
not the enumeration, is controlling.

---

## 4. One local root seam

After resolving the two adjacent constant-pivot pieces, the unresolved middle
four-port has ordered branch word

\[
(z,z,w,w).
\]

Its three binary pairings have the following central values:

1. pairing equal labels gives `z+z=w+w=0`;
2. each crossed pairing gives the root
   \[
   u=z+w\in R_5.
   \]

Thus there is exactly one zero topology and two root-valued topologies.  The
two root topologies are joined by one relative root NNI, fixing the two turn
corollas and all six ordered exterior incidences.

Choose the canonical-star root topology as common target.  Each of the two
root-valued side restrictions reaches it by zero or one relative root NNI:

\[
X^-\rightsquigarrow S^\star\leftsquigarrow X^+.
\]

### Theorem 4.1 — complete pivot-change seam

Every genuine pivot-change source cell contains a transverse root-valued seam
which fixes literally:

- both turn corollas;
- all source vertex and dart slots on the cell boundary;
- every exterior source edge and root;
- both side roots;
- support transport;
- cap block and route orientation;
- every surviving or suspended mark.

### Proof

Lemma 3.1 gives the `(0,2,2)` coefficient table.  The relative NNI changes only
the internal pairing of the four middle branches.  All listed data live on the
fixed boundary and are therefore unchanged. ∎

No neighbouring cell is required to carry the same canonical star.

---

## 5. Disjoint seam collars

There are finitely many genuine pivot-change occurrences on one finite track.
Choose a small closed collar around the seam in each cell.

If two change cells are consecutive and share a history vertex, insert a
finite identity interval at that state.  The repeated state is fully labelled
and root-valued, so the identity subdivision changes neither source data nor
the singular relation.  Assign the two collars to opposite sides of the
identity interval.

### Lemma 5.1 — collar separation

The seam collars may be chosen with pairwise disjoint interiors, and every
collar meets the rest of the history only in its two complete labelled root
boundary states.

This is a finite cellular refinement, not a new source move.

---

## 6. Cutting produces constant-pivot intervals

Replace every pivot-change collar by its root seam and cut the singular
neighbourhood along the seam copies.

Every genuine pivot change has been removed.  Since immediate backtracks were
removed before Section 3, each remaining singular component lies in one
maximal constant-pivot run.

### Lemma 6.1

After all cuts, the residual singular locus is a finite disjoint union of open
constant-pivot intervals.  Each finite endpoint short side is one of:

- a literal root seam copy;
- a root-normalized local birth/death collar;
- a switch--pop collar carrying the root short side reconstructed in
  `AC_PD_5CDC_R2_7_FIXED_ORDER_CONSUMER_COMPATIBILITY.md`;
- the unresolved original outer endpoint.

For a closed original track with at least one pivot change, every residual
endpoint is a seam copy.

---

## 7. Relative constant-run rootification

Let one residual interval be

\[
F_t=\{s,d_t\},
\qquad a\le t\le b.
\]

At each transition, the side-root equation uniquely chooses the nonpivot
resolution

\[
r_t=d_t.
\]

The full-state constant-pivot theorem gives one simultaneous section which:

- rootifies every atom in the interval;
- preserves every emitted side-root occurrence;
- preserves every exterior rooted attachment and incidence order;
- preserves support transport, cap block and route;
- matches the actual root endpoint resolution at each end.

The endpoint matching is literal.  At a pivot-change state `{s,t}`, the
`s`-pivot run forces resolution `t`, while the `t`-pivot run forces resolution
`s`; these are precisely the two root sides furnished by the local seam of
Section 4.

### Theorem 7.1 — complete-boundary constant-run strip

Every residual constant-pivot interval whose two short sides are root-valued
has a root-valued rectangular replacement fixing its complete boundary.

If a closed track has no pivot change, it is one closed constant-pivot run.
The same nonpivot section closes because the initial and terminal complete
state of the circle is identical.  Nontrivial support transport is retained in
the rooted data and is not declared trivial.

---

## 8. Identity gluing

For every cut seam, the adjacent run strips use exactly the root state supplied
by the seam.  They agree on:

- source vertex and dart slots;
- all edge roots;
- crossed-resolution choice;
- side-root and support-transport data;
- cap block and route orientation;
- surviving or suspended marks.

Hence pieces glue by the identity map on the complete labelled state.
Coefficient equality alone is not used.

### Theorem 8.1 — closed-track erasure

Every finite closed normalized full-state co-root track has a singularity-free
root-valued cylinder replacement with the same complete labelled exterior
boundary.

### Proof

If there is no pivot change, apply the closed constant-run section.  Otherwise
place the disjoint seams, cut, rootify all constant-run intervals and glue by
identity.  Every replacement piece is root-valued, so the reconstructed
cylinder contains no singular edge. ∎

This conclusion is independent of Petersen simple-cycle length.  In
particular, the `C_5/C_6/C_8/C_9` extraction and a global `C_6/C_8` canonical
section are not load-bearing inputs to Theorem 8.1.

---

## 9. Open tracks

### Both endpoints root-normalized

If both endpoint collars have root-valued short sides, include those sides,
place all interior seams, rootify all residual constant-pivot intervals and
glue.

### Theorem 9.1 — normalized open-track erasure

An open normalized track with two root-valued short sides has a root-valued
rectangle replacement fixing both long histories and both complete short
sides.

Switch--pop collars satisfy this hypothesis by the explicit placement of their
short side on the preceding root-valued `B` insertion boundary.

### Accepted exits

A route/profile, bounded, theta or separator/category exit terminates the
current proof branch.  It is not necessary to manufacture a root rectangle
past that terminal.  The phrase “accepted endpoint” is therefore a discharge
condition, not an assertion that every terminal gadget is an internal
root-valued Ptolemy side.

### One unresolved outer endpoint

If exactly one endpoint is the unresolved original outer context, consume all
closed pieces and every completed constant-pivot interval.  The unique final
component incident with that outer side remains the exact endpoint obligation.
It is not declared rootified.

This preserves the endpoint-scope correction.

---

## 10. Periodic unresolved endpoint

Assume variable-order calls have already been compressed to fixed order and
the same complete unresolved endpoint state occurs twice.

Identify the two collars by the identity on their complete labelled state.
The intervening comparison becomes a finite history cylinder; every singular
component in it is closed.  Apply Theorem 8.1 component by component to obtain
a connected root-valued history cylinder with the same two boundary histories.

### Lemma 10.1 — connected root `1`-skeleton

The `1`-skeleton of the resulting finite history cylinder is connected.

### Proof

Every `2`-cell is attached along the connected image of a circle and therefore
cannot join two previously disconnected components of the `1`-skeleton.  If
the `1`-skeleton were disconnected, the whole cell complex would be
disconnected. ∎

Choose a shortest `1`-skeleton path between the two boundary components.  It
is simple, and no internal vertex lies on either boundary, since otherwise the
path could be shortened.  It is therefore a proper embedded root-valued
crosscut of the cylinder.  Cutting along it gives a root-valued rectangle.

### Theorem 10.2 — periodic endpoint discharge

A repeated complete unresolved endpoint occurrence can be replaced by a
root-valued rectangle, strictly removing the two unresolved occurrences while
fixing both long labelled boundary histories.

---

## 11. Dependency and supersession consequences

### Retained load-bearing inputs

- one-token nonbranching and complete full-state state semantics from `R2.4`;
- source-faithful immediate-backtrack removal;
- the local genuine pivot-change `(0,2,2)` seam;
- the unique side-preserving constant-pivot root section;
- switch--pop root endpoint collars;
- literal full-labelled seam gluing.

### No longer required for R2.6

- a global canonical `C_6` history section;
- simultaneous or alternating six-star source states;
- `C_8=C_6\triangle C_6` as an annulus theorem;
- a proper Petersen subcycle treated as a complete physical annulus;
- a raw support-switch correction inside a closed Ptolemy core;
- target-order descent inside track erasure.

`AC_PD_5CDC_R2_5_ORIENTED_ODD_EXCLUSION.md` remains a valid independent
strengthening of the forced backbone, but odd-cycle exclusion is not needed by
the cellwise erasure theorem.  The proof DAG is therefore strictly shorter
than the earlier `R2.4 -> R2.5 -> C6/C8 -> R2.7` route.

---

## 12. Trust boundary

### Closed here

- exact human proof of the `120/120` side-root intersection table;
- one complete root seam at every genuine pivot change;
- disjoint seam collars after identity subdivision;
- reduction to constant-pivot intervals;
- endpoint-relative constant-run rootification;
- literal full-state seam/run gluing;
- closed-track root cylinder;
- normalized open-track root rectangle;
- one-unresolved-endpoint scope;
- periodic endpoint root crosscut.

### Still downstream

- final R2.7 resolved-call/contextual-transfer synthesis;
- literal audit of all cap/route/terminal consumers at the R2-to-R1 interface;
- independent adversarial audit of the complete dependency graph;
- cap restoration and the global five-support/five-CDC theorem.

### No downstream status implied

No Lean theorem, Curator/canonical movement, manuscript acceptance, release,
tag, arXiv, DOI, peer review or publication status follows from this dossier.
