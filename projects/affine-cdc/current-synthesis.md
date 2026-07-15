# AffineCDC — active mathematical spine

**Last structural rewrite:** 2026-07-15  
**Status:** evolving theorem-level synthesis. The original coordinate-free
compatibility chain and conditional cubic CDC extraction are Lean-verified in
`Yuren-Tang/affine-cdc`. The Fano support-boundary compression below is a
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
\text{quotient sheaf}
\longrightarrow
\text{Fano cohomological duality}
\longrightarrow
\text{support-boundary identity}
\longrightarrow
\text{compatibility}
\longrightarrow
\text{CDC extraction}.
\]

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

## 1. Quotient sheaf and affine obstruction

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

Define the quotient-sheaf cochain spaces

\[
C_f^0=\Gamma^{V(G)},
\qquad
C_f^1=\bigoplus_{e=uv}\Gamma/\langle f(e)\rangle,
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

Its class

\[
[c_f]\in H_f^1
\]

is the complete affine compatibility obstruction. The gluing problem is
solvable exactly when \([c_f]=0\).

The solution set, when nonempty, is a torsor under \(H_f^0\). After quotienting
by constant vertex potentials,

\[
\mathcal B_f:=H_f^0/\Gamma
\]

is the homogeneous gauge or moduli code.

## 2. Local Fano duality

Let

\[
\omega\in\Lambda^3\Gamma^*
\]

be the unique nonzero volume form. For a plane \(W\le\Gamma\), define

\[
\operatorname{DualConfig}(W)
=
\left\{
(\eta_h)_{h\in W\setminus\{0\}}:
\eta_h\in\operatorname{Ann}(h),\ 
\sum_h\eta_h=0
\right\}.
\]

Then

\[
\boxed{
\mathcal H_W:\Gamma\overset\sim\longrightarrow
\operatorname{DualConfig}(W),
\qquad
(\mathcal H_W(a))_h(x)=\omega(a,h,x)
}
\]

is an isomorphism.

This is the local mechanism previously encoded by legal dual configurations,
the cross-pairing bit and the codimension-one branching analysis.

## 3. Global Fano cohomological duality

An equilibrium stress is a family

\[
\psi_e\in\operatorname{Ann}(f(e))
\]

whose incident sum is zero at every vertex. The stress space is canonically

\[
\operatorname{Stress}(f)\cong(H_f^1)^*.
\]

For \(k\in H_f^0\), define

\[
(\mathcal H_f k)_e([x])
=
\omega(k_u,f(e),x),
\qquad e=uv.
\]

This is independent of the endpoint because

\[
k_u+k_v\in\langle f(e)\rangle.
\]

It is an equilibrium stress because the three incident flow values sum to
zero. Conversely, a stress gives at every vertex a unique \(k_v\) by local
Fano duality; equality of the two endpoint descriptions on an edge forces

\[
k_u+k_v\in\langle f(e)\rangle.
\]

Thus the local inverses glue automatically, giving the constructive global
isomorphism

\[
\boxed{
\mathcal H_f:H_f^0\overset\sim\longrightarrow
\operatorname{Stress}(f)
\cong(H_f^1)^*.
}
\]

Equivalently, there is a perfect pairing

\[
\langle-,-\rangle_f:
H_f^0\times H_f^1\to\mathbf F_2.
\]

## 4. The transverse-edge chain

For a global section \(k=(k_v)\in H_f^0\), define

\[
s(k)\in\mathbf F_2^{E(G)}
\]

by

\[
s(k)_e=1
\iff
k_u\notin\langle f(e)\rangle,
\qquad e=uv.
\]

This is well defined, since the section condition implies

\[
k_u\in\langle f(e)\rangle
\iff
k_v\in\langle f(e)\rangle.
\]

At a vertex \(v\), define the outside-plane bit

\[
b(k)_v=1
\iff
k_v\notin W_v.
\]

The three incident flow lines are exactly the three one-dimensional subspaces
of \(W_v\). Hence:

| position of \(k_v\) | degree of \(s(k)\) at \(v\) | \(b(k)_v\) |
|---|---:|---:|
| \(k_v=0\) | \(0\) | \(0\) |
| \(k_v\in W_v\setminus\{0\}\) | \(2\) | \(0\) |
| \(k_v\notin W_v\) | \(3\) | \(1\) |

Therefore

\[
\boxed{b(k)=\partial s(k)}
\]

as vertex chains over \(\mathbf F_2\). This is the branching identity in its
minimal form.

## 5. The support-boundary proof of compatibility

The local definition of the affine obstruction gives

\[
\boxed{
\langle k,[c_f]\rangle_f
=
\sum_{v\in V(G)} b(k)_v.
}
\]

Let

\[
\varepsilon:\mathbf F_2^{V(G)}\to\mathbf F_2
\]

be augmentation. Then

\[
\boxed{
\langle k,[c_f]\rangle_f
=
\varepsilon b(k)
=
\varepsilon\partial s(k)
=0.
}
\]

The last equality is the handshaking identity: every edge has two endpoints.
Since the Fano pairing is perfect, this holds for every \(k\in H_f^0\) only if

\[
\boxed{[c_f]=0.}
\]

Thus every nowhere-zero \(\mathbf F_2^3\)-flow on a finite cubic graph admits a
compatible affine gluing.

The entire compatibility proof is therefore:

1. perfect Fano self-duality;
2. the local identity \(b(k)=\partial s(k)\);
3. augmentation kills boundaries.

## 6. Why the hypotheses fit exactly

The mechanism composes three exceptional facts.

- **Binary field:** a one-dimensional quotient has a unique nonzero value, so
  its coordinate is a support bit.
- **Rank three:** each vertex plane has codimension one, so leaving the plane is
  a single bit.
- **Cubic graph:** the incident values are exactly the three nonzero points and
  three lines of a binary plane, giving local degrees \(0,2,3\).

The theorem is exceptional because these features turn the affine obstruction
into the augmentation of an ordinary graph boundary.

## 7. CDC extraction

The compatible gauges determine local even families whose edge labels agree.
The verified dart-level construction pairs the relevant incidences, takes
orbits of the resulting permutation and obtains a standard cycle double
cover. This extraction remains part of the Paper-1 dependency cone, but is
logically downstream of the compatibility theorem above.

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

- constructive global Fano cohomological duality as an explicit isomorphism;
- the transverse-edge chain \(s(k)\);
- the identity \(b(k)=\partial s(k)\);
- the one-line support-boundary proof
  \[
  \langle k,[c_f]\rangle=\varepsilon\partial s(k)=0;
  \]
- exact balanced flags as relative quadratic unisolvent configurations.

These new formulations require independent mathematical review before they
replace the older presentation in a formal release.

## 17. Current Paper-1 boundary

The smallest coherent first paper should contain:

1. local affine families and the intrinsic obstruction;
2. the quotient sheaf;
3. local and global Fano duality;
4. the support-boundary compatibility proof;
5. the verified CDC extraction;
6. a theorem-to-Lean map and trust-boundary audit.

The broad code-flag/Koszul theory, exact-balanced interpolation, circuit
classifications, interface theory and topological state sums should not block
closure of Paper 1. They may appear as brief outlooks or later companion work.

## 18. Living-document rule

This file states the current best synthesis. When a later structure strictly
improves it, this file should be rewritten rather than merely supplemented.
Superseded arguments remain citable through Git history and specialized notes;
they need not remain in the active narrative.
