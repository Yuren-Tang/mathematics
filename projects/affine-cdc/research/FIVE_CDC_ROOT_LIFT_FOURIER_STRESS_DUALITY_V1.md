# Root-lift controllability, relative stresses, and the Fourier avoidance formula

**Programme:** `AffineCDC — Research Lead`  
**Status:** theorem-level structural checkpoint; not canonical pending Director review and literature audit  
**Parents:** `FIVE_CDC_UNIVERSAL_ORTHOGONAL_ROOT_LIFT_V1.md`, `FIVE_CDC_GAUGE_AS_PIECEWISE_ROOT_TRANSLATION_V1.md`, canonical affine pair-complex formalism

## 1. Purpose

The current five-support search has two apparently different regimes.

1. If the compatible-family / root-lift torsor has enough local freedom, one hopes to choose a lift avoiding a prescribed set of root labels by averaging or direct control.
2. If that freedom is deficient, one expects a harmonic or stress-type obstruction.

These are not separate theories. They are the primal and dual sides of one finite linear map. Moreover, the exact number of lifts avoiding any product set of forbidden fibre values is given by a Fourier sum over the dual relative-stress code.

Thus orbit averaging is the zero-frequency term, while harmonic certificates are precisely the nonzero Fourier frequencies.

## 2. The affine pair differential

Let `G` be a finite loopless graph, let `Gamma` be a finite-dimensional binary vector space, and let

\[
f:E(G)\longrightarrow \Gamma\setminus\{0\}
\]

be a nowhere-zero flow. For an edge `e=uv`, put

\[
Q_e:=\Gamma/\langle f(e)\rangle.
\]

Define

\[
C_f^0:=\Gamma^{V(G)},
\qquad
C_f^1:=\bigoplus_{e\in E(G)}Q_e
\]

and the differential

\[
\delta_f:C_f^0\longrightarrow C_f^1,
\qquad
(\delta_fk)_e=[k_u+k_v]_e.
\]

The admissible vertex-translation space is

\[
H_f^0:=\ker\delta_f.
\]

For every edge,

\[
Q_e^*\cong \operatorname{Ann}(f(e))\leq\Gamma^*.
\]

Under this identification the transpose is

\[
\delta_f^*:\bigoplus_e\operatorname{Ann}(f(e))
\longrightarrow (\Gamma^*)^{V(G)},
\]

\[
\boxed{
(\delta_f^*\psi)_v
=
\sum_{e\ni v}\psi_e.
}
\]

Thus `delta_f^* psi` is the vertex divergence of an edge-covector field whose value on each edge annihilates the flow direction.

## 3. Vertex controllability and relative equilibrium stresses

Fix a vertex set

\[
U\subseteq V(G)
\]

and let

\[
r_U:H_f^0\longrightarrow\Gamma^U
\]

be restriction. For

\[
\alpha\in(\Gamma^*)^U,
\]

write `tilde alpha` for its extension by zero to all vertices.

Define the relative obstruction space

\[
\operatorname{RelOb}_f(U)
:=
\left\{
\alpha\in(\Gamma^*)^U:
\widetilde\alpha\in\operatorname{im}\delta_f^*
\right\}.
\]

### Theorem 3.1 — vertex controllability/stress duality

One has

\[
\boxed{
(\operatorname{im}r_U)^\perp
=
\operatorname{RelOb}_f(U).
}
\]

Consequently:

1. `r_U` is surjective if and only if `RelOb_f(U)=0`;
2. a prescribed translation pattern `a in Gamma^U` extends to an admissible global field if and only if
   \[
   \alpha(a)=0
   \qquad
   (\alpha\in\operatorname{RelOb}_f(U));
   \]
3. the rank defect is exact:
   \[
   \boxed{
   \operatorname{codim}(\operatorname{im}r_U)
   =
   \dim\operatorname{RelOb}_f(U).
   }
   \]

Equivalently, a nonzero obstruction is represented by an edge-covector field

\[
\psi_e\in\operatorname{Ann}(f(e))
\]

whose divergence vanishes outside `U` and equals a nonzero prescribed source pattern on `U`.

#### Proof

For `alpha in (Gamma^*)^U`,

\[
\alpha\perp\operatorname{im}r_U
\]

if and only if its zero extension annihilates `ker delta_f`. Finite-dimensional linear algebra gives

\[
(\ker\delta_f)^\perp
=
\operatorname{im}\delta_f^*.
\]

This is exactly the defining condition for `RelOb_f(U)`. The three consequences follow immediately. ∎

This is the precise Fredholm alternative for local root-triangle translations.

## 4. Edge-fibre evaluation

Fix an edge set

\[
F\subseteq E(G).
\]

For every `e=uv in F`, choose either endpoint `s(e)`. Since `k in H_f^0` satisfies

\[
[k_u]_e=[k_v]_e\in Q_e,
\]

the following map is independent of that choice:

\[
\rho_F:H_f^0\longrightarrow Q_F:=\bigoplus_{e\in F}Q_e,
\qquad
(\rho_Fk)_e=[k_{s(e)}]_e.
\]

For a fixed base root lift `g`, the vector `rho_F(k)` is exactly the change of its root-fibre coordinates on `F` under the gauge translation field `k`.

Let

\[
y=(y_e)_{e\in F}\in Q_F^*
=
\bigoplus_{e\in F}\operatorname{Ann}(f(e)).
\]

Define the one-sided source field

\[
\sigma_F(y)\in(\Gamma^*)^{V(G)}
\]

by placing `y_e` at the chosen endpoint `s(e)` and summing when several selected half-edges meet.

### Theorem 4.1 — edge-fibre controllability/stress duality

One has

\[
\boxed{
y\in(\operatorname{im}\rho_F)^\perp
\iff
\sigma_F(y)\in\operatorname{im}\delta_f^*.
}
\]

Equivalently, `y` is a dual obstruction precisely when there exists an edge-covector field

\[
\psi_e\in\operatorname{Ann}(f(e))
\]

whose vertex divergence equals the one-sided source pattern `sigma_F(y)`.

This condition is independent of the chosen endpoints. Changing the chosen endpoint of one edge changes `sigma_F(y)` by the divergence of the edge field supported on that edge with value `y_e`, and hence does not change membership in `im delta_f^*`.

#### Proof

The map `rho_F` is the restriction to `ker delta_f` of the linear half-edge evaluation map

\[
R_F:C_f^0\to Q_F.
\]

Therefore

\[
y\perp\operatorname{im}\rho_F
\iff
R_F^*y\in(\ker\delta_f)^\perp
\iff
R_F^*y\in\operatorname{im}\delta_f^*.
\]

Under the quotient-dual identification, `R_F^*y=sigma_F(y)`. ∎

Put

\[
\mathcal C_F:=\operatorname{im}\rho_F\leq Q_F
\]

and call it the **root-fibre evaluation code**. Its dual

\[
\mathcal C_F^\perp
\]

is the corresponding **relative stress code**.

## 5. Prescribed and forbidden root values

Let `q_e(g) in Q_e` be the fibre coordinate of the base root lift on edge `e`. Under a translation field `k`,

\[
q_e(g^k)=q_e(g)+(\rho_Fk)_e.
\]

Hence arbitrary prescribed root values on `F` are simultaneously realizable if and only if their difference from the base assignment lies in `mathcal C_F`.

More generally, let

\[
A_e\subseteq Q_e
\]

be any allowed set of final fibre values and put

\[
A:=\prod_{e\in F}(A_e-q_e(g))\subseteq Q_F.
\]

Then a root lift satisfying all edgewise restrictions exists if and only if

\[
\boxed{
\mathcal C_F\cap A\neq\varnothing.
}
\]

If each `A_e` is the complement of one forbidden root value, this is the basic root-avoidance problem.

For a target root set `P subset E(K_8)`, take `F` to be all source edges whose Fano direction occurs in `P`, and let `A_e` be the roots in the corresponding fibre not belonging to `P`. Then a lift avoids every root in `P` exactly when `mathcal C_F cap A` is nonempty.

The three complete positive compression templates

\[
3K_2,
\qquad
K_3\sqcup K_2,
\qquad
K_4
\]

are therefore product-avoidance problems on suitable root fibres.

## 6. Exact Fourier formula

Let

\[
Q=Q_F,
\qquad
C=\mathcal C_F\leq Q.
\]

For `y in Q^*`, write

\[
\chi_y(q):=(-1)^{\langle y,q\rangle}.
\]

For a function `phi:Q->C`, use the unnormalized Fourier transform

\[
\widehat\phi(y)
:=
\sum_{q\in Q}\phi(q)\chi_y(q).
\]

### Theorem 6.1 — root-avoidance Fourier/stress formula

For every allowed set `A subseteq Q`,

\[
\boxed{
|C\cap A|
=
\frac{|C|}{|Q|}
\sum_{y\in C^\perp}
\widehat{\mathbf1_A}(y).
}
\]

If `A=product_e A_e` is a product set, then

\[
\boxed{
\widehat{\mathbf1_A}(y)
=
\prod_{e\in F}
\widehat{\mathbf1_{A_e}}(y_e).
}
\]

Thus every nonzero Fourier term is indexed by a relative stress certificate from Theorem 4.1.

#### Proof

The indicator of the linear code `C` is

\[
\mathbf1_C(q)
=
\frac{|C|}{|Q|}
\sum_{y\in C^\perp}\chi_y(q).
\]

Multiply by `1_A(q)`, sum over `q in Q`, and interchange the sums. Product factorization is ordinary finite Fourier factorization. ∎

The zero character contributes

\[
\frac{|C|}{|Q|}|A|,
\]

which is exactly the uniform-orbit main term. All deviation from uniform averaging is carried by nonzero relative stresses.

## 7. Rank-three one-value avoidance

Assume now

\[
\Gamma=F_2^3.
\]

Then every edge quotient `Q_e` has four elements. Suppose one fibre value `a_e` is forbidden on every edge of `F`, so

\[
A_e=Q_e\setminus\{a_e\}.
\]

For `y_e in Q_e^*`,

\[
\widehat{\mathbf1_{A_e}}(y_e)
=
\begin{cases}
3,&y_e=0,\\
-\chi_{y_e}(a_e),&y_e\neq0.
\end{cases}
\]

Therefore, if `z(y)` is the number of zero coordinates of `y`,

\[
\boxed{
|C\cap A|
=
\frac{|C|}{4^{|F|}}
\sum_{y\in C^\perp}
3^{z(y)}(-1)^{|F|-z(y)}\chi_y(a).
}
\]

In particular, the zero-frequency main term is

\[
|C|\left(\frac34\right)^{|F|}.
\]

A phase-free sufficient condition for positivity is

\[
\boxed{
\sum_{0\neq y\in C^\perp}3^{-\operatorname{wt}(y)}<1.
}
\]

Indeed, after factoring out the zero term `3^{|F|}`, the absolute value of all nonzero corrections is bounded by the left side.

This exhibits a direct code-theoretic route:

- large minimum weight or a sparse weight enumerator in the relative stress code forces an avoiding lift;
- failure of avoidance requires enough low-weight relative stresses to cancel the uniform term.

## 8. Strategic interpretation

The earlier proposed dichotomy is now one theorem rather than two projects.

### Primal side

Study the image code

\[
\mathcal C_F=\operatorname{im}\rho_F
\]

and show that enough root-fibre assignments are attainable. Direct surjectivity is the strongest form; Fourier positivity is a weaker and more realistic criterion.

### Dual side

If the image is deficient or an avoidance count vanishes, the nonzero terms lie in

\[
\mathcal C_F^\perp,
\]

whose elements are exactly relative stress fields with prescribed half-edge sources. These are not an unrelated fallback: they are the Fourier spectrum of the same orbit problem.

Thus the durable next target is:

\[
\boxed{
\text{bound the relative-stress weight enumerators attached to the three compression templates.}
}
\]

A proof that at least one template has positive Fourier count would produce a five-support lift for the fixed Fano flow. A counterexample would require all three template families to have exact cancellation, thereby yielding a structured collection of low-weight relative stresses.

## 9. Relation to existing gauge circuits

The canonical gauge code `B_f` describes the moduli of complete root lifts modulo global translations. The present relative stress codes are dual codes attached to projections of that torsor onto selected root fibres.

They should not be identified blindly:

- gauge circuits classify minimal piecewise-translation interfaces in the source graph;
- relative stress words classify minimal Fourier dependencies among selected root-fibre evaluations.

They are paired through the same affine complex. Low-weight gauge circuits may enlarge the primal orbit, while low-weight relative stresses create the only possible Fourier obstruction.

This explains why classifying gauge circuits by cardinality alone cannot close the five-support problem, but also why the gauge and stress programmes remain mathematically inseparable.

## 10. Reliability boundary and next calculations

The linear-duality and Fourier identities are complete finite-dimensional arguments. No probabilistic independence is assumed.

The next computational tasks are exact and well suited to independent backends:

1. construct `rho_F` and `C_F^perp` over `F_2` for explicit Fano flows;
2. compute relative-stress weight enumerators for all three template orbits;
3. verify the Fourier count against direct enumeration of the root-lift torsor;
4. search for flows for which every template count vanishes;
5. extract compact dual certificates when a count is zero.

These calculations may be performed in Python and independently cross-checked in Wolfram Language using exact `Modulus -> 2` linear algebra and finite graph routines.