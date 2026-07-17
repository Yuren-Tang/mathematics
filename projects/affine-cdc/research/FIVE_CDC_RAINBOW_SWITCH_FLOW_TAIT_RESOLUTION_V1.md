# Rainbow switch flows and the Tait-resolution dichotomy

**Programme:** `AffineCDC — Research Lead`  
**Status:** theorem-level chain identities and graph-level lifting criteria, with exact finite monodromy/root-fibre verification; the final replacement/escape theorem remains open  
**Parents:** `FIVE_CDC_INTERIOR_AFFINE_HOLONOMY_NORM_V1.md`, `FIVE_CDC_ROOT_ADMISSIBLE_LINEARIZATION_V1.md`, `FIVE_CDC_FLOW_TENSION_FINITE_STATE_BOUNDARY_V1.md`

## 1. Purpose

The preceding packets treated a zero-norm rainbow loop as an affine equation

\[
z=(1+\pi)y
\]

with an edgewise root constraint.  That formulation is correct but too broad: a genuine rainbow loop is not an arbitrary affine-line instance.  It is the composite of exactly three terminal-path switches with routing colours `0,1,2`.

This packet restores that loop word and obtains a much smaller graph-theoretic object.

For every lifted canonical rainbow loop:

1. the first and third switches have the same support-pair coefficient `u`;
2. the middle switch has coefficient `v`;
3. all interior switch data lie in the two-dimensional plane
   \[
   W=\langle u,v\rangle\cong F_2^2;
   \]
4. after the ambient norm obstruction vanishes, root-admissible linearization is equivalent to lifting one `W`-valued switch flow through
   \[
   Q_\pi=1+\pi:R_5\longrightarrow Q_\pi(R_5);
   \]
5. for all four monodromy types, this lifting problem is equivalent to a Tait-resolution problem;
6. failure is witnessed only by a zero edge, an all-zero cubic vertex, or an odd component of a matching-complement two-factor.

Thus the true rainbow branch does not contain an arbitrary four-valued tension obstruction.  Its residual graph geometry is Tait colouring versus oddness.

No five-cycle double cover theorem, Tutte five-flow theorem, or Four Colour theorem is claimed.

## 2. The three-switch plane

Use the canonical boundary triangle

\[
B_1\xrightarrow{0}B_2\xrightarrow{1}D_0\xrightarrow{2}B_1.
\]

Choose the ordered initial `B_1` signature

\[
\varnothing,\ \varnothing,\ \{1,3\},\ \{2,4\},\ \{1,2,3,4\}.
\]

Let the three switched terminal-path components be

\[
P_0,\qquad P_1,\qquad P_2.
\]

The first switch acts on supports `3,4`.  The middle switch acts on one empty support `\varepsilon\in\{1,2\}` and support `5`.  Immediately before the third switch, the two `M_2` traces are again carried by supports `3,4`.  Hence the three support coefficients are

\[
\boxed{
 w_1=u=e_3+e_4,
 \qquad
 w_2=v=e_\varepsilon+e_5,
 \qquad
 w_3=u.
}
\]

If `x` is the initial indexed root cover and `x^\gamma` is the final cover before quotienting support names, then

\[
\boxed{
 x^\gamma
 =x+(P_0+P_2)\otimes u+P_1\otimes v.
}
\]

Define the **switch flow**

\[
\boxed{
 t_\gamma:=x+x^\gamma.
}
\]

Then

\[
\boxed{
 t_\gamma\in C_1(P)\otimes W,
 \qquad
 W:=\langle u,v\rangle.
}
\]

At every internal cubic vertex, `t_gamma` satisfies Kirchhoff conservation because it is the difference of two root flows.

### Exact boundary values

Up to exchanging the two blocks of the initial matching `M_1`, the terminal values are:

- for monodromy types `4` and `5`,
  \[
  (v,u,v,u);
  \]
- for types `3+2` and `2+2`, with `\kappa=u+v`,
  \[
  (\kappa,0,\kappa,0).
  \]

The dependency-free Wolfram verifier reproduces all sixteen monodromies and these switch coefficients.

## 3. Zero norm and the quotient-flow lifting equation

Let `\pi` be the support monodromy and

\[
Q_\pi:=1+\pi.
\]

The interior affine defect is

\[
z=x^\gamma+\pi x.
\]

Therefore

\[
\boxed{
 t_\gamma
 =x+x^\gamma
 =Q_\pi x+z.
}
\]

Assume the ambient norm defect vanishes.  By the preceding cyclic-cohomology theorem, there is an absolute cycle tensor `y` such that

\[
z=Q_\pi y.
\]

Put

\[
r:=x+y.
\]

Then

\[
\boxed{
 Q_\pi r=t_\gamma.
}
\]

### Theorem 3.1 — root-linearization is a quotient-flow lift

A zero-norm rainbow loop is root-admissibly translation-conjugate to its pure support permutation if and only if there exists a root-valued flow

\[
r:E(P)\to R_5
\]

with the same terminal values as `x` and satisfying

\[
\boxed{Q_\pi r=t_\gamma.}
\]

#### Proof

If `y` is a root-admissible conjugator, then `r=x+y` is root-valued, has the same boundary as `x`, and the displayed equation follows from `Q_pi y=z`.

Conversely, given such `r`, put `y=x+r`.  Since `x,r` are flows with the same boundary, `y` is an absolute cycle tensor.  Moreover

\[
Q_\pi y
 =Q_\pi x+Q_\pi r
 =Q_\pi x+t_\gamma
 =z.
\]

Finally `x+y=r` is root-valued. ∎

This removes the auxiliary affine section from the main object.  The problem is to lift a low-rank quotient flow through the ten-root map `Q_pi|R_5`.

## 4. Exact root-fibre table on the switch plane

The sixteen monodromies split into four equal classes.  For one representative of each class, exact finite computation gives:

\[
\begin{array}{c|c|c}
\text{type of }\pi
& W\cap\operatorname{im}Q_\pi
& |Q_\pi^{-1}(t)\cap R_5|
\\
\hline
2^2 1
&\{0,\kappa\}
&2\text{ over }0,\quad4\text{ over }\kappa
\\
3 2
&\{0,\kappa\}
&1\text{ over }0,\quad2\text{ over }\kappa
\\
4 1
&W
&0\text{ over }0,\quad2\text{ over every }t\ne0
\\
5
&W
&0\text{ over }0,\quad1\text{ over every }t\ne0.
\end{array}
\]

For every double-transposition lift, the finite verifier additionally proves

\[
\pi u=v,
\qquad
\pi v=u,
\qquad
W^\pi=\{0,\kappa\}.
\]

The same two-point actual image `\{0,kappa\}` occurs for type `3+2`, although its full `Q_pi` image has dimension three.

## 5. Full-rank types: `4` and `5`

For these types the actual quotient space is all of `W`, but zero has no root preimage.

### Proposition 5.1 — zero edge is the complete local obstruction

If

\[
t_\gamma(e)=0
\]

on any edge, no root lift exists.

If `t_gamma` is nonzero on every edge, then at every internal cubic vertex its three incident values are the three nonzero elements

\[
u,\qquad v,\qquad\kappa=u+v.
\]

Hence `t_gamma` is a Tait `F_2^2` flow on the four-pole.

### Theorem 5.2 — type `5` lifts uniquely

For type `5`, every nonzero value of `W` has one root preimage.  The three preimage roots form one root triangle, so the unique edgewise lift is automatically a root flow.  On terminal edges it equals `x`, because `t=Q_pi x` there and `Q_pi` is injective.

Thus a type-`5` zero-norm loop is root-linearizable if and only if `t_gamma` has no zero edge.

### Theorem 5.3 — type `4` has only a binary extension

For type `4`, let `k_0` generate `ker Q_pi`.  One may choose a linear section

\[
s:W\to E_5
\]

such that every `s(t)`, `t\ne0`, is a root and

\[
s(u)+s(v)+s(\kappa)=0.
\]

Every root over a nonzero `t` is

\[
s(t)+b k_0,
\qquad b\in F_2.
\]

At a cubic vertex root conservation is therefore exactly

\[
b_1+b_2+b_3=0.
\]

The terminal bits prescribed by `x` have even total: both `x` and the linear section `s(t)` have total terminal sum zero.  Since the four-pole is connected, the prescribed terminal bits extend to a binary flow.  Consequently a type-`4` zero-norm loop is root-linearizable if and only if `t_gamma` has no zero edge.

Thus the generic singleton-forbidden cut system collapses, for the actual loop word, to one standard binary flow extension which is automatically solvable after the edge-local test.

## 6. Rank-one types: matching plus two-factor

Now let `pi` have type `3+2` or `2+2`.  Then

\[
t_\gamma(e)\in\{0,\kappa\}.
\]

At an internal cubic vertex, conservation permits only

\[
(0,0,0)
\qquad\text{or}\qquad
(0,\kappa,\kappa).
\]

### Proposition 6.1 — all-zero vertices never lift

For type `3+2`, the root fibre over zero consists of one nonzero root `a`; three copies sum to `a`, not zero.

For type `2+2`, the zero fibre consists of two linearly independent roots `a,b`; no sum of three elements chosen from `\{a,b\}` is zero.

Hence a root lift cannot contain an all-zero cubic vertex.

Assume from now on that no such vertex occurs.  Then

\[
\boxed{
 M:=t_\gamma^{-1}(0)
}
\]

is a perfect matching of the internal cubic vertices, including the two zero-valued terminal semiedges, and

\[
\boxed{
 F:=t_\gamma^{-1}(\kappa)
}
\]

has degree two at every internal vertex.  Its components are:

- one path joining the two `kappa`-valued terminals, which form one block of `M_1`;
- zero or more closed cycles.

### Theorem 6.2 — exact even-component criterion

For types `3+2` and `2+2`, a root lift exists if and only if every component of `F` contains an even number of internal vertices.

#### Necessity for type `3+2`

The zero fibre is one root `a`; the `kappa` fibre is `\{r,r+a\}`.  At every vertex of an `F` component, the two `F`-edge choices must differ by `a`.  Thus choices alternate.  A closed cycle closes only when its length is even.  The two terminal values on the unique path are equal, so that path also requires an even number of internal vertices.

#### Sufficiency for type `3+2`

Put root `a` on every matching edge and alternate `r,r+a` on each even `F` component, beginning with the prescribed terminal root on the terminal path.  At every internal vertex

\[
a+r+(r+a)=0.
\]

#### Necessity for type `2+2`

The zero fibre is `\{a,b\}` with `a,b` independent.  Summing root conservation over all vertices of an `F` component cancels every internal `F` edge.  On a cycle, the sum of its incident matching roots must be zero.  On the terminal path, the two equal prescribed terminal roots cancel and the same condition remains.  An odd number of terms chosen from `\{a,b\}` cannot sum to zero.

#### Sufficiency for type `2+2`

Choose the boundary-compatible root `a` on every matching edge.  The `kappa` fibre is an affine torsor over `ker Q_pi`, so if `r` is the prescribed terminal root then `r+a` is also in the fibre.  Alternate `r,r+a` on every even component.  Again

\[
a+r+(r+a)=0
\]

at each vertex. ∎

## 7. Tait resolution

The preceding four cases admit one common interpretation.

### Definition 7.1

A **Tait resolution** of the actual switch flow is:

- for types `4` and `5`, the nowhere-zero `W`-flow `t_gamma` itself;
- for types `3+2` and `2+2`, the three-edge-colouring obtained by colouring every matching edge in `M` by `kappa` and alternating colours `u,v` on every component of `F`.

### Theorem 7.2 — rainbow root lifting equals Tait resolution

A zero-norm lifted canonical rainbow loop is root-admissibly linearizable if and only if its switch flow admits a Tait resolution.

Equivalently, failure is exactly one of:

1. **zero-edge obstruction:** a type `4` or `5` switch flow has a zero edge;
2. **zero-vertex obstruction:** a rank-one switch flow has an all-zero cubic vertex;
3. **odd-component obstruction:** the rank-one nonzero support contains an odd cycle or an odd terminal path.

#### Proof

Types `4` and `5` are Theorems 5.2 and 5.3.  Rank-one types are Theorem 6.2.  In the latter case an alternating colouring exists precisely on even components, and at each vertex its three colours are `u,v,kappa`. ∎

Thus every root-linearizable rainbow loop exposes a Tait-coloured four-pole.  Every non-linearizable loop exposes a concrete edge-, vertex-, or component-level parity certificate.

## 8. Why the earlier general tension universe was too large

For an arbitrary affine-line system with coefficient space `F_2^2`, exact quotient enumeration shows that genuinely four-valued irreducible tension certificates exist.  They begin when the four potential levels have almost complete pairwise interaction.

They do not arise from the exact three-switch word automatically.  The genuine loop satisfies all of:

- `w_1=w_3`;
- `t_gamma` lies in the two-generator switch plane `W`;
- zero norm restricts `t_gamma` to `W cap im Q_pi`;
- the root fibres are the four classes in Section 4;
- cubic conservation forces either a Tait flow or a matching-plus-two-factor skeleton.

Therefore the correct order of reasoning is:

\[
\text{loop word}
\to
\text{switch plane}
\to
\text{quotient flow}
\to
\text{root-fibre lift}
\to
\text{Tait resolution},
\]

not an unrestricted census of affine-line constraint systems.

## 9. Updated mechanism diagram

The holonomy branch now reads

\[
\boxed{
\begin{array}{c}
\text{rainbow }C_3\text{ routing loop}
\\ \downarrow
\\
(\pi,z)\in (Z_1(P)\otimes E_5)\rtimes S_5
\\ \downarrow
\\
\text{norm defect }N_\pi z
\\ \downarrow
\\
\begin{cases}
N_\pi z\ne0
&\Rightarrow\text{pure interior translation / period doubling},
\\
N_\pi z=0
&\Rightarrow Q_\pi r=t_\gamma.
\end{cases}
\\ \downarrow
\\
\begin{cases}
\text{Tait resolution}
&\Rightarrow\text{root-linearized pure label holonomy},
\\
\text{no Tait resolution}
&\Rightarrow\text{zero or oddness certificate}.
\end{cases}
\end{array}
}
\]

This is now a composition-level mechanism.  The next theorem must convert the two outputs into strict progress:

- a Tait-coloured shore must be replaceable, serially decomposable, or force profile expansion;
- a zero/oddness certificate must force a smaller separator, an odd-ring reduction, or a nontrivial orbit escape.

## 10. Trust boundary

The following are theorem-level:

- the three-switch chain identity;
- the quotient-flow lifting equivalence;
- the full-rank lifting proofs;
- the rank-one matching/two-factor structure;
- the even-component criterion;
- the Tait-resolution equivalence.

The following are exact finite computations:

- all sixteen boundary monodromies;
- `w_1=w_3` for every lift;
- `pi u=v`, `pi v=u` for all four double transpositions;
- the switch-plane/root-fibre table.

The following remain open:

- proving that every Tait-resolved kernel shore is replaceable or expands its complete five-support profile;
- converting an odd component into a strict minimal-counterexample reduction;
- handling nonzero norm defect by orbit escape or decomposition;
- proving that every abstract boundary loop used in the minimal-kernel argument has the required repeatable interior lift;
- integrating Tait resolution with the orientation transgression and the good-surface obstruction arrangement.

## 11. Next exact tasks

1. Compute the complete five-support boundary profile forced by a Tait-resolved four-pole together with the three rainbow switch paths.
2. Test whether the Tait resolution makes the rainbow loop Kempe-contractible in the sense of flow reconfiguration.
3. Formulate an odd-ring reduction for an odd component of `F` and determine its transfer state under gluing.
4. Relate the rank-one even-component criterion to standard oddness and multipole three-edge-colouring invariants.
5. Keep the four-valued abstract tension examples as a trust-boundary warning; do not admit them into the main branch without an actual three-switch realization.
