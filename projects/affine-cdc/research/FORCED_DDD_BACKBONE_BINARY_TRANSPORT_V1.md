# Forced DDD backbones carry one transported binary route, not one bit per cell

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `da10c05c3ef80fa1e5315aa6c9e43cf57c5ab417`  
**Parents:**

- `projects/affine-cdc/research/PIVOT_CHANGE_SIX_PORT_STAR_COMPLETION_V1.md`;
- `projects/affine-cdc/research/PETERSEN_PIVOT_RESOLUTION_V1.md`;
- `projects/affine-cdc/research/DDD_ROUTE_ORIENTATION_COVER_V1.md`;
- `projects/affine-cdc/research/ORIENTED_CHANNEL_LOCK_BOUNDARY_CALIBRATION_V1.md`;
- `projects/affine-cdc/research/PETERSEN_BACKTRACKS_TYPE_T_BOUNDED_CORE_V1.md`.

**Status:** exact transport theorem for the residual branch in which every pivot-change six-port cell forces the disjoint pivot pair. The two remaining binary pairings are exactly the two crossed root routes of the central DDD atom. Canonical Petersen transport sends the unordered crossed-route pair of one atom bijectively to that of the next atom. Hence a chain of forced backbones carries a two-sheeted local system with one initial sheet and, on a closed return, one orientation holonomy; it does not carry an independent bit at every pivot change. In an oriented inverse-dipole lock the return holonomy is trivial. After formal Petersen backtrack reduction, every remaining obstruction is supported on a bounded reduced pivot path or one bounded simple Petersen cycle, together with the already retained side-root attachments.  
**Not implied:** graph-safe deletion of every backtrack, automatic elimination of the bounded simple-cycle core, strict separator extraction, global induction, canonical acceptance, Lean verification, manuscript readiness, or the global five-support theorem.

---

## 1. Crossed routes of one DDD state

Let

\[
F=\{s,t\}
\]

be one Petersen edge, so `s,t` are disjoint roots and together use four support indices.

The perfect matchings of those four support indices are:

1. the bad DDD matching
   \[
   B_F=\{s,t\};
   \]
2. two crossed root matchings
   \[
   X_F,
   \qquad
   Y_F.
   \]

For the standard state

\[
s=12,
\qquad
t=34,
\]

one may write

\[
X_F=\{13,24\},
\qquad
Y_F=\{14,23\}.
\]

These are exactly the two crossed route classes of the DDD quotient and the two root-valued alternatives to the original co-root realization.

---

## 2. The two forbidden star matchings are `X_F` and `Y_F`

Consider the six-port pivot-change cell

\[
F^-=\{s,x\}
\longrightarrow
F=\{s,t\}
\longrightarrow
F^+=\{t,y\},
\]

with emitted side roots `z,w`, so

\[
x+t+z=0,
\qquad
s+y+w=0.
\]

Its boundary is

\[
(s,x,z\mid w,t,y).
\]

The six-port star theorem gives two non-root-completable cross matchings. Both contain the forced pair

\[
s\mathbin{-}t.
\]

After deleting this pair, their other two internal root sums are exactly the two crossed matchings of `F`.

### Theorem 2.1 — binary-pairing identification

The two residual forbidden matchings are canonically

\[
\boxed{B_F+X_F}
\]

and

\[
\boxed{B_F+Y_F},
\]

where `B_F` denotes the forced co-root backbone and `X_F,Y_F` denote the two possible pairings of the remaining four ports.

### Standard certificate

For

\[
(s,t,x,z,y,w)
=(12,34,35,45,15,25),
\]

the two forbidden matchings are

\[
(12,34),\ (35,25),\ (45,15),
\]

whose two root sums are

\[
23,\ 14
\]

and hence give

\[
Y_F=\{14,23\},
\]

and

\[
(12,34),\ (35,15),\ (45,25),
\]

whose two root sums are

\[
13,\ 24
\]

and hence give

\[
X_F=\{13,24\}.
\]

Thus the binary residue of the six-port table is not a new pairing coordinate. It is exactly the old DDD crossed-route coordinate.

---

## 3. Transport between adjacent DDD states

Let three consecutive pivots be

\[
s,t,u
\]

with

\[
s\perp t,
\qquad
t\perp u,
\qquad s\ne u.
\]

The adjacent DDD states are

\[
F=\{s,t\},
\qquad
F'=\{t,u\}.
\]

Let `z` be the third Petersen neighbour of `t` distinct from `s,u`. The co-root transport theorem identifies the physical transition with the support transposition

\[
\tau_z.
\]

It satisfies

\[
\tau_z(t)=t,
\qquad
\tau_z(s)=u.
\]

### Theorem 3.1 — crossed-route transport

\[
\boxed{
\tau_z\bigl(\{X_F,Y_F\}\bigr)
=
\{X_{F'},Y_{F'}\}.
}
\]

In words: canonical Petersen transport maps the two crossed routes of one DDD atom bijectively onto the two crossed routes of the next atom.

### Proof

The transposition `tau_z` sends the bad matching

\[
B_F=\{s,t\}
\]

to

\[
B_{F'}=\{u,t\}.
\]

A support permutation sends the complete set of three perfect matchings of the four active support indices to the complete set of three perfect matchings of the new four active indices. Since it sends the distinguished bad matching to the distinguished bad matching, it sends the complementary two-element crossed set to the complementary two-element crossed set. ∎

### Exact finite certificate

There are sixty ordered adjacent Petersen triples `(s,t,u)` with `s ne u`. Exhaustive enumeration verifies in all sixty cases:

\[
\tau_z\{s,t\}=\{t,u\},
\]

and

\[
\tau_z\{X_F,Y_F\}=\{X_{F'},Y_{F'}\}.
\]

No exceptional transition occurs.

---

## 4. The forced-backbone local system

Let

\[
s_0,F_1,s_1,F_2,\ldots,F_k,s_k
\]

be the pivot skeleton of a residual co-root strip, where

\[
F_i=\{s_{i-1},s_i\}.
\]

Assume every pivot-change cell lies in the forced-backbone branch of the six-port star theorem.

At each `F_i` the residual choice is one of

\[
X_{F_i},
\qquad
Y_{F_i}.
\]

Theorem 3.1 supplies a transition bijection between the two choices at `F_i` and the two choices at `F_(i+1)`.

### Theorem 4.1 — one initial sheet

On an open pivot skeleton, choosing one crossed route at `F_1` uniquely transports a crossed route through every later forced-backbone cell.

Therefore a chain of `k` forced pivot changes has only

\[
\boxed{2}
\]

coherent crossed-route choices, not

\[
2^k.
\]

### Closed skeleton

On a closed pivot skeleton, transport may return the chosen crossed route or exchange the two sheets. Thus the complete residual binary datum is one return character

\[
\omega_{\mathrm{DDD}}\in\mathbf F_2.
\]

This is the existing crossed-route orientation holonomy, not a new chain invariant.

---

## 5. Oriented inverse-dipole locks kill the return bit

In the inverse-dipole setting, the two original cap vertices distinguish the two blocks of the fixed route. The oriented-channel calibration theorem therefore supplies a global orientation of the relevant crossed route.

The DDD orientation-cover theorem identifies sheet exchange with the character

\[
\nu_X=\kappa
\]

or

\[
\nu_Y=\kappa+\chi,
\]

depending on which crossed route is selected.

### Theorem 5.1 — no independent backbone holonomy

For a forced-backbone chain contained in one oriented inverse-dipole lock, the transported crossed-route sheet returns to itself. Hence

\[
\boxed{\omega_{\mathrm{DDD}}=0.}
\]

Equivalently, the DDD cocycle on the forced-backbone transport subgroup is a coboundary.

### Trust note

This theorem removes the affine/orientation bit. It does not by itself replace the source graph: side-root attachments and the forced bad backbone remain physical incidence data.

---

## 6. Backtracks and the Type-T word

Suppose the pivot skeleton contains an immediate backtrack

\[
s\longrightarrow t\longrightarrow s.
\]

The two DDD states are the same Petersen edge with opposite traversal directions.

The pivot-resolution theorem gives the forced shore-resolution word

\[
\boxed{t,\ s,\ s,\ t.}
\]

Thus every forced-backbone backtrack carries the exact Type-T word

\[
\boxed{abba}.
\]

The binary crossed-route sheet is transported out and back, so it contributes no additional state to this unit.

### Consequence 6.1

A pivot backtrack in the forced-backbone sector is precisely the already identified coefficient-side Type-T unit, now with its six-port binary residue calibrated.

The global physical Type-T four-pole kernel is impossible by disjoint-support route invariance. What remains open is only graph-safe localisation or removal of a Type-T unit embedded inside a larger interval.

---

## 7. Reduced pivot skeleton

Perform formal free reduction of the oriented Petersen pivot path by deleting adjacent inverse edges.

### Theorem 7.1 — no unbounded binary backbone state

After all formal backtrack cancellations, exactly one of the following holds.

1. **Short open skeleton.**  
   The reduced open pivot path has at most nine edges unless a pivot repeats.

2. **Bounded cycle core.**  
   A repeated pivot contains a shortest nonempty reduced closed subpath. It is a simple Petersen cycle on at most ten pivot vertices.

3. **Empty closed skeleton.**  
   The original closed skeleton is a product of Type-T backtrack units.

In every case the forced-backbone crossed-route data add at most one initial sheet and no further local bits. In an oriented lock even the closed return bit is zero.

### Proof

This is free edge-path reduction in the Petersen graph, together with Theorems 4.1 and 5.1. The Petersen graph has ten vertices, so an open reduced path with more than nine edges repeats a vertex; a shortest repeated-vertex segment is a simple cycle. ∎

---

## 8. Revised residual DDD frontier

The forced-backbone branch no longer contains an arbitrary chain of independent six-port choices.

It has the exact normal form

\[
\boxed{
\text{rank-two constant-pivot runs}
+
\text{Type-T backtrack units}
+
\text{one bounded reduced Petersen skeleton}
}
\]

with one globally transported crossed-route sheet.

Thus the only remaining graph-side tasks are:

1. composition-safe elimination of an embedded Type-T backtrack unit;
2. finite analysis of one bounded simple Petersen-cycle core with its side attachments;
3. separator extraction when those attachments prevent a crossed star route;
4. integration with rank-one equality transport defects and rank-two braid defects.

There is no remaining unbounded DDD state alphabet or independent binary word.

---

## 9. Trust boundary

### Exact here

- identification of the two forbidden six-port pairings with the DDD crossed routes `X_F,Y_F`;
- transport of the crossed-route pair under every adjacent Petersen transition;
- the sixty-transition finite certificate;
- reduction from one bit per cell to one transported two-sheet local system;
- triviality of the return bit in an oriented inverse-dipole lock;
- calibration of a pivot backtrack with the exact Type-T `abba` word;
- reduction to a short path or bounded simple Petersen-cycle core.

### Still open

- graph-safe deletion or replacement of an embedded Type-T backtrack;
- finite complete-profile analysis of the bounded simple-cycle core;
- separator extraction from blocked crossed star routes;
- strict composition of rank-one and rank-two equality defects;
- global well-founded induction and horizontal bookkeeping;
- canonical acceptance, independent audit, Lean verification, manuscript integration;
- the global five-support theorem.
