# Cut interfaces, four-pole states, and routing rigidity

## 1. Why interfaces are the natural source-side language

The surface and gauge theories detect obstruction cores, but a global proof needs strict progress on the source graph. The natural progress operations are:

- split along a small edge cut;
- replace a bounded multipole;
- glue compatible boundary covers;
- show that a persistent obstruction forces one of these interfaces.

For five supports the three-edge and four-edge interfaces behave very differently. Three-edge data are unique up to support permutation; four-edge data form a ten-state finite geometry with nontrivial routing.

## 2. The cubic local boundary law

At a cubic vertex, let $n_{ij}$ count supports using exactly the two incident edges $e_i,e_j$. Exact double coverage gives

$$
n_{12}+n_{13}=2,
\qquad
n_{12}+n_{23}=2,
\qquad
n_{13}+n_{23}=2.
$$

Hence

$$
\boxed{n_{12}=n_{13}=n_{23}=1.}
$$

Exactly three support indices occur locally, one for every pair of incident edges; two support indices are locally absent.

This elementary law drives three-cut gluing and the cap construction for four-poles.

## 3. Three-edge-cut gluing

Let a cyclic three-edge cut separate shores $A,B$. Complete each shore by one new cubic vertex attached to its three boundary semiedges. If the original graph is bridgeless and both shores contain cycles, both completions are bridgeless cubic loopless multigraphs.

At each new boundary vertex, the cubic local law assigns one support index to each pair of boundary edges. Permute the five support indices on one shore so that the three pair-supports agree; the two absent indices may be matched arbitrarily. Deleting the new vertices and joining the corresponding boundary edges gives a global five-support cover.

### Theorem 3.1 — three-cut gluing

Five-support covers glue across every cyclic three-edge cut.

### Corollary 3.2

A vertex-minimal bridgeless cubic counterexample has no cyclic three-edge cut. It may be assumed cyclically four-edge-connected.

## 4. Harmonic $K_4$ reserve lines are decomposition certificates

Let a marked connected dual obstruction core have reserve $R_C$, and suppose its occurrence locus has a weight-six direction whose harmonic cut quotient is $K_4$.

All marked face circuits avoid the six support edges. Adjacency of marked faces forces them into one component of the complement. In the $K_4$ quotient, that component has exactly one edge to each of the other three components.

### Theorem 4.1 — reserve-line separation

A connected marked core admitting a $K_4$ reserve direction lies behind a cyclic three-edge cut.

Therefore no such affine occurrence line appears in the gauge fibre of a vertex-minimal counterexample. The positive-dimensional $K_4$ lines found in finite renewal censuses are decomposition certificates, not irreducible obstruction atoms.

After three-cut reduction, the corresponding renewal geometry is pure private-point geometry.

## 5. Four-edge boundary traces

Let $P$ be a cubic four-pole with labelled boundary semiedges $1,2,3,4$. Restrict an indexed five-support cover to the boundary. Every support trace is an even subset of the four terminals, and each terminal occurs twice overall.

Up to support permutation there are exactly ten states:

$$
\mathcal S
=
\{A,B_i,C_i,D_i:i=0,1,2\}.
$$

The index $i$ refers to one of the three perfect matchings $M_i$ of four terminals.

- $A$: two full traces and three empty traces;
- $B_i,C_i,D_i$: the remaining trace multiplicity patterns, distinguished by matching index and repetition type.

The ten states are the complete support-unordered boundary alphabet.

## 6. Exact four-cut gluing

For a four-pole $P$, let

$$
\Sigma(P)\subseteq\mathcal S
$$

be its complete boundary profile.

### Theorem 6.1 — signature intersection

If a cyclic four-edge cut has shores $P,Q$, then their covers glue exactly when

$$
\Sigma(P)\cap\Sigma(Q)\ne\varnothing.
$$

After choosing a common support-unordered state, one may permute support indices to align the full labelled traces and glue coordinatewise.

Thus a minimal-counterexample four-cut is possible only when two cap-forced profiles are disjoint.

## 7. Cap forcing

For each matching $M_i$, attach the standard two-vertex cap whose two terminal pairs are the blocks of $M_i$. Minimality gives a five-support cover of the capped smaller graph. Restricting back to the shore yields one state in

$$
\mathcal K_i
=
\{B_j,D_j:j\ne i\}.
$$

### Theorem 7.1 — cap forcing

Every shore profile in the minimal-counterexample regime meets all three cap sets:

$$
\Sigma(P)\cap\mathcal K_i\ne\varnothing
\qquad(i=0,1,2).
$$

Cap forcing does not imply that one full $\mathcal K_i$ lies in the profile. The missing information is the routing of support-pair symmetric differences inside the shore.

## 8. Kempe paths and pairing alignment

Choose complementary support indices $a,b$ whose boundary traces differ at all four terminals. Their symmetric difference

$$
X_{ab}=F_a\triangle F_b
$$

is a relative even subgraph. Its boundary-connected part consists of two terminal paths realizing one matching

$$
M_P(a,b).
$$

In the standard cap for $M_i$, the same symmetric difference realizes $M_i$.

### Theorem 8.1 — cap/Kempe alignment

A support-pair Kempe switch changes the support-unordered boundary state if and only if

$$
M_P(a,b)=M_i.
$$

- aligned matchings produce two separate cap-shore cycles; switching one changes one boundary block;
- misaligned matchings produce one four-terminal cycle; switching it is only a global transposition of support names.

Therefore the full-cap problem is a theorem about internal four-terminal linkage, not merely closure of a ten-state table.

## 9. Routing-weight coordinates

Identify the four terminals with $AG(2,2)$. The three matchings are its three parallel classes. For each matching $M_i=X_i\mid Y_i$ and each boundary trace $S_r$, define

$$
q_i(S_r)=|S_r\cap X_i|\pmod2,
$$

and

$$
\omega_i(\sigma)=\frac12\sum_{r=1}^5q_i(S_r)
\in\{0,1,2\}.
$$

### Theorem 9.1 — ten-state coordinate geometry

The map

$$
\Omega:\mathcal S\longrightarrow\{0,1,2\}^3
$$

is injective, with

$$
\begin{array}{c|c}
A&(0,0,0)\\
B_0&(0,1,1)\\
B_1&(1,0,1)\\
B_2&(1,1,0)\\
C_0&(0,2,2)\\
C_1&(2,0,2)\\
C_2&(2,2,0)\\
D_0&(2,1,1)\\
D_1&(1,2,1)\\
D_2&(1,1,2).
\end{array}
$$

A Kempe switch routed by $M_i$ preserves exactly $\omega_i$.

For one fixed routing matching, the transition graph is

$$
P_3\sqcup C_4\sqcup P_3,
$$

and the middle $C_4$ is exactly $\mathcal K_i$.

## 10. Uniform routing is reducible

Call a four-pole globally $i$-routed if every complementary support-pair difference in every indexed cover realizes $M_i$.

The profile is then a union of connected components of the fixed-routing transition graph. Cap forcing implies that the entire middle component $\mathcal K_i$ is present.

### Theorem 10.1 — uniform-routing elimination

No shore of a cyclic four-edge cut in a vertex-minimal counterexample is globally routed by one matching.

Uniform linkage rigidity is therefore not the residual obstruction. A real residual profile must correlate route choices with states and challenges.

## 11. Kempe closure and the four abstract kernels

The abstract closure game has three actors:

1. the current support-unordered state;
2. a complementary support-pair challenge;
3. one of three routing matchings, which chooses the next state.

A profile is Kempe-closed if routing has a memoryless strategy to stay inside it after every challenge.

Exact finite closure leaves four minimal disjoint cap-forced profile-pair kernels. These are finite combinatorial possibilities, not proven realizable four-poles.

Moreover, every state/challenge in each kernel has exactly one safe route. Thus each kernel carries a deterministic routing automaton.

## 12. Two residual routing mechanisms

After simultaneous permutation of the three routing colours and exchange of shores, the four kernel pairs collapse to two dynamical types.

### Type T — tree routing

$$
P_5\mid P_5.
$$

Both shore automata are paths with edge-colour word $abba$ up to symmetry. The intended mechanism is unique or nested terminal linkage, leading to serial decomposition or a smaller separator.

### Type H — routing holonomy

$$
P_4\mid C_3.
$$

One shore is a rainbow triangle. Traversing it induces nontrivial support-index monodromy. The sixteen lifted boundary monodromies have cycle types

$$
2^21,\quad41,\quad32,\quad5
$$

four of each and generate $S_5$.

The boundary holonomy is not itself a contradiction, because support names are gauge data. Its interior lift is the substantive object treated in the holonomy chapter.

## 13. Exact small four-pole census

Every connected cap-admissible cubic four-pole through six internal vertices was enumerated exactly. Among thirty underlying multigraph classes, only eight complete profiles occur:

$$
\mathcal K_i,
\qquad
\mathcal S\setminus\{B_i\},
\qquad
\mathcal S\setminus\{A\},
\qquad
\mathcal S.
$$

Every one contains a complete cap set $\mathcal K_i$.

### Finite corollary

Every shore of a cyclic four-edge cut in a vertex-minimal counterexample has at least eight internal vertices.

The universal statement

$$
\exists i:\mathcal K_i\subseteq\Sigma(P)
$$

for every admissible four-pole remains open. Larger exploratory searches found the same eight profiles but are not exhaustive.

## 14. The full-cap-profile target

The natural theorem target is not “enumerate more profiles”, but:

$$
\boxed{
\text{pairing alignment}
\quad\text{or}\quad
\text{four-pole decomposition}.
}
$$

More explicitly, prove that every minimal-counterexample shore either:

1. has enough aligned support-pair paths to generate a full $\mathcal K_i$; or
2. has systematic misalignment forcing a bounded cut, serial composition, or replaceable fragment.

Either alternative would eliminate the four abstract mismatch kernels.

## 15. Relation to target-side obstruction cores

Four-pole interfaces and marked dual cores are complementary.

- target-side obstruction identifies a finite family of problematic faces;
- its reserve code measures persistence under gauge motion;
- a $K_4$ reserve line yields a three-cut immediately;
- a private core or a repeated $2K_3$ interface leads naturally to a four-pole;
- the four-pole transfer state records what must be preserved under replacement or gluing.

The sought global theorem should translate persistent target obstruction into bounded source-interface data.

## 16. Reliability boundary

The cubic local law, three-cut gluing, reserve-line separation, ten-state classification, signature intersection, cap forcing, pairing-alignment theorem, routing-weight conservation, fixed-routing sectors, and uniform-routing elimination are theorem-level.

The four closure kernels, deterministic-policy tables, two policy-pair orbits, monodromy counts, and small-profile census are exact finite computations. Their realizability and universal full-cap consequences remain open. No current theorem eliminates every cyclic four-edge cut or proves the global five-support statement.