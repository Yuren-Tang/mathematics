# The universal six-dimensional renewal module

**Programme:** `AffineCDC — Research Lead`  
**Status:** exact finite computational evidence with affine-mechanism interpretation; not canonical pending Director review and literature audit  
**Parents:** `FIVE_CDC_HORIZONTAL_RENEWAL_NEIGHBOURHOOD_V1.md`, `FIVE_CDC_UNIVERSAL_RENEWAL_CUBE_TEMPLATE_V1.md`, `FIVE_CDC_RENEWAL_SKELETON_AND_RESERVE_CODE_CENSUS_V1.md`

## 1. Purpose

The complete horizontal bad-neighbour census of the five universal three-dimensional renewal cubes contains exactly two target flows with essential renewal dimension six.

A priori these could represent unrelated high-dimensional obstruction systems. Exact weighted-dual comparison shows instead that they realize the same sixty-four-state renewal module.

The result is:

\[
\boxed{
\text{the two }d_{\mathrm{ren}}=6\text{ fibres are statewise copies of one universal module.}
}
\]

The comparison is made at the level of weighted dual one-skeletons. Full surface rotation-system equivalence and equivalence of the two Fano flows are not claimed.

## 2. The two flows

Relative to the fixed ordering of the forty-five source edges in the thirty-vertex certificate, the two nowhere-zero Fano flows differ on only three edges. Their value changes are

\[
4\leftrightarrow7,
\qquad
7\leftrightarrow4,
\qquad
1\leftrightarrow2.
\]

This small Hamming separation is descriptive only. The universal-module statement below does not depend on treating these coordinate labels as intrinsic.

Each flow has reduced gauge code

\[
B_f\cong\mathbf F_2^6.
\]

Its essential renewal quotient equals the whole gauge code: the common lineality is zero.

## 3. Sixty-four weighted-dual types

For every gauge state

\[
\beta\in B_f,
\]

let `D_\beta` be the weighted dual graph of the corresponding cycle-face embedding.

### Computational Theorem 3.1

For either of the two six-dimensional fibres:

1. the sixty-four graphs `D_\beta` are pairwise nonisomorphic;
2. after using the exact gauge bases produced by the solver, corresponding states in the two fibres have isomorphic weighted dual graphs:
   \[
   D^{(1)}_\beta\cong D^{(2)}_\beta
   \qquad
   \text{for all }\beta\in\mathbf F_2^6.
   \]

Thus there are exactly sixty-four universal weighted-dual types

\[
\mathsf U_q,
\qquad q\in\mathbf F_2^6,
\]

and both flows realize the same state-to-type map.

### Verification status

Weighted graph isomorphism is checked exactly by backtracking with weighted degree and multiplicity invariants. No hash equality is used as a proof of isomorphism.

The statewise equality currently uses the gauge bases selected by the exact solver. An intrinsic coordinate system on the sixty-four types remains open.

## 4. Renewal arrangement

Every one of the sixty-four states carries at least one private marked `K_6`.

The statewise clique-count profile is:

\[
\begin{array}{c|c}
\text{marked }K_6\text{ count}&\text{states}\\
\hline
1&60\\
2&4
\end{array}
\]

The four double-clique states are

\[
\{16,17,20,21\}
\]

in the solver coordinates. They form the affine two-flat

\[
16+\langle1,4\rangle.
\]

The complete descended occurrence arrangement consists of:

- all sixty-four singleton points;
- two additional affine lines
  \[
  \{16,17\},
  \qquad
  \{20,21\}.
  \]

The two lines are parallel, both having direction `1`. Together they partition the displayed affine two-flat.

Because all sixty-four singleton points already occur, both lines are redundant in every minimal cover. They record extra persistent marked cliques rather than states that lack a private core.

## 5. The line direction

The common line direction is a gauge word `\lambda` with

\[
\operatorname{wt}(\lambda)=6.
\]

Its harmonic cut quotient is

\[
\boxed{K_4.}
\]

Thus the only positive-dimensional decoration of the universal six-cube is the same weight-six `K_4` reserve-line atom found throughout the complete horizontal bad neighbourhood.

The arrangement can therefore be written schematically as

\[
\boxed{
\text{all points of }\mathbf F_2^6
\quad+\quad
\text{two parallel }K_4\text{-reserve lines in one affine square}.
}
\]

## 6. Gauge-code weight spectrum

The sixty-three nonzero gauge words have weight distribution

\[
\begin{array}{c|r}
\text{weight}&\text{words}\\
\hline
4&1\\
6&4\\
8&4\\
10&6\\
12&9\\
14&12\\
16&9\\
18&6\\
20&8\\
22&4
\end{array}
\]

The code therefore contains several low-weight harmonic modes, including one weight-four mode and four weight-six modes. Only one of the weight-six directions supports the two persistent `K_4` reserve lines in the marked-clique arrangement.

The existence of many other low-weight modes without positive-dimensional clique persistence reinforces the reserve-shortened-code principle: persistence depends not merely on the word type but on whether its complete support fits inside a particular marked core's reserve.

## 7. Surface-size profile

The number of support-cycle faces across the sixty-four states is distributed as

\[
\begin{array}{c|r}
\text{faces}&\text{states}\\
\hline
7&4\\
8&18\\
9&25\\
10&13\\
11&3\\
12&1
\end{array}
\]

For the fixed source with thirty vertices and forty-five edges, the corresponding Euler characteristics are

\[
\chi=F-15,
\]

ranging from `-8` to `-3`.

The sixty-four weighted-dual types therefore explore a substantially larger topological range than the universal three-cube while preserving complete pointwise `K_6` renewal coverage.

## 8. Mechanism comparison with the universal three-cube

The universal three-cube has:

- eight states;
- eight private clique cores;
- one weighted-dual type per state;
- no positive-dimensional occurrence locus;
- a unique minimum `2K_3` harmonic circuit;
- intrinsic parity coordinates already known.

The universal six-cube has:

- sixty-four states;
- sixty-four private point loci;
- sixty-four weighted-dual types;
- two redundant parallel `K_4` lines;
- several low-weight harmonic modes;
- no known intrinsic six-bit coordinate formula.

Thus the six-cube is not a simple direct product of two three-cubes. Its obstruction skeleton is a complete point-renewal cube with a localized two-flat decoration.

## 9. Mechanism significance

The two highest-dimensional residual flows again fail to exhibit uncontrolled diversity.

Instead, horizontal reconfiguration has produced another reusable affine module:

\[
\boxed{
\mathbf F_2^6
\xrightarrow{
\text{one weighted-dual type per state}
}
\text{private }K_6\text{ renewal},
}
\]

with a single line atom repeated twice in parallel.

This strengthens the current working picture:

1. persistent componentwise failure is organized by finite affine modules;
2. the principal bulk is point renewal;
3. positive-dimensional persistence is a sparse `K_4` line decoration;
4. different Fano flows can realize the same renewal module.

## 10. Existing mechanism and unresolved layer

### Explained

- why the arrangement covers all states: every state has a private point core;
- why the two extra lines do not matter to minimal covering: all their endpoints already have private cores;
- why the two flows are not separate mechanisms: their sixty-four weighted-dual states match exactly;
- why the line decoration is familiar: it is the universal weight-six `K_4` reserve atom.

### Unresolved

- an intrinsic six-bit coordinate system on the sixty-four weighted-dual types;
- a conceptual derivation of the statewise type map from the gauge code;
- whether the full rotation systems of corresponding states are equivalent;
- why exactly one weight-six direction, rather than the other low-weight modes, produces the two line cores;
- whether one further connected-cycle move necessarily escapes this module or transports it to another universal module.

## 11. Next targets

### 11.1 Intrinsic coordinates

Search for six graph or surface observables that give an affine bijection

\[
I_6:\{\mathsf U_q:q\in\mathbf F_2^6\}
\longrightarrow\mathbf F_2^6.
\]

Simple parity observables that suffice in dimension three do not yet produce full rank six; higher-order motif or rotation-system invariants may be required.

### 11.2 Square-decoration theorem

Explain conceptually why two parallel `K_4` reserve lines occur on one affine two-flat and why they are redundant relative to the private point system.

### 11.3 Module transition graph

Classify connected-cycle switches between universal renewal modules. The desired finite-state object has:

- vertices: intrinsic renewal-module types;
- edges: horizontal connected-cycle transitions;
- absorbing exits: fibres with an uncovered good state.

### 11.4 Decomposition alternative

If the three-cube and six-cube modules recur indefinitely under horizontal transitions, use their repeated low-weight harmonic interfaces to extract a source-graph cut or gluing decomposition.

## 12. Trust boundary

The two flows, gauge dimensions, sixty-four pairwise distinct weighted-dual types, statewise correspondence, clique arrangement, parallel-line structure, word-weight distribution, and face-count distribution are exact finite computational facts.

The interpretation as a universal six-dimensional renewal module is a mechanism-level synthesis of those facts.

No statement here proves horizontal escape from every six-cube, equivalence of full embeddings, a general module classification, or the five-cycle double cover conjecture.
