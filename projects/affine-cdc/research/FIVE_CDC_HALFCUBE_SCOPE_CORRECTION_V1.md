# Scope correction — factorable half-cube compression and connected-cycle adjacency

**Programme:** `AffineCDC — Research Lead`  
**Status:** controlling research-branch correction; the finite graph theorems and computations remain valid in their corrected scopes  
**Supersedes:** the broad compression interpretation in `FIVE_CDC_HALFCUBE_SUBGRAPH_CLASSIFICATION_V1.md` and the use of “adjacent” for all `7737` binary-cycle switches in `FIVE_CDC_SUPPORT_CYCLE_PIVOT_AND_FLOW_RECONFIGURATION_V1.md`

## 1. Half-cube classification scope

The theorem

\[
J\to\mathscr A_5
\iff
K_6\nsubseteq J
\text{ and }
K_8-C_5\nsubseteq J
\]

is correct for every spanning subgraph `J\subseteq K_8`.

For a root lift `g`, applying it to the used-index graph `J_g` classifies exactly those five-support constructions whose half-cube potential is constant on every cycle component carrying the same old support index. Equivalently, it classifies maps

\[
T_g\to J_g\to\mathscr A_5
\]

that factor through the global eight-color quotient.

It does **not** classify all componentwise maps

\[
T_g\to\mathscr A_5.
\]

The latter is the correct same-embedding criterion and may succeed even when `J_g` contains `K_6` or `K_8-C_5`.

Therefore every statement in the parent packet that says simply

> `g` compresses to five supports if and only if `J_g\to\mathscr A_5`

must be read as

> `g` admits a global-index-factorable compression if and only if `J_g\to\mathscr A_5`.

The underlying eight-vertex graph classification, conflict-graph proof, Clebsch calculations, and positive templates remain unchanged.

## 2. Defect-core scope

The two-apex, pentagon, and one-star defect-core theorems remain exact for the global-index-factorable route. They describe the complement of the used **color quotient**.

They are not complete obstructions to a componentwise half-cube potential on the full dual triangulation. A lift may be quotient-bad but componentwise-good.

The defect-core programme therefore remains:

- a finite sufficient route to five supports;
- a useful quotient-level recoloring theory;
- a source of explicit support-pivot moves;

but not the full fixed-lift obstruction theory.

## 3. Binary-cycle switches versus reconfiguration edges

For a nonzero `a\in\mathbf F_2^3`, every nonzero word

\[
z\in\mathcal C(G-E_a)
\]

defines a nowhere-zero rank-one tensor switch

\[
f\mapsto f+a z.
\]

In a cubic graph, the support of `z` is a disjoint union of connected source cycles. If it has more than one component, the switch is a composition of the corresponding connected-cycle switches.

Hence:

- **connected-cycle switch:** one edge of the nowhere-zero flow reconfiguration graph;
- **general binary-cycle switch:** a commuting multi-edge move, or a path obtained by switching its connected components successively.

For the thirty-vertex fixed obstruction:

\[
7737
\]

is the number of all nonzero pairs `(a,z)`, while exactly

\[
2801
\]

have connected support and are genuine single-edge reconfiguration neighbours.

All future reports separate these two populations.

## 4. Corrected strategic hierarchy

The relevant levels are now:

1. quotient-factorable compression `J_g\to\mathscr A_5`;
2. componentwise same-embedding compression `T_g\to\mathscr A_5`;
3. code-filtered partial-Petrial changes of `T_g` inside one gauge fibre;
4. connected-cycle reconfiguration of the Fano flow;
5. compositions of connected-cycle moves, including general binary-cycle switches.

No claim in this correction proves five-support existence. It narrows prior statements to their exact trust boundaries and exposes the larger componentwise freedom.
