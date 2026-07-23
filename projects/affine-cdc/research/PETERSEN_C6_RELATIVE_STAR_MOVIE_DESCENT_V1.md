# Petersen identity `C6` tracks admit a relative root movie to strict cancellation

## Research dossier v1 — primitive even-track consumption

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `067d0331476954207d27f717bce8748bfc4f4b50`.

**Parents:**

- `PTOLEMY_ROOT_TUBE_HISTORY_LIFT_SCOPE_CORRECTION_V1.md`;
- `PETERSEN_C6_CANONICAL_STAR_SECTION_V1.md`;
- `PIVOT_CHANGE_SIX_PORT_STAR_COMPLETION_V1.md`;
- `SIX_LEAF_NNI_ROOT_EXCHANGE_V1.md`;
- `PACHNER_FIRST_FAILURE_CRITICAL_OVERLAP_V1.md`;
- `ROOT_FLOW_TRIANGLE_COMPLEX_PACHNER_V1.md`;
- `CONTEXTUAL_TRANSFER_TARGET_ORDER_CORRECTION_V1.md`;
- the category-safe root NNI and equal-face cancellation alternatives.

**Status:** exact relative-movie theorem for the sole primitive even Petersen orbit. After the two adjacent constant-pivot turns of one identity-hexagon cell are root-resolved, they give two fixed root corollas. Relative to those corollas, the remaining local interface has branch word `(z,z,w,w)`. Its three binary topologies have pairing-sum pattern `(0,2,2)`: one zero/equality path and exactly two root topologies, namely the canonical fixed-triangle star and one cross path. Hence every root-valued boundary lift of the Ptolemy annulus is either already the canonical star or differs from it by the unique root-preserving NNI fixing both overlap corollas and all exterior ports. The canonical star contains one internal equal-face dipole. Cancelling it gives strict cap-target order descent, unless the category-safe alternative exposes an already established separator or bounded degeneration. Thus a simple Petersen `C6` track cannot be a closed same-order contextual obstruction.

**Assurance boundary:** this theorem consumes `C6` by a root movie followed by strict cancellation; it does not claim that the earlier abstract longitudinal word itself labels every original history state. It repairs the primitive even-track branch by a different, stronger source-level exit. The `C8` consequence still uses the exact two-`C6` decomposition and must preserve its seam data as stated below.

---

## 1. One identity-hexagon pivot cell

Let

\[
p_{i-1},p_i,p_{i+1},p_{i+2}
\]

be four consecutive pivots on one simple Petersen `C6`, and let

\[
z_i,\quad z_{i+1}
\]

be the emitted side roots at `p_i,p_(i+1)`.

Use the six-port notation

\[
(s,x,z\mid w,t,y)
=
(p_i,p_{i-1},z_i
\mid
z_{i+1},p_{i+1},p_{i+2}).
\]

The two turn equations are

\[
\boxed{x+t=z}
\]

and

\[
\boxed{s+y=w.}
\]

The adjacent constant-pivot runs are already root-resolved in the forced-backbone normal form. Therefore they determine two fixed root-labelled corollas:

\[
\boxed{L=(x,t,z)}
\]

and

\[
\boxed{R=(s,y,w).}
\]

Both are root triangles.

The six-port cell also has one exterior side incidence labelled `z` and one labelled `w`. After contracting the fixed rooted branches `L,R` to their outgoing root values, the unresolved middle is therefore a four-branch interface with ordered multiset

\[
\boxed{(z,z,w,w).}
\]

The two copies of each root are distinct incidences: one is the spoke of a turn corolla and one is the exterior side port.

---

## 2. Exact relative triality

Write the four rooted branches as

\[
L_z,\quad Z,\quad W,\quad R_w,
\]

where their values are respectively

\[
z,z,w,w.
\]

There are three binary resolutions.

### Equality resolution

Pair

\[
L_z-Z
\]

and

\[
W-R_w.
\]

Both central sums are zero:

\[
z+z=0,
\qquad
w+w=0.
\]

This is the singular equality path.

### Cross-path resolution

Pair

\[
L_z-W
\]

and

\[
Z-R_w.
\]

Both central sums are

\[
\boxed{u=z+w.}
\]

In an identity hexagon, `z,w` are two distinct members of the repeated side-root triangle, so `u` is its third root. This topology is root-valued.

### Star resolution

Pair the two turn branches

\[
L_z-R_w
\]

and pair the two exterior side branches

\[
Z-W.
\]

Again both sums are `u=z+w`. Expanding the second pair as its cherry gives exactly the canonical three-cherry star of `PETERSEN_C6_CANONICAL_STAR_SECTION_V1.md`:

- turn cherry `(x,t)` with spoke `z`;
- turn cherry `(s,y)` with spoke `w`;
- side cherry `(z,w)` with spoke `u`;
- central triangle `(z,w,u)`.

Therefore:

### Theorem 2.1 — relative `(0,2,2)` table

Relative to the fixed turn corollas `L,R`, the complete local topology table is

\[
\boxed{
\text{one equality path}
+
\text{one root cross path}
+
\text{one root canonical star}.}
\]

The two root topologies have the same complete six-port boundary and differ by one NNI on the middle edge. The third NNI topology has central value zero.

This is exactly the four-root pairing-sum pattern

\[
\boxed{(0,2,2).}
\]

---

## 3. Unique relative root exchange

Let

\[
P_i^\times
\]

be the root cross path and

\[
S_i^\star
\]

be the canonical star.

### Theorem 3.1 — one-move relative movie

There is one unique root-preserving NNI

\[
\boxed{
P_i^\times
\longleftrightarrow
S_i^\star
}
\]

which fixes throughout:

1. the complete turn corolla `L=(x,t,z)`;
2. the complete turn corolla `R=(s,y,w)`;
3. all six labelled boundary incidences;
4. every exterior source edge and root value.

The opposite NNI direction is the zero/equality path.

### Proof

After treating `L,R,Z,W` as four rooted branches, the two root resolutions and the zero resolution are exactly the three NNI topologies of Section 2. The two-root rule gives a unique root-preserving exchange between the two root topologies. Since NNI changes only the middle pairing of the four rooted branches, `L,R` and all their internal labels are untouched. ∎

### Corollary 3.2 — relative classification of root lifts

Every root-valued local lift of the two-turn cell which respects the already fixed turn corollas is exactly one of:

\[
P_i^\times,
\qquad
S_i^\star.
\]

Hence it is either already canonical or reaches the canonical star in one root NNI.

No unrestricted twenty-state six-leaf connectivity theorem is needed. The relative state space has only two root vertices.

---

## 4. Why the annular boundary satisfies the relative hypothesis

Let `gamma` be one reduced closed co-root track in a lifted Ptolemy van Kampen diagram. A sufficiently small regular neighbourhood `N(gamma)` is an annulus whose two boundary circles lie in the root-valued part of the lift.

At a pivot-change cell, the forced-backbone normal form includes the two adjacent constant-pivot turns. The pivot-resolution theorem fixes their root resolutions as `t` on the left and `s` on the right, equivalently the two corollas

\[
L=(x,t,z),
\qquad
R=(s,y,w).
\]

The restriction of either annular boundary lift to the cell is root-valued and retains those turn data. Therefore Corollary 3.2 applies.

### Theorem 4.1 — local boundary-to-star movie

For every pivot-change cell of a Petersen identity `C6`, each root-valued annular boundary restriction either:

1. already equals `S_i^star`; or
2. equals `P_i^times` and reaches `S_i^star` by the unique relative root NNI.

If the incidence-level NNI does not remain in the connected bridgeless cubic category, the category-safe theorem exposes a two-/three-/four-edge separator, loop/parallel degeneration, or bounded appendage in the relevant pre-move graph. That is an established exit.

---

## 5. Compatibility on adjacent cells

Consecutive identity-hexagon cells share exactly one resolved turn corolla. In the notation of the canonical-section theorem, the shared corolla is

\[
R_{i+1}
=
(p_i,p_{i+2},z_{i+1}).
\]

The relative NNI of Theorem 3.1 treats that corolla as an unchanged rooted branch. Thus:

### Theorem 5.1 — relative movie overlap

The local boundary-to-star movies on adjacent cells agree at every shared source incidence:

- the shared corolla is fixed pointwise;
- its three root labels are unchanged;
- no local NNI support contains an internal vertex of the shared corolla;
- the two local movies may be glued after the usual cell subdivision of the annular neighbourhood.

If two movie supports are scheduled sequentially, the first leaves the complete rooted branch used by the second unchanged. Hence the second remains the same relative NNI. No new critical-pair datum is introduced.

### Proof

The NNI support is the two middle vertices of the relative four-branch interface. The turn corollas occur only as rooted exterior branches. Consecutive cells share one such branch and have disjoint middle interiors in the regular cell subdivision of `N(gamma)`. The incidence labels on the common branch agree by `PETERSEN_C6_CANONICAL_STAR_SECTION_V1.md`. ∎

### Corollary 5.2 — coherent canonicalisation

All six local annular boundary restrictions can be changed coherently to the six canonical star sections without changing the exterior root data, ordered cap shore, or side-root word.

This is a genuine relative history movie, not a pointwise reinterpretation of the old co-root transition pairs as arbitrary longitudinal roots.

---

## 6. Strict cancellation inside the star

In `S_i^star`, the central vertex has incident root triangle

\[
(z,w,u),
\qquad u=z+w.
\]

The outer side-cherry vertex has boundary roots `z,w` and internal root `u`. It carries the identical support triangle

\[
(z,w,u).
\]

They are joined by the edge `u`.

### Theorem 6.1 — internal equal-face dipole

Every canonical star contains an equal-face pair joined along `u`. Cancelling it:

1. removes exactly two source vertices;
2. preserves the complete six-port root boundary;
3. preserves both fixed turn corollas;
4. preserves every exterior side-root incidence;
5. creates no coefficient defect.

If the cancellation leaves the connected bridgeless category, the category-safe alternative exposes an established separator or bounded degeneration.

### Corollary 6.2 — strict target-order exit

After coherent canonicalisation, choose any one canonical cell and cancel its internal equal-face dipole. Then exactly one of:

\[
\boxed{
\text{cap-context target order drops by two}
}
\]

or

\[
\boxed{
\text{separator/category exit occurs}.}
\]

Thus the closed track cannot remain in a fixed-order nonterminal component.

---

## 7. Primitive `C6` consumption theorem

### Theorem 7.1 — no same-order Petersen `C6` obstruction

Let `gamma` be a closed nonbranching first-failure track in an oriented fixed-route Ptolemy history, and suppose its reduced Petersen core is a simple `C6`.

Then one of:

1. a relative root NNI or equal-face cancellation exposes a separator/category exit;
2. the annular lift is coherently changed to the canonical star section and one internal equal-face dipole is cancelled, giving a cap-context problem with two fewer vertices.

Consequently a simple Petersen `C6` cannot support a closed same-order contextual sink.

### Proof

Apply Theorem 4.1 cellwise and glue the local movies by Theorem 5.1. If no category exit occurs, Corollary 5.2 reaches the canonical section complex. Apply Theorem 6.1 to one cell. ∎

### Important distinction

The theorem does not erase the `C6` by relabelling the original annulus with the abstract longitudinal word

\[
(b,c,a,b,c,a).
\]

Instead it constructs legal root NNIs to a canonical source topology and then uses an actual equal-face cancellation. This directly answers the history-lift scope correction without asserting the false pointwise identification of tube roots with original atom resolutions.

---

## 8. Consequence for `C8`

`PETERSEN_C8_TWO_C6_HISTORY_FILLING_REDUCTION_V1.md` decomposes every simple `C8` into two `C6` identity cells with:

- unchanged nonseam side roots;
- one equal middle seam root;
- root-triangle seams at the two endpoints.

The relative `C6` movies fix all side and seam corollas. Therefore they remain valid after the two cells are glued.

### Theorem 8.1 — even-track strict descent

Every simple even Petersen track (`C6` or `C8`) yields one of:

\[
\boxed{
\text{separator/category exit}
}
\]

or

\[
\boxed{
\text{strictly smaller cap-context target}.}
\]

For `C8`, apply the relative movie in either one of the two `C6` factors while holding the common seam fixed, then cancel its internal equal-face dipole.

Thus no primitive abstract `C8` history lift is needed beyond the exact two-`C6` seam theorem.

---

## 9. Repair of the corrected contextual-transfer interface

The scope correction retained:

- forced Petersen tracks;
- odd-cycle exclusion;
- exact `C6/C8` side words;

but made even-track removal conditional on a coherent history lift.

The present theorem supplies a logically sufficient replacement:

- local history cells are reduced relative to their fixed turn corollas;
- every root-valued annular boundary lift is one NNI from a canonical star;
- adjacent movies preserve common rooted branches;
- canonical stars have strict equal-face cancellations.

Therefore the even-track branch no longer requires a same-order root tube filling. It exits through strict target-order descent.

### Corollary 9.1 — restored even-track disposition

In a fixed-order contextual state graph, a recurrent co-root track cannot contain an even simple Petersen cycle without reaching a lower-order or category exit.

Combined with the established odd-cycle orientation contradiction, no closed reduced Petersen track survives in a nonterminal same-order sink.

### Corollary 9.2 — contextual induction interface

A first-failure atom transported through a pure Pachner block either:

1. reaches complete root transfer;
2. changes route/profile;
3. exposes a separator/category exit;
4. reaches a bounded direct-pairing terminal;
5. or enters the strict-order layer by the cancellation of Theorem 6.1.

This restores the well-founded same-order-to-strict-order transition at the precise interface quarantined by `PTOLEMY_ROOT_TUBE_HISTORY_LIFT_SCOPE_CORRECTION_V1.md`.

---

## 10. Trust boundary

### Exact here

- reduction of one two-turn cell to the relative branch word `(z,z,w,w)`;
- complete `(0,2,2)` topology table relative to the fixed turn corollas;
- the unique one-NNI movie from the root cross path to the canonical star;
- preservation of both overlap corollas and all six boundary roots;
- compatibility of adjacent relative movies under the annular cell subdivision;
- the internal equal-face dipole of every canonical star;
- strict target-order or category exit from every simple Petersen `C6`;
- extension to `C8` through the two-`C6` seam reduction;
- replacement of the unsupported abstract-tube history lift by a root-NNI/cancellation descent.

### Imported authorial mathematics

- the forced-backbone two-turn cell and fixed turn resolutions;
- the category-safe NNI and equal-face cancellation alternatives;
- the annular regular-neighbourhood description;
- odd Petersen cycle exclusion;
- the `C8` two-`C6` seam theorem;
- strict target-order bookkeeping after a genuine cancellation.

### Still outside this checkpoint

- downstream proof-development expansion or independent verification of the imported local cell incidence model;
- curation or canonical movement;
- Lean verification;
- manuscript integration;
- release, arXiv, DOI, peer review, or publication.
