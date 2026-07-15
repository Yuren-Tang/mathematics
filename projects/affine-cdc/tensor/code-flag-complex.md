# Based quotient data, code flags, and the tensor complex

**Status.** The linear-algebra statements in this chapter are theorem-level.
The name “mixed Schur–Koszul complex” is descriptive and provisional. The
construction must be compared carefully with the existing literature on Schur
products, Koszul complexes, diagonal tensor products, Khatri–Rao matrices, and
represented matroid quotients before any novelty claim is made.

This chapter abstracts the tensor reduction from its graphical source. It does
not replace the affine incidence geometry or retain the cycle-double-cover
output data.

## 1. Based quotient data

Let $E$ be a finite set and put

$$
A:=\mathbf F_2^E
$$

with its distinguished coordinate basis. A **based quotient datum** is a pair of
surjections

$$
\boxed{
A\xrightarrow{\pi}Q\xrightarrow{F}\Gamma.
}
$$

Write

$$
q_e:=\pi(e),
\qquad
f_e:=F(q_e).
$$

The datum is nondegenerate when every $q_e$ and $f_e$ is nonzero. The basis is
part of the structure: the tensor operator uses the basis diagonal

$$
\Delta_E:A\longrightarrow A\otimes A,
\qquad
\Delta_E(e)=e\otimes e.
$$

## 2. Tensor and wedge operators

Define

$$
T_{\pi,F}
:=(F\otimes\operatorname{id}_Q)
(\pi\otimes\pi)\Delta_E.
$$

Thus

$$
\boxed{
T_{\pi,F}(\lambda)
=
\sum_{e\in E}\lambda_ef_e\otimes q_e.
}
$$

Define

$$
W_F:\Gamma\otimes Q\longrightarrow\Lambda^2\Gamma,
\qquad
W_F(a\otimes q)=a\wedge F(q).
$$

For every edge column,

$$
W_F(f_e\otimes q_e)=f_e\wedge f_e=0,
$$

so

$$
W_FT_{\pi,F}=0.
$$

The associated tensor complex is

$$
\boxed{
\mathcal T(\pi,F):
A
\xrightarrow{T_{\pi,F}}
\Gamma\otimes Q
\xrightarrow{W_F}
\Lambda^2\Gamma.
}
$$

Write

$$
H_0(\pi,F):=\ker T_{\pi,F},
$$

and

$$
H_1(\pi,F):=\ker W_F/\operatorname{im}T_{\pi,F}.
$$

Because $F$ is surjective, $W_F$ is surjective.

## 3. Index and balanced data

Let

$$
m:=|E|,
\qquad
q:=\dim Q,
\qquad
r:=\dim\Gamma.
$$

Euler characteristic gives

$$
\boxed{
\dim H_0(\pi,F)-\dim H_1(\pi,F)
=
m-rq+\binom r2.
}
$$

Define the tensor index by

$$
\operatorname{ind}(\pi,F)
:=
m-rq+\binom r2.
$$

The datum is **balanced** when this index is zero. Balancedness is a dimension
condition; exactness is the stronger assertion that both homology groups
vanish.

## 4. Duality with nested code flags

Use the standard pairing to identify $A\cong A^*$. Dualizing the two
surjections gives inclusions

$$
\Gamma^*\xrightarrow{F^*}Q^*\xrightarrow{\pi^*}A.
$$

Define

$$
D:=\pi^*F^*(\Gamma^*),
\qquad
C:=\pi^*(Q^*).
$$

Then

$$
\boxed{D\subseteq C\subseteq A}
$$

is a flag of binary linear codes.

Conversely, given a code flag $D\subseteq C\subseteq A$, put

$$
Q:=C^*,
\qquad
\Gamma:=D^*.
$$

Define

$$
\pi:A\longrightarrow C^*,
\qquad
\pi(x)(c)=\langle x,c\rangle,
$$

and let $F:C^*\to D^*$ be restriction. Both are surjective. Hence, up to the
canonical coordinate identifications,

$$
\boxed{
\text{based quotient data}
\simeq
\text{nested binary code flags }D\subseteq C\subseteq A.
}
$$

The quotient language makes the tensor columns transparent; the code-flag
language makes Schur multiplication and symmetries transparent.

## 5. The dual Schur–Koszul complex

Dualizing the tensor complex and using the code-flag identifications gives

$$
\boxed{
\Lambda^2D
\xrightarrow{\kappa}
D\otimes C
\xrightarrow{\mu}
A.
}
$$

The second map is coordinatewise multiplication:

$$
\boxed{
\mu(d\otimes c)=d*c.
}
$$

The first map is

$$
\boxed{
\kappa(d_1\wedge d_2)
=
d_1\otimes d_2+d_2\otimes d_1,
}
$$

where the second tensor factor uses $D\subseteq C$. Commutativity and
characteristic two give $\mu\kappa=0$.

The image of $\mu$ is the Schur product code

$$
C*D.
$$

Consequently,

$$
\boxed{
H_0(\pi,F)=(C*D)^\perp,
}
$$

and

$$
\boxed{
H_1(\pi,F)^*
\cong
\ker\mu/\operatorname{im}\kappa.
}
$$

Thus the dual of the middle tensor homology is the space of first syzygies of
Schur multiplication modulo the universal commutativity relations.

The phrase **mixed Schur–Koszul complex** refers to this truncated complex. It
is not asserted to be established terminology.

## 6. Relative quadratic evaluation

Define

$$
\mathcal Q(D,C)
:=
(D\otimes C)/\kappa(\Lambda^2D).
$$

Schur multiplication descends to an evaluation map

$$
\operatorname{ev}_{D,C}:\mathcal Q(D,C)\longrightarrow A.
$$

Then

$$
\ker\operatorname{ev}_{D,C}
\cong
H_1(\pi,F)^*,
$$

while

$$
\operatorname{coker}\operatorname{ev}_{D,C}
\cong
H_0(\pi,F)^*.
$$

Therefore a balanced datum is exact if and only if the relative quadratic
classes in $\mathcal Q(D,C)$ are uniquely determined by their coordinate
evaluations. This is the precise unisolvence content behind the determinant and
torsion theory. It is downstream from compatibility: singular evaluation does
not prevent the distinguished AffineCDC class from vanishing in rank three.

## 7. The constraint matroid

The edge columns

$$
t_e:=f_e\otimes q_e
$$

represent a binary matroid

$$
M^\otimes(\pi,F)
$$

on ground set $E$. Its cycle code is

$$
\boxed{
\mathcal C(M^\otimes)=\ker T_{\pi,F}=H_0(\pi,F),
}
$$

and its cocycle code is

$$
\boxed{
\mathcal C^*(M^\otimes)=C*D.
}
$$

Thus:

- nonzero degree-zero classes are matroid cycles;
- inclusion-minimal supports are circuits;
- circuit elimination is automatic;
- rigidity is equivalent to the constraint matroid being free.

The matroid depends only on the nested code flag, not on chosen generator
matrices.

## 8. Represented matroid quotients

The columns $q_e$ represent a binary matroid $M$ in $Q$. Their images $f_e$
represent a lower-rank binary matroid $N$ in $\Gamma$. Every dependency among
the $q_e$ remains a dependency among the $f_e$, so $N$ is a represented
identity-ground-set quotient of $M$, equivalently a strong-map image in the
representable binary setting.

The tensor columns $f_e\otimes q_e$ are therefore attached to a represented
matroid quotient

$$
M\twoheadrightarrow N
$$

together with the common distinguished ground set. In a graphical realization,
$M$ is the cographic representation arising from the cycle code.

## 9. The diagonal coalgebra and strict morphisms

The distinguished basis of $A$ is equivalently encoded by

$$
\Delta_E(e)=e\otimes e,
\qquad
\varepsilon_E(e)=1.
$$

### Proposition 9.1

A linear map

$$
\phi:\mathbf F_2^E\longrightarrow\mathbf F_2^{E'}
$$

satisfies

$$
\Delta_{E'}\phi=(\phi\otimes\phi)\Delta_E
$$

if and only if every basis vector is sent either to zero or to one basis
vector. If it also preserves the counit, every basis vector is sent to a basis
vector. Hence counital diagonal-coalgebra maps are exactly set maps

$$
E\longrightarrow E'.
$$

### Proof

Write $\phi(e)=\sum_ja_jj$. Comparing $\Delta\phi(e)$ with
$(\phi\otimes\phi)\Delta(e)$ forces every off-diagonal coefficient $a_ja_k$ to
vanish. Thus at most one coefficient is nonzero, and counitality forces it to
be one. $\square$

A strict morphism of based quotient data

$$
(A\xrightarrow{\pi}Q\xrightarrow{F}\Gamma)
\longrightarrow
(A'\xrightarrow{\pi'}Q'\xrightarrow{F'}\Gamma')
$$

is a triple $(\phi,\alpha,\beta)$ in which $\phi$ is a counital diagonal map and

$$
\alpha\pi=\pi'\phi,
\qquad
\beta F=F'\alpha.
$$

The induced maps satisfy

$$
(\beta\otimes\alpha)T_{\pi,F}
=
T_{\pi',F'}\phi
$$

and

$$
(\Lambda^2\beta)W_F
=
W_{F'}(\beta\otimes\alpha),
$$

so every strict morphism induces a chain map.

In code-flag language, a set map $s:E\to E'$ defines a strict morphism exactly
when its coordinate pullback satisfies

$$
s^*(C')\subseteq C,
\qquad
s^*(D')\subseteq D.
$$

## 10. Automorphisms

An automorphism must be a permutation of $E$. Hence

$$
\boxed{
\operatorname{Aut}(D\subseteq C\subseteq\mathbf F_2^E)
=
\{\sigma\in\operatorname{Sym}(E):\sigma C=C,\ \sigma D=D\}.
}
$$

There are no additional hidden linear automorphisms of $Q$ or $\Gamma$: the
surjections force those maps once the coordinate permutation is fixed.

For a flow-labelled graph,

$$
C=\mathcal C(G),
\qquad
D=\mathcal F_f
:=\{\ell\circ f:\ell\in\Gamma^*\}.
$$

Graph automorphisms preserving the flow up to coefficient automorphism form a
subgroup of the code-flag automorphism group. The full group may be larger,
because a cycle-matroid automorphism need not come from a vertex automorphism
of one graph realization.

## 11. Graphical and affine enhancements

For a connected graph with a spanning binary flow, take

$$
Q=Q_G:=\mathbf F_2^E/\mathcal C(G)^\perp,
\qquad
F=F_f.
$$

Then

$$
C=\mathcal C(G),
\qquad
D=\mathcal F_f.
$$

At this layer:

- $H_0$ is the gauge-moduli code;
- $H_1^*$ is the essential-stress space;
- constraint-matroid circuits are harmonic cut quotients;
- coefficient quotients give ordinary chain maps;
- graph interfaces act by mixed-variance correspondences;
- an affine enhancement is a distinguished class in $H_1$.

The bare code flag does not determine the AffineCDC affine class. It also need
not remember vertices, a particular graph realization, local affine families,
darts, embeddings, or surfaces. Those are additional graphical, affine, or
topological enhancements.

## 12. Partial maps and the categorical boundary

Dropping counitality permits basis vectors to map to zero, giving partial set
maps. These are candidates for deletion-like operations. Graph deletion and
contraction, however, change cycle spaces in opposite variance and generally
require spans, correspondences, or bicartesian diagrams rather than only strict
chain maps.

The established strict category therefore covers coordinate maps preserving
both levels of the code flag. A complete category containing graph cuts,
deletion, contraction, affine classes, and Hodge enhancements remains a
programme.

## 13. Recognition and novelty boundary

The following are established internally:

- the tensor and dual complexes;
- the code-flag equivalence;
- the homology and index formulas;
- the Schur-product row space;
- the constraint matroid;
- strict morphisms and automorphisms.

The following require external validation before publication as a general new
theory:

1. comparison with standard Schur-product and syzygy constructions;
2. comparison with Koszul, Segre, Khatri–Rao, and diagonal tensor complexes;
3. examples not reverse-engineered from AffineCDC;
4. a theorem materially strengthened or shortened by the abstraction;
5. a stable correspondence theory for graph operations.

The abstract branch should be judged by these tests, not by the elegance of its
terminology.