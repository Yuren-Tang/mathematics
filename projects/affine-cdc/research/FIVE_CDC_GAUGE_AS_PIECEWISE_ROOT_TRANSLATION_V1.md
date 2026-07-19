# Gauge modes as piecewise translations of AffineCDC root lifts

**Programme:** `AffineCDC — Research Lead`  
**Status:** theorem-level structural checkpoint; not canonical pending review  
**Parents:** `FIVE_CDC_UNIVERSAL_ORTHOGONAL_ROOT_LIFT_V1.md`, canonical `gauge/gauge-modes-and-circuits.md`

## 1. Root fibres and translations

Let

\[
\Gamma=F_2^3
\]

and let the eight support indices be the points of `\Gamma`. For `0\neq h\in
\Gamma`, the four roots above `h` are

\[
\mathcal R_h
=
\bigl\{r_{s,s+h}:s\in\Gamma\bigr\}/(s\sim s+h).
\]

For `k\in\Gamma`, define

\[
\tau_k(r_{s,s+h})
:=
r_{s+k,s+h+k}.
\]

Since translation by `h` exchanges the two endpoints of the pair,

\[
\boxed{\tau_{k+h}=\tau_k\quad\text{on }\mathcal R_h.}
\]

Thus the translation action on the fibre `\mathcal R_h` factors through

\[
Q_h=\Gamma/\langle h\rangle.
\]

## 2. Vertex translation fields

Let `G` be a finite loopless cubic multigraph and let

\[
f:E(G)\longrightarrow\Gamma\setminus\{0\}
\]

be a nowhere-zero flow. Fix one AffineCDC root lift

\[
g:E(G)\longrightarrow\mathcal R_8
\]

with moment `f`.

A **vertex translation field** is a map

\[
k:V(G)\longrightarrow\Gamma.
\]

Call it **admissible for `f`** when

\[
\boxed{
k_u+k_v\in\langle f(e)\rangle
\qquad(e=uv).
}
\]

Equivalently, for every edge there is a unique bit `\lambda_e` satisfying

\[
\boxed{
k_u+k_v=\lambda_e f(e).}
\]

This is exactly the potential equation defining the canonical gauge-moduli code.

### Theorem 2.1 — root-lift torsor theorem

For every admissible translation field `k`, the formula

\[
\boxed{
g^k(e):=\tau_{k_u}(g(e))
}
\]

is independent of the chosen endpoint `u` of `e` and defines another root lift
of the same Fano flow `f`.

Conversely, every root lift `g'` of `f` is uniquely of the form `g^k` for one
admissible vertex translation field `k`.

Hence the root-lift space over `f` is a torsor under the linear space

\[
H_f^0
=
\left\{k:V(G)\to\Gamma:
 k_u+k_v\in\langle f(e)\rangle\text{ on every edge}
\right\}.
\]

#### Proof

Let `e=uv` and put `h=f(e)`. Admissibility gives

\[
k_v=k_u\quad\text{or}\quad k_v=k_u+h.
\]

Since `\tau_{k+h}=\tau_k` on `\mathcal R_h`, the two endpoint definitions agree.
At a vertex `v`, the three incident roots of `g` are the three edges of a local
affine triangle `T_v`. Applying `\tau_{k_v}` translates the whole triangle to
`T_v+k_v`, whose three roots still sum to zero. Thus `g^k` is a root flow. The
moment is unchanged because translating both endpoints of a root pair does not
change their difference.

Conversely, let `g'` be another lift. At a vertex `v`, the local root triangles
of `g` and `g'` project to the same three Fano directions. The intrinsic local
classification says that both are affine triangles with the same direction
plane, so there is a unique translation `k_v\in\Gamma` carrying the first to the
second. On an edge `e=uv`, both endpoint translations carry `g(e)` to the same
root `g'(e)`. The stabilizer of an `h`-root pair under translation is exactly
`\langle h\rangle`, so

\[
k_u+k_v\in\langle h\rangle.
\]

Thus `k` is admissible and `g'=g^k`. Uniqueness follows from the trivial
translation stabilizer of a three-point affine triangle. ∎

## 3. Gauge code versus global support relabelling

The map

\[
k\longmapsto\lambda,
\qquad
k_u+k_v=\lambda_e f(e),
\]

has image equal to the gauge code `\mathcal B_f`.

If `G` is connected, its kernel consists of the constant fields

\[
k_v=c\qquad(v\in V(G)).
\]

A constant field translates all eight support indices globally. Therefore

\[
\boxed{
\mathcal B_f
\cong
H_f^0/\Gamma
}
\]

is the moduli of root lifts modulo global affine relabelling of the support
indices.

This clarifies the meaning of the gauge support: `\operatorname{supp}\lambda`
does not record the source edges whose root labels change. It records the
interfaces across which chosen representatives of the regional translations
jump by the local flow direction.

## 4. Piecewise translation on harmonic cut quotients

Let `0\neq\lambda\in\mathcal B_f`, choose a potential field `k`, and put

\[
S=\operatorname{supp}\lambda.
\]

On every edge outside `S`, one has `k_u=k_v`. Hence `k` is constant on every
connected component `X` of `G-S`; write the constant value as

\[
p_X\in\Gamma.
\]

For a crossing edge `e=XY`, the gauge equation gives

\[
\boxed{f(e)=p_X+p_Y.}
\]

Thus the contracted quotient `Q_S` is the harmonic exact flow–tension quotient
from the canonical gauge theorem.

### Theorem 4.1 — piecewise root-translation theorem

The gauge move associated with `k` acts as follows.

1. Every local root triangle in a source region `X` is translated by `p_X`.
2. Every source edge internal to `X` has its root label translated by `p_X`.
3. For a crossing edge `e=XY` of direction `h=p_X+p_Y`, the two regional
   translations induce the same new root because
   \[
   \tau_{p_Y}=\tau_{p_X+h}=\tau_{p_X}
   \quad\text{on }\mathcal R_h.
   \]

Hence a gauge mode is precisely a system of affine translations applied
piecewise to connected source regions, with exact-tension transition functions
on the quotient interfaces.

This is the root-geometric content of the harmonic cut quotient theorem.

## 5. Low-weight gauge circuits in root form

Assume `\dim\Gamma\leq3`. The canonical circuit classification through weight
six becomes the following list of minimal regional translation patterns.

### Weight two

The quotient consists of two regions joined by two equal-labelled edges of one
direction `h`. After a global normalization, the region translations are

\[
0,\quad h.
\]

Thus one source side is translated by `h`; the two interface root pairs are fixed
because translation by their own direction exchanges their endpoints.

### Weight four

The same two-region translation occurs across an equal-labelled four-edge cut.
The mode is minimal in the gauge matroid even though the regional action has the
same affine form as at weight two.

### Weight six: `6K_2`

Again there are two regions with translations `0,h`, now separated by six
parallel quotient edges of direction `h`.

### Weight six: `2K_3`

There are three source regions with translation potentials

\[
0,\quad x,\quad y.
\]

The doubled interfaces carry directions

\[
x,\quad y,\quad x+y.
\]

The move is a three-region affine repositioning. After fixing the region of
potential zero, the two interfaces incident with it are represented without a
root shift, while the closing `x+y` interface is translated by the class of `x`
(or equivalently `y`) in `\Gamma/\langle x+y\rangle`.

### Weight six: affine-plane `K_4`

There are four source regions with translation potentials

\[
0,\quad x,\quad y,\quad x+y.
\]

Every pair of regions is joined in the quotient, and the interface direction is
the difference of their potentials. This is the smallest gauge circuit whose
regional translations fill an affine plane.

The table shows that low gauge weight measures interface size, not the number of
source edges or target labels changed inside the regions. A weight-two mode may
translate an arbitrarily large source subgraph and therefore alter a large part
of the used-label graph.

## 6. Relation to paired triangle multidesigns

Under the triangle-complex description, a gauge move sends

\[
T_v\longmapsto T_v+k_v
\]

at every source vertex. Equal target-edge occurrences remain paired because the
two endpoint translations agree in the relevant quotient fibre.

Thus the gauge action preserves all of:

- the source graph and its edge pairing;
- the projected Fano flow `f`;
- the root-flow equations;
- exact double coverage.

It may change:

- the root label on many source edges;
- the used-label graph `J_g`;
- the presence of a `K_6` or `K_8-C_5` obstruction;
- which half-cube compression templates occur in `K_8-J_g`.

This is the correct mechanism for moving a fixed Fano flow between compressible
and noncompressible root lifts.

## 7. Strategic consequence

The exact half-cube classification reduces fixed-flow five-support compression
to the following orbit problem.

> Given the `H_f^0`-torsor of root lifts of a nowhere-zero Fano flow, must at least
> one orbit point have a used-label graph containing neither `K_6` nor
> `K_8-C_5`?

Modulo global support translation, the acting space is the gauge code
`\mathcal B_f`. Its low-weight circuits are now explicit piecewise-affine moves
on two, three, or four source regions.

The next finite and structural tasks are:

1. compute how each circuit type changes the two dense label obstructions;
2. determine whether a fixed Fano flow can have every root lift obstructed;
3. if so, identify the minimal harmonic quotient certificate;
4. compare the first genuinely necessary move with the unclassified weight-eight
gauge layer.
