# Rank-two route-lock gives Tait escape

**Programme:** `AffineCDC — Research Lead`  
**Status:** theorem-level elimination of the rank-drop branch inside the locked atom quotient  
**Parent:** `FIVE_CDC_ATOM_ROUTE_LOCK_CURVATURE_V1.md`

## 1. Setting

Universal route-lock at a repeated-matching `C` state produces a nowhere-zero quotient flow

\[
c:E(Q)\to E_4\setminus\{0\}
\cong F_2^3\setminus\{0\},
\]

with all four terminal values equal to

\[
g=(1,1,1,1).
\]

The four coordinate projections are the four full-challenge scalar sheets, all pairing the terminals as `12|34`.

This packet treats the case

\[
\dim\langle c(E(Q))\rangle\le2.
\]

## 2. Rank one is impossible

A rank-one nowhere-zero flow could use only one nonzero colour.  At an internal cubic vertex the sum of three copies of that colour is the colour itself, not zero.  Hence

\[
\boxed{
\dim\langle c(E(Q))\rangle\ne1.
}
\]

Therefore the rank-drop case has rank exactly two.

## 3. A rank-two quotient flow is a Tait colouring

Let

\[
L=\langle c(E(Q))\rangle\le E_4
\]

be the two-dimensional colour plane.  Since every terminal has colour `g`,

\[
g\in L.
\]

The plane has exactly three nonzero elements:

\[
L\setminus\{0\}=\{a,b,g\},
\qquad
a+b=g.
\]

At a cubic vertex the three incident colours are nonzero and sum to zero.  No two can agree, since that would force the third to be zero.  Hence every internal vertex sees exactly

\[
a,b,g.
\]

Thus:

\[
\boxed{
\text{every rank-two locked quotient flow is a Tait three-edge-colouring.}
}
\]

All four terminal semiedges have the same Tait colour `g`.

## 4. Root-triangle sections of the three planes

Fix the canonical locked `C` quotient

\[
\chi:E_5\twoheadrightarrow E_4,
\qquad
\ker\chi=\langle q\rangle.
\]

There are exactly three two-dimensional subspaces of `E_4` containing `g`.  For every such plane, one can choose a root representative of each nonzero colour so that the three representatives sum to zero.

### Computational Theorem 4.1

For all three planes

\[
L\le E_4,
\qquad
\dim L=2,
\qquad
g\in L,
\]

there exists a section

\[
s_L:L\setminus\{0\}\to R_5
\]

such that

\[
\chi(s_L(x))=x
\]

and

\[
\boxed{
\sum_{x\in L\setminus\{0\}}s_L(x)=0.
}
\]

In canonical coordinates, one may take:

\[
\begin{array}{c|c}
L\setminus\{0\}&
\text{one root section}\
\hline
\{0011,1100,1111\}&
\{11000,10100,01100\}\\
\{0101,1010,1111\}&
\{10010,10001,00011\}\\
\{0110,1001,1111\}&
\{00101,00110,00011\}.
\end{array}
\]

The third plane has four possible root-triangle sections; the table displays one.

Exact Wolfram enumeration checks every root fibre and every possible section.

## 5. Global root lift

Define

\[
\widetilde r(e)=s_L(c(e)).
\]

At every internal vertex the quotient colours are exactly the three nonzero elements of `L`, so the root labels are exactly the chosen root triangle and sum to zero.  Therefore

\[
\widetilde r:E(Q)\to R_5
\]

is a root-valued `E_5` flow.

Every terminal edge has quotient colour `g`, hence every terminal receives the same root

\[
s_L(g).
\]

Thus the boundary signature consists of two full supports and three empty supports, namely boundary state

\[
A.
\]

### Theorem 5.1 — rank-two Tait escape

\[
\boxed{
\text{universal route-lock}
+
\operatorname{rank}c=2
\Longrightarrow
\text{a root-valued lift with boundary state }A.
}
\]

Since `A` lies outside every Type H rainbow triangle profile, this gives strict profile escape.

## 6. Consequence for the atom composition problem

The locked atom quotient no longer has a rank-drop residual branch.  The only possible surviving locked sector is

\[
\boxed{
\operatorname{rank}\langle c(E(Q))\rangle=3.
}
\]

Hence the previous trichotomy sharpens to:

\[
\boxed{
\begin{array}{c}
\text{atom full challenges}\
\downarrow\\
\begin{cases}
\text{a crossed route occurs}
&\Rightarrow\text{root resolution candidate};\\
\text{all routes locked, rank }2
&\Rightarrow\text{Tait lift and }A\text{-state escape};\\
\text{all routes locked, rank }3
&\Rightarrow\text{quadratic-curvature analysis}.
\end{cases}
\end{array}}
\]

The rank-two route-lock example with internal pair-separating cut four remains useful as a warning: the escape is algebraic/Tait, not a consequence of a graph two-separation.

## 7. Trust boundary

Proved/exact:

- rank one is impossible;
- rank two forces a Tait colouring of the quotient four-pole;
- all three planes through `g` have root-triangle sections;
- the resulting root flow has all four terminal labels equal and therefore boundary state `A`;
- the rank-two locked branch escapes the Type H profile.

Open:

- composition-safe transfer in the crossed-route branch;
- the full-rank flat-potential sector;
- the full-rank nonzero-curvature sector;
- extension from one atom to longer Petersen-transducer paths and zero-branched defect trees.

## 8. Next target

The only genuine locked atom obstruction is now full rank.  The next theorem should prove:

\[
\boxed{
\operatorname{rank}c=3
\Longrightarrow
\begin{cases}
\Omega(c)=0&\Rightarrow\text{safe flat-potential resolution};\\
\Omega(c)\ne0&\Rightarrow\text{localised }D_8\text{/transition-matroid factor}.
\end{cases}
}
\]
