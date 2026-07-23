# Equality and DDD carriers share one discrete-Morse termination theorem

## Research Lead mechanism compression v1.1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Original parent head:** `4e51227611a0cb9cecdacf41021ad88c62207dc6`.  
**v1.1 sharpening:** equality needs coefficient `1`, not the conservative coefficient `7`.

**Parents:**

- `EQUALITY_LOCK_GLOBAL_PACHNER_POTENTIAL_V1.md`;
- `DDD_LOCK_GLOBAL_PACHNER_POTENTIAL_V1.md`;
- `ROOT_FLOW_TRIANGLE_COMPLEX_PACHNER_V1.md`.

**Purpose:** replace the appearance of two different global termination theories by one positive additive triangle-Morse theorem with two singular-boundary orbit certificates.

**Status:** exact authorial scalarisation and architectural unification of the existing potential theorems. The finite flip tables and no-local-minimum arguments remain substantive inputs to be reconstructed by PDL.

---

## 1. Root triangle source language

The ten cubic root states are the support triangles

\[
\binom{[5]}3.
\]

At a vertex of type `ijk`, the incident roots are

\[
ij,ik,jk.
\]

Two equal adjacent triangles admit equal-face `2--0` cancellation. Two distinct adjacent triangles lie in one four-support tetrahedron and admit the unique nontrivial root-valued `2--2` flip.

There are exactly two singular inverse-cap boundary orbits.

### Type Z — equality

After support permutation, the boundary is

\[
12,12,12,12.
\]

### Type D — DDD/co-root

After support permutation, the boundary is

\[
12,12,34,34.
\]

The two boundary types are the zero and nonzero singular fibres of root triality.

---

## 2. Equality scalarisation

For the equality boundary `12^4`, the existing primary visibility is

\[
\nu(T)=
\begin{cases}
3,&12\subset T,\\
0,&T=345,\\
2,&\text{otherwise}.
\end{cases}
\]

The existing tie-breaker is

\[
\phi(124)=1,
\qquad
\phi(125)=3,
\qquad
\phi(T)=0\text{ otherwise}.
\]

The old potential is lexicographic in

\[
(E,\Phi,|V|),
\]

where

\[
E=\sum_v\nu(\Delta_v),
\qquad
\Phi=\sum_v\phi(\Delta_v).
\]

The exact thirty-pair flip census has the stronger property:

\[
\boxed{
\Delta E<0
\Longrightarrow
\Delta\Phi\le0
}
\]

for every flip oriented to the lexicographically lower side. The secondary function `Phi` is used only on the `E`-neutral involutions.

Define the positive triangle weight

\[
\boxed{
w_Z(T)=\nu(T)+\phi(T)+1.
}
\]

Its complete table is

\[
\boxed{
\begin{array}{c|cccccccccc}
T&123&124&125&134&135&145&234&235&245&345\\
\hline
w_Z(T)&4&5&7&3&3&3&3&3&3&1.
\end{array}}
\]

For a root-labelled equality carrier `R`, put

\[
\boxed{
\mathcal M_Z(R)=\sum_{v\in V(R)}w_Z(\Delta_v).
}
\]

### Lemma 2.1 — every equality-selected flip lowers `M_Z`

If a selected flip lowers `E`, then it does not increase `Phi`, so

\[
\Delta\mathcal M_Z
=
\Delta E+\Delta\Phi<0.
\]

If the flip is `E`-neutral, it is oriented precisely to lower `Phi`, and again

\[
\Delta\mathcal M_Z<0.
\]

The constant `+1` cancels across every `2--2` flip and does not affect its orientation.

### Lemma 2.2 — every equality cancellation lowers `M_Z`

Equal-face cancellation removes two vertices of the same positive weight. Therefore

\[
\Delta\mathcal M_Z=-2w_Z(T)<0.
\]

This includes the complementary triangle `345`, whose old `(E,Phi)` contribution was zero:

\[
w_Z(345)=1.
\]

Thus all three old coordinates are absorbed into one positive scalar potential.

---

## 3. DDD scalarisation

For the DDD boundary `12,12,34,34`, the existing triangle weight is

\[
\omega:
\binom{[5]}3\to\mathbf Z_{\ge0}
\]

with table

\[
\begin{array}{c|cccccccccc}
T&123&124&125&134&135&145&234&235&245&345\\
\hline
\omega(T)&3&0&1&3&0&1&1&3&3&3.
\end{array}
\]

Define the positive weight

\[
\boxed{
w_D(T)=\omega(T)+1.
}
\]

Thus

\[
\boxed{
\begin{array}{c|cccccccccc}
T&123&124&125&134&135&145&234&235&245&345\\
\hline
w_D(T)&4&1&2&4&1&2&2&4&4&4.
\end{array}}
\]

For a DDD carrier `R`, put

\[
\boxed{
\mathcal M_D(R)=\sum_{v\in V(R)}w_D(\Delta_v).
}
\]

### Lemma 3.1 — DDD flips and cancellations lower `M_D`

A selected DDD flip strictly lowers the old sum

\[
\Omega=\sum_v\omega(\Delta_v)
\]

while preserving vertex number. It therefore strictly lowers `M_D`.

An equal-face cancellation removes two vertices of positive weight and hence strictly lowers `M_D`, including triangle types with `omega=0`.

The old lexicographic pair `(Omega,|V|)` is therefore one positive scalar potential.

---

## 4. Two-orbit singular Morse theorem

Let

\[
\sigma\in\{Z,D\}
\]

be the singular boundary orbit. Transport the normalised table `w_sigma` by a support permutation to the actual boundary labels.

### Theorem 4.1 — singular carrier discrete-Morse descent

Let `R` be a nonempty connected root-labelled cubic four-pole with boundary of singular type `sigma`.

Then `R` contains at least one of:

1. an equal adjacent triangle pair, giving a `2--0` cancellation that strictly lowers
   \[
   \mathcal M_\sigma;
   \]
2. a distinct adjacent triangle pair whose root `2--2` flip strictly lowers
   \[
   \mathcal M_\sigma.
   \]

Consequently every adaptively chosen sequence of these decreasing root surgeries is finite.

### Proof

For `sigma=Z`, the exact equality nondecreasing-adjacency table proves that no nonempty carrier can avoid both an equal pair and a flip decreasing `(E,Phi)`. Lemmas 2.1--2.2 replace that lexicographic order by `M_Z`.

For `sigma=D`, the exact DDD `15/15` flip table and its boundary elimination proof give the corresponding result, and Lemma 3.1 replaces `(Omega,|V|)` by `M_D`. ∎

---

## 5. Conceptual interpretation

The termination theorem depends only on:

1. one of the two singular boundary orbits of `O^-(4,2)`;
2. the ten root triangles;
3. the fifteen tetrahedral flip involutions;
4. one positive discrete-Morse weight table for that orbit.

Equality and DDD are therefore not two global theories. They are two finite certificates for one theorem schema:

\[
\boxed{
\text{nonempty singular root carrier}
\Longrightarrow
\text{strict root surgery}.
}
\]

The distinction between them survives only in the local weight table and boundary normalisation.

---

## 6. Architectural consequence

The singular-confluence package should consume one theorem:

> **Singular carrier termination theorem.** Every nonempty equality or DDD carrier admits a root-valued `2--2` move or equal-face `2--0` cancellation decreasing a positive additive triangle Morse function.

The proof needs only two finite-certificate subsections:

- Type Z table `w_Z`;
- Type D table `w_D`.

There should not be separate equality and DDD global termination chapters.

---

## 7. Limits of the unification

The two weight tables have not yet been derived from one closed invariant formula in the singular vector and cap orientation.

The zero singular vector and the five nonzero singular vectors form different symmetry orbits, so two normalised tables are not intrinsically unnatural.

A stronger future theorem may construct one compact singular-triality complex and one generic Morse function whose restrictions are `w_Z,w_D`. That is not needed for the present compression and is not claimed.

---

## 8. PDL obligations

PDL should verify:

1. the complete `30`-pair equality flip census;
2. the equality no-local-minimum boundary elimination;
3. the sharpened finite fact
   \[
   \Delta E<0\Rightarrow\Delta\Phi\le0;
   \]
4. the scalar equality table `w_Z`;
5. the complete `30`-pair DDD flip census;
6. the DDD no-local-minimum boundary elimination;
7. positivity and support-permutation covariance of both tables;
8. strict decrease under every cancellation.

The resulting theorem supplies the termination hypothesis of singular contextual confluence.

---

## 9. Trust boundary

### Exact authorial addition

- equality lexicographic potential scalarises to `M_Z` with coefficient `1`;
- DDD lexicographic potential scalarises to `M_D`;
- both are instances of one positive additive triangle-Morse theorem.

### Not added

- independent verification of either finite flip census;
- a universal closed formula for both tables;
- contextual transfer, cap restoration, global five-CDC acceptance, Lean verification, manuscript, release, or publication status.
