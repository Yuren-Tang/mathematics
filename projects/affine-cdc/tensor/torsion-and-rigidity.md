# Balanced tensor torsion and rigidity

**Status.** The determinant-line and rigidity statements are theorem-level
linear algebra. The rank-three basis-packing interpretation is a coordinate
expansion of the invariant construction. This presentation has not yet been
Lean-formalized.

## 1. Balanced tensor data

Let

$$
A\xrightarrow{T}\Gamma\otimes Q\xrightarrow{W}\Lambda^2\Gamma
$$

be the tensor complex of a based quotient datum, and assume it is balanced:

$$
\dim A=\dim\ker W.
$$

For each coordinate $e\in E$, write

$$
t_e:=T(e)=f_e\otimes q_e\in\ker W.
$$

Define the canonical top wedge

$$
\boxed{
\Theta_{\pi,F}
:=
\bigwedge_{e\in E}t_e
\in
\det(\ker W).
}
$$

Over $\mathbf F_2$, reordering the coordinates introduces no sign, so this
element is independent of an ordering of $E$.

## 2. Exactness criterion

### Theorem 2.1

For a balanced datum, the following are equivalent:

1. $\Theta_{\pi,F}\neq0$;
2. the edge columns $(t_e)_{e\in E}$ form a basis of $\ker W$;
3. $T:A\to\ker W$ is an isomorphism;
4. $H_0(\pi,F)=0$;
5. $H_1(\pi,F)=0$;
6. the constraint matroid is free.

### Proof

The domain $A$ and target $\ker W$ have the same dimension. The top wedge is
nonzero exactly when the columns are linearly independent, hence exactly when
$T$ is an isomorphism onto $\ker W$. Its kernel is $H_0$, and its cokernel
inside $\ker W$ is $H_1$. $\square$

Thus balancedness gives a square determinant problem, while torsion detects
whether the square complex is exact.

## 3. Binary tensor torsion

Since $\det(\ker W)$ is one-dimensional, define

$$
\tau_{\pi,F}
:=
\begin{cases}
1,&\Theta_{\pi,F}\neq0,\\
0,&\Theta_{\pi,F}=0.
\end{cases}
$$

This invariant is preserved by isomorphisms of based quotient data. It is a
characteristic-two determinant-line analogue of torsion for this finite
complex. The name is descriptive; no comparison with a specific established
torsion theory is asserted without further literature work.

## 4. Cubic rank-three flows

Let $G$ be a finite connected cubic graph on $n$ vertices and let

$$
f:E(G)\longrightarrow\Gamma=\mathbf F_2^3
$$

be a spanning nowhere-zero flow. Then

$$
|E|=\frac{3n}{2},
\qquad
\dim Q_G=\frac n2+1.
$$

Since $W_f$ is surjective,

$$
\dim\ker W_f
=
3\left(\frac n2+1\right)-3
=
\frac{3n}{2}
=|E|.
$$

Hence the rank-three graphical tensor complex is balanced. Define

$$
\boxed{
\Theta_f
:=
\bigwedge_{e\in E}
\bigl(f(e)\otimes\bar e\bigr)
\in
\det(\ker W_f)
}
$$

and let $\tau_f$ be its nonvanishing bit.

The homogeneous gauge-moduli code is

$$
\mathcal B_f=\ker T_f.
$$

Therefore:

### Theorem 4.1 — Fano rigidity criterion

$$
\boxed{
\tau_f=1
\iff
\mathcal B_f=0
\iff
f\text{ is gauge-rigid}.
}
$$

Equivalently, $\tau_f=1$ if and only if the flow constraint matroid is free.

## 5. Fano Hodge symmetry

For cubic rank-three flows, the Fano quadratic structure gives a canonical
duality

$$
\mathcal B_f
\cong
\mathcal K_f^*
\cong
\operatorname{EssStress}(f).
$$

Thus zero torsion means that both the flexibility space and the essential
obstruction-direction space are nonzero and have the same dimension. Nonzero
torsion means that the reduced tensor complex is exact.

This exactness is logically distinct from affine compatibility. The rank-three
Fano theorem proves that the distinguished affine class vanishes even when the
complex is singular. Torsion detects rigidity of the solution torsor, not
existence of a solution.

## 6. Divided-square factorization

Let

$$
K_f:=\ker(F_f:Q_G\to\Gamma).
$$

The canonical exact sequence

$$
0\longrightarrow
\Gamma\otimes K_f
\longrightarrow
\ker W_f
\longrightarrow
D^2\Gamma
\longrightarrow0
$$

induces

$$
\det(\ker W_f)
\cong
\det(\Gamma\otimes K_f)
\otimes
\det(D^2\Gamma).
$$

The edge tensor $f(e)\otimes\bar e$ maps to

$$
f(e)\otimes f(e)
$$

in the divided-square quotient. Hence $\Theta_f$ factors into a canonical
Veronese determinant and an extension-kernel determinant. This factorization
is intrinsic and does not depend on a cycle basis.

## 7. Coordinate basis-packing expansion

Choose an adapted cycle-space basis that splits

$$
Q_G\cong\Gamma\oplus K_f.
$$

Under the resulting noncanonical decomposition

$$
\ker W_f
\cong
D^2\Gamma\oplus(\Gamma\otimes K_f),
$$

an edge tensor becomes

$$
t_e
=
\bigl(f(e)\otimes f(e),\ f(e)\otimes k_e\bigr).
$$

Expanding the top wedge selects:

1. six edges whose six distinct nonzero Fano labels fill
   $D^2(\mathbf F_2^3)$;
2. the remaining edges to fill the three coefficient copies of $K_f$.

The resulting parity count is the previously derived Fano basis-packing number
$N_f(K_f)$. The invariant statement is

$$
\boxed{
\tau_f=N_f(K_f)\pmod2.
}
$$

The count is therefore not the definition of torsion. It is a coordinate
expansion of $\Theta_f$.

## 8. Relative quadratic unisolvence

Let $D\subseteq C\subseteq A$ be the dual code flag and put

$$
\mathcal Q(D,C)
:=
(D\otimes C)/\kappa(\Lambda^2D).
$$

The Schur multiplication map descends to

$$
\operatorname{ev}_{D,C}:\mathcal Q(D,C)\longrightarrow A.
$$

When the datum is balanced, the following are equivalent:

1. $\tau_{\pi,F}=1$;
2. the tensor complex is exact;
3. $\operatorname{ev}_{D,C}$ is an isomorphism;
4. relative quadratic classes are uniquely determined by coordinate evaluation.

Thus torsion measures an unisolvence locus in the abstract code-flag theory.
AffineCDC compatibility, by contrast, uses a particular quadratic identity
that remains valid outside this locus.

## 9. Interface behaviour

For a rank-three cubic flow assembled across an AffineCDC interface satisfying
the cap-extension property, let $L_S$ be the common boundary-line intersection.
The gauge-dimension formula is

$$
b_G=b_A+b_B+\dim L_S.
$$

### Three-edge interface

The three nonzero boundary labels are distinct and span a plane, so $L_S=0$.
Hence

$$
b_G=b_A+b_B.
$$

The sewn flow is rigid exactly when both capped factors are rigid, and therefore

$$
\boxed{
\tau_G=\tau_A\tau_B.
}
$$

### Two-edge interface

The two boundary labels are equal, so $\dim L_S=1$. Hence

$$
b_G=b_A+b_B+1.
$$

Every genuine two-edge sum has a nonzero sewing mode and is non-rigid:

$$
\boxed{\tau_G=0.}
$$

The detailed pullback–pushout and cap-extension statements are proved in
[`../gauge/interface-gluing.md`](../gauge/interface-gluing.md).

## 10. Scope

The established invariant is the determinant-line element of a balanced binary
tensor complex and its exactness criterion. The following remain separate
questions:

- whether a useful integral or polynomial lift exists;
- whether the construction agrees with a standard named torsion;
- whether deletion and contraction admit torsion recurrences;
- whether nonbinary coefficient fields support an analogous invariant;
- whether the basis-packing expansion has stronger enumerative consequences.

These questions should not be folded into the theorem statement.