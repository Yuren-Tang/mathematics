# AC-PD-5CDC EQ-RETURN 4 — triangle contraction and the first bounded-exception theorem

**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**State:** `EXACT SOURCE REDUCTION / PRIME OBSTRUCTION TRIANGLE-FREE`.

---

## 1. Cubic triangle contraction

Let `G` be a finite connected loopless cubic multigraph and let

\[
T=v_1v_2v_3v_1
\]

be a simple triangle. Let `a_i` be the unique edge leaving `v_i`. Contract `T` to one cubic vertex `v_T`, retaining the three external edge objects `a_1,a_2,a_3`. Denote the resulting cubic multigraph by

\[
G/T.
\]

Parallel edges are permitted.

---

## 2. Contraction of a root flow

Let

\[
\lambda:E(G)\to R_5
\]

be a root-valued flow and write

\[
x_i=\lambda(a_i).
\]

Summing the three vertex equations on `T` cancels every internal triangle edge twice and gives

\[
\boxed{x_1+x_2+x_3=0.}
\]

Because every `x_i` is a nonzero root, no two are equal: if `x_1=x_2`, then `x_3=0`. Hence the three roots are distinct, and

\[
x_3=x_1+x_2\in R_5.
\]

Two distinct roots have root sum exactly when they intersect in one support index. Therefore `x_1,x_2,x_3` are the three edges of one support triangle.

### Theorem 2.1 — root-flow contraction

Keeping every exterior edge label unchanged and replacing `T` by the vertex `v_T` gives an `R_5`-valued flow on `G/T`.

---

## 3. Exact expansion count

Conversely, let

\[
\mu:E(G/T)\to R_5
\]

be a root flow. At `v_T`, its three incident roots form one root triangle. Relabel its three support indices as

\[
\{i,j,k\}
\]

so that the external roots at `v_1,v_2,v_3` are

\[
ij,\quad ik,\quad jk.
\]

Let `ell` be one of the two indices in

\[
[5]\setminus\{i,j,k\}.
\]

Assign the internal triangle roots

\[
\lambda(v_1v_2)=i\ell,
\qquad
\lambda(v_1v_3)=j\ell,
\qquad
\lambda(v_2v_3)=k\ell.
\]

Then the three local equations are

\[
ij+i\ell+j\ell=0,
\]

\[
ik+i\ell+k\ell=0,
\]

\[
jk+j\ell+k\ell=0.
\]

All internal labels are roots.

### Theorem 3.1 — exact root-flow expansion

Every root flow on `G/T` has exactly two root-valued expansions across `T`, indexed by the two support indices outside the external root triangle.

### Proof of uniqueness

At `v_1v_2`, the internal root must intersect both external roots `ij` and `ik` in the common support `i`; otherwise one of the two vertex sums is not a root. Its second support must be outside `{i,j,k}`, and conservation then forces the other two internal labels. The same outside index must occur on all three internal edges. There are exactly two choices. ∎

---

## 4. Marked-edge preservation

Let `e,f` be two edge objects not internal to `T`. They survive contraction, including the case in which one is an external edge `a_i`.

Contraction and either expansion leave their root labels unchanged. Consequently

\[
B(\lambda(e),\lambda(f))
\]

is unchanged, where `B` is the polar form of the minus-type root quadric. In particular, the relation

\[
\text{equal}/\text{disjoint}/\text{intersecting}
\]

is preserved.

### Corollary 4.1 — marked reduction

If a marked pair outside the internal triangle admits an intersecting-root realization on `G/T`, it admits one on `G`.

Equivalently, a marked bad pair on `G` contracts to a marked bad pair on `G/T` whenever neither marked edge is internal to `T`.

---

## 5. Triangle versus cyclic connectivity

The three external edges of `T` form the cut

\[
\delta_G(V(T)).
\]

If `G-V(T)` contains a circuit, this is a cyclic three-edge cut.

Assume instead that `G-V(T)` is acyclic. Let it have `n` vertices and `c` connected components. All three cut incidences enter this forest. Hence

\[
2(n-c)=3n-3,
\]

so

\[
n=3-2c.
\]

Connectedness gives `c>=1`, while `n>=1`; therefore

\[
c=1,\qquad n=1.
\]

The outside consists of one cubic vertex joined once to each triangle vertex. Thus

\[
G\cong K_4.
\]

### Theorem 5.1 — triangle alternative

A connected bridgeless cubic graph containing a triangle satisfies exactly one of:

1. it has a cyclic three-edge cut separating the triangle from a circuit-bearing outside;
2. it is `K_4`.

Therefore every graph in the prime branch after cyclic small-cut and bounded-base reductions is triangle-free.

---

## 6. Corrected finite certificate

An exact Boolean satisfiability model was used:

- five Boolean support coordinates per edge;
- even parity at every vertex in every coordinate;
- coordinate weight exactly two on every edge;
- exactly one shared support coordinate on the selected marked pair.

The parity formula was independently cross-checked against cycle-space enumeration on `K_4` and the triangular prism.

### Complete connected simple cubic census through eight vertices

There are eight such graphs. The exact bad-pair counts are:

| graph | girth | bad marked pairs |
|---|---:|---:|
| `K_4` | 3 | 3 |
| triangular prism | 3 | 6 |
| `Cubic(8,3)` | 3 | 3 |
| `MinimalRegularMatchstick(3)` | 3 | 9 |
| pentagonal wedge | 3 | 9 |
| cube | 4 | 0 |
| `K_{3,3}` | 4 | 0 |
| Wagner graph | 4 | 0 |

Thus every small bad graph has a triangle; every triangle-free graph in the complete census has no bad pair.

### Snark check

For the first 18-vertex Blanuša snark, all

\[
\binom{27}{2}=351
\]

unordered edge pairs admit an intersecting-root realization.

These computations are evidence and base-case certificates only. The source theorem is Theorem 5.1, not extrapolation from the census.

---

## 7. Consequence for the prime target

The full-lock source-reduction target may now assume:

\[
\boxed{
G\text{ is simple, triangle-free, and has no accepted cyclic cut of size at most four}.}
\]

All triangle-bearing marked failures lie either in the bounded `K_4` base or behind an already accepted cyclic three-cut.

This removes every observed finite bad pair through eight vertices from the prime frontier.

---

## 8. Trust boundary

### Exact here

- contraction of root flows through a cubic triangle;
- exactly two root-valued expansions;
- preservation of exterior marked labels;
- triangle/cyclic-three-cut/`K_4` alternative;
- complete corrected small census and Blanuša finite check.

### Open

- marked-pair flexibility in arbitrary triangle-free prime graphs;
- four-cycle reduction and other bounded contractions;
- full-channel lock elimination;
- marked-weld return and universal five-CDC.