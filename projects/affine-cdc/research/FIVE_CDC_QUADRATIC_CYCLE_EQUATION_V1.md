# A quadratic cycle-code equation for five-support double covers

**Programme:** `AffineCDC — Research Lead`  
**Status:** theorem-level research checkpoint; not canonical pending review

## 1. Statement

Let `G` be a finite cubic loopless multigraph and let

\[
\mathcal C(G)\subseteq\mathbf F_2^{E(G)}
\]

be its binary cycle space. Write `\mathbf1` for the all-edge word and use `*` for
coordinatewise multiplication.

### Theorem 1.1 — quadratic cycle equation

The following are equivalent.

1. `G` has a five-support double cover.
2. There exist four binary cycle words

   \[
   b,d,x,y\in\mathcal C(G)
   \]

   satisfying the edgewise quadratic equation

   \[
   \boxed{
   b*d=(\mathbf1+x)*(\mathbf1+y).
   }
   \]

Equivalently,

\[
\boxed{
\mathbf1+x+y+x*y+b*d=0.
}
\]

No separate nowhere-zero condition is required in item 2.

## 2. Proof

Assume first that `G` has a five-support double cover. By the
matching/four-flow characterization developed in
`FIVE_CDC_MATCHING_FOUR_FLOW_BRIDGE_V1.md`, there are even supports `B,D` such
that

\[
M:=B\cap D
\]

is a matching and `G-M` carries a nowhere-zero `F₂²`-flow

\[
w=(x,y).
\]

Extend `w` by zero on `M`, and let `b,d` be the indicator words of `B,D`.
All four words lie in `\mathcal C(G)`. Edgewise,

\[
(\mathbf1+x_e)(\mathbf1+y_e)=1
\]

exactly when `x_e=y_e=0`, that is, exactly when `e∈M`. Also

\[
b_ed_e=1
\]

exactly when `e∈B\cap D=M`. Hence

\[
b*d=(\mathbf1+x)*(\mathbf1+y).
\]

Conversely, suppose `b,d,x,y∈\mathcal C(G)` satisfy the equation. Put

\[
M:=\{e:x_e=y_e=0\}.
\]

The right side is the indicator word of `M`, so the equation gives

\[
M=\operatorname{supp}b\cap\operatorname{supp}d.
\]

Define the rank-three flow

\[
f=(b,x,y).
\]

It is automatically nowhere zero. Indeed, if

\[
b_e=x_e=y_e=0,
\]

then the left side `b_ed_e` is zero while the right side
`(1+x_e)(1+y_e)` is one, contradicting the equation.

Because `G` is cubic, the zero set of the projected `F₂²`-flow `(x,y)` in a
nowhere-zero rank-three flow is a matching. Thus `M` is a matching. On `G-M`,
`(x,y)` is a nowhere-zero `F₂²`-flow. The supports of `b` and `d` are even and
intersect exactly in `M`. The matching/four-flow reconstruction theorem now
produces a five-support double cover. ∎

## 3. Linear slices of the quadratic equation

The equation is quadratic globally but linear in each variable after the other
three are fixed.

Fix `b,x,y` and put

\[
m:=(\mathbf1+x)*(\mathbf1+y).
\]

Then solving for `d∈\mathcal C(G)` means

\[
\boxed{
b*d=m.}
\]

The equation prescribes `d=1` on the projected zero matching `M`, prescribes
`d=0` on `\operatorname{supp}b\setminus M`, and leaves `d` free outside
`\operatorname{supp}b`. A cycle completion exists exactly when every connected
component of `G-\operatorname{supp}b` is incident with an even number of edges of
`M`. This is the colour-cut and Schur-quotient obstruction in its simplest
linear-extension form.

Similarly, fixing `d,x,y` makes the equation linear in `b`. Fixing `b,d,y`
makes it an affine linear equation in `x`, subject to `x∈\mathcal C(G)`, and
likewise for `y`.

Thus the internal/external switch dichotomy consists of moving along different
linear slices of one quadratic cycle variety.

## 4. Symmetries

The equation has the evident symmetries

\[
b\leftrightarrow d,
\qquad
x\leftrightarrow y.
\]

The first exchanges the two distinguished even supports. The second changes the
basis of the projected `F₂²`-flow. Replacing `y` by `x+y` produces an equivalent
coordinate description after the corresponding relabelling of the five support
indices.

The factorized form

\[
b*d=(\mathbf1+x)*(\mathbf1+y)
\]

exhibits the five-support condition as equality between

- the intersection of two even subgraphs; and
- the common zero set of two binary flows.

This is the algebraic content of the matching/four-flow bridge.

## 5. Odd-subgraph form

Put

\[
r:=\mathbf1+x,
\qquad
s:=\mathbf1+y.
\]

Since `G` is cubic and `x,y` are even supports, `r,s` have odd degree at every
vertex. The equation becomes

\[
\boxed{
b*d=r*s.}
\]

Hence a five-support cover is equivalently a pair of even subgraphs and a pair
of everywhere-odd subgraphs having the same edgewise intersection.

This form may be useful for matching and parity arguments: in a cubic graph an
everywhere-odd subgraph has local degree one or three.

## 6. Code-theoretic position

Let `C=\mathcal C(G)`. Define the quadratic solution set

\[
\mathfrak V_5(G)
:=
\{(b,d,x,y)\in C^4:
 b*d=(\mathbf1+x)*(\mathbf1+y)\}.
\]

Then

\[
\boxed{
G\text{ has a five-support double cover}
\iff
\mathfrak V_5(G)\neq\varnothing.
}
\]

The Cycle Double Cover theorem corresponds to unconditional existence of an
eight-index affine cover. The five-support strengthening asks for a point on the
much smaller quadratic cycle variety `\mathfrak V_5(G)`.

The single-switch correction codes are tangent-direction images of this
quadratic equation along selected linear slices. Two independent coordinate
switches reveal the bilinear second-order term, which is the polarization of the
Schur product in the defining equation.

## 7. Next questions

1. Determine the tangent and second-order obstruction spaces of
   `\mathfrak V_5(G)` at a nowhere-zero rank-three flow.
2. Identify whether the equation is naturally a rank-one condition in a quotient
   of the Schur square `C*C`.
3. Compare `\mathfrak V_5(G)` with classical matching/four-flow and 5-CDC
   varieties in the literature.
4. Find graph operations under which nonemptiness of `\mathfrak V_5(G)` is
   preserved or glued from smaller pieces.