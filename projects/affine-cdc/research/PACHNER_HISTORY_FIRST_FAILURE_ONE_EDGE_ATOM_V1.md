# First failed inverse transfer is exactly one equality/DDD edge atom

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent:** `b3b8daa6c3ec328bee45d93aa9cc34d8d5135c6d`.  

**Parents:**

- `EQUALITY_LOCK_GLOBAL_PACHNER_POTENTIAL_V1.md`;
- `ROOT_FLOW_TRIANGLE_COMPLEX_PACHNER_V1.md`;
- `FULL_DEFECT_TREE_NNI_DESCENT_V1.md`;
- the four-root pairing-sum classification;
- the equality/DDD inverse-dipole rescue programme.

**Status:** exact transfer-localisation theorem. Given a finite history of root-valued `2--2` Pachner flips and equal-face `2--0` cancellations, start with any root-valued flow on the terminal graph and reverse the history only while root admissibility is preserved. If the complete inverse transfer fails, its first failed step creates exactly one non-root central edge and leaves every other edge root-valued. The new value is necessarily zero or a co-root. Hence the complete obstruction to inverse transfer is one residual equality/DDD edge atom, not an accumulated defect network.

**Not implied:** that the residual atom is automatically enclosed in a strictly shorter Pachner history, elimination of the quadruple-equality singular fibre, cover-independent transfer through the entire history, global proof-DAG closure, canonical acceptance, Lean verification, manuscript integration, release, publication, or the global five-support theorem.

---

## 1. Root-surgery histories

Let

\[
G_0\longrightarrow G_1\longrightarrow\cdots\longrightarrow G_m
\]

be a finite sequence of local source surgeries. Every step is one of:

1. a root-valued tetrahedral `2--2` Pachner flip between two adjacent distinct root triangles;
2. an equal-face `2--0` cancellation.

Every step is performed at four labelled exterior incidences and preserves their current root values. The four external ports of the equality carrier are untouched by the history.

The forward history may have been selected by the global potential

\[
\mathcal P=(E,\Phi,|V|),
\]

but the theorem below uses only the local form of the moves.

Let

\[
\rho_m:E(G_m)\to R_5
\]

be an arbitrary root-valued flow on the terminal graph. It need not be the flow used to construct the forward history.

---

## 2. Maximal root-valued inverse prefix

Reverse the moves in the order

\[
G_m\to G_{m-1}\to\cdots\to G_0.
\]

As long as the inverse local move produces a root-valued central edge, perform it and retain the resulting root flow.

There is a unique maximal index

\[
0\le j\le m
\]

such that `rho_m` transfers root-valuedly through

\[
G_m,G_{m-1},\ldots,G_j.
\]

If `j=0`, the complete transfer succeeds. Assume henceforth

\[
j>0.
\]

Then the inverse step

\[
G_j\longrightarrow G_{j-1}
\]

is the first failed step. Before attempting it, every edge of `G_j` is root-valued.

Because all later inverse steps succeeded, no previous defect exists when the first failure is reached.

---

## 3. First failure of an inverse Pachner flip

Suppose the forward step

\[
G_{j-1}\longrightarrow G_j
\]

was a root `2--2` Pachner flip.

At the inverse step, remove the current two-vertex topology and expose four exterior incidences carrying roots

\[
a,b,c,d\in R_5.
\]

The current topology in `G_j` is root-valued, so one pairing sum, say

\[
a+c=b+d,
\]

is a root.

Restoring the old topology forces the central value

\[
\boxed{x=a+b=c+d.}
\]

The four-root pairing-sum theorem gives

\[
\operatorname{wt}(x)\in\{0,2,4\}.
\]

Thus exactly one of:

1. `x` is a root and the inverse transfer succeeds;
2. `x=0`;
3. `x` is a co-root.

At the first failed step only Cases 2--3 occur.

### Theorem 3.1 — Pachner first-failure atom

After restoring the old two-vertex topology and assigning its forced central value `x`:

1. the flow equation holds at both restored cubic vertices;
2. every exterior incidence remains root-valued;
3. every edge outside the restored central edge remains root-valued;
4. the unique non-root edge is the central edge;
5. its value is zero or a co-root.

### Proof

The four external roots are unchanged. At the first restored vertex the incident values are `a,b,x` and

\[
a+b+x=0.
\]

At the second they are `c,d,x` and

\[
c+d+x=0.
\]

No other edge is modified. Since the incoming flow on `G_j` was root-valued everywhere, the displayed central edge is the only possible defect. The weight classification gives zero or co-root in the failure branch. ∎

---

## 4. First failure of an inverse equal-face cancellation

Suppose the forward step

\[
G_{j-1}\longrightarrow G_j
\]

cancelled two equal root triangles. In `G_j`, the cancellation left two reconnected edges. Under the arbitrary terminal-derived flow `rho_j`, let their root values be

\[
a,b\in R_5.
\]

To reverse the cancellation, split both edges, insert two cubic vertices, and join them by one new central edge. Conservation forces the central value

\[
\boxed{x=a+b.}
\]

For two roots:

- if `a,b` are distinct and intersect, `x` is a root;
- if `a=b`, then `x=0`;
- if `a,b` are disjoint, `x` is a co-root.

### Theorem 4.1 — cancellation first-failure atom

The inverse cancellation either succeeds root-valuedly, or produces exactly one non-root central edge:

\[
\boxed{
\begin{array}{c|c}
a=b&x=0\\
a\cap b=\varnothing&x=a+b\text{ is a co-root}.
\end{array}}
\]

Every other edge remains root-valued and both new vertex equations hold.

### Proof

Both halves of the first split edge retain value `a`, and both halves of the second retain value `b`. At each new cubic vertex the incident values are `a,b,a+b`, whose sum is zero. No old edge value changes. ∎

---

## 5. Exact local grammar of the failed edge

Let `e` be the unique failed central edge.

### Zero branch

If

\[
\rho(e)=0,
\]

then at each endpoint the two other incident roots are equal. Thus the local states are

\[
(0,a,a)
\qquad\text{and}\qquad
(0,b,b).
\]

If `a,b` are distinct and intersect, the crossed root topologies are available. The singular residues are:

1. quadruple equality `a=b`;
2. doubled disjoint roots.

### Co-root branch

If

\[
\rho(e)=Q_i,
\]

then each endpoint carries two disjoint roots summing to `Q_i`. The four boundary roots form two one-factor leaves, and the two crossed NNI topologies are root-valued.

### Corollary 5.1 — no new first-failure alphabet

The first failed inverse transfer belongs exactly to the existing one-edge normal form:

\[
\boxed{
\text{zero/equality atom}
\quad\text{or}\quad
\text{co-root/DDD atom}.}
\]

The Type-T singular interpretation appears only through the established doubled-root / doubled-disjoint boundary fibres. There is no history-specific third coefficient type.

---

## 6. Boundary and enclosure data retained at first failure

Every surgery in the history is internal to the selected equality four-pole. Therefore, at the first failed inverse step:

1. the ordered four external terminal incidences of the whole carrier retain the chosen terminal root word;
2. every successfully reversed move retains its labelled local boundary;
3. the failed atom has a canonical ordered four-root boundary supplied by the inverse move;
4. the two shores of that boundary retain the old/new Pachner or cancellation pairing;
5. any route-orientation data attached to the deleted cap is not erased by the coefficient failure.

Thus the residual atom is not merely an abstract zero/co-root edge. It is one oriented one-edge inverse-lift problem embedded in a carrier whose exterior remains root-valued.

What is not yet proved is that its entire repair lock is enclosed in a strict subinterval of the original equality carrier.

---

## 7. Transfer dichotomy for a finite history

### Theorem 7.1 — success or one atom

For every root-valued terminal flow `rho_m`, exactly one of:

1. **complete transfer:** `rho_m` reverses through the entire history to a root-valued flow on `G_0` with the same external terminal word;
2. **first-failure atom:** there is a unique first failed inverse step, and restoring that step gives an `E_5` flow on `G_(j-1)` with exactly one defect edge, which is zero or a co-root.

In particular:

\[
\boxed{
\text{inverse transfer through an arbitrarily long history}
\not\Rightarrow
\text{an arbitrarily large defect network}.}
\]

Stopping at the first failure localises the entire obstruction to one edge.

---

## 8. Relation to defect-tree descent

The full-defect-tree theorem proves that any defect component with at least three vertices admits category-safe NNI descent and cannot survive in a secondary-minimal counterexample. The present theorem is sharper for Pachner-history transfer: no large component is ever created before localisation, because the process stops at the first non-root edge.

Hence the only transfer frontier is already the final normal form of the defect programme:

\[
\boxed{
\text{one oriented equality/DDD inverse-dipole lock}.}
\]

This exactly matches the one-edge frontier left after arbitrary defect-tree descent.

---

## 9. Revised final local obligation

The remaining theorem is now precise.

### Target 9.1 — first-failure enclosure or consumption

Given the first-failure atom of Theorem 7.1, prove one of:

1. a crossed root topology gives immediate profile/route escape;
2. the co-root atom is consumed by the oriented DDD resolution theorem;
3. the zero atom is non-singular and has a root NNI;
4. quadruple equality is enclosed in a strictly smaller equality carrier or shorter causal Pachner cone;
5. doubled disjoint roots localise a Type-T/DDD unit;
6. the ordered four-root boundary exposes a two-, three-, or four-edge separator;
7. the atom is one bounded direct-pairing terminal.

Only Item 4 remains genuinely equality-recursive. The transfer problem is no longer about arbitrary-length defect accumulation.

---

## 10. Trust boundary

### Exact here

- maximal root-valued inverse prefix;
- complete first-failure classification for inverse `2--2` flips;
- complete first-failure classification for inverse `2--0` cancellations;
- exactly one defect edge at first failure;
- zero/co-root dichotomy;
- identification with the established equality/DDD one-edge grammar;
- preservation of the outer terminal root word and local pairing data;
- success-or-one-atom transfer theorem.

### Still open

- strict enclosure of a quadruple-equality first failure;
- cover-independent consumption of every first-failure atom;
- final bounded direct-pairing transfer;
- global well-founded proof-DAG assembly;
- canonical acceptance, independent audit, Lean verification, manuscript integration, release, publication;
- the global five-support theorem.