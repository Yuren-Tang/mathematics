# The divided-square exact sequence behind the flow tensor complex

**Date:** 2026-07-14  
**Status:** theorem-level structural draft; not yet Lean-formalized.

Let

$$
F^*:Q\to\Gamma
$$

be a surjective linear map of finite-dimensional vector spaces over
$\mathbf F_2$, and put

$$
K:=\ker F^*.
$$

Define

$$
W:\Gamma\otimes Q\to\Lambda^2\Gamma,
\qquad
W(a\otimes q)=a\wedge F^*(q).
$$

Write

$$
Z(F^*):=\ker W.
$$

This is the middle cycle space of the flow tensor complex.

## 1. The divided-square space

Define

$$
D^2\Gamma
:=
\ker\!\left(
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

Its dimension is

$$
\boxed{
\dim D^2\Gamma=\frac{r(r+1)}2,
}
$$

where $r=\dim\Gamma$.

This is the correct basis-free replacement for the informal
"$\operatorname{Sym}^2\Gamma$" appearing after a chosen splitting.

## 2. Canonical exact sequence

The map

$$
\operatorname{id}_\Gamma\otimes F^*
:
\Gamma\otimes Q
\longrightarrow
\Gamma\otimes\Gamma
$$

sends $Z(F^*)$ into $D^2\Gamma$, because

$$
\wedge\circ
(\operatorname{id}_\Gamma\otimes F^*)
=
W.
$$

Its kernel on $Z(F^*)$ is exactly

$$
\Gamma\otimes K.
$$

It is also surjective onto $D^2\Gamma$: if

$$
z=\sum_i a_i\otimes b_i\in D^2\Gamma,
$$

choose $q_i\in Q$ with $F^*(q_i)=b_i$. Then

$$
\widetilde z=\sum_i a_i\otimes q_i
$$

lies in $Z(F^*)$ and maps to $z$.

Therefore there is a canonical short exact sequence

$$
\boxed{
0
\longrightarrow
\Gamma\otimes K
\longrightarrow
Z(F^*)
\longrightarrow
D^2\Gamma
\longrightarrow
0.
}
$$

No splitting of $Q$ is required.

A chosen section $\Gamma\to Q$ merely splits this exact sequence
noncanonically:

$$
Z(F^*)
\cong
(\Gamma\otimes K)\oplus D^2\Gamma.
$$

## 3. Application to a flow

For a flow-labelled graph, take

$$
Q=Q_G,
\qquad
F^*=F_f^*,
\qquad
K_f:=\ker F_f^*.
$$

The edge tensor is

$$
t_e=f(e)\otimes\bar e\in Z(F_f^*).
$$

Its image in $D^2\Gamma$ is

$$
\boxed{
t_e\longmapsto f(e)\otimes f(e).
}
$$

Thus the upper Veronese block of the reduced tensor matrix is canonical: it is
the divided-square quotient of the edge tensors.

The lower block is the extension part $\Gamma\otimes K_f$.

## 4. Dimension formula

Let

$$
c=\dim Q_G=\dim\mathcal C(G).
$$

Since $\dim K_f=c-r$,

$$
\dim Z(F_f^*)
=
r(c-r)+\frac{r(r+1)}2
=
rc-\frac{r(r-1)}2.
$$

This agrees with

$$
\dim\ker W_f
=
\dim(\Gamma\otimes Q_G)-\dim\Lambda^2\Gamma.
$$

For a connected cubic graph,

$$
c=\frac n2+1.
$$

At rank three,

$$
\dim K_f
=
\frac n2-2,
$$

and the exact sequence becomes

$$
0
\to
\mathbf F_2^3\otimes K_f
\to
\ker W_f
\to
D^2(\mathbf F_2^3)
\to
0,
$$

with dimensions

$$
3\left(\frac n2-2\right)
+
6
=
\frac{3n}{2}
=
|E|.
$$

This is the conceptual source of the decomposition

$$
|E|
=
3d+6
$$

in the Fano basis-packing formula.

## 5. Why six exceptional Fano edges appear

For $\Gamma=\mathbf F_2^3$,

$$
\dim D^2\Gamma=6.
$$

The quadratic Veronese map is

$$
\nu:\Gamma\to D^2\Gamma,
\qquad
\nu(x)=x\otimes x.
$$

The seven nonzero vectors of $\Gamma$ give seven nonzero Veronese columns in a
six-dimensional space. They satisfy

$$
\sum_{x\ne0}x\otimes x=0.
$$

This is their unique linear dependence. Hence any six distinct nonzero Fano
labels form a basis of $D^2\Gamma$.

Therefore the "six complementary edges with six distinct Fano labels" in the
basis-packing determinant are exactly the six edge tensors selected to fill
the canonical divided-square quotient.

The remaining edges fill the extension kernel

$$
\Gamma\otimes K_f.
$$

## 6. Determinant-line interpretation

For every short exact sequence of finite-dimensional spaces,

$$
0\to A\to B\to C\to0,
$$

there is a canonical determinant-line isomorphism

$$
\det B\cong\det A\otimes\det C.
$$

Applying this to the divided-square exact sequence gives

$$
\boxed{
\det(\ker W_f)
\cong
\det(\Gamma\otimes K_f)
\otimes
\det(D^2\Gamma).
}
$$

The Fano torsion

$$
\Theta_f
=
\bigwedge_{e\in E}t_e
$$

therefore decomposes canonically into:

1. a divided-square/Veronese factor;
2. an extension-kernel basis-packing factor.

Choosing an adapted cycle basis only writes this canonical determinant-line
factorization in coordinates.

## 7. Structural significance

The exact sequence explains several earlier observations at once:

- the upper quadratic block is intrinsic;
- the lower block measures the kernel of the flow quotient map;
- six exceptional edges at rank three come from $\dim D^2\Gamma=6$;
- the seven Fano labels form the projective Veronese configuration with one
  dependence;
- the basis-packing parity is a determinant-line expansion, not an accidental
  combinatorial formula;
- the balanced cubic rank-three determinant is the point where the total edge
  space can exactly fill both the extension kernel and the divided-square
  quotient.

This exact sequence should be treated as part of the definition-level theory
of the flow tensor datum.
