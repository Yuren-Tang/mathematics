# Physical commutation eliminates the Type-T four-pole kernel

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `866e4465b0be6d2240fb25a6453edf4bd6f06323`  
**Parents:**

- `projects/affine-cdc/five-support/cuts-four-poles-and-routing.md`;
- `projects/affine-cdc/research/FOUR_POLE_CAP_LIBRARY_TEN_STATE_PROFILES_V1.md`;
- `projects/affine-cdc/research/TYPE_T_KERNEL_SQUARE_ENVELOPE_V1.md`;
- `projects/affine-cdc/research/PETERSEN_BACKTRACK_TYPE_T_CORE_V1.md`;
- `projects/affine-cdc/research/SHIFT_MATCHING_BANDS_ROUTE_TAIT_PEELING_V1.md`.

**Status:** exact physical elimination of the abstract Type-T `P_5 | P_5` four-pole mismatch kernel. The abstract deterministic routing table permits the route word `abba`, but one of its two disjoint support-pair challenges is unchanged by the first switch. Its physical terminal matching therefore cannot change from `a` to `b`. The unchanged matching forces an immediate boundary-profile escape. Hence no physical four-pole profile can realise the Type-T kernel as a closed residual mismatch mechanism.  
**Not implied:** deletion of every local coefficient-side `abba` unit, automatic contraction of an arbitrary Petersen backtrack, elimination of the Type-H/DDD kernel, canonical acceptance, Lean verification, manuscript readiness, or the global five-support theorem.

---

## 1. Indexed boundary traces and physical routes

Let `P` be a cubic four-pole with ordered terminals

\[
1,2,3,4.
\]

An indexed five-support cover is written

\[
\mathcal F=(F_1,F_2,F_3,F_4,F_5).
\]

For each support index `r`, let

\[
S_r\subseteq\{1,2,3,4\}
\]

be its even boundary trace.

A complementary support-pair challenge is a pair `r,s` with

\[
S_r\triangle S_s=\{1,2,3,4\}.
\]

Its symmetric-difference subgraph is

\[
X_{rs}=F_r\triangle F_s.
\]

At every internal cubic vertex, `X_{rs}` has degree zero or two. Its boundary-connected components are therefore two terminal paths and determine one perfect matching

\[
M_P(r,s)
\]

of the four terminals.

Switching one of the two boundary paths exchanges that path between `F_r` and `F_s`. At the boundary it toggles one block of the matching `M_P(r,s)` in both traces.

---

## 2. The missing physical law in the abstract closure game

### Lemma 2.1 — disjoint-support route invariance

Let `{r,s}` and `{u,v}` be disjoint support-index pairs. Perform any Kempe switch using only supports `r,s`. Then

\[
\boxed{
F_u\triangle F_v
\text{ is unchanged.}
}
\]

Consequently, whenever `{u,v}` remains a full four-terminal challenge,

\[
\boxed{
M_P(u,v)
\text{ is unchanged.}
}
\]

### Proof

A switch on `{r,s}` changes only `F_r` and `F_s`. Since

\[
\{r,s\}\cap\{u,v\}=\varnothing,
\]

both `F_u` and `F_v` remain literally unchanged. Hence so do their symmetric difference and its two terminal-path components. ∎

### Significance

The ten-state abstract routing game records:

1. the current support-unordered boundary state;
2. one complementary support-pair challenge;
3. a chosen routing matching.

It does not, by itself, require route choices for two disjoint challenges to be compatible under switches that leave one challenge subgraph unchanged.

Lemma 2.1 is the first composition law that couples two rows of the abstract automaton through one physical indexed cover.

---

## 3. Canonical Type-T kernel

The exact finite routing classification leaves, up to terminal-matching permutation and exchange of shores, one Type-T kernel pair

\[
P_5\mid P_5.
\]

Choose the standard `A`-containing shore

\[
\boxed{
\mathcal P
=
\{A,B_0,C_1,D_0,D_1\}.
}
\]

Its deterministic policy graph is the path

\[
\boxed{
A
\xleftrightarrow{M_0}
B_0
\xleftrightarrow{M_2}
D_1
\xleftrightarrow{M_2}
D_0
\xleftrightarrow{M_0}
C_1.
}
\]

Thus its route-colour word is

\[
\boxed{M_0,M_2,M_2,M_0,}
\]

the abstract Type-T word `abba`.

Only the first two edges of this path are needed below.

The exact challenge rows are:

\[
\begin{array}{c|ccc}
\text{state and challenge}&M_0&M_1&M_2\\
\hline
A\text{, full/empty}&B_0&B_1&B_2\\
B_0\text{, full/empty}&C_0&D_2&D_1.
\end{array}
\]

Inside `\mathcal P`, the first row has the unique safe route `M_0`, while the second has the unique safe route `M_2`.

---

## 4. Two disjoint challenges in the `A` state

Choose an indexed representative of `A` with traces

\[
(S_1,S_2,S_3,S_4,S_5)
=
(F,F,0,0,0),
\]

where

\[
F=\{1,2,3,4\}.
\]

Consider the two disjoint full/empty challenges

\[
\{1,3\},
\qquad
\{2,4\}.
\]

They use four distinct support indices.

Assume that a physical profile is trapped in the Type-T shore `\mathcal P`.

At state `A`, every full/empty challenge must use route `M_0`, because the other two routes produce `B_1` or `B_2`, neither of which belongs to `\mathcal P`.

Switch the first challenge `{1,3}` along one `M_0` path. The resulting support-unordered state is

\[
B_0.
\]

The supports `F_2,F_4` were not changed. Therefore

\[
F_2\triangle F_4
\]

and its physical route remain exactly what they were at `A`.

Hence the second challenge `{2,4}` still has route

\[
M_0.
\]

But at `B_0`, the full/empty challenge row is

\[
M_0\mapsto C_0,
\qquad
M_1\mapsto D_2,
\qquad
M_2\mapsto D_1.
\]

Therefore switching the unchanged second challenge produces

\[
\boxed{C_0.}
\]

Since

\[
C_0\notin\mathcal P,
\]

the profile escapes immediately.

---

## 5. Main theorem

### Theorem 5.1 — Type-T physical inconsistency

No physical four-pole boundary profile can realise the `A`-containing Type-T `P_5` policy as a Kempe-closed residual profile.

More precisely, every indexed cover in state `A` whose first disjoint full/empty challenge switches to the Type-T neighbour `B_i` forces, through a second untouched full/empty challenge, the state `C_i` outside the Type-T path.

### Proof

The canonical proof above gives `i=0`. The other two cases follow by permuting the three terminal matchings. ∎

### Corollary 5.2 — elimination of the Type-T kernel pair

Every abstract Type-T mismatch kernel pair has, after symmetry and exchange of shores, one `A`-containing `P_5` shore of the form treated in Theorem 5.1.

Hence

\[
\boxed{
\text{no physical disjoint cap-forced Kempe-closed profile pair has Type T.}
}
\]

The abstract `P_5\mid P_5` kernel is a finite routing artefact caused by omitting disjoint-support route invariance.

---

## 6. Relation to the `abba` square and Petersen backtracks

The route word

\[
M_0,M_2,M_2,M_0
\]

has the same palindromic `abba` shape as:

1. the disjoint doubled-root boundary word carried by the four-cycle square;
2. a Petersen pivot backtrack and its forced root-resolution word.

The present theorem does not identify these three objects by notation alone.

Its exact content is narrower and stronger at the four-pole profile level:

- the Type-T deterministic routing path requires one untouched support-pair route to change;
- physical indexed covers forbid that change;
- therefore the profile escapes before any graph contraction is needed.

The square remains a useful bounded completion carrier for the `(0,4,4)` root orbit. It is not needed to eliminate the abstract Type-T mismatch kernel.

Local Petersen backtracks may still occur inside a larger Type-H/DDD strip. Their graph-side cancellation remains a separate bounded composition question.

---

## 7. Consequence for the four-pole frontier

The exact abstract closure classification had two residual dynamical types:

\[
\text{Type T}
\qquad\text{and}\qquad
\text{Type H}.
\]

Theorem 5.1 removes Type T physically.

Therefore the genuine residual four-pole mismatch frontier is

\[
\boxed{
\text{Type H / DDD holonomy only.}
}
\]

Combined with the current side-network reductions:

- complementary Tait components admit coloured-dipole peeling;
- shift-matching bands admit route-Tait peeling;
- low-port residues glue or expose small cuts;
- four-port Tait responses reduce to bounded cap/square/equality/DDD events;
- Type-T profile lock is impossible by physical commutation.

Thus the remaining finite composition burden is concentrated in:

1. zero/equality cells;
2. one-co-root DDD cells and their crossed resolutions;
3. bounded matching flips;
4. Type-H unique-bad-route and orientation-sheet compatibility.

---

## 8. Reproducible finite certificate

Use four-bit terminal masks

\[
F=15,
\qquad
X_0=3,
\qquad
X_2=9.
\]

Start with labelled traces

\[
(15,15,0,0,0).
\]

Toggle supports `1,3` by `X_0`. The state becomes `B_0`.

Supports `2,4` remain exactly

\[
(15,0),
\]

so their symmetric difference remains `15` and their physical route remains `M_0`.

At `B_0`:

\[
M_0\mapsto C_0,
\qquad
M_2\mapsto D_1.
\]

This is the complete finite certificate. The proof of route invariance is graph-theoretic and does not depend on enumeration.

---

## 9. Revised descent bookkeeping

The global descent no longer needs a coordinate for an irreducible Type-T four-pole profile.

A suitable residual local ordering may use

\[
\bigl(
N_T+N_M,
N_{\mathrm{eq}},
N_{\mathrm{DDD}},
N_{\mathrm{flip}},
N_H
\bigr),
\]

where:

- `N_T+N_M` is strictly lowered by Tait and route-Tait dipole peeling;
- equality, DDD, and matching-flip counts record bounded lift failures;
- `N_H` records the remaining Type-H/DDD holonomy carrier.

There is no separate unbounded Type-T profile coordinate.

---

## 10. Trust boundary

### Exact here

- disjoint-support Kempe switches preserve the other pair's symmetric-difference subgraph and route;
- the canonical Type-T `A`-shore profile and its first two exact challenge rows;
- the two-disjoint-challenge contradiction;
- elimination of every physical Type-T `P_5\mid P_5` residual kernel by symmetry;
- reduction of the genuine four-pole mismatch frontier to Type H.

### Still open

- deletion or contraction of an arbitrary local coefficient-side `abba` unit;
- full locked-profile transfer for zero/equality cells;
- full locked-profile transfer for one-co-root DDD cells and matching flips;
- simultaneous `Y`-route / sheet-exchange compatibility in Type H;
- one global theorem ordering graph descent, separator decomposition, and horizontal escape;
- the global five-support theorem;
- canonical acceptance, independent audit, Lean verification, and manuscript status.
