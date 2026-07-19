# AffineCDC current mathematical state

This file gives the compact current-best mathematical picture after the deep corpus reconstruction. It is not a replacement for the proofs or the exact source packets.

## 1. Complete result line

At paper level, the project has a complete Cycle Double Cover spine:

$$
\text{finite-active-edge bridgeless multigraph}
\longrightarrow
\text{cycle double cover}.
$$

The proof architecture separates:

1. loop deletion and reinsertion;
2. an outer cubic binary-flow construction;
3. rank-three affine compatibility;
4. graph-level even-cover extraction;
5. cut-even collapse transport;
6. one final circuit decomposition.

The natural theorem allows loops and uses finite active edge set. The current Lean checkpoint is earlier, loopless, and ambient-finite; the unconditional endpoint is not yet machine-checked.

## 2. Five-support object

The open strengthening asks for five indexed even supports. This is equivalent to a root-valued flow

$$
E(G)\to R_5\subset E_5,
$$

or to a $K_5$ triangle labelling, matching/four-flow structure, quadratic-cycle solution, or cographic map.

Above any cubic Fano flow, a compatible eight-support root lift exists. The five-support problem asks whether one can choose the flow and lift so that the cycle-face dual triangulation maps to the half-cube:

$$
\boxed{T_g^{(1)}\to\mathscr A_5.}
$$

The global-colour quotient $J_g\to\mathscr A_5$ is only the factorable subroute.

## 3. Closed theorem blocks

The current durable backbone includes:

- fixed-plane component-parity/singular-quotient criterion;
- Schur, stress, Fourier, and colour-cut equivalents;
- root-lift/surface/dual correspondence;
- exact factorable $K_6/K_8-C_5$ classification in its corrected scope;
- dominating-clique target capacity for ranks two through five;
- gauge/Petrial equivalence and marked-core affine occurrence loci;
- internal/external flow-switch dichotomy;
- three-edge-cut gluing;
- ten-state four-edge boundary theory;
- cap forcing, Kempe pairing, routing coordinates, and uniform-routing elimination;
- reduction of abstract four-cut kernels to Type T and Type H;
- cyclic affine holonomy and root-fibre section theory;
- Tait resolution and elimination of the soluble Type H branch;
- BBD simultaneous origin, $K_6$ completion, and defect-strip geometry;
- induced defect forests and Petersen transport;
- DDD atom triality and unique bad route;
- rank-two Tait escape;
- full-rank curvature/common-cut duality and flat-potential equivalence.

## 4. Controlling negative boundaries

The following overstrong statements are false or unsupported:

- every fixed Fano flow has a five-support lift;
- $J_g$ is the complete fixed-lift object;
- $K_6$-free implies a half-cube map;
- a bad fixed-flow fibre makes the graph bad;
- every binary-cycle switch is one horizontal adjacency;
- route-lock forces a graph two-cut;
- route-lock is automatically flat;
- repeated Petersen state implies a replaceable strip;
- a finite census proves universal closure.

## 5. Current sharp frontier

For a blocked co-root atom, unique-bad-route reduction gives a locked quotient flow with equal terminal colour and four scalar circuit partitions.

- rank two escapes by a Tait lift;
- full rank with $\Omega\ne0$ gives a support-minimal common-cut witness $\eta\subseteq E_g$ with odd terminal parity;
- full rank with $\Omega=0$ gives an eight-state affine potential.

The immediate missing theorem must convert these outputs into a bounded DDD/Petersen factor, smaller separator, transition split, finite four-pole transfer state, or profile/orbit escape.

At the wider level, the remaining bridges are:

1. Type T unique-linkage decomposition;
2. Type H translation/zero/oddness reduction;
3. full-cap-profile or realizability theorem for four-poles;
4. horizontal escape-or-decomposition for bad-flow components;
5. a controlled target-certificate language beyond dominating cliques.

## 6. Exact source and assurance state

The reconstruction uses:

- canonical base `main@749e0579581fcc838685138b3582f4de306b8e72`;
- accepted MP2 source `0927011177cabac20f06a57fa5e57476d6f13dee`;
- complete public five-support checkpoint `dad218dd18ed05d1b7cb730c2dc2431b4db5ec9c`;
- exact reconstruction base `7a166d2eb5642ec967f640323488e49f1c2ad5d4`.

All public research packets remain in place. This reconstruction changes navigation and synthesis only; it does not add independent audit, Lean verification, peer review, manuscript, release, DOI, arXiv, or theorem-completeness status.

## 7. Reading order

- architecture: [`MATHEMATICAL_ARCHITECTURE.md`](MATHEMATICAL_ARCHITECTURE.md);
- theorem graph: [`THEOREM_DEPENDENCY_MAP.md`](THEOREM_DEPENDENCY_MAP.md);
- five-support corpus: [`five-support/README.md`](five-support/README.md);
- exact frontier: [`FRONTIER_STATUS.md`](FRONTIER_STATUS.md);
- reliability: [`FORMAL_STATUS.md`](FORMAL_STATUS.md).