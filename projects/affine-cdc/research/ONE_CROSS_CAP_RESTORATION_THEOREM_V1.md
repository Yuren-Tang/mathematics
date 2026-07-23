# One smaller cross flow restores the original cubic cap

## Research Lead inductive theorem v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `adf67f984eae48c4f960b75ddb1db46b96d31d58`.

**Parents:**

- `ONE_CROSS_SINGULAR_FIXED_ROUTE_REDUCTION_V1.md`;
- equality and DDD current-flow termination potentials;
- `SINGULAR_ROOT_TRIALITY_CONFLUENCE_MASTER_THEOREM_V1.md`;
- route-change and direct-pairing terminal normalisation;
- root-surgery automatic category safety.

**Purpose:** replace the repaired all-three full-channel theorem by the exact inductive statement needed by the global proof. One lower-order cross reconnection root flow suffices to restore the deleted simple edge.

**Status:** complete compressed authorial theorem, conditional on the concrete singular-confluence hypotheses already claimed on the research branch. This theorem does not add downstream assurance.

---

## 1. Inductive setup

Fix a target vertex order `N`. Assume:

> every connected loopless bridgeless cubic multigraph with fewer than `N` vertices has a root-valued `E_5` flow.

Let `P` be an ordered four-pole obtained by deleting the endpoints of one simple edge from a connected loopless bridgeless cubic graph `G` with

\[
|V(G)|=N.
\]

Let `cap_i` be the original two-vertex cap, so

\[
G=P\cup cap_i.
\]

Let `E_j` be one cross zero-vertex reconnection, `j ne i`, and assume

\[
G_j=P\cup E_j
\]

is connected, loopless, bridgeless, cubic, and has `N-2` vertices.

By the induction hypothesis, `G_j` has a root-valued flow.

We prove that `G` has a root-valued flow.

---

## 2. Boundary trichotomy from the selected cross flow

Let the two cross reconnection edges carry roots

\[
p,q\in R_5.
\]

The boundary state of `P` lies in

\[
J_j=\{A,B_j,C_j\}.
\]

Equivalently, exactly one of:

1. `p=q`, giving state `A`;
2. `p,q` are distinct intersecting roots, giving state `B_j`;
3. `p,q` are disjoint roots, giving state `C_j`.

### Root case

Since

\[
B_j\in K_i=\Sigma(cap_i),
\]

the `B_j` state is cap-compatible. Align the labelled support traces by one global `S_5` permutation and glue. The theorem follows.

Assume henceforth that the selected state is `A` or `C_j`.

---

## 3. Cap blocking and fixed route

If `P` has any root boundary state in `K_i`, the original cap glues and the theorem follows.

Assume for contradiction

\[
\Sigma(P)\cap K_i=\varnothing.
\]

Apply `ONE_CROSS_SINGULAR_FIXED_ROUTE_REDUCTION_V1.md`.

### Equality

If the selected state is `A`, then either:

1. one separating equality Kempe component changes exactly one marked root and gives an immediate cap-compatible root insertion; or
2. every relevant channel is locked and the current flow lies in the fixed-route equality outer orbit
   \[
   J_i=A-B_i-C_i,
   \]
   with physical route `M_i`.

### DDD

If the selected state is `C_j`, then either:

1. one separating crossed DDD component repairs the insertion; or
2. every relevant channel is locked and the current flow lies in the fixed-route DDD outer orbit
   \[
   L_i=C_j-D_i-C_k,
   \]
   with physical route `M_i`.

The separating branches glue the cap immediately. Thus only the two oriented full-channel locks remain.

---

## 4. Finite forward histories

### Equality history

The equality boundary is

\[
r,r,r,r.
\]

The equality potential

\[
(E,\Phi,|V|)
\]

produces a finite sequence of root Pachner flips and equal-face cancellations. Every nonempty current carrier has a strictly lowering move or a route event.

### DDD history

The DDD boundary is

\[
p,p,q,q,
\qquad p\cap q=\varnothing.
\]

The DDD potential

\[
(\Omega,|V|)
\]

produces the analogous finite history. No positive-vertex generic bounded residual survives.

Root-valued NNI moves are automatically connected and bridgeless. Equal-face cancellation gives componentwise bridgeless lower-order contexts. Therefore no extra category branch is present.

---

## 5. Terminal alphabet

Every finite forward history reaches one of the following.

### Route-changing terminal

Before the first route change, the ordered boundary state stays on the selected outer orbit and the route is `M_i`.

If the physical route changes to `M_j` or `M_k`, the exact route row gives a boundary state in

\[
K_i
\]

on the current descendant. This is a cap-compatible terminal state for inverse transfer.

### Direct-pairing terminal

If all source vertices disappear, the four-pole is one direct matching.

- A cross matching closes with `cap_i` to the root-soluble theta graph.
- The same matching first gives two loops joined by a zero edge; one crossed `(0,2,2)` root resolution converts it to the same theta terminal.

Thus every direct terminal is cap-compatible.

### Strict cancellation

Any genuine equal-face cancellation lowers target order by two and enters the outer induction hypothesis.

There is no fourth terminal type.

---

## 6. Cover-independent return

The root flow available on a terminal descendant is arbitrary and need not be the current flow used to construct the forward history.

Apply `SINGULAR_ROOT_TRIALITY_CONFLUENCE_MASTER_THEOREM_V1.md`.

At first failed inverse transfer:

1. exactly one zero/co-root token appears;
2. zero is immediately rootified;
3. co-root critical overlaps transport one token without branching;
4. constant-pivot runs have their unique full-state root section;
5. a recurrent token has a simple Petersen core;
6. odd `C5,C9` cannot preserve the oriented cap sheet;
7. even `C6` has the relative canonical-star cancellation movie;
8. `C8` reduces to two seam-compatible `C6` cells.

The lexicographic induction parameter is

\[
(	ext{target order},	ext{remaining history length}).
\]

Therefore every cap-compatible terminal returns to a state in `K_i` on the original four-pole `P`.

This contradicts the cap-blocking assumption.

---

## 7. One-cross cap restoration theorem

### Theorem 7.1

Assume the lower-order cubic root-flow theorem below vertex order `N` and the concrete singular-confluence hypotheses.

Let `G` be a connected loopless bridgeless cubic graph of order `N`, let `uv` be a simple edge, and let one cross reconnection closure of `G-{u,v}` be a connected loopless bridgeless cubic graph of order `N-2`.

Then

\[
\boxed{G\text{ has a root-valued }E_5\text{ flow}.}
\]

### Proof

Sections 2--6 exhaust the selected cross root flow. Every branch gives the original cap lift. ∎

---

## 8. Logical compression

Theorem 7.1 removes the following assumptions from cap restoration:

- all three reconnection closures are soluble;
- the complete profile meets all three `J_r`;
- the complete profile is classified as `J_i` or `J_i union L_i`;
- prior two-, three-, or four-cut reduction;
- Type T and Type H physical mismatch elimination.

The finite boundary input has become only:

\[
J_j\cap K_i=\{B_j\}
\]

plus the unique non-`K_i` route rows from `A` and `C_j`.

---

## 9. Interface with the global proof

`ONE_CROSS_RECONNECTION_EXISTENCE_V1.md` proves that every simple edge in a connected loopless bridgeless cubic graph has at least one valid smaller cross closure.

Every non-theta connected loopless cubic graph has a simple edge, and theta is an explicit root-soluble base.

Therefore Theorem 7.1 alone closes the cubic minimal-counterexample argument.

---

## 10. PDL obligations

PDL should treat this theorem as the controlling Package B--D bridge and verify:

1. the selected cross boundary trichotomy;
2. one-cross route forcing;
3. equality and DDD termination without hidden separator hypotheses;
4. exact terminal normalisation;
5. the concrete hypotheses of singular contextual confluence;
6. lexicographic noncircularity.

No small-cut or all-three profile theorem should be inserted unless an actual hidden dependence is discovered.

---

## 11. Trust boundary

### Exact authorial claim

- one lower-order cross root flow suffices to restore the original simple edge;
- the repaired singular confluence machinery can be consumed from one selected outer orbit;
- the previous all-three full-channel theorem is stronger than necessary.

### Not claimed

- independent reconstruction of the confluence hypotheses;
- canonical acceptance, Lean verification, manuscript integration, release, peer review, or publication.
