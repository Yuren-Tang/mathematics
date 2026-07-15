# The canonical rank-four \(K_{3,3}\) residue example

**Date:** 2026-07-15  
**Status:** exact finite-field computation; theorem-level example draft, not yet Lean-formalized.

This note computes the smallest gauge-rigid rank-four obstruction and shows
that it is detected by exactly one local cubic directional residue.

Let

\[
\Gamma=\mathbf F_2^4
\]

with basis

\[
a,b,c,d
\]

and dual basis

\[
a^*,b^*,c^*,d^*.
\]

Let the bipartition of \(K_{3,3}\) be

\[
L_0,L_1,L_2
\qquad\text{and}\qquad
R_0,R_1,R_2.
\]

---

## 1. The canonical spanning flow

Because the cycle rank of \(K_{3,3}\) is four, every spanning rank-four binary
flow is equivalent under \(\operatorname{GL}(\Gamma)\) to the following one.
Arrange the edge labels in a \(3\times3\) matrix, with rows indexed by the left
vertices and columns by the right vertices:

\[
\boxed{
F=
\begin{pmatrix}
a&b&a+b\\
c&d&c+d\\
a+c&b+d&a+b+c+d
\end{pmatrix}.
}
\]

Every row and every column sums to zero, so this is a flow. All nine labels are
nonzero, and the labels span \(\Gamma\).

A direct row reduction of the homogeneous quotient-sheaf equations gives

\[
\dim H^0(K_{3,3};\mathscr Q_f)=4.
\]

The four-dimensional constant-section space is always contained in \(H^0\),
so equality holds:

\[
H^0(K_{3,3};\mathscr Q_f)=\Gamma.
\]

Hence the reduced gauge code vanishes:

\[
\boxed{\mathcal B_f=0.}
\]

The flow is gauge-rigid.

---

## 2. Stress dimensions

An equilibrium stress is a matrix of covectors \(\psi_{ij}\in\Gamma^*\)
satisfying

\[
\psi_{ij}(F_{ij})=0
\]

and having zero sum in every row and every column.

The explicit linear system has

\[
\dim\operatorname{Stress}(f)=7.
\]

Global alternating two-forms give the canonical six-dimensional subspace

\[
\operatorname{AltStress}(f)
\cong
\Lambda^2\Gamma^*.
\]

Therefore

\[
\boxed{
\dim\operatorname{EssStress}(f)=1.
}
\]

This agrees with the rank-four index formula

\[
\dim\operatorname{EssStress}(f)
=
\dim\mathcal B_f+\frac{|V|-4}{2}
=
0+1.
\]

---

## 3. A generator of the essential stress

A representative of the unique nonzero essential class is

\[
\boxed{
\Psi=
\begin{pmatrix}
b^*&a^*&a^*+b^*\\
b^*&a^*&a^*+b^*\\
0&0&0
\end{pmatrix}.
}
\]

It is an equilibrium stress:

- each entry annihilates the corresponding flow label;
- every row sums to zero;
- every column contains two equal covectors and zero, hence sums to zero.

It is not a global alternating stress. Indeed, a global two-form \(\alpha\)
producing the first row would satisfy

\[
\iota_a\alpha=b^*,
\qquad
\iota_b\alpha=a^*,
\]

so

\[
\alpha(b,c)=0.
\]

Producing the second row would require

\[
\iota_c\alpha=b^*,
\]

so

\[
\alpha(c,b)=1,
\]

contradicting alternating symmetry over \(\mathbf F_2\). Thus \(\Psi\) is
essential.

---

## 4. The six local residues

At a vertex \(v\), let

\[
\beta_v
\]

be the local cross-bit, let

\[
\sigma_v
\]

be the parity of the number of nonzero incident stress covectors, and put

\[
\rho_v=\sigma_v+\beta_v.
\]

For \(\Psi\), the values are:

| vertex | \(\beta_v\) | \(\sigma_v\) | \(\rho_v\) |
|---|---:|---:|---:|
| \(L_0\) | 1 | 1 | 0 |
| \(L_1\) | 0 | 1 | 1 |
| \(L_2\) | 0 | 0 | 0 |
| \(R_0\) | 0 | 0 | 0 |
| \(R_1\) | 0 | 0 | 0 |
| \(R_2\) | 0 | 0 | 0 |

Thus

\[
\boxed{
\sum_v\rho_v=1.
}
\]

The unique essential stress carries an odd cubic residue.

---

## 5. The two nontrivial local two-forms

At \(L_0\), the local configuration is induced by

\[
\alpha_{L_0}=a^*\wedge b^*.
\]

Its restriction to the local flow plane

\[
W_{L_0}=\langle a,b\rangle
\]

is nonzero. Hence

\[
\beta_{L_0}=1,
\qquad
\rho_{L_0}=0.
\]

At \(L_1\), the local configuration is induced by

\[
\alpha_{L_1}
=
b^*\wedge c^*+a^*\wedge d^*.
\]

Its local flow plane is

\[
W_{L_1}=\langle c,d\rangle.
\]

The restriction of \(\alpha_{L_1}\) to \(W_{L_1}\times W_{L_1}\) vanishes, but
the cross-pairing

\[
W_{L_1}\times\Gamma/W_{L_1}\to\mathbf F_2
\]

is perfect. Equivalently,

\[
\operatorname{Pf}(\alpha_{L_1})=1.
\]

Therefore

\[
\beta_{L_1}=0,
\qquad
\rho_{L_1}=1.
\]

This is the unique cubic directional defect.

---

## 6. Incompatibility

The global residue formula gives

\[
\Psi(c_f)
=
\sum_v\rho_v
=1.
\]

Hence \(\Psi\) does not annihilate the affine obstruction. By the dual
solvability criterion,

\[
\boxed{
[c_f]\ne0.
}
\]

Thus the canonical rank-four flow on \(K_{3,3}\) is incompatible.

Since the essential-stress space is one-dimensional, this single residue bit
is the complete obstruction after the canonical alternating stresses have been
removed.

---

## 7. Structural interpretation

The example shows exactly what first fails beyond rank three.

- At each vertex, a legal configuration still comes from a local alternating
  two-form.
- In rank three, those local forms are forced into the Fano quadratic support
  identity, and no residue remains.
- In rank four, neighboring vertices may require local two-forms that cannot be
  restrictions of one global alternating form.
- The first such mismatch is measured by the Pfaffian cubic residue.

For the canonical \(K_{3,3}\) flow, the entire incompatibility is concentrated
at one vertex where the local plane is isotropic but perfectly paired with its
quotient.

Thus the one-dimensional essential obstruction is not merely a dimension
count. It is the parity of a concrete local symplectic-transversality defect.
