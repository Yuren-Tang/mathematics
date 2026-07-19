# Orientation transgression and coefficient holonomy

**Programme:** `AffineCDC — Research Lead`  
**Status:** theorem-level cohomological and group-theoretic mechanism plus exact finite holonomy classification; not canonical pending Director review and literature audit  
**Parents:** `FIVE_CDC_TAIT_FANO_TUTTE_BRIDGE_V1.md`, `FIVE_CDC_ROUTING_WEIGHT_HOLONOMY_V1.md`, `FIVE_CDC_MIXED_CORE_AFFINE_ARRANGEMENT_V1.md`

## 1. Purpose

The previous bridge packet identified two extra structures needed to extract a nowhere-zero five-flow from the five-support programme:

1. an orientable cycle-face state in the fixed Fano-flow gauge fibre;
2. an affine `F_5` structure on the five support names.

This packet replaces both apparent side conditions by intrinsic obstruction mechanisms.

- Orientability is controlled by one linear transgression
  \[
  \theta_f:B_f\longrightarrow H^1(G;F_2).
  \]
  Every fixed-flow fibre has a canonical orientation-obstruction class in `coker(theta_f)`.

- An affine `F_5` structure on a naked five-element support set is the same thing as a Sylow `5`-subgroup of `S_5`. The six coefficient structures therefore form one faithful two-transitive `S_5`-set.

- A reconfiguration component admits globally consistent coefficient transport exactly when its support-label holonomy group is contained in a conjugate of `AGL(1,5)`.

- The canonical rainbow routing triangle has full `S_5` holonomy. It therefore admits no such reduction. Its `(3,2)` monodromies act as six-cycles on the coefficient structures.

The result is a sharper mechanism map:

\[
\boxed{
\text{five-flow extraction}
=
\text{vanishing orientation transgression}
+
\text{endpoint coefficient choice},
}
\]

while any proof that attempts to transport one fixed coefficient structure through a reconfiguration loop must additionally solve a genuine structure-group reduction problem.

No statement here proves Tutte's five-flow conjecture, the five-cycle double cover conjecture, or the Four Colour Theorem.

## 2. Signed rotation systems and the orientation class

Let `G` be connected. Write

\[
C^0(G)=F_2^{V(G)},
\qquad
C^1(G)=F_2^{E(G)}.
\]

The coboundary map

\[
\delta:C^0(G)\longrightarrow C^1(G)
\]

has image the binary cut space

\[
B^1(G)=\operatorname{Cut}(G).
\]

For a cycle-face embedding `S_g`, choose local orientations of all vertex discs. Let

\[
s_g\in C^1(G)
\]

record which edge bands reverse those local orientations.

Changing the orientation of a vertex disc toggles all incident edge signs. Therefore changing all chosen vertex-disc orientations replaces `s_g` by

\[
s_g+\delta x
\]

for some `x\in C^0(G)`.

Hence the quotient class

\[
\boxed{
 w_1(g):=[s_g]
 \in
 H^1(G;F_2)
 :=C^1(G)/B^1(G)
}
\]

is independent of all local orientation choices.

### Proposition 2.1 — orientability criterion

The cycle-face surface `S_g` is orientable if and only if

\[
\boxed{w_1(g)=0.}
\]

#### Proof

A global surface orientation exists exactly when the vertex-disc orientations can be chosen so that every edge band preserves the induced orientations. Equivalently, the sign vector can be killed by vertex-disc reversals, so `s_g\in B^1(G)`. This is exactly `[s_g]=0`. ∎

The class `w_1(g)` is the orientation character of the signed graph spine and agrees with the first Stiefel--Whitney obstruction of the surface.

## 3. Gauge words act linearly on orientation classes

Fix a nowhere-zero Fano flow `f` and one compatible root lift `g`. Let

\[
B_f\subseteq C^1(G)
\]

be the reduced gauge code, represented as edge words.

A gauge word `k\in B_f` performs the partial Petrial on the edges of `k`, hence toggles precisely those edge-band signs:

\[
s_{g^k}=s_g+k.
\]

Passing to cohomology gives

\[
w_1(g^k)=w_1(g)+[k].
\]

Define the **orientation transgression**

\[
\boxed{
\theta_f:B_f\longrightarrow H^1(G;F_2),
\qquad
\theta_f(k)=[k].
}
\]

This is the restriction to `B_f` of the quotient map `C^1(G) -> C^1(G)/B^1(G)`.

### Theorem 3.1 — intrinsic orientation obstruction

The class

\[
\boxed{
\mathfrak o_f
:=
 w_1(g)+\operatorname{im}\theta_f
 \in
 \operatorname{coker}\theta_f
}
\]

is independent of the chosen base root lift `g` in the fixed-flow gauge fibre.

Moreover the following are equivalent:

1. the fibre contains an orientable state;
2. `w_1(g)\in\operatorname{im}\theta_f`;
3. `\mathfrak o_f=0`.

#### Proof

Changing the base lift from `g` to `g^k` changes `w_1(g)` by `\theta_f(k)`, so its class modulo `im(theta_f)` is unchanged.

A state `g^k` is orientable exactly when

\[
0=w_1(g^k)=w_1(g)+\theta_f(k),
\]

which is solvable exactly when `w_1(g)` lies in the image. ∎

Thus orientability of a fixed flow fibre is not a state-by-state topological mystery. It is the vanishing of one canonical class in a finite binary quotient.

### Corollary 3.2 — orientable slice and exact size

If `\mathfrak o_f\ne0`, the fibre contains no orientable state.

If `\mathfrak o_f=0` and `k_0` is one solution of

\[
\theta_f(k_0)=w_1(g),
\]

then the complete orientable locus is

\[
\boxed{
\operatorname{Ori}_f(g)
=
 k_0+\ker\theta_f
=
B_f\cap\bigl(s_g+\operatorname{Cut}(G)\bigr).
}
\]

Its direction and cardinality are

\[
\ker\theta_f
=
B_f\cap\operatorname{Cut}(G),
\]

\[
\boxed{
|\operatorname{Ori}_f(g)|
=
2^{\dim B_f-\operatorname{rank}\theta_f}.
}
\]

Hence every nonempty orientable slice has power-of-two size and can be found by one linear solve.

## 4. Relation to the obstruction arrangement

For every finite marked obstruction certificate `C`, its occurrence locus in the gauge torsor is an affine coset

\[
A_C
=
\beta_C+
\bigl(B_f\cap F_2^{R_C}\bigr).
\]

The fixed-flow sufficient condition for a nowhere-zero five-flow is therefore

\[
\boxed{
\operatorname{Ori}_f(g)
\not\subseteq
\bigcup_C A_C.
}
\]

Both sides now have affine descriptions:

- `Ori_f(g)` is one fibre of the orientation transgression;
- every marked bad certificate gives one affine occurrence coset.

Thus the Tutte-oriented problem is an affine covering problem inside the same gauge code, not a separate topological programme.

The new exact alternatives for one fixed Fano flow are:

1. `\mathfrak o_f\ne0`: the entire gauge fibre is nonorientable;
2. `\mathfrak o_f=0`, but the orientable slice is covered by bad-certificate cosets;
3. the orientable slice contains a componentwise-good state, yielding an orientable five-support CDC and hence a nowhere-zero five-flow.

## 5. Affine `F_5` structures as Sylow subgroups

Let `X` be a naked five-element set. An affine `F_5` structure on `X` means a choice of bijection

\[
c:X\longrightarrow F_5
\]

modulo postcomposition by

\[
x\longmapsto ax+b,
\qquad
 a\in F_5^\times,\ b\in F_5.
\]

For one such structure, the translations

\[
x\longmapsto x+b
\]

form a regular cyclic subgroup

\[
T\cong C_5
\]

of `Sym(X)\cong S_5`.

Conversely, a regular subgroup `T\cong C_5` acts simply transitively on `X`. Choosing one point as zero identifies `X` with the additive group of `F_5`; changing the zero point or additive generator changes the coordinate only by an affine transformation.

### Theorem 5.1 — coefficient structures are Sylow `5`-subgroups

Affine `F_5` structures on `X` are naturally equivalent to Sylow `5`-subgroups of `S_5`.

There are exactly

\[
\boxed{6}
\]

such structures.

The stabilizer of one structure is the normalizer of its translation group:

\[
\boxed{
N_{S_5}(C_5)
\cong
AGL(1,5),
\qquad
|AGL(1,5)|=20.
}
\]

#### Proof

The equivalence was described above. Sylow counting gives a number congruent to `1 mod 5` and dividing `24`, hence six. The normalizer acts on the regular cyclic group by its four automorphisms and contains its five translations, so it has order `20` and is the affine group. ∎

Thus the coefficient-structure space is the homogeneous `S_5`-set

\[
\boxed{
\mathscr A_5^{\mathrm{coeff}}
=
S_5/AGL(1,5),
\qquad
|\mathscr A_5^{\mathrm{coeff}}|=6.
}
\]

## 6. The exceptional six-point action

`S_5` acts on its six Sylow `5`-subgroups by conjugation.

### Computational Theorem 6.1 — faithful two-transitive action

The action

\[
S_5\curvearrowright\mathscr A_5^{\mathrm{coeff}}
\]

is faithful and two-transitive.

For an element of `S_5`, its ordinary cycle type on the five supports determines the following cycle type on the six coefficient structures:

\[
\begin{array}{c|c|c}
\text{type on five supports}
&\text{type on six structures}
&\text{fixed structures}\\
\hline
1^5&1^6&6\\
2\,1^3&2^3&0\\
3\,1^2&3^2&0\\
2^2\,1&1^2 2^2&2\\
4\,1&1^2 4&2\\
3\,2&6&0\\
5&1\,5&1.
\end{array}
\]

#### Proof status

The six Sylow subgroups and their conjugation action are generated exactly by the dependency-free Wolfram verifier. The image has order `120`, so the action is faithful. The orbit of one ordered pair of distinct structures has size `30`, hence the action is two-transitive. The table is obtained from one representative of every conjugacy class. ∎

The table has immediate structural meanings.

- A `(3,2)` support permutation acts as one six-cycle and individually traverses all coefficient structures.
- A five-cycle fixes exactly its own translation structure and cycles the other five.
- Double transpositions and four-cycles preserve exactly two coefficient structures.
- Transpositions and three-cycles preserve none.

## 7. General coefficient-holonomy reduction theorem

Let `R` be a connected reconfiguration graph or groupoid of indexed five-support states. Choose a base state. Transport of support indices along closed reconfiguration walks gives a monodromy representation

\[
\rho:\pi_1(R)\longrightarrow S_5.
\]

Let

\[
H_\rho=\operatorname{im}\rho
\]

be the support-label holonomy group.

A **globally transported affine coefficient structure** is a choice of affine `F_5` structure at every state, compatible with every support-index transport.

### Theorem 7.1 — structure-group reduction criterion

The reconfiguration component admits a globally transported affine `F_5` structure if and only if the following equivalent conditions hold:

1. `H_\rho` fixes a point of `S_5/AGL(1,5)`;
2. `H_\rho` preserves one affine `F_5` structure on the support set;
3. after conjugating support names,
   \[
   H_\rho\le AGL(1,5).
   \]

#### Proof

A compatible coefficient structure is exactly a section of the associated six-point bundle. On a connected base, such a section is determined by its value at one state and is well-defined around every loop exactly when that value is fixed by the monodromy group. A coset `xAGL(1,5)` is fixed precisely when

\[
x^{-1}H_\rho x\le AGL(1,5).
\]

∎

This theorem separates two notions.

- To extract a five-flow from one final orientable cover, choose any endpoint coefficient structure; no global reduction is required.
- To transport one fixed coefficient system through a proof by reconfiguration, the holonomy reduction criterion is mandatory.

## 8. Rainbow triangle on the six structures

For the canonical rainbow routing triangle, the sixteen possible boundary monodromies have four representatives of each ordinary `S_5` type

\[
2^2 1,
\qquad
4 1,
\qquad
3 2,
\qquad
5.
\]

Using Theorem 6.1, their induced actions on the six coefficient structures are therefore:

\[
\begin{array}{c|c|c}
\text{support type}
&\text{coefficient type}
&\text{number among sixteen}\\
\hline
2^2 1&1^2 2^2&4\\
4 1&1^2 4&4\\
3 2&6&4\\
5&1 5&4.
\end{array}
\]

### Corollary 8.1 — maximal coefficient holonomy

The rainbow monodromies generate `S_5`; hence their action on the six coefficient structures is faithful and two-transitive.

In particular:

1. no affine coefficient structure is globally preserved;
2. no proper nonempty subset of coefficient structures is invariant under the full rainbow holonomy;
3. each of the four `(3,2)` monodromies individually acts as a six-cycle.

Thus the rainbow loop is not merely incompatible with one chosen coefficient labelling. It has maximal structure-group obstruction.

## 9. Combined obstruction stack

The fixed-flow and reconfiguration mechanisms now occupy two different levels.

### State-level orientation obstruction

For one fixed Fano flow:

\[
\boxed{
\mathfrak o_f
\in
\operatorname{coker}
\bigl(B_f\to H^1(G;F_2)\bigr).
}
\]

Its vanishing is necessary and sufficient for the gauge fibre to contain an orientable state.

### Loop-level coefficient obstruction

For one connected indexed-cover reconfiguration component:

\[
\boxed{
H_\rho\le S_5.
}
\]

A globally transported coefficient structure exists exactly when `H_rho` reduces to a conjugate of `AGL(1,5)`.

These are logically independent:

- orientation is a binary cohomological obstruction inside one gauge torsor;
- coefficient transport is a nonabelian holonomy obstruction over a reconfiguration component.

A final orientable good state needs the first obstruction to vanish but does not require the second. A proof mechanism that insists on one globally fixed coefficient system must solve both.

## 10. Consequences for the main programme

### 10.1 No state enumeration is needed for orientability

Compute `theta_f` once. The entire fibre is classified by one cokernel class and, when solvable, one affine kernel fibre.

This creates a natural exact statistic for every laboratory flow:

\[
\bigl(
\dim B_f,
\operatorname{rank}\theta_f,
\mathfrak o_f
\bigr).
\]

### 10.2 Tutte-compatible escape problem

The strongest fixed-flow target becomes

\[
\boxed{
\text{find }
 k\in B_f
\text{ such that }
\theta_f(k)=w_1(g)
\text{ and }
g^k\text{ is good}.
}
\]

This is an affine slice avoiding an affine obstruction arrangement.

### 10.3 Rainbow holonomy cannot be handled by frozen coefficients

Any argument that assigns one permanent `F_5` coordinate system to supports before traversing the rainbow loop is structurally impossible. A successful proof must instead:

- choose coefficients only after reaching a final orientable cover;
- carry the full six-point coefficient local system;
- or prove that the rainbow branch decomposes or escapes before coefficient transport is needed.

### 10.4 Relation to the tree/holonomy dichotomy

The cyclic four-cut programme remains:

\[
\boxed{
\begin{cases}
\text{tree routing}&\Rightarrow\text{strict decomposition};\\
\text{rainbow holonomy}&\Rightarrow\text{interior orbit escape or decomposition}.
\end{cases}
}
\]

The new theorem says that the holonomy branch must be analysed at the level of the interior gauge/orientation code, not neutralized by a clever fixed `Z_5` relabelling.

## 11. Higher-level mechanism boundary

Several local universes are now closed:

1. four-edge boundary signatures form a ten-point coordinate geometry;
2. fixed routing preserves one cut-parity coordinate;
3. minimal abstract mismatch policies reduce to tree or rainbow holonomy;
4. orientability in a gauge fibre is one linear transgression problem;
5. coefficient structures form one two-transitive six-point `S_5`-space;
6. global coefficient transport is one subgroup-reduction problem.

The remaining global gap is not another finite classification. It is the interaction of:

\[
\boxed{
\text{interior cycle-space coherence}
+
\text{orientation transgression}
+
\text{rainbow support holonomy}.
}
\]

The next theorem should prove one of:

- a rainbow loop acts nontrivially on the interior orientation/gauge quotient and forces escape from the minimal kernel;
- persistent trivial interior action forces a smaller separator or serial four-pole decomposition;
- the orientable affine slice cannot be covered by the persistent mixed-core obstruction arrangement.

## 12. Trust boundary

The orientation-class construction, orientation transgression, intrinsic cokernel obstruction, affine-slice formula, Sylow interpretation of coefficient structures, and structure-group reduction criterion are theorem-level.

The faithful two-transitive six-point action, conjugacy-class table, and rainbow induced cycle types are exact finite computations reproduced by the private Wolfram verifier.

The proposed escape/decomposition consequences are programme targets. No result here proves existence of an orientable five-support cover for every bridgeless cubic graph, eliminates the rainbow branch, proves Tutte's five-flow conjecture, proves the five-cycle double cover conjecture, or proves the Four Colour Theorem.
