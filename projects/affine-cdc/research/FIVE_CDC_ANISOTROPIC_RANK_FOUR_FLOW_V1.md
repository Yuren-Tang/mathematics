# Five-support double covers as anisotropic rank-four flows

**Programme:** `AffineCDC — Research Lead`  
**Status:** theorem-level research checkpoint; not canonical pending review  
**Literature boundary:** the formulation may have classical equivalents in the
5-CDC, Petersen-colouring, or normal-colouring literature; no novelty claim is
made before a dedicated source audit.

## 1. The canonical five-coordinate quadratic space

Let

\[
H_5:=\left\{s=(s_1,\dots,s_5)\in\mathbf F_2^5:
\sum_{i=1}^5s_i=0\right\}.
\]

This is a four-dimensional vector space. Define

\[
q_5(s):=\sum_{1\le i<j\le5}s_is_j.
\]

For `s∈H_5`, the Hamming weight is even, hence is `0`, `2`, or `4`, and

\[
q_5(s)=\binom{\operatorname{wt}(s)}2\pmod2.
\]

Therefore

\[
\boxed{
q_5(s)=1
\iff
\operatorname{wt}(s)=2.
}
\]

The polar form is

\[
B_5(s,t)
=q_5(s+t)+q_5(s)+q_5(t)
=\sum_{i=1}^5s_it_i
\qquad(s,t\in H_5).
\]

The standard dot product is nondegenerate on `H_5`, because its orthogonal
complement in `F₂⁵` is spanned by the all-one vector, which does not belong to
`H_5`. Hence `(H_5,q_5)` is a nondegenerate four-dimensional quadratic space.

It has ten anisotropic vectors, namely the ten weight-two vectors, and five
nonzero singular vectors, namely the five weight-four vectors. Thus it is the
minus-type, or Arf-one, quadratic four-space.

The anisotropic vectors are canonically identified with the edges of `K_5`: a
weight-two vector records a two-element subset of a five-element set.

## 2. Anisotropic-flow equivalence

Let `G` be a finite loopless multigraph. An `H_5`-valued flow is an edge map

\[
g:E(G)\to H_5
\]

whose incident values sum to zero at every vertex.

### Theorem 2.1 — anisotropic-flow characterization

The following are equivalent.

1. `G` has a double cover by five even edge supports

   \[
   F_1,\dots,F_5.
   \]

2. `G` has an `H_5`-valued flow `g` satisfying

   \[
   \boxed{q_5(g(e))=1\quad\text{for every edge }e.}
   \]

#### Proof

Given five even supports, define

\[
g(e):=(\mathbf1_{e\in F_1},\dots,\mathbf1_{e\in F_5}).
\]

Every coordinate is an even support, so `g` satisfies the flow equation.
Every edge occurs in exactly two supports, so `g(e)` has weight two and hence is
anisotropic.

Conversely, let `g` be anisotropic on every edge. Since `g(e)∈H_5` and
`q_5(g(e))=1`, every edge value has weight exactly two. For each coordinate `i`,
let

\[
F_i:=\{e:g_i(e)=1\}.
\]

The coordinate flow equation makes every `F_i` even, and weight two gives exact
double coverage. ∎

Thus the five-support conjecture is exactly an anisotropic-flow existence
problem in a fixed rank-four quadratic space.

## 3. Cubic local geometry

Assume now that `G` is cubic. At a vertex with incident edges `e_1,e_2,e_3`,
flow conservation gives

\[
g(e_1)+g(e_2)+g(e_3)=0.
\]

Each value is a weight-two vector, hence an edge of `K_5`. Three distinct edges
of `K_5` sum to zero exactly when they are the three edges of a triangle.
Indeed, if two weight-two vectors share one coordinate, their sum is the
weight-two vector joining the other two coordinates; disjoint pairs sum to a
weight-four singular vector.

Therefore:

\[
\boxed{
\text{at every cubic vertex, the three }K_5\text{-edge labels form a triangle.}
}
\]

Equivalently, three of the five cover supports are locally active, each on two
of the three incident graph edges.

There are

\[
\binom53\cdot3!=60
\]

labelled local states: choose the active triangle of support indices and assign
its three edges to the three incident graph edges.

## 4. Linear coordinates and the quadratic cycle equation

Define a linear isomorphism

\[
\Phi:\mathbf F_2^4\longrightarrow H_5
\]

by

\[
\boxed{
\Phi(b,d,x,y)
=
\bigl(
 b,
 d,
 b+d+y,
 b+d+x,
 b+d+x+y
\bigr).
}
\]

The coordinate sum is zero, and the map is visibly injective, hence is an
isomorphism.

A direct calculation gives

\[
\boxed{
q_5(\Phi(b,d,x,y))
=bd+x+y+xy.
}
\]

Consequently the anisotropic condition `q_5=1` is exactly

\[
\boxed{
bd=(1+x)(1+y).}
\]

This recovers the quadratic cycle-code equation from
`FIVE_CDC_QUADRATIC_CYCLE_EQUATION_V1.md`.

Under `\Phi`, the five coordinate supports are

\[
\boxed{
F_0=b,
\quad
F_a=d,
\quad
F_{a+e_1}=b+d+y,
\quad
F_{a+e_2}=b+d+x,
\quad
F_{a+e_1+e_2}=b+d+x+y.
}
\]

Thus the five supports are linear combinations of the four cycle variables;
the sole nonlinear condition is that every edge value land on the anisotropic
quadric rather than at a singular or zero vector.

## 5. Direct local meaning of the quadratic equation

For arbitrary bits `(b,d,x,y)`, the five-vector `\Phi(b,d,x,y)` always has even
weight. It has:

- weight `2` for the ten states satisfying `bd=(1+x)(1+y)`;
- weight `0` for one exceptional state;
- weight `4` for the other five exceptional states.

Hence the quadratic equation is precisely the pointwise statement that the
five cover indicators have weight two. It is not an auxiliary matching
condition imposed after the fact; it is the canonical quadratic equation of the
five-support alphabet.

At a cubic vertex, requiring the four variables to be cycle words leaves exactly
sixty local quadruples, matching the sixty labelled `K_5`-triangle states above.

## 6. Relation to AffineCDC rank three

The ordinary AffineCDC core starts from a nowhere-zero flow in

\[
\Gamma=\mathbf F_2^3
\]

and proves automatic compatibility by the special rank-three Fano quadratic
geometry.

A five-support witness instead gives an anisotropic flow in the rank-four
quadratic space `(H_5,q_5)`. The projection

\[
\pi:H_5\to\mathbf F_2^3,
\qquad
\pi\Phi(b,d,x,y)=(b,x,y),
\]

forgets the distinguished-support coordinate `d`. Its kernel is one-dimensional.
The equation `q_5=1` determines whether an edgewise lift of a rank-three flow can
remain on the anisotropic quadric while satisfying the global flow equations.

Thus five-support existence may be viewed as a rank-four anisotropic lifting
problem over a rank-three Fano flow.

This places the problem exactly at the first higher-rank layer where the
project's general rank hierarchy ceases to be automatically unobstructed. The
rank-four residue theory and the present anisotropic-flow problem are not yet
identified, but they now occupy the same natural quadratic dimension and should
be compared directly.

## 7. Reformulated conjecture

For bridgeless cubic graphs, the five-support cycle double cover conjecture is
equivalent to:

> Every bridgeless cubic graph admits a flow into the minus-type quadratic
> four-space `(H_5,q_5)` whose value on every edge is anisotropic.

Equivalently, every such graph admits an edge labelling by the ten edges of
`K_5` such that the three labels at every vertex form a triangle of `K_5`.

## 8. Next questions

1. Audit whether this anisotropic-flow formulation is already standard under a
   different name in the 5-CDC or Petersen-colouring literature.
2. Compare the Arf-one space `(H_5,q_5)` with the rank-four Pfaffian residue
   space in the existing AffineCDC hierarchy.
3. Determine whether Seymour's rank-three binary flow can be lifted to an
   anisotropic `H_5`-flow by an obstruction class whose local formula is the
   existing five-support component parity.
4. Study graph sums and cut interfaces directly in the `K_5`-triangle alphabet.
5. Determine whether the orthogonal group `O^-(4,2)` supplies a more natural
   symmetry group for the five-support problem than the chosen
   matching/four-flow coordinates.