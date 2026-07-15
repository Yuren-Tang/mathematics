# The rank-four six-vertex dichotomy

**Date:** 2026-07-15  
**Status:** exact finite-field computation and short classification; not yet
Lean-formalized.

This note compares the two connected simple cubic graphs on six vertices. Each
has cycle rank four and therefore carries, up to a coefficient change in
\(\operatorname{GL}(4,2)\), a unique spanning rank-four binary flow. The two
flows have the same index data but opposite affine compatibility behaviour.

---

## 1. The two graphs

If \(G\) is a simple cubic graph on six vertices, then its complement is a
simple two-regular graph on six vertices. Hence the complement is either

\[
C_6
\]

or

\[
C_3\sqcup C_3.
\]

The corresponding cubic graphs are respectively:

1. the triangular prism \(P_3\);
2. \(K_{3,3}\).

Thus these are the only connected simple cubic graphs on six vertices.

Both are bridgeless and have

\[
|E|-|V|+1=9-6+1=4.
\]

A spanning rank-four flow identifies \(\Gamma^*\) with the four-dimensional
cycle space. Therefore it is unique up to \(\operatorname{GL}(\Gamma)\).

---

## 2. The triangular-prism flow

Let

\[
\Gamma=\langle a,b,c,d\rangle.
\]

Use top vertices \(0,1,2\), bottom vertices \(3,4,5\), and vertical edges
\(03,14,25\). A canonical spanning flow is

\[
\begin{array}{c|c}
	ext{edge}&f(e)\\ \hline
01&a+c+d\\
12&a+d\\
20&a\\
34&b+c+d\\
45&b+d\\
53&b\\
03&c+d\\
14&c\\
25&d
\end{array}
\]

At every vertex the three incident values sum to zero, and all nine values are
nonzero.

A direct solution of the affine gluing equation is

\[
\boxed{
\begin{aligned}
m_0&=a+b+c,\\
m_1&=a+b+c+d,\\
m_2&=a+b,\\
m_3&=c,\\
m_4&=c+d,\\
m_5&=0.
\end{aligned}
}
\]

For every edge \(e=uv\), the difference \(m_u+m_v\) represents exactly the
intrinsic edge obstruction class \(c_{f,e}\). Hence

\[
\boxed{[c_f]=0}
\]

for the triangular prism.

A row reduction gives

\[
\dim H^0=4,
\qquad
\dim\operatorname{Stress}=7.
\]

Thus the flow is gauge-rigid and

\[
\dim\operatorname{EssStress}=1.
\]

A representative of the essential class assigns the covector \(b^*\) to all
three top-triangle edges and zero to the other six edges. It is a stress because
\(b^*\) annihilates all top-triangle flow values and occurs twice at each top
vertex.

At every vertex its local residue is zero: the nonzero local pattern is always
\((b^*,b^*,0)\), never a hidden dual Fano line.

---

## 3. The \(K_{3,3}\) flow

For \(K_{3,3}\), arrange the edge labels as

\[
F=
\begin{pmatrix}
a&b&a+b\\
c&d&c+d\\
a+c&b+d&a+b+c+d
\end{pmatrix}.
\]

Again the flow is spanning and gauge-rigid, with

\[
\dim\operatorname{EssStress}=1.
\]

A representative of the essential class is

\[
\Psi=
\begin{pmatrix}
b^*&a^*&a^*+b^*\\
b^*&a^*&a^*+b^*\\
0&0&0
\end{pmatrix}.
\]

Its six local residue bits have parity one. Therefore

\[
\Psi(c_f)=1
\]

and

\[
\boxed{[c_f]\ne0.}
\]

Thus the canonical rank-four flow on \(K_{3,3}\) is incompatible.

---

## 4. Dichotomy theorem

### Theorem

For connected simple cubic graphs on six vertices equipped with their canonical
spanning rank-four binary flows:

\[
\boxed{
\begin{array}{c|c|c|c}
G&\dim\mathcal B_f&\dim\operatorname{EssStress}(f)&[c_f]\\ \hline
\text{triangular prism}&0&1&0\\
K_{3,3}&0&1&\ne0
\end{array}
}
\]

Hence neither gauge rigidity nor the dimension of the essential-stress space
determines compatibility. The distinction is exactly the dual-Fano residue
character on the unique essential direction.

---

## 5. Structural meaning

The prism essential stress is supported on a triangle and has even local
support degree at every vertex. It represents a genuine essential deformation
but carries no residue.

The \(K_{3,3}\) essential stress contains one vertex at which the three incident
covectors fill the annihilator plane. This single hidden dual Fano line produces
the nonzero affine obstruction.

The pair is therefore the smallest concrete demonstration that

\[
\boxed{
\text{essential stress}
\not\Rightarrow
\text{incompatibility},
}
\]

while

\[
\boxed{
\text{odd dual-Fano residue parity}
\Longleftrightarrow
\text{incompatibility}.
}
\]
