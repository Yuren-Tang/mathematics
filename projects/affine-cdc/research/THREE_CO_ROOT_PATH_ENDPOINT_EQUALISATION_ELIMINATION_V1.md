# Endpoint equalisation eliminates the global three-co-root path

## Research dossier v2

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Original parent head:** `e453949843df18f3c00cc2cf70b1d46714af3c9c`  
**v2 correction:** consumes the incidence-level `BRIDGELESS_ROOT_STAR_REPLACEMENT_V1.md` v2 and therefore has no repeated-attachment exception.  

**Parents:**

- `projects/affine-cdc/research/SECONDARY_DEFECT_MINIMALITY_THREE_EDGE_LOCALISATION_V1.md`;
- `projects/affine-cdc/research/BRIDGELESS_ROOT_STAR_REPLACEMENT_V1.md`;
- `projects/affine-cdc/research/SHIFT_MATCHING_BANDS_ROUTE_TAIT_PEELING_V1.md`;
- the category-safe dipole cancellation and inverse root/equality/DDD lift table.

**Status:** exact elimination of the global three-edge defect normal form for arbitrary exterior attachment coincidences. Write the three co-root labels as `Q_i,Q_j,Q_k`, where `Q_m` is the weight-four vector missing support `m` and `i,j,k` are distinct. The outer-index root `a=ik` repairs the middle defect and exchanges the two outer co-root types. Defect minimality forces the exterior `H_a` terminal routing to pair each endpoint locally; otherwise an explicit cycle toggle decreases the defect number. A local zero-cost toggle changes the defect word to `Q_k,Q_j,Q_k`. The middle two vertices become a backtrack dipole with equal outer labels and equal side labels. Cancelling that dipole gives a graph with two fewer vertices or an already handled small separator. A root cover of the smaller graph expands either root-valuedly or with only one zero/co-root defect, contradicting the global minimum `delta(G)=3`.  

**Not implied:** that every earlier research reduction has already been assembled into a gap-free global proof DAG reaching this normal form, canonical acceptance, Lean verification, manuscript integration, or the global five-support theorem.

---

## 1. Co-root path normal form

For

\[
m\in[5]
\]

write

\[
Q_m=\sum_{h\ne m}e_h.
\]

Thus `Q_m` is the co-root missing support `m`, and for distinct `m,n`,

\[
\boxed{Q_m+Q_n=mn.}
\]

Let the refined defect-minimal counterexample have the global normal form

\[
v_0v_1v_2v_3
\]

with internal labels

\[
\boxed{Q_i,Q_j,Q_k}
\]

for pairwise distinct `i,j,k`.

The side roots are

\[
ij
\qquad\text{and}\qquad
jk.
\]

At the left endpoint the two boundary roots form a perfect matching of

\[
[5]\setminus\{i\};
\]

at the right endpoint they form a perfect matching of

\[
[5]\setminus\{k\}.
\]

All exterior edges are root-valued and

\[
\boxed{\delta(G)=3.}
\]

The six terminal incidences may meet arbitrary exterior vertices.

---

## 2. The outer-index root

Put

\[
\boxed{a=ik.}
\]

Then

\[
Q_i+a=Q_k,
\qquad
Q_k+a=Q_i,
\]

while

\[
Q_j+a
\]

is the root on the two support indices outside `{i,j,k}`.

Thus adding `a`:

- exchanges the two outer co-root types;
- repairs the middle co-root completely.

---

## 3. Four scalar terminals in the exterior

Let

\[
H_a
=
\{e\text{ exterior}:\lambda(e)\in R_5,
\ \lambda(e)+a\in R_5\}.
\]

Because the exterior flow is root-valued, `H_a` is an even scalar subgraph with four boundary incidences after the path is removed.

- Among the two left endpoint roots, exactly one contains `k`; call its terminal `L`.
- The left side root `ij` gives terminal `Z`.
- Among the two right endpoint roots, exactly one contains `i`; call its terminal `R`.
- The right side root `jk` gives terminal `W`.

Hence the boundary-connected part of `H_a` has terminals

\[
\boxed{L,Z,W,R}
\]

and one of the three pairings

\[
LZ\mid WR,
\qquad
LW\mid ZR,
\qquad
LR\mid ZW.
\]

This statement concerns labelled incidences and is unaffected when several terminals share an exterior vertex.

---

## 4. Two pairings decrease the defect number

### Middle pairing

If `Z` is paired with `W`, combine the exterior `Z--W` path with the middle defect edge `Q_j`. Toggling the resulting cycle by `a` sends `Q_j` to a root and keeps every exterior edge root-valued.

Therefore

\[
\delta
\]

drops from three to two, contradiction.

### Cross pairing

If `L` is paired with `W`, combine that exterior path with the internal subpath carrying `Q_i,Q_j`. The toggle sends

\[
Q_i\mapsto Q_k
\]

and repairs `Q_j`, so the defect number drops by one.

The complementary path `Z--R` gives the symmetric right-hand repair.

Therefore both pairings

\[
LR\mid ZW
\qquad\text{and}\qquad
LW\mid ZR
\]

are impossible.

### Theorem 4.1 — forced endpoint-local route

\[
\boxed{
M_a=LZ\mid WR.
}
\]

This is forced solely by `delta(G)=3`.

---

## 5. Zero-cost endpoint equalisation

Let `P_(LZ)` be the exterior path joining `L` and `Z`.

The union of:

- `P_(LZ)`;
- the two terminal edges;
- the first internal defect edge `Q_i`;

is a cycle. Toggle it by `a=ik`.

Every exterior edge remains a root. The first defect changes as

\[
Q_i\mapsto Q_k,
\]

while the other two remain unchanged. Hence the new defect word is

\[
\boxed{Q_k,Q_j,Q_k}
\]

and still has defect number three.

The left side root changes from

\[
ij
\]

to

\[
ij+ik=jk,
\]

which equals the right side root. Thus the two middle transport vertices now have incidence tables

\[
\begin{array}{c|ccc}
v_1&Q_k&Q_j&jk\\
v_2&Q_j&Q_k&jk.
\end{array}
\]

This is the immediate co-root backtrack.

---

## 6. Central dipole cancellation

Cancel `v_1,v_2` and reconnect:

1. the two `Q_k` half-edges;
2. the two `jk` half-edges.

The reduced graph `G'` has

\[
|V(G')|=|V(G)|-2.
\]

The category-safe cancellation theorem gives one of:

1. `G'` is connected and bridgeless;
2. a cyclic three-cut is exposed;
3. a bounded acyclic, loop, or parallel-edge degeneration is exposed.

The last two are already handled by the three-cut / bounded-category modules. Hence only the bridgeless branch remains in an irreducible minimal counterexample.

---

## 7. Inverse expansion from the smaller graph

By vertex minimality, a bridgeless `G'` has a root-valued five-support flow.

Let the two reconnection edges have roots

\[
p,q\in R_5.
\]

Reinsert the two vertices. The four noncentral edges receive

\[
p,p,q,q,
\]

and the central edge receives

\[
p+q.
\]

Exactly one of:

1. `p,q` are distinct and intersecting, so `p+q` is a root and the expansion gives a root flow on `G`;
2. `p=q`, so the central edge is zero;
3. `p,q` are disjoint, so the central edge is a co-root.

In Cases 2 and 3, every edge except the central edge is root-valued. Thus the expansion gives an `E_5` flow on `G` with

\[
\delta\le1.
\]

---

## 8. Elimination theorem

### Theorem 8.1 — no global three-co-root path

The three-edge normal form cannot occur in the refined minimal counterexample, with or without exterior attachment coincidences.

### Proof

Endpoint equalisation produces the backtrack dipole.

- A separator or bounded degeneration is already a progress branch.
- In the bridgeless reduced branch, root-valued inverse expansion gives a root cover of `G`, contradiction.
- Equality or DDD inverse expansion gives an `E_5` flow with at most one defect, contradicting
  \[
  \delta(G)=3.
  \]

All branches are impossible. ∎

---

## 9. Global meaning

The final composition move uses the lexicographic measure

\[
\boxed{(|V(G)|,\delta(G)).}
\]

- The horizontal `ik` toggle preserves the vertex count and defect number but converts the pivot path to a backtrack.
- The central cancellation lowers the vertex count by two.
- Any failed inverse expansion lowers the defect number from three to at most one.

Thus the final unbounded pivot-change carrier admits strict progress in every branch.

No separate repeated-attachment or six-port topology exception survives.

---

## 10. Trust boundary

### Exact here

- the outer-index repair root;
- the four-terminal exterior scalar system;
- exclusion of two pairings by explicit defect-decreasing cycle toggles;
- forced route `LZ|WR`;
- zero-cost endpoint equalisation;
- the backtrack incidence labels;
- category-safe central dipole cancellation;
- inverse root/equality/DDD expansion;
- elimination for arbitrary terminal-incidence coincidences.

### Consumed inputs

- global localisation `delta(G)=3`;
- all exterior edges root-valued;
- incidence-level bridgeless star replacement;
- three-cut / bounded-degeneration handling.

### Still open

- verification that the complete preceding proof DAG reaches the three-edge normal form with no omitted branch;
- one global well-founded theorem packaging all vertical and horizontal reductions;
- canonical acceptance, independent audit, Lean verification, manuscript integration;
- the global five-support theorem.
