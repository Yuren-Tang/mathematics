# Renewal skeletons, reserve-shortened gauge codes, and the residual-neighbour census

**Programme:** `AffineCDC — Research Lead`  
**Status:** theorem-level structural deductions plus exact finite computational evidence; not canonical pending Director review and literature audit  
**Parents:** `FIVE_CDC_FACE_TRANSITION_OBSTRUCTION_ARRANGEMENT_V1.md`, `FIVE_CDC_ESSENTIAL_RENEWAL_QUOTIENT_V1.md`, `FIVE_CDC_K6_ESCAPE_OR_FROZEN_CYCLE_CERTIFICATE_V1.md`, `FIVE_CDC_COMPONENTWISE_DUAL_CENSUS_V1.md`

## 1. Purpose

For a fixed nowhere-zero Fano flow, the reduced gauge code parametrizes a finite partial-Petrial orbit of cycle-face embeddings. Every marked certified obstruction core occurs on an affine subspace of that gauge torsor.

The preceding packets reduced persistent fixed-flow failure to a finite affine-cover problem on the essential renewal quotient. This packet adds two further layers.

1. It identifies the direction space of one marked core with a shortened gauge code on the source edges outside that core's face zone.
2. It computes the complete renewal-cover type for all `360` connected-cycle neighbours whose whole reduced fibre remains componentwise bad.

The resulting mechanism is much more rigid than an arbitrary affine-subspace cover. Every residual fibre has essential renewal dimension at most three. Apart from twelve two-dimensional line-persistence examples, every nontrivial fibre is a point-renewal system: every old `K_6` is individually destructible, but each gauge state generates private replacement cliques.

## 2. The reserve-shortened code

Fix a gauge state `\beta` and a marked obstruction core `C` in its dual triangulation. Let

\[
Z_C\subseteq E(G)
\]

be the union of the source edges traversed by the marked face circuits of `C`. Put

\[
R_C:=E(G)\setminus Z_C.
\]

Call `R_C` the **reserve** of the marked core.

The marked-face stabilizer theorem gives the occurrence direction

\[
L_C
=
\{\lambda\in B_f:\lambda|_{Z_C}=0\}.
\]

### Theorem 2.1 — shortened-reserve formula

For every marked core `C`,

\[
\boxed{
L_C
=
B_f\cap \mathbf F_2^{R_C}.
}
\]

Here `\mathbf F_2^{R_C}` denotes the coordinate subspace of edge words supported inside `R_C`.

Hence

\[
\boxed{
\dim A_C
=
\dim\bigl(B_f\cap\mathbf F_2^{R_C}\bigr),
}
\]

where `A_C=\beta+L_C` is the affine occurrence locus.

#### Proof

A gauge word belongs to `L_C` exactly when it vanishes on every edge in `Z_C`. This is equivalent to its support being contained in the complementary edge set `R_C`. Intersecting with `B_f` gives the displayed formula. ∎

Thus core persistence is controlled by the shortened gauge code on the reserve, not by the full gauge code in isolation.

### Corollary 2.2 — distance criterion for a private core

Let

\[
d(B_f)
:=
\min\{\operatorname{wt}(\lambda):0\ne\lambda\in B_f\}.
\]

If

\[
|R_C|<d(B_f),
\]

then

\[
L_C=0,
\]

so `C` occurs at exactly one gauge state.

The inequality is sufficient, not necessary. A larger reserve may still fail to contain the support of any nonzero gauge word.

### Interpretation

- `L_C=0`: the core is **private** to one state;
- `\dim L_C=1`: the core persists along one affine line;
- `L_C=B_f`: the core is pointwise rigid throughout the whole gauge fibre.

A positive-dimensional occurrence locus therefore means that a genuine harmonic cut quotient can be supported entirely in the part of the source graph not touched by the marked obstruction faces.

## 3. The renewal skeleton

Let

\[
Q_f=B_f/L_{\mathrm{com}}
\]

be the essential renewal quotient for a chosen marked obstruction library, and let

\[
\overline A_C\subseteq Q_f
\]

be the descended occurrence loci.

Define the **renewal incidence graph** `\mathcal R_f` to be the bipartite graph whose two vertex classes are:

- the essential gauge states `q\in Q_f`;
- the marked obstruction cores `C`;

with

\[
q\sim C
\iff
q\in\overline A_C.
\]

This graph records which obstruction is active at each essential state, after all common invisible gauge directions have been removed.

### Proposition 3.1 — point-renewal skeleton

Assume every nonempty descended occurrence locus is a singleton. Then every marked core has one private essential state, and `\mathcal R_f` is a state-indexed family of private cores.

After choosing a basis of `Q_f\cong\mathbf F_2^d`, the state side carries the standard `d`-cube Cayley graph. Gauge moves along basis directions destroy every core at the old vertex and replace it with cores attached to the new vertex.

If there is exactly one marked core at each state, the state-core incidence is a canonical bijection and the obstruction dynamics is a literal **renewal cube**.

This proposition is a reformulation of singleton affine loci. It does not assert that every gauge fibre has point renewal.

## 4. Complete residual-neighbour census

The componentwise census found `360` connected-cycle neighbours of the thirty-vertex fixed-Fano certificate whose entire reduced root-lift fibre remains bad. Their fibre sizes were

\[
1,2,4,8
\]

with multiplicities

\[
92,216,47,5.
\]

For each of these fibres the new computation constructs every marked dual `K_6`, its face zone, its affine occurrence locus, the common lineality, the essential renewal quotient, and a minimal irredundant cover.

### Theorem-level computational result 4.1

For all `360` residual fibres,

\[
\boxed{
d_{\mathrm{ren}}=\dim B_f.
}
\]

Thus the common lineality is trivial in every example: no nonzero gauge direction is invisible to all active marked `K_6` cores.

The complete mechanism distribution is

\[
\begin{array}{c|c|c}
\dim B_f=d_{\mathrm{ren}}&\text{renewal cover type}&\text{fibres}\\
\hline
0&\text{rigid one-state system}&92\\
1&\text{two singleton points}&216\\
2&\text{four singleton points}&35\\
2&\text{one affine line plus two complementary points}&12\\
3&\text{eight singleton points}&5
\end{array}
\]

The counts sum to

\[
92+216+35+12+5=360.
\]

No other two-dimensional irredundant cover type occurs. In particular, the census contains no parallel-pair cover, no two-nonparallel-lines-plus-point cover, and no three-concurrent-lines cover.

### Consequence 4.2 — renewal dominates rigidity

The `92` zero-dimensional fibres have no nontrivial gauge move. Among the remaining

\[
360-92=268
\]

fibres, no marked `K_6` is rigid throughout the whole fibre. Every individual clique can be destroyed by some admissible partial Petrial.

Nevertheless all `268` fibres remain wholly bad because replacement cliques cover the other states.

Among these nontrivial fibres,

\[
216+35+5=256
\]

are pure point-renewal systems. Only twelve have any positive-dimensional marked occurrence locus.

The numerical equality `256=2^8` is recorded only as a census count; no structural significance is claimed.

## 5. One-dimensional renewal: harmonic quotient types

Every one-dimensional residual fibre has exactly two essential states and one nonzero gauge word. The unique word destroys every marked clique in one state and the other state supplies replacements.

The harmonic cut quotient of that word has the following exact distribution:

\[
\begin{array}{c|c|c}
\text{weight}&\text{harmonic quotient type}&\text{fibres}\\
\hline
4&4K_2&22\\
6&2K_3&130\\
6&K_4&14\\
8&2C_4&46\\
18&\text{larger nine-vertex quotient}&4
\end{array}
\]

Here `2C_4` is the four-cycle with every edge doubled. The first four rows account for

\[
212/216
\]

of the two-point renewal systems.

Thus almost every one-dimensional replacement is driven by a small harmonic quotient already visible in the low-weight gauge programme, together with one natural weight-eight extension.

## 6. The twelve line-persistence fibres

Exactly twelve two-dimensional fibres have descended arrangement

\[
\boxed{
\text{one affine line plus the two points of its complementary line}.
}
\]

Relative to the fixed Fano-coordinate labelling of the certificate, all twelve arise from switches in direction `3`. This direction label is coordinate-dependent and is not asserted to be intrinsic.

Every such fibre has statewise clique counts

\[
(7,7,2,2).
\]

The two states on the affine line carry marked cliques that persist between them. For every positive-dimensional marked-clique appearance:

- the reserve has exactly eight source edges;
- the shortened reserve code is one-dimensional;
- its nonzero word has weight six;
- the harmonic cut quotient of that word is `K_4`.

Hence the sole observed mechanism for partial clique persistence is

\[
\boxed{
\text{an eight-edge reserve containing a weight-six }K_4
\text{ harmonic circuit}.
}
\]

This is not an arbitrary affine line. It is a concrete low-weight gauge mode living entirely outside the six marked faces.

## 7. The five three-dimensional renewal cubes

Exactly five residual fibres have

\[
B_f\cong\mathbf F_2^3.
\]

Relative to the fixed certificate labelling, all five arise from switches in direction `7`.

For every one of the five fibres:

1. there are eight gauge states;
2. every state contains exactly one marked `K_6`;
3. every marked core occurs at exactly one state;
4. the eight states and eight marked cliques are therefore canonically paired;
5. the renewal skeleton is the three-dimensional cube.

The seven nonzero gauge-word weights are

\[
\boxed{
6,12,14,18,24,24,26.
}
\]

The unique minimum-weight word has harmonic quotient type

\[
2K_3.
\]

Across the forty state-core pairs in the five fibres, the reserve sizes are

\[
\begin{array}{c|c}
|R_C|&\text{occurrences}\\
\hline
1&25\\
3&15
\end{array}
\]

Since

\[
d(B_f)=6,
\]

Corollary 2.2 forces every clique to be private:

\[
|R_C|\le3<6=d(B_f).
\]

The renewal cube is therefore a **large-zone / code-distance phenomenon**. Every `K_6` touches all but one or three source edges, so no nonzero gauge word can avoid it. A move necessarily destroys the old clique, but another almost-global clique appears at the new cube vertex.

## 8. Mechanism map

The present fixed-flow mechanism can now be separated into four layers.

### Layer A — surface and half-cube target

A root lift gives a cycle-face embedding and a dual triangulation. The actual five-support target is

\[
T_g\longrightarrow\mathscr A_5.
\]

This componentwise freedom removes many false obstructions produced by the old eight-colour quotient.

### Layer B — local Petrial exposure

A gauge word changes face-side matchings. Exposure rank determines whether one marked clique survives. This completely solves the local question for a fixed marked core.

### Layer C — reserve-shortened harmonic code

The occurrence direction is the shortened code

\[
B_f\cap\mathbf F_2^{R_C}.
\]

This identifies the precise source-side resource needed for persistence. Small reserves force private cores; special low-weight harmonic quotients create affine-line persistence.

### Layer D — global renewal cover

Even when every marked clique is locally destructible, the complete family of private or partially persistent cores may cover the entire gauge fibre. This is the surviving fixed-flow obstruction.

In the present neighbourhood this global layer is low-dimensional and highly discrete:

- no essential dimension exceeds three;
- every nontrivial core is destructible;
- `256/268` nontrivial residual fibres are pure point renewal;
- the only positive-dimensional persistence is the weight-six `K_4` reserve mechanism;
- the highest-dimensional examples are five canonical renewal cubes driven at minimum weight by `2K_3`.

## 9. What the evidence supports

The census supports the following working picture.

1. **The main obstruction is no longer local rigidity.** In nontrivial fibres, old cliques are destroyed readily.
2. **The obstruction is organized replacement.** Gauge moves transport the system between private, almost-global clique cores.
3. **Low-weight harmonic quotients drive the transport.** The canonical `4K_2`, `2K_3`, and `K_4` circuits, together with `2C_4`, account for nearly all one-dimensional renewals.
4. **Large face zones explain privacy.** In the renewal cubes the complement of a clique zone is too small to support any codeword.
5. **The essential quotient does not shrink these residual examples.** Every gauge direction is detected by some active obstruction core.

These are exact statements for the displayed finite neighbourhood, not universal theorems about all compatible dual triangulations.

## 10. Refined obstruction and next targets

The remaining mechanism is:

\[
\boxed{
\text{small harmonic quotient}
\longrightarrow
\text{destroy old almost-global }K_6
\longrightarrow
\text{create new almost-global }K_6.
}
\]

The next theorem-level targets are therefore:

### 10.1 Reserve-interface theorem

Classify how a weight-six `K_4` harmonic circuit can lie inside an eight-edge reserve of a dual `K_6`. Determine whether the resulting interface forces a bounded topological decomposition or a gluing configuration.

### 10.2 Renewal-cube classification

Classify the five three-dimensional renewal cubes up to source-graph, gauge-code, and face-transition equivalence. The common features to explain are:

- minimum circuit `2K_3`;
- weight spectrum `6,12,14,18,24,24,26`;
- exactly one clique per gauge state;
- reserve sizes one or three;
- complete state-core bijection.

### 10.3 Horizontal transport of renewal skeletons

A connected-cycle switch changes the Fano flow and therefore changes both the gauge code and the reserve-shortened subcodes. Derive an update rule for the renewal incidence graph under one horizontal switch.

The desired dichotomy is:

\[
\boxed{
\text{a horizontal move produces an uncovered essential state}
\quad\text{or}\quad
\text{persistent renewal skeletons force a gluable decomposition}.
}
\]

### 10.4 Deeper obstruction library

The present neighbourhood has no `K_6`-free componentwise-bad lift. General graph-homomorphism theory does have deeper obstructions, so later work must enlarge the marked-core library if compatible `K_6`-free examples are found.

## 11. Trust boundary

The census is exact finite computation, reproduced by dependency-free scripts in the private research workbench. The shortened-reserve formula and renewal-skeleton deductions are elementary theorems.

No statement here proves that every gauge fibre has an uncovered state, that every `K_6`-free compatible dual maps to `\mathscr A_5`, that every renewal cube can be broken by one horizontal switch, or that every cubic graph has a five-support cycle double cover.
