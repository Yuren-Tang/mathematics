# Open Petersen defect tracks admit root-valued strip replacements

## Research Lead diagrammatic endpoint theorem v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Parents:**

- `PETERSEN_PIVOT_RESOLUTION_V1.md`;
- `PIVOT_CHANGE_SIX_PORT_STAR_COMPLETION_V1.md`;
- `PETERSEN_C6_CANONICAL_STAR_SECTION_V1.md`;
- `PETERSEN_C6_RELATIVE_STAR_MOVIE_DESCENT_V1.md`;
- `CONSTANT_PIVOT_FULL_STATE_CONTEXTUAL_CONSUMPTION_V1.md`;
- `ROOT_VALUED_ALTERNATIVE_INVERSE_CANCELLATION_INSERTION_V1.md`;
- `DOUBLED_DISJOINT_THREE_VERTEX_BORROWING_DICHOTOMY_V1.md`.

**Status:** exact root-strip theorem for the sole endpoint case left after closed-track erasure. The canonical relative star cell used on a Petersen `C6` is not special to the six-cycle. For every nonbacktracking four-pivot path, the two consecutive emitted side roots are distinct intersecting roots. Hence every open pivot-change cell has the same relative `(0,2,2)` table: one singular path, one root cross path, and one canonical root star, with fixed turn corollas. Along an open defect track the canonical cells glue linearly, with no cyclic holonomy condition. The two root-valued long sides of a regular rectangular neighbourhood both canonicalise to the same star strip. Concatenating the canonicalisations replaces the complete open co-root track by a root-valued history rectangle while preserving all four sides of the rectangle.

This theorem closes the open-arc interface left by `PTOLEMY_CLOSED_DEFECT_TRACK_ERASURE_V1.md`.

---

## 1. Four consecutive pivots

Let

\[
x,s,t,y
\]

be four consecutive pivots of a reduced Petersen path, so

\[
x\perp s,
\qquad
s\perp t,
\qquad
t\perp y,
\]

and there is no immediate backtrack:

\[
x\ne t,
\qquad
s\ne y.
\]

Let `z` be the third Petersen neighbour of `s` outside `{x,t}`, and let `w` be the third Petersen neighbour of `t` outside `{s,y}`.

Thus the turn equations are

\[
\boxed{x+t=z,}
\]

and

\[
\boxed{s+y=w.}
\]

---

## 2. Consecutive side roots always intersect

### Theorem 2.1 — open-cell side-triangle lemma

For every nonbacktracking four-pivot path,

\[
\boxed{
z\ne w,
\qquad
z\cap w\ne\varnothing.
}
\]

Hence

\[
\boxed{u=z+w\in R_5.}
\]

### Proof

By support permutation normalize the central Petersen edge to

\[
s=12,
\qquad
t=34.
\]

The three neighbours of `12` are

\[
34,35,45.
\]

Since `x` and `z` are the two neighbours other than `t=34`, one has

\[
\{x,z\}=\{35,45\}.
\]

Likewise the three neighbours of `34` are

\[
12,15,25,
\]

so

\[
\{y,w\}=\{15,25\}.
\]

Every root in `{35,45}` and every root in `{15,25}` share the support index `5`, and no two are equal. Therefore `z,w` are distinct intersecting roots. ∎

### Exact finite certificate

There are

\[
\boxed{120}
\]

ordered nonbacktracking four-pivot paths in the Petersen graph. Exhaustive enumeration gives `intersect` in all `120` cases, with no equal or disjoint exception.

---

## 3. Canonical star for an arbitrary open cell

Use the six-port boundary

\[
B=(s,x,z\mid w,t,y).
\]

Define the matching

\[
\boxed{
\begin{cases}
s\longleftrightarrow y,\\
x\longleftrightarrow t,\\
z\longleftrightarrow w.
\end{cases}}
\]

The three forced internal spoke roots are

\[
s+y=w,
\qquad
x+t=z,
\qquad
z+w=u.
\]

By Theorem 2.1 all three are roots, and

\[
z+w+u=0.
\]

Thus they form the root triangle

\[
(z,w,u).
\]

### Theorem 3.1 — open-cell canonical star

Every nonbacktracking pivot-change cell has a root-valued three-cherry star completion whose fixed turn corollas are

\[
L=(x,t,z),
\qquad
R=(s,y,w),
\]

and whose side cherry and centre both carry the root triangle `(z,w,u)`.

The canonical star contains an equal-face pair, but no cancellation will be used in the strip theorem.

---

## 4. Relative `(0,2,2)` table

Treat the turn corollas `L,R` as fixed rooted exterior branches. The unresolved middle has four branch values

\[
(z,z,w,w).
\]

Because `z,w` are distinct intersecting, its three binary resolutions are:

1. one zero/equality path;
2. one root cross path;
3. the root canonical star of Theorem 3.1.

The two root topologies differ by the unique root-preserving relative NNI fixing:

- both turn corollas;
- all six boundary incidences;
- all side-root values;
- every exterior source edge.

### Corollary 4.1 — common canonical target

Every root-valued restriction of either side of a pivot-change history cell is either the root cross path or the canonical star, and therefore canonicalises to the same star in at most one relative root NNI.

---

## 5. An open defect track and its rectangle

Let

\[
\gamma
\]

be one open nonbranching co-root track in a lifted Ptolemy comparison. After resolving maximal constant-pivot runs and deleting immediate backtracks, write its ordered pivot-change cells as

\[
B_1,B_2,\ldots,B_k.
\]

Choose a sufficiently small regular neighbourhood

\[
N(\gamma)
\]

which is a rectangle. Its boundary consists of:

- two long sides
  \[
  \partial_-N(\gamma),
  \qquad
  \partial_+N(\gamma),
  \]
  lying in the root-valued histories on the two sides of the defect;
- two short endpoint sides lying in the root-valued local normalisation cells or in an accepted route/bounded boundary cell.

Zero-valued endpoints do not occur:

- inverse-flip zero uses the other root NNI;
- inverse-cancellation equality uses a direct root-valued alternative insertion;
- good doubled-disjoint cancellation uses a direct root-valued alternative insertion.

Thus every unbounded open singular arc is purely co-root and has root-valued two-sided boundary data.

---

## 6. Linear gluing of canonical cells

Consecutive pivot-change cells share one complete rooted turn corolla. Every relative NNI of Section 4 fixes that corolla pointwise.

Unlike a closed track, an open chain has no final-to-initial identification. Therefore no return character or cyclic compatibility condition is required.

Canonicalise every cell restriction on the minus side to its canonical star, in path order. The moves glue because the common turn branch is fixed. Do the same on the plus side.

Both sides reach one and the same canonical star strip

\[
\mathcal T_\gamma^\star.
\]

At the two endpoints, the local relative moves fix all six external incidences, hence in particular fix the short sides of the rectangle.

### Theorem 6.1 — two-sided canonicalisation of an open track

There are root-valued relative history movies

\[
\partial_-N(\gamma)
\rightsquigarrow
\mathcal T_\gamma^\star,
\]

and

\[
\partial_+N(\gamma)
\rightsquigarrow
\mathcal T_\gamma^\star,
\]

which agree on all four sides of `partial N(gamma)` and preserve every rooted exterior attachment.

---

## 7. Root-valued strip replacement

Reverse the plus-side canonicalisation and concatenate:

\[
\partial_-N(\gamma)
\rightsquigarrow
\mathcal T_\gamma^\star
\leftsquigarrow
\partial_+N(\gamma).
\]

This is a history rectangle all of whose source states and history edges are root-valued.

### Theorem 7.1 — open-track root strip

Every open co-root defect track has a singularity-free root-valued strip replacement with exactly the same complete labelled rectangular boundary.

Replacing `N(gamma)` by this strip:

1. removes the open singular component `gamma`;
2. changes no history data outside the rectangle;
3. fixes both endpoint sides pointwise;
4. preserves the outer cap block and physical route;
5. introduces no zero or co-root edge;
6. requires no equal-face cancellation or target-order recursion.

---

## 8. Constant-pivot and bounded endpoint cases

### No pivot change

An open constant-pivot track has the unique nonpivot root section. It is already a root-valued strip and disappears.

### Immediate backtrack

The normalized `abba` unit cancels before forming the reduced open chain.

### Bounded source identification

If an endpoint cell contains a loop, parallel-edge collapse, or insufficient adjacent root vertex for the borrowing construction, it is one of the established bounded theta/direct/separator exits and need not enter the strip.

### Missing-index endpoint

The missing-index doubled-disjoint borrowing produces the standard transport cell `(Q_i,Q_j,ij)`. This is precisely the first cell of the co-root track and is covered by the strip construction after full-state normalization.

---

## 9. No short-open-core case remains

The earlier forced-backbone theorem reduced an open track to a simple Petersen path of at most nine edges but left finite source analysis open.

The strip theorem is stronger: its proof is uniform in path length and uses only the local nonbacktracking side-triangle lemma. Therefore no separate enumeration of the finitely many simple paths is needed.

### Corollary 9.1

Every short open Petersen skeleton, with arbitrary constant-pivot rooted decorations retained, is diagrammatically root-removable or exits through an established bounded/route branch.

---

## 10. Assurance boundary

### Exact here

- the `120/120` consecutive-side intersection theorem;
- the canonical root star on every open pivot-change cell;
- the relative `(0,2,2)` table for arbitrary nonbacktracking cells;
- linear compatibility of canonical cells along an open chain;
- preservation of both endpoint sides;
- singularity-free root strip replacement for every open co-root track;
- removal of the previously unclassified short-open-core branch.

### Imported authorial mathematics

- full-state track/backbone identification;
- constant-pivot root sections;
- first-failure nonbranching;
- root-valued alternative inverse-cancellation insertions;
- source-category safety of relative root NNIs;
- bounded endpoint exits.

### Not supplied here

- downstream PDL reconstruction or independent audit;
- a final reassembled contextual-transfer theorem;
- cap restoration or global five-support closure;
- Lean verification, manuscript integration, release, arXiv, DOI, peer review, or publication.
