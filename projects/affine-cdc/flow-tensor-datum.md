# The flow tensor datum as the master object

**Date:** 2026-07-14  
**Status:** theorem-level structural draft; not yet Lean-formalized.

Let $G$ be a finite connected graph, let

$$
U_E:=\mathbf F_2^E,
$$

and let $\mathcal C(G)\le U_E$ be the binary cycle space. Put

$$
Q_G:=U_E/\mathcal C(G)^\perp
\cong \mathcal C(G)^*,
$$

with quotient map

$$
\pi_G:U_E\to Q_G.
$$

Let

$$
f:E(G)\to\Gamma
$$

be a binary flow whose values span $\Gamma$. Extending $f$ linearly gives

$$
\widehat f:U_E\to\Gamma.
$$

Because every coordinate of $f$ is a binary cycle, $\widehat f$ vanishes on
$\mathcal C(G)^\perp$. Hence it factors canonically through $Q_G$:

$$
\widehat f=F_f^*\pi_G,
\qquad
F_f^*:Q_G\to\Gamma.
$$

The basic object is therefore the pointed quotient datum

$$
\boxed{
\mathfrak T(G,f)
=
\left(
U_E\xrightarrow{\pi_G}Q_G\xrightarrow{F_f^*}\Gamma
\right),
}
$$

where $U_E$ retains its distinguished edge basis.

## 1. The edge diagonal and the tensor operator

The distinguished basis defines the linear edge-diagonal map

$$
\Delta_E:U_E\to U_E\otimes U_E,
\qquad
\Delta_E(e)=e\otimes e.
$$

Define

$$
T_f
:=
(F_f^*\otimes\operatorname{id}_{Q_G})
(\pi_G\otimes\pi_G)\Delta_E.
$$

Thus

$$
\boxed{
T_f(\lambda)
=
\sum_{e\in E}
\lambda_e\,f(e)\otimes\bar e,
}
$$

where $\bar e=\pi_G(e)$.

This factorization shows exactly which data $T_f$ uses:

1. the edge basis;
2. the cographic quotient $\pi_G$;
3. the flow quotient map $F_f^*$.

It is therefore intrinsic to the flow-labelled graph, not to any chosen
cycle-space basis.

## 2. The wedge operator

Define

$$
W_f:\Gamma\otimes Q_G\to\Lambda^2\Gamma,
\qquad
W_f(a\otimes q)=a\wedge F_f^*(q).
$$

For each edge basis vector,

$$
W_fT_f(e)
=
f(e)\wedge f(e)
=
0.
$$

Hence

$$
\boxed{
W_fT_f=0.
}
$$

The resulting flow tensor complex is

$$
\boxed{
U_E
\xrightarrow{T_f}
\Gamma\otimes Q_G
\xrightarrow{W_f}
\Lambda^2\Gamma.
}
$$

The map $W_f$ is the first wedge/Koszul-type differential associated with the
surjection $F_f^*:Q_G\to\Gamma$.

## 3. Homology dictionary

Define

$$
H_0(\mathfrak T_f):=\ker T_f
$$

and

$$
H_1(\mathfrak T_f):=\ker W_f/\operatorname{im}T_f.
$$

Then

$$
\boxed{
H_0(\mathfrak T_f)=\mathcal B_f,
}
$$

the homogeneous gauge-moduli code.

Moreover,

$$
\boxed{
H_1(\mathfrak T_f)^*
\cong
\operatorname{EssStress}(f),
}
$$

the equilibrium-stress space modulo canonical alternating stresses.

The affine gluing obstruction defines a canonical class

$$
\boxed{
\kappa_f\in H_1(\mathfrak T_f),
}
$$

and

$$
\boxed{
\delta_fm=c_f
\text{ is solvable}
\iff
\kappa_f=0.
}
$$

Thus flexibility and obstruction are the two homology groups of one tensor
datum.

## 4. The dual map and the Schur code

Using

$$
Q_G^*\cong\mathcal C(G),
$$

the dual of $T_f$ is

$$
T_f^*:\Gamma^*\otimes\mathcal C(G)\to U_E^*.
$$

On a pure tensor,

$$
T_f^*(\ell\otimes c)(e)
=
\ell(f(e))\,c(e).
$$

Therefore

$$
\boxed{
\operatorname{im}T_f^*
=
\mathcal C(G)*\mathcal F_f,
}
$$

where

$$
\mathcal F_f
=
\{\ell\circ f:\ell\in\Gamma^*\}.
$$

Consequently,

$$
\boxed{
\mathcal B_f
=
(\mathcal C(G)*\mathcal F_f)^\perp.
}
$$

The Schur-code theorem is therefore simply the row-space description of the
master tensor operator.

## 5. Constraint matroid

The edge columns

$$
t_e=f(e)\otimes\bar e
$$

represent a binary matroid

$$
M_f^\otimes.
$$

Its cycle space is

$$
\mathcal C(M_f^\otimes)=\ker T_f=\mathcal B_f,
$$

and its cocycle space is

$$
\mathcal C^*(M_f^\otimes)
=
\mathcal C(G)*\mathcal F_f.
$$

Hence:

- nonzero gauge modes are matroid cycles;
- inclusion-minimal gauge supports are circuits;
- circuit elimination follows automatically;
- gauge rigidity is equivalent to $M_f^\otimes$ being free.

Thus the support family does not require a second new matroid: it is already
the circuit geometry of the flow constraint matroid.

## 6. Harmonic cut quotients as circuit geometry

Let $\lambda\in\ker T_f$ and let

$$
S=\operatorname{supp}\lambda.
$$

The corresponding gauge potential is constant on the components of $G-S$.
Contracting those components gives a quotient graph $Q_S$ on which the induced
edge labels are simultaneously:

- a nowhere-zero flow;
- an exact tension.

Therefore every codeword has a harmonic cut quotient.

Conversely every compatible harmonic cut quotient gives a codeword in
$\ker T_f$.

For a circuit $\lambda$, the quotient is support-minimal. Thus harmonic cut
quotients are the geometric realization of the circuits of $M_f^\otimes$.

They should not be regarded as a separate linear localization theory unless an
additional universal property is later established.

## 7. Rank, torsion and exactness

The rank of $T_f$ measures the number of independent edge constraints:

$$
\operatorname{rank}T_f
=
|E|-\dim\mathcal B_f.
$$

For cubic rank-three flows,

$$
\dim U_E=\dim\ker W_f=|E|.
$$

Hence $T_f$ induces a square map

$$
\overline T_f:U_E\to\ker W_f.
$$

Its top exterior product is

$$
\Theta_f
=
\bigwedge_{e\in E}
\bigl(f(e)\otimes\bar e\bigr)
\in
\det(\ker W_f).
$$

Then

$$
\boxed{
\Theta_f\ne0
\iff
H_0(\mathfrak T_f)=0
\iff
H_1(\mathfrak T_f)=0.
}
$$

The binary Fano torsion is therefore the balanced-rank determinant of the
master tensor complex.

## 8. Fano Hodge duality

In rank three, the volume form gives a canonical duality

$$
H_0(\mathfrak T_f)
\cong
H_1(\mathfrak T_f)^*.
$$

Equivalently,

$$
\mathcal B_f
\cong
\operatorname{EssStress}(f).
$$

Thus the rank-three theory is a self-dual balanced tensor complex:

- $H_0$ records gauge flexibility;
- $H_1$ records essential obstruction directions;
- Fano Hodge identifies them;
- the branching theorem proves that the distinguished affine class
  $\kappa_f$ vanishes.

## 9. Functorial shadows

The same master object produces the previously discovered structures:

| Shadow of $\mathfrak T(G,f)$ | Result |
|---|---|
| $\ker T_f$ | gauge-moduli code |
| $\operatorname{im}T_f^*$ | Schur product $\mathcal C*\mathcal F_f$ |
| column matroid of $T_f$ | flow constraint matroid |
| circuits of that matroid | minimal harmonic cut quotients |
| rank of $T_f$ | rigidity defect |
| middle homology | essential obstruction space |
| affine class in middle homology | compatibility obstruction |
| top wedge in balanced rank | Fano torsion |
| adapted-coordinate expansion | Fano basis-packing parity |
| gluing exact sequences | 2-edge and 3-edge factorization |

This is the sense in which the flow tensor datum is the master object rather
than merely another consequence of the CDC construction.

## 10. Next structural questions

The natural next problems are:

1. characterize morphisms of flow tensor data;
2. derive deletion, contraction and cut-gluing exact sequences directly at the
   tensor-complex level;
3. classify circuits of $M_f^\otimes$ through harmonic cut quotients;
4. determine whether $T_f$ is a known diagonal tensor/Khatri–Rao matroid
   construction;
5. construct a universal lift over $\mathbf Z$ or a polynomial ring whose
   determinant refines the binary Fano torsion;
6. formalize the master diagram in Lean before its API fragments into separate
   ad hoc modules.
