# Endpoint equalisation eliminates the global three-co-root path

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `e453949843df18f3c00cc2cf70b1d46714af3c9c`  

**Parents:**

- `projects/affine-cdc/research/SECONDARY_DEFECT_MINIMALITY_THREE_EDGE_LOCALISATION_V1.md`;
- `projects/affine-cdc/research/BRIDGELESS_ROOT_STAR_REPLACEMENT_V1.md`;
- `projects/affine-cdc/research/SHIFT_MATCHING_BANDS_ROUTE_TAIT_PEELING_V1.md`;
- the category-safe dipole cancellation and inverse root/equality/DDD lift table.

**Status:** exact elimination of the distinct-attachment global three-edge defect normal form. Write the three co-root labels as `Q_i,Q_j,Q_k`, where `Q_m` is the weight-four vector missing support `m` and `i,j,k` are distinct. The outer-index root `a=ik` repairs the middle defect and exchanges the two outer co-root types. Defect minimality forces the exterior `H_a` terminal routing to pair each endpoint locally; otherwise one of two explicit cycle toggles decreases the defect number. A local zero-cost toggle then changes the defect word to `Q_k,Q_j,Q_k`. The middle two vertices become a backtrack dipole with equal outer labels and equal side labels. Cancelling that dipole gives a graph with two fewer vertices or an already handled small separator. A root cover of the smaller graph expands either root-valuedly or with only one zero/co-root defect, contradicting the previously established global minimum `delta(G)=3`.  

**Not implied:** elimination of repeated exterior attachment vertices, completion of the full global proof DAG outside the final pivot-path hypothesis, canonical acceptance, Lean verification, manuscript integration, or the global five-support theorem.

---

## 1. Co-root notation

For

\[
m\in[5],
\]

write

\[
Q_m
=
\sum_{h\ne m}e_h.
\]

Thus `Q_m` is the unique co-root missing support index `m`.

For distinct indices `m,n`,

\[
\boxed{
Q_m+Q_n=mn,
}
\]

a root.

Let the defect-minimal global normal form be the four-vertex path

\[
v_0v_1v_2v_3
\]

with internal labels

\[
\boxed{
Q_i,
\qquad
Q_j,
\qquad
Q_k,
}
\]

where

\[
i,j,k
\]

are pairwise distinct.

The side root at `v_1` is

\[
ij,
\]

and the side root at `v_2` is

\[
jk.
\]

At the left endpoint `v_0`, the two root boundary labels form a disjoint pair whose union is

\[
[5]\setminus\{i\}.
\]

At the right endpoint `v_3`, the two root boundary labels form a disjoint pair whose union is

\[
[5]\setminus\{k\}.
\]

All exterior edges are root-valued, and the complete defect number is

\[
\delta(G)=3.
\]

---

## 2. The outer-index repair root

Put

\[
\boxed{a=ik.}
\]

Then:

\[
\boxed{
Q_i+a=Q_k,
}
\]

and

\[
\boxed{
Q_k+a=Q_i.
}
\]

Because `i,k` are both different from `j`, the root `a` is contained in `Q_j`, so

\[
\boxed{
Q_j+a
\in R_5.
}
\]

More explicitly, `Q_j+a` is the root on the two support indices outside

\[
\{i,j,k\}.
\]

Thus toggling by `a`:

- keeps an outer defect non-root while exchanging its missing index;
- repairs the middle defect completely.

---

## 3. Four exterior scalar terminals

Let

\[
H_a
=
\{e\text{ exterior root edge}:\lambda(e)+a\in R_5\}.
\]

Since the exterior flow is root-valued, `H_a` is an even scalar subgraph away from the six deleted path incidences.

### Left endpoint

Among the two left endpoint roots, exactly one contains `k`. Call it

\[
L.
\]

The other contains neither endpoint of `a` and is disjoint from `a`.

Hence exactly `L` is an `H_a` terminal at `v_0`.

The side root

\[
ij
\]

intersects `a=ik` at `i`, so it is also an `H_a` terminal. Denote this terminal by

\[
Z.
\]

### Right endpoint

Among the two right endpoint roots, exactly one contains `i`. Call it

\[
R.
\]

It is the unique `H_a` endpoint terminal at `v_3`.

The side root

\[
jk
\]

intersects `a` at `k`; denote this terminal by

\[
W.
\]

Therefore the exterior scalar system has exactly four terminals:

\[
\boxed{L,Z,W,R.}
\]

Its boundary-connected part consists of two paths realising one of the three matchings

\[
LZ\mid WR,
\qquad
LW\mid ZR,
\qquad
LR\mid ZW.
\]

---

## 4. Two pairings strictly reduce the defect count

### Lemma 4.1 — middle repair

If the exterior route contains a path

\[
Z\longleftrightarrow W,
\]

then the union of that path, the two terminal edges `Z,W`, and the middle internal edge `Q_j` is a cycle.

Toggling this cycle by `a`:

- sends `Q_j` to a root;
- keeps every exterior edge root-valued;
- changes no other defect edge.

Hence it produces an `E_5` flow with defect number two, contradicting

\[
\delta(G)=3.
\]

Therefore the route

\[
LR\mid ZW
\]

is impossible.

### Lemma 4.2 — left-to-middle repair

If the exterior route contains a path

\[
L\longleftrightarrow W,
\]

combine it with the internal subpath

\[
v_0v_1v_2,
\]

whose defect labels are `Q_i,Q_j`.

Toggling the resulting cycle by `a`:

- sends `Q_i` to the co-root `Q_k`;
- sends `Q_j` to a root;
- keeps all exterior edges root-valued.

Thus the total defect number drops by one.

Similarly, a path

\[
Z\longleftrightarrow R
\]

combined with the subpath `v_1v_2v_3` repairs `Q_j` while preserving one outer co-root.

Therefore the route

\[
LW\mid ZR
\]

is impossible.

### Theorem 4.3 — forced local pairing

Defect minimality forces

\[
\boxed{
M_a=LZ\mid WR.
}
\]

No other exterior `H_a` pairing is compatible with `delta(G)=3`.

---

## 5. Zero-cost endpoint equalisation

Let

\[
P_{LZ}
\]

be the exterior `H_a` path joining `L` to `Z`.

The union of:

- `P_(LZ)`;
- the terminal edges `L,Z`;
- the first internal defect edge `Q_i`;

is a cycle `C_L`.

Toggle `C_L` by `a=ik`.

Every exterior label remains a root because `C_L` lies in `H_a` outside the defect path. The first internal value changes by

\[
Q_i+a=Q_k,
\]

which is still a co-root. The middle and right defects are unchanged.

Hence the new flow `lambda'` still satisfies

\[
\delta(\lambda')=3.
\]

Its internal defect word is

\[
\boxed{
Q_k,
\qquad
Q_j,
\qquad
Q_k.
}
\]

The left side root becomes

\[
ij+a=jk,
\]

while the right side root was already `jk`.

Therefore both transport vertices `v_1,v_2` now have the same side-root label

\[
\boxed{jk.}
\]

This is the endpoint-equal / immediate-backtrack normal form.

---

## 6. Central backtrack dipole

In the flow `lambda'`, the two middle vertices have local incidence labels

\[
\begin{array}{c|ccc}
v_1&Q_k&Q_j&jk\\
v_2&Q_j&Q_k&jk.
\end{array}
\]

Thus relative to the central edge `v_1v_2`:

- the two outer path incidences have equal label `Q_k`;
- the two side incidences have equal root label `jk`.

Cancel the adjacent vertices `v_1,v_2` and reconnect:

1. the two `Q_k` half-edges to one new edge;
2. the two `jk` half-edges to one new edge.

Call the reduced graph

\[
G'.
\]

It has

\[
|V(G')|=|V(G)|-2.
\]

### Category-safe alternative

The general dipole-cancellation lemmas give one of:

1. `G'` is a connected bridgeless cubic multigraph;
2. the cancellation exposes a cyclic three-edge cut of `G`;
3. it exposes a bounded acyclic / loop / parallel-edge degeneration.

The second and third branches belong to the already established three-cut gluing or bounded-category reductions.

Thus the only irreducible branch is the first.

---

## 7. Root cover of the reduced graph

Assume `G'` is bridgeless. By vertex minimality, `G'` has a root-valued five-support flow.

Let the two new reconnection edges receive roots

\[
p,q\in R_5.
\]

Reinsert `v_1,v_2`. The four noncentral restored edges receive respectively

\[
p,p,q,q,
\]

and the central edge is forced to have value

\[
p+q.
\]

Exactly one of:

1. `p,q` are distinct intersecting roots, so `p+q` is a root and the expansion gives a root flow on `G`;
2. `p=q`, so the central edge has value zero;
3. `p,q` are disjoint, so the central edge has a co-root value.

In Cases 2 and 3, every edge except the central restored edge is root-valued. Therefore the expansion gives an `E_5` flow on `G` with

\[
\delta\le1.
\]

---

## 8. Elimination theorem

### Theorem 8.1 — no global three-co-root path

The distinct-attachment three-edge normal form cannot occur in the refined minimal counterexample.

### Proof

After endpoint equalisation, cancel the central backtrack dipole.

- A separator or bounded degeneration is already a progress branch.
- In the bridgeless reduced branch, vertex minimality gives a root cover of `G'`.
- Root-valued inverse expansion gives a root cover of `G`, contradiction.
- Equality or DDD inverse expansion gives an `E_5` flow on `G` with at most one defect, contradicting
  \[
  \delta(G)=3.
  \]

Every branch is impossible in the irreducible minimal-counterexample regime. ∎

---

## 9. Mechanistic interpretation

The final three-edge obstruction is eliminated by two strict scales.

### Horizontal scale

The outer-index root `ik` supplies a zero-cost cycle which transports one outer co-root endpoint across the middle pivot:

\[
(Q_i,Q_j,Q_k)
\longrightarrow
(Q_k,Q_j,Q_k).
\]

Defect minimality determines the required exterior route uniquely.

### Vertical / graph scale

The endpoint-equal word is an immediate co-root transport backtrack. Cancelling its middle dipole lowers the graph by two vertices.

Any failure of inverse root expansion lowers the defect number from three to one.

Thus the lexicographic measure

\[
\boxed{
(|V(G)|,\delta(G))
}

strictly decreases in every non-root branch.

This is the first complete composition move combining horizontal defect relocation with vertical graph descent.

---

## 10. Remaining bounded branch

The theorem assumes the six exterior attachment vertices of the original pivot path are distinct, through the bridgeless-star localisation theorem.

If exterior attachment vertices repeat, the path lies in a bounded five-or-fewer attachment multipole. Those configurations remain to be enumerated or reduced to the existing two-/three-/four-port libraries.

No unbounded distinct-attachment pivot path survives.

---

## 11. Trust boundary

### Exact here

- co-root index notation and the outer-index repair root;
- the four-terminal exterior `H_(ik)` system;
- exclusion of two pairings by explicit defect-decreasing cycle toggles;
- forced local pairing `LZ|WR`;
- zero-cost endpoint equalisation;
- the backtrack incidence labels `Q_k,Q_j,Q_k` with equal side roots;
- category-safe central dipole cancellation;
- inverse expansion with root/equality/DDD table;
- contradiction with vertex minimality or `delta(G)=3`.

### Consumed earlier inputs

- global localisation `delta(G)=3`;
- all exterior edges root-valued;
- six distinct exterior attachment vertices;
- three-cut / bounded-degeneration handling for dipole cancellation.

### Still open

- repeated exterior attachment configurations;
- verification that every route to the final frontier satisfies the three-edge localisation hypotheses without a hidden branch;
- global proof-DAG packaging and well-founded induction;
- canonical acceptance, independent audit, Lean verification, manuscript integration;
- the global five-support theorem.
