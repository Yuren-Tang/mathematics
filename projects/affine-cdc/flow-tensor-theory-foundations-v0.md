# Flow tensor theory — foundational draft v0

**Date:** 2026-07-14  
**Status:** definition-level research draft; not yet Lean-formalized.

The theory separates three layers:

1. an abstract based linear datum;
2. graphical realizations;
3. affine enhancements carrying a distinguished obstruction class.

## 1. Based quotient datum

Let $E$ be finite and put $U_E=\mathbf F_2^E$ with its distinguished basis.
A based quotient datum is a pair of surjections

$$
U_E\xrightarrow{\pi}Q\xrightarrow{F}\Gamma.
$$

Write $q_e=\pi(e)$ and $f_e=F(q_e)$. It is nondegenerate when every $q_e$
and $f_e$ is nonzero. The basis of $U_E$ is essential structure.

## 2. Tensor operator

The basis diagonal is

$$
\Delta_E(e)=e\otimes e.
$$

Define

$$
T_{\pi,F}
=
(F\otimes\operatorname{id}_Q)(\pi\otimes\pi)\Delta_E,
$$

so

$$
T_{\pi,F}(\lambda)=\sum_e\lambda_e f_e\otimes q_e.
$$

## 3. Wedge differential and tensor complex

Define

$$
W_F(a\otimes q)=a\wedge F(q).
$$

Since $W_F(f_e\otimes q_e)=f_e\wedge f_e=0$,

$$
W_FT_{\pi,F}=0.
$$

Thus

$$
C(\pi,F):
\quad
U_E\xrightarrow{T_{\pi,F}}\Gamma\otimes Q
\xrightarrow{W_F}\Lambda^2\Gamma
$$

is the flow tensor complex.

## 4. Tensor homology and index

Define

$$
H_0(\pi,F)=\ker T_{\pi,F},
\qquad
H_1(\pi,F)=\ker W_F/\operatorname{im}T_{\pi,F}.
$$

If $m=|E|$, $q=\dim Q$, and $r=\dim\Gamma$, then

$$
\dim H_0-\dim H_1
=
m-rq+\binom r2.
$$

Call this the tensor index:

$$
\operatorname{ind}(\pi,F)=m-rq+\binom r2.
$$

## 5. Constraint matroid

The columns $f_e\otimes q_e$ represent a binary matroid
$M^\otimes(\pi,F)$ with cycle space

$$
\mathcal C(M^\otimes)=H_0(\pi,F).
$$

Hence minimal flexibility supports are circuits and rigidity means that this
matroid is free.

The dual map satisfies

$$
T_{\pi,F}^*(\ell\otimes c)(e)=\ell(f_e)c(q_e),
$$

so its row space is the coordinatewise product of the two represented linear
systems.

## 6. Balanced data and torsion

The datum is balanced if

$$
\operatorname{ind}(\pi,F)=0.
$$

Then $U_E$ and $\ker W_F$ have equal dimension. Define

$$
\Theta_{\pi,F}
=
\bigwedge_{e\in E}(f_e\otimes q_e)
\in\det(\ker W_F).
$$

Over $\mathbf F_2$ this has no ordering-sign ambiguity. Its binary torsion is
nonzero exactly when the balanced complex is exact:

$$
\Theta_{\pi,F}\ne0
\iff
H_0(\pi,F)=0
\iff
H_1(\pi,F)=0.
$$

## 7. Divided-square exact sequence

Let $K=\ker F$ and

$$
D^2\Gamma
=
\ker(\Gamma\otimes\Gamma\to\Lambda^2\Gamma).
$$

There is a canonical short exact sequence

$$
0\to\Gamma\otimes K
\to\ker W_F
\to D^2\Gamma
\to0.
$$

The edge column maps to $f_e\otimes f_e$. This is the intrinsic quadratic or
Veronese part of every determinant expansion.

## 8. Graphical realization

For a connected graph $G$, let

$$
Q_G=\mathbf F_2^E/\mathcal C(G)^\perp
\cong\mathcal C(G)^*.
$$

A binary flow induces $F_f:Q_G\to\Gamma$, $F_f(\bar e)=f(e)$.

At this layer:

- $H_0$ is the gauge-moduli code;
- $H_1^*$ is the essential equilibrium-stress space;
- circuits become harmonic cut quotients;
- graph cuts become cycle-space pullbacks and cographic pushouts.

For a connected cubic graph with $n$ vertices and a spanning rank-$r$ flow,

$$
\operatorname{ind}(G,f)
=
\frac{(3-r)(n-r)}2.
$$

Since $r\le n/2+1$, rank three is the unique balanced rank in the nontrivial
cubic range.

## 9. Affine enhancement

The bare tensor complex does not determine an affine compatibility problem.

An affine enhancement is a distinguished class

$$
\kappa\in H_1(\pi,F).
$$

It is compatible when $\kappa=0$.

AffineCDC supplies a specific class $\kappa_f$. The rank-three branching and
Hodge theorem proves $\kappa_f=0$.

## 10. Hodge enhancement

A Hodge enhancement is additional structure giving

$$
H_0(\pi,F)\cong H_1(\pi,F)^*.
$$

For cubic graphical rank-three data, the Fano volume form supplies this
duality.

Thus the Fano case combines:

1. balancedness;
2. Hodge self-duality;
3. vanishing of the distinguished affine class.

These are logically distinct.

## 11. Morphisms

Coefficient quotients $g:\Gamma\twoheadrightarrow\Gamma'$ give ordinary
morphisms of complexes and long exact sequences.

Graph cuts have mixed variance:

- edge-coordinate pullbacks;
- cycle-space fiber products;
- cographic pushouts.

They should be modelled by spans or linear correspondences, not only ordinary
chain maps.

## 12. Minimal vocabulary

The current foundational vocabulary is:

1. based quotient datum;
2. tensor operator;
3. flow tensor complex;
4. tensor homology;
5. tensor index;
6. constraint matroid;
7. balanced datum and torsion;
8. graphical realization;
9. affine enhancement;
10. Hodge enhancement;
11. coefficient morphism;
12. interface correspondence.

The first seven form the abstract linear core.

## 13. Theorem hierarchy

### Abstract layer

1. $W_FT_{\pi,F}=0$.
2. Tensor index formula.
3. Constraint-matroid interpretation.
4. Divided-square exact sequence.
5. Balanced torsion criterion.
6. Coefficient-quotient long exact sequence.

### Graphical layer

7. Gauge code equals $H_0$.
8. Essential stresses equal $H_1^*$.
9. Harmonic cut-quotient characterization.
10. Interface pullback-pushout correspondence.

### Rank-three Fano layer

11. Cubic rank-three balance.
12. Local Fano Hodge isomorphism.
13. Global Hodge self-duality.
14. Vanishing of the AffineCDC class.
15. Cycle-double-cover extraction.

## 14. Validation tests

Before treating this as a new mathematical framework, four tests are required:

1. **External examples:** natural based quotient data beyond the present CDC
   construction.
2. **Recognition:** comparison with Khatri--Rao, Segre, rigidity, sheaf and
   Koszul constructions.
3. **Functorial closure:** composition and naturality of coefficient morphisms
   and graphical correspondences.
4. **Payoff:** at least one theorem must become materially shorter or stronger
   through the framework.

The framework should be judged by these tests, not by terminological elegance.
