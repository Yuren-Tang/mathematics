# Code flags and the mixed Schur–Koszul complex

**Date:** 2026-07-14  
**Status:** theorem-level structural draft; terminology provisional.

Let $E$ be finite and put

$$
A:=\mathbf F_2^E
$$

with coordinatewise multiplication $*$ and its standard perfect pairing.

## 1. Based quotient data are nested code flags

Start with a based quotient datum

$$
A\xrightarrow{\pi}Q\xrightarrow{F}\Gamma.
$$

Dualizing the surjections gives inclusions

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

Conversely, given a code flag $D\subseteq C\subseteq A$, set

$$
Q:=C^*,
\qquad
\Gamma:=D^*.
$$

Using the standard pairing on $A$, define

$$
\pi:A\to C^*,
\qquad
\pi(x)(c)=\langle x,c\rangle,
$$

and let $F:C^*\to D^*$ be restriction of functionals. Both maps are
surjective. Thus, up to the coordinate-basis identifications,

$$
\boxed{
\text{based quotient data}
\;\simeq\;
\text{nested binary code flags }D\subseteq C\subseteq A.
}
$$

## 2. The dual tensor complex

Dualizing

$$
A\xrightarrow{T}\Gamma\otimes Q\xrightarrow{W}\Lambda^2\Gamma
$$

gives

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
\boxed{\mu(d\otimes c)=d*c.}
$$

The first map is

$$
\boxed{
\kappa(d_1\wedge d_2)
=
d_1\otimes d_2+d_2\otimes d_1,
}
$$

where the second tensor factor uses $D\subseteq C$. Since multiplication is
commutative and the characteristic is two, $\mu\kappa=0$.

This is a truncated mixed Koszul-type complex for the nested code flag. The
name **mixed Schur–Koszul complex** is provisional.

## 3. Homology dictionary

Since $\operatorname{im}\mu=C*D$,

$$
\boxed{H_0(T)^*\cong A/(C*D),}
$$

or equivalently

$$
H_0(T)=(C*D)^\perp.
$$

Moreover,

$$
\boxed{
H_1(T)^*
\cong
\ker\mu/\operatorname{im}\kappa.
}
$$

Thus essential stresses are the first syzygies of Schur multiplication,
modulo the universal commutativity relations.

## 4. Constraint matroid

The row space of the tensor representation is $C*D$. Hence its constraint
matroid has cocycle code

$$
\boxed{C*D}
$$

and cycle code

$$
\boxed{(C*D)^\perp.}
$$

It depends only on the nested code flag, not on chosen generator matrices.

## 5. Tensor index

If

$$
m=|E|,
\qquad
c=\dim C,
\qquad
d=\dim D,
$$

then

$$
\boxed{
\operatorname{ind}(D\subseteq C)
=
m-cd+\binom d2.
}
$$

The flag is balanced when $m=cd-\binom d2$.

## 6. Graphical realization

For a connected graph $G$ with a spanning binary flow $f:E\to\Gamma$,

$$
C=\mathcal C(G)
$$

is the cycle code and

$$
D=\mathcal F_f
=
\{\ell\circ f:\ell\in\Gamma^*\}
$$

is the coordinate-flow code. Since every coordinate of a flow is a binary
cycle, $D\subseteq C$.

Thus the graphical flow tensor datum is exactly the mixed Schur–Koszul complex
of

$$
\boxed{\mathcal F_f\subseteq\mathcal C(G).}
$$

The graph adds cut geometry, harmonic quotients, cographic gluing and the local
affine class, but the abstract tensor homology exists for every nested code
flag.

## 7. Matroid quotient interpretation

The columns representing $C^*$ define a binary matroid $M$. Applying the
quotient map $F$ gives a lower-rank matroid $N$ on the same ground set. Every
dependency of $M$ remains a dependency of $N$, so $N$ is a representable
quotient, equivalently an identity-ground-set strong-map image, of $M$.

Hence the object may also be described as

$$
\boxed{
\text{a represented binary matroid quotient }M\twoheadrightarrow N
}
$$

together with its diagonal tensor representation. In the graphical case,
$M$ is the cographic matroid of $G$.

## 8. External examples

Every nested pair of binary linear codes gives an example. Natural test classes
include:

- Reed–Muller code flags;
- nested cyclic or constacyclic codes;
- evaluation-code flags;
- quotients of binary projective-geometry matroids;
- arbitrary represented binary matroid quotients.

The existing Schur-product literature studies the image code $C*D$ and its
parameters. The additional package here is the multiplication map, its
syzygies modulo commutativity, tensor homology, constraint matroid, balanced
torsion and graphical affine enhancements.

## 9. Recognition status

This construction does not invent componentwise code products. What appears
distinctive is the package

$$
\Lambda^2D\to D\otimes C\to A
$$

attached to a nested flag, together with its homology and enhancements. A
literature review must determine whether this exact syzygy package has a
standard name. Until then, “mixed Schur–Koszul complex” is descriptive, not
established terminology.

## 10. Revised abstract core

The abstract linear theory can now be organized around:

1. $A=\mathbf F_2^E$;
2. a code flag $D\subseteq C\subseteq A$;
3. Schur multiplication $\mu:D\otimes C\to A$;
4. $\kappa:\Lambda^2D\to D\otimes C$;
5. mixed Schur–Koszul homology;
6. the constraint matroid of $C*D$;
7. balanced index and torsion.

The code-flag and quotient-datum languages are dual and complementary.