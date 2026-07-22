# Every nontrivial full-defect tree admits category-safe NNI descent

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `7b38babca6688c1e5f172036526822273b863b9d`  

**Parents:**

- `projects/affine-cdc/research/ANCHORED_ROOT_CATERPILLAR_BRIDGELESS_REPLACEMENT_V1.md`;
- `projects/affine-cdc/research/SIX_LEAF_NNI_ROOT_EXCHANGE_V1.md`;
- `projects/affine-cdc/research/SECONDARY_DEFECT_MINIMALITY_THREE_EDGE_LOCALISATION_V1.md`;
- the defect-minimal forest grammar;
- the two-/three-cut and bounded-category reductions.

**Status:** exact local and global descent theorem for an induced defect-tree component whose every internal edge is zero or co-root. Every such tree with at least three internal vertices contains an internal edge with an NNI alternative whose new central value is a root. Replacing the local two-vertex topology by that NNI either preserves connected bridgelessness or exposes a two-edge separator / bounded degeneration in the original graph. In the bridgeless branch, secondary defect minimality makes the NNI graph soluble; transferring its root cover back through the inverse NNI gives an `E_5` flow on the original graph with at most one defect. Hence a defect-minimal counterexample cannot contain a defect-tree component with at least three vertices.

**Not implied:** elimination of all one-edge zero/equality/DDD defect components; a complete audit that every preceding AffineCDC branch enters the defect-minimal forest setting; global well-founded packaging; canonical acceptance; independent audit; Lean verification; manuscript integration; or the global five-support theorem.

---

## 1. Full-defect tree grammar

Let `K` be one induced tree component of the defect support of an `E_5` flow. Every internal edge of `K` has value either:

- zero;
- a co-root
  \[
  Q_i=\sum_{h\ne i}e_h.
  \]

Every edge leaving `K` is root-valued.

At a cubic vertex, conservation gives exactly the established grammar.

### Degree one in `K`

The vertex is a leaf of the defect tree.

1. **Equality leaf**
   \[
   (0,a,a),
   \qquad a\in R_5.
   \]
2. **DDD one-factor leaf**
   \[
   (Q_i,a,b),
   \qquad a,b\in R_5,
   \qquad a\cap b=\varnothing,
   \qquad a+b=Q_i.
   \]

### Degree two in `K`

The vertex is a co-root transport vertex:

\[
\boxed{(Q_i,Q_j,ij),
\qquad i\ne j.}
\]

No zero edge can occur at degree two, since `(0,d,r)` with `d` non-root cannot have root `r=d`.

### Degree three in `K`

Exactly one of:

1. **mixed branch**
   \[
   \boxed{(0,Q_i,Q_i);}
   \]
2. **all-zero branch**
   \[
   \boxed{(0,0,0).}
   \]

There is no three-co-root zero-sum vertex.

---

## 2. NNI coefficient triality

Let one internal edge `e` join two cubic vertices. Removing `e` exposes four rooted branches with total values

\[
A,B,C,D\in E_5,
\qquad
A+B+C+D=0.
\]

The three local binary tree topologies have central values

\[
p=A+B,
\qquad
q=A+C,
\qquad
r=A+D,
\]

and

\[
p+q+r=0.
\]

The current tree uses `p`. An NNI move replaces it by `q` or `r` and changes no other internal split or edge label.

Thus an NNI is defect-lowering exactly when one of `q,r` is a root.

---

## 3. A co-root cherry always descends

Choose a cherry vertex of `K`, namely a defect-tree leaf whose two other incidences are boundary roots.

Assume its internal defect edge has label

\[
p=Q_i.
\]

Let its two boundary roots be `A,B`, so

\[
A+B=Q_i,
\qquad A\cap B=\varnothing.
\]

Let `y` be the neighbouring defect-tree vertex.

### Case 3.1 — transport neighbour

At `y`, the other two incidences are

\[
Q_j
\qquad\text{and}\qquad
ij
\]

for some `j\ne i`.

The two NNI alternatives based on one cherry root `A` are

\[
A+Q_j
\qquad\text{and}\qquad
A+ij.
\]

The root `A` avoids support index `i`.

- If `A` contains `j`, then `A+ij` is a root and `A+Q_j` is a co-root.
- If `A` avoids `j`, then `A+Q_j` is a root and `A+ij` is a co-root.

Hence exactly one NNI alternative is root-valued.

### Case 3.2 — mixed-branch neighbour

At `y`, the other two defect incidences are

\[
Q_i
\qquad\text{and}\qquad
0.
\]

One NNI alternative has central value

\[
A+0=A,
\]

a root.

### Theorem 3.3 — co-root leaf descent

Every DDD/co-root cherry in a defect tree with more than two vertices admits an immediately defect-lowering NNI.

The excluded two-vertex tree is the single inverse-dipole atom and is treated separately.

---

## 4. Equality cherries

Assume the cherry edge is

\[
p=0.
\]

The two boundary roots at the cherry are equal:

\[
A=B=a.
\]

The neighbouring vertex cannot be a degree-two transport vertex, because a zero incidence at degree two would force its boundary incidence to be non-root.

### Case 4.1 — all-zero neighbour

The two other branch values are

\[
C=D=0.
\]

Both NNI alternatives have value

\[
a+0=a,
\]

so they are root-valued.

### Case 4.2 — mixed neighbour

The two other branch values are

\[
C=D=Q_i.
\]

The NNI value is

\[
a+Q_i.
\]

This is a root exactly when `a` avoids the missing index `i`. If `a` contains `i`, write

\[
a=ih.
\]

Then

\[
a+Q_i=Q_h,
\]

a co-root. This is the only nonlowering equality-cherry configuration.

---

## 5. Propagation along a constant co-root arm

Assume the exceptional equality-cherry configuration:

- a zero cherry labelled by repeated root `a=ih`;
- its zero edge enters a mixed vertex carrying
  \[
  (0,Q_i,Q_i).
  \]

Follow one of the two `Q_i` arms away from that mixed vertex.

At every later vertex reached by an incoming `Q_i` edge, one of the following occurs.

### Transport exit

The local labels are

\[
(Q_i,Q_j,ij),
\qquad j\ne i.
\]

For the NNI centred on the incoming `Q_i` edge, the branch values on the mixed side are

\[
0,Q_i,
\]

and on the transport side are

\[
Q_j,ij.
\]

One NNI alternative has central value

\[
0+ij=ij,
\]

a root.

### DDD leaf exit

The two branch values at the leaf side are roots. Pairing either with the zero branch on the mixed side gives a root NNI value.

### Mixed continuation

The next vertex again carries

\[
(0,Q_i,Q_i),
\]

and the constant-`Q_i` arm continues.

Because `K` is a finite tree, a constant-`Q_i` arm cannot continue through mixed vertices forever and cannot close into a cycle. It must eventually reach a transport vertex or a DDD leaf. At that first exit, a root-valued NNI exists.

### Theorem 5.1 — equality-leaf propagation

Every equality cherry in a defect tree with at least three vertices either has an immediate root NNI or lies at the start of a finite constant-co-root arm whose first nonmixed exit has a root NNI.

---

## 6. Full-defect NNI descent theorem

Every finite unrooted cubic tree with at least two leaves has a cherry. Apply Sections 3–5 to a cherry of `K`.

### Theorem 6.1

Let `K` be a full-defect tree component with

\[
|V(K)|\ge3.
\]

Then there is an internal edge `e` and one NNI alternative `K'` such that:

1. every internal edge other than `e` keeps its old value;
2. the old value on `e` is zero or co-root;
3. the new value on `e` is a root.

Therefore the topology defect energy drops by exactly one:

\[
\boxed{
E(K')=E(K)-1.
}
\]

No fully defective tree of size at least three is an NNI local minimum.

### Finite checks

Exact exhaustive enumeration confirms:

- every fully defective five-leaf topology has a lowering NNI;
- every fully defective six-leaf topology has a lowering NNI;
- the only four-leaf local minima are the expected one-edge equality/DDD singular fibres.

The proof above is independent of the finite checks.

---

## 7. Category-safe NNI replacement

Consider the two adjacent cubic vertices around `e`. Removing them leaves four labelled branch incidences

\[
A,B,C,D.
\]

The original topology is

\[
AB\mid CD.
\]

Suppose the lowering NNI is

\[
AC\mid BD.
\]

Let `H` be the exterior graph after deleting the two local vertices. Its connected components partition the four branch incidences.

Because the original graph is bridgeless, no exterior component contains exactly one branch incidence. Hence the partition is either:

\[
4
\qquad\text{or}\qquad
2+2.
\]

Every branch attachment edge remains nonbridging after the NNI, for the same no-singleton reason.

The new central edge is a bridge exactly when the exterior partition is

\[
\boxed{AC\mid BD.}
\]

### Theorem 7.1 — NNI category alternative

A local NNI replacement in a connected bridgeless cubic multigraph gives exactly one of:

1. a connected bridgeless cubic multigraph of the same order;
2. a two-edge cut in the original graph;
3. a bounded acyclic / parallel-edge degeneration attached through at most two edges.

### Proof

If the exterior partition is not `AC|BD`, the new central edge reconnects the two exterior shores and is nonbridging; all branch edges are also nonbridging.

If the exterior partition is `AC|BD`, place both original local vertices on the `AC` shore. The two branch edges leading to `B,D` are then the only edges crossing to the other exterior component. Hence they form a two-edge cut in the original graph.

If both shores contain cycles, this is the established cyclic two-cut gluing branch. If one shore is acyclic or consists only of a bounded multiple-edge neighbourhood, it is a bounded category degeneration. ∎

Terminal endpoint coincidences create only parallel edges between old and new vertices and do not invalidate the argument.

---

## 8. Secondary-minimality contradiction

Choose a connected bridgeless cubic counterexample `G` lexicographically minimal for

\[
\boxed{(|V(G)|,\delta(G)).}
\]

Let `lambda` be a defect-minimal `E_5` flow and let `K` be a defect component with

\[
|V(K)|\ge3.
\]

By Theorem 6.1, replace one local topology by a lowering NNI. The inherited flow on the replacement graph `G'` has

\[
\boxed{
\delta(\lambda')=\delta(G)-1.
}
\]

### Separator branch

If `G'` is not bridgeless, Theorem 7.1 exposes a two-cut or bounded degeneration already handled by the global reduction programme.

### Bridgeless branch

Assume `G'` is connected and bridgeless. It has the same vertex count as `G` and an `E_5` flow with fewer defects. Hence it cannot be a counterexample by secondary minimality. Let

\[
\rho:E(G')\to R_5
\]

be a root-valued flow.

Transfer `rho` back through the inverse NNI to the original topology. The four branch incidences carry roots

\[
A,B,C,D\in R_5,
\qquad
A+B+C+D=0.
\]

The central value in `G'` is one root pairing sum. The central value forced in `G` is one of the other two pairing sums. By the exact four-root classification, it is one of:

- a root;
- zero;
- a co-root.

Every other edge remains root-valued. Therefore the transferred `E_5` flow on `G` has

\[
\boxed{
\delta\le1.
}
\]

But `K` contains

\[
|E(K)|=|V(K)|-1\ge2
\]

defect edges in the selected defect-minimal flow, so

\[
\delta(G)\ge2.
\]

Contradiction.

### Theorem 8.1 — no large defect component

A lexicographically minimal counterexample has no defect-tree component with at least three vertices.

Equivalently every remaining defect component consists of exactly one zero or co-root edge between two cubic vertices.

---

## 9. Relation to the previous pivot-path route

The earlier composition programme reduced the inverse-dipole full lock to a four-vertex three-co-root pivot path and then eliminated that path by:

\[
\delta(G)=3
\longrightarrow
\text{endpoint equalisation}
\longrightarrow
\text{central dipole cancellation}.
\]

The present theorem gives a shorter vertical reduction whenever a defect-minimal component has at least three vertices:

\[
\text{full-defect tree}
\longrightarrow
\text{one lowering NNI}
\longrightarrow
\delta(G)\le1.
\]

Thus the three-co-root path elimination remains a valid independent certificate and a bounded check on the old route, but the global forest analysis need not force every large component specifically into that path before obtaining strict progress.

---

## 10. Remaining one-edge normal form

After Theorem 8.1, the only defect components are one-edge atoms.

### Co-root atom

The central value is `Q_i`; the four boundary roots form two one-factor leaves. The two crossed NNI topologies are root-valued.

### Zero atom

The central value is zero; each endpoint has two equal boundary roots. If the two endpoint roots are distinct and intersecting, both crossed NNI topologies are root-valued. The singular residues are:

- quadruple equality;
- doubled disjoint roots.

These are exactly the equality/DDD/Type-T singular fibres already isolated by the inverse-dipole and cap-profile programme.

The remaining global task is therefore no longer arbitrary forest descent. It is the complete elimination of one-edge inverse-dipole locks, together with proof-DAG verification that all separator and low-rank branches are consumed.

---

## 11. Reliability boundary

### Exact theorem-level results

- complete local grammar of a full-defect tree;
- immediate descent at every co-root cherry;
- equality-cherry classification;
- propagation along a finite constant-co-root mixed arm;
- existence of a root-lowering NNI for every full-defect tree with at least three vertices;
- category-safe bridgeless-or-two-cut NNI replacement;
- inverse NNI transfer with at most one defect;
- exclusion of every defect component of size at least three by secondary minimality.

### Still open

- elimination of every residual one-edge zero/co-root inverse-dipole lock in one gap-free global theorem;
- consumption of all equality, DDD, Type-T, and fixed-route subbranches without circular use of minimality;
- final proof-DAG audit and well-founded packaging;
- canonical acceptance, independent audit, Lean verification, manuscript integration;
- the global five-support theorem.
