# The dual Fano residue theorem

**Date:** 2026-07-15  
**Status:** theorem-level structural draft; finite-field identities checked exhaustively in ranks three through six, not yet independently audited or Lean-formalized.

This note gives an all-rank description of the affine compatibility obstruction.
The rank-three theorem follows because a one-dimensional annihilator cannot
contain a Fano plane. The rank-four Pfaffian residue is the first nontrivial
specialization.

Let \(\Gamma\) be a binary vector space and let \(W\le\Gamma\) be a plane. Put

\[
D=W\setminus\{0\}.
\]

A legal dual configuration is a family

\[
\eta=(\eta_h)_{h\in D},
\qquad
\eta_h\in\operatorname{Ann}(h),
\qquad
\sum_{h\in D}\eta_h=0.
\]

---

## 1. The cross-bit and support parity

The cross-pairing theorem gives a common value

\[
\beta_W(\eta)
=
\eta_h(h')
\qquad(h\ne h').
\]

This is independent of the chosen ordered pair of distinct directions.

Define the local support parity

\[
\sigma_W(\eta)
=
\sum_{h\in D}\mathbf1_{\eta_h\ne0}.
\]

The previously verified local theorem says

\[
\beta_W(\eta)=0
\iff
\eta_h|_W=0
\text{ for every }h\in D.
\]

Thus, when \(\beta_W(\eta)=0\), all three components lie in

\[
\operatorname{Ann}(W).
\]

---

## 2. The hidden dual Fano line

### Definition

Define

\[
\rho_W(\eta)=1
\]

exactly when

1. \(\beta_W(\eta)=0\); and
2. all three components \(\eta_h\) are nonzero.

Otherwise put \(\rho_W(\eta)=0\).

If \(\rho_W(\eta)=1\), then the three covectors lie in
\(\operatorname{Ann}(W)\), are nonzero, and sum to zero. Therefore they are
pairwise distinct and are exactly the three nonzero points of a plane

\[
P_\eta\le\operatorname{Ann}(W).
\]

Hence \(\rho_W\) detects a **hidden dual Fano line** inside the annihilator of
the local flow plane.

Conversely, any ordered identification

\[
D\overset\sim\longrightarrow P\setminus\{0\}
\]

with a plane \(P\le\operatorname{Ann}(W)\) defines a residue configuration.

---

## 3. The local residue identity

### Theorem 3.1

For every legal dual configuration,

\[
\boxed{
\sigma_W(\eta)
=
\beta_W(\eta)+\rho_W(\eta).
}
\]

### Proof

If \(\beta_W(\eta)=1\), then for every \(h\in D\), the covector \(\eta_h\)
takes value one on either of the other two directions. Hence all three
components are nonzero, so

\[
\sigma_W(\eta)=1,
\qquad
\rho_W(\eta)=0.
\]

Suppose \(\beta_W(\eta)=0\). Then all components lie in
\(\operatorname{Ann}(W)\) and sum to zero. A triple summing to zero cannot have
support size one. Its support parity is therefore odd exactly when all three
components are nonzero. This is precisely the condition \(\rho_W(\eta)=1\).

---

## 4. Counting the local residues

Let

\[
r=\dim\Gamma.
\]

Then

\[
\dim\operatorname{Ann}(W)=r-2.
\]

The legal-configuration space has dimension

\[
2r-3,
\]

and hence contains

\[
2^{2r-3}
\]

configurations.

A residue configuration is obtained by choosing a plane

\[
P\le\operatorname{Ann}(W)
\]

and an ordered isomorphism from the three directions of \(W\) to the three
nonzero points of \(P\). Each plane gives

\[
|\operatorname{GL}(2,2)|=6
\]

such identifications. Therefore the number of residue configurations is

\[
\boxed{
6{r-2\brack2}_2
=
(2^{r-2}-1)(2^{r-2}-2).
}
\]

In particular:

| rank \(r\) | legal configurations | residue configurations |
|---:|---:|---:|
| 3 | 8 | 0 |
| 4 | 32 | 6 |
| 5 | 128 | 42 |
| 6 | 512 | 210 |

Rank four is the first possible residue layer.

---

## 5. The global residue theorem

Let \(G\) be a finite cubic graph with a nowhere-zero binary flow

\[
f:E(G)\to\Gamma.
\]

At a vertex \(v\), let \(W_v\) be the plane spanned by the three incident flow
values.

Let \(\psi\) be an equilibrium stress. Its three incident edge covectors form a
legal dual configuration

\[
\psi_v\in\operatorname{DualConfig}(W_v).
\]

The local cross-pairing calculation gives

\[
\psi(c_f)
=
\sum_v\beta_{W_v}(\psi_v).
\]

On the other hand, every nonzero edge covector is counted at both endpoints,
so the handshaking identity gives

\[
\sum_v\sigma_{W_v}(\psi_v)=0.
\]

Applying Theorem 3.1 yields:

### Theorem 5.1 — dual Fano residue formula

\[
\boxed{
\psi(c_f)
=
\sum_{v\in V(G)}\rho_{W_v}(\psi_v).
}
\]

Consequently:

\[
\boxed{
[c_f]=0
\iff
\text{every equilibrium stress has an even number of hidden dual-Fano vertices}.
}
\]

This is the complete affine compatibility criterion in every rank.

---

## 6. Rank three

If \(\dim\Gamma=3\), then

\[
\dim\operatorname{Ann}(W_v)=1.
\]

A one-dimensional binary space has only one nonzero point and cannot contain a
plane. Therefore

\[
\rho_{W_v}\equiv0
\]

at every vertex. The global residue theorem immediately gives

\[
\psi(c_f)=0
\]

for every equilibrium stress, hence

\[
\boxed{[c_f]=0.}
\]

Thus the rank-three compatibility theorem has the following minimal
explanation:

\[
\boxed{
\operatorname{Ann}(W_v)\text{ is too small to contain a dual Fano line.}
}
\]

The old branching identity is the local statement that no residue can occur.

---

## 7. Rank four

If \(\dim\Gamma=4\), then

\[
\dim\operatorname{Ann}(W_v)=2.
\]

There is exactly one plane in the annihilator, namely the whole annihilator.
A residue vertex is therefore characterized by

\[
\{\psi_e:e\ni v\}
=
\operatorname{Ann}(W_v)\setminus\{0\}.
\]

Under the alternating-two-form description of legal configurations, this
indicator is exactly the cubic Pfaffian residue

\[
\rho_W([\alpha])
=
(1+\beta_W([\alpha]))\operatorname{Pf}(\alpha).
\]

Thus the Pfaffian formula is the algebraic equation of a hidden dual Fano line.

---

## 8. Higher rank

For rank greater than four, the annihilator has dimension at least three and
may contain many dual Fano planes. The local residue remembers not only that a
support-parity failure occurs, but also a plane

\[
P_\eta\le\operatorname{Ann}(W).
\]

The scalar affine obstruction records only the parity of the residue vertices.
The distribution of the planes \(P_\eta\) may contain finer higher-rank
structure not visible to the original compatibility class.

This suggests a refinement of the higher-rank theory in which residue vertices
are decorated by annihilator planes, and global essential stresses are studied
through the geometry of these dual Fano decorations.

---

## 9. Structural hierarchy

The compatibility mechanism now has a uniform description:

\[
\boxed{
\begin{array}{c|c}
\text{rank three}&\text{no annihilator plane, hence automatic compatibility}\\
\text{rank four}&\text{a unique possible local dual plane, detected cubically}\\
\text{higher rank}&\text{many possible dual planes and a richer residue geometry}.
\end{array}
}
\]

The exceptional rank-three theorem and the first rank-four counterexample are
therefore consecutive cases of one dual-Fano residue principle.
