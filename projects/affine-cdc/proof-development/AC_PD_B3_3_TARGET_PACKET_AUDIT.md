# AC-PD-B3.3 — target-packet and factorable defect-core audit

**Proof-development state:** `COMPLETE-DRAFT / SCOPE-NORMALIZATION`  
**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Exact initial corpus base:** `main@960c92b7ff231c78b387894149779083060a75eb`  
**Recovered source checkpoint:** `research/affine-cdc-five-cdc-v1@dad218dd18ed05d1b7cb730c2dc2431b4db5ec9c`  
**Depends on:** B1.4, B3.1, B3.2  
**Immediate consumers:** consolidated B3 map; B4 reconfiguration; B8 certificate ledger; B9 target route  
**External mathematical inputs:** none

## 0. Audit rule

Every target packet is classified by both proof status and object scope.

- `FULL-DUAL`: concerns $T_g^{(1)}\to\mathscr A_5$.
- `FACTORABLE`: concerns the old-colour quotient $J_g\to\mathscr A_5$.
- `TARGET-GRAPH`: concerns arbitrary graph homomorphisms into $\mathscr A_5$.
- `THEOREM`: has a self-contained mathematical proof.
- `CERTIFICATE`: depends on explicit finite data or private computation not independently regenerated here.
- `EVIDENCE`: numerical or orbit data not used as a theorem premise.

A theorem about $J_g$ may give a sufficient five-support construction, but failure of $J_g\to\mathscr A_5$ is not failure of the full-dual same-embedding problem.

## 1. Validated target-graph theorems

### 1.1 Clique links

`FIVE_CDC_HALFCUBE_CLIQUE_LINK_CAPACITY_V1.md` is `VALID / TARGET-GRAPH / THEOREM`.

Its link table is correct:

$$
\begin{array}{c|c|c}
r&\operatorname{Lk}(Q_r)&\chi\\
\hline
1&L(K_5)&5\\
2&K_3\square K_2&3\\
3&K_2\sqcup K_1&2\\
4&K_1&1\\
5&\varnothing&0.
\end{array}
$$

B3.1 gives a general quadratic derivation.

### 1.2 Exact dominating-clique capacity

`FIVE_CDC_DOMINATING_CLIQUE_EXACT_CAPACITY_V1.md` is `VALID / TARGET-GRAPH / THEOREM`.

For $2\le r\le5$,

$$
K_r\vee H\to\mathscr A_5
\quad\Longleftrightarrow\quad
\chi(H)\le5-r.
$$

For $r=1$, the exact remainder target is $L(K_5)$ rather than a chromatic threshold.

### 1.3 $K_6$-free warning

`FIVE_CDC_K6_FREE_HALFCUBE_WARNING_V1.md` is `VALID / TARGET-GRAPH / THEOREM`.

The Mycielski graph $M(K_5)$ is $K_6$-free but does not map to $\mathscr A_5$. The proof using the rigidity of four-neighbour links inside a target $K_5$ is correct. The packet explicitly does not claim realization as a compatible dual triangulation.

### 1.4 Exact eight-vertex classification

`FIVE_CDC_HALFCUBE_SUBGRAPH_CLASSIFICATION_V1.md` is `VALID / TARGET-GRAPH / THEOREM`.

For a graph $J$ on eight fixed vertices,

$$
J\to\mathscr A_5
\quad\Longleftrightarrow\quad
K_6\nsubseteq J
\text{ and }
K_8-C_5\nsubseteq J.
$$

Equivalently, $K_8-J$ contains $3K_2$, $K_3\sqcup K_2$, or $K_4$. The proof is structural, using conflict graphs and elementary Clebsch parameters; it is not merely a private enumeration.

## 2. Source-dependent compression packets

### 2.1 Source-dependent half-cube compression

`FIVE_CDC_SOURCE_DEPENDENT_HALFCUBE_COMPRESSION_V1.md` is `VALID / FACTORABLE / SUFFICIENT-THEOREM`.

A homomorphism

$$
J_g\to\mathscr A_5
$$

produces a cut-continuous map to $K_5$ and therefore a genuine five-support cover of the source graph. This implication is fully valid.

It is not a complete criterion for componentwise compression of the fixed root lift, because a map

$$
T_g^{(1)}\to\mathscr A_5
$$

may fail to factor through $J_g$.

### 2.2 Unused matching

`FIVE_CDC_UNUSED_MATCHING_COMPRESSION_V1.md` is `VALID / FACTORABLE / SUFFICIENT-THEOREM`.

If the unused-root graph contains $3K_2$, then identifying the endpoints of those three unused edges gives a map $J_g\to K_5\subset\mathscr A_5$. The fourteen-used-root and small-cubic-graph corollaries are correct.

### 2.3 Matching orbits

`FIVE_CDC_UNUSED_MATCHING_ORBITS_V1.md` is `VALID WITH DISPLAY CORRECTION / FINITE-GEOMETRY THEOREM`.

The action of $\operatorname{AGL}(3,2)$ on the 420 three-edge matchings has exactly three orbits of sizes

$$
28,\qquad168,\qquad224,
$$

classified by direction multiplicities:

1. three equal directions;
2. exactly two equal directions;
3. three independent directions.

The displayed representative for the all-parallel orbit is wrong: $\{05,14,23\}$ has directions $5,5,1$, not three copies of $5$. A correct all-parallel representative is

$$
\boxed{\{01,23,45\}},
$$

with three copies of direction $1$. The other displayed representatives have the stated direction patterns.

The orbit theorem and sizes are unaffected by this representative typo.

## 3. Factorable bad-core packets

### 3.1 Container dichotomy

`FIVE_CDC_BAD_LIFT_CONTAINER_DICHOTOMY_V1.md` is `VALID / FACTORABLE / THEOREM` after terminology normalization.

Let $U_g=K_8-J_g$. Then

$$
J_g\not\to\mathscr A_5
$$

if and only if

$$
\tau(U_g)\le2
\quad\text{or}\quad
U_g\subseteq C_5
$$

for some five-cycle. The used/unused pivot update formula is exact.

Every occurrence of “compressible” in this packet should read “old-colour-factorably compressible” unless the implication to a source five-support cover is being used only in the successful direction.

### 3.2 Two-apex or pentagon core

`FIVE_CDC_DEFECT_CORE_QUOTIENT_AND_TWO_LEVEL_ARRANGEMENT_V1.md` is `VALID / FACTORABLE / THEOREM+EVIDENCE`.

The sharp static theorem is correct:

$$
J_g\not\to\mathscr A_5
\quad\Longleftrightarrow\quad
\tau(U_g)\le2
\text{ or }
U_g\cong C_5.
$$

A proper subgraph of a five-cycle has vertex-cover number at most two. The Burnside count of 100 marked two-apex presentations is correct. The collapse to 88 unmarked isomorphism types is computational evidence and is not used by the proof.

The defect spectrum $\Sigma(f)$ detects factorable goodness of the fibre, not full componentwise goodness. Its two-level reconfiguration architecture remains useful after that scope correction.

### 3.3 Ideal-pivot depth

`FIVE_CDC_DEFECT_COVER_DEPTH_AND_IDEAL_PIVOT_V1.md` is `VALID / FACTORABLE TARGET MODEL / THEOREM`.

The ideal target update has

$$
\tau(P_{c,d,L}(U))\le\tau(U)+1.
$$

Among factorably bad cores, every ideal pivot remains bad exactly when $\tau(U)\le1$. Two-cover states of exact cover number two and the pentagon admit an abstract one-step target escape.

The packet correctly states that this does not prove realizability by an actual source support cycle. Its star-core escape problem is a source-side reconfiguration problem and belongs downstream in B4–B7.

## 4. Compatible flower obstruction and finite certificates

`FIVE_CDC_FLOWER_J5_MIXED_CORE_OBSTRUCTION_V1.md` has two layers.

### Theorem layer

The target argument is `VALID / FULL-DUAL CONDITIONAL THEOREM`:

- the common link of an edge is the triangular prism;
- therefore $K_2\vee H\not\to\mathscr A_5$ whenever $\chi(H)\ge4$;
- equivalently $K_3\vee C_{2m+1}$ gives a rank-three obstruction;
- if the displayed dual $D_9$ contains $K_3\vee C_5$, then $D_9\not\to\mathscr A_5$.

### Certificate layer

The explicit flower flow, reduced-fibre size, dual graphs, face lengths, 712-neighbour census, and all detailed counts are `EXACT FINITE CERTIFICATE / NOT INDEPENDENTLY REGENERATED BY AC-PDL`.

They remain admissible evidence with their exact refs and private verifier, but Curator integration must not recast the numerical tables as independently audited theorem facts. The short human obstruction proof is independent once the certified dual subgraph containment is accepted.

## 5. Componentwise checkpoint

`FIVE_CDC_COMPONENTWISE_PROGRAMME_CHECKPOINT_V1.md` is `VALID / SCOPE CHECKPOINT + CERTIFICATE`.

Its central correction from $J_g$ to $T_g$ is correct. The neighbourhood counts are finite certificate data and remain on that assurance axis. The statement that every one of 752 displayed bad duals contains $K_6$ is exact only for that enumerated laboratory and is not a universal theorem.

## 6. Scope map

The validated implication chain is

$$
J_g\to\mathscr A_5
\Longrightarrow
T_g^{(1)}\to\mathscr A_5
\Longrightarrow
\text{five-support cover},
$$

where the first arrow uses the quotient map $T_g^{(1)}\to J_g$.

The converse of the first arrow fails in general. Consequently:

- used-root graphs, unused-root containers, matching orbits, two-apex cores, pentagon cores, and ideal pivots classify the factorable route;
- clique links and dominating joins apply to any target graph, including full duals;
- flower $D_9$ is a full-dual obstruction once its certified dual graph is fixed;
- factorable badness cannot be promoted to full-dual badness.

## 7. Curator normalization requirements

1. Preserve the clique-link, exact capacity, and eight-vertex classification packets as valid theorem sources.
2. Correct only the all-parallel standard representative in the unused-matching orbit packet.
3. Rename unqualified “compressible/bad lift” terminology in the container and defect-core packets to “old-colour-factorably compressible/bad”.
4. Keep 88 unmarked cores and all neighbourhood censuses on the computational-evidence axis.
5. Preserve ideal-pivot theorems as target-side models, not actual source-move existence theorems.
6. Keep the full-dual flower obstruction separate from the factorable two-apex/pentagon quotient theory.

## 8. Completion assessment

`AC-PD-B3.3` is `COMPLETE-DRAFT / SCOPE-NORMALIZATION`. No controlling target packet inspected here is false. One displayed matching representative requires correction, and several theorem families require factorable/full-dual terminology separation.