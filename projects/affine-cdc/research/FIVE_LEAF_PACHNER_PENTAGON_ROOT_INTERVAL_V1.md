# Root-valued topologies form one interval on every five-leaf Pachner pentagon

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `1a61cfe3646adfc120a173a21a42a330a8d5a2ea`.

**Parents:**

- `ROOT_FLOW_TRIANGLE_COMPLEX_PACHNER_V1.md`;
- `SIX_LEAF_NNI_ROOT_EXCHANGE_V1.md`;
- `PACHNER_FIRST_FAILURE_CRITICAL_OVERLAP_V1.md`;
- the four-root pairing-sum classification.

**Status:** exact topological/coefficient critical-pair theorem. Two NNI moves supported on the two internal edges of a three-vertex path generate one canonical five-cycle in the five-leaf NNI graph. For every fixed ordered conserved five-root boundary word, the root-valued topologies on that pentagon form one cyclic interval. The only possible cardinalities are `0,1,2,3,5`; there is no disconnected root sector and no four-state sector. Consequently, if the short two-move commutation route passes through a non-root topology while its two branch endpoints are root-valued, the opposite three-move side of the pentagon is entirely root-valued and gives an exact boundary-preserving Pachner commutation.

**Not implied:** that every outer-history overlap has both branch endpoints root-valued for the returned cover, automatic elimination of a surviving one-defect token, global confluence of all equality/DDD reductions, final proof-DAG closure, canonical acceptance, Lean verification, manuscript integration, release, publication, or the global five-support theorem.

---

## 1. Five-leaf topologies and one NNI pentagon

Let the ordered external branches be

\[
A,B,C,D,E.
\]

An unrooted cubic five-leaf tree has three internal vertices, two internal edges, two disjoint cherries, and one central singleton branch.

Consider the following five topologies:

\[
\begin{aligned}
T_0&=BC\mid A\mid DE,\\
T_1&=AC\mid B\mid DE,\\
T_2&=AC\mid E\mid BD,\\
T_3&=AE\mid C\mid BD,\\
T_4&=AE\mid D\mid BC.
\end{aligned}
\]

Consecutive topologies differ by one NNI, including

\[
T_4\longleftrightarrow T_0.
\]

Thus

\[
\boxed{T_0T_1T_2T_3T_4T_0}
\]

is one five-cycle in the NNI graph.

Every pair of NNI moves on the two adjacent internal edges of a three-vertex path is, after relabelling the five external branches, this configuration.

### Theorem 1.1 — topological pentagon relation

Suppose two NNI moves are available from `T_0`, one to `T_1` and one to `T_4`. The two resulting topologies are connected without returning through `T_0` by the unique opposite path

\[
\boxed{
T_1\longrightarrow T_2\longrightarrow T_3\longrightarrow T_4.}
\]

Hence an overlap of two adjacent NNI supports is not a square critical pair. It is one bounded five-leaf pentagon critical pair.

---

## 2. Fixed root boundary word

Let the five external branch values be roots

\[
a,b,c,d,e\in R_5
\]

with total sum

\[
\boxed{a+b+c+d+e=0.}
\]

For two roots `x,y`, write

\[
[x\sim y]=1
\]

when `x+y` is a root, equivalently when `x,y` are distinct and intersect in exactly one support index.

Define five binary predicates

\[
\begin{aligned}
x_0&=[b\sim c],\\
x_1&=[d\sim e],\\
x_2&=[a\sim c],\\
x_3&=[b\sim d],\\
x_4&=[a\sim e].
\end{aligned}
\]

These are the root-admissibility predicates for the five cherries that occur around the pentagon.

---

## 3. Exact validity formula

A five-leaf topology is root-valued exactly when both of its cherry sums are roots. Conservation then forces the central three-root vertex automatically.

Let

\[
\epsilon_i\in\{0,1\}
\]

record whether `T_i` is root-valued for the fixed boundary word.

### Theorem 3.1 — pentagon edge formula

\[
\boxed{
\begin{aligned}
\epsilon_0&=x_0x_1,\\
\epsilon_1&=x_1x_2,\\
\epsilon_2&=x_2x_3,\\
\epsilon_3&=x_3x_4,\\
\epsilon_4&=x_4x_0.
\end{aligned}}
\]

### Proof

For example, `T_0` has cherries `BC` and `DE`, so it is root-valued exactly when

\[
b+c\in R_5
\quad\text{and}\quad
d+e\in R_5,
\]

namely when `x_0=x_1=1`. The other four formulas are identical. ∎

### Interpretation

Place the five predicates

\[
x_0,x_1,x_2,x_3,x_4
\]

on the vertices of a combinatorial cycle `C_5`. Then the valid topologies are exactly the cycle edges whose two endpoint predicates are both one.

Thus the root-valued topology set is the edge set of the subgraph of `C_5` induced by the true predicates.

---

## 4. Root sectors are connected intervals

### Lemma 4.1 — induced edges of `C_5`

For any subset `X` of the five vertices of `C_5`, the induced edge set `E(C_5[X])` is either:

1. empty;
2. one connected path;
3. the complete five-cycle.

It cannot have two nonempty connected components.

### Proof

Two nonempty induced-edge components would each require at least two selected vertices. They would also require at least one unselected separator vertex in each of the two cyclic gaps between the components. This would require at least

\[
2+2+1+1=6
\]

vertices, impossible in `C_5`. ∎

### Theorem 4.2 — five-leaf root-interval theorem

For every ordered conserved five-root boundary word, the root-valued topologies among

\[
T_0,T_1,T_2,T_3,T_4
\]

form exactly one cyclic interval.

Their cardinality is one of

\[
\boxed{0,1,2,3,5.}
\]

There is:

- no disconnected root-valued sector;
- no four-topology root-valued sector.

### Proof

Apply Lemma 4.1 to the predicate set

\[
X=\{i:x_i=1\}.
\]

By Theorem 3.1, valid topologies are the induced edges. A proper connected subgraph of `C_5` has one, two, or three edges; four induced edges force all five predicate vertices and hence all five edges. ∎

---

## 5. Exact root-compatible pentagon commutation

Consider the critical pair at `T_0`:

\[
T_1\longleftarrow T_0\longrightarrow T_4.
\]

### Theorem 5.1 — failed short route forces a root-valued long route

Assume

\[
\epsilon_0=0,
\qquad
\epsilon_1=1,
\qquad
\epsilon_4=1.
\]

Then

\[
\boxed{\epsilon_2=\epsilon_3=1.}
\]

Therefore the complete opposite path

\[
\boxed{
T_1\longrightarrow T_2\longrightarrow T_3\longrightarrow T_4
}
\]

is root-valued and preserves the complete ordered five-root boundary word.

### Proof

The root-valid set is a connected cyclic interval containing the two neighbours `T_1,T_4` of `T_0` but not `T_0`. The only connected path in the remaining four vertices joining `T_1` to `T_4` is

\[
T_1T_2T_3T_4.
\]

Hence all four vertices of that path are valid. ∎

### Corollary 5.2 — root Pachner pentagon

Whenever two overlapping source surgeries have root-valued branch endpoints for the same returned boundary word, but the direct intermediate topology is the equality/DDD singular topology, the surgeries commute through three boundary-preserving root Pachner moves on the opposite side of the five-leaf pentagon.

No defect token is needed in this branch.

---

## 6. When only one branch endpoint is root-valued

Assume

\[
\epsilon_1=1,
\qquad
\epsilon_0=0,
\]

but do not assume `epsilon_4=1`.

By Theorem 4.2, the valid set beginning at `T_1` along the long side is exactly one of:

\[
\{T_1\},
\qquad
\{T_1,T_2\},
\qquad
\{T_1,T_2,T_3\},
\]

unless all five topologies are valid.

Thus moving along

\[
T_1\to T_2\to T_3\to T_4
\]

has one first failed edge and never leaves and later re-enters the root sector.

### Theorem 6.1 — nonbranching pentagon failure

A failed overlapping commutation which does not satisfy Theorem 5.1 relocates the equality/DDD first failure monotonically to one boundary edge of a single root-valid interval. It cannot split into two independent failures inside the pentagon.

Combined with `PACHNER_FIRST_FAILURE_CRITICAL_OVERLAP_V1.md`, the failed edge carries at most one normalized zero/co-root atom.

---

## 7. Exact finite census

There are

\[
\boxed{6240}
\]

ordered five-root boundary words

\[
(a,b,c,d,e)\in R_5^5
\]

with total sum zero.

For one labelled pentagon, exhaustive enumeration gives the following complete pattern census.

### Empty root sector

\[
00000:\qquad 720.
\]

### Singleton sectors

Each of the five rotations of

\[
10000
\]

occurs

\[
540
\]

times.

### Two-topology intervals

Each of the five rotations of

\[
11000
\]

occurs

\[
120
\]

times.

### Three-topology intervals

Each of the five rotations of

\[
11100
\]

occurs

\[
420
\]

times.

### Complete pentagon

\[
11111:\qquad120.
\]

The total is

\[
720+5\cdot540+5\cdot120+5\cdot420+120=6240.
\]

No other binary pattern occurs.

### Corollary 7.1 — five-leaf profile sizes

Each labelled five-leaf topology is root-valued for

\[
\boxed{2160}
\]

ordered conserved boundary words.

Two adjacent topologies have intersection size

\[
\boxed{1080}.
\]

Thus an NNI transfers exactly half of the five-leaf boundary profile, matching the half-profile phenomenon in the six-leaf census.

The human interval proof is controlling; the census is an independent finite certificate.

---

## 8. Consequence for contextual transfer

The local commutation frontier now has only two branches.

### Full root commutation

If both branch endpoints of an overlapping critical pair are root-valued for the returned cover, Theorem 5.1 replaces the overlap by the root-valued three-step pentagon path.

### One-atom relocation

If only one endpoint is root-valued, the root sector has one endpoint along the long path. The first failure relocates monotonically to that endpoint and remains one normalized equality/DDD atom by the critical-overlap theorem.

Hence overlapping surgery histories cannot create:

- two separated root sectors on one critical pentagon;
- repeated loss and recovery of root admissibility;
- two independent first-failure atoms;
- an unbounded local braid relation.

The only remaining global question is whether repeated one-atom relocations must reach:

1. a smaller recursive target;
2. a route-changing matching flip;
3. a bounded direct-pairing terminal;
4. a separator/category exit.

---

## 9. Trust boundary

### Exact here

- canonical five-leaf NNI pentagon;
- exact predicate formula for all five topology indicators;
- induced-`C_5` interpretation;
- connected root-sector theorem;
- possible sector sizes `0,1,2,3,5`;
- root-compatible three-step commutation when the short intermediate fails;
- nonbranching relocation when only one endpoint is root-valued;
- exact `6240`-word pattern census;
- profile size `2160` and adjacent intersection size `1080`.

### Still open

- a global termination theorem for repeated one-atom pentagon relocations;
- proof that the atom cannot return to the same outer lock after a nontrivial circuit;
- complete contextual-transfer synthesis;
- final proof-DAG audit and well-founded packaging;
- canonical acceptance, independent audit, Lean verification, manuscript integration, release, publication;
- the global five-support theorem.
