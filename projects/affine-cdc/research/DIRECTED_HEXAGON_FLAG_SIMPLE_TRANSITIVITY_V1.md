# Directed lifted Petersen hexagon flags form one simply transitive symmetry orbit

## Research Lead finite theorem dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `403e795f2b08e379331fdded5181edd0942370f1`.

**Parents:**

- `RELATIVE_PROJECTIVITY_HEXAGON_2_COMPLEX_V1.md`;
- `RELATIVE_PROJECTIVITY_DIRECTED_REWRITING_BOUNDARY_V1.md`;
- `ROOT_SUPPORT_TRANSPORT_PROJECTIVITY_GROUPOID_V1.md`.

**Status:** exact finite symmetry theorem with a reproducible Wolfram certificate. It reduces the proposed directed hexagon-lift property from a family of labelled rules to one canonical equivariant source-lifting obligation. It does not prove that obligation.

---

## 1. Directed lifted-hexagon flags

Let

\[
P=KG(5,2)
\]

be the Petersen graph on the ten roots, and let

\[
\widetilde P=P\times\mathbf F_2
\]

be the sheet-toggling orientation cover.

A **directed lifted-hexagon flag** is a pair consisting of:

1. one lifted simple `C6` in `widetilde P`;
2. one directed edge on that lifted cycle.

Equivalently it is an ordered six-tuple

\[
(v_0^{b_0},v_1^{b_1},\ldots,v_5^{b_5})
\]

such that:

- consecutive roots are disjoint;
- `b_(i+1)=b_i+1` modulo two;
- the six vertices are distinct;
- the distinguished directed edge is
  \[
  v_0^{b_0}\longrightarrow v_1^{b_1}.
  \]

The Petersen graph has ten simple `C6` cycles. Each has two lifts. Each lifted cycle has twelve directed edge flags. Therefore the total number is

\[
\boxed{10\cdot2\cdot12=240.}
\]

---

## 2. Natural symmetry group

The support permutation group

\[
S_5
\]

acts on roots by

\[
\{i,j\}\longmapsto\{\sigma(i),\sigma(j)\}.
\]

The sheet involution

\[
\epsilon\in C_2
\]

acts by

\[
(r,b)\longmapsto(r,b+\epsilon).
\]

Thus

\[
\mathcal G=S_5\times C_2
\]

acts on directed lifted-hexagon flags, with

\[
|\mathcal G|=120\cdot2=240.
\]

---

## 3. Canonical flag

Choose

\[
\boxed{
\mathfrak h_0=
(13^0,24^1,35^0,14^1,23^0,45^1).
}
\]

Every consecutive pair is disjoint, including `45` and `13`, so this is a lifted Petersen `C6`. Its distinguished directed edge is

\[
\boxed{13^0\longrightarrow24^1.}
\]

The corresponding base hexagon is the identity hexagon associated to active root

\[
34,
\]

because its six pivot roots are exactly the roots meeting `34` in one support index:

\[
13,14,23,24,35,45.
\]

---

## 4. Simple transitivity

### Theorem 4.1

The action of

\[
S_5\times C_2
\]

on directed lifted-hexagon flags is simply transitive.

### Proof

A direct exact enumeration gives:

\[
\#\{\text{directed lifted-hexagon flags}\}=240.
\]

The orbit of `mathfrak h_0` under `S_5 times C_2` also has cardinality `240`. Its stabilizer has cardinality one and consists only of

\[
(\operatorname{id}_{[5]},0).
\]

Since the orbit has the same size as the complete flag set, it is the complete set. Trivial stabilizer gives freeness. ∎

### Intrinsic stabilizer check

The ordered flag lists six roots whose incidence pattern distinguishes all five support indices. A support permutation fixing the ordered six-tuple must fix every support index and hence is the identity. Fixing the sheet-labelled tuple also forces zero sheet flip.

---

## 5. Consequence for directed hexagon lifting

Every selected core rewrite rule consists of:

- one lifted primitive hexagon;
- one orientation of its distinguished edge;
- replacement of that edge by the complementary directed five-edge arc.

By Theorem 4.1 every such directed rule is the image of the canonical rule

\[
13^0\longrightarrow24^1
\]

versus

\[
13^0\longrightarrow45^1\longrightarrow23^0
\longrightarrow14^1\longrightarrow35^0\longrightarrow24^1
\]

under one **unique** element of `S_5 times C_2`.

### Corollary 5.1 — one canonical `DHL` obligation

Suppose the AffineCDC source category, cap-block data and accepted exits are equivariant under:

1. permutation of the five support indices;
2. simultaneous reversal of the projectivity sheet convention.

Then core `DHL` is equivalent to the single canonical statement:

> Every full-context occurrence of the directed token transition `13^0 -> 24^1` either lifts the complementary five-step path
> 
> `13^0 -> 45^1 -> 23^0 -> 14^1 -> 35^0 -> 24^1`
> 
> with all ordered source, side-root, cap-block and route data, or yields an accepted transfer, route, terminal, category or strict-order exit.

No list of eleven separately labelled source theorems is required.

---

## 6. What symmetry does and does not remove

### Removed

- dependence on the arbitrary selected spanning-tree labels;
- eleven separate directed rewrite checks;
- two hundred forty directed flag cases;
- any need to distinguish support names in the local source-lifting theorem.

### Not removed

- construction of the complementary five critical-overlap states;
- proof that they lie in one common source context;
- preservation of side-root attachments and the distinguished cap block;
- compatibility of the five-step movie with source topology;
- strict cancellation or another accepted exit.

The symmetry theorem reduces the size of the missing theorem. It does not supply its physical content.

---

## 7. Wolfram certificate

The computation uses:

1. the ten vertices `Subsets[Range[5],{2}]`;
2. Petersen adjacency by disjointness;
3. all simple cycles from `FindCycle[...,{6},All]`;
4. both sheet lifts;
5. all six cyclic starts and both cycle orientations;
6. all `120` support permutations and both sheet flips.

It returns:

\[
\begin{array}{c|c}
\text{quantity}&\text{value}\\
\hline
\#C_6(P)&10\\
\#\text{ directed lifted flags}&240\\
|S_5\times C_2|&240\\
|\operatorname{Orb}(\mathfrak h_0)|&240\\
|\operatorname{Stab}(\mathfrak h_0)|&1.
\end{array}
\]

A canonical set comparison verifies that the orbit equals the complete independently enumerated flag set.

---

## 8. Trust boundary

### Exact here

- count `240` of directed lifted-hexagon flags;
- natural `S_5 times C_2` action;
- canonical flag `mathfrak h_0`;
- orbit size `240`;
- trivial stabilizer;
- simple transitivity;
- reduction of equivariant core `DHL` to one canonical directed source-lifting theorem.

### Not proved

- equivariant canonical `DHL` itself;
- existence of the complementary five-step physical history;
- any replacement of the controlling actual-`C6/C8` recurrence proof;
- PDL reconstruction, independent audit, Lean verification, manuscript integration, release, arXiv, DOI, peer review, publication, or the global five-cycle double-cover theorem.