# AC-PD-B5 — cuts, four-poles, and routing hierarchy

**Proof-development state:** `READY-FOR-CURATOR / FRONTIER-LOCALIZED`  
**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Exact initial corpus base:** `main@960c92b7ff231c78b387894149779083060a75eb`  
**Constituent units:** B5.1–B5.3  
**External mathematical inputs:** none  
**Assurance:** complete authorial proof-development checkpoint for the separator/interface layer; residual Type T/H mechanisms remain open

## 0. Separator hierarchy

The five-support source-side decomposition programme has three levels.

1. Three-edge interfaces: one local support pattern, automatic gluing.
2. Four-edge interfaces: ten labelled-terminal states, gluing by exact profile intersection.
3. Routing refinement: an abstract state transition is realizable only when the internal four-terminal path pairing matches the chosen route.

## 1. Cubic local law

At a cubic vertex, exactly one support uses each incident-edge pair. Therefore three distinct support indices occur locally and two are absent.

This unique law yields exact gluing across cyclic three-edge cuts.

## 2. Three-cut reduction

If both cyclic shores of a three-edge cut are completed by one cubic boundary vertex, the completions are bridgeless cubic loopless multigraphs. Covers of the two completions can be aligned by one support permutation and glued.

Hence a vertex-minimal counterexample is cyclically four-edge-connected.

A connected marked core with a $K_4$ harmonic reserve direction lies behind such a cyclic three-cut, so these reserve lines are decomposition certificates rather than irreducible atoms.

## 3. Four-edge alphabet

With labelled terminals and support order forgotten, the exact state set is

$$
\mathcal S=\{A,B_i,C_i,D_i:i=0,1,2\}.
$$

- $A$: two full traces;
- $B_i$: one full trace plus matching $M_i$;
- $C_i$: doubled matching $M_i$;
- $D_i$: four-cycle whose missing matching is $M_i$.

There are 640 ordered five-support assignments. Terminal permutation reduces the ten states to four types $A,B,C,D$.

## 4. Exact four-cut gluing

For a four-pole $P$, let $\Sigma(P)\subseteq\mathcal S$ be its labelled-terminal, support-unordered profile. Two shores glue exactly when

$$
\Sigma(P)\cap\Sigma(Q)\ne\varnothing.
$$

Terminal labels must remain fixed until the corresponding original cut edges are glued.

## 5. Standard caps and minimality

For cap matching $M_i$, the exact cap state set is

$$
\mathcal K_i=\{B_j,D_j:j\ne i\}.
$$

In a vertex-minimal counterexample every shore profile meets every $\mathcal K_i$. Equivalently its B/D matching-index projection has size at least two.

The two shore profiles remain disjoint. Minimal two-state cap witnesses and their orbit kernels are finite certificate data; cap forcing itself is theorem-level.

## 6. Pairing alignment

For complementary supports $a,b$, the boundary-connected part of

$$
F_a\triangle F_b
$$

inside a four-pole consists of two terminal paths and determines one matching $M_P(a,b)$.

In a cap with matching $M_i$:

- if $M_P(a,b)=M_i$, the symmetric difference splits into two cap-shore cycles; switching one changes one boundary block and gives a new support-unordered state;
- if $M_P(a,b)\ne M_i$, there is one four-terminal cycle; switching it is only a global boundary transposition of $a,b$.

Thus state-table closure does not imply actual closure unless the required path pairing is realized.

## 7. Routing-weight coordinates

The ten states embed injectively in $\{0,1,2\}^3$ by

$$
\omega_i
=\frac12\sum_r |S_r\cap X_i|\pmod2.
$$

A switch routed by $M_i$ preserves exactly the coordinate $\omega_i$. The fixed-routing transition graph is

$$
\mathcal G_i\cong P_3\sqcup C_4\sqcup P_3,
$$

with middle component $\mathcal K_i$.

The union of two distinct routing-colour graphs is connected on all ten states.

## 8. Uniform-routing elimination

If a four-pole is globally routed by one matching $M_i$, its profile is a union of $\mathcal G_i$ components. Cap forcing then forces the whole middle component

$$
\mathcal K_i\subseteq\Sigma(P),
$$

which necessarily intersects the opposite shore profile. Therefore no shore of an irreducible cyclic four-cut is globally routed by one matching.

## 9. Certificate layer

The following remain exact finite classifications requiring their tables/verifiers:

- six minimal cap-forcing witness-pair orbits before Kempe closure;
- four minimal Kempe-closed mismatch kernels;
- unique routing policy at every kernel state/challenge;
- two policy-pair types $P_5\mid P_5$ and $P_4\mid C_3$;
- sixteen boundary monodromies and their cycle types;
- the small four-pole profile census.

Their realizability and universal consequences are not supplied by the theorem layer alone.

## 10. Localized frontier

All uniform routing is eliminated. The residual mechanisms are:

1. **Type T:** acyclic unique routing, expected to force nested linkage, serial composition, or a smaller separator;
2. **Type H:** rainbow routing holonomy, requiring an interior affine/flow lift rather than a boundary-name contradiction.

The exact unresolved structural alternative is:

$$
\boxed{
\text{sufficient pairing alignment}
\quad\text{or}\quad
\text{bounded four-pole decomposition}.}
$$

B6 receives these two mechanisms together with the certified kernel automata.

## 11. Assurance boundary

Three-cut gluing, ten-state classification, signature intersection, cap forcing, pairing alignment, routing coordinates, fixed-route sectors, and uniform-routing elimination are theorem-level. Kernel, monodromy, and census tables remain certificate data. No theorem here eliminates every cyclic four-cut or proves the global five-support result.

## 12. Completion assessment

`AC-PD-B5` is `READY-FOR-CURATOR / FRONTIER-LOCALIZED`. B6 becomes active.