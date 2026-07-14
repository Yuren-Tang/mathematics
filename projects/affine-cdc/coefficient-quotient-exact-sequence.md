# Coefficient quotients and the long exact sequence of flow tensor homology

**Date:** 2026-07-14  
**Status:** theorem-level structural draft; not yet Lean-formalized.

Let $G$ be a finite connected graph and let

$$
f:E(G)\to\Gamma
$$

be a spanning binary flow. Write

$$
Q_G=\mathbf F_2^E/\mathcal C(G)^\perp
$$

and let

$$
F_f^*:Q_G\to\Gamma
$$

be the induced surjection.

The flow tensor complex is

$$
C_f:\qquad
\mathbf F_2^E
\xrightarrow{T_f}
\Gamma\otimes Q_G
\xrightarrow{W_f}
\Lambda^2\Gamma,
$$

where

$$
T_f(e)=f(e)\otimes\bar e,
\qquad
W_f(a\otimes q)=a\wedge F_f^*(q).
$$

## 1. Quotienting the coefficient space

Let

$$
g:\Gamma\twoheadrightarrow\Gamma'
$$

be a surjective linear map, and define the quotient flow

$$
f':=g\circ f.
$$

Assume $f'$ remains nowhere zero and spans $\Gamma'$. Then

$$
F_{f'}^*=gF_f^*.
$$

Hence the maps

$$
\operatorname{id}_{\mathbf F_2^E},
\qquad
g\otimes\operatorname{id}_{Q_G},
\qquad
\Lambda^2g
$$

form a morphism of complexes

$$
\begin{array}{ccccc}
\mathbf F_2^E
&\xrightarrow{T_f}&
\Gamma\otimes Q_G
&\xrightarrow{W_f}&
\Lambda^2\Gamma\\
\Vert&&
\downarrow g\otimes1&&
\downarrow\Lambda^2g\\
\mathbf F_2^E
&\xrightarrow{T_{f'}}&
\Gamma'\otimes Q_G
&\xrightarrow{W_{f'}}&
\Lambda^2\Gamma'.
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

Thus the flow tensor construction is functorial under coefficient quotients.

## 2. The relative wedge complex

Put

$$
K:=\ker g.
$$

Since tensor product over a field is exact,

$$
\ker(g\otimes1)=K\otimes Q_G.
$$

For a surjection $g$,

$$
\ker(\Lambda^2g)=K\wedge\Gamma,
$$

the image of

$$
K\otimes\Gamma\to\Lambda^2\Gamma,
\qquad
k\otimes a\mapsto k\wedge a.
$$

The kernel complex is therefore concentrated in degrees one and two:

$$
R_{K,f}:\qquad
0
\longrightarrow
K\otimes Q_G
\xrightarrow{\partial_{K,f}}
K\wedge\Gamma
\longrightarrow0,
$$

with

$$
\boxed{
\partial_{K,f}(k\otimes q)
=
k\wedge F_f^*(q).
}
$$

Consequently there is a short exact sequence of complexes

$$
\boxed{
0\longrightarrow
R_{K,f}
\longrightarrow
C_f
\longrightarrow
C_{f'}
\longrightarrow0.
}
$$

## 3. Long exact sequence

Define

$$
\mathcal B_f:=H_0(C_f)=\ker T_f
$$

and

$$
\mathcal K_f:=H_1(C_f)=\ker W_f/\operatorname{im}T_f.
$$

For the relative complex,

$$
H_1(R_{K,f})=\ker\partial_{K,f},
$$

and

$$
H_2(R_{K,f})=\operatorname{coker}\partial_{K,f}.
$$

The short exact sequence of complexes gives

$$
\boxed{
0
\to
\mathcal B_f
\to
\mathcal B_{f'}
\to
\ker\partial_{K,f}
\to
\mathcal K_f
\to
\mathcal K_{f'}
\to
\operatorname{coker}\partial_{K,f}
\to
0.
}
$$

This is the coefficient-quotient long exact sequence.

It precisely measures how quotienting the flow labels creates new gauge modes and removes or creates essential obstruction homology.

## 4. A one-dimensional kernel

Suppose

$$
K=\langle k\rangle
$$

is one-dimensional. Then

$$
K\otimes Q_G\cong Q_G
$$

and

$$
K\wedge\Gamma\cong \Gamma/K.
$$

Under these identifications,

$$
\partial_{K,f}(q)=k\wedge F_f^*(q).
$$

Because $F_f^*$ is surjective, $\partial_{K,f}$ is surjective. Therefore

$$
\boxed{H_2(R_{K,f})=0}
$$

and

$$
\boxed{
\dim H_1(R_{K,f})
=
\dim Q_G-(\dim\Gamma-1).
}
$$

For a connected cubic graph with $n$ vertices,

$$
\dim Q_G=\frac n2+1.
$$

If $\dim\Gamma=r$, then

$$
\boxed{
\dim H_1(R_{K,f})
=
\frac n2-r+2.
}
$$

## 5. Rank three to rank two

Let

$$
\dim\Gamma=3,
\qquad
\dim\Gamma'=2.
$$

Then

$$
\dim H_1(R_{K,f})
=
\frac n2-1.
$$

The long exact sequence becomes

$$
0
\to
\mathcal B_f
\to
\mathcal B_{f'}
\to
\mathbf F_2^{\,n/2-1}
\to
\mathcal K_f
\to
\mathcal K_{f'}
\to
0.
$$

For a spanning rank-two flow,

$$
\mathcal K_{f'}=0.
$$

In rank three, Fano Hodge gives

$$
\dim\mathcal K_f=\dim\mathcal B_f.
$$

Taking dimensions therefore yields

$$
\boxed{
\dim\mathcal B_{f'}
=
\frac n2-1.
}
$$

Thus the exact rank-two moduli count is the relative homology created by quotienting a balanced rank-three flow through one coefficient direction.

This explains the rank-two formula as a functorial degeneration of the rank-three tensor complex rather than an isolated local count.

## 6. General rank drop by one

For a quotient

$$
\Gamma\twoheadrightarrow\Gamma'
$$

with

$$
\dim\Gamma'=r-1,
$$

the relative homology has dimension

$$
\boxed{
\dim H_1(R_{K,f})
=
\frac n2-r+2
}
$$

on a connected cubic graph.

The exact sequence

$$
0
\to
\mathcal B_f
\to
\mathcal B_{f'}
\to
H_1(R_{K,f})
\to
\mathcal K_f
\to
\mathcal K_{f'}
\to
0
$$

shows that every rank drop trades a controlled relative space between degree-zero flexibility and degree-one obstruction.

## 7. Iterated flags

Given a flag of coefficient quotients

$$
\Gamma_r\twoheadrightarrow
\Gamma_{r-1}\twoheadrightarrow\cdots\twoheadrightarrow
\Gamma_2,
$$

the flow tensor homology changes by successive one-dimensional relative wedge complexes.

In particular, the rank trichotomy can be studied by descending from higher rank through a sequence of explicit homological degenerations.

## 8. Structural consequences

The coefficient-quotient exact sequence supplies the first genuine morphism theory for the master flow tensor datum:

- it is canonical;
- it is compatible with the edge basis;
- it induces a chain map;
- it produces a short exact sequence of complexes;
- it gives a computable long exact sequence on moduli and obstruction spaces.

The next questions are:

1. identify the connecting map
   $$
   \mathcal B_{f'}\to\ker\partial_{K,f}
   $$
   explicitly in gauge-potential terms;
2. determine when the sequence splits;
3. relate successive rank quotients to the higher-rank obstruction defect;
4. compare this coefficient functoriality with graph-cut Mayer--Vietoris functoriality.
