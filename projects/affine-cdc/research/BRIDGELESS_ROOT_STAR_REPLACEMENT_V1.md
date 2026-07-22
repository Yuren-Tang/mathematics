# One root-valued pivot star replacement always remains bridgeless

## Research dossier v2

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Original parent head:** `0ebf2e72d22819e041425a8c8fc7f55d5839e309`  
**v2 correction head:** after `e8294d6210cf9d0a44f98f58a3907c641a502c18`  

**Parents:**

- `projects/affine-cdc/research/PIVOT_CHANGE_SIX_PORT_STAR_COMPLETION_V1.md`;
- `projects/affine-cdc/research/SIX_LEAF_TOPOLOGY_ENERGY_TRIALITY_V1.md`;
- the three-/four-cut gluing and bounded-degeneration modules.

**Status:** exact source-category theorem with no distinct-attachment hypothesis. Let a bridgeless cubic multigraph contain the four-vertex pivot path. Regard its six exterior semiedges as six labelled terminal incidences, allowing several incidences to meet the same exterior vertex. Replace the path by any of the four root-valued three-cherry stars from the six-port table. At least one of those four replacement graphs is bridgeless. The proof uses only the component partition of the six terminal incidences: every exterior component contains at least two incidences, an internal star edge is a bridge exactly when its cherry pair is one two-incidence exterior component, and no family of pairwise disjoint two-terminal blocks can meet all four good matchings. Parallel edges created by coincident exterior vertices are allowed and create no loop.  

**Not implied:** transfer of a five-support cover from the replacement graph back to the original path, that a same-order replacement is strict graph descent, global induction, canonical acceptance, Lean verification, manuscript integration, or the global five-support theorem.

---

## 1. Four-vertex pivot path and terminal incidences

Let `G` be a connected bridgeless cubic multigraph. Let

\[
P=v_0v_1v_2v_3
\]

be an induced four-vertex path whose six exterior incidences are labelled

\[
(s,x)\text{ at }v_0,
\qquad
z\text{ at }v_1,
\qquad
w\text{ at }v_2,
\qquad
(t,y)\text{ at }v_3.
\]

Delete the four vertices of `P` and retain the six terminal semiedges. Put

\[
H=G-V(P).
\]

The six labels denote boundary incidences, not necessarily six distinct exterior vertices. Two or more labels may occur at the same vertex of `H`.

The components of `H` induce a partition

\[
\Pi
\]

of the six terminal incidences

\[
\{s,x,z,w,t,y\}.
\]

Multiplicity at one exterior vertex causes no ambiguity: all incidences at that vertex belong to the same block of `Pi`.

---

## 2. No singleton exterior component

### Lemma 2.1

Every block of `Pi` has size at least two.

### Proof

Suppose one component of `H` contained exactly one terminal incidence `a`. The original boundary edge at `a` would be the only edge joining that component to `P` and hence to the remainder of `G`. It would be a bridge of `G`, contradiction. ∎

This remains valid when two terminal incidences have the same exterior endpoint: they form two elements of the same block.

Consequently the possible block-size patterns are among

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

of the six terminal incidences, form the three-cherry star `S_M`:

- one central cubic vertex;
- one outer cubic cherry vertex for each pair `P_i`;
- the two terminal incidences of `P_i` attached to that cherry;
- the three cherries joined to the central vertex.

Let

\[
G_M=H\cup S_M.
\]

If two terminal incidences have the same exterior endpoint, `G_M` may contain parallel edges. This is allowed in the cubic multigraph category. No loop is created because every terminal edge joins an exterior vertex to a new cherry vertex.

### Lemma 3.1 — boundary edges stay nonbridges

Every terminal edge of `G_M` is nonbridging.

### Proof

Let terminal incidence `a` belong to exterior component `C` of `H`. By Lemma 2.1, `C` contains another terminal incidence `b`.

After deleting the terminal edge at `a`, its exterior endpoint remains connected inside `C` to the exterior endpoint of `b`; if `a,b` have the same endpoint this path has length zero. The incidence `b` remains attached to the star. Hence the deleted edge is not a bridge. ∎

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

Deleting `e_i` separates the two terminal incidences of `P_i` from the other four inside the star. The shores are reconnected through `H` exactly when some exterior component meets both `P_i` and its complement.

Thus `e_i` is a bridge exactly when `P_i` is a union of blocks of `Pi`. Since `|P_i|=2` and every block has size at least two, this occurs exactly when `P_i` itself is one two-element block. ∎

Therefore `G_M` is bridgeless exactly when no pair of `M` is a two-terminal exterior-component block.

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

be the set of two-element blocks of `Pi`. Its members are pairwise disjoint as sets of terminal incidences.

A matching `M_i` produces an internal bridge exactly when

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

the only pair disjoint from `sw` is `zt`; hence `zt in Q`.

Every pair in

\[
M_4=\{sy,xt,zw\}
\]

meets `sw` or `zt`, contradiction.

#### Case 2: `sy in Q`

To meet

\[
M_1=\{sw,xt,zy\},
\]

the only pair disjoint from `sy` is `xt`; hence `xt in Q`.

Every pair in

\[
M_2=\{sw,xy,zt\}
\]

meets `sy` or `xt`, contradiction.

#### Case 3: neither `sw` nor `sy` belongs to `Q`

To meet `M_2`, the family contains `xy` or `zt`.

- If `zt in Q`, both alternatives `xt,zy` for meeting `M_1` intersect `zt`, contradiction.
- Hence `xy in Q`.

To meet `M_3` without `sy` or `zt`, one must have `xw in Q`; but `xy` and `xw` intersect, contradiction. ∎

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

If all four had bridges, Lemma 3.2 would imply that the pairwise disjoint family `Q` of two-terminal exterior-component blocks meets all four matchings. This contradicts Lemma 5.1. ∎

### Corollary 6.2

Failure of all four root-valued star completions cannot be blamed on loss of bridgelessness, even when exterior attachment vertices coincide.

At least one star lies in the same connected bridgeless cubic multigraph category as the original graph.

The only remaining obstruction to using that star is five-support profile transfer / same-order minimality, not source-category admissibility.

---

## 7. Relation to defect minimality

Suppose an `E_5` flow on `G` has three co-root internal edges on `P` and the standard six root boundary. Every one of the four matchings `M_i` gives a root-valued star completion of that boundary.

By Theorem 6.1, one replacement graph is bridgeless. On that graph the inherited `E_5` flow has three fewer defect edges.

This is the exact category input for the secondary minimal-counterexample order by defect number, with no exceptional repeated-attachment branch.

The theorem itself does not transfer a root cover from the star graph back to the path graph.

---

## 8. Trust boundary

### Exact here

- treatment of terminals as labelled incidences with arbitrary endpoint coincidences;
- exterior components have terminal multiplicity at least two;
- preservation of terminal edges as nonbridges;
- the internal-star bridge criterion;
- allowance of parallel edges without loops;
- the pairwise-disjoint four-matchings hitting lemma;
- existence of at least one bridgeless root-valued star replacement in all attachment configurations.

### Still open

- cover transfer from a same-order star replacement to the original path;
- consumption by secondary defect minimality and the three-edge elimination theorem;
- global proof-DAG packaging;
- canonical acceptance, independent audit, Lean verification, manuscript integration;
- the global five-support theorem.
