# AffineCDC — current structural synthesis

**First public synthesis:** 2026-07-14  
**Status:** evolving theorem-level draft. The original coordinate-free compatibility chain and the conditional cubic CDC extraction are Lean-verified in `Yuren-Tang/affine-cdc`; several structural reformulations below are paper-proof complete or computationally verified but not yet formalized in their present form.

This file records the presently coherent mathematical spine. It is intentionally not a finished paper. Sections may later split, merge or be replaced as the theory stabilizes.

---

## 1. Local affine obstruction

Let \(G\) be a finite connected cubic graph and let

\[
f:E(G)\to \Gamma
\]

be a nowhere-zero flow over a binary vector space. At each vertex the three incident nonzero values sum to zero and span a plane \(W_v\).

The local affine gluing choices form a torsor, and global compatibility is governed by the linear operator

\[
\delta_f:\Gamma^{V(G)}\longrightarrow
\bigoplus_{e=uv}\Gamma/\langle f(e)\rangle,
\qquad
(\delta_fk)_e=[k_u+k_v].
\]

The affine equation is

\[
\delta_fm=c_f.
\]

Its solution space, when nonempty, is a torsor under \(\ker\delta_f\). Modulo global translations by \(\Gamma\), the homogeneous moduli code is

\[
\mathcal B_f:=\ker\delta_f/\Gamma.
\]

Equivalently, a codeword \(\lambda\in\mathbf F_2^E\) belongs to \(\mathcal B_f\) precisely when there is a potential \(k:V\to\Gamma\) satisfying

\[
k_u+k_v=\lambda_e f(e)
\qquad(e=uv).
\]

---

## 2. Local Fano Hodge duality

Now take

\[
\Gamma=\mathbf F_2^3
\]

with its canonical nonzero alternating volume form

\[
\omega\in\Lambda^3\Gamma^*.
\]

For a plane \(W\le\Gamma\), define the legal dual configurations by triples

\[
\eta_h\in\operatorname{Ann}(h)
\qquad(h\in W\setminus\{0\})
\]

satisfying

\[
\sum_{h\ne0}\eta_h=0.
\]

The map

\[
\mathcal H_W:\Gamma\longrightarrow\operatorname{DualConfig}(W),
\qquad
(\mathcal H_W(a))_h(x)=\omega(a,h,x)
\]

is an isomorphism.

This identifies the earlier coordinate cross-bit with the quotient bit detecting whether \(a\notin W\). It is the local mechanism behind the exceptional rank-three compatibility theorem.

---

## 3. Flow quotient sheaf

Define a cellular sheaf \(\mathscr Q_f\) on \(G\) by

\[
\mathscr Q_f(v)=\Gamma,
\qquad
\mathscr Q_f(e)=\Gamma/\langle f(e)\rangle,
\]

with endpoint restrictions equal to the quotient maps. Its cellular coboundary is exactly \(\delta_f\).

Hence

\[
[c_f]\in H^1(G;\mathscr Q_f)
\]

is the intrinsic affine compatibility obstruction, while

\[
\widetilde H^0(G;\mathscr Q_f)
:=H^0(G;\mathscr Q_f)/\Gamma
\cong\mathcal B_f.
\]

The dual of \(H^1\) is the equilibrium-stress space consisting of covectors

\[
\psi_e\in\operatorname{Ann}(f(e))
\]

whose incident sum vanishes at every vertex:

\[
H^1(G;\mathscr Q_f)^*\cong\operatorname{Stress}(f).
\]

For a cubic graph with \(n=|V|\) and \(r=\dim\langle f(E)\rangle\),

\[
\chi(G;\mathscr Q_f)
=r|V|-(r-1)|E|
=\frac{3-r}{2}n.
\]

Thus rank three is the unique balanced rank.

---

## 4. Canonical alternating stresses and the index trichotomy

Every alternating form

\[
\Omega\in\Lambda^2\Gamma^*
\]

defines an equilibrium stress

\[
\psi_e^\Omega(x)=\Omega(f(e),x).
\]

If the flow values span \(\Gamma\), these form a canonical subspace of dimension

\[
\binom r2.
\]

Let

\[
\operatorname{EssStress}(f)
:=\operatorname{Stress}(f)/\operatorname{AltStress}(f).
\]

Writing \(b_f=\dim\mathcal B_f\), one obtains

\[
\boxed{
\dim\operatorname{EssStress}(f)
=b_f+\frac{(r-3)(n-r)}2.
}
\]

This yields the rank trichotomy:

- **rank two:** flexibility is forced, with \(b_f=n/2-1\), and every stress is canonical;
- **rank three:** \(\dim\operatorname{EssStress}(f)=b_f\), producing Fano self-duality;
- **rank greater than three:** even gauge-rigid systems generally possess dimensionally forced essential obstruction directions.

The explicit rank-four \(K_{3,3}\) example has \(b_f=0\) but one essential stress direction, which detects incompatibility.

---

## 5. Wedge–handshake identity and Fano compatibility

At a cubic vertex with incident values

\[
h_1+h_2+h_3=0,
\]

the element

\[
q_v=h_1\wedge h_2\in\Lambda^2\Gamma
\]

is independent of the chosen pair. For every \(\alpha,\beta\in\Gamma^*\), the value

\[
(\alpha\wedge\beta)(q_v)
\]

is the degree parity at \(v\) of the intersection of the binary flows \(\alpha\circ f\) and \(\beta\circ f\). Summing over all vertices counts each common edge twice, so

\[
\boxed{\sum_v q_v=0.}
\]

Therefore every canonical alternating stress annihilates the affine obstruction.

In rank three, the global Hodge map

\[
(\mathcal H_fk)_e(x)=\omega(k_u,f(e),x)
\]

identifies global sections with equilibrium stresses. Constants correspond to canonical determinant stresses, and reduced global sections correspond to essential stresses. The branching identity then annihilates the remaining essential part, yielding

\[
[c_f]=0.
\]

Thus every nowhere-zero \(\mathbf F_2^3\)-flow on a finite cubic graph admits a compatible affine gluing.

---

## 6. Schur code and flow constraint matroid

Let \(\mathcal C(G)\le\mathbf F_2^E\) be the binary cycle space and let

\[
\mathcal F_f=\{\ell\circ f:\ell\in\Gamma^*\}.
\]

Then

\[
\boxed{
\mathcal B_f=(\mathcal C(G)*\mathcal F_f)^\perp,
}
\]

where \(*\) is coordinatewise multiplication.

Equivalently, put

\[
Q_G=\mathbf F_2^E/\mathcal C(G)^\perp\cong\mathcal C(G)^*
\]

and write \(\bar e\in Q_G\) for the class of the edge coordinate. Define

\[
T_f:\mathbf F_2^E\to\Gamma\otimes Q_G,
\qquad
T_f(\lambda)=\sum_e\lambda_e f(e)\otimes\bar e.
\]

Then

\[
\ker T_f=\mathcal B_f.
\]

The columns

\[
f(e)\otimes\bar e
\]

define a canonical binary represented matroid \(M_f^\otimes\), the **flow constraint matroid**. Its cycle space is \(\mathcal B_f\), and its cocycle space is \(\mathcal C(G)*\mathcal F_f\). Gauge rigidity is equivalent to this matroid being free.

---

## 7. Flow tensor complex

The flow induces a surjection

\[
F^*:Q_G\to\Gamma,
\qquad
F^*(\bar e)=f(e).
\]

Define

\[
W_f:\Gamma\otimes Q_G\to\Lambda^2\Gamma,
\qquad
W_f(a\otimes q)=a\wedge F^*(q).
\]

Since

\[
W_f(f(e)\otimes\bar e)=f(e)\wedge f(e)=0,
\]

we obtain the canonical complex

\[
0\to\mathcal B_f\to\mathbf F_2^E
\xrightarrow{T_f}\Gamma\otimes Q_G
\xrightarrow{W_f}\Lambda^2\Gamma\to0,
\]

exact except possibly at the middle tensor space. Its middle homology is

\[
\mathcal K_f:=\ker W_f/\operatorname{im}T_f.
\]

There is a canonical duality

\[
\mathcal K_f^*\cong\operatorname{EssStress}(f).
\]

The affine obstruction determines a class

\[
\kappa_f\in\mathcal K_f,
\]

and compatibility is equivalent to \(\kappa_f=0\).

For cubic rank-three flows, \(T_f\) becomes a square map onto \(\ker W_f\), and the following are equivalent:

\[
\mathcal B_f=0
\iff
\mathcal K_f=0
\iff
T_f:\mathbf F_2^E\overset\sim\longrightarrow\ker W_f
\iff
M_f^\otimes\text{ is free}.
\]

This is the current intrinsic gauge-rigidity criterion for cyclic cores.

---

## 8. Fano basis-packing parity

Choose a cycle-space basis beginning with the three coordinate flows and complete it by a matrix \(H\) of dimension

\[
d=\frac n2-2.
\]

The reduced tensor determinant expands into ordered triples \((R_1,R_2,R_3)\) of pairwise disjoint \(H\)-bases such that

\[
R_i\subseteq\operatorname{supp}(f_i),
\]

and the six complementary edges carry six distinct nonzero Fano labels.

If \(N_f(H)\) is the number of these packings, then

\[
\boxed{
\det\overline T_f=N_f(H)\pmod2.
}
\]

Consequently

\[
f\text{ is gauge-rigid}
\iff
N_f(H)\text{ is odd}.
\]

The integer count depends on the chosen complement, but its parity is intrinsic.

---

## 9. Embeddings, Petrials and cut gluing

A compatible affine gauge can be interpreted as a strong embedding equipped with \(\Gamma\)-valued face potentials satisfying

\[
f(e)=t(F_e^+)+t(F_e^-).
\]

The moduli code acts by code-constrained partial Petrials. This leads to genus and orientability distributions, transition-matroid state sums and a syndrome-refined universal invariant.

Low edge cuts admit exact gluing laws. For a two-edge sum,

\[
b_G=b_A+b_B+1,
\qquad
\Pi_G=2\Pi_A\Pi_B.
\]

For a three-edge sum,

\[
b_G=b_A+b_B,
\qquad
\Pi_G=\Pi_A\Pi_B.
\]

These are naturally interpreted as Mayer–Vietoris statements for the flow quotient sheaf.

---

## 10. Formalization and publication path

The current Lean repository proves the coordinate-free rank-three compatibility chain and extracts a standard cycle double cover for cubic graphs carrying a nowhere-zero \(\mathbf F_2^3\)-flow. The unconditional CDC endpoint remains the eventual integration target.

Before the public Lean API is frozen, the Hodge/sheaf reformulation should be prototyped and compared against the existing branching proof. The broader moduli, embedding, transition and cut-factorization theory belongs to the mathematical research layer and need not block the first stable formal release.

A dated SHA-256 snapshot manifest in this project records the original notes, scripts and outputs from which this synthesis was distilled.
