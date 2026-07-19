# Exact small four-pole profile census and the full-cap-profile target

**Programme:** `AffineCDC — Research Lead`  
**Status:** exact finite computational theorem through six internal vertices, with a general structural conjecture; not canonical pending Director review and literature audit  
**Parents:** `FIVE_CDC_FOUR_EDGE_BOUNDARY_SIGNATURES_V1.md`, `FIVE_CDC_FOUR_EDGE_CAP_FORCING_KERNELS_V1.md`, `FIVE_CDC_FOUR_POLE_KEMPE_CLOSURE_V1.md`

## 1. Purpose

The four-pole programme has reduced a cyclic four-edge cut in a vertex-minimal counterexample to four Kempe-stable disjoint profile-pair kernels.

This packet asks what complete boundary profiles actually occur for small cubic four-poles. The exact census reveals a much stronger pattern than cap forcing or abstract Kempe closure alone:

\[
\boxed{
\text{every small admissible profile contains one entire standard-cap set }\mathcal K_i.
}
\]

Only eight complete profile types occur through six internal vertices. The four Kempe-stable obstruction kernels are absent.

## 2. Four-poles and admissibility

A labelled cubic four-pole is represented by:

- a connected loopless subcubic multigraph `P`;
- four labelled boundary semiedges filling the degree deficits, so every internal vertex has total degree three.

The four-pole is called **cap-admissible** when no internal bridge separates all four boundary semiedges from none. Equivalently, attaching the four-pole to a connected opposite shore does not leave an internal edge which is forced to remain a bridge solely by the cap.

Parallel internal edges are allowed; loops are not.

For each four-pole, the complete profile

\[
\Sigma(P)
\subseteq
\mathcal S
=
\{A,B_i,C_i,D_i:i=0,1,2\}
\]

is computed by an exact constraint solver. Each internal edge receives a two-element subset of five support indices, and at every cubic vertex the three incident labels must be the three edges of a triangle on three support indices.

This is exactly the local five-support condition, not a relaxation.

## 3. Exact graph population

For `n=2,4,6` internal vertices, every connected loopless subcubic multigraph with total degree deficit four is generated and quotiented by vertex isomorphism.

The numbers of underlying multigraph isomorphism classes are

\[
\begin{array}{c|ccc}
n&2&4&6\\
\hline
\text{classes}&1&4&25.
\end{array}
\]

Thus the census covers

\[
\boxed{30}
\]

underlying graph classes.

After assigning the four labelled boundary semiedges to the degree-deficit slots and removing non-admissible assignments, the representative-level labelled assignment counts are

\[
6,\qquad54,\qquad354.
\]

These counts include boundary labellings related by graph automorphisms; they are verifier bookkeeping rather than orbit counts.

## 4. The eight observed profiles

Recall the standard cap sets

\[
\mathcal K_i
=
\{B_j,D_j:j\ne i\}.
\]

Let

\[
\mathcal S
=
\{A,B_0,B_1,B_2,C_0,C_1,C_2,D_0,D_1,D_2\}.
\]

### Computational Theorem 4.1

Across all cap-admissible labelled four-poles with at most six internal vertices, exactly the following eight complete profiles occur:

\[
\boxed{
\mathcal K_0,\ \mathcal K_1,\ \mathcal K_2,
}
\]

\[
\boxed{
\mathcal S\setminus\{B_0\},
\quad
\mathcal S\setminus\{B_1\},
\quad
\mathcal S\setminus\{B_2\},
}
\]

\[
\boxed{
\mathcal S\setminus\{A\},
\qquad
\mathcal S.
}
\]

No other cap-forced Kempe-closed profile occurs.

The order-by-order appearance is:

\[
\begin{array}{c|l}
2&\mathcal K_0,\mathcal K_1,\mathcal K_2\\
4&\mathcal K_i\text{ and }\mathcal S\setminus\{B_i\}\\
6&\text{all eight profile types}.
\end{array}
\]

The result is an exhaustive finite theorem, reproduced by a dependency-free generator, graph-isomorphism canonicalizer, bridge test, and triangle-label CSP.

## 5. Full-cap property in the exact range

Every one of the eight profiles contains at least one complete cap set:

\[
\boxed{
\forall P,\quad |V(P)|\le6
\Longrightarrow
\exists i\in\{0,1,2\}:
\mathcal K_i\subseteq\Sigma(P).
}
\]

For the three smallest profiles this is equality. For each larger profile it follows by inspection.

This is substantially stronger than cap forcing, which only gives

\[
\Sigma(P)\cap\mathcal K_i\ne\varnothing
\qquad(i=0,1,2).
\]

Cap forcing requires one state from each of three overlapping sets. The small-profile theorem gives all four states of one set.

## 6. Minimal-counterexample size consequence

Let `G` be a vertex-minimal bridgeless cubic graph without a five-support cycle double cover, and suppose a cyclic four-edge cut has shores `P,Q`.

Both shore profiles are cap-forced. If, for example, `P` has at most six internal vertices, Theorem 4.1 gives an index `i` with

\[
\mathcal K_i\subseteq\Sigma(P).
\]

Cap forcing on `Q` gives

\[
\Sigma(Q)\cap\mathcal K_i\ne\varnothing.
\]

Therefore

\[
\Sigma(P)\cap\Sigma(Q)\ne\varnothing,
\]

contradicting the exact four-cut gluing criterion.

### Corollary 6.1

Every shore of a cyclic four-edge cut in a vertex-minimal counterexample has at least eight internal vertices.

Since a cubic four-pole has an even number of internal vertices, the excluded orders are exactly `2,4,6`.

In particular, any minimal counterexample containing a cyclic four-cut has at least sixteen vertices across the two shores. This numerical bound is secondary; the structural exclusion of all small shore profiles is the main conclusion.

## 7. Relation to the four Kempe kernels

None of the four Kempe-stable mismatch profiles contains a full `\mathcal K_i`. Thus none appears in the exact small census.

This identifies the next theorem target very sharply.

### Full-cap-profile target

For every connected cap-admissible cubic four-pole which occurs as a shore in the minimal-counterexample regime, prove

\[
\boxed{
\exists i:
\mathcal K_i\subseteq\Sigma(P).
}
\]

If this holds, every cyclic four-edge cut in a vertex-minimal counterexample is impossible: one shore contains `\mathcal K_i`, while the other shore, by cap forcing, meets it.

Thus the full-cap-profile theorem would improve cyclic four-edge connectivity to cyclic five-edge connectivity.

## 8. Evidence beyond the exhaustive range

A deterministic exploratory search over connected simple cap-admissible four-poles of orders eight, ten, and twelve found only the same eight profile types.

This larger-order search is evidence, not an exhaustive theorem. It is not used in Corollary 6.1.

The persistence of exactly eight profiles suggests that the observed family may be universal:

\[
\boxed{
\Sigma(P)\in
\{\mathcal K_i,\mathcal S\setminus\{B_i\},
\mathcal S\setminus\{A\},\mathcal S\}
}
\]

for every connected cap-admissible cubic four-pole. The weaker full-cap-profile target is sufficient for the decomposition programme and should be attacked first.

## 9. Possible mechanism behind the eight profiles

For an ordinary even subgraph meeting all four terminals, the internal degree condition forces two terminal-to-terminal paths. Let

\[
L(P)\subseteq\{M_0,M_1,M_2\}
\]

be the set of terminal pairings realizable by such full-trace even subgraphs.

In the exact census:

- singleton linkage sets occur with the profiles `\mathcal K_i`;
- two-element linkage sets occur with `\mathcal S\setminus\{B_i\}` or `\mathcal S`;
- the full three-matching linkage set occurs with `\mathcal S\setminus\{A\}` or `\mathcal S`.

This suggests that the eight-profile phenomenon is controlled by:

1. the ordinary four-terminal linkage set `L(P)`;
2. one additional bit recording whether the most degenerate full-trace pairing can be doubled compatibly to produce Type A.

This interpretation is not yet a theorem. It provides a more geometric route than continuing raw profile enumeration.

## 10. Updated mechanism map

The four-pole branch of the programme now reads:

\[
\text{four boundary edges}
\longrightarrow
10\text{ labelled states}
\longrightarrow
\text{cap forcing}
\longrightarrow
\text{Kempe closure}
\longrightarrow
4\text{ mismatch kernels}.
\]

The small census adds:

\[
\boxed{
\text{actual small four-poles occupy only eight large profile types,
all containing a full }\mathcal K_i.
}
\]

Hence the four surviving abstract kernels are not small local atoms. If they are realizable at all, they require a larger coherent linkage-routing structure.

## 11. Next targets

### 11.1 Prove the full-cap property

Use Kempe routing and four-terminal linkage theory to show that every cap-forced profile contains one full `\mathcal K_i`.

### 11.2 Linkage-set classification

Determine the exact relation between `L(P)` and `\Sigma(P)`. A theorem recovering the eight observed profiles from `L(P)` plus one binary invariant would eliminate the four kernels.

### 11.3 Search for the first counterprofile

Perform an exhaustive order-eight multigraph census or a certified SAT search specifically for a cap-admissible four-pole whose profile is cap-forced but contains no full `\mathcal K_i`.

Either outcome is useful:

- absence supplies the next exact range and stronger evidence;
- an example identifies the first genuine four-pole obstruction atom.

## 12. Trust boundary

The class counts, assignment counts, eight profile sets, and order-six full-cap property are exact finite computation.

The order-eight-and-above observations and universal eight-profile statement are evidence and conjecture.

No statement here proves the full-cap-profile theorem, eliminates all cyclic four-edge cuts, or proves the five-cycle double cover conjecture.
