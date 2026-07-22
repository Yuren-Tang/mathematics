# Constant-pivot oriented locks have a canonical root section

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `3f42fa158e67ea6ac35f22c220afeb5189ec1f45`  
**Parents:**

- `projects/affine-cdc/research/ORIENTED_CHANNEL_LOCK_BOUNDARY_CALIBRATION_V1.md`;
- `projects/affine-cdc/research/PETERSEN_PIVOT_RESOLUTION_V1.md`;
- `projects/affine-cdc/research/DDD_ROUTE_ORIENTATION_COVER_V1.md`;
- `projects/affine-cdc/research/TAIT_SURFACE_DDD_ORIENTATION_COMPARISON_V1.md`.

**Status:** exact root-admissible resolution theorem for the constant-pivot base case of an oriented full-channel lock. Along a constant-pivot Petersen/DDD strip, each local transport fixes the pivot sheet and carries the nonpivot endpoint to the next nonpivot endpoint. The nonpivot sheet is exactly the unique choice satisfying every emitted side-root triangle. Since the original dipole cap distinguishes the two blocks of the locked matching, one may choose this sheet globally. Hence every constant-pivot oriented lock has a unique simultaneous root section preserving the complete side-root output word.  
**Not implied:** contraction of a pivot-changing strip, enclosure of the next failed inverse expansion, global induction, canonical acceptance, Lean verification, manuscript readiness, or the global five-support theorem.

---

## 1. Petersen state walk

Let

\[
F_0,F_1,\ldots,F_m
\]

be the Petersen-edge state walk of one enriched co-root strip. Assume it has one constant pivot

\[
s\in R_5.
\]

Thus for each `t` there is a root `d_t` disjoint from `s` such that

\[
\boxed{F_t=\{s,d_t\}.}
\]

Consecutive states are distinct and share `s`. For one transition

\[
F_{t-1}=\{s,x\}
\longrightarrow
F_t=\{s,y\},
\]

let `z` be the emitted side root. The three roots `x,y,z` are the three edges of the complementary triangle on

\[
[5]\setminus s.
\]

Hence

\[
\boxed{x+y+z=0.}
\]

---

## 2. The actual transport transposition

Let

\[
\tau_z
\]

be the support transposition whose two moved support indices are the endpoints of the root `z`.

### Lemma 2.1 — two invariant sheets

For every constant-pivot transition,

\[
\boxed{\tau_z(s)=s,}
\]

and

\[
\boxed{\tau_z(x)=y.}
\]

### Proof

The pivot `s` is disjoint from every root on the complementary triangle, in particular from `z`. Therefore the transposition of the two endpoints of `z` fixes both endpoints of `s` and hence fixes the root `s`.

The roots `x,y,z` are the three edges of one triangle. Transposing the endpoints of `z` exchanges the other two triangle edges, so `x` is sent to `y`. ∎

### Finite certificate

There are ten choices of pivot `s`; each has three Petersen neighbours and six ordered transitions between distinct neighbours. Direct enumeration of all

\[
10\cdot3\cdot2=60
\]

ordered transitions verifies simultaneously:

- `tau_z(s)=s`;
- `tau_z(x)=y`;
- `x+y+z=0`.

There are no exceptional transitions.

---

## 3. Pivot and nonpivot orientation sheets

The DDD atom state

\[
F_t=\{s,d_t\}
\]

has exactly two crossed root resolutions, its two Petersen endpoints.

Choosing one block of the crossed terminal matching therefore gives one of two oriented sheets:

1. the **pivot sheet**, selecting `s` at every state;
2. the **nonpivot sheet**, selecting `d_t` at state `F_t`.

Lemma 2.1 shows that both choices are transported consistently as oriented matching blocks:

\[
s\longmapsto s,
\qquad
 d_{t-1}\longmapsto d_t.
\]

Thus orientation alone gives two possible global sections. Root admissibility distinguishes them.

---

## 4. Local root admissibility selects the nonpivot sheet

At the transition

\[
\{s,x\}\longrightarrow\{s,y\}
\]

with emitted side root `z`, a simultaneous root resolution must choose roots

\[
r^-\in\{s,x\},
\qquad
r^+\in\{s,y\}
\]

satisfying

\[
r^-+r^++z=0.
\]

The Petersen pivot-resolution theorem gives the unique solution

\[
\boxed{r^-=x,
\qquad
r^+=y.}
\]

### Theorem 4.1 — local sheet selection

The pivot sheet is never root-admissible at a genuine transition, whereas the nonpivot sheet is always root-admissible and preserves the actual emitted side root.

### Proof

The pivot choice gives

\[
s+s+z=z\ne0.
\]

The nonpivot choice gives

\[
x+y+z=0.
\]

The mixed choices contain two disjoint roots and produce a co-root rather than the side root `z`. Hence the nonpivot choice is unique. ∎

---

## 5. Global constant-pivot section

### Theorem 5.1 — canonical root section

Every constant-pivot state walk

\[
F_t=\{s,d_t\}
\]

has the unique simultaneous root resolution

\[
\boxed{r_t=d_t.}
\]

This section:

1. is transported consistently along the oriented crossed route;
2. satisfies the root-triangle equation at every turn;
3. preserves every actual emitted side-root label;
4. lies entirely in the complementary rank-two plane
   \[
   W_s\cong\mathbf F_2^2.
   \]

### Proof

Lemma 2.1 transports `d_{t-1}` to `d_t`. Theorem 4.1 proves that this transported section is the unique root-admissible local choice at every transition. Compatibility on overlapping transitions gives one global section. The roots `d_t` and every side root belong to the complementary triangle of `s`, hence to `W_s`. ∎

### Closed-return case

If

\[
F_m=F_0,
\]

then `d_m=d_0`, so the nonpivot section returns to itself. A constant-pivot closed return has no residual orientation or affine holonomy after choosing the root-admissible sheet.

---

## 6. Why the cap orientation is sufficient

In a general unoriented DDD strip, choosing the correct crossed-route sheet may fail to descend around a loop. In an inverse-dipole full lock, the original two cap vertices distinguish the two blocks of the locked matching.

The cap therefore supplies a global orientation of the route. The choice of which oriented block is called positive is auxiliary; exchanging the two names does not change the unordered boundary matching. Choose the positive block at the first state to be the nonpivot endpoint `d_0`.

Lemma 2.1 then forces the positive block at every later state to be `d_t`.

### Corollary 6.1 — root-admissible use of the cap orientation

For a constant-pivot oriented inverse-dipole lock, the cap orientation can always be chosen to coincide with the nonpivot sheet. The complete strip then resolves root-valuedly without changing:

- the ordered four-port matching;
- any emitted side-root edge;
- the external incidence order.

Thus constant-pivot composition is not an additional obstruction.

### Trust note

This conclusion uses the freedom to orient an already fixed unordered matching. It does not change the physical route or exchange the two cap shores. It merely chooses which of the two existing route blocks is used as the affine/root section.

---

## 7. Pivot changes are the only remaining local failures

Let the pivot word be partitioned into maximal constant runs. Theorem 5.1 resolves each run uniquely.

At a pivot change

\[
s\ne t,
\]

the shared DDD state is

\[
F=\{s,t\}.
\]

The run on the left forces resolution `t`, while the run on the right forces resolution `s`. These are the two opposite crossed resolutions of the same one-co-root atom.

### Theorem 7.1 — reduction to switch states

A holonomy-free oriented full-channel lock is root-resolvable unless its pivot skeleton contains a pivot change.

Equivalently, after resolving every constant-pivot run, the complete remaining obstruction is supported on the finite set of DDD switch states

\[
\boxed{F=\{s,t\}}
\]

at which adjacent runs demand opposite resolutions.

There is no unresolved serial or constant-pivot branch.

---

## 8. Revised final local theorem

The oriented-lock descent target now reduces to one statement.

### Target 8.1 — pivot-change enclosure

For a support-minimal oriented full-channel lock containing a pivot change state `F={s,t}`, prove one of:

1. one crossed resolution is admitted and the original inverse dipole lifts;
2. an external attachment distinguishes the two resolutions and gives profile escape;
3. the switch state lies behind a two-, three-, or four-edge separator;
4. peeling the adjacent rank-two runs creates a strictly smaller oriented full-channel lock centred at `F`;
5. `F` is a bounded one-co-root DDD cell admitting the explicit parallel/crossed orientation switch.

The only unproved descent datum is the enclosure in alternative 4. All constant-pivot runs on either side are now exact root-valued objects and may be treated as rank-two Tait carriers rather than unresolved co-root strips.

---

## 9. Consequence for the global frontier

The local composition frontier has passed through the reductions

\[
\text{equality/DDD}
\longrightarrow
\text{oriented full-channel lock}
\longrightarrow
\text{pivot-change DDD switch state}.
\]

Thus the final unbounded datum is no longer:

- a six-channel word;
- a four-channel word;
- a constant-pivot strip;
- an orientation bit;
- or a Type-T/Type-H boundary automaton.

It is only the graph-incidence enclosure of finitely many pivot-change atoms after their adjoining rank-two runs have been resolved.

---

## 10. Trust boundary

### Exact here

- `tau_z` fixes the pivot and maps one nonpivot endpoint to the next;
- the pivot and nonpivot oriented sheets;
- unique local root admissibility of the nonpivot sheet;
- unique global root section on every constant-pivot run;
- preservation of the complete emitted side-root word;
- compatibility of the cap-supplied block orientation with the nonpivot section;
- elimination of constant-pivot strips as residual local obstructions;
- reduction of the remaining lock to pivot-change DDD switch states.

### Still open

- composition-safe resolution or strict enclosure descent at every pivot change;
- proof that repeated switch states cannot retain unbounded attached semantics;
- one global well-founded induction combining graph reduction and horizontal rescue;
- canonical acceptance, independent audit, Lean verification, manuscript integration;
- the global five-support theorem.
