# Recursive equality failure can occur only after strict vertex descent

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent:** `02490ceb9db1212636e3fdfc95b9d91182b03667`.  

**Parents:**

- `PACHNER_HISTORY_FIRST_FAILURE_ONE_EDGE_ATOM_V1.md`;
- `EQUALITY_LOCK_GLOBAL_PACHNER_POTENTIAL_V1.md`;
- `ROOT_FLOW_TRIANGLE_COMPLEX_PACHNER_V1.md`;
- the four-root pairing-sum classification;
- the equality/DDD/Type-T one-edge atom grammar.

**Status:** exact sharpening of the first-failure theorem and well-foundedness result. A quadruple-equality first failure cannot arise when reversing a `2--2` Pachner flip. The zero branch of an inverse flip is automatically the nonsingular doubled-intersecting-root case and has the other crossed root topology. Recursive quadruple equality arises only when reversing a prior equal-face cancellation and the two reconnected edges receive the same root. That cancellation removed two vertices. Consequently every recursive equality inverse-expansion problem has target graph order at least two smaller than the equality problem that generated the surgery history.

**Not implied:** elimination of the nonrecursive DDD/Type-T first-failure atoms, transfer from the bounded direct-pairing terminal, final horizontal bookkeeping, global proof-DAG closure, canonical acceptance, Lean verification, manuscript integration, release, publication, or the global five-support theorem.

---

## 1. Outer equality problem and its reduction history

Let

\[
\widehat G
\]

be the target graph of one two-vertex equality inverse expansion. Deleting its two cap vertices and reconnecting the four exterior incidences gives a smaller graph

\[
G_0,
\qquad
|V(\widehat G)|=|V(G_0)|+2.
\]

Assume `G_0` carries the pure-gauge equality lock. Apply the globally monotone root-surgery reduction inside the complementary four-pole:

\[
G_0\longrightarrow G_1\longrightarrow\cdots\longrightarrow G_m.
\]

Every `2--2` Pachner flip preserves vertex count and every equal-face cancellation removes two vertices. Hence

\[
\boxed{|V(G_j)|\le |V(G_0)|<|V(\widehat G)|}
\]

for every stage `j`.

Choose a cap-compatible root flow on a terminal or route-changing stage and reverse the history until the first failed inverse step, as in `PACHNER_HISTORY_FIRST_FAILURE_ONE_EDGE_ATOM_V1.md`.

---

## 2. Zero failure of an inverse Pachner flip is never quadruple equality

Suppose the first failed inverse step restores one old `2--2` topology. Let its ordered four exterior roots be

\[
a_1,a_2,b_1,b_2.
\]

The old central value is forced to be

\[
x=a_1+a_2=b_1+b_2.
\]

Assume the failure is the zero branch:

\[
x=0.
\]

Then

\[
a_1=a_2=a,
\qquad
b_1=b_2=b.
\]

The current topology in the later graph is root-valued. It pairs one `a` with one `b`, so its central value is

\[
a+b\in R_5.
\]

Therefore:

\[
\boxed{a\ne b\quad\text{and}\quad a\cap b\ne\varnothing.}
\]

In particular `a=b` is impossible: if all four exterior roots were equal, every two-two pairing sum would be zero and the current topology could not have been root-valued.

### Theorem 2.1 — inverse-flip zero branch is nonsingular

A zero first failure of an inverse Pachner flip has boundary multiset

\[
\boxed{a,a,b,b}
\]

with `a,b` distinct intersecting roots. The two crossed pairings both have the root central value

\[
a+b.
\]

Thus the failed zero topology has an immediate alternative root topology. It is not the recursive quadruple-equality fibre and not the doubled-disjoint Type-T fibre.

---

## 3. Co-root failure of an inverse Pachner flip

If the restored central value has weight four, it is a co-root. The current topology is root-valued and the old topology is the third member of the local root/root/co-root triality.

Therefore the first failure belongs to the oriented DDD one-edge atom already isolated by the four-root and inverse-dipole programme.

### Corollary 3.1

Reversing a same-order root Pachner flip produces no recursive equality problem. Its only failures are:

1. a nonsingular zero atom with an alternative root NNI;
2. a co-root/DDD atom.

---

## 4. First failure of an inverse cancellation

Suppose the failed inverse step restores two vertices removed by an equal-face cancellation. In the current smaller graph, let the two reconnected edges carry roots

\[
a,b\in R_5.
\]

The restored central value is

\[
x=a+b.
\]

Exactly three cases occur.

### Root case

If `a,b` are distinct and intersect, then

\[
x=a+b\in R_5
\]

and the inverse cancellation succeeds.

### Equality case

If

\[
a=b,
\]

then

\[
x=0
\]

and the restored local boundary is

\[
\boxed{a,a,a,a.}
\]

This is the unique recursive quadruple-equality first failure.

### Doubled-disjoint case

If `a,b` are disjoint, then

\[
x=a+b
\]

is a co-root and the boundary is

\[
\boxed{a,a,b,b,
\qquad a\cap b=\varnothing.}
\]

This is the established doubled-disjoint Type-T/DDD singular fibre, not equality recursion.

### Theorem 4.1 — cancellation trichotomy

An inverse equal-face cancellation gives exactly:

\[
\boxed{
\begin{array}{c|c}
\text{relation of }a,b&\text{inverse outcome}\\
\hline
\text{distinct intersecting}&\text{root success}\\
a=b&\text{quadruple equality}\\
a\cap b=\varnothing&\text{doubled-disjoint co-root atom}.
\end{array}}
\]

No fourth case exists.

---

## 5. Equality recursion strictly lowers target order

Assume the first failed inverse step is the quadruple-equality case of Section 4. Let

\[
G_{j-1}\longrightarrow G_j
\]

be the corresponding forward equal-face cancellation. Then

\[
|V(G_{j-1})|=|V(G_j)|+2.
\]

The failed inverse step is a new equality inverse-expansion problem whose:

- smaller side is `G_j`;
- target graph is `G_(j-1)`.

Since `G_(j-1)` is a stage of the reduction history inside `G_0`,

\[
|V(G_{j-1})|\le |V(G_0)|.
\]

The outer equality target satisfies

\[
|V(\widehat G)|=|V(G_0)|+2.
\]

Therefore:

\[
\boxed{
|V(G_{j-1})|
\le |V(G_0)|
=|V(\widehat G)|-2.}
\]

### Theorem 5.1 — strict recursive vertex descent

Every recursive quadruple-equality first failure has a target graph with at least two fewer vertices than the target graph of the equality problem that generated the surgery history.

Equivalently:

\[
\boxed{
\text{equality}\longrightarrow\text{equality recurrence}
\quad\Rightarrow\quad
|V|\text{ drops by at least }2.}
\]

The recurrence cannot occur across a same-order Pachner flip.

---

## 6. Well-founded equality measure

For an equality inverse-expansion problem define

\[
\boxed{
\mathfrak M_{\mathrm{eq}}
=igl(|V(\widehat G)|,E,\Phi,|V(R)|\bigr),}
\]

ordered lexicographically, where:

- `|V(widehat G)|` is the target graph order of the current equality expansion;
- `(E,Phi,|V(R)|)` is the monotone current-flow Pachner potential on its reduced four-pole.

Then:

1. internal root Pachner moves and cancellations selected within one equality problem lower the suffix `(E,Phi,|V(R)|)`;
2. a recursive quadruple-equality first failure lowers the leading target-order coordinate by at least two;
3. inverse-flip failures never recurse to equality;
4. the other inverse-cancellation failure is doubled-disjoint Type-T/DDD.

### Corollary 6.1 — equality recursion cannot cycle

There is no infinite or same-order cycle of nested pure-gauge equality locks. Every recursive equality call strictly lowers the integer target graph order.

This removes the need to prove that a quadruple-equality atom is enclosed in a strictly shorter same-order Pachner interval. Vertex order itself supplies the required well-founded descent.

---

## 7. Revised disposition of first failures

Combining the first-failure and vertex-descent theorems gives the exact table:

\[
\boxed{
\begin{array}{c|c}
\text{first failed inverse move}&\text{disposition}\\
\hline
2\!-\!2,\ x=0&\text{nonsingular doubled-intersecting; alternate root NNI}\\
2\!-\!2,\ \mathrm{wt}(x)=4&\text{oriented DDD atom}\\
2\!-\!0,\ a=b&\text{recursive equality at target order }-2\\
2\!-\!0,\ a\cap b=\varnothing&\text{doubled-disjoint Type-T/DDD atom}.
\end{array}}
\]

Thus the only equality-recursive row is already strictly vertex-decreasing.

---

## 8. Consequence for the local equality programme

The connected equality carrier now has two independent well-founded controls:

1. **within one target order:**
   \[
   (E,\Phi,|V(R)|)
   \]
   decreases under adaptive current-flow Pachner surgery;
2. **between recursive equality problems:**
   \[
   |V(\widehat G)|
   \]
   decreases by at least two.

Therefore neither projection changes, private-edge flips, nor first-failure equality recurrence can generate an infinite descent obstruction.

The remaining local branches are nonrecursive:

- oriented DDD;
- doubled-disjoint Type-T/DDD;
- bounded direct-pairing terminal;
- route-changing matching flip;
- small separator/category exit.

---

## 9. Trust boundary

### Exact here

- impossibility of quadruple equality at an inverse Pachner flip;
- nonsingularity of every inverse-flip zero atom;
- immediate alternate root topology in that branch;
- complete inverse-cancellation trichotomy;
- identification of quadruple equality as the unique recursive branch;
- strict target-order drop by at least two;
- combined well-founded equality measure;
- exclusion of same-order equality recursion cycles.

### Still open

- complete consumption of the oriented DDD and doubled-disjoint Type-T/DDD rows in one global transfer theorem;
- transfer from the bounded direct-pairing and matching-flip terminals;
- horizontal/profile bookkeeping across recursive returns;
- final proof-DAG assembly;
- canonical acceptance, independent audit, Lean verification, manuscript integration, release, publication;
- the global five-support theorem.