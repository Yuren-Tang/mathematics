# The rank-three coincidence principle

**Date:** 2026-07-15  
**Status:** theorem-level structural draft; not yet independently audited or Lean-formalized in this presentation.

This note explains why rank three is the unique place where the local affine geometry, the quotient-sheaf index and the support polynomial all become one quadratic-Lagrangian structure.

Let

\[
\Gamma=\mathbf F_2^r
\]

and let a cubic vertex carry three distinct nonzero flow values

\[
h_1+h_2+h_3=0.
\]

For each incident direction \(h\), put

\[
Q_h=\Gamma/\langle h\rangle.
\]

Then

\[
\dim Q_h=r-1.
\]

---

## 1. The canonical support polynomial

For a binary vector space \(U\) of dimension \(d\), define

\[
\nu_U(u)=
\begin{cases}
0,&u=0,\\
1,&u\ne0.
\end{cases}
\]

Choose coordinates \(u=(x_1,\dots,x_d)\). Then

\[
\boxed{
\nu_U(x)
=
1+\prod_{i=1}^d(1+x_i)
=
\sum_{\varnothing\ne S\subseteq\{1,\dots,d\}}
\prod_{i\in S}x_i.
}
\]

Indeed, the product is one only at the origin and zero elsewhere.

Consequently:

\[
\boxed{
\deg \nu_U=d.
}
\]

This degree is intrinsic, since invertible linear coordinate changes preserve algebraic degree.

The top additive polarization of \(\nu_U\) is the determinant form. More precisely, after choosing a nonzero volume form

\[
\operatorname{vol}\in\Lambda^dU^*,
\]

one has

\[
D_{u_1}\cdots D_{u_d}\nu_U(0)
=
\operatorname{vol}(u_1,\dots,u_d),
\]

where \(D_u f(x)=f(x+u)+f(x)\).

Thus \(\nu_U\) is the canonical degree-\(d\) refinement of the binary volume form.

---

## 2. Applied to edge quotients

For an edge direction \(h\), the support function on

\[
Q_h=\Gamma/\langle h\rangle
\]

has degree

\[
r-1.
\]

Hence:

- \(r=2\): the support function is linear;
- \(r=3\): the support function is quadratic;
- \(r=4\): the support function is cubic;
- in general: it has degree \(r-1\).

Therefore:

\[
\boxed{
r=3
\text{ is the unique nontrivial rank for which the edge support norm is quadratic.}
}
\]

When \(r=3\), its polar form is bilinear and nondegenerate:

\[
B_h([x],[y])
=
\omega(h,x,y),
\]

where \(\omega\in\Lambda^3\Gamma^*\) is the volume form. This produces the quadratic symplectic geometry used by AffineCDC.

When \(r=4\), the first new term is genuinely cubic. Its third polarization is

\[
T_h([x],[y],[z])
=
\Omega(h,x,y,z),
\]

for a volume form \(\Omega\in\Lambda^4\Gamma^*\). There is no bilinear polar form carrying the full support datum, so the quadratic-Lagrangian argument no longer applies.

---

## 3. The local half-dimension equation

At a cubic vertex, define the incidence space

\[
\mathbb E_v
=
Q_{h_1}\oplus Q_{h_2}\oplus Q_{h_3}.
\]

Its dimension is

\[
\dim\mathbb E_v=3(r-1).
\]

The diagonal map

\[
\Delta_v:\Gamma\to\mathbb E_v,
\qquad
x\mapsto([x]_{h_1},[x]_{h_2},[x]_{h_3})
\]

is injective, because the three distinct flow lines have zero common intersection. Hence

\[
\dim\operatorname{im}\Delta_v=r.
\]

For this image to be half-dimensional, one needs

\[
2r=3(r-1).
\]

This has the unique solution

\[
\boxed{r=3.}
\]

Thus rank three is the unique rank in which the local homogeneous family space can be Lagrangian inside the three edge quotients.

For \(r=2\), the incidence space has odd dimension \(3\), so no nondegenerate symplectic structure of this kind is possible.

For \(r>3\), the diagonal image is strictly smaller than half-dimensional.

---

## 4. The global Euler-balance equation

For a cubic graph,

\[
|E|=\frac32|V|.
\]

The quotient-sheaf cochain dimensions are

\[
\dim C_f^0=r|V|
\]

and

\[
\dim C_f^1=(r-1)|E|
=
\frac32(r-1)|V|.
\]

Equality holds exactly when

\[
r=\frac32(r-1),
\]

equivalently

\[
2r=3(r-1).
\]

Again:

\[
\boxed{r=3.}
\]

The sheaf Euler characteristic is

\[
\chi_f
=
\dim C_f^0-\dim C_f^1
=
\frac{3-r}{2}|V|.
\]

Thus:

- rank two has positive index and forced flexibility;
- rank three is balanced;
- rank greater than three has negative index and dimensionally forced obstruction directions.

The local Lagrangian half-dimension equation and the global Euler-balance equation are literally the same equation.

---

## 5. The threefold coincidence

For cubic binary flow geometry, the following are equivalent:

1. the edge-quotient support function is quadratic;
2. the local diagonal family space is half-dimensional;
3. the global quotient-sheaf complex has index zero;
4. the local Fano family space can be a Lagrangian;
5. the global compatibility problem can be expressed as an intersection of two Lagrangians in one nondegenerate quadratic space.

They hold exactly at

\[
\boxed{r=3.}
\]

This is the rank-three coincidence principle.

---

## 6. Why rank four is the first failure layer

At rank four:

- each edge quotient has dimension three;
- its canonical support function is cubic;
- the local incidence space has dimension nine;
- the diagonal local family space has dimension four, not half of nine;
- the global quotient-sheaf index is negative.

Therefore the three mechanisms that force compatibility at rank three all break simultaneously.

This does not merely say that the rank-three proof fails technically. It explains why incompatibility can genuinely occur in rank four: there are new cubic and dimensionally essential obstruction directions that cannot be encoded by a quadratic Lagrangian intersection.

The known rank-four incompatible examples occupy exactly this first post-quadratic layer.

---

## 7. Relation to gauge-code evenness

There is a parallel degree principle on the coefficient space itself.

For \(\Gamma=\mathbf F_2^r\), the nonzero indicator

\[
\nu_\Gamma(a)=\mathbf 1_{a\ne0}
\]

has degree \(r\).

Graph bicycle spaces satisfy linear, pairwise and triple overlap cancellation. Thus they annihilate all polynomial monomials of degree at most three. It follows that the gauge-code parity argument closes for

\[
r\le3,
\]

while rank four introduces a quartic term not controlled by third-order orthogonality.

Hence two sharp rank-three phenomena have the same algebraic source:

- **compatibility:** edge quotient support has degree \(r-1\), which is quadratic only at \(r=3\);
- **gauge evenness:** coefficient support has degree \(r\), which is controlled by third-order orthogonality only for \(r\le3\).

This places the quadratic-Lagrangian compatibility theorem and the even gauge-code theorem in one degree hierarchy.

---

## 8. Structural conclusion

Rank three is not exceptional merely because the Fano plane is visually small. It is the unique solution of three independent-looking requirements:

\[
\boxed{
\begin{aligned}
r-1&=2
&&\text{(quadratic support degree)},\\
r&=\frac12\,3(r-1)
&&\text{(local Lagrangian balance)},\\
r|V|&=(r-1)|E|
&&\text{(global Euler balance)}.
\end{aligned}
}
\]

All three equations say the same thing:

\[
\boxed{r=3.}
\]

The Fano quadratic-Lagrangian package is therefore not an accidental elegant rephrasing. It is the unique balanced quadratic member of a higher-degree rank hierarchy.
