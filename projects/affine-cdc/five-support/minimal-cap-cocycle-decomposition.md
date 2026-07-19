# Minimal two-cap cocycle completions

## 1. Purpose

The bounded touch-residue theorem associates to every nonflat common-cut witness two specified transition elements

$$
R=\{r_p,r_q\}
$$

at the two route-cap vertices `p` and `q` of the canonical route-capped `4`-regular carrier.

The bare residue is not a cocycle of the full transition matroid: every full cocycle meets each vertex triple in even cardinality.  This chapter resolves the next purely matroidal question.

1. Except for an immediate loop degeneration, a full cocycle containing both residue elements always exists.
2. An inclusion-minimal such cocycle is either one cocircuit coupling the two caps or the disjoint union of exactly two cocircuits, one carrying each cap.
3. In an isotropic matroid, the two cocircuits in the second case have disjoint vertex supports.

Thus the global completion branch has an exact mechanism dichotomy:

$$
\boxed{
\text{one coupled cap-to-cap cocircuit}
\quad\text{or}\quad
\text{two disjoint one-cap cocircuits}.
}
$$

The first branch is the only one that can carry an irreducible two-ended obstruction.  The second branch already separates the two terminal residues at the full-matroid level.

## 2. Linear existence of a completion

Let `M` be a binary matroid represented by a matrix `B`, and let `a,b` be two elements with columns `B_a,B_b`.

A cocycle is a row-space vector

$$
yB.
$$

It contains both `a` and `b` exactly when

$$
 y\cdot B_a=1,
 \qquad
 y\cdot B_b=1.
$$

### Proposition 2.1 — two-marker cocycle feasibility

Exactly one of the following occurs.

1. One of `a,b` is a loop.  Then no cocycle contains that element.
2. `B_a=B_b\ne0`.  Then `\{a,b\}` is a two-element circuit, and every row vector evaluating to one on this common column gives a cocycle containing both.
3. `B_a,B_b` are distinct nonzero columns.  Then the two displayed equations are independent and have a simultaneous solution.

#### Proof

Over `\mathbf F_2`, two nonzero one-dimensional linear functionals are dependent exactly when they are equal.  A nonzero functional takes the value one somewhere.  Two distinct nonzero functionals are independent, so the map

$$
y\longmapsto(y\cdot B_a,y\cdot B_b)
$$

is surjective onto `\mathbf F_2^2`. ∎

### Corollary 2.2 — application to the cap residue

If neither selected cap transition is an isotropic loop, there exists a full transition-matroid cocycle containing the two-transition residue.

If one selected transition is a loop, the obstruction is already a one-element circuit at a cap vertex.  In a simple IAS representation, this can occur only for a `\chi` column at an isolated interlacement vertex, hence is an immediate low-connectivity case.

The existence of a completion therefore does not require an additional graph theorem.

## 3. Cocycle decomposition in a binary matroid

Recall that the cocycles of `M` are the cycles of the dual matroid `M^*`.  Consequently every nonzero cocycle is a disjoint union of cocircuits.

Fix two nonloop elements `a,b`.  Call a cocycle `C` **`\{a,b\}`-minimal** if

$$
\{a,b\}\subseteq C
$$

and no proper cocycle subset of `C` contains both `a` and `b`.

### Theorem 3.1 — two-marker minimal-cocycle dichotomy

Let `C` be an `\{a,b\}`-minimal cocycle of a binary matroid.  Exactly one of the following holds.

1. **Coupled case.**  `C` is a cocircuit containing both `a` and `b`.
2. **Separated case.**  There are disjoint cocircuits `D_a,D_b` such that
   $$
   C=D_a\sqcup D_b,
   $$
   with
   $$
   a\in D_a,\quad b\notin D_a,
   \qquad
   b\in D_b,\quad a\notin D_b.
   $$

#### Proof

Decompose `C` into pairwise disjoint cocircuits:

$$
C=D_1\sqcup\cdots\sqcup D_m.
$$

If some `D_i` contains both `a` and `b`, then `D_i` is a cocycle subset of `C` containing both markers.  Minimality gives `D_i=C`, so `C` is one cocircuit.

Assume no component contains both markers.  A component containing neither marker could be removed while leaving a proper cocycle subset containing `a,b`, contradicting minimality.  Hence every component contains exactly one marker.  There are only two markers, so `m=2`; one component contains `a` and the other contains `b`. ∎

This theorem is representation-free and does not use any special property of transition matroids.

## 4. Isotropic vertex-support consequence

Now let

$$
M=M[IAS(G)].
$$

Every cocycle has, at each vertex `v`, coordinate triple

$$
\bigl(y_v,(yA)_v,y_v+(yA)_v\bigr).
$$

Therefore it meets the vertex triple `\tau(v)` in zero or two elements.

For a cocycle `D`, define its vertex support

$$
L(D)=\{v:D\cap\tau(v)\ne\varnothing\}.
$$

### Lemma 4.1 — disjoint cocycles have disjoint vertex supports

If two nonzero cocycles `D_1,D_2` are disjoint as transition sets, then

$$
L(D_1)\cap L(D_2)=\varnothing.
$$

#### Proof

Every nonzero intersection with one vertex triple has size two.  Any two two-element subsets of a three-element set intersect.  Hence two disjoint cocycles cannot both meet the same vertex triple. ∎

### Corollary 4.2 — cap-completion mechanism

Let `C` be a minimal full cocycle completion of the nonflat cap residue `\{r_p,r_q\}`.

Then exactly one of:

1. `C` is a single cocircuit whose vertex support contains both cap vertices `p,q`;
2. `C=D_p\sqcup D_q`, where `D_p,D_q` are cocircuits with disjoint vertex supports, `p\in L(D_p)` and `q\in L(D_q)`.

Thus the separated branch contains no isotropic vertex at which the two one-cap certificates interact.

## 5. Local-set interpretation

For a row coefficient vector `y`, put

$$
S=\operatorname{supp}(y).
$$

The vertex support of the corresponding cocycle is

$$
\boxed{
L(y)=S\cup\operatorname{Odd}_G(S).
}
$$

Hence every cocircuit carrier in Corollary 4.2 is a local set of the interlacement graph.

A caution is essential.  Cocircuit minimality is minimality of the **transition-element support**.  It is not automatically the same as inclusion-minimality of the local vertex set.  At one vertex, the three possible nonzero cocycle pairs are incomparable two-element subsets of the vertex triple, so a cocycle on a smaller local set need not be a subset of a given cocircuit.

Accordingly, the Claudet--Perdrix cut-rank characterization of minimal local sets is relevant to later refinement, but cannot simply be substituted for the cocircuit theorem above.

## 6. Component code of one completion

Let `C=c(y)` be one cocycle, and define

$$
\mathcal K_C
=
\{y':\operatorname{supp}c(y')\subseteq C\}.
$$

This is a binary subspace.  Its nonzero minimal supports are precisely the cocircuit components contained in `C`.

For an `\{r_p,r_q\}`-minimal completion:

- in the coupled case, `\dim\mathcal K_C=1`;
- in the separated case, `\dim\mathcal K_C=2`, generated by the two disjoint one-cap cocircuits.

Thus the coupled/separated dichotomy can be detected by one restricted row-space nullity computation; it does not require enumerating all decompositions.

## 7. Consequences for the proof mechanism

The nonflat route-locked frontier now has four ordered layers.

### Layer 1 — bounded curvature residue

All internal witness transitions cancel, leaving one selected transition at each route cap.

### Layer 2 — immediate local degeneration

A loop, a parallel residue pair, or a cocycle supported only on the two cap triples yields the already classified isolated/twin/pendant low-connectivity configurations.

### Layer 3 — minimal full completion

Outside those local cases, choose an inclusion-minimal full cocycle containing the two residue transitions.  Theorem 3.1 gives:

- two disjoint one-cap cocircuits; or
- one coupled cap-to-cap cocircuit.

### Layer 4 — physical projection

The next graph theorem must prove:

1. the separated branch projects to two independent terminal interfaces, a serial decomposition, or a terminal-even separator in the physical quotient `\Gamma_g`;
2. the coupled branch either produces a proper isotropic split / physical separator, breaks route-lock through an alternate transition, or carries the unique comparison data needed for the DDD support-label class.

Only the coupled branch remains a candidate for a genuinely irreducible two-ended obstruction.

## 8. Finite verification

As a sanity check, exhaustive Wolfram evaluation over all simple graphs of orders `2,3,4`, all pairs of marked vertices, and all nine choices of marked transition types found:

- `9072` support-minimal completions that are single cocircuits;
- `2536` support-minimal completions that split into two disjoint one-marker cocircuits;
- no failures of Theorem 3.1.

The proof is the general binary-matroid argument above; the computation is not an assumption.

## 9. Reliability boundary

Proved here:

- exact linear feasibility of a two-transition full cocycle completion;
- loop and parallel degenerations;
- the general two-marker minimal-cocycle dichotomy;
- disjointness of isotropic vertex supports in the separated branch;
- the local-set and restricted-nullity formulations.

Not proved here:

- a physical separator from two disjoint one-cap cocircuits;
- a split theorem for a coupled cocircuit;
- comparison of the coupled branch with the DDD support-label cocycle;
- the global five-support theorem.

No Lean, independent-review, peer-review, publication, release, arXiv, DOI, or merge status is implied.
