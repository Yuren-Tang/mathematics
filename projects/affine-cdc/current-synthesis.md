# AffineCDC — active mathematical spine

**Last structural rewrite:** 2026-07-15  
**Status:** evolving theorem-level synthesis. The original coordinate-free
compatibility chain and conditional cubic CDC extraction are Lean-verified in
`Yuren-Tang/affine-cdc`. The quadratic-Lagrangian compression below is a
paper-proof draft awaiting an independent proof audit and a later Lean
refactor.

This file is the **active spine**, not an archive. It is expected to be
rewritten as the mathematics improves. Earlier versions remain available in
Git history. Specialized notes linked below retain calculations, proofs and
branches that no longer belong in the main narrative.

---

## 0. Current map

The project now separates into four layers.

### A. Paper-1 core: affine Fano compatibility

\[
\text{local Fano quadratic package}
\longrightarrow
\text{vertex characteristic torsor}
\cap
\text{edge-diagonal Lagrangian}
\longrightarrow
\text{compatibility}
\longrightarrow
\text{CDC extraction}.
\]

The quotient-sheaf obstruction, global Fano duality and support-boundary
identity are equivalent linear and combinatorial projections of this
quadratic-Lagrangian intersection.

This is the present logical and expository core.

### B. Rigidity and interpolation

\[
\text{relative quadratic evaluation}
\longrightarrow
\text{balancedness}
\longrightarrow
\text{unisolvence / exactness}
\longrightarrow
\text{constraint matroid circuits}.
\]

This explains exact balanced flags, but it is **not** the primitive behind
AffineCDC: compatibility remains nontrivial on singular systems.

### C. Generalized tensor and code-flag theory

The flow tensor complex, nested code flags, Schur multiplication, Koszul
homology, exact sequences, morphisms and interfaces form a broader theory.
They organize the defect spaces and their functoriality, but do not currently
belong to the minimal Paper-1 proof.

### D. Graphical consequences

The even gauge-code theorem, low-weight circuit classifications, embeddings,
Petrials and cut gluing are consequences and test cases of the structural
framework.

---

# Part I. The Paper-1 core

## 1. Quotient sheaf and affine gluing

Let \(G\) be a finite cubic graph and let

\[
f:E(G)\to \Gamma,
\qquad
\Gamma=\mathbf F_2^3,
\]

be a nowhere-zero flow. At a vertex \(v\), the three incident nonzero values
sum to zero and are the three nonzero points of a plane

\[
W_v\le \Gamma.
\]

For an edge \(e=uv\), put

\[
Q_e=\Gamma/\langle f(e)\rangle.
\]

The quotient-sheaf cochain spaces are

\[
C_f^0=\Gamma^{V(G)},
\qquad
C_f^1=\bigoplus_{e\in E(G)}Q_e,
\]

with coboundary

\[
(\delta_f k)_e=[k_u+k_v].
\]

Write

\[
H_f^0=\ker\delta_f,
\qquad
H_f^1=\operatorname{coker}\delta_f.
\]

The local affine classification supplies an intrinsic right-hand side

\[
c_f\in C_f^1.
\]

Its class \([c_f]\in H_f^1\) is the affine compatibility obstruction. The
original formulation proves compatibility by showing \([c_f]=0\).

The quadratic formulation below encodes the same equation as an affine
Lagrangian-intersection problem.

## 2. The local Fano quadratic package

Every binary plane \(Q_e\) carries the canonical anisotropic quadratic form

\[
q_e(x)=\mathbf 1_{x\ne0}.
\]

Its polar form is the unique nonzero alternating form on \(Q_e\). If

\[
\omega\in\Lambda^3\Gamma^*
\]

is the unique nonzero volume form, then

\[
B_e([x],[y])=\omega(f(e),x,y).
\]

At a vertex \(v\), put

\[
\mathbb E_v=\bigoplus_{e\ni v}Q_e,
\qquad
q_v=\sum_{e\ni v}q_e.
\]

Define

\[
\Delta_v:\Gamma\to\mathbb E_v,
\qquad
\Delta_v(x)=([x]_e)_{e\ni v}.
\]

Its image

\[
L_v:=\operatorname{im}\Delta_v
\]

is a Lagrangian subspace for the polar form of \(q_v\). The three incident flow
values sum to zero, so the quadratic restriction loses its quadratic part:

\[
q_v(\Delta_vx)=\ell_{W_v}(x),
\]

where \(\ell_{W_v}\) is the unique nonzero functional with kernel \(W_v\).

For a Lagrangian \(L\) in a quadratic space \((E,q)\), define

\[
\operatorname{Char}_q(L)
=
\{\kappa\in E:B(z,\kappa)=q(z)\ \forall z\in L\}.
\]

This is an affine torsor under \(L\). In the Fano package,

\[
\boxed{
\text{local affine-family space at }v
=
\operatorname{Char}_{q_v}(L_v).
}
\]

The homogeneous Lagrangian \(L_v\) is also the space of legal dual
configurations at \(v\). The old cross-bit is simply \(q_v|_{L_v}\), and the
old support-parity branching identity is the statement that this quadratic
restriction is the parity of the nonzero incidence components.

## 3. The global incidence space and its two Lagrangians

Let

\[
I(G)=\{(v,e):v\in e\}
\]

be the incidence set, and define

\[
\mathbb E_f
=
\bigoplus_{(v,e)\in I(G)}Q_e,
\qquad
q_f
=
\sum_{(v,e)\in I(G)}q_e.
\]

This is a nondegenerate quadratic space. The vertex Lagrangian is

\[
L_{\mathrm{vert}}=\bigoplus_vL_v.
\]

Its characteristic torsor is the product of all local affine-family spaces:

\[
\operatorname{Char}_{q_f}(L_{\mathrm{vert}})
=
\bigoplus_v\operatorname{Char}_{q_v}(L_v).
\]

For an edge \(e=uv\), define the diagonal

\[
D_e=\{(x,x):x\in Q_e\}
\le Q_e^{(u)}\oplus Q_e^{(v)}.
\]

Put

\[
L_{\mathrm{edge}}=\bigoplus_eD_e.
\]

Each \(D_e\) is Lagrangian and totally singular, since

\[
q_e(x)+q_e(x)=0.
\]

Thus \(L_{\mathrm{edge}}\) is a totally singular Lagrangian. Membership in it
means exactly that the two endpoint labels on every edge agree. Hence

\[
\boxed{
\text{compatible global affine families}
=
\operatorname{Char}_{q_f}(L_{\mathrm{vert}})
\cap L_{\mathrm{edge}}.
}
\]

## 4. The affine Lagrangian-intersection theorem

Let \((E,q)\) be any finite-dimensional nondegenerate quadratic space over
\(\mathbf F_2\), and let \(L,M\le E\) be Lagrangians.

Then

\[
\boxed{
\operatorname{Char}_q(L)\cap M\ne\varnothing
\iff
q|_{L\cap M}=0.
}
\]

When nonempty, the intersection is a torsor under \(L\cap M\).

Indeed, for \(\kappa\in\operatorname{Char}_q(L)\), the condition
\(q|_{L\cap M}=0\) says

\[
B(z,\kappa)=0
\qquad(z\in L\cap M),
\]

so

\[
\kappa\in(L\cap M)^\perp=L+M.
\]

Writing \(\kappa=\ell+m\) with \(\ell\in L\), \(m\in M\), one gets

\[
m=\kappa+\ell\in\operatorname{Char}_q(L)\cap M.
\]

In particular, the characteristic torsor of any Lagrangian meets every totally
singular Lagrangian.

## 5. Compatibility and the full solution torsor

Apply the theorem to

\[
L=L_{\mathrm{vert}},
\qquad
M=L_{\mathrm{edge}}.
\]

Since \(L_{\mathrm{edge}}\) is totally singular,

\[
\boxed{
\operatorname{Char}_{q_f}(L_{\mathrm{vert}})
\cap L_{\mathrm{edge}}\ne\varnothing.
}
\]

This is the Fano compatibility theorem: one may choose a local affine family at
every vertex so that the two endpoint labels agree along every edge.

Moreover, the compatible-family space is a torsor under

\[
L_{\mathrm{vert}}\cap L_{\mathrm{edge}}.
\]

An element of \(L_{\mathrm{vert}}\) has a unique form

\[
z_{v,e}=[k_v]_e.
\]

The edge-diagonal condition is

\[
[k_u]_e=[k_v]_e,
\]

or equivalently

\[
k_u+k_v\in\langle f(e)\rangle.
\]

Therefore

\[
\boxed{
L_{\mathrm{vert}}\cap L_{\mathrm{edge}}
\cong H_f^0.
}
\]

Thus the intersection theorem simultaneously gives existence and the complete
solution torsor. In the quotient-sheaf language this is exactly \([c_f]=0\) and
the usual affine torsor under \(\ker\delta_f\).

## 6. Fano duality and support-boundary as projections

Using the polar form on \(Q_e\) identifies

\[
Q_e\cong\operatorname{Ann}(f(e)).
\]

Under this identification, \(L_v\) is the legal dual-configuration space at
\(v\), while \(L_{\mathrm{edge}}\) says that the two endpoint covectors on an
edge coincide. Hence the same intersection is also the equilibrium-stress
space:

\[
\boxed{
L_{\mathrm{vert}}\cap L_{\mathrm{edge}}
\cong H_f^0
\cong\operatorname{Stress}(f)
\cong(H_f^1)^*.
}
\]

Global Fano cohomological duality is therefore not an accidental isomorphism:
global sections and stresses are two readings of one Lagrangian intersection.

The quadratic-handshaking proof is the restriction criterion in coordinates.
For \(z\in L_{\mathrm{vert}}\cap L_{\mathrm{edge}}\),

\[
q_f(z)=2\sum_eq_e(z_e)=0.
\]

Recording only which edge components are nonzero gives an edge chain \(s\), and
this equality projects to

\[
b=\partial s,
\qquad
\varepsilon\partial s=0.
\]

Thus the support-boundary proof is the combinatorial shadow of the affine
Lagrangian-intersection theorem.

The exceptional hypotheses fit exactly because:

- binary edge quotients have canonical quadratic norms;
- a rank-three vertex plane gives the Fano Lagrangian and its characteristic
  torsor;
- each edge appears twice, making the edge diagonal totally singular.

## 7. CDC extraction

A point of

\[
\operatorname{Char}_{q_f}(L_{\mathrm{vert}})
\cap L_{\mathrm{edge}}
\]

is precisely a compatible collection of local even families. The verified
dart-level construction pairs the relevant incidences, takes orbits of the
resulting permutation and obtains a standard cycle double cover. This
extraction remains downstream of the quadratic compatibility theorem.

---

# Part II. Reduced duality and the tensor bridge

## 8. Constants and alternating stresses

A constant section \(k_v=a\) maps to

\[
\psi_e(x)=\omega(a,f(e),x),
\]

a canonical alternating stress. Contraction with \(\omega\) identifies

\[
\Gamma\cong\Lambda^2\Gamma^*,
\]

so constants correspond exactly to the alternating-stress subspace. The global
Fano isomorphism descends to

\[
\boxed{
\mathcal B_f
\cong
\operatorname{EssStress}(f),
}
\]

where

\[
\operatorname{EssStress}(f)
=
\operatorname{Stress}(f)/\operatorname{AltStress}(f).
\]

## 9. Flow tensor complex

Let \(\mathcal C(G)\le\mathbf F_2^E\) be the binary cycle space and

\[
\mathcal F_f=\{\ell\circ f:\ell\in\Gamma^*\}.
\]

Then

\[
\mathcal B_f=(\mathcal C(G)*\mathcal F_f)^\perp.
\]

Equivalently, with

\[
Q_G=\mathbf F_2^E/\mathcal C(G)^\perp,
\]

define

\[
T_f:\mathbf F_2^E\to\Gamma\otimes Q_G,
\qquad
T_f(\lambda)=\sum_e\lambda_e f(e)\otimes\bar e,
\]

and

\[
W_f:\Gamma\otimes Q_G\to\Lambda^2\Gamma,
\qquad
W_f(a\otimes q)=a\wedge F^*(q).
\]

The middle homology

\[
\mathcal K_f=\ker W_f/\operatorname{im}T_f
\]

satisfies

\[
\mathcal K_f^*\cong\operatorname{EssStress}(f).
\]

Combining this with reduced Fano duality gives

\[
\boxed{
\mathcal B_f\cong\mathcal K_f^*.
}
\]

Thus the tensor defect duality is the reduced form of the quotient-sheaf Fano
cohomological duality, after removing constants and alternating stresses.

The tensor language is structurally valuable, but it is not needed to state
the shortest compatibility proof.

---

# Part III. Rigidity as relative quadratic interpolation

## 10. Relative quadratic evaluation

For a full-support nested binary code flag

\[
D\subseteq C\subseteq A=\mathbf F_2^E,
\]

define

\[
\kappa:\Lambda^2D\to D\otimes C,
\qquad
\kappa(d_1\wedge d_2)=d_1\otimes d_2+d_2\otimes d_1,
\]

and

\[
\mathcal Q(D,C)
:=(D\otimes C)/\kappa(\Lambda^2D).
\]

Coordinatewise multiplication descends to the relative quadratic evaluation
map

\[
\operatorname{ev}_{D,C}:\mathcal Q(D,C)\to A.
\]

Since

\[
\dim\mathcal Q(D,C)
=(\dim D)(\dim C)-\binom{\dim D}{2},
\]

the flag is balanced exactly when evaluation is a square linear system.

## 11. Exact balanced flags are unisolvent

For a balanced flag, the following are equivalent:

- the flow-tensor complex is exact;
- \(\operatorname{ev}_{D,C}\) is injective;
- \(\operatorname{ev}_{D,C}\) is surjective;
- every function on \(E\) has a unique relative quadratic interpolant.

Hence

\[
\boxed{
\text{exact balanced flag}
=
\text{relatively quadratically unisolvent coordinate set}.
}
\]

The balanced determinant is an interpolation determinant. Constraint-matroid
circuits are minimal failures of relative quadratic unisolvence.

This is the correct positive meaning of exact balancedness, but exactness is
only the rigid locus \(\mathcal B_f=\mathcal K_f=0\). On that locus compatibility
is automatic, so exact balancedness cannot be the primitive behind AffineCDC.

---

# Part IV. Consequences and specialized branches

## 12. Gauge parity and circuit structure

For rank at most three, every gauge word has even Hamming weight. Equivalently,
the constraint matroid is bipartite. The rank bound is sharp: rank four admits
odd gauge words.

See:

- [Even gauge code](even-gauge-code.md)
- [Weight-six circuit classification](weight6-circuit-classification.md)

The low-weight graphical circuit layers currently read:

| weight | circuit type |
|---:|---|
| \(2\) | equal-labelled \(2K_2\) quotient |
| \(4\) | equal-labelled \(4K_2\) quotient |
| \(6\) | \(6K_2\), doubled triangle \(2K_3\), or affine-plane \(K_4\) |

The next unresolved layer is weight eight.

## 13. General code-flag and tensor theory

These notes develop the broader algebraic framework:

- [Flow tensor datum](flow-tensor-datum.md)
- [Flow tensor foundations v0](flow-tensor-theory-foundations-v0.md)
- [Code flags, Schur products and Koszul homology](code-flag-schur-koszul.md)
- [Divided-square exact sequence](divided-square-exact-sequence.md)
- [Coefficient-quotient exact sequence](coefficient-quotient-exact-sequence.md)
- [Morphisms and automorphisms](flow-tensor-morphisms-and-automorphisms.md)

Their current role is **generalization and rigidity theory**, not the minimal
logical core of Paper 1. Earlier language identifying the flow tensor datum as
the unique master object should therefore be read as a productive provisional
hypothesis, not the final ontology of the project.

## 14. Interfaces and gluing

The following notes study cuts and sewing:

- [Interface correspondence](interface-correspondence.md)
- [Interface line duality](interface-line-duality.md)

They are relevant to decomposition, Mayer--Vietoris phenomena and future
functorial theory, but do not block Paper 1.

## 15. Embeddings and topological interpretations

Compatible affine gauges may be interpreted through strong embeddings, face
potentials and code-constrained partial Petrials. Genus/orientability
distributions, transition-matroid state sums and cut-factorization laws remain
active research branches. They should be developed in specialized notes rather
than expanded inside this spine before the compatibility paper closes.

---

# Part V. Status and publication discipline

## 16. Verified versus newly compressed

### Lean-verified in `Yuren-Tang/affine-cdc`

- local affine classification and naturality;
- quotient universality and gauge classification;
- legal dual configurations and the cross-bit formulation;
- codimension-one branching identity;
- rank-three global compatibility;
- dart-level conditional cycle-double-cover extraction;
- axiom and no-`sorry` audit.

### Paper-proof draft, not yet formalized in this presentation

- the local Fano quadratic space \((\mathbb E_v,q_v)\);
- local affine families as the characteristic torsor of a Fano Lagrangian;
- the abstract affine Lagrangian-intersection criterion;
- the vertex/edge Lagrangian proof of global compatibility;
- global sections and stresses as the same Lagrangian intersection;
- the support-boundary identity as the support projection of that proof;
- exact balanced flags as relative quadratic unisolvent configurations.

See [Fano quadratic transgression](fano-quadratic-transgression.md),
[the Fano quadratic Lagrangian package](fano-quadratic-lagrangian-package.md),
and [affine Lagrangian intersection](affine-lagrangian-intersection.md).

These new formulations require independent mathematical review before they
replace the older presentation in a formal release.

## 17. Current Paper-1 boundary

The smallest coherent first paper should contain:

1. the local Fano quadratic package;
2. local affine families as characteristic torsors;
3. the global vertex and edge Lagrangians;
4. the affine Lagrangian-intersection theorem;
5. the quotient-sheaf and support-boundary translations;
6. the verified CDC extraction;
7. a theorem-to-Lean map and trust-boundary audit.

The broad code-flag/Koszul theory, exact-balanced interpolation, circuit
classifications, interface theory and topological state sums should not block
closure of Paper 1. They may appear as brief outlooks or later companion work.

## 18. Living-document rule

This file states the current best synthesis. When a later structure strictly
improves it, this file should be rewritten rather than merely supplemented.
Superseded arguments remain citable through Git history and specialized notes;
they need not remain in the active narrative.
