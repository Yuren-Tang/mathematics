# AC-PD-B5.2 — cap forcing and Kempe pairing alignment

**Proof-development state:** `COMPLETE-DRAFT / FRONTIER-EXPLICIT`  
**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Exact initial corpus base:** `main@960c92b7ff231c78b387894149779083060a75eb`  
**Validated sources:** `FIVE_CDC_FOUR_EDGE_CAP_FORCING_KERNELS_V1.md` and `FIVE_CDC_CAP_KEMPE_PAIRING_ALIGNMENT_V1.md`  
**Depends on:** B5.1 ten-state alphabet and cap sets  
**Immediate consumers:** B5.3 routing weights and closure; B6 decomposition/holonomy  
**External mathematical inputs:** none

## 0. Minimal-counterexample setting

Let $G$ be a vertex-minimal bridgeless cubic loopless multigraph without an indexed five-support even double cover. Let a cyclic four-edge cut have shore four-pole $P$ with labelled terminals $1,2,3,4$.

Write

$$
\Sigma(P)\subseteq\mathcal S
$$

for its complete boundary profile and

$$
\Pi(P)=\Sigma(P)\cap\{B_i,D_i:i=0,1,2\}
$$

for its standard-cap profile.

For cap matching $M_i$, B5.1 gives

$$
\mathcal K_i=\{B_j,D_j:j\ne i\}.
$$

## 1. Bridgeless cap completion

Attach the standard two-vertex cap for $M_i$.

### Lemma 1.1

Every cap completion $P^{M_i}$ is a connected bridgeless cubic loopless multigraph.

### Proof

Cubicity, connectedness, and looplessness are immediate. For the cap edge, choose one terminal endpoint in each cap block and connect them by a path inside the connected shore; adjoining the two terminal edges and cap edge gives a cycle.

For a terminal edge, use a cycle through the corresponding original cut edge in the bridgeless ambient graph. Its shore segment joins that terminal to another boundary terminal and closes through the cap.

For an internal shore edge, use an ambient cycle through it. If the cycle leaves the shore, its maximal shore segment containing the edge has two boundary endpoints and closes through the cap. $\square$

Since the opposite shore is cyclic, it has at least four vertices; therefore adding two cap vertices produces a graph strictly smaller than $G$.

## 2. Cap forcing

### Theorem 2.1

For every cap matching $M_i$,

$$
\boxed{
\Pi(P)\cap\mathcal K_i\ne\varnothing.}
$$

Equivalently, $\Pi(P)$ contains states with at least two distinct matching indices.

### Proof

The completion $P^{M_i}$ is smaller, bridgeless, cubic, and loopless. By vertex minimality it has a five-support cover. Restricting to $P$ gives one of the four cap states in $\mathcal K_i$.

A subset of the six prism states meets all three $\mathcal K_i$ exactly when its matching-index projection has size at least two. $\square$

### Corollary 2.2

Every cap-forced profile contains a minimal two-state witness

$$
\{X_i,Y_j\},
\qquad
X,Y\in\{B,D\},\quad i\ne j.
$$

There are twelve such minimal profiles.

This theorem does not imply that any complete set $\mathcal K_i$ lies in $\Sigma(P)$.

## 3. Disjointness across a counterexample cut

If $Q$ is the opposite shore, B5.1 gives

$$
\boxed{
\Sigma(P)\cap\Sigma(Q)=\varnothing.}
$$

Hence $\Pi(P)$ and $\Pi(Q)$ are disjoint cap-forced subsets of the triangular-prism state set. Selecting one minimal two-state witness on each shore yields a finite mismatch kernel; orbit enumeration of such pairs is certificate/computation data, not needed for cap forcing itself.

## 4. Support-pair symmetric difference

Fix a capped cover and two support indices $a,b$ whose boundary traces differ at all four terminals. Put

$$
X_{ab}=F_a\triangle F_b.
$$

Inside the closed capped graph, $X_{ab}$ is an even subgraph. Inside the four-pole, every internal vertex has degree zero or two in $X_{ab}$, while all four boundary terminals have degree one. Therefore the boundary-connected part is two terminal paths, defining one perfect matching

$$
M_P(a,b)
$$

of the terminals. Internal cycle components do not affect this pairing.

## 5. Cap pairing

Let the cap matching be

$$
M_i=12\mid34.
$$

### Lemma 5.1

Inside the cap, $X_{ab}$ consists of the two paths

$$
1-x-2,
\qquad
3-y-4,
$$

and does not use the cap edge.

### Proof

At each cap vertex, both terminal edges lie in the symmetric difference because the traces of $a,b$ differ there. They already give degree two, so evenness excludes the cap edge. $\square$

## 6. Alignment dichotomy

### Theorem 6.1 — cap/Kempe pairing alignment

There are two cases.

#### Aligned

If

$$
M_P(a,b)=M_i,
$$

then the boundary-connected part of $X_{ab}$ in the capped graph consists of two separate cycles, one for each cap block. Switching the names $a,b$ on exactly one of these cycles preserves the five-support cover and changes the traces on exactly one block of $M_i$.

For a standard-cap state, this produces a distinct support-unordered cap state.

#### Misaligned

If

$$
M_P(a,b)\ne M_i,
$$

then the shore matching and cap matching form one four-cycle. All four terminals lie on one component of $X_{ab}$. Switching $a,b$ on that component transposes their names at all four terminals, so the support-unordered boundary state is unchanged.

### Proof

Equal perfect matchings form two doubled terminal pairs; distinct perfect matchings form one simple four-cycle. A Kempe switch on one connected component of a support-pair symmetric difference preserves evenness and exact edge multiplicity by exchanging the two support memberships on that component.

In the aligned case, choosing one of the two components affects only one terminal block and cannot be a global transposition. In the misaligned case, the unique boundary component affects all four terminals and is precisely the global boundary transposition of $a,b$. $\square$

Thus, for a specified support pair,

$$
\boxed{
\text{a nontrivial cap-state transition is available}
\quad\Longleftrightarrow\quad
M_P(a,b)=M_i.}
$$

## 7. Exact trace update

In the aligned case, if $P_i$ is one block of $M_i$, then

$$
(\partial F_a,\partial F_b)
\longmapsto
(\partial F_a\triangle P_i,
 \partial F_b\triangle P_i).
$$

Using the complementary block gives the same support-unordered target state. This finite update determines the abstract ten-state Kempe transition table; the pairing theorem determines whether a listed transition is actually realizable in a given four-pole cover.

## 8. Why full-cap closure is open

Minimality supplies one state in every $\mathcal K_i$, but does not control the shore matchings $M_P(a,b)$. If all relevant support-pair paths are misaligned, all corresponding switches are only global support-name transpositions.

Therefore

$$
\Sigma(P)\cap\mathcal K_i\ne\varnothing
$$

does not by itself imply

$$
\mathcal K_i\subseteq\Sigma(P).
$$

The missing structural alternative is:

1. sufficient pairing alignment to generate a full cap set; or
2. systematic misalignment forcing a bounded cut, serial composition, or replaceable four-pole fragment.

This is a genuine source-routing question.

## 9. Assurance boundary

Bridgeless cap completion, cap forcing, profile disjointness, terminal-path pairing, and the alignment dichotomy are theorem-level. The finite orbit count of mismatch kernels, their realizability, and the universal full-cap theorem remain separate.

## 10. Completion assessment

`AC-PD-B5.2` is `COMPLETE-DRAFT / FRONTIER-EXPLICIT`. The next active unit is B5.3: prove the routing-weight coordinate system and fixed-route transition sectors, then classify exactly which later kernel/automaton statements are theorem-level and which are finite certificates.