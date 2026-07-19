# Universal orthogonal root lifts for AffineCDC and five-support covers

**Programme:** `AffineCDC — Research Lead`  
**Status:** theorem-level research checkpoint; not canonical pending review  
**Scope:** the universal eight-index cover module, its Hamming Lagrangian quotient, and five-coordinate minus-type slices

## 1. The even-weight root module

Let

\[
\Gamma=\mathbf F_2^3
\]

and use the eight points of `Γ` as a coordinate set. Put

\[
\mathcal H_8
:=
\left\{z=(z_s)_{s\in\Gamma}\in\mathbf F_2^\Gamma:
\sum_{s\in\Gamma}z_s=0
\right\}.
\]

For distinct `s,t∈Γ`, write

\[
r_{s,t}:=e_s+e_t\in\mathcal H_8.
\]

The **roots** are

\[
\mathcal R_8:=\{r_{s,t}:s\neq t\}.
\]

They are naturally the twenty-eight edges of `K_8` on vertex set `Γ`.

Define the moment map

\[
\mu:\mathcal H_8\longrightarrow\Gamma,
\qquad
\mu(z):=\sum_{s\in\Gamma}z_s s.
\]

Then

\[
\boxed{\mu(r_{s,t})=s+t.}
\]

Hence every root has nonzero image. For each `0\neq h∈Γ`, the roots above `h` are

\[
\mu^{-1}(h)\cap\mathcal R_8
=
\{r_{s,s+h}:s\in\Gamma\}/(s\sim s+h),
\]

namely the four edges of the affine perfect matching in direction `h`.

## 2. The Hamming kernel

Put

\[
\mathcal K:=\ker\mu.
\]

Explicitly,

\[
\mathcal K
=
\left\{
 z\in\mathbf F_2^\Gamma:
 \sum_s z_s=0,
 \ \sum_s z_s s=0
\right\}.
\]

### Theorem 2.1 — extended-Hamming kernel

The code `\mathcal K` is the binary extended Hamming code `[8,4,4]`, equivalently
`RM(1,3)`. Its words have weights

\[
0,\quad 4,\quad 8,
\]

with weight distribution

\[
1+14X^4+X^8.
\]

The fourteen weight-four words are the indicators of the fourteen affine planes
in `Γ`, and the weight-eight word is the all-one word `\mathbf1`.

#### Proof

The parity coordinate together with the three coordinate moments gives a
rank-four parity-check map on `\mathbf F_2^8`, so `\dim\mathcal K=4`. A nonzero
word of weight two has nonzero moment, hence the minimum weight is at least four.
Every affine plane has even cardinality and zero xor-sum, so its indicator lies
in `\mathcal K`. The fourteen affine planes, together with `0` and `\mathbf1`,
account for all sixteen codewords. ∎

In particular,

\[
0\longrightarrow\mathcal K
\longrightarrow\mathcal H_8
\xrightarrow{\mu}\Gamma
\longrightarrow0
\]

is exact.

## 3. The plus-type six-space

Let `\mathbf1` denote the all-one word. It belongs to `\mathcal K`. For even-weight
`z`, define

\[
q_8(z):=\frac{\operatorname{wt}(z)}2\pmod2.
\]

Its polar form on `\mathcal H_8` is the standard dot product:

\[
B_8(z,w)=q_8(z+w)+q_8(z)+q_8(w)=z\cdot w.
\]

The radical of `B_8|_{\mathcal H_8}` is exactly `\langle\mathbf1\rangle`, and
`q_8(\mathbf1)=0`. Therefore `q_8` descends to a nondegenerate quadratic form on

\[
\mathcal V_8:=\mathcal H_8/\langle\mathbf1\rangle.
\]

Put

\[
L:=\mathcal K/\langle\mathbf1\rangle\leq\mathcal V_8.
\]

### Theorem 3.1 — universal orthogonal extension

The quadratic space `(\mathcal V_8,q_8)` is the six-dimensional plus-type space,
and `L` is a totally singular Lagrangian. Moreover,

\[
\boxed{
0\longrightarrow L
\longrightarrow\mathcal V_8
\xrightarrow{\bar\mu}\Gamma
\longrightarrow0.
}
\]

The twenty-eight anisotropic vectors of `\mathcal V_8` are canonically in
bijection with the twenty-eight roots `r_{s,t}`: every anisotropic class has a
unique representative of weight two.

#### Proof

Every word of `\mathcal K` has weight divisible by four, so `q_8` vanishes on
`L`. Since `\dim L=3=\frac12\dim\mathcal V_8`, it is a totally singular
Lagrangian; hence the quadratic space has plus type. If an even word has
`q_8=1`, its weight is two or six. Adding `\mathbf1` exchanges weights two and
six, so every anisotropic quotient class has a unique weight-two representative.
∎

Thus the roots of `K_8` are not merely a convenient alphabet: they are the
anisotropic points of `O^+(6,2)`. Coordinate permutations give the full natural
`S_8` action; choosing the Hamming Lagrangian `L` breaks this symmetry to its
Hamming/Fano stabilizer.

## 4. Root flows and indexed even double covers

Let `G` be a finite loopless multigraph. A **root flow** is a flow

\[
g:E(G)\longrightarrow\mathcal R_8\subset\mathcal H_8.
\]

For `s∈Γ`, define

\[
F_s:=\{e\in E(G):g(e)_s=1\}.
\]

### Theorem 4.1 — root-flow/cover equivalence

Root flows `g:E(G)\to\mathcal R_8` are equivalent to `Γ`-indexed even double
covers

\[
(F_s)_{s\in\Gamma}
\]

in which every edge occurs in exactly two indexed supports.

#### Proof

Every coordinate of a flow is an even edge support, and every root has exactly
two nonzero coordinates. Conversely, the incidence word of the two supports
containing an edge is a root, and coordinatewise evenness is exactly the flow
equation in `\mathcal H_8`. ∎

If `G` is cubic, the three roots incident with any vertex sum to zero. Three
weight-two words sum to zero exactly when they are the three edges of a triangle
on three coordinate points. Thus the local state of a root flow is precisely an
affine triangle of support indices.

## 5. AffineCDC as anisotropic lifting

Let

\[
f:E(G)\longrightarrow\Gamma\setminus\{0\}
\]

be a nowhere-zero rank-three flow on a finite cubic graph.

### Theorem 5.1 — compatible families are root lifts

There is a canonical equivalence between:

1. globally compatible AffineCDC local families for `f`;
2. root flows
   \[
   g:E(G)\to\mathcal R_8
   \]
   satisfying
   \[
   \mu\circ g=f;
   \]
3. `Γ`-indexed even double covers whose edge-index pair has difference `f(e)`.

#### Proof

A root above `h=f(e)` is exactly a pair `{s,s+h}`. At a cubic vertex, three
incident roots satisfy the flow equation exactly when they form a triangle
`{s_1,s_2,s_3}`. If the incident flow values are the three nonzero elements of a
plane `W`, then this triangle is

\[
\{s_1,s_2,s_3\}=m+(W\setminus\{0\}),
\qquad
m=s_1+s_2+s_3,
\]

which is the intrinsic local affine-family formula. Equality of the root on the
two ends of an edge is exactly edge compatibility. The cover interpretation is
Theorem 4.1. ∎

Consequently the rank-three AffineCDC compatibility theorem may be restated as:

> Every nowhere-zero `F_2^3`-flow on a finite cubic graph lifts through the
> Hamming-Lagrangian quotient
> \[
> \mathcal V_8\twoheadrightarrow\mathcal V_8/L\cong\mathbf F_2^3
> \]
> to an anisotropic `O^+(6,2)`-valued flow.

This is equivalent to the existing affine/Fano theorem; it is a new universal
root-space presentation, not an additional unproved existence claim.

## 6. Five-coordinate slices

Let `A\subset\Gamma` have cardinality five and put `T:=\Gamma\setminus A`, so
`|T|=3`. Define

\[
\mathcal H_A
:=
\{z\in\mathcal H_8:\operatorname{supp}z\subseteq A\},
\qquad
\mathcal R_A
:=
\{r_{s,t}:s,t\in A,\ s\neq t\}.
\]

Then `\dim\mathcal H_A=4`, and `\mathcal R_A` consists of the ten edges of the
induced `K_5` on `A`.

Let

\[
r_T:=\sum_{t\in T}t,
\qquad
P_T:=T\cup\{r_T\}.
\]

This is the affine plane spanned by `T`. Let

\[
C_T:=\Gamma\setminus P_T.
\]

Then `C_T\subseteq A` is the parallel affine plane disjoint from `P_T`.

### Theorem 6.1 — the five-slice singular extension

The restriction

\[
\mu_A:=\mu|_{\mathcal H_A}:\mathcal H_A\longrightarrow\Gamma
\]

is surjective, and

\[
\boxed{
\ker\mu_A
=
\langle k_A\rangle,
\qquad
k_A:=\mathbf1_{C_T}.
}
\]

Moreover:

1. `k_A` has weight four and is singular for `q_8|_{\mathcal H_A}`;
2. `(\mathcal H_A,q_8)` is the four-dimensional minus-type quadratic space;
3. its ten anisotropic vectors are exactly `\mathcal R_A`;
4. the doubled-fibre plane in the quotient is the direction plane of `P_T`.

#### Proof

A five-point subset of `Γ` cannot lie in an affine plane, so its pairwise
differences span `Γ`; hence `\mu_A` is surjective. Its kernel is one-dimensional.
The affine plane `C_T` has even cardinality and zero xor-sum, so `k_A` lies in the
kernel and generates it.

The nonzero even words on five coordinates have weights two or four. The ten
weight-two words have `q_8=1`, while the five weight-four words have `q_8=0`.
Thus the restriction is the minus-type four-space and its anisotropic vectors are
precisely the roots of `K_5`.

Finally, in `\mathcal H_A=k_A^\perp` relative to the quotient direction, a word
orthogonal to `k_A` has zero coordinate at `r_T` and is an even word supported on
the affine coset `C_T`. Its moment lies in, and spans, the direction plane of
`C_T` and `P_T`. ∎

This recovers the previously isolated singular-line quotient

\[
0\longrightarrow\langle k_A\rangle
\longrightarrow\mathcal H_A
\xrightarrow{\mu_A}\Gamma
\longrightarrow0.
\]

## 7. Orthogonal complement of an omitted triple

Let `\overline{\mathcal H_A}` denote the image of `\mathcal H_A` in
`\mathcal V_8`. Let

\[
U_T
:=
\operatorname{span}\{r_{u,v}:u,v\in T\}
\leq\mathcal V_8.
\]

The three nonzero vectors of `U_T` are the three edges of the triangle on `T`, so
`U_T` is an anisotropic binary plane.

### Theorem 7.1 — omitted-triangle orthogonality

One has

\[
\boxed{
\overline{\mathcal H_A}=U_T^\perp.
}
\]

Thus every five-coordinate slice is a nondegenerate minus-type four-space, the
orthogonal complement of the anisotropic plane carried by the omitted triple.

#### Proof

A vector represented by an even word supported on `A` has zero dot product with
every even word supported on the disjoint set `T`. Hence
`\overline{\mathcal H_A}\subseteq U_T^\perp`. Both spaces have dimension four,
so equality holds. ∎

The fifty-six choices of omitted triples are therefore the fifty-six anisotropic
planes, or equivalently their minus-type orthogonal four-spaces, in the universal
plus-type six-space.

## 8. The five-support conjecture inside the universal space

For a finite cubic loopless multigraph `G`, the following are equivalent.

1. `G` has a five-support double cover.
2. `G` has a root flow whose values all lie in `\mathcal R_A` for some
   five-subset `A\subset\Gamma`.
3. `G` has an anisotropic `\mathcal V_8`-flow whose image lies in
   `U_T^\perp` for some anisotropic plane `U_T`.
4. `G` has an anisotropic flow in the minus-type four-space
   `(\mathcal H_A,q_8)`.
5. For some nowhere-zero rank-three flow `f` and some five-slice singular
   quotient `\mathcal H_A\twoheadrightarrow\Gamma`, the flow `f` has an
   anisotropic lift.

The ordinary AffineCDC theorem supplies an anisotropic flow in the full plus-type
six-space. The five-support strengthening asks whether one may choose such a
flow inside one of its minus-type four-dimensional coordinate slices.

Equivalently:

\[
\boxed{
\text{CDC via AffineCDC}
=
\text{unrestricted anisotropic lift in }O^+(6,2),
}
\]

whereas

\[
\boxed{
5\text{-support CDC}
=
\text{anisotropic lift confined to }O^-(4,2)=U_T^\perp.
}
\]

## 9. Relation to the current obstruction calculations

Fixing a five-subset `A` and projecting

\[
\mathcal H_A\twoheadrightarrow\Gamma
\]

recovers all of the earlier five-support formulations:

- the three omitted indices are `T`;
- their affine direction plane is the doubled-fibre plane;
- the kernel is the singular line `\langle k_A\rangle`;
- the component-parity obstruction is the obstruction to correcting vertex
  conservation in that kernel line;
- the Schur-product equation is a coordinate chart on the anisotropic quadric of
  `\mathcal H_A`;
- the matching/four-flow bridge is the corresponding factorization of the ten
  anisotropic roots.

Thus the fixed-triple, Schur, matching, quadratic-cycle, and singular-quotient
pictures are not parallel coincidences. They are coordinate resolutions of one
subspace-constrained root-lifting problem.

## 10. Reliability and next questions

The finite-dimensional code and quadratic-space arguments above are complete.
The equivalence with the existing AffineCDC compatible-family API uses the
already established local affine-triangle interpretation. No claim is made that
this presentation is absent from the literature; the `K_5`-flow, matroid-map,
and Petersen-colouring literature require a dedicated audit.

The next structural questions are:

1. characterize the moduli of anisotropic root flows in `O^+(6,2)` and their
   intersections with the fifty-six minus-type four-slices;
2. determine whether the Hamming Lagrangian and its self-duality give a shorter
   invariant proof of rank-three affine compatibility;
3. express switch moves as root-flow deformations relative to the pair
   `(L,U_T^\perp)`;
4. compare the singular-line lift obstruction with, but do not conflate it with,
   the existing rank-four Pfaffian affine-compatibility residue;
5. identify the precise matroidal or tension/flow-continuous name of the
   `K_5` root-flow formulation.