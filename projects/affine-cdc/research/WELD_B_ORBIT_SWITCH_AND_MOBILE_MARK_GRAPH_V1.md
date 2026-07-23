# Intersecting weld pairs are switch-stable exactly without marked-route separation

## Research Lead finite-state dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `a3c0f50f587b81bc0ac5e974a50f91bb4897be12`.

**Parents:**

- `MARKED_WELD_RELATIVE_CONTEXTUAL_RETURN_TARGET_V1.md`;
- `MARKED_WELD_PACHNER_OVERLAP_SCOPE_V1.md`;
- the support-pair/Kempe switching rules;
- the root-valued Pachner flip table.

**Status:** exact weakening and finite obstruction theorem. An inverse equal-face weld does not require preservation of the original support names `z,w`; it requires only that the two reconnecting-edge roots remain distinct and intersecting. This `B` relation is preserved by every support-pair switch which affects both marked edges or neither, and is destroyed by every eligible switch which affects exactly one. Allowing active central Pachner crossings gives a connected cyclic sixty-state mobile-mark graph, so no coefficient-only local rank exists. The shortest viable repair remains a source-level side-enclosure theorem preventing active-diagonal and separating-channel crossings of the canonical weld.

---

## 1. The minimal inverse-weld requirement

Let the two reconnecting edges after an equal-face cancellation carry roots

\[
p,q\in R_5.
\]

Inverse insertion of two equal root triangles is possible exactly when

\[
\boxed{p\ne q,\qquad |p\cap q|=1.}
\]

Then

\[
r=p+q\in R_5
\]

and both inserted vertices carry the root triangle

\[
(p,q,r).
\]

Thus exact preservation of a word `(z,z,w,w)` is sufficient but stronger than necessary. The true coefficient target is preservation of the support-unordered boundary orbit

\[
\boxed{B=\text{distinct intersecting pair}.}
\]

---

## 2. One support-pair switch

Let

\[
h=ab
\]

be one support-pair switch. A root `p` is eligible for the `h` channel precisely when

\[
|p\cap h|=1,
\]

and switching its component changes its root to

\[
p\longmapsto p+h=p\triangle h.
\]

Fix an ordered `B` pair `(p,q)` and assume both roots are eligible for the same channel `h`.

### Theorem 2.1 — simultaneous-switch stability

If the switch affects both marked edges or neither, the returned pair is again distinct and intersecting.

\[
\boxed{
(p,q)\in B
\Longrightarrow
(p+h,q+h)\in B.
}
\]

### Proof

Each root contains exactly one of the two support indices of `h`. Switching exchanges those two indices. If `p,q` share the same selected index, their images share the other. If they select opposite indices, their common support lies outside `h` and remains unchanged. Equality cannot be created because symmetric difference by the same `h` is injective. ∎

### Theorem 2.2 — one-sided switch leaves `B`

If exactly one of the two marked edges is switched, the resulting pair is never distinct intersecting. It is either equal or disjoint.

The exhaustive ordered count is:

\[
\boxed{
\begin{array}{c|c}
\text{one-sided outcome}&\text{count}\
\hline
\text{disjoint}&240\\
\text{equal}&120\\
\text{intersecting}&0.
\end{array}}
\]

The count ranges over both choices of the switched side in all 180 eligible ordered triples `(p,q;h)`.

### Corollary 2.3 — first marked-route separation

Starting from a weld-admissible `B` pair, failure of weld admissibility under support-pair switching occurs exactly when one channel component contains one marked edge but not the other.

Thus:

\[
\boxed{
\text{inverse-weld failure}
\Longleftrightarrow
\text{marked-route separation}.}
\]

The equal outcome gives the zero/quadruple-equality insertion row; the disjoint outcome gives the co-root/doubled-disjoint row.

---

## 3. Mobile central-diagonal states

If one marked edge becomes the active central edge of a root-valued Pachner flip, its root moves to a disjoint root. Allow this as a mobile mark rather than requiring pointwise preservation.

A weld-admissible mobile state is an ordered pair

\[
(p,q)
\]

of distinct intersecting roots. There are

\[
\boxed{60}
\]

such states.

A mobile central move changes exactly one coordinate to a disjoint root while retaining the `B` relation with the other coordinate.

### Oriented two-path model

Write

\[
p=ab,
\qquad
q=ac
\]

with common support `a`. Identify the ordered pair with the oriented two-path

\[
\boxed{b-a-c}
\]

in `K_5`.

A legal mobile move changes one endpoint diagonal and shifts the shared support to one end of the path. For example,

\[
(b-a-c)\longmapsto(d-c-a),
\qquad
d\notin\{a,b,c\},
\]

or the symmetric move at the other coordinate.

---

## 4. Exact mobile graph certificate

Let `M_B` be the graph of the sixty ordered `B` states with one-coordinate mobile central moves.

Exact enumeration gives:

\[
\boxed{
|V(M_B)|=60,
\qquad
|E(M_B)|=120.
}
\]

Moreover:

\[
\boxed{
M_B\text{ is connected and }4\text{-regular},
\qquad
\operatorname{diam}(M_B)=5.
}
\]

Its short simple-cycle census begins:

\[
\boxed{
\#C_4=30,
\qquad
\#C_6=20,
\qquad
\#C_7=240.
}
\]

It has no triangles or pentagons, but it is not bipartite because of the seven-cycles.

### Consequence 4.1

There is no strictly monotone scalar rank depending only on the ordered mobile root pair and decreasing along every allowed central move.

A mobile-envelope return theorem therefore needs additional data:

- source incidence and enclosure;
- cap/route orientation;
- causal history position;
- or an independently proved macro rank.

The `B` coefficient state alone does not simplify the recurrence.

---

## 5. Revised repair hierarchy

### First priority — side-enclosed `B` return

For the actual `C6/C8` canonical weld, prove throughout the remaining return history:

1. neither reconnecting edge becomes an active central diagonal;
2. every support-pair switch affects both marked edges or neither.

Then the edges remain topologically fixed and Theorem 2.1 preserves weld admissibility, even if their support names change simultaneously.

### Second priority — first-separation localisation

If a support-pair channel first separates the two marked edges, record that exact move. The inverse-weld obstruction is immediately one known zero/co-root atom. A repair may be possible if the first-separation position gives a strictly shorter causal prefix.

### Last priority — full mobile-envelope return

Only if active central overlaps cannot be excluded should the sixty-state mobile graph be added to the contextual state. Because `M_B` is connected and cyclic, this route requires new source-level control and is not a finite coefficient shortcut.

---

## 6. Exact next theorem

### Target 6.1 — canonical weld enclosure or first separation

For the two reconnecting edges created by one canonical `C6/C8` cancellation, trace the remaining return history until the first move which is not disjoint/exterior and not a simultaneous switch. Prove one of:

1. no such move occurs, so inverse weld succeeds after relative return;
2. the first support-pair separation gives a shorter-prefix zero/co-root atom;
3. the first active-diagonal crossing gives a shorter causal interval or immediate route/category exit.

This theorem is strictly weaker than arbitrary pointwise `MWR` and retains the exact local failure grammar.

---

## 7. Trust boundary

### Exact here

- `B` as the minimal coefficient condition for inverse weld;
- simultaneous/none support-pair switch preservation of `B`;
- one-sided switch outcomes `A` or `C`, never `B`;
- exact one-sided outcome counts;
- identification of inverse-weld failure with marked-route separation;
- the sixty-state ordered mobile-mark graph;
- its size, regularity, connectivity, diameter and short-cycle census;
- absence of a coefficient-only monotone mobile rank.

### Not proved

- canonical-weld side enclosure;
- shorter-prefix disposition of the first marked-route separation;
- mobile-envelope source realization;
- repaired cancellation macro-return;
- R2 global return, cap restoration, or global five-support closure;
- independent audit, curation, Lean verification, manuscript integration, release, arXiv, DOI, peer review, or publication.
