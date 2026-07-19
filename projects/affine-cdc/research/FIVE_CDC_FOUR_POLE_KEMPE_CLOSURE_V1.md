# Kempe-path closure for four-pole boundary profiles

**Programme:** `AffineCDC — Research Lead`  
**Status:** theorem-level structural reduction plus exact finite profile classification; not canonical pending Director review and literature audit  
**Parents:** `FIVE_CDC_FOUR_EDGE_BOUNDARY_SIGNATURES_V1.md`, `FIVE_CDC_FOUR_EDGE_CAP_FORCING_KERNELS_V1.md`

## 1. Purpose

The four-edge boundary programme previously reduced a cyclic four-cut in a vertex-minimal counterexample to six minimal two-state mismatch kernels in the triangular-prism state space

\[
\mathcal P=\{B_0,B_1,B_2,D_0,D_1,D_2\}.
\]

Those kernels used only cap forcing and signature disjointness. They did not yet use the internal cycle structure of two supports in one boundary cover.

This packet adds a universal Kempe-path closure law. It proves that every realized four-pole profile must contain further signatures forced by support-pair switches. Combining Kempe closure with cap forcing enlarges all six previous kernels and leaves only four disjoint profile-pair orbits.

The mechanism is elementary:

\[
\boxed{
F_a\triangle F_b
\text{ with four boundary endpoints}
\text{ is two terminal paths plus cycles.}
}
\]

Switching the names `a,b` on either path preserves the five-support cover and changes the boundary signature.

## 2. Support-pair symmetric differences

Let

\[
(F_1,\ldots,F_5)
\]

be an indexed five-support boundary cover of a cubic four-pole `P` with terminals `1,2,3,4`.

For two support indices `a,b`, put

\[
H_{ab}:=F_a\triangle F_b.
\]

At every internal cubic vertex, both `F_a` and `F_b` have even degree. Hence `H_{ab}` has internal degree zero or two.

A boundary terminal is an endpoint of `H_{ab}` precisely when exactly one of the two support traces contains that terminal.

### Lemma 2.1 — four-endpoint path decomposition

If `H_{ab}` has all four boundary terminals as endpoints, then

\[
\boxed{
H_{ab}
=
P_1\sqcup P_2\sqcup\mathcal Z,
}
\]

where `P_1,P_2` are terminal-to-terminal paths whose endpoints form one perfect matching of the four terminals, and `\mathcal Z` is a disjoint union of cycles.

#### Proof

Every internal vertex has degree zero or two in `H_{ab}`. Therefore each nontrivial connected component is a path or a cycle. A path component contains exactly two degree-one boundary endpoints. With four endpoints in total there are exactly two path components; all remaining components are cycles. ∎

### Lemma 2.2 — Kempe-path switch

Switch the memberships of supports `a` and `b` on every edge of one path `P_r`.

Then:

1. both new supports remain even at every internal vertex;
2. every edge still belongs to exactly two of the five supports;
3. all other supports are unchanged;
4. the two path endpoints exchange whether they belong to `a` or `b`.

Hence the switched family is another indexed five-support boundary cover of the same four-pole.

#### Proof

On an internal path vertex, exactly two incident edges are switched, so parity is preserved. On each switched edge the two support names are exchanged rather than added or removed, so the total edge multiplicity remains two. ∎

This switch is always available; no embedding, root lift, or Fano flow is required.

## 3. The ten labelled boundary states

Use the ten support-unordered, terminal-labelled states

\[
\mathcal S
=
\{A,B_i,C_i,D_i:i=0,1,2\},
\]

where `i` records one of the three perfect matchings of the four terminals.

Let

\[
\Sigma(P)\subseteq\mathcal S
\]

be the complete boundary-signature profile of `P`.

For each state, inspect every support pair having four boundary disagreement endpoints. Lemmas 2.1 and 2.2 force `\Sigma(P)` to meet the appropriate set of possible path-pairing outcomes.

Write

\[
\{i,j,k\}=\{0,1,2\}.
\]

### Theorem 3.1 — four-pole Kempe closure table

Every realizable profile `\Sigma(P)` satisfies the following implications.

#### State `A`

\[
A\in\Sigma(P)
\Longrightarrow
\Sigma(P)\cap\{B_0,B_1,B_2\}\ne\varnothing.
\]

#### State `B_i`

\[
B_i\in\Sigma(P)
\Longrightarrow
\Sigma(P)\cap\{A,B_j,B_k\}\ne\varnothing
\]

and

\[
B_i\in\Sigma(P)
\Longrightarrow
\Sigma(P)\cap\{C_i,D_j,D_k\}\ne\varnothing.
\]

#### State `C_i`

\[
C_i\in\Sigma(P)
\Longrightarrow
\Sigma(P)\cap\{B_i,D_j,D_k\}\ne\varnothing.
\]

#### State `D_i`

\[
D_i\in\Sigma(P)
\Longrightarrow
\Sigma(P)\cap\{B_j,C_j,D_k\}\ne\varnothing
\]

and

\[
D_i\in\Sigma(P)
\Longrightarrow
\Sigma(P)\cap\{B_k,C_k,D_j\}\ne\varnothing.
\]

#### Proof

Choose canonical support labels for each boundary type. For every support pair with four disagreement terminals, Lemma 2.1 says the two paths induce one of the three perfect matchings. Switching one path by Lemma 2.2 gives the corresponding state in the displayed outcome set.

For example, in state `B_i`:

- switching the two complementary pair-supports gives `A`, `B_j`, or `B_k` according to the path pairing;
- switching the full-trace support with either absent support gives `C_i`, `D_j`, or `D_k`.

The remaining rows are the same finite boundary calculation. ∎

A profile satisfying all displayed implications will be called **Kempe-closed**.

## 4. Interaction with cap forcing

For a shore `P` of a cyclic four-edge cut in a vertex-minimal counterexample, the standard two-vertex caps give

\[
\Sigma(P)\cap\mathcal K_i\ne\varnothing
\qquad(i=0,1,2),
\]

where

\[
\mathcal K_i=\{B_j,D_j:j\ne i\}.
\]

Thus every such shore profile is both:

1. **cap-forced**: it meets all three `\mathcal K_i`;
2. **Kempe-closed**: it obeys Theorem 3.1.

If `P,Q` are the two shores of a counterexample cut, exact gluing still requires

\[
\Sigma(P)\cap\Sigma(Q)=\varnothing.
\]

The problem is therefore a finite classification of disjoint cap-forced Kempe-closed subsets of `\mathcal S`.

## 5. Exact finite profile classification

The ten-state space has only `2^{10}` subsets, so the closure problem is exhausted directly.

### Computational Theorem 5.1

There are exactly

\[
\boxed{368}
\]

cap-forced Kempe-closed profiles.

Their size distribution is

\[
\begin{array}{c|rrrrrrrr}
|\Sigma|&3&4&5&6&7&8&9&10\\
\hline
\text{profiles}&4&27&66&111&104&45&10&1.
\end{array}
\]

Exactly

\[
\boxed{31}
\]

are inclusion-minimal. Under simultaneous permutation of the three matching indices, these form

\[
\boxed{8}
\]

profile orbits.

The finite counts are reproduced by the dependency-free private verifier.

## 6. Four Kempe-stable mismatch kernels

Choose one inclusion-minimal cap-forced Kempe-closed subprofile from each shore of a disjoint pair. There are exactly

\[
\boxed{18}
\]

labelled disjoint pairs.

Quotient simultaneously by:

- the `S_3` permutation of matching indices;
- interchange of the two shores.

### Theorem 6.1 — four Kempe-stable pair orbits

Exactly four orbits remain. Representatives are:

\[
\begin{array}{c|c}
\text{shore }P&\text{shore }Q\\
\hline
\{A,B_0,C_1,D_0,D_1\}
&\{B_1,B_2,C_0,C_2,D_2\}\\
\{A,B_0,C_1,D_2\}
&\{B_1,B_2,D_0\}\\
\{B_0,B_1,C_0,C_1\}
&\{D_0,D_1,D_2\}\\
\{B_0,B_1,D_2\}
&\{C_0,C_1,D_0,D_1\}.
\end{array}
\]

Every disjoint cap-forced Kempe-closed profile pair contains, after relabelling and shore exchange, one of these four representatives.

#### Proof status

The Kempe closure table is theorem-level. The profile and orbit counts are an exact exhaustive finite classification over the ten-state space. ∎

These four pairs are minimal profile witnesses, not a classification of all enlarged disjoint pairs.

## 7. Relation to the previous six kernels

The earlier cap-forcing packet selected only two-state witnesses from the triangular-prism subsystem and found six pair orbits.

Theorem 3.1 shows that none of those two-state profiles can be a complete realizable shore profile: every one forces additional A/B/C/D states by Kempe path switching.

After adjoining all mandatory closure states and taking inclusion-minimal profiles, the six old kernels merge into four Kempe-stable pair types.

Thus the irreducible four-pole obstruction has been reduced from

\[
\text{six two-state prism kernels}
\]

to

\[
\boxed{
\text{four full ten-state Kempe-closed mismatch kernels}.
}
\]

## 8. Mechanism map

The decomposition side of the programme now has the following levels.

### Level A — cyclic three-cuts

A weight-six `K_4` reserve direction yields a cyclic three-edge cut. The three-boundary signature is unique, so five-support covers glue automatically.

### Level B — four-boundary alphabet

Four terminals carry the ten labelled states

\[
A,B_i,C_i,D_i.
\]

### Level C — cap forcing

Minimality forces every shore profile to meet each standard cap set `\mathcal K_i`.

### Level D — Kempe closure

Internal support-pair paths force transitions among A/B/C/D states according to Theorem 3.1.

### Level E — irreducible mismatch

Only four minimal disjoint profile-pair orbits survive both forcing mechanisms.

The updated target is therefore:

\[
\boxed{
\text{pure point renewal}
\longrightarrow
\text{four Kempe-stable four-pole kernels}
\longrightarrow
\text{escape or bounded decomposition}.
}
\]

## 9. What the four kernels encode

The four representatives reveal two qualitatively different regimes.

1. **A-containing kernels.**  
   Two pair orbits contain a shore with Type A. For such a cover, several support-pair path systems must all select a restricted set of terminal matchings in order to avoid generating a common signature on the opposite shore.

2. **A-free kernels.**  
   Two pair orbits use only B/C/D states. Their mismatch is a constrained routing problem among doubled matchings and four-cycle traces.

In both regimes, persistence of disjointness is no longer merely a boundary-count condition. It requires a coherent system of terminal pairings for the internal Kempe paths.

This suggests the next invariant should record not only which signature occurs but which perfect matching is induced by each four-endpoint support-pair symmetric difference.

## 10. Refined next targets

### 10.1 Kempe-routing refinement

For every boundary cover, record the terminal matching induced by each four-endpoint graph

\[
F_a\triangle F_b.
\]

Classify the compatible routing data over the four surviving profile pairs. Determine whether any pair can be realized without creating a common signature.

### 10.2 Universal-module projection

For the minimum `2K_3` circuit in the universal three-dimensional renewal cube, cut the source graph into its three four-pole components and compute their complete Kempe-closed profiles and routing data.

This will test whether the universal cube realizes one of the four kernels or instead lives strictly outside the minimal-counterexample regime.

### 10.3 Unique-linkage alternative

If one of the A-containing kernels forces all relevant Kempe path systems to use one terminal matching, extract a bounded linkage or separation certificate from that routing rigidity.

### 10.4 Kernel elimination

For each of the four pairs, prove one of:

\[
\boxed{
\text{Kempe routing forces a common signature}
}
\]

or

\[
\boxed{
\text{the four-pole has a smaller cut/decomposition interface}.
}
\]

## 11. Trust boundary

The path-decomposition lemma, Kempe-path switch, and closure implications are elementary theorem-level arguments.

The counts `368`, `31`, `8`, `18`, and `4`, and the four displayed orbit representatives, are exact finite computation.

No statement here proves that the four kernels are realizable, eliminates all cyclic four-edge cuts, proves horizontal escape from pure point renewal, or proves the five-cycle double cover conjecture.
