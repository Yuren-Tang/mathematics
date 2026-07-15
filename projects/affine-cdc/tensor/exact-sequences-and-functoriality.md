# Exact sequences and coefficient functoriality

**Status.** The statements in this chapter are theorem-level linear algebra and
have complete proofs. They have not yet been Lean-formalized.

Let

$$
A\xrightarrow{\pi}Q\xrightarrow{F}\Gamma
$$

be a based quotient datum, with tensor complex

$$
A\xrightarrow{T}\Gamma\otimes Q\xrightarrow{W}\Lambda^2\Gamma.
$$

This chapter describes the internal structure of $\ker W$ and the behaviour of
tensor homology under quotienting the coefficient space.

## 1. The divided-square space

Put

$$
K:=\ker F.
$$

Define

$$
D^2\Gamma
:=
\ker\left(
\Gamma\otimes\Gamma
\xrightarrow{\wedge}
\Lambda^2\Gamma
\right).
$$

In characteristic two this is the natural divided-square subspace. It is
spanned by

$$
x\otimes x
$$

and

$$
x\otimes y+y\otimes x.
$$

If $r=\dim\Gamma$, then

$$
\boxed{
\dim D^2\Gamma=\frac{r(r+1)}2.
}
$$

The notation $D^2\Gamma$ avoids choosing a splitting or identifying this space
with a convention-dependent version of $\operatorname{Sym}^2\Gamma$.

## 2. The canonical divided-square exact sequence

The map

$$
\operatorname{id}_\Gamma\otimes F:
\Gamma\otimes Q
\longrightarrow
\Gamma\otimes\Gamma
$$

sends $\ker W$ into $D^2\Gamma$, because

$$
\wedge\circ(\operatorname{id}\otimes F)=W.
$$

### Theorem 2.1

There is a canonical short exact sequence

$$
\boxed{
0\longrightarrow
\Gamma\otimes K
\longrightarrow
\ker W
\xrightarrow{\operatorname{id}\otimes F}
D^2\Gamma
\longrightarrow0.
}
$$

### Proof

The kernel of $\operatorname{id}\otimes F$ on $\Gamma\otimes Q$ is
$\Gamma\otimes K$, and this space lies in $\ker W$.

For surjectivity, write

$$
z=\sum_i a_i\otimes b_i\in D^2\Gamma.
$$

Choose $q_i\in Q$ with $F(q_i)=b_i$. Then

$$
\widetilde z:=\sum_i a_i\otimes q_i
$$

satisfies $W(\widetilde z)=0$ and maps to $z$. $\square$

No splitting of $Q$ is required. A chosen section of $F$ merely produces a
noncanonical decomposition

$$
\ker W
\cong
(\Gamma\otimes K)\oplus D^2\Gamma.
$$

## 3. Edge columns and the Veronese quotient

For a coordinate $e\in E$, the tensor column is

$$
t_e=f_e\otimes q_e\in\ker W.
$$

Its image in the divided-square quotient is

$$
\boxed{
t_e\longmapsto f_e\otimes f_e.
}
$$

Thus the upper “quadratic block” seen after choosing an adapted basis is
canonical: it is the Veronese image in $D^2\Gamma$. The remaining information
lies in the extension kernel $\Gamma\otimes K$.

The dimension formula is

$$
\begin{aligned}
\dim\ker W
&=r(\dim Q-r)+\frac{r(r+1)}2\\
&=r\dim Q-\binom r2.
\end{aligned}
$$

This agrees with surjectivity of $W$.

## 4. The rank-three Veronese configuration

Let $\Gamma=\mathbf F_2^3$. Then

$$
\dim D^2\Gamma=6.
$$

The seven nonzero vectors of $\Gamma$ give seven nonzero columns

$$
\nu(x):=x\otimes x\in D^2\Gamma.
$$

They satisfy

$$
\boxed{
\sum_{x\neq0}x\otimes x=0.
}
$$

This is their unique linear dependence, so any six distinct nonzero Fano labels
form a basis of $D^2\Gamma$. Consequently, the six exceptional edges in the
coordinate basis-packing formula are exactly the six columns selected to fill
the canonical divided-square quotient. The remaining columns fill
$\Gamma\otimes K$.

For a connected cubic graph on $n$ vertices,

$$
\dim Q_G=\frac n2+1,
$$

and in rank three

$$
\dim K=\frac n2-2.
$$

The exact sequence becomes

$$
0\longrightarrow
\mathbf F_2^3\otimes K
\longrightarrow
\ker W_f
\longrightarrow
D^2(\mathbf F_2^3)
\longrightarrow0,
$$

with

$$
3\left(\frac n2-2\right)+6
=
\frac{3n}{2}
=
|E|.
$$

This is the invariant source of the decomposition $|E|=3d+6$ in the adapted
basis-packing determinant.

## 5. Determinant-line factorization

Every short exact sequence

$$
0\longrightarrow U\longrightarrow V\longrightarrow Z\longrightarrow0
$$

induces a canonical determinant-line isomorphism

$$
\det V\cong\det U\otimes\det Z.
$$

Applying this to Theorem 2.1 gives

$$
\boxed{
\det(\ker W)
\cong
\det(\Gamma\otimes K)
\otimes
\det(D^2\Gamma).
}
$$

Therefore the top wedge of the edge columns decomposes canonically into:

1. a divided-square or Veronese factor;
2. an extension-kernel basis-packing factor.

An adapted cycle basis only writes this invariant factorization in coordinates.

## 6. Coefficient quotients

Return to a connected graph $G$ with a spanning nowhere-zero flow

$$
f:E(G)\longrightarrow\Gamma.
$$

Let

$$
g:\Gamma\twoheadrightarrow\Gamma'
$$

be a surjective linear map and define

$$
f':=g\circ f.
$$

Assume $f'$ remains nowhere zero and spans $\Gamma'$. The maps

$$
\operatorname{id}_{\mathbf F_2^E},
\qquad
g\otimes\operatorname{id}_{Q_G},
\qquad
\Lambda^2g
$$

form a morphism of tensor complexes

$$
\begin{array}{ccccc}
\mathbf F_2^E&\xrightarrow{T_f}&\Gamma\otimes Q_G&\xrightarrow{W_f}&\Lambda^2\Gamma\\
\Vert&&\downarrow g\otimes1&&\downarrow\Lambda^2g\\
\mathbf F_2^E&\xrightarrow{T_{f'}}&\Gamma'\otimes Q_G&\xrightarrow{W_{f'}}&\Lambda^2\Gamma'.
\end{array}
$$

Indeed,

$$
T_{f'}=(g\otimes1)T_f
$$

and

$$
W_{f'}(g\otimes1)=(\Lambda^2g)W_f.
$$

Thus coefficient quotients are ordinary covariant morphisms of tensor
complexes.

## 7. The relative wedge complex

Put

$$
L:=\ker g.
$$

Then

$$
\ker(g\otimes1)=L\otimes Q_G
$$

and

$$
\ker(\Lambda^2g)=L\wedge\Gamma,
$$

the image of $L\otimes\Gamma\to\Lambda^2\Gamma$. The kernel complex of the
coefficient quotient is

$$
\boxed{
R_{L,f}:
0\longrightarrow
L\otimes Q_G
\xrightarrow{\partial_{L,f}}
L\wedge\Gamma
\longrightarrow0,
}
$$

where

$$
\partial_{L,f}(\ell\otimes q)
=
\ell\wedge F_f(q).
$$

Therefore there is a short exact sequence of complexes

$$
\boxed{
0\longrightarrow
R_{L,f}
\longrightarrow
\mathcal T_f
\longrightarrow
\mathcal T_{f'}
\longrightarrow0.
}
$$

## 8. Long exact sequence in tensor homology

Write

$$
\mathcal B_f:=H_0(\mathcal T_f),
\qquad
\mathcal K_f:=H_1(\mathcal T_f).
$$

For the relative complex,

$$
H_1(R_{L,f})=\ker\partial_{L,f},
$$

and

$$
H_2(R_{L,f})=\operatorname{coker}\partial_{L,f}.
$$

The short exact sequence of complexes gives:

### Theorem 8.1 — coefficient-quotient long exact sequence

$$
\boxed{
0
\longrightarrow
\mathcal B_f
\longrightarrow
\mathcal B_{f'}
\longrightarrow
\ker\partial_{L,f}
\longrightarrow
\mathcal K_f
\longrightarrow
\mathcal K_{f'}
\longrightarrow
\operatorname{coker}\partial_{L,f}
\longrightarrow0.
}
$$

This sequence measures exactly how quotienting coefficient directions creates
new gauge modes and changes essential obstruction homology.

## 9. A one-dimensional rank drop

Suppose

$$
L=\langle\ell\rangle
$$

is one-dimensional. Then

$$
L\otimes Q_G\cong Q_G,
\qquad
L\wedge\Gamma\cong\Gamma/L.
$$

Since $F_f:Q_G\to\Gamma$ is surjective, the relative differential is
surjective. Hence

$$
H_2(R_{L,f})=0
$$

and

$$
\dim H_1(R_{L,f})
=
\dim Q_G-(\dim\Gamma-1).
$$

For a connected cubic graph on $n$ vertices and $r=\dim\Gamma$,

$$
\boxed{
\dim H_1(R_{L,f})
=
\frac n2-r+2.
}
$$

The long exact sequence shortens to

$$
0\longrightarrow
\mathcal B_f
\longrightarrow
\mathcal B_{f'}
\longrightarrow
H_1(R_{L,f})
\longrightarrow
\mathcal K_f
\longrightarrow
\mathcal K_{f'}
\longrightarrow0.
$$

## 10. Rank three to rank two

Let $\dim\Gamma=3$ and $\dim\Gamma'=2$. Then

$$
\dim H_1(R_{L,f})=\frac n2-1.
$$

For a spanning rank-two flow,

$$
\mathcal K_{f'}=0.
$$

For a spanning rank-three cubic flow, Fano self-duality gives

$$
\dim\mathcal K_f=\dim\mathcal B_f.
$$

Taking dimensions in the long exact sequence yields

$$
\boxed{
\dim\mathcal B_{f'}=\frac n2-1.
}
$$

Thus the exact rank-two moduli count is the relative homology created by
quotienting a balanced rank-three flow through one coefficient direction.

## 11. Cubic tensor index across ranks

For a connected cubic graph on $n$ vertices and a spanning rank-$r$ flow,

$$
|E|=\frac{3n}{2},
\qquad
\dim Q_G=\frac n2+1.
$$

Therefore

$$
\boxed{
\operatorname{ind}(G,f)
=
\frac{(3-r)(n-r)}2.
}
$$

Rank three is the unique balanced rank in the nontrivial cubic range. Rank two
has positive flexibility index; rank four and above have negative index and
therefore dimensionally forced middle homology. The coefficient-quotient exact
sequence gives a functorial way to pass between these layers.

## 12. Iterated coefficient flags

For a flag of coefficient quotients

$$
\Gamma_r\twoheadrightarrow
\Gamma_{r-1}\twoheadrightarrow\cdots\twoheadrightarrow\Gamma_2,
$$

tensor homology changes by successive relative wedge complexes. This is an
established formal mechanism. Relating the connecting maps explicitly to the
higher-rank dual-Fano residue remains an open structural problem.

## 13. Functorial boundary

Coefficient quotients act covariantly and produce ordinary chain maps and long
exact sequences. Graph cuts behave differently: edge-coordinate spaces are
assembled by pullbacks, while cycle-dual quotients are assembled by pushouts.
Their natural structure is therefore a correspondence rather than a single
covariant map. The graphical interface theory is developed separately in
[`../gauge/interface-gluing.md`](../gauge/interface-gluing.md).