# Internal coordinate switches and external reslicing switches

**Programme:** `AffineCDC — Research Lead`  
**Status:** theorem-level research checkpoint; not canonical pending review

## 1. Setup

Let

\[
f:E(G)\to\Gamma=\mathbf F_2^3\setminus\{0\}
\]

be a nowhere-zero flow on a finite cubic loopless multigraph. A colour-cycle
switch in direction `t∈Γ\setminus\{0\}` along a binary cycle `z` is

\[
f'(e)=f(e)+z_e t.
\]

It is admissible exactly when `z` avoids the colour class

\[
f^{-1}(t),
\]

because only an edge already labelled `t` can be sent to zero.

Fix a candidate five-support direction plane

\[
W=\ker b\leq\Gamma.
\]

There are two fundamentally different switch types according to whether `t`
lies in `W`.

## 2. Internal switches

Assume

\[
t\in W.
\]

Choose coordinates

\[
f=(b,x,y)
\]

such that `t` is the `x`-direction in `W`. Then

\[
\boxed{
f'=(b,x+z,y).
}
\]

Thus:

- the plane-membership word `b` is unchanged;
- the subgraph `G_W={b=0}` and quotient `Q_W` are unchanged;
- one `W`-coordinate changes;
- the Schur defect changes linearly by

  \[
  \partial_{Q_W}(y*z).
  \]

The exact admissible image is the fibre syndrome of the bipartite
component-incidence cycle code constructed in
`FIVE_CDC_SWITCH_INCIDENCE_GRAPH_V1.md`.

## 3. External switches

Assume

\[
t\notin W.
\]

Normalize `b(t)=1` and choose two independent functionals `x,y` annihilating
`t`. Then `(b,x,y)` is a dual basis and

\[
\boxed{
f'=(b+z,x,y).
}
\]

Thus:

- the two `W`-coordinates are unchanged;
- the Schur word

  \[
  p:=x*y
  \]

  is unchanged;
- only the plane-membership word changes from `b` to `b+z`;
- the zero subgraph to be contracted changes from `{b=0}` to `{b+z=0}`.

For the fixed target plane `W`, the new defect is therefore

\[
\boxed{
d_W(f')=\partial_{Q_{b+z}}(p).
}
\]

An external switch is a **reslicing operation**: it keeps the quadratic Schur
word fixed and changes the quotient on which that word is required to be a
flow.

## 4. Fixed matching form of external switching

In the external coordinates, put

\[
w=(x,y):E(G)\to W
\]

and

\[
M:=\{e:w(e)=0\}.
\]

Since `f` is nowhere zero,

\[
M=f^{-1}(t)
\]

and `M` is a matching. Moreover, `w` is a nowhere-zero `W`-flow on `G-M`.

Write

\[
B:=\operatorname{supp}b.
\]

Then `B` is an even support containing `M`. An admissible external switch has
`z∈C(G-M)` and replaces `B` by

\[
B':=\operatorname{supp}(b+z).
\]

Conversely, every even support `B'` containing `M` differs from `B` by a binary
cycle avoiding `M`, and hence arises from an admissible external switch.

### Theorem 4.1 — external-switch criterion

An admissible external switch in direction `t` produces a five-support flow for
the target plane `W` if and only if there is an even support

\[
B'\supseteq M
\]

such that every connected component `K` of `G-B'` satisfies

\[
\boxed{
|M\cap\delta_G(K)|\equiv0\pmod2.
}
\]

#### Proof

The admissible-switch parametrization above identifies the possible new
plane-membership words with the binary cycles `b'` satisfying `b'_e=1` on `M`.
For such a word, the colour-cut/Schur criterion computes the obstruction of a
component `K` of `{b'=0}=G-B'` as the parity of the outside colour `t`. Those
edges are exactly the fixed zero matching `M`. Hence the defect vanishes
componentwise exactly under the displayed parity condition. ∎

By the matching/four-flow bridge, the same condition is equivalent to the
existence of a second even support `D` with

\[
B'\cap D=M.
\]

Thus external switching does not change the projected four-flow `w`; it searches
through the affine space of even supports containing its fixed zero matching
until that matching becomes the exact intersection of two even supports.

## 5. The switch dichotomy

Relative to a candidate plane `W`, every Fano colour-cycle switch is exactly one
of the following.

\[
\boxed{
\begin{array}{c|c|c}
& t\in W & t\notin W\\
\hline
\text{operation} & \text{coordinate correction} & \text{quotient reslicing}\\
\text{fixed data} & b,\ Q_W & x,y,\ x*y,\ M\\
\text{variable data} & x\text{ or }y & b,\ G-B\\
\text{criterion} & \text{incidence-cycle syndrome} & \text{matching parity by components}
\end{array}
}
\]

This explains why fixed-plane one-switch failure does not imply global
one-switch failure: an external switch may replace the slicing quotient rather
than correct the defect inside the old quotient.

## 6. Two-switch frontier

A one-switch proof strategy would need either an internal correction for some
plane or an external reslicing that makes some plane good. Finite examples show
that both possibilities can fail simultaneously for every single switch from a
given flow, although two switches may succeed.

The two-switch problem must therefore analyze interactions between the two
modes:

1. internal followed by internal — a bilinear Schur-product term appears;
2. external followed by internal — the quotient is changed before the linear
   correction code is evaluated;
3. external followed by external — both the slicing flow and the fixed zero
   matching presentation may change.

This internal/external normal form is the natural starting point for that
analysis.