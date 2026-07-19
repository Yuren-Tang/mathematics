# Five-support affine covers, matchings, and nowhere-zero four-flows

**Programme:** `AffineCDC — Research Lead`  
**Status:** theorem-level research checkpoint; not canonical pending review  
**Literature boundary:** this appears to recover a classical type of `5-CDC`
characterization; exact attribution and convention matching remain to be audited
before canonical promotion.

## 1. Conventions

A **five-support double cover** of a cubic loopless multigraph is a list of five
possibly empty even edge supports in which every edge occurs exactly twice.
Each support is a 2-regular subgraph, possibly disconnected. The five entries are
occurrences, so repeated underlying supports remain distinct entries.

This is the `k`-even-subgraph convention for `5-CDC`. It is not a claim that the
cover decomposes into at most five inclusion-minimal circuits.

Let

\[
\Gamma=\mathbf F_2^3,
\qquad
W\leq\Gamma,
\quad \dim W=2,
\qquad
a\in\Gamma\setminus W.
\]

Every `Γ`-valued flow has a unique decomposition

\[
\boxed{
f=w+b\,a,
}
\]

where

\[
w:E(G)\to W,
\qquad
b:E(G)\to\mathbf F_2
\]

are flows. The binary flow `b` records whether `f(e)` lies outside `W`.

## 2. The projected zero set is a matching

Assume `f` is nowhere zero and `G` is cubic. Put

\[
B:=\operatorname{supp}b,
\qquad
M:=\{e:w(e)=0\}.
\]

### Proposition 2.1

One has

1. `B` is an even edge support;
2. `M⊆B`;
3. `M` is a matching;
4. the restriction of `w` to `G-M` is a nowhere-zero `W`-flow.

#### Proof

The support of a binary flow is even, giving (1). If `b(e)=0`, then `f(e)=w(e)`;
nowhere-zeroness of `f` gives `w(e)≠0`, so `M⊆B`.

At a cubic vertex, the binary flow `b` has either zero or two incident `1`-edges.
In the second case, if the two corresponding `w`-values were both zero, the
third `w`-value would also be zero by flow conservation, contradicting
nowhere-zeroness on the third edge, which is outside `B`. Hence at most one
incident edge belongs to `M`, so `M` is a matching.

Deleting zero-valued edges does not alter the flow equations. Every remaining
edge has nonzero `w`-value, proving (4). ∎

Thus every choice of a plane quotient of a nowhere-zero `F₂³`-flow produces a
matching whose deletion carries a nowhere-zero `F₂²`-flow.

## 3. What a five-support affine family produces

Translate the support indices so that the three forbidden points are

\[
W\setminus\{0\}.
\]

The five allowed indices are then

\[
\{0\}\sqcup(a+W).
\]

Let `(F_s)` be a compatible affine family using only these five indices.

### Theorem 3.1 — distinguished supports

With `f=w+ba` as above,

\[
\boxed{
F_0=B.
}
\]

Moreover,

\[
\boxed{
F_0\cap F_a=M.
}
\]

#### Proof

If `b(e)=0`, then `f(e)∈W`; the two support indices of `e` lie in the same
`W`-coset. Since the local triangles avoid `W\setminus\{0\}`, the pair lies in
`a+W`, and `0` is not one of its indices.

If `b(e)=1`, then `f(e)∉W`. The fixed-forbidden-triple local classification
forces the pair

\[
\{0,f(e)\}=
\{0,a+w(e)\}.
\]

Therefore `e∈F_0` exactly when `b(e)=1`, proving `F_0=B`. Among those edges, the
second index is `a` exactly when `w(e)=0`. Hence

\[
F_0\cap F_a
=
\{e:b(e)=1,\ w(e)=0\}
=M.
\]

∎

Since every `F_s` is even, a five-support affine family therefore yields:

- two even supports `F_0` and `F_a`;
- their intersection `M`, which is a matching;
- a nowhere-zero `F₂²`-flow on `G-M`.

## 4. Converse construction

### Theorem 4.1 — matching/four-flow reconstruction

Suppose there are even edge supports `B,D⊆E(G)` such that

\[
M:=B\cap D
\]

is a matching, and suppose `G-M` carries a nowhere-zero `W`-flow

\[
w:E(G-M)\to W\setminus\{0\}.
\]

Extend `w` by zero on `M`, put

\[
b:=\mathbf1_B,
\qquad
f:=w+b\,a.
\]

Then:

1. `f` is a nowhere-zero `Γ`-flow;
2. there is a compatible affine family using only the five indices
   `\{0\}\sqcup(a+W)`;
3. its distinguished supports satisfy

   \[
   F_0=B,
   \qquad
   F_a=D.
   \]

#### Proof

Because `B` is even, `b` is a binary flow. The extension of `w` is still a
`W`-flow, so `f` is a `Γ`-flow.

If `e∉B`, then `e∉M` and `f(e)=w(e)≠0`. If `e∈B`, then the `a`-coordinate of
`f(e)` is one, so `f(e)≠0`. Thus `f` is nowhere zero.

We now choose the local triangles. At a vertex where no incident edge lies in
`B`, the three flow values lie in `W`. Membership of the three incident edges in
`D` has even parity because `D` is even. The four even subsets of the three
incident edges are exactly the four local triangles contained in `a+W`,
classified by whether their selected edge-pairs contain the index `a`.

At a vertex incident with two edges of `B`, the third edge is outside `B`. The
matching condition says at most one of the two `B`-edges lies in `M`. On a
`B`-edge, the forced outside pair contains `a` exactly when `w(e)=0`, that is,
exactly when `e∈M=B∩D`. Since `D` is even, its membership on the third edge is
then forced. This is precisely the unique local triangle avoiding
`W\setminus\{0\}` from the fixed-forbidden-triple classification.

The local choices agree on every edge by construction, hence form a compatible
family. An edge lies in `F_0` exactly when it lies in `B`, and it lies in `F_a`
exactly when it lies in `D`. ∎

## 5. Exact equivalence

### Corollary 5.1

For a finite cubic loopless multigraph `G`, the following are equivalent.

1. `G` has a five-support double cover.
2. There exist a nowhere-zero `F₂³`-flow `f`, a plane `W`, and a compatible
   affine family for `f` using at most five indices.
3. There exist even supports `B,D` such that `M=B∩D` is a matching and `G-M`
   has a nowhere-zero `F₂²`-flow.

#### Proof

`(2)⇒(3)` is Theorem 3.1 and Proposition 2.1. `(3)⇒(2)` is Theorem 4.1.

For `(1)⇒(2)`, label the five support occurrences by the five points
`\{0\}\sqcup(a+W)`. Every edge belongs to exactly two labelled supports; define
its flow value as the difference of those two labels. At a cubic vertex, every
support has local degree zero or two, and the total support incidence is six.
Thus exactly three support labels occur locally, each twice, and the three edge
pairs are the edges of their affine triangle. The resulting values are nonzero,
sum to zero, and the labelled supports are a compatible affine family.

Finally `(2)⇒(1)` forgets the unused three indices. ∎

## 6. Relation to the colour-cut obstruction

For `f=w+ba`, the graph `G_W` is `G-B`. The zero matching is `M=B∩F_a`.
The fixed-plane component obstruction has the following equivalent form:

\[
\boxed{
\text{every component of }G-B
\text{ is incident with an even number of edges of }M.
}
\]

Indeed, the colour-cut formula may be evaluated at the outside colour `a`; its
edges are exactly `M`. This condition is precisely what allows the endpoints of
`M` to be joined inside the components of `G-B` so as to form an even support
`D` with `B∩D=M`.

Thus the affine boundary obstruction, the existence of the second distinguished
even support, and the matching/four-flow condition are the same object at three
resolutions.

## 7. Consequences for strategy

The affine five-support problem is not solved merely by the rank-three
compatibility theorem. The compatibility theorem supplies an eight-support
double cover for every fixed Fano flow, while the five-support strengthening is
exactly the additional problem of arranging:

- a projected zero matching `M`;
- a nowhere-zero four-flow on `G-M`;
- two even supports intersecting exactly in `M`.

The cube fixed-flow obstruction shows that motion inside one compatible-family
torsor may fail. Any proof of the graph-level five-support conjecture through
AffineCDC must also control the choice of flow, equivalently the pair `(B,w)`.

The most promising next use of the affine language is therefore not to restate
the matching/four-flow condition, but to study how its component obstruction
changes under elementary flow switches.