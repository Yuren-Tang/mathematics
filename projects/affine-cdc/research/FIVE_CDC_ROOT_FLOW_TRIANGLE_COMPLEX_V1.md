# Root flows as paired even triangle multidesigns

**Programme:** `AffineCDC — Research Lead`  
**Status:** theorem-level structural checkpoint; not canonical pending review  
**Parents:** `FIVE_CDC_UNIVERSAL_ORTHOGONAL_ROOT_LIFT_V1.md`, `FIVE_CDC_HALFCUBE_SUBGRAPH_CLASSIFICATION_V1.md`

## 1. Local triangles and global pairings

Let `S` be a finite support-index set and identify the roots of the even-weight
module on `S` with the edges of the complete graph `K_S`:

\[
r_{ij}=e_i+e_j,
\qquad i\neq j.
\]

Let `G` be a finite loopless cubic multigraph and let

\[
g:E(G)\longrightarrow E(K_S)
\]

be a root-valued flow.

At a source vertex `v`, the three incident root labels sum to zero. Three
distinct weight-two words sum to zero exactly when they are the three edges of a
triangle of `K_S`. Denote this local label triangle by

\[
T_v\in\binom{S}{3}.
\]

Thus a root flow has two complementary descriptions.

1. **Source description:** equal root labels are paired across the two ends of
   every source edge.
2. **Target description:** every source vertex contributes one triangle of the
   support-index complete graph.

The passage between them is exact.

## 2. Even triangle multidesigns

A finite multiset `\mathcal T` of triangles of a graph `J` is called an **even
triangle multidesign** when every edge of `J` occurs in an even number of members
of `\mathcal T`, counted with multiplicity.

It is **support-exact** when every edge of `J` occurs at least once.

### Theorem 2.1 — root-flow pairing theorem

The following data are equivalent.

1. A finite loopless cubic multigraph `G` together with a root flow
   \[
   g:E(G)\to E(J)
   \]
   whose used-label graph is exactly `J`.
2. A support-exact even triangle multidesign `\mathcal T` on `J`, together with,
   for every edge `a\in E(J)`, a pairing of all occurrences of `a` among the
   triangles of `\mathcal T`.

Under the equivalence:

- the members of `\mathcal T` are the vertices of `G`;
- an occurrence of a label edge `a` in a triangle is an `a`-labelled half-edge;
- paired occurrences form one source edge labelled by `a`.

#### Proof

Given a root flow, take the multiset

\[
\mathcal T_g:=\{T_v:v\in V(G)\}.
\]

For a target edge `a\in E(J)`, every source edge labelled `a` contributes one
occurrence at each of its two endpoints. Hence the total number of occurrences
of `a` in `\mathcal T_g` is even. Pair the two occurrences belonging to each
source edge. Since `J` is the used-label graph, the multidesign is support-exact.

Conversely, create one source vertex for every triangle occurrence in
`\mathcal T`. Give it three half-edges labelled by the three target edges of that
triangle. Pairing equal-labelled occurrences produces source edges. A triangle
contains each of its edges only once, so no paired half-edges lie at the same
source vertex; the resulting multigraph is loopless. Every source vertex has
degree three. Its incident roots are the three edges of a target triangle and
therefore sum to zero, so the inherited labelling is a root flow. Support
exactness gives used-label graph exactly `J`. ∎

Parallel source edges and disconnected source graphs are allowed, as in the
ambient AffineCDC multigraph convention.

## 3. Which label graphs can occur?

### Corollary 3.1 — triangle-covered realization criterion

A finite graph `J` occurs as the used-label graph of some finite loopless cubic
root flow if and only if every edge of `J` lies in a triangle of `J`.

#### Proof

Necessity follows from the local-triangle description.

For sufficiency, choose for every edge `a\in E(J)` one triangle `T_a` containing
it, and take two copies of every selected triangle. Every target edge then occurs
an even number of times, and every target edge occurs positively because it lies
in its chosen triangle. Apply Theorem 2.1. ∎

The constructed source graph carries a nowhere-zero flow and is therefore
bridgeless on every edge-bearing component.

### Consequence 3.2

Both dense half-cube obstructions

\[
K_6
\qquad\text{and}\qquad
K_8-C_5
\]

are genuine possible used-label graphs of cubic root flows: every edge in either
graph lies in a triangle.

Thus the exact half-cube classification cannot be completed by proving that one
of the two obstruction graphs is locally unrealizable. The remaining difficulty
must use information beyond the used-label graph alone, such as:

- the fixed source graph and its pairing topology;
- the projected Fano flow;
- the Hamming-Lagrangian moduli of root lifts;
- decomposition and gluing constraints.

## 4. The simplicial two-cycle

Let `\Delta_S` be the simplex on vertex set `S`, and work over `F_2`. A root flow
defines the triangle chain

\[
\tau_g:=\sum_{v\in V(G)}[T_v]
\in C_2(\Delta_S;F_2).
\]

### Theorem 4.1 — triangle-cycle identity

One has

\[
\boxed{\partial\tau_g=0.}
\]

Consequently there is a three-chain

\[
\Xi_g\in C_3(\Delta_S;F_2)
\]

such that

\[
\boxed{\tau_g=\partial\Xi_g.}
\]

#### Proof

In `\partial\tau_g`, the coefficient of a target edge `a` is the parity of the
number of local triangles containing `a`. This number is twice the number of
source edges labelled `a`, so it is zero. Thus `\tau_g` is a two-cycle.

The simplex `\Delta_S` is contractible, hence its positive-dimensional reduced
homology vanishes. Therefore every two-cycle is a boundary. ∎

Equivalently, the parity pattern of local root triangles is generated by the
boundaries of target tetrahedra. A tetrahedral boundary consists of the four
triangles on a four-element support-index set.

This does **not** by itself give a deformation of a fixed source root flow: a
valid deformation must also respect the pairing of equal label occurrences and,
for a fixed Fano flow, the moment of every source edge. It does identify the
universal target-side relation among local states.

## 5. Separation of roles

The triangle multidesign picture separates three layers that had previously been
mixed.

1. **Local root geometry:** allowed cubic states are triangles of `K_S`.
2. **Target parity:** the triangle multiset is an even two-cycle, generated
   mod two by tetrahedral boundaries.
3. **Source topology:** equal label occurrences are paired to form the actual
   edges of `G`.

The used-label graph records only which target edges occur. It forgets both the
multiplicity two-cycle and the source pairing. The `K_6` and `K_8-C_5`
classification therefore detects the complete obstruction to one fixed global
target compression, but not the full deformation theory of root flows.

## 6. Strategic consequence

After the exact half-cube classification, the five-support problem may be stated
as follows.

> Choose an AffineCDC root flow so that its paired even triangle multidesign has a
> used-label graph avoiding `K_6` and `K_8-C_5`, or else decompose the source graph
> so that locally compressible target maps glue across the source interfaces.

A target-only argument cannot prove this: Corollary 3.1 realizes both dense
obstructions. The next AffineCDC-specific object is therefore the action of the
Hamming-Lagrangian gauge space on paired triangle multidesigns, not merely on
unpaired label graphs.

The natural elementary moves to investigate are tetrahedral changes of the local
triangle cycle together with the smallest source-pairing changes that realize
them while preserving the projected `F_2^3` flow.
