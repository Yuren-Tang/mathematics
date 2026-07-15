# Higher-degree Fano transgression

**Date:** 2026-07-15  
**Status:** theorem-level structural draft; not yet independently audited or Lean-formalized.

This note isolates the all-rank finite-geometric identity behind the rank-three quadratic package.

Let

\[
\Gamma=\mathbf F_2^r
\]

and let \(W\le \Gamma\) be a plane. Write

\[
D=W\setminus\{0\}.
\]

For each \(h\in D\), define

\[
Q_h=\Gamma/\langle h\rangle
\]

and let

\[
\nu_h:Q_h\to\mathbf F_2
\]

be the nonzero indicator:

\[
\nu_h(q)=
\begin{cases}
0,&q=0,\\
1,&q\ne0.
\end{cases}
\]

Also let

\[
\nu_{\Gamma/W}:\Gamma/W\to\mathbf F_2
\]

be the nonzero indicator on the plane quotient.

---

## 1. The degree-lowering identity

### Theorem 1.1

For every \(x\in\Gamma\),

\[
\boxed{
\sum_{h\in D}\nu_h([x]_h)
=
\nu_{\Gamma/W}([x]_W).
}
\]

### Proof

There are three cases.

- If \(x=0\), all terms vanish.
- If \(x\in W\setminus\{0\}\), then \(x\) spans exactly one of the three lines \(\langle h\rangle\). One quotient class is zero and the other two are nonzero, so the sum is \(0\).
- If \(x\notin W\), then \(x\notin\langle h\rangle\) for every \(h\in D\). All three terms are one, so the sum is \(1\).

This is exactly the right-hand side.

---

## 2. Polynomial degree

The nonzero indicator on a \(d\)-dimensional binary vector space has algebraic degree \(d\). Therefore:

\[
\deg \nu_h=r-1,
\qquad
\deg \nu_{\Gamma/W}=r-2.
\]

The theorem says that summing the three degree-\((r-1)\) edge-quotient support polynomials over a Fano line cancels their top-degree part and produces the degree-\((r-2)\) support polynomial on the plane quotient.

Thus:

\[
\boxed{
\text{Fano summation lowers support degree by one.}
}
\]

If \(\Omega\in\Lambda^r\Gamma^*\) is a volume form, the top polarization of \(\nu_h\) is contraction by \(h\). The cancellation of the degree-\((r-1)\) parts is therefore the identity

\[
\sum_{h\in D}\iota_h\Omega
=
\iota_{\sum_{h\in D}h}\Omega
=
0.
\]

---

## 3. The affine local-family identity

For each \(h\in D\), let

\[
\kappa_h\in Q_h
\]

be the common class of the other two nonzero elements of \(W\). Put

\[
\kappa_W=(\kappa_h)_{h\in D}.
\]

### Theorem 3.1

For every \(m\in\Gamma\),

\[
\boxed{
\sum_{h\in D}
\nu_h\bigl(\kappa_h+[m]_h\bigr)
=
1.
}
\]

### Proof

If \(m\notin W\), none of the three classes can vanish, so the sum is three, hence one.

If \(m=0\), all three \(\kappa_h\) are nonzero, so again the sum is one.

If \(m\in W\setminus\{0\}\), exactly two of the three translated classes vanish and one remains nonzero. Hence the sum is one.

Therefore the local affine-family torsor

\[
\kappa_W+\Delta_W(\Gamma)
\]

is contained in the constant level set

\[
\left\{
z:
\sum_h\nu_h(z_h)=1
\right\}.
\]

This statement holds in every rank.

---

## 4. Rank three as the quadratic member

At rank three:

\[
\dim Q_h=2,
\qquad
\dim(\Gamma/W)=1.
\]

Hence:

- each \(\nu_h\) is quadratic;
- \(\nu_{\Gamma/W}\) is linear;
- the degree-lowering theorem is the Fano quadratic transgression;
- the affine level set above is the characteristic torsor of a Lagrangian.

Thus the rank-three package is the quadratic-linear member of the all-rank identity.

At rank four:

\[
\dim Q_h=3,
\qquad
\dim(\Gamma/W)=2.
\]

The same theorem becomes a cubic-to-quadratic transgression. The support identity survives, but the bilinear symplectic geometry does not: the edge support functions are genuinely cubic and the local homogeneous family space is not half-dimensional.

---

## 5. Global support parity in every rank

Let \(G\) be cubic and let \(k=(k_v)\) be a global section of the quotient sheaf. Define

\[
s(k)_e
=
\nu_{f(e)}([k_v]_e).
\]

This is independent of the endpoint.

At each vertex, Theorem 1.1 gives

\[
(\partial s(k))_v
=
\nu_{\Gamma/W_v}([k_v]_{W_v}).
\]

Therefore:

\[
\boxed{
\sum_v
\nu_{\Gamma/W_v}([k_v]_{W_v})
=
0.
}
\]

So in every rank, the number of vertices at which \(k_v\notin W_v\) is even.

What is special at rank three is not this parity identity itself. It is that \(\Gamma/W_v\) is one-dimensional, so the nonzero indicator is the complete quotient coordinate. The scalar parity identity therefore captures the whole local obstruction.

For rank greater than three, the quotient contains directional information that the support indicator forgets. The parity identity remains true but is no longer sufficient for compatibility.

---

## 6. Structural boundary

The all-rank picture is:

\[
\boxed{
\begin{array}{c}
\text{edge support polynomial of degree }r-1\\
\downarrow\ \text{Fano summation}\\
\text{outside-plane support polynomial of degree }r-2.
\end{array}
}
\]

Rank three is the unique point where this becomes

\[
\boxed{
\text{quadratic edge norms}
\longrightarrow
\text{linear vertex obstruction bit}.
}
\]

Only there can the transgression be encoded by a nondegenerate quadratic space, a Lagrangian, and its characteristic torsor.

Thus the rank-three theorem is both exceptional and part of a coherent higher-degree hierarchy.
