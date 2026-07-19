# Defect-cover depth and the ideal-pivot theorem

**Programme:** `AffineCDC — Research Lead`  
**Status:** theorem-level structural checkpoint; not canonical pending Director review  
**Parents:** `FIVE_CDC_DEFECT_CORE_QUOTIENT_AND_TWO_LEVEL_ARRANGEMENT_V1.md`, `FIVE_CDC_BAD_LIFT_CONTAINER_DYNAMICS_V1.md`, `FIVE_CDC_SUPPORT_CYCLE_PIVOT_AND_FLOW_RECONFIGURATION_V1.md`

## 1. Purpose

The sharp defect-core theorem says that a noncompressible root lift has unused-root graph `U` satisfying

\[
\tau(U)\le2
\quad\text{or}\quad
U\cong C_5.
\]

This packet asks which of these static cores are genuinely stable under the target-side effect of one support-cycle pivot, temporarily forgetting whether the required release pattern is realizable by a source cycle.

The answer is exact: the only one-pivot traps are the one-star cores `\tau(U)\le1`. Every two-cover core of exact cover number two, and the exceptional pentagon, admits a one-step ideal target escape.

## 2. Ideal target pivot

Let `U` be a graph on the eight support indices. Choose distinct support indices `c,d` and a nonempty leaf set

\[
L\subseteq V(K_8)-\{c,d\}.
\]

Define the **ideal pivot update**

\[
P_{c,d,L}(U)
:=
\left(
U\cup\{cs:s\in L,\ cs\notin U\}
\right)
-
\{ds:s\in L,\ ds\in U\}.
\]

This is the maximal target-side version of a support-cycle pivot `c\to d` on a cycle with leaf set `L`:

- every old `c`-star root absent from `U` is assumed to disappear globally from the used graph and hence becomes unused;
- every old unused `d`-star root on the same leaf set is consumed by the pivot.

A genuine support-cycle pivot has the same form with a possibly smaller released set, according to which old roots occur only on the chosen source cycle.

## 3. Cover-number Lipschitz bound

### Proposition 3.1

For every ideal pivot,

\[
\boxed{
\tau(P_{c,d,L}(U))\le \tau(U)+1.
}
\]

#### Proof

Let `T` be a minimum vertex cover of `U`. Every newly added edge is incident with `c`; deleting edges cannot create a new covering requirement. Hence

\[
T\cup\{c\}
\]

covers the updated graph. ∎

Consequently, a defect graph of cover number zero or one cannot reach the compressible range `\tau\ge3` in one support pivot.

## 4. Exact one-pivot trap theorem

### Theorem 4.1 — ideal-pivot escape dichotomy

Let `U` be a noncompressible unused-root graph on eight support indices. Then the following are equivalent.

1. Every ideal pivot update `P_{c,d,L}(U)` is noncompressible.
2. `\tau(U)\le1`.

Equivalently, among all bad defect cores, the exact one-pivot traps are the empty graph and the subgraphs of a single star.

#### Proof

If `\tau(U)\le1`, then `U` is contained in one star, say with centre `h`. An ideal pivot adds edges from at most one further star, with centre `c`, and deletes some edges. Therefore

\[
P_{c,d,L}(U)
\subseteq
\operatorname{Star}(h)\cup\operatorname{Star}(c),
\]

so its vertex-cover number is at most two. It remains noncompressible.

Conversely, assume `U` is bad but `\tau(U)\ge2`. By the sharp defect-core theorem, either `\tau(U)=2` or `U\cong C_5`.

### Case 1: `\tau(U)=2` and `U` has a matching of size two

Choose two disjoint unused edges

\[
e_1,e_2.
\]

They occupy four support indices. Choose two distinct indices `c,s` among the remaining four. Then

\[
cs\notin U,
\]

because otherwise `e_1,e_2,cs` would already form an unused `3K_2` and `U` would be compressible. Choose `d` distinct from `c,s`. Apply the ideal pivot with leaf set `L={s}`.

The update adds `cs`. It can delete only `ds`, which is not either of the matching edges because `s` is outside their four endpoints. Thus

\[
e_1,e_2,cs
\]

survive as an unused `3K_2`. The updated graph is compressible.

### Case 2: `\tau(U)=2` and `U` has no matching of size two

Then every two edges of `U` intersect. Since `U` has no one-vertex cover, the elementary classification of pairwise-intersecting edges in a simple graph implies

\[
U\cong K_3
\]

with five isolated support indices. Choose distinct isolated indices `c,s,d` and use `L={s}`. The pivot adds the unused edge `cs` and consumes no triangle edge. Hence the updated graph contains

\[
K_3\sqcup K_2
\]

and is compressible.

### Case 3: `U\cong C_5`

There are three isolated support indices. Choose distinct isolated indices `c,s,d` and use `L={s}`. The pivot adds the edge `cs` and removes no pentagon edge. Two disjoint edges of the pentagon together with `cs` form an unused `3K_2`. Hence the updated graph is compressible.

This proves the converse. ∎

## 5. Defect-cover depth

Define the cover deficit

\[
\delta(U):=\max\{0,3-\tau(U)\}.
\]

For every support-cycle pivot,

\[
\delta(U')\ge \delta(U)-1.
\]

Thus `\delta(U)` is a lower bound on the number of pure support-cycle pivots needed to enter the cover-number part of the good locus.

- `\tau(U)=2`: target-side depth one;
- `\tau(U)=1`: target-side depth at least two;
- `\tau(U)=0`: target-side depth at least three;
- `U=C_5`: exceptional parity depth one despite `\tau(U)=3`.

The fixed-Fano orbit obstruction with one unused root has `\tau(U)=1`; therefore no single support-cycle pivot can make its directly transported root lift compressible. This explains, without computation, why the successful five-cycle example required a pivot followed by a nontrivial gauge move in the new fibre.

## 6. What remains source-dependent

The ideal theorem removes target-side ambiguity. Every bad core except a one-star core has an abstract one-step escape. Therefore any failure to realize that escape must come from source-side restrictions:

- the desired old root may have occurrences outside the chosen support cycle and hence fail to be released;
- the needed leaf set may not occur on one connected support component;
- consumed new roots may destroy the selected matching or triangle witness;
- the required support-cycle component may not exist in the current lift.

For one-star cores the obstruction is deeper: even perfect release along one support cycle can add only one further star, leaving a two-cover defect. A proof must combine at least two horizontal releases, or one horizontal move with vertical gauge motion that changes more than one star direction.

This yields a sharper current target.

> **Star-core escape problem.** Starting from a bad lift with `U` contained in one star, prove that some finite sequence of rank-one cycle switches and vertical gauge moves produces unused roots of cover number at least three, unless the source graph admits a decomposition certificate suitable for interface gluing.

The two-apex and pentagon states are secondary realizability problems; the one-star state is the genuine dynamical core.

No statement here proves that every star-core state can be escaped in an actual cubic source graph.