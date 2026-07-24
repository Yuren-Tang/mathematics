# Fixed-channel component-chain candidate

## 1. Status

Exact authorial source:

`Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1@02b37476198e9eaa2b4cd8d2a2edd76782bdcd49`.

Controlling file:

`projects/affine-cdc/research/FIXED_CHANNEL_COMPONENT_CHAIN_ROOT_NNI_THEOREM_V1.md`.

Current class:

`TIER II / RL-AUTHORIAL / PDL RECONSTRUCTION ACTIVE IN #80 / INDEPENDENT REVIEW ACTIVE IN #81`.

Nothing in this chapter freezes the final theorem status.

## 2. Exact object

Fix a complete root-valued cubic state and a support pair $h=ab$. Define

$$
H_h=F_a\triangle F_b.
$$

Every cubic vertex has $H_h$-degree zero or two. The unique inactive support triangle is

$$
I_h=[5]\setminus h.
$$

All other vertices are channel-active.

Let $R$ be the connected physical carrier obtained after cutting the two marked channel edges in the co-root case, or after deleting the active two-vertex cell in the zero-parent case.

The quotient $\mathcal Q_h(R)$ has:

- one node for each nontrivial connected component of $H_h\cap R$;
- one singleton node for each $I_h$ vertex;
- one quotient edge for each physical edge of $R$ outside $H_h$, retaining the exact source edge witness.

Physical connectedness of $R$ implies connectedness of $\mathcal Q_h(R)$.

## 3. Candidate contraction theorem

Choose two distinguished terminal path components $P_0,P_1$ and a shortest simple witnessed quotient path

$$
\mathfrak c=(X_0=P_0,X_1,\ldots,X_\ell=P_1).
$$

The candidate rank is the retained physical path length

$$
\Lambda_h(\mathfrak c)=\ell.
$$

### Inactive first node

If $X_1$ is one inactive vertex, an ordinary root NNI absorbs that vertex into $X_0$. The old channel passage is extended through the vertex, and the next physical quotient edge is claimed to remain available.

### Active closed component

If $X_1$ is a closed $H_h$ component, an active/active root NNI, or in the equal-triangle case the root branch swap, merges it into $X_0$. The later witnessed connectors are claimed to remain available.

### Final connector

When $\ell=1$, the physical non-channel edge joins the two distinguished terminal paths. Its root alternative changes their terminal matching.

Thus every nonterminal step contracts the first retained quotient edge and lowers $\Lambda_h$ by one. The claimed bound is the initial witnessed quotient distance, not a finite-state or SCC distance.

## 4. Co-root corollary

In a fixed co-root rescue channel, cut the two marked channel edges. Their common component becomes two marked arcs. The component-chain candidate selects a connector between those actual arcs, not an arbitrary equal face.

The final matching change gives either:

- a separating channel, consumed by the established horizontal mechanism; or
- the opposite marked route, consumed by the cap/route output.

This is intended to repair the exact same-arc Heawood witness that refuted `Xi` totality.

## 5. Zero-parent corollary

Normalize the equality word to

$$
(A,B,C,D)=(13,13,23,23),\qquad h=35.
$$

The residual full lock has two terminal paths $A--B$ and $C--D$ in $H_{35}\cap R$. The candidate changes the outside matching to a crossed matching. One then:

1. chooses the crossed root sheet with that matching;
2. uses at most one active equal-face root branch swap;
3. switches one closed $H_{35}$ component;
4. obtains active word $(15,13,25,23)$;
5. performs the literal parent NNI with central root $35$.

This is the current authorial repair of the previously omitted zero-parent row.

## 6. Exact nondependencies

The component-chain candidate does not use:

- an arbitrary equal-face route-or-split lemma;
- `Xi` as a total source selector;
- the local/exterior `Omega` orbit-minimum argument;
- a `2--0` cancellation;
- a lower-order call during fixed-order return;
- track erasure as target progress;
- generic root/NNI connectivity;
- finite-state recurrence or SCC distance;
- an abstract quotient distance recomputed after each move without inherited witnesses;
- the old $Q_N,M_N,d_N$ nested-bubble completion route.

## 7. Required independent checks

Issues #80 and #81 control the following questions.

1. Does channel parity really leave exactly one inactive triangle?
2. Do all active/inactive rows preserve root-valuedness and the exact stable darts?
3. In every active/active case, is the claimed root alternative legal, especially for equal endpoint triangles?
4. After the first contraction, do all later physical connectors inherit literally, rather than merely exist anew?
5. Does the final connector necessarily change the matching of the distinguished paths?
6. Are disconnected-carrier cases exhausted by named cut/bounded outputs?
7. Do cap, route, graph category, parent topology and stored prefix survive each move?
8. Does the zero-parent crossed-sheet/switch/parent sequence preserve all labels and ordered incidences?
9. Does the co-root corollary avoid every same-arc form of the audit witness?
10. Does full inverse-table integration introduce no unranked reset or unconsumed exit?

## 8. Status switch

- Both reviews pass: replace this header by exact independently supported SHAs.
- Bounded repair: retain this source as provenance and point to the repaired statement.
- Material failure: classify this as a failed candidate and restore component-chain return to the active frontier.

The rest of AC-CORPUS-V2 remains valid under all three outcomes.