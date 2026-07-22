# One root-valued pivot star replacement always remains bridgeless

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `0ebf2e72d22819e041425a8c8fc7f55d5839e309`  

**Parents:**

- `projects/affine-cdc/research/PIVOT_CHANGE_SIX_PORT_STAR_COMPLETION_V1.md`;
- `projects/affine-cdc/research/SIX_LEAF_TOPOLOGY_ENERGY_TRIALITY_V1.md`;
- the three-/four-cut gluing and bounded-degeneration modules.

**Status:** exact source-category theorem. Let a bridgeless cubic graph contain the four-vertex pivot path with six distinct exterior attachment vertices. Replace the path by any of the four root-valued three-cherry stars from the six-port table. At least one of those four replacement graphs is bridgeless. The proof uses only the component partition of the exterior six-pole: every component contains at least two terminals, an internal star edge is a bridge exactly when its cherry pair is one two-terminal exterior component, and no family of pairwise disjoint two-terminal blocks can meet all four good matchings.  

**Not implied:** transfer of a five-support cover from the replacement graph back to the original path, that a same-order replacement is strict graph descent, elimination of repeated attachment vertices without a bounded-case lemma, global induction, canonical acceptance, Lean verification, manuscript integration, or the global five-support theorem.

---

## 1. Four-vertex pivot path

Let `G` be a connected bridgeless cubic graph. Let

\[
P=v_0v_1v_2v_3
\]

be an induced four-vertex path whose exterior incidences are labelled

\[
(s,x)\text{ at }v_0,
\qquad
z\text{ at }v_1,
\qquad
w\text{ at }v_2,
\qquad
(t,y)\text{ at }v_3.
\]

Assume the six exterior attachment vertices are distinct.

Delete the four vertices of `P` and retain the six resulting terminal semiedges. Let

\[
H=G-V(P).
\]

The components of `H` induce a partition

\[
\Pi
\]

of the terminal set

\[
\{s,x,z,w,t,y\}.
\]

---

## 2. No singleton exterior component

### Lemma 2.1

Every block of `Pi` has size at least two.

### Proof

Suppose one component of `H` contained exactly one terminal, say `a`. The original boundary edge at `a` would be the only edge joining that component to `P` and hence to the remainder of `G`. It would therefore be a bridge of `G`, contrary to the hypothesis. ∎

Consequently the possible block-size patterns of `Pi` are among

\[
6,
\qquad4+2,
\qquad3+3,
\qquad2+2+2.
\]

---

## 3. Three-cherry star replacements

For a perfect matching

\[
M=\{P_1,P_2,P_3\}
\]

of the six terminals, form the three-cherry star `S_M`:

- one central cubic vertex;
- one outer cubic cherry vertex for each pair `P_i`;
- the two terminals of `P_i` attached to that cherry;
- the three cherries joined to the central vertex.

Let

\[
G_M=H\cup S_M.
\]

The six boundary edges are inherited from `G`; only the internal four-vertex tree is replaced.

### Lemma 3.1 — boundary edges stay nonbridges

Every terminal edge of `G_M` is nonbridging.

### Proof

Let terminal `a` belong to exterior component `C` of `H`. By Lemma 2.1, `C` contains another terminal `b`. After deleting the terminal edge at `a`, the vertex on the exterior side remains connected in `H` to `b`, and `b` remains attached to the star. Thus the deleted edge does not separate `G_M`. ∎

### Lemma 3.2 — internal bridge criterion

Let `e_i` be the internal star edge joining the cherry of pair `P_i` to the centre. Then

\[
\boxed{
e_i\text{ is a bridge of }G_M
\iff
P_i\text{ is a two-element block of }\Pi.
}
\]

### Proof

Deleting `e_i` separates the two terminals of `P_i` from the other four inside the star. The two shores are reconnected through `H` exactly when some component of `H` meets both `P_i` and its complement.

Thus `e_i` is a bridge exactly when `P_i` is a union of blocks of `Pi`. Since `|P_i|=2` and every block has size at least two, this occurs exactly when `P_i` itself is a two-element block. ∎

Therefore `G_M` is bridgeless exactly when no pair of `M` is a two-terminal exterior component.

---

## 4. The four root-valued matchings

For one pivot-change boundary, the four root-valued star matchings are

\[
\begin{aligned}
M_1&=\{sw,xt,zy\},\\
M_2&=\{sw,xy,zt\},\\
M_3&=\{sy,xw,zt\},\\
M_4&=\{sy,xt,zw\}.
\end{aligned}
\]

The two omitted matchings contain the forbidden pivot pair `st`.

Let

\[
\mathcal Q
\]

be the set of two-element blocks of `Pi`. Its members are pairwise disjoint.

A matching `M_i` produces a bridge exactly when

\[
M_i\cap\mathcal Q\ne\varnothing.
\]

---

## 5. Four-matchings hitting lemma

### Lemma 5.1

No family of pairwise disjoint terminal pairs meets all four matchings

\[
M_1,M_2,M_3,M_4.
\]

### Proof

Assume a pairwise disjoint family `Q` meets all four.

#### Case 1: `sw in Q`

To meet

\[
M_3=\{sy,xw,zt\},
\]

the only pair disjoint from `sw` is `zt`. Hence `zt in Q`.

But every pair in

\[
M_4=\{sy,xt,zw\}
\]

meets either `sw` or `zt`. Thus `Q` cannot meet `M_4`, contradiction.

#### Case 2: `sy in Q`

To meet

\[
M_1=\{sw,xt,zy\},
\]

the only pair disjoint from `sy` is `xt`. Hence `xt in Q`.

But every pair in

\[
M_2=\{sw,xy,zt\}
\]

meets either `sy` or `xt`. Contradiction.

#### Case 3: neither `sw` nor `sy` belongs to `Q`

To meet `M_2`, the family must contain `xy` or `zt`.

- If `zt in Q`, then both alternatives `xt,zy` for meeting `M_1` intersect `zt`, contradiction.
- Hence `xy in Q`.

To meet `M_3` without `sy` or `zt`, one must then have `xw in Q`. But `xy` and `xw` intersect, contradicting pairwise disjointness.

All cases are impossible. ∎

---

## 6. Bridgeless replacement theorem

### Theorem 6.1 — one good star survives

Among the four root-valued star replacement graphs

\[
G_{M_1},
G_{M_2},
G_{M_3},
G_{M_4},
\]

at least one is bridgeless.

### Proof

If all four had bridges, Lemma 3.2 would imply that the pairwise disjoint family `Q` of two-terminal exterior components meets all four matchings. This contradicts Lemma 5.1. ∎

### Corollary 6.2

Failure of all four root-valued star completions cannot be blamed on loss of bridgelessness.

At least one star lies in the same bridgeless cubic multigraph category as the original graph.

The only remaining obstruction to using that star is five-support profile transfer / same-order minimality, not source-category admissibility.

---

## 7. Repeated exterior vertices

The theorem assumes six distinct exterior attachment vertices.

If two or more terminal semiedges meet the same exterior cubic vertex, the pivot cell together with that vertex is a bounded multipole with at most five external incidences. Such coincidences must be routed to the bounded-category / small-interface library before applying Theorem 6.1.

No claim is made here that every repeated-vertex configuration is already a cyclic four-cut; a dedicated finite degeneration lemma may be required for the five-boundary case.

---

## 8. Relation to defect-minimality

Suppose an `E_5` flow on `G` has three co-root internal edges on `P` and the standard six root boundary. Every one of the four matchings `M_i` gives a root-valued star completion of that same boundary.

By Theorem 6.1, one such replacement graph is bridgeless. On that graph the inherited `E_5` flow has three fewer defect edges.

This is the exact category input required for a secondary minimal-counterexample order by defect number.

The theorem itself does not transfer a root cover from the star graph back to the path graph.

---

## 9. Trust boundary

### Exact here

- exterior components have terminal multiplicity at least two;
- the internal-star bridge criterion;
- preservation of all terminal edges as nonbridges;
- the pairwise-disjoint four-matchings hitting lemma;
- existence of at least one bridgeless root-valued star replacement.

### Still open

- repeated exterior attachment vertices;
- cover transfer from a same-order star replacement to the original path;
- consumption by secondary defect minimality;
- elimination of the resulting three-defect global normal form;
- global well-founded induction;
- canonical acceptance, independent audit, Lean verification, manuscript integration;
- the global five-support theorem.
