# AC-PD-B5.1 — three-cut gluing and the ten-state four-pole boundary alphabet

**Proof-development state:** `COMPLETE-DRAFT`  
**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Exact initial corpus base:** `main@960c92b7ff231c78b387894149779083060a75eb`  
**Validated sources:** `FIVE_CDC_K4_RESERVE_LINE_THREE_CUT_REDUCTION_V1.md` and `FIVE_CDC_FOUR_EDGE_BOUNDARY_SIGNATURES_V1.md`  
**Depends on:** B1.1 indexed five-support semantics  
**Immediate consumers:** B5.2 cap forcing and Kempe alignment; B5.3 routing automata; B6 decomposition  
**External mathematical inputs:** none

## 0. Indexed support object

An indexed five-support even double cover is a five-tuple

$$
(F_1,\ldots,F_5)
$$

of even edge sets such that every edge belongs to exactly two indexed occurrences. Supports may be empty, disconnected, or equal as edge sets. Support names may be permuted globally, but occurrences must not be collapsed.

## 1. Cubic local boundary law

Let $v$ be cubic with incident edges $e_1,e_2,e_3$. Every support uses zero or two of these edges. Let $n_{ij}$ count supports using exactly $e_i,e_j$.

Exact double coverage gives

$$
n_{12}+n_{13}=2,
\qquad
n_{12}+n_{23}=2,
\qquad
n_{13}+n_{23}=2.
$$

### Lemma 1.1

$$
\boxed{n_{12}=n_{13}=n_{23}=1.}
$$

Thus exactly three distinct support indices occur locally, one for each incident-edge pair, and two indices are absent.

### Proof

Subtracting the equations gives equality of the three integers; substitution gives their common value one. $\square$

## 2. Cyclic three-cut completions

Let a three-edge cut

$$
\delta(A)=\{e_1,e_2,e_3\}
$$

separate shores $A,B$. Complete each shore by replacing the three dangling semiedges with edges incident to one new cubic boundary vertex.

### Lemma 2.1 — bridgeless completion

If $G$ is bridgeless and both shores contain cycles, both completions are bridgeless cubic loopless multigraphs.

### Proof

Cubicity and looplessness are immediate. Every original edge lies on a cycle of $G$. If such a cycle crosses the cut, it crosses an even number of times, necessarily two in a three-cut; replace the opposite-shore segment by the two-edge route through the new boundary vertex. This gives a completion cycle through the chosen shore edge.

For a new boundary edge, take a cycle of $G$ containing the corresponding original cut edge. It uses a second cut edge; the shore segment between them and the two new boundary edges form a completion cycle. $\square$

## 3. Three-cut gluing

### Theorem 3.1

If both cyclic-shore completions have indexed five-support even double covers, then $G$ has one.

### Proof

At each new boundary vertex, Lemma 1.1 assigns one support index to each boundary pair

$$
12,\qquad13,\qquad23.
$$

Permute the five support indices on one side so that these three pair-supports agree; map the two absent indices arbitrarily to the two absent indices.

Delete the new vertices and glue corresponding semiedges. For each support index, unite the two shore restrictions and include a cut edge exactly when its aligned boundary trace contains that terminal. Evenness at old vertices is unchanged. Internal edges retain multiplicity two. Each cut edge belongs to the same two aligned pair-supports on both sides and hence to exactly two global support occurrences. $\square$

### Corollary 3.2

A vertex-minimal bridgeless cubic counterexample has no cyclic three-edge cut; it may be assumed cyclically four-edge-connected.

## 4. Four-pole traces

Let $P$ be a cubic four-pole with labelled terminals

$$
T=\{1,2,3,4\}.
$$

The trace of one support is an even subset of $T$, hence empty, a pair, or all of $T$. Every terminal belongs to exactly two traces overall.

Let $t$ be the number of full traces. Removing them, encode every pair trace as an edge of a loopless multigraph $M$ on $T$. Then $M$ is $(2-t)$-regular.

Since $t\le2$, there are only four structural possibilities:

1. $t=2$: no pair traces;
2. $t=1$: one perfect matching;
3. $t=0$: one doubled perfect matching;
4. $t=0$: one simple four-cycle.

## 5. Ten support-unordered states

Let $M_0,M_1,M_2$ be the three perfect matchings of the labelled terminal set.

### Definition 5.1

- $A$: two full traces and three empty traces.
- $B_i$: one full trace, the two pair traces of $M_i$, and two empty traces.
- $C_i$: both pairs of $M_i$ occur twice, with one empty trace.
- $D_i$: the four pair traces form the unique labelled four-cycle whose missing perfect matching is $M_i$, with one empty trace.

### Theorem 5.2 — complete boundary alphabet

Up to permutation of the five support indices, the complete labelled-terminal boundary alphabet is

$$
\boxed{
\mathcal S
=
\{A,B_i,C_i,D_i:i=0,1,2\}.}
$$

These ten states are pairwise distinct. After quotienting also by terminal permutations, they form four orbits $A,B,C,D$.

### Proof

The regular pair-multigraph classification gives existence and completeness. The number of full traces distinguishes $A$ and $B$ from the other types. For $t=0$, multiplicity distinguishes doubled matching from simple four-cycle. With terminal labels retained, the underlying or missing perfect matching distinguishes the three indices. $\square$

## 6. Ordered assignment count

### Proposition 6.1

There are exactly

$$
\boxed{640}
$$

ordered five-support boundary assignments.

### Proof

- Type $A$: choose the two full support indices: $\binom52=10$.
- Type $B$: choose one of three matchings; choose the full support, then ordered supports for its two labelled blocks:
  $$
  3\cdot5\cdot4\cdot3=180.
  $$
- Type $C$: choose one of three matchings; choose the empty support and two of the remaining four supports for one labelled block:
  $$
  3\cdot5\cdot\binom42=90.
  $$
- Type $D$: choose one of three missing matchings; choose the empty support and biject the four cycle edges with the remaining supports:
  $$
  3\cdot5\cdot4!=360.
  $$

The sum is $640$. $\square$

## 7. Exact four-cut gluing

For a four-pole $P$, let

$$
\Sigma(P)\subseteq\mathcal S
$$

be the set of support-unordered states realizable with the fixed terminal labels.

### Theorem 7.1 — signature intersection

If a four-edge cut has shores $P,Q$, then

$$
\boxed{
G\text{ has a five-support cover}
\quad\Longleftrightarrow\quad
\Sigma(P)\cap\Sigma(Q)\ne\varnothing.}
$$

### Proof

A global cover restricts to equal labelled terminal traces on both shores, hence a common state.

Conversely choose a common support-unordered state and globally permute the five support names on one shore so the five labelled traces agree coordinatewise. Glue corresponding semiedges. Internal parity and multiplicities remain valid, and each cut edge appears in the same two support indices on both sides. $\square$

The state must retain labelled terminals. Quotienting by terminal permutations before comparing two fixed shores would lose the correspondence of the original cut edges.

## 8. Standard two-vertex cap

For matching $M_i=X_i\mid Y_i$, attach two cubic vertices, join the two terminals of $X_i$ to one, the two of $Y_i$ to the other, and connect the new vertices.

### Proposition 8.1

The boundary states admitted by this cap are exactly

$$
\boxed{
\mathcal K_i=\{B_j,D_j:j\ne i\}.}
$$

### Proof

The two supports using the internal cap edge each join one terminal from $X_i$ to one from $Y_i$. The support using both $X_i$ terminals at the first cap vertex and the support using both $Y_i$ terminals at the second are either the same or distinct.

If they are the same, one full trace appears and the remaining pair traces form one of the two matchings distinct from $M_i$, giving $B_j$ with $j\ne i$.

If they are distinct, the four pair traces form a four-cycle that uses the two cap-crossing choices and omits one of the two matchings distinct from $M_i$, giving $D_j$ with $j\ne i$. Every such choice is realizable by assigning the local pair-supports at the two cubic cap vertices. $\square$

Thus a standard cap samples four of the ten labelled-terminal states.

## 9. Assurance boundary

The local law, bridgeless completion, three-cut gluing, ten-state alphabet, ordered count, exact four-cut gluing, and cap state set are elementary theorem-level results. No statement here proves that every four-pole profile contains one full cap set or that every cyclic four-cut is reducible.

## 10. Completion assessment

`AC-PD-B5.1` is `COMPLETE-DRAFT`. The next active unit is B5.2: prove minimality-based cap forcing and the exact Kempe path-pairing alignment theorem, including the difference between an aligned local state change and a global support-name transposition.