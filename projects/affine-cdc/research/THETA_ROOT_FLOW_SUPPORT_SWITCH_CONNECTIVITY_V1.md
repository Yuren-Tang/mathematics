# All labelled root flows on the theta graph are connected by support-pair switches

## Research Lead bounded-terminal theorem v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`

**Parent:** `BOUNDED_DIRECT_PAIRING_CAP_TERMINAL_V1.md`.

**Status:** exact root-history presentation of the soluble theta terminal. On the two-vertex three-parallel-edge theta graph, every root flow is one ordered root triangle `(ab,ac,bc)`. Support-pair switches replace one support index of the triangle or transpose two edge labels. These moves connect all sixty labelled root flows; the exact switch graph is 9-regular and has diameter three. Thus choosing a different explicit theta root flow never requires an unmodelled recolouring jump.

---

## 1. Root flows on `Theta_3`

Let the three labelled parallel edges be

\[
e_1,e_2,e_3.
\]

A root-valued flow is an ordered triple

\[
(x_1,x_2,x_3)\in R_5^3
\]

with

\[
x_1+x_2+x_3=0.
\]

Three nonzero roots have xor zero exactly when they are the three edges of one support triangle. Hence every flow is

\[
\boxed{
(ab,ac,bc)
}
\]

in some edge order, for one three-element support set `{a,b,c}`.

There are

\[
\binom53\cdot3!=10\cdot6=60
\]

labelled root flows.

---

## 2. Replace one support index

Fix a flow whose unordered root set is

\[
\{ab,ac,bc\}.
\]

Let `d` be a support index outside `{a,b,c}` and use switch direction

\[
h=cd.
\]

The roots `ac,bc` contain exactly one endpoint of `h`, while `ab` contains neither. Therefore

\[
F_c\triangle F_d
\]

on the theta graph is exactly the two-edge cycle formed by the edges carrying `ac,bc`.

Switch it:

\[
ac\mapsto ad,
\qquad
bc\mapsto bd,
\qquad
ab\mapsto ab.
\]

The new unordered triangle is

\[
\boxed{
\{ab,ad,bd\},
}
\]

so one support index `c` has been replaced by `d` without changing the labelled edge carrying `ab`.

### Lemma 2.1

Every edge of the Johnson graph

\[
J(5,3)
\]

on support triples is realised by one ordinary theta support-pair switch.

Since `J(5,3)` has diameter two, any support triple can be changed to any other in at most two switches.

---

## 3. Permute the three edge labels

Within the fixed support triangle `{a,b,c}`, use direction

\[
h=ab.
\]

The roots `ac,bc` are eligible and form one two-edge theta cycle. Switching it gives

\[
ac+ab=bc,
\qquad
bc+ab=ac,
\]

while the `ab` edge is fixed.

Thus the switch transposes the two edge labels `ac,bc`.

Using directions `ab,ac,bc` gives the three transpositions fixing one triangle edge. They generate the full permutation group

\[
S_3.
\]

### Lemma 3.1

For a fixed support triple, every permutation of its three root labels among the three parallel edges is realised by support-pair switches.

---

## 4. Connectivity theorem

### Theorem 4.1 — theta root-flow connectivity

Any labelled root flow on `Theta_3` can be transformed into any other by a finite sequence of ordinary support-pair component switches.

### Proof

First use Lemma 2.1 to change the support triple. Then use Lemma 3.1 to match the edge ordering. ∎

### Sharp finite diameter

Exact enumeration of the sixty flows gives a switch graph with:

\[
\boxed{
60\text{ vertices},
\qquad
\deg=9,
\qquad
\text{connected},
\qquad
\operatorname{diam}=3.
}
\]

Thus at most three switches are required. The structural connectivity proof is controlling; the diameter count is a finite certificate.

---

## 5. Consequence for bounded terminal selection

When a direct cross-matching closure gives `Theta_3`, the inherited theta root flow and any explicitly selected terminal triangle flow are connected by a root-valued history of at most three support switches.

Therefore the terminal step in a successful fixed-order return may be represented inside the same root-history category. It is not an arbitrary discontinuous recolouring.

The same-matching terminal remains a bridge/category exit and requires no return history.

---

## 6. Assurance boundary

### Exact here

- classification of all theta root flows as ordered support triangles;
- support-index replacement by one switch;
- edge-label transpositions by one switch;
- connectivity of all sixty flows;
- exact diameter-three certificate;
- removal of the bounded terminal recolouring jump.

### Not claimed

- root-flow connectivity on general cubic graphs;
- variable-order bubble compression by itself;
- R2.7 closure, cap restoration or global five-support closure;
- PDL reconstruction, audit, Lean, manuscript, curation, release or publication.
