# DDD route-lock quotient and quadratic transgression

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Parents:**

- `projects/affine-cdc/research/OCTAHEDRAL_OVERLAP_TRANSPORT_V1.md`;
- `projects/affine-cdc/research/DDD_COHOMOLOGY_GENERATOR_V1.md`.

**Status:** exact finite algebraic theorem; the physical orientation law and bounded graph localisation remain open.  
**Not implied:** canonical acceptance, independent audit, Lean verification, manuscript readiness, or the global five-support theorem.

---

## 1. The DDD four-point quotient

Fix the DDD matching

\[
M_0=\{r_1,r_2\},
\qquad
r_1=12,
\qquad
r_2=34,
\]

and put

\[
c=r_1+r_2=1234.
\]

Let

\[
E_4=\{x\in\mathbf F_2^{\{1,2,3,4\}}:|x|\equiv0\pmod2\}
\subset E_5.
\]

The vector `c` is the radical vector of the restriction of the polar form to `E_4`, and

\[
q(c)=0.
\]

Hence the quadratic form descends to

\[
Q=E_4/\langle c\rangle\cong\mathbf F_2^2.
\]

The four quotient points are

\[
O=\{0,c\},
\qquad
B=\{12,34\}=M_0,
\]

and the two crossed matchings

\[
X=\{13,24\},
\qquad
Y=\{14,23\}.
\]

Thus the four points of `Q` are exactly

\[
\boxed{O,B,X,Y.}
\]

The descended quadratic form `bar q` is anisotropic:

\[
\bar q(O)=0,
\qquad
\bar q(B)=\bar q(X)=\bar q(Y)=1.
\]

The three nonzero points are the three perfect matchings of `K_4`; `O` is the zero/co-root defect coset.

---

## 2. Linear action of the DDD stabiliser

Let

\[
D_8=\operatorname{Stab}_{S_4}(M_0)
\]

with generators

\[
a=(12),
\qquad
b=(34),
\qquad
p=(13)(24).
\]

Write

\[
g=a^{\epsilon_1}b^{\epsilon_2}p^\sigma.
\]

Define the two characters

\[
\kappa(g)=\epsilon_1+\epsilon_2,
\qquad
\chi(g)=\sigma.
\]

Here `kappa` is internal-flip parity and `chi` is exchange of the two bad root sheets.

### Theorem 2.1 — action on the matching quotient

The linear `D_8` action on `Q` satisfies:

1. `O` and `B` are fixed;
2. `X` and `Y` are exchanged exactly when `kappa(g)=1`;
3. the sheet-exchange character `chi` acts trivially on the four quotient points.

### Proof

The generators `a` and `b` each exchange the two crossed perfect matchings and preserve `M_0`; their product preserves both crossed matchings. The pair exchange `p` preserves each perfect matching setwise. The zero/co-root coset is fixed because `c` is `D_8`-fixed.

---

## 3. Quotient of the explicit DDD cocycle

The explicit generator from `DDD_COHOMOLOGY_GENERATOR_V1.md` is

\[
\alpha(g)=\epsilon_1r_2+\epsilon_2r_1.
\]

Modulo `c`, the two bad roots represent the same quotient point:

\[
\bar r_1=\bar r_2=B.
\]

Therefore:

### Theorem 3.1 — route-lock translation

\[
\boxed{
\bar\alpha(g)=\kappa(g)B
\in Q.
}
\]

Define the affine action

\[
A_g(x)=gx+\bar\alpha(g)
\qquad(x\in Q).
\]

Then:

\[
\boxed{
A_g(X)=X,
\qquad
A_g(Y)=Y
\quad\text{for every }g\in D_8,
}
\]

while

\[
\boxed{
A_g(O),A_g(B)
=
\begin{cases}
(O,B),&\kappa(g)=0,\\
(B,O),&\kappa(g)=1.
\end{cases}}
\]

Thus the affine cocycle locks the two crossed route classes pointwise in the quotient and confines all non-root motion to the defect/bad-route pair `O,B`.

### Mechanistic interpretation

The quotient action is not a generic affine `D_8` action. It has exactly:

- two globally fixed crossed root routes;
- one two-point bad/defect orbit.

This is the intrinsic finite geometry of DDD route lock.

---

## 4. Full root-orbit statement

Return to `E_4`. Let

\[
g\star x=gx+\alpha(g).
\]

### Theorem 4.1 — crossed root invariance

Each crossed matching is invariant under the affine action:

\[
\boxed{
g\star X=X,
\qquad
g\star Y=Y.}
\]

The four-point set

\[
L=\{0,r_1,r_2,c\}=\langle r_1,r_2\rangle
\]

is one invariant affine orbit containing exactly the two roots of the original matching together with zero and the co-root `c`.

Consequently, inside `E_4`, the vectors whose entire affine `D_8` orbit remains root-valued are exactly

\[
\boxed{X\cup Y.}
\]

The original matching `B` is the unique route class whose affine orbit meets the defect set.

### Proof

The quotient theorem gives invariance of the crossed cosets and exchange of the two bad cosets. Translation by `c` only exchanges the two roots inside either crossed matching, so no crossed root leaves its matching. The orbit of zero under the affine action is `L`; it contains `0,c,r_1,r_2`. No element of `B` has an all-root orbit.

---

## 5. Uniqueness modulo simultaneous sheet swap

For `g in D_8`, consider translations `v in E_4` such that

\[
x\longmapsto gx+v
\]

preserves both crossed matching sets `X` and `Y` individually.

### Theorem 5.1 — exact locking fibre

\[
\boxed{
\{v:gX+v=X\text{ and }gY+v=Y\}
=
\alpha(g)+\{0,c\}.
}
\]

### Proof

In `Q`, preserving `X` and `Y` individually determines a unique translation: it must be `kappa(g)B=bar alpha(g)`. The two lifts of this quotient translation to `E_4` differ by the radical vector `c`. Both lifts preserve each crossed matching setwise, because translation by `c` exchanges the two antipodal roots inside every perfect matching.

### Consequence 5.2

The physical route-lock correction is canonical modulo one simultaneous crossed-sheet swap. Choosing the orientation of one crossed matching selects one of the two lifts.

This isolates the exact datum still missing from the overlap transport: the enriched physical word must determine whether the lift is `alpha(g)` or `alpha(g)+c`.

---

## 6. Classification of route-locking cocycles

Let

\[
z:D_8\to E_4
\]

be a cocycle such that every affine map

\[
x\mapsto gx+z(g)
\]

preserves both crossed matching sets individually.

By Theorem 5.1 there is a function

\[
\eta:D_8\to\mathbf F_2
\]

with

\[
z(g)=\alpha(g)+\eta(g)c.
\]

Because `c` is fixed and both `z` and `alpha` are cocycles, `eta` is a character. Hence

\[
\eta=u\chi+v\kappa,
\qquad u,v\in\mathbf F_2.
\]

The following coboundary identities are exact:

\[
\boxed{\chi(g)c=r_1+gr_1,}
\]

and, for `x=13` in the crossed matching `X`,

\[
\boxed{
\alpha(g)+\kappa(g)c=x+gx.
}
\]

Therefore:

### Theorem 6.1 — orientation fork

For a route-locking cocycle

\[
z=\alpha+(u\chi+v\kappa)c,
\]

its cohomology class is

\[
\boxed{
[z]=(1+v)[\alpha]
\in H^1(D_8,E_5).
}
\]

In particular:

- adding the ordinary sheet-exchange character `chi c` is gauge-trivial;
- adding `c` on every internal twist, namely `kappa c`, cancels the exceptional DDD class;
- the existence of the nontrivial DDD class is decided exactly by the physical internal-twist orientation law.

This is the sharp form of the remaining ambiguity. Bare sheet exchange is not the obstruction. The only decisive question is whether an internal endpoint twist simultaneously flips the two crossed root sheets.

---

## 7. Quadratic transgression

The quadratic form on `Q` is the unique odd-parity Boolean function modulo affine functions.

Indeed,

\[
\sum_{x\in Q}\bar q(x)=1,
\]

whereas every affine function `Q -> F_2` has even total parity. Hence

\[
\boxed{
\operatorname{Fun}(Q,\mathbf F_2)/\operatorname{Aff}(Q,\mathbf F_2)
\cong\mathbf F_2,
}
\]

with generator `[bar q]`.

For the route-lock affine action define

\[
\Theta_g(x)=\bar q(A_gx)+\bar q(x).
\]

### Theorem 7.1 — explicit transgression formula

\[
\boxed{
\Theta_g(x)
=
\kappa(g)\bigl(1+\bar b(x,B)\bigr).
}
\]

Thus:

- `Theta_g=0` when `kappa(g)=0`;
- when `kappa(g)=1`, `Theta_g` is the affine indicator of the line `{O,B}`;
- restricted to the three route points `{B,X,Y}`, it is the indicator of the unique bad route `B`.

### Proof

The linear `D_8` action preserves `bar q` and fixes `B`. Since `bar alpha(g)=kappa(g)B`, polarization gives

\[
\bar q(gx+\bar\alpha(g))+\bar q(x)
=
\bar q(\bar\alpha(g))
+
\bar b(gx,\bar\alpha(g)).
\]

If `kappa=0`, this is zero. If `kappa=1`, then `bar q(B)=1` and

\[
\bar b(gx,B)=\bar b(x,B),
\]

so the expression is `1+bar b(x,B)`.

### Corollary 7.2 — recovery of the cocycle

The linear part of `Theta_g` is

\[
x\longmapsto\bar b(x,\bar\alpha(g)).
\]

Because `bar b` is nondegenerate, the transgression `Theta` determines `bar alpha` uniquely.

Hence the DDD cocycle is the polar/linear shadow of the failure of the quadratic rootness function to be invariant under the route-lock affine action.

---

## 8. Canonical comparison with curvature parity

The flat-potential/common-cut branch uses four-bit functions on an affine plane `AG(2,2)`. A local word is affine exactly when its total parity is zero; the non-affine quotient is one-dimensional.

The DDD quotient `Q` is itself canonically an anisotropic affine plane, and its rootness function `bar q` is the unique non-affine class. Therefore the coefficient-level comparison is not merely dimension counting:

\[
\boxed{
\text{DDD affine cocycle}
\xrightarrow{\text{quadratic transgression}}
[\bar q]
\in
\operatorname{Fun}(Q)/\operatorname{Aff}(Q),
}
\]

while the full-channel curvature obstruction is measured by the same parity quotient of four-point functions.

This gives an explicit canonical bridge between:

1. the internal-twist cocycle `alpha`;
2. the unique-bad-route quadratic defect;
3. the one-dimensional non-affine curvature class.

### Trust boundary

This is an exact finite coefficient-level comparison. A graph-level theorem must still identify the physical four scalar sheets or route states with this quotient `Q` functorially and show that regional boundaries respect the transgression.

---

## 9. Consequences for octahedral overlap returns

An enriched overlap return supplies

\[
\pi_\gamma\in D_8.
\]

The quotient route-lock correction is now forced:

\[
\boxed{
\bar z_\gamma
=
\bar\alpha(\pi_\gamma)
=
\kappa(\pi_\gamma)B.
}
\]

Any full lift preserving the two crossed route classes has the form

\[
\boxed{
z_\gamma
=
\alpha(\pi_\gamma)+\nu_\gamma c.}
\]

The enriched physical orientation word must determine `nu_gamma`.

If the return data define a cocycle on the return group, then

\[
\nu=u\chi+v\kappa.
\]

Its DDD class is nontrivial exactly when `v=0`.

Thus the latest physical frontier is one explicit binary law:

### Target 9.1 — internal-twist orientation law

Determine, from the octahedral state walk and its side-root output word, whether an internal twist contributes a simultaneous crossed-sheet flip. Equivalently, decide whether the physical route-locking cocycle is cohomologous to

\[
\alpha
\quad\text{or to}\quad
\alpha+\kappa c.
\]

The first case is the genuine DDD exception; the second is gauge-trivial.

### Target 9.2 — graph-level transgression

Construct the physical chain map from the overlap return to the four-point route quotient and prove that the induced quadratic transgression agrees with the common-cut/full-channel curvature word on regional boundaries.

### Target 9.3 — localisation

If the nontrivial class occurs, localise the first internal-twist return to a bounded DDD blossom, common-cut witness, or defect-forest unit. If the class vanishes, produce a gauge/serial reduction, profile escape, or smaller separator.

---

## 10. Exact theorem versus open frontier

### Exact in this dossier

- the four-point quotient `Q=E_4/<c>` and its matching interpretation;
- the linear `D_8` action on `Q`;
- `bar alpha(g)=kappa(g)B`;
- pointwise route lock of the two crossed matching classes;
- the exact locking fibre `alpha(g)+{0,c}`;
- classification of all route-locking cocycles;
- the orientation-fork cohomology formula;
- the explicit quadratic transgression formula;
- the coefficient-level canonical comparison with the unique non-affine curvature class.

### Still open

- extraction of the physical lift bit `nu_gamma` from the enriched overlap word;
- proof that the actual four-pole affine translation is the route-locking lift above;
- graph-level identification with the common-cut curvature class;
- bounded DDD localisation and contraction;
- Type T/Type H composition, horizontal/global induction, and the global five-support theorem.
