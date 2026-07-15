# Fano quadratic transgression

**Date:** 2026-07-15  
**Status:** theorem-level draft; independently checkable finite geometry, not yet Lean-formalized in this form.

This note isolates the local identity behind the compressed AffineCDC proof and
explains why the relative-quadratic and Fano-cohomological viewpoints meet.

Let

\[
\Gamma=\mathbf F_2^3
\]

and choose the unique nonzero volume form

\[
\omega\in\Lambda^3\Gamma^*.
\]

---

## 1. The canonical quadratic form on a binary plane

Let \(U\) be a two-dimensional \(\mathbf F_2\)-vector space. Define

\[
q_U(u)=
\begin{cases}
0,&u=0,\\
1,&u\ne0.
\end{cases}
\]

Its polarization is

\[
B_U(u,v)=q_U(u+v)+q_U(u)+q_U(v).
\]

If \(u,v\) are dependent, then \(B_U(u,v)=0\). If they are independent, then
\(u,v,u+v\) are the three nonzero elements of \(U\), so

\[
B_U(u,v)=1.
\]

Hence \(B_U\) is the unique nonzero alternating bilinear form on \(U\), and
\(q_U\) is its canonical anisotropic quadratic refinement. No basis or
additional choice is involved.

---

## 2. Quotient quadratics attached to Fano points

For every nonzero \(h\in\Gamma\), put

\[
Q_h=\Gamma/\langle h\rangle.
\]

This is a binary plane, so it carries the canonical quadratic form

\[
q_h:Q_h\to\mathbf F_2,
\qquad
q_h([x])=\mathbf 1_{x\notin\langle h\rangle}.
\]

Its polarization is

\[
\boxed{
B_h([x],[y])=\omega(h,x,y).
}
\]

Indeed, both sides are nonzero exactly when the classes of \(x,y\) are
independent in \(Q_h\).

Thus contraction of the Fano volume form by \(h\) is not merely alternating:
it comes with a canonical quadratic refinement because the quotient has only
three nonzero elements.

---

## 3. The local Fano quadratic identity

Let \(W\le\Gamma\) be a plane. Its three nonzero elements satisfy

\[
\sum_{h\in W\setminus\{0\}}h=0.
\]

Define

\[
L_W(x)=
\sum_{h\in W\setminus\{0\}}q_h([x]).
\]

### Theorem

\[
\boxed{
L_W(x)=
\begin{cases}
0,&x\in W,\\
1,&x\notin W.
\end{cases}
}
\]

Equivalently, if

\[
\ell_W:\Gamma\to\mathbf F_2
\]

is the unique nonzero functional with kernel \(W\), then

\[
\boxed{
\ell_W
=
\sum_{h\in W\setminus\{0\}}
q_h\circ\pi_h,
}
\]

where \(\pi_h:\Gamma\to Q_h\) is the quotient map.

### Conceptual proof

The polarization of \(L_W\) is

\[
\begin{aligned}
B_{L_W}(x,y)
&=
\sum_{h\in W\setminus\{0\}}B_h([x],[y])\\
&=
\sum_{h\in W\setminus\{0\}}\omega(h,x,y)\\
&=
\omega\!\left(\sum_{h\in W\setminus\{0\}}h,x,y\right)\\
&=0.
\end{aligned}
\]

Therefore \(L_W\) is linear, although it is presented as a sum of three
quadratic functions.

For \(x\in W\setminus\{0\}\), exactly one of the three quotient classes
\([x]\in Q_h\) is zero and the other two are nonzero, so \(L_W(x)=0\). For
\(x\notin W\), all three classes are nonzero, so \(L_W(x)=1\). Thus
\(L_W=\ell_W\).

This quadratic-to-linear collapse is the local Fano transgression.

---

## 4. Support-boundary form on a cubic flow

Let \(G\) be a finite cubic graph with a nowhere-zero flow

\[
f:E(G)\to\Gamma.
\]

At each vertex \(v\), the incident flow values are the three nonzero elements
of a plane \(W_v\).

For a global section \(k=(k_v)\) of the quotient sheaf, define

\[
s(k)_e=q_{f(e)}([k_v])
\qquad(e\ni v).
\]

This is independent of the endpoint because the section condition says that
the two endpoint values have the same class in
\(\Gamma/\langle f(e)\rangle\).

Applying the local Fano identity at each vertex gives

\[
\begin{aligned}
(\partial s(k))_v
&=
\sum_{e\ni v}q_{f(e)}([k_v])\\
&=
\ell_{W_v}(k_v).
\end{aligned}
\]

Hence

\[
\boxed{
\partial s(k)=b(k),
\qquad
b(k)_v=\mathbf 1_{k_v\notin W_v}.
}
\]

The earlier three-row support table is therefore the evaluation table of one
canonical quadratic identity.

---

## 5. Affine compatibility

Under the perfect Fano pairing

\[
H^0(G;\mathscr Q_f)\cong H^1(G;\mathscr Q_f)^*,
\]

the affine obstruction satisfies

\[
\langle k,[c_f]\rangle
=
\sum_v\ell_{W_v}(k_v).
\]

Using the quadratic transgression,

\[
\begin{aligned}
\langle k,[c_f]\rangle
&=
\varepsilon b(k)\\
&=
\varepsilon\partial s(k)\\
&=0.
\end{aligned}
\]

Thus \([c_f]=0\). The compressed compatibility theorem is the global
cancellation of the local quadratic transgressions.

---

## 6. Odd-valence plane-supported extension

The local identity is not intrinsically restricted to three distinct
incidences.

Suppose the incident flow values at a vertex all lie in one plane \(W\), and
let \(m_h\) be the multiplicity of the direction \(h\in W\setminus\{0\}\).
The flow equation implies

\[
m_{h_1}\equiv m_{h_2}\equiv m_{h_3}\pmod2.
\]

Their common parity is also the degree parity. Therefore

\[
\boxed{
\sum_{e\ni v}q_{f(e)}([x])
=
(\deg v\bmod2)\,\ell_W(x).
}
\]

For odd valence this is the same outside-plane identity; for even valence the
quadratic contributions cancel locally. This extends the support-boundary
mechanism beyond the simple cubic star, although the full affine-family and CDC
interpretation still requires separate local definitions.

---

## 7. Structural meaning

The identity connects the principal strands of the project.

- The functions \(q_h\) are canonical relative quadratic functions on the edge
  quotients.
- Their polar forms are the local Fano contractions
  \(\omega(h,-,-)\).
- Their sum over a Fano plane loses its quadratic part and becomes the linear
  outside-plane obstruction bit.
- Evaluating on a global section produces the transverse-edge chain.
- The graph boundary and augmentation then force global compatibility.

Thus the common primitive is not exact balancedness. It is a canonical
quadratic transgression from edge-quotient quadratics to the vertex
codimension-one bit:

\[
\boxed{
\text{edge quadratic norms}
\longrightarrow
\text{Fano linear quotient bit}
\longrightarrow
\text{graph boundary cancellation}.
}
\]

Exact balanced flags describe the unisolvent rigidity locus of the broader
relative-quadratic evaluation problem. AffineCDC instead exploits one special
quadratic identity that remains meaningful on singular systems.
