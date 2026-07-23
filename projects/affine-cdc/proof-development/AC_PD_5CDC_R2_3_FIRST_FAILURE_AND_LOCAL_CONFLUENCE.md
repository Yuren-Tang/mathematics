# AC-PD-5CDC-R2.3 — first failure and local confluence

**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Programme:** compressed five-support proof, extension unit `R2`  
**Classification:** `COMPLETE-DRAFT / F CLOSED / LOCAL L CLOSED / GLOBAL RETURN ACTIVE`.

This dossier reconstructs the first-failure and bounded critical-overlap portions of the contextual-return theorem. It deliberately separates local confluence from the still-global recurrence and strict-order interfaces.

Controlling RL sources:

- `PACHNER_HISTORY_FIRST_FAILURE_ONE_EDGE_ATOM_V1.md`;
- `PACHNER_FIRST_FAILURE_CRITICAL_OVERLAP_V1.md`;
- `FIRST_FAILURE_NORMALIZATION_AUTOMATIC_CATEGORY_SAFETY_V1.md`;
- `FULL_DEFECT_TREE_NNI_DESCENT_V1.md`;
- `ROOT_SURGERY_AUTOMATIC_CATEGORY_SAFETY_V1.md`;
- `CONTEXTUAL_TRANSFER_TARGET_ORDER_CORRECTION_V1.md`.

---

## 1. First failed inverse step

Let

\[
G_0\to G_1\to\cdots\to G_m
\]

be a finite history of root-valued `2--2` flips and equal-face `2--0` cancellations. Start with an arbitrary root-valued flow on `G_m` and reverse the history while every restored central edge remains a root.

At the first failed inverse step all pre-existing edges are roots. Only the restored central edge is new.

### Inverse `2--2`

If the four exterior roots are `a,b,c,d`, conservation gives

\[
a+b=c+d=:x.
\]

The other current pairing is root-valued. The binary four-root sum law gives

\[
\operatorname{wt}(x)\in\{0,2,4\}.
\]

Failure means `x` has weight zero or four.

### Inverse `2--0`

If the two reconnected edges of the smaller graph have roots `a,b`, reinsertion forces

\[
x=a+b.
\]

Again failure means either `a=b`, so `x=0`, or `a,b` are disjoint, so `x` is a co-root.

### Theorem 1.1 — one-edge first-failure atom

At the first failed inverse step:

1. every edge except the restored central edge remains root-valued;
2. both restored cubic conservation equations hold;
3. the unique non-root edge is labelled `0` or one co-root `Q_i`;
4. the ordered four exterior incidences, old/new pairing, cap block and route orientation are retained.

No defect network is accumulated before localization.

---

## 2. The zero branch

### Inverse-flip zero

Suppose `x=0` in an inverse `2--2` failure. Then the old pairing has boundary word

\[
a,a,b,b.
\]

The current topology is root-valued, so it pairs `a` with `b` and has central value `a+b\in R_5`. Therefore `a,b` are distinct intersecting roots. The second crossed topology also has central root `a+b`.

Hence every inverse-flip zero failure has an immediate root-valued alternative NNI. Quadruple equality is impossible in this row.

### Inverse-cancellation zero

For a failed inverse cancellation, `x=0` means `a=b` and the four exterior roots are

\[
a,a,a,a.
\]

All three pairing sums are zero. There is no immediate root NNI. This is the unique quadruple-equality recursive branch.

Thus the statement “zero atoms rootify immediately” is valid only for a pure same-order inverse-flip block. The inverse-cancellation equality row must be routed through a separately justified strict-order/contextual recursion theorem.

---

## 3. One atom adjacent to one root flip

Let the unique defect edge `c` have value `x(c)`, and suppose a neighbouring root edge `a` is the central edge of a root Pachner move. At the far root vertex write

\[
a=d+e,
\]

where `d,e` are distinct intersecting roots. The two alternative central values are

\[
q=x(c)+d,
\qquad
r=x(c)+e.
\]

### Zero atom

If `x(c)=0`, then `q=d,r=e` are roots. The zero edge remains the sole defect and no second defect is created. In the inverse-flip branch one immediately chooses the alternative topology that removes the zero state.

### Co-root atom

Let `x(c)=Q_i`. The adjacent root `a` avoids `i`, so `d_i=e_i`.

1. If both `d,e` avoid `i`, then `Q_i+d,Q_i+e` are roots. The atom commutes/relocates without proliferation.
2. If both contain `i`, write `d=ij,e=ik`. Then
   \[
   Q_i+d=Q_j,
   \qquad
   Q_i+e=Q_k.
   \]
   One NNI creates exactly one adjacent co-root, and the shared local state is
   \[
   (Q_i,Q_j,ij).
   \]

This is the unique bad critical overlap.

---

## 4. Normalization of the bad overlap

The transient bad-overlap defect support has exactly three defect-tree vertices and two adjacent co-root edges. It is a special case of the full-defect tree grammar.

At a co-root cherry `Q_i`, the two outer roots are disjoint and avoid `i`. If the neighbouring defect vertex is the transport state `(Q_i,Q_j,ij)`, exactly one of the two NNI central values

\[
A+Q_j,
\qquad
A+ij
\]

is a root, according as the cherry root `A` avoids or contains `j`. Thus one local NNI replaces one co-root edge by a root and lowers the defect count from two to at most one.

No general defect-tree minimality argument is needed for this three-vertex instance; the root alternative follows directly from the displayed two cases.

### Theorem 4.1 — bounded local critical-pair normalization

A first-failure atom meeting one root surgery has exactly one of:

1. disjoint strict commutation;
2. inverse-flip zero rootification;
3. one co-root relocation;
4. one transient two-co-root overlap followed by one root-lowering NNI.

After normalization there is either a root state or at most one co-root atom. There is no branching local alphabet and the defect count never exceeds two transiently.

---

## 5. Category safety

A connected graph carrying a group-valued flow has every bridge labelled zero, by summing conservation over one bridge shore.

Every persistent state in Sections 3--4 has only root and co-root values, all nonzero. A two-vertex NNI output is connected: after removing the old adjacent pair, the exterior has one component or two components each with two terminals; any replacement two-vertex topology reconnects them through a new vertex or the new central edge.

Therefore every co-root relocation and the transient normalization are connected and bridgeless. An inverse-flip zero branch is replaced immediately by a root-valued NNI and has the same property.

### Corollary 5.1

The local contextual move alphabet needs no separator/category branch:

- disjoint/root commutation;
- co-root relocation;
- bad-overlap normalization;
- inverse-flip zero removal

are all category-safe.

The inverse-cancellation quadruple-equality row remains outside this same-order alphabet.

---

## 6. What is and is not closed

The following hypotheses of the finite-condensation framework are now reconstructed:

- `F`: first failure produces exactly one zero/co-root central edge;
- the local algebraic part of `L`: no atom branching, no new coefficient type, bounded critical overlaps;
- automatic category safety of all persistent same-order token moves.

Still not closed by this dossier:

1. global exhaustiveness of the forced Petersen backbone after all full-state data are retained;
2. the oriented odd-cycle exclusion;
3. the relative `C6/C8` source movies;
4. the exact recursive treatment of inverse-cancellation quadruple equality;
5. the passage from a genuine cancellation exit to a fully justified lower-order contextual return.

These are the remaining global return obligations, not missing local coefficient algebra.