# Fixed-flow five-support reduction and the cube obstruction

**Programme:** `AffineCDC — Research Lead`  
**Base:** `749e0579581fcc838685138b3582f4de306b8e72`  
**Status:** theorem-level research checkpoint; not canonical pending review  
**Scope:** fixed nowhere-zero `F₂³`-flow and the eight indexed affine supports

## 1. Scope and convention

Let `Γ = F₂³`, let `G` be a finite cubic loopless multigraph, and let

\[
f:E(G)\to\Gamma\setminus\{0\}
\]

be a nowhere-zero flow. At every vertex `v`, the three incident values are the
nonzero elements of a plane

\[
U_v\leq\Gamma.
\]

A compatible affine family gives eight indexed even supports

\[
(F_s)_{s\in\Gamma},
\]

with every edge in exactly two supports. The question studied here is whether a
compatible family may be chosen with at most five nonempty `F_s`.

On a cubic graph each `F_s` is a 2-regular subgraph. Thus this is the natural
five-even-subgraph or five-support version of `5-CDC`. It should not be confused
with requiring at most five inclusion-minimal circuits after the project's final
circuit decomposition; decomposition does not preserve the number five.

## 2. Local triangles

For a plane `U ≤ Γ`, put `D = U \ {0}`. A local affine family at a vertex with
flow plane `U` is parametrized by `m ∈ Γ`. Its three edge-pairs are the edges of
the affine triangle

\[
\Delta(U,m):=m+D.
\]

Indeed, if `D={h_1,h_2,h_3}` and `h_1+h_2+h_3=0`, then the pair attached to
`h_1` is

\[
\{m+h_2,m+h_3\},
\]

and cyclically. Compatibility across an edge of value `h` means that the same
`h`-pair is selected at its two ends.

Consequently, three indices are absent from all eight indexed supports exactly
when there is a compatible choice of local triangles avoiding a fixed
three-point set `T ⊂ Γ`.

## 3. The fixed-three-point local reduction

Fix a three-point set

\[
T=\{t_0,t_1,t_2\}\subset\Gamma.
\]

Its affine span is the four-point plane

\[
A=r+W,
\qquad
r:=t_0+t_1+t_2,
\qquad
W:=\langle t_1+t_0,t_2+t_0\rangle,
\]

so `T=A\{r}`. Let `C` be the other affine `W`-coset. Thus

\[
\Gamma\setminus T=\{r\}\sqcup C,
\qquad |C|=4.
\]

### Theorem 3.1 — local forbidden-triple classification

Let `U ≤ Γ` be a plane.

1. If `U=W`, the `T`-avoiding local triangles are exactly

   \[
   C\setminus\{p\},
   \qquad p\in C.
   \]

   Hence there are four choices.

2. If `U\neq W`, let

   \[
   U\cap W=\langle h\rangle,
   \qquad h\neq0.
   \]

   There is exactly one `T`-avoiding local triangle, namely

   \[
   (r+U)\setminus\{r+h\}.
   \]

#### Proof

Every local triangle is an affine `U`-plane with one point omitted. If `U=W`,
the two affine `U`-planes are `A` and `C`. Omitting one point from `A` cannot
remove all three points of `T`, while omitting any point from `C` works.

If `U\neq W`, each affine `U`-plane meets `A` in a two-point affine line. Of the
two `U`-cosets, exactly one intersection line contains `r`; it is `r+U`, and its
intersection with `A` is `{r,r+h}`. Omitting `r+h` gives the unique triangle
whose other three points avoid `T`. ∎

## 4. The plane subgraph and its boundary bits

For a plane `W`, define

\[
G_W:=(V(G),\{e:f(e)\in W\}).
\]

At a vertex `v`,

\[
\deg_{G_W}(v)=
\begin{cases}
3,&U_v=W,\\
1,&U_v\neq W.
\end{cases}
\]

Thus every non-isolated vertex of `G_W` has degree one or three.

If `f(e)=h\notin W`, Theorem 3.1 forces the same edge-pair

\[
\{r,r+h\}
\]

at both ends, so such edges are automatically compatible. Only the edges of
`G_W` remain.

Choose `a∉W`. For every nonzero `h∈W`, let

\[
\ell_h:W\to\mathbf F_2
\]

be the unique nonzero functional with kernel `⟨h⟩`.

At a degree-three vertex, write its free state as

\[
p_v=r+a+x_v\in C,
\qquad x_v\in W.
\]

For an incident edge of value `h`, the selected `h`-pair is determined by the
bit `\ell_h(x_v)`; using the complementary pair merely changes all conventions
coherently. If the three incident values are `h_1,h_2,h_3`, then

\[
\ell_{h_1}+\ell_{h_2}+\ell_{h_3}=0,
\]

and therefore the three incident bits have even parity.

At a degree-one vertex `v`, let `h` be its unique incident value in `W` and
choose either `g_v∈U_v\setminus W`. The unique local triangle prescribes the
boundary bit

\[
\beta_W(v):=1+\ell_h(g_v+a).
\]

This is independent of the choice of `g_v`, since the two possible choices
differ by `h`.

For a connected component `K` of `G_W`, define

\[
\Omega_W(K):=
\sum_{\substack{v\in V(K)\\\deg_{G_W}(v)=1}}
\beta_W(v)
\in\mathbf F_2.
\]

Changing `a` changes each boundary bit of colour `h` by `\ell_h(w)` for a fixed
`w∈W`. In a degree-one/degree-three component, the numbers of leaves of the
three colours have the same parity. Hence `\Omega_W(K)` is independent of `a`.
The formula is also independent of the missing point `r`; for fixed `W`, all
eight forbidden triples have the same obstruction.

### Theorem 4.1 — fixed-three-colour criterion

For a fixed three-point set `T` with direction plane `W`, a compatible affine
family avoiding `T` exists if and only if

\[
\boxed{
\Omega_W(K)=0
\quad\text{for every connected component }K\text{ of }G_W.
}
\]

#### Proof

Assign one bit to every edge of `G_W`. At a degree-three vertex the three bits
must have even parity, and at a degree-one vertex the incident bit is fixed to
`\beta_W(v)`. The edge bit is shared by its two endpoints.

Summing the degree-three parity equations over a component cancels every
internal edge twice and leaves the sum of the prescribed leaf bits. Thus
`\Omega_W(K)=0` is necessary.

It is sufficient as well. If the component has degree-three vertices, remove
its leaves and solve the binary incidence equations on the connected internal
subgraph; the image of its incidence map is exactly the even-sum vertex
vectors. If the component is a single edge joining two leaves, the condition is
precisely equality of the two prescribed endpoint bits. The resulting edge bits
recover the states `x_v∈W` at every degree-three vertex because the map

\[
x\longmapsto
(\ell_{h_1}(x),\ell_{h_2}(x),\ell_{h_3}(x))
\]

identifies `W` with the even-parity subspace of `F₂³`. ∎

### Corollary 4.2 — fixed-flow five-support criterion

The fixed flow `f` admits a compatible affine family with at most five nonempty
indexed supports if and only if there is a plane `W≤Γ` for which every component
of `G_W` has zero obstruction.

The criterion depends on the direction `W`, not on the particular forbidden
triple of that direction.

## 5. A cube flow obstructing every plane

Represent the nonzero vectors of `Γ` by the integers `1,…,7`, with addition
written as bitwise xor. Let `G` be the cube with edge set

\[
\begin{aligned}
&01,03,04,12,17,23,26,35,45,47,56,67.
\end{aligned}
\]

Define the nowhere-zero flow by

| edge | value | edge | value |
|---|---:|---|---:|
| `01` | `5` | `03` | `2` |
| `04` | `7` | `12` | `7` |
| `17` | `2` | `23` | `1` |
| `26` | `6` | `35` | `3` |
| `45` | `1` | `47` | `6` |
| `56` | `2` | `67` | `4` |

The local flow planes are

\[
\begin{array}{c|c}
\text{vertices}&U_v\\\hline
0,1&\{2,5,7\}\\
2,4&\{1,6,7\}\\
3,5&\{1,2,3\}\\
6,7&\{2,4,6\}.
\end{array}
\]

Flow conservation is immediate from the xor-zero condition in each row.

For the seven planes, the following table gives one component with nonzero
obstruction:

| `W\setminus{0}` | obstructed component |
|---|---|
| `{1,2,3}` | `{0,2,3,4,5,6}` |
| `{1,4,5}` | `{2,3}` |
| `{1,6,7}` | `{0,4,5,7}` |
| `{2,4,6}` | `{0,3}` |
| `{2,5,7}` | `{0,1,2,3,4,7}` |
| `{3,4,7}` | `{0,4}` |
| `{3,5,6}` | `{2,6}` |

In every listed component, `\Omega_W=1`. Therefore no three indices can be
simultaneously absent from a compatible affine family for this fixed flow.
Every compatible family uses at least six indices.

The bound six is attained. One compatible family has local triangles

\[
\begin{array}{c|c}
v&\Delta_v\\\hline
0&\{2,5,7\}\\
1&\{0,2,7\}\\
2&\{0,6,7\}\\
3&\{5,6,7\}\\
4&\{2,4,5\}\\
5&\{4,5,6\}\\
6&\{0,4,6\}\\
7&\{0,2,4\}.
\end{array}
\]

The six nonempty supports are indexed by

\[
0,2,4,5,6,7
\]

and are exactly the six square faces of the cube:

\[
\begin{array}{c|l}
0&12,17,26,67\\
2&01,04,17,47\\
4&45,47,56,67\\
5&03,04,35,45\\
6&23,26,35,56\\
7&01,03,12,23.
\end{array}
\]

Hence the minimum number of nonempty indexed supports for this fixed flow is
exactly six.

### Consequence

The following tempting strengthening is false:

> Every fixed nowhere-zero `F₂³`-flow has a compatible affine family using at
> most five indexed supports.

This is not a counterexample to `5-CDCC`. The cube has other flows, and the
five-support problem for a graph allows the flow and compatible family to be
chosen jointly.

## 6. Correct next problem

The natural AffineCDC strengthening is now:

> Does every bridgeless cubic graph admit **some** nowhere-zero `F₂³`-flow `f`
> and some compatible affine family for `f` with at most five nonempty indexed
> supports?

Equivalently, can one choose `f` so that the fixed-flow criterion of Corollary
4.2 succeeds for at least one plane `W`?

This is a joint flow-and-gauge optimization problem. The cube example shows
that gauge motion inside the solution torsor cannot replace flow selection.

## 7. Reliability and promotion boundary

- The local forbidden-triple classification and component-parity criterion are
  elementary paper proofs.
- The cube is a finite explicit certificate; every table entry is directly
  checkable from the displayed flow.
- A separate exhaustive check of the eight local states at each cube vertex
  confirms that the compatible-family torsor has eight elements and every one
  uses exactly six indices, but that enumeration is not needed for the stated
  obstruction proof.
- No canonical file, Lean file, frozen dossier, public theorem, or engineering
  contract is changed here.
- Canonical promotion requires review, especially of the relation between the
  five-support convention here and external formulations of `5-CDC`.