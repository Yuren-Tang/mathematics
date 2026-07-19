# Defect-core quotient and the two-level arrangement mechanism

**Programme:** `AffineCDC — Research Lead`  
**Status:** theorem-level structural checkpoint and agenda compression; not canonical pending Director review  
**Parents:** `FIVE_CDC_BAD_LIFT_CONTAINER_DYNAMICS_V1.md`, `FIVE_CDC_SUPPORT_CYCLE_PIVOT_AND_FLOW_RECONFIGURATION_V1.md`, `FIVE_CDC_ROOT_LIFT_CONTROLLABILITY_STRESS_FOURIER_V1.md`

## 1. Purpose

The five-support programme has two kinds of motion:

1. **vertical motion** inside the affine root-lift torsor above one fixed Fano flow;
2. **horizontal motion** between nowhere-zero Fano flows by rank-one cycle switches.

The vertical theory is now explicit: its fibres are affine spaces, their local evaluation defects are relative stresses, and half-cube compressibility depends only on the unused-root graph. This packet integrates out that solved direction and identifies the finite defect cores that remain visible to the horizontal dynamics.

The main conclusions are:

- a bad lift has either a two-apex defect core or one exceptional pentagon core;
- the marked two-apex static state space has exactly one hundred symmetry types;
- the exceptional pentagon is the Petersen/Clebsch odd-cycle residue of the half-cube geometry;
- all Fano flows form a tensor space, nowhere-zero flows form an arrangement complement, and cycle switches are exactly rank-one tensor moves;
- the remaining unknown is a finite-core transport problem over this base arrangement.

## 2. Sharp defect-core theorem

Let

\[
U_g:=K_8-J_g
\]

be the unused-root graph of a root lift `g`.

The exact half-cube classification and the sparse-container theorem give

\[
g\text{ noncompressible}
\iff
\tau(U_g)\le 2
\quad\text{or}\quad
U_g\subseteq C_5
\]

for some five-cycle on the eight support indices.

### Theorem 2.1 — two-apex-or-pentagon core

For every root lift `g`,

\[
\boxed{
 g\text{ is noncompressible}
 \iff
 \tau(U_g)\le 2
 \quad\text{or}\quad
 U_g\cong C_5.
}
\]

Here `C_5` means a five-cycle together with three isolated support indices.

#### Proof

Only the implication from the previous container theorem needs sharpening. If

\[
U_g\subsetneq C_5,
\]

then `U_g` is a proper subgraph of a cycle. Hence it is a forest whose components are paths, with at most four edges in total. Its maximum matching has size at most two, and for a bipartite graph König's theorem gives

\[
\tau(U_g)\le2.
\]

Thus the only pentagon-container state not already of two-cover type is the full five-cycle. The converse follows from the exact half-cube classification. ∎

Therefore the static bad locus has only two geometric species.

1. **Two-apex core.** There is a two-set `T={p,q}` meeting every unused root.
2. **Pentagon core.** The unused roots are exactly the five edges of one `C_5`.

The numbers two and five are forced by matching theory and parity: excluding an unused `3K_2` gives matching number at most two; the only non-bipartite residual graph surviving the triangle and `K_4` exclusions is the shortest remaining odd cycle, namely `C_5`.

## 3. Finite quotient of the two-apex core

Retain a chosen unordered two-vertex cover

\[
T=\{p,q\}.
\]

For each of the remaining six support indices, record its adjacency to `p` and `q` in the unused graph. There are four possible types:

\[
00,\quad 10,\quad 01,\quad 11.
\]

Let

\[
(n_{00},n_{10},n_{01},n_{11})
\]

be the four type counts, with total six, and let

\[
\varepsilon\in\{0,1\}
\]

record whether the unused edge `pq` is present.

Permuting the six bulk indices changes no count. Swapping `p` and `q` exchanges `n_{10}` and `n_{01}`.

### Theorem 3.1 — one hundred marked two-apex states

Up to permutations of the six bulk indices and interchange of the two marked apices, there are exactly

\[
\boxed{100}
\]

marked two-apex defect-core types.

#### Proof

There are

\[
\binom{6+4-1}{4-1}=\binom93=84
\]

four-part compositions of six. Including `\varepsilon` gives `168` states before swapping the apices.

A state is fixed by the apex swap exactly when

\[
n_{10}=n_{01}.
\]

Writing this common value as `r`, one has

\[
n_{00}+n_{11}+2r=6.
\]

For `r=0,1,2,3`, the numbers of solutions are respectively

\[
7,5,3,1,
\]

for a total of `16`; including `\varepsilon` gives `32` fixed states. Burnside's lemma therefore gives

\[
\frac{168+32}{2}=100.
\]

∎

The cover is part of the marked state. A graph with several two-covers may represent more than one marked state. An independent Wolfram canonical-graph computation collapses the one hundred marked presentations to eighty-eight unmarked graph isomorphism types; this finite count is retained as computational evidence rather than used in any proof.

Together with the single genuine pentagon core, the static obstruction theory is therefore finite and very small.

## 4. The Petersen meaning of the five-point core

Let `X` be the five active support indices of the exceptional pentagon. The ten roots internal to `X` are the two-subsets

\[
\binom X2.
\]

Declare two such roots adjacent when they are disjoint. This is the Kneser graph

\[
KG(5,2),
\]

the Petersen graph.

Equivalently, in the even half-cube on five coordinates, the ten weight-two vertices form a Petersen graph inside the Clebsch conflict graph: two distinct weight-two words are in conflict exactly when their supports are disjoint.

If `C` is a five-cycle on `X`, then its five edges form an induced five-cycle in this Petersen graph under disjointness. The five diagonals of `K_X` form the other five-cycle in the standard Petersen presentation.

Thus the exceptional unused `C_5` is not numerology. It is the unique odd-cycle residue in the weight-two layer of the half-cube/Clebsch geometry. Its self-complementarity on five points explains why it survives after all matching and clique templates have been excluded.

## 5. The horizontal base as an arrangement complement

Let

\[
Z_1(G):=Z_1(G;\mathbf F_2)
\]

be the binary cycle space and let

\[
\Gamma=\mathbf F_2^3.
\]

The space of all `\Gamma`-valued flows is canonically

\[
\boxed{
\operatorname{Flow}(G;\Gamma)
\cong
Z_1(G)\otimes\Gamma.
}
\]

For every source edge `e`, evaluation gives a linear map

\[
\operatorname{ev}_e:Z_1(G)\otimes\Gamma\to\Gamma.
\]

The nowhere-zero flows form the finite-field arrangement complement

\[
\boxed{
\operatorname{NZFlow}(G;\Gamma)
=
\operatorname{Flow}(G;\Gamma)
-
\bigcup_{e\in E(G)}\ker\operatorname{ev}_e.
}
\]

A rank-one cycle switch is addition by

\[
z\otimes a,
\qquad
z\in Z_1(G),\quad 0\ne a\in\Gamma.
\]

When `z` is the indicator of a connected source cycle, these are exactly the edges of the nowhere-zero flow reconfiguration graph in exponent two.

Hence the horizontal problem is itself an arrangement-complement reconfiguration problem driven by rank-one tensors.

## 6. The total two-level state space

Let

\[
\mathscr E(G)
\]

be the set of pairs `(f,g)` where `f` is a nowhere-zero Fano flow and `g` is a compatible root lift above `f`. Projection to the first coordinate gives

\[
\pi:\mathscr E(G)\to\operatorname{NZFlow}(G;\Gamma).
\]

The fibre

\[
\pi^{-1}(f)
\]

is an affine torsor under the admissible translation space `H_f^0`, modulo global support translations when reduced lifts are desired.

There are two reversible kinds of motion.

1. **Vertical gauge moves:** remain inside one fibre.
2. **Horizontal cycle switches:** move in the base; support-cycle pivots provide explicit partial lifts of some such moves to `\mathscr E(G)`.

Define the defect spectrum of one base flow by

\[
\Sigma(f):=
\{[U_g]:g\in\pi^{-1}(f)\},
\]

where brackets denote support-index isomorphism type. Then

\[
\boxed{
 f\text{ is good}
 \iff
 \Sigma(f)\text{ contains a graph outside the two-apex and pentagon cores.}
}
\]

This is the precise implementation of integrating out the solved vertical direction. One may replace the entire affine fibre by its finite defect spectrum, or merely by the Boolean good/bad value, when studying the horizontal base.

The fibre cannot be forgotten completely during a move: a horizontal switch changes the fibre dimension and its root-lift realization, and the unused-root update depends on transport data such as the released and consumed root sets

\[
R_C,
\qquad
A_{C,d}.
\]

Thus the effective quotient is a base reconfiguration graph decorated by finite defect cores and finite transport signatures.

## 7. The obstruction-witness bundle

For a bad lift `g`, define its witness set

\[
\mathcal W(g)
\]

as the union of:

- all two-sets covering `U_g`;
- the five-cycle `U_g` itself when `U_g\cong C_5`.

Then

\[
g\text{ bad}
\iff
\mathcal W(g)\ne\varnothing.
\]

A pivot or cycle switch changes `U_g`, and hence induces a finite transition relation between witness sets. If an entire connected region of the total reconfiguration space were bad, every state in it would carry at least one witness. Closed sequences of switches would then produce a finite witness-transport or monodromy problem.

This yields a sharper alternative than the previous informal descent/decomposition dichotomy.

> **Core-escape / coherent-witness alternative.** Either some horizontal and vertical sequence leaves the finite bad-core set, or the bad component supports a coherent two-apex/pentagon witness system. Such a coherent system is the candidate compact certificate from which a cut quotient, harmonic interface, or decomposition theorem should be extracted.

The missing global theorem may therefore be sought as either:

1. a proof that no coherent witness system exists on the relevant reconfiguration component; or
2. a classification showing that every coherent witness system forces a graph decomposition on which five-support covers can be glued.

## 8. Strategic consequences

The current five-support programme is no longer an unstructured search over eight supports.

- The vertical affine direction is explicit and may be integrated out.
- The horizontal base is a tensor-space arrangement complement with rank-one generators.
- The bad target has one hundred marked two-apex static types plus one genuine pentagon type.
- The pentagon type is the Petersen odd-cycle residue of the half-cube geometry.
- The remaining difficulty is the realizability and transport of these finite cores over source cycles.

This also identifies a publication-sized mathematical block independent of the unresolved 5-CDC endpoint: the root-lift compression theorem, sharp defect-core classification, fixed-flow obstruction, and reconfiguration/pivot framework form a complete structural note with an exact negative boundary and a new finite-state programme.

No statement here proves that every cubic graph has a good Fano flow or a five-support cover.