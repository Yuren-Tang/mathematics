# Tait residues, Fano line fields, and the Tutte-flow bridge

**Programme:** `AffineCDC — Research Lead`  
**Status:** theorem-level structural bridge plus programme-level consequences; not canonical pending Director review and literature audit  
**Parents:** `FIVE_CDC_ROUTING_WEIGHT_HOLONOMY_V1.md`, `FIVE_CDC_MIXED_CORE_AFFINE_ARRANGEMENT_V1.md`, `FIVE_CDC_PETERSEN_FANO_FLOW_CLASSIFICATION_V1.md`

## 1. Purpose

The four-pole programme repeatedly produces a three-way structure:

- three perfect matchings of four terminals;
- three routing coordinates;
- three colours in the deterministic routing automata.

This packet identifies the exact rank-two geometry behind that structure and places the present `F_2^3` framework inside the classical hierarchy

\[
\text{Tait colouring / Four Colour Theorem}
\quad\leftrightarrow\quad
F_2^2\text{-flows},
\]

\[
F_2^3\text{-flows}
\quad\leftrightarrow\quad
8\text{-flows},
\]

\[
\text{orientable five-support CDC}
\quad\Longrightarrow\quad
\mathbb Z_5\text{-flow}.
\]

The main structural conclusions are:

1. the three terminal matchings are exactly the three affine directions of `AG(2,2)`;
2. a Tait colouring is exactly a constant Fano-line field inside an `F_2^3` flow;
3. an `F_2^3` cycle switch acts by a Fano-line pivot, with ordinary Tait Kempe switching as the line-preserving special case;
4. a five-support CDC is exactly a root-valued flow in the even subspace of `F_2^5`;
5. an orientable five-support CDC produces a nowhere-zero `Z_5` flow;
6. orientability is itself an affine slice of a fixed gauge torsor;
7. the rainbow `S_5` holonomy preserves no affine `F_5` structure on the support set, so coefficient transport through the quotient reconfiguration loop is genuinely obstructed.

No claim is made that this proves the Four Colour Theorem, Tutte's 5-flow conjecture, or the five-cycle double cover conjecture.

## 2. Four terminals form the affine plane `AG(2,2)`

Identify the four labelled terminals with the four points of

\[
A=F_2^2.
\]

For each nonzero direction

\[
a\in F_2^2\setminus\{0\},
\]

the involution

\[
x\longmapsto x+a
\]

partitions `A` into two pairs. These are the two affine lines parallel to `a`, hence one perfect matching of the four terminals.

### Theorem 2.1 — terminal-direction correspondence

The three perfect matchings of four terminals are exactly the three parallel classes

\[
M_a=\{\{x,x+a\}:x\in F_2^2\}/\text{duplication},
\qquad
0\ne a\in F_2^2.
\]

The full affine group satisfies

\[
AGL(2,2)\cong S_4
\]

on the four terminal points. Its induced action on the three directions is

\[
GL(2,2)\cong S_3,
\]

and the kernel is the translation group

\[
F_2^2\cong V_4.
\]

#### Proof

Every nonzero vector of `F_2^2` has order two and gives two disjoint translation pairs. The three nonzero vectors give the three perfect matchings.

There are `|F_2^2| |GL(2,2)| = 4\cdot 6=24` affine transformations, acting faithfully on four points, hence the point action is `S_4`. Translations fix directions, and the quotient action is the natural faithful action of `GL(2,2)` on the three nonzero vectors. ∎

Thus the earlier matching-index `S_3` is not a convenient symmetry imposed after classification. It is the projective direction action of the four-point affine plane.

## 3. Tait colouring as the rank-two residue of a Fano flow

Let `G` be cubic and let

\[
f:E(G)\to F_2^r\setminus\{0\}
\]

be a nowhere-zero binary flow.

At a cubic vertex with incident edges `e_1,e_2,e_3`, Kirchhoff's law is

\[
f(e_1)+f(e_2)+f(e_3)=0.
\]

### Proposition 3.1 — rank two

For `r=2`, the three incident values are the three distinct nonzero elements of `F_2^2`.

Hence a nowhere-zero `F_2^2` flow on a cubic graph is exactly a proper three-edge-colouring, and conversely.

#### Proof

There are only three nonzero vectors. No two incident values can agree, since then the third would be zero. Their sum is zero, so all three occur. ∎

This is the standard Tait-flow correspondence.

### Proposition 3.2 — rank three line field

For `r=3`, the three incident values form one projective line of the Fano plane

\[
PG(2,2).
\]

Thus every nowhere-zero Fano flow determines a vertex line field

\[
\ell_f:V(G)\to\mathcal L,
\]

where `\mathcal L` is the set of seven Fano lines.

Moreover the following are equivalent:

1. `f(E(G))` is contained in one two-dimensional subspace `U\le F_2^3`;
2. `\ell_f` is constant with value `U\setminus\{0\}`;
3. `f` is a nowhere-zero `F_2^2` flow after identifying `U\cong F_2^2`;
4. `G` has the corresponding Tait three-edge-colouring.

#### Proof

A zero-sum triple of distinct nonzero vectors in `F_2^3` is exactly

\[
\{a,b,a+b\},
\]

the nonzero point set of a two-dimensional subspace. If all vertex lines equal `U\setminus\{0\}`, connectedness places every edge value in `U`. The converse implications are immediate. ∎

Therefore

\[
\boxed{
\text{Tait colouring}
=
\text{constant Fano line field}.
}
\]

For a bridgeless planar cubic graph, the Tait form of the Four Colour Theorem is exactly the assertion that at least one nowhere-zero Fano flow has constant line field.

This is an exact reformulation, not a new proof.

## 4. Cycle switches are Fano-line pivots

Let `C` be a cycle and let `h\in F_2^3\setminus\{0\}`. The standard binary cycle switch replaces

\[
f(e)\longmapsto f(e)+h
\qquad(e\in C),
\]

and leaves all other edges fixed, provided no switched edge has value `h`.

At a cycle vertex write the two cycle-edge values as `a,b` and the off-cycle value as

\[
c=a+b.
\]

The old Fano line is

\[
L=\{a,b,c\}.
\]

After switching, the new line is

\[
L'=\{a+h,b+h,c\}.
\]

### Theorem 4.1 — local pivot law

There are two cases.

1. If `h=c`, then
   \[
   a+h=b,\qquad b+h=a,
   \]
   so `L'=L`. The switch merely exchanges the two cycle colours inside one rank-two palette.

2. If `h\notin L`, then `L'\ne L` and
   \[
   L\cap L'=\{c\}.
   \]
   Thus the vertex line pivots to another Fano line through the unchanged off-cycle point `c`.

For fixed `L` and `c\in L`, the proper switches reach exactly the other two Fano lines through `c`.

#### Proof

The first case is immediate. In the second, `c` belongs to both lines. If another old point belonged to `L'`, one of the switched values would force `h` into `L`, contrary to assumption. The Fano plane has exactly three lines through `c`, and the admissible outside values realize the other two. ∎

Hence ordinary Tait Kempe switching is precisely the line-preserving residue of the general Fano cycle-switch dynamics.

A possible Four-Colour mechanism programme is therefore:

\[
\boxed{
\text{start with an arbitrary Fano flow}
\longrightarrow
\text{flatten its line field by admissible pivots}
\longrightarrow
\text{constant line / Tait colouring}.
}
\]

Planarity has not yet been converted into a monotone flattening theorem. Any such theorem would be a genuinely new proof architecture, not a consequence of the present finite classifications alone.

## 5. Five-support CDCs are root-valued binary flows

Let

\[
\mathcal F=(F_1,\ldots,F_5)
\]

be an indexed five-support cycle double cover of a graph `G`: every `F_i` is even and every edge belongs to exactly two supports.

Define

\[
E_5=
\left\{
 x\in F_2^5:
 \sum_{i=1}^5x_i=0
\right\}.
\]

This is a four-dimensional binary vector space. Let

\[
R_5=\{e_i+e_j:1\le i<j\le5\}
\subset E_5
\]

be the ten weight-two roots.

For an edge belonging to supports `F_i,F_j`, set

\[
\lambda(e)=e_i+e_j.
\]

### Theorem 5.1 — root-flow equivalence

Indexed five-support cycle double covers of `G` are equivalent to nowhere-zero `E_5`-flows

\[
\lambda:E(G)\to R_5
\]

whose values are restricted to the ten roots.

#### Proof

For every vertex and coordinate `i`, the sum of the incident `i`-coordinates equals the degree of `F_i` at that vertex modulo two, hence is zero. Thus `\lambda` is a binary flow. It is nowhere zero and root-valued because every edge lies in exactly two supports.

Conversely, given a root-valued `E_5` flow, let `F_i` be the edges whose `i`-coordinate is one. Coordinatewise conservation makes every `F_i` even, and every root has exactly two nonzero coordinates. ∎

Thus the five-CDC problem sits inside flow theory as a constrained rank-raising problem:

\[
\boxed{
F_2^3\text{ nowhere-zero flow}
\longrightarrow
E_5\cong F_2^4\text{ root-valued flow}.
}
\]

The difficulty is not ordinary existence of a binary flow in a larger group. It is forcing every edge value into the ten-element root set `R_5`.

### Corollary 5.2 — local support triangle

At every cubic vertex, the three incident root labels are exactly

\[
e_i+e_j,
\qquad
e_j+e_k,
\qquad
e_k+e_i
\]

for one three-element subset `\{i,j,k\}\subset[5]`.

Equivalently, the three edge labels form one triangle in `K_5`.

#### Proof

The three roots contribute six coordinate incidences. Conservation forces each coordinate multiplicity to be even, hence exactly three coordinates occur twice. The only loopless two-regular three-edge multigraph on those three coordinates is a triangle. ∎

So a five-support CDC may be viewed as a cubic graph carrying a locally varying Tait triangle inside `K_5`.

## 6. Orientable five-support CDCs imply nowhere-zero five-flows

Call a five-support CDC **orientable** if every cycle component of every support can be oriented so that on each graph edge the two support occurrences traverse that edge in opposite directions.

Choose any bijection

\[
c:\{1,\ldots,5\}\to\mathbb Z_5.
\]

For each directed support component take its `\mathbb Z_5` circulation and weight it by `c(i)`. Sum the five weighted circulations.

### Theorem 6.1 — oriented-cover-to-flow map

An orientable five-support CDC gives a nowhere-zero `\mathbb Z_5` flow.

#### Proof

A weighted sum of directed cycles is a circulation. Suppose edge `e` belongs to supports `i,j`, traversed in opposite directions. Relative to either reference orientation, its resulting value is

\[
\pm(c(i)-c(j)).
\]

Since `c` is injective, this value is nonzero in `\mathbb Z_5`. ∎

At a cubic vertex with local support triangle `i,j,k`, the three edge values can be written, after compatible orientation, as

\[
c(j)-c(i),
\qquad
c(k)-c(j),
\qquad
c(i)-c(k),
\]

whose sum is zero by telescoping.

This is the precise Tutte bridge:

\[
\boxed{
\text{orientable five-support CDC}
\Longrightarrow
\text{nowhere-zero }5\text{-flow}.
}
\]

It is a sufficient route, not an asserted equivalence.

## 7. Orientability is an affine gauge slice

Fix a Fano flow `f`, a compatible root lift `g`, and its reduced gauge code

\[
B_f\subseteq F_2^{E(G)}.
\]

Represent the cycle-face embedding `S_g` by a signed rotation system. After choosing orientations of the vertex discs, let

\[
s_g\in F_2^{E(G)}
\]

record which edge bands are twisted.

Reversing the orientation of a set of vertex discs toggles the signs on the corresponding cut. Therefore the surface is orientable exactly when

\[
s_g\in\operatorname{Cut}(G).
\]

A partial Petrial gauge word `k\in B_f` toggles precisely the edge signs in its support, so

\[
s_{g^k}=s_g+k.
\]

### Theorem 7.1 — orientable gauge locus

The orientable states in the fixed-flow gauge torsor are

\[
\boxed{
\operatorname{Ori}_f(g)
=
B_f\cap\bigl(s_g+\operatorname{Cut}(G)\bigr).
}
\]

This set is either empty or one affine coset whose direction space is

\[
\boxed{
B_f\cap\operatorname{Cut}(G).
}
\]

#### Proof

A state `g^k` is orientable exactly when `s_g+k` differs from zero by vertex-disc reversals, equivalently when `s_g+k` lies in the cut space. Intersect with the admissible gauge code. ∎

Consequently the fixed-flow sufficient condition for a nowhere-zero five-flow becomes

\[
\boxed{
\operatorname{Ori}_f(g)
\not\subseteq
\operatorname{Bad}_f,
}
\]

where `Bad_f` is the complete obstruction locus for componentwise goodness.

Since every finite marked obstruction library gives an affine-coset arrangement, the Tutte-oriented problem is the same arrangement problem restricted to one affine slice.

This is structurally compatible with the existing renewal framework.

## 8. Support-label structure group and rainbow holonomy

The five support names carry a natural `S_5` action. To transport `\mathbb Z_5` coefficient data canonically through a reconfiguration groupoid, one must choose an affine-line structure on the five-element set.

Two coefficient bijections

\[
c,c':[5]\to F_5
\]

are equivalent for flow extraction when

\[
c'=ac+b,
\qquad
a\in F_5^\times,\ b\in F_5,
\]

because translation cancels in differences and multiplication rescales the flow.

The stabilizer of one affine structure is

\[
AGL(1,5),
\qquad
|AGL(1,5)|=20.
\]

Hence a naked five-element support set has exactly

\[
\boxed{
|S_5|/|AGL(1,5)|=120/20=6
}
\]

affine `F_5` structures.

### Computational Theorem 8.1 — boundary holonomy has no affine reduction

For the canonical rainbow routing triangle, the sixteen boundary support-index monodromies:

- have cycle types
  \[
  2+2,
  \quad4,
  \quad3+2,
  \quad5,
  \]
  four of each;
- generate the full group `S_5`;
- preserve none of the six affine `F_5` structures.

Moreover a permutation of cycle type `3+2` lies in no conjugate of `AGL(1,5)`, so four of the sixteen monodromies individually destroy every affine-line structure.

#### Proof status

Exact finite group computation, reproduced by the Wolfram verifier on the private notebook branch. ∎

This does **not** obstruct extracting a five-flow from one final orientable five-support cover: one may label that final support set arbitrarily by `F_5`.

It obstructs a stronger mechanism in which one fixed affine coefficient structure is transported consistently around the quotient reconfiguration loop. Thus the rainbow triangle is simultaneously:

- a routing holonomy obstruction in the five-CDC programme;
- a structure-group obstruction in any reconfiguration-compatible Tutte-flow extraction.

## 9. Evaluation of the Four Colour connection

The relation is exact at the local and rank-two levels:

\[
\text{three terminal matchings}
=
\text{three directions of }AG(2,2)
=
F_2^2\setminus\{0\},
\]

and

\[
\text{Tait colouring}
=
\text{constant Fano line field}.
\]

The current framework therefore offers a potentially useful mechanism language for the Four Colour Theorem:

- an always-available higher-rank binary flow;
- a Fano line field;
- local line pivots under cycle switches;
- a target constant section.

What is missing is precisely the planar global theorem:

\[
\boxed{
\text{planarity forces existence of a constant-line Fano flow}
}
\]

or the stronger constructive statement that an arbitrary Fano flow can be flattened through nowhere-zero cycle switches.

No monotone planar energy, reducible-configuration theorem, or terminating pivot algorithm is currently known in this framework. Therefore the framework gives a new exact reformulation and a plausible research route, not yet a mechanistic proof of the Four Colour Theorem.

## 10. Evaluation of the Tutte-flow connection

The connection is stronger than analogy.

1. By Tutte's group-order theorem, choosing `F_2^3` as the coefficient group is a geometric realization of ordinary nowhere-zero `8`-flow theory.
2. The AffineCDC root-lift problem asks for a special root-valued flow in `E_5\cong F_2^4`.
3. If a good root lift is orientable, the resulting five-support cover gives a nowhere-zero `Z_5` flow.
4. Orientability is an affine subspace condition over the same gauge code used by the obstruction arrangement.

Thus one can define the oriented-good locus

\[
\operatorname{Good}^{\mathrm{or}}_f
=
\operatorname{Good}_f\cap\operatorname{Ori}_f.
\]

A sufficient AffineCDC route to Tutte's conjecture is:

\[
\boxed{
\forall G\text{ bridgeless cubic},
\quad
\exists f:
\operatorname{Good}^{\mathrm{or}}_f\ne\varnothing.
}
\]

This route is stronger than merely producing a `5`-flow and may therefore be harder than Tutte's conjecture itself. Its value is that it places the additional orientability demand inside the already developed affine/gauge machinery rather than introducing an unrelated problem.

## 11. New global mechanism map

The combined picture is

\[
\boxed{
\begin{array}{c}
\text{ordinary 8-flow / }F_2^3\text{ flow}\\
\downarrow\\
\text{Fano line field and cycle-pivot dynamics}\\
\downarrow\\
\text{root-valued }E_5\text{ flow / five-support CDC}\\
\downarrow\\
\text{orientable affine gauge slice}\\
\downarrow\\
\mathbb Z_5\text{ nowhere-zero flow}.
\end{array}
}
\]

The two central unresolved global operations are now clear:

1. **rank reduction / flattening**
   \[
   F_2^3\to F_2^2,
   \]
   relevant to Tait colouring and the Four Colour Theorem;

2. **orientation reduction**
   \[
   S_5\text{-symmetric root cover}
   \to
   \text{orientable cover with coherent }F_5\text{ coefficients},
   \]
   relevant to Tutte's five-flow conjecture.

Both are reductions of structure, not additional finite case lists.

## 12. Exact next targets

### 12.1 Planar Fano flattening probe

For a Fano flow define, for example,

\[
D(f)=|\{uv\in E(G):\ell_f(u)\ne\ell_f(v)\}|
\]

and the number of used Fano lines. Determine the exact effect of admissible cycle pivots. Search for a planar surgery that strictly reduces a lexicographic line-field complexity.

This is a bounded conceptual probe, not yet a main proof claim.

### 12.2 Orientability-gauge law in the current laboratories

For every Petersen and flower-snark fibre compute:

- whether `Ori_f` is empty;
- `\dim(B_f\cap\operatorname{Cut}(G))`;
- whether the obstruction arrangement covers `Ori_f`;
- horizontal distance from a flow with no orientable good state to one with such a state.

### 12.3 Tree/holonomy refinement

For tree routing, test whether the unique linkage automaton forces a lower separator.

For rainbow holonomy, lift the `S_5` boundary action simultaneously to:

- the interior gauge code;
- the six affine `F_5` structures;
- the orientability coset.

The desired theorem is either orbit escape from the mismatch kernel or a strict decomposition.

### 12.4 Literature positioning

Compare this structure-group language with:

- the Tait-flow form of the Four Colour Theorem;
- Tutte's group-order theorem;
- Jaeger's 8-flow theorem and Seymour's 6-flow theorem;
- oriented cycle-double-cover implications for five-flows;
- existing 4-flow and Catlin-reduction approaches to five-cycle double covers.

## 13. Trust boundary

The following are theorem-level:

- the `AG(2,2)` matching correspondence;
- Tait colourings as rank-two binary flows;
- Fano line fields and the local pivot law;
- root-valued `E_5` flow equivalence;
- the local support-triangle theorem;
- orientable five-support CDC implies a nowhere-zero `Z_5` flow;
- orientability as an affine gauge slice.

The six affine structures and rainbow-holonomy statements are exact finite computation.

The following remain programme-level:

- planar line-field flattening;
- existence of orientable good lifts for all bridgeless cubic graphs;
- using the holonomy action to prove orbit escape;
- any new proof of the Four Colour Theorem, Tutte's 5-flow conjecture, or the five-cycle double cover conjecture.
