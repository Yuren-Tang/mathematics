# Interior affine holonomy and norm defects for rainbow routing

**Programme:** `AffineCDC — Research Lead`  
**Status:** theorem-level ambient chain and representation mechanism, with exact finite `E_5` computation; graph-level root-admissibility consequences remain programme-level  
**Parents:** `FIVE_CDC_ROUTING_WEIGHT_HOLONOMY_V1.md`, `FIVE_CDC_ORIENTATION_TRANSGRESSION_COEFFICIENT_HOLONOMY_V1.md`

## 1. Purpose

The boundary rainbow triangle returns to the same support-unordered four-terminal state but induces a nontrivial permutation of the five support indices. Boundary monodromy alone does not record what happened inside the four-pole.

This packet identifies the natural interior lift.

For one lifted quotient loop, the complete ambient datum is

\[
(\pi,z)
\in
\bigl(Z_1(P;F_2)\otimes E_5\bigr)\rtimes S_5,
\]

where:

- `\pi` is the support-index monodromy;
- `z` is a closed interior support-chain defect;
- `E_5` is the even subspace of `F_2^5`.

The principal conclusions are:

1. repeated traversal is governed by the norm operator
   \[
   N_\pi=1+\pi+\cdots+\pi^{m-1},
   \qquad m=\operatorname{ord}(\pi);
   \]
2. the pure interior translation
   \[
   d_\gamma=N_\pi z
   \]
   is independent of affine origin;
3. for all four support-permutation types occurring in the rainbow triangle,
   \[
   H^1(\langle\pi\rangle,E_5)=0;
   \]
4. consequently `d_gamma` is the complete ambient affine-conjugacy obstruction;
5. the possible norm-defect space has dimension only `2,1,1,0` for the four types
   \[
   2+2,\quad4,\quad3+2,\quad5.
   \]

Thus the interior holonomy does not open an uncontrolled new classification. It reduces to at most two cycle-space channels.

No claim is made that a nonzero norm defect already forces profile escape, or that an ambient affine conjugacy is realized inside the nonlinear root-valued cover space.

## 2. Indexed support chains

Let `P` be a connected four-pole with terminal set `T`. Work over `F_2`.

Write

\[
C_1(P)=F_2^{E(P)}
\]

for edge chains, with the boundary map retaining the four terminal incidences. Let

\[
Z_1(P)=\ker\partial
\]

be the absolute interior cycle space.

An indexed five-support cover is represented by

\[
x=(x_1,\ldots,x_5)
\in C_1(P)\otimes F_2^5,
\]

where `x_i` is the incidence chain of support `i`.

Every edge belongs to exactly two supports. Hence its five-coordinate incidence vector has weight two and lies in

\[
E_5=
\left\{
 a\in F_2^5:
 \sum_{i=1}^5 a_i=0
\right\}.
\]

Therefore

\[
\boxed{
x\in C_1(P)\otimes E_5.
}
\]

The indexed boundary signature is `\partial x`.

### Proposition 2.1 — equal-boundary differences are cycle-valued

If two indexed five-support chains `x,x'` have the same terminal traces, then

\[
\boxed{
x+x'\in Z_1(P)\otimes E_5.
}
\]

#### Proof

Coordinatewise equality of terminal traces gives

\[
\partial(x_i+x_i')=0
\]

for every support coordinate. Both chains are `E_5`-valued edgewise, so their difference is also `E_5`-valued. ∎

## 3. Interior defect of a quotient loop

Let `gamma` be a lifted reconfiguration walk beginning at an indexed cover `x`. Suppose its support-unordered boundary state closes, and choose the induced support-index transport

\[
\pi\in S_5
\]

so that

\[
\partial x^\gamma=\pi(\partial x).
\]

Define

\[
\boxed{
z_\gamma=x^\gamma+\pi x.
}
\]

### Proposition 3.1 — the defect is an interior cycle tensor

\[
\boxed{
z_\gamma\in M_P,
\qquad
M_P:=Z_1(P)\otimes E_5.
}
\]

#### Proof

The two chains `x^gamma` and `pi x` have the same indexed boundary traces by construction. Apply Proposition 2.1. ∎

The pair

\[
\boxed{(\pi,z_\gamma)}
\]

is the ambient interior holonomy datum.

A **repeatable lifted loop** means that subsequent traversals are obtained by transporting the chosen lifted switch sequence through the current support labels. On the ambient difference torsor, one traversal then has the affine form

\[
A_{\pi,z}(u)=\pi u+z.
\]

This is the standard semidirect-product composition law

\[
(\pi,z)(\sigma,w)
=
(\pi\sigma,z+\pi w).
\]

The nonlinear question of which ambient points remain root-valued admissible covers is deliberately postponed.

## 4. Change of affine origin

Changing the ambient origin by `y\in M_P` conjugates `A_{pi,z}` by the translation `u\mapsto u+y`. Over `F_2`, the new translation part is

\[
\boxed{
z' = z+(1+\pi)y.
}
\]

Thus the raw defect `z` depends on origin, while its class modulo

\[
\operatorname{im}(1+\pi)
\]

is the first natural affine invariant.

## 5. Iteration and the norm defect

Let

\[
m=\operatorname{ord}(\pi),
\qquad
N_\pi=1+\pi+\cdots+\pi^{m-1}.
\]

### Theorem 5.1 — affine iteration law

For every positive integer `r`,

\[
A_{\pi,z}^r(u)
=
\pi^r u+
\sum_{j=0}^{r-1}\pi^jz.
\]

In particular,

\[
\boxed{
A_{\pi,z}^m(u)=u+d,
\qquad
d:=N_\pi z.
}
\]

Moreover

\[
\pi d=d.
\]

#### Proof

The iteration formula follows by induction from the semidirect-product law. Since `pi^m=1`, the `m`-th power has trivial linear part. Finally

\[
\pi N_\pi=N_\pi
\]

because cyclically permuting the summands leaves their sum unchanged. ∎

Call

\[
\boxed{d_\gamma=N_\pi z_\gamma}
\]

the **interior norm defect**.

### Proposition 5.2 — origin invariance

The norm defect is unchanged by every affine-origin change

\[
z\mapsto z+(1+\pi)y.
\]

#### Proof

\[
N_\pi(1+\pi)
=
(1+\pi+\cdots+\pi^{m-1})(1+\pi)
=
1+\pi^m
=0
\]

over `F_2`. ∎

Thus `d_gamma` is intrinsic to the ambient affine-conjugacy class of the lifted loop.

## 6. Exact `E_5` norm calculation

Let `pi` act on `E_5` by permuting the five coordinates.

For a cyclic group generated by `pi`, write

\[
H^1(\langle\pi\rangle,E_5)
=
\ker N_\pi/\operatorname{im}(1+\pi).
\]

The four support-permutation types occurring among the sixteen rainbow monodromies are

\[
2^2 1,
\qquad
4 1,
\qquad
3 2,
\qquad
5.
\]

### Computational Theorem 6.1 — norm and cohomology table

For representatives of these four classes, the exact dimensions are

\[
\begin{array}{c|c|c|c|c|c|c}
\text{type}
&m
&\dim E_5^\pi
&\operatorname{rank}N_\pi
&\dim\ker N_\pi
&\operatorname{rank}(1+\pi)
&\dim H^1
\\
\hline
2^2 1&2&2&2&2&2&0\\
4 1&4&1&1&3&3&0\\
3 2&6&1&1&3&3&0\\
5&5&0&0&4&4&0.
\end{array}
\]

In every case,

\[
\boxed{
\operatorname{im}N_\pi=E_5^\pi
}
\]

and

\[
\boxed{
H^1(\langle\pi\rangle,E_5)=0.
}
\]

The fixed subspaces can be written explicitly as follows:

\[
\begin{array}{c|c}
\pi& E_5^\pi\\
\hline
(12)(34)&
\langle11000,00110\rangle\\
(1234)&
\langle11110\rangle\\
(123)(45)&
\langle00011\rangle\\
(12345)&0.
\end{array}
\]

#### Proof status

Exact dependency-free Wolfram computation on the private notebook branch. The fixed-space descriptions also follow directly by requiring coordinates to be constant on permutation orbits and imposing even total parity. ∎

### Corollary 6.2 — tensor stability

For

\[
M_P=Z_1(P)\otimes E_5,
\]

where `pi` acts trivially on the cycle-space factor,

\[
\boxed{
H^1(\langle\pi\rangle,M_P)=0.
}
\]

Moreover

\[
M_P^\pi
=
Z_1(P)\otimes E_5^\pi,
\]

so the possible norm-defect channel count is respectively

\[
2\dim Z_1(P),
\quad
\dim Z_1(P),
\quad
\dim Z_1(P),
\quad
0.
\]

#### Proof

Both `N_pi` and `1+pi` act as the identity on the cycle-space factor tensored with the corresponding operator on `E_5`. ∎

## 7. Complete ambient affine classification

### Theorem 7.1 — norm defect is complete

Let `pi` have one of the four rainbow types and let

\[
A(u)=\pi u+z
\]

act on `M_P`.

1. If
   \[
   d=N_\pi z\ne0,
   \]
   then
   \[
   A^m=t_d
   \]
   is a nontrivial pure translation. The order of `A` is exactly `2m`.

2. If
   \[
   d=0,
   \]
   then there exists `y\in M_P` such that
   \[
   z=(1+\pi)y.
   \]
   Translation by `y` conjugates `A` to the pure linear action `u\mapsto\pi u`.

Hence

\[
\boxed{
N_\pi z
}
\]

is the complete obstruction to translation-conjugating the ambient affine holonomy to its boundary permutation.

#### Proof

If `d\ne0`, Theorem 5.1 gives `A^m=t_d`. Binary translation has order two, so `A^{2m}=1`; projection to `pi` forces the order to be a multiple of `m`, and `A^m\ne1`, hence the order is `2m`.

If `d=0`, then `z\in\ker N_pi`. Corollary 6.2 gives

\[
\ker N_\pi=\operatorname{im}(1+\pi),
\]

so `z=(1+pi)y`. Apply the origin-change formula. ∎

### Corollary 7.2 — the five-cycle type is always ambient-linearizable

If `pi` is a five-cycle, then

\[
N_\pi=0
\]

on `E_5`, hence on `M_P`. Every affine lift of that type is translation-conjugate to the pure five-cycle action.

### Corollary 7.3 — low-channel period doubling

For the other three rainbow types, a nonzero interior norm defect can occur only in:

- two paired-support channels for type `2^2 1`;
- one four-support channel for type `4 1`;
- one transposed-pair channel for type `3 2`.

Thus every non-linearizable rainbow lift produces a pure internal translation in a fixed submodule of dimension at most two per independent shore cycle.

## 8. Concrete support meaning of the channels

The explicit fixed vectors give the following interpretations.

### Type `2^2 1`

For representative `(12)(34)`,

\[
d
=
q_1\otimes11000
+
q_2\otimes00110
\]

for interior cycles `q_1,q_2`. These are two independent paired-support channels.

### Type `4 1`

For representative `(1234)`,

\[
d=q\otimes11110.
\]

The pure interior defect toggles the four supports in the four-cycle orbit and leaves the fixed support untouched.

### Type `3 2`

For representative `(123)(45)`,

\[
d=q\otimes00011.
\]

Only the transposed support pair can carry the accumulated pure interior defect.

### Type `5`

No invariant even support vector exists, so no pure interior norm defect can remain after five traversals.

These are ambient chain statements. An individual tensor expression need not by itself preserve the edgewise root condition when applied to an arbitrary cover; admissibility is guaranteed only for defects arising from actual lifted loops.

## 9. Relation to deterministic routing kernels

A nonzero norm defect produces, after `m` traversals:

- the same support labels;
- the same boundary signature;
- a different interior indexed support chain related by one closed cycle tensor `d`.

This creates a direct test against the previously proved unique routing policies of the residual four-pole kernels.

The next graph-theoretic target is:

\[
\boxed{
\begin{array}{l}
 d_\gamma\ne0
 \Longrightarrow
 \text{the induced internal cycle switch changes some forced routing choice,}\
 \text{or else exposes a smaller separator / serial decomposition};\\[2mm]
 d_\gamma=0
 \Longrightarrow
 \text{the ambient linearization can be realized by admissible covers,}\
 \text{or failure of realization itself exposes a root-valued obstruction.}
\end{array}
}
\]

This is the precise interface between the finite boundary automaton and the unbounded interior graph.

## 10. Trust boundary

The following are theorem-level:

- equal-boundary differences lie in `Z_1(P) tensor E_5`;
- the semidirect affine iteration and origin-change formulas;
- origin invariance of the norm defect;
- the exact `E_5` norm, fixed-space, and cyclic-cohomology table;
- vanishing of `H^1` after tensoring with any shore cycle space;
- complete ambient affine classification by `N_pi z`.

The following remain open:

- proving that every abstract boundary rainbow loop has a repeatable lifted realization in an arbitrary four-pole;
- classifying which ambient conjugating origins correspond to root-valued admissible covers;
- showing that a nonzero norm defect forces profile escape or graph decomposition;
- connecting the cycle-tensor defect functorially to the fixed-Fano-flow gauge code `B_f` and its orientation transgression;
- eliminating the tree and holonomy kernels in all minimal-counterexample shores.

No five-cycle double cover theorem, Tutte five-flow theorem, or Four Colour theorem is claimed.

## 11. Next exact tasks

1. **Root-admissible linearization:** characterize when `z=(1+pi)y` has a solution `y` within the difference set of actual root-valued covers.
2. **Routing stabilizer:** determine the subgroup of internal cycle tensors preserving every unique routing decision of a Type H kernel.
3. **Defect-to-cut theorem:** prove that a nonzero routing-preserving norm defect forces a smaller edge separator or serial four-pole decomposition.
4. **Gauge comparison:** construct the map, when defined, from `M_P` to the global gauge code or orientation cohomology and calculate the image of `d_gamma`.
5. **Laboratory verification:** add `(pi,z,d)` output to exact small-four-pole and snark reconfiguration verifiers only after the chain-level extraction is implemented.