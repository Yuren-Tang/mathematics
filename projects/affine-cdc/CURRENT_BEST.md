# AffineCDC current mathematical state

This file gives the compact current-best picture after substantive reconstruction and current-tree retirement. Proofs live in the active chapters; exact historical packets remain recoverable from Git.

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

The natural theorem allows loops and finite active edge set. The current Lean checkpoint is earlier, loopless, and ambient-finite; the unconditional endpoint is not yet machine-checked.

## 2. Five-support object

The open strengthening asks for five indexed even supports. This is equivalent to a root-valued flow

$$
E(G)\longrightarrow R_5\subset E_5,
$$

or to a `K_5` triangle labelling, matching/four-flow structure, quadratic-cycle solution, or cographic map.

Above any cubic Fano flow, a compatible eight-support root lift exists. The complete fixed-lift target is

$$
\boxed{T_g^{(1)}\longrightarrow\mathscr A_5.}
$$

The quotient `J_g -> A_5` is only the global-index-factorable subroute.

## 3. Durable closed blocks

The current backbone includes:

- fixed-plane component parity and its singular, Schur, stress/Fourier, and colour-cut forms;
- root-lift/surface/dual correspondence;
- exact factorable half-cube classification in corrected scope;
- dominating-clique target capacity for ranks two through five;
- gauge/Petrial equivalence and affine occurrence loci for marked certificates;
- connected-cycle horizontal motion and the internal/external switch dichotomy;
- three-edge-cut gluing and the ten-state four-edge interface;
- cap forcing, Kempe pairing, routing coordinates, and Type T/Type H reduction;
- affine holonomy, root-fibre section theory, Tait resolution, and elimination of the soluble Type H branch;
- BBD common origin, canonical defect flow, `K_6` completion, induced defect forests, and Petersen transport;
- DDD atom triality, unique bad route, and rank-two Tait escape;
- full-rank curvature/common-cut duality and flat-potential equivalence;
- common-cut component incidence, odd witness circuits, and the singleton/transition/quartic-core localisation trichotomy;
- unbounded abstract quartic witness designs and their symplectic cross-intersection form;
- the quotient Tait-phase representation of route-locked flows, the affine plane of four scalar sheets, and complete aligned/crossed endpoint switch signatures.

## 4. Controlling negative boundaries

The following are false or unsupported:

- every fixed Fano flow has a five-support lift;
- `J_g` is the complete fixed-lift object;
- `K_6`-free implies a half-cube map;
- a bad fixed-flow fibre makes the graph bad;
- every binary-cycle switch is one horizontal adjacency;
- route-lock forces a graph two-cut or automatic flatness;
- a scalar-common-cut witness must be a cut in the underlying four-pole;
- repeated Petersen state implies a replaceable strip;
- finite census proves universal closure;
- the quartic near-resolution and rank axioms bound the residual common-cut core.

The physical-cut statement is explicitly false: the exact nonflat singleton witness is a common cut in all four scalar sheets while its unique witness edge is not a bridge of the underlying graph.

The abstract quartic branch is genuinely unbounded: for every `k\ge1` there is a quartic witness design on `4k+1` points satisfying all incidence-level near-resolution, rank, omitted-point, and odd-side constraints. Any bound must therefore use physical flow compatibility.

## 5. Sharp frontier

For a blocked co-root atom, unique-bad-route reduction gives a locked quotient flow with equal terminal colour and four scalar circuit partitions.

- rank two escapes through a Tait lift;
- full rank with zero curvature gives an eight-state affine potential;
- full rank with nonzero curvature gives a support-minimal curvature-odd circuit in the four-partite closed-component incidence matroid.

The nonflat circuit has exactly three possible forms:

1. a singleton enriched `g`-edge atom;
2. a closed scalar component meeting the witness in two edges, hence a marked transition interval;
3. a quartic near-resolution core of size `4k+1`, with one terminal witness edge per sheet and independent four-edge closed-component blocks.

The singleton is either aligned, with resolution labels `g,g,0`, or crossed, with DDD/Petersen resolution labels `g,r,r+g`.

The quartic incidence axioms alone cannot reduce case 3. Physical route-lock adds the exact quotient-phase structure:

1. after quotient by `\langle g\rangle`, the flow is a degenerate `\mathbf F_2^2` Tait flow whose zero edges are exactly `E_g`;
2. one binary phase reconstructs the full `\mathbf F_2^3` flow;
3. the four scalar sheets form an affine plane, and their three nonzero differences are quotient Kempe cycle systems;
4. every `g`-edge carries one of nine ordered endpoint quotient labels;
5. aligned edges have switch signatures `(0,0),(1,1),(1,1)`, while crossed edges have `(0,1),(1,0),(1,1)`.

The immediate missing theorem must:

1. compose an aligned zero/equality-wire singleton or crossed DDD singleton;
2. convert a two-edge scalar interval into a smaller separator, transition split, finite four-pole transfer state, or bounded replacement;
3. classify or decompose enriched quartic phase designs using cyclic orders, quotient labels, Kempe cycle differences, and intervening path data;
4. extract a finite interface from the flat potential.

Wider open bridges are:

1. defect-forest pruning;
2. Type T unique-linkage decomposition;
3. residual Type H translation/zero/oddness reduction;
4. full-cap-profile or realizability theorem;
5. horizontal escape-or-decomposition for bad-flow components;
6. target-certificate completion beyond dominating cliques.

## 6. Source and active-surface state

The synthesis uses:

- canonical ancestor `main@749e0579581fcc838685138b3582f4de306b8e72`;
- accepted outer-shell source `0927011177cabac20f06a57fa5e57476d6f13dee`;
- complete public five-support checkpoint `dad218dd18ed05d1b7cb730c2dc2431b4db5ec9c`;
- reconstruction base `7a166d2eb5642ec967f640323488e49f1c2ad5d4`;
- completed corpus migration `960c92b7ff231c78b387894149779083060a75eb`;
- later active Research Lead frontier commits on `research/affine-cdc-five-cdc-v1`.

The seventy-eight discovery-order source packets are retired from the current tip after exact successor mapping. They remain ancestors and are recoverable from `dad218dd...`; they are not the active reading surface.

See:

- [`ACTIVE_MATHEMATICAL_SURFACE.md`](ACTIVE_MATHEMATICAL_SURFACE.md);
- [`CHAPTER_PROVENANCE.md`](CHAPTER_PROVENANCE.md);
- [`RETIRED_SOURCE_CLASSIFICATION.md`](RETIRED_SOURCE_CLASSIFICATION.md);
- [`SOURCE_RECOVERY_AUDIT.md`](SOURCE_RECOVERY_AUDIT.md).

## 7. Assurance state

The corpus separates theorem-level arguments, exact finite results, counterexamples, corrections, and open programmes. Current-best inclusion and Research Lead checkpointing do not add independent review, Lean verification, peer review, manuscript approval, release, DOI, arXiv, or publication status.

## 8. Reading order

- architecture: [`MATHEMATICAL_ARCHITECTURE.md`](MATHEMATICAL_ARCHITECTURE.md);
- theorem graph: [`THEOREM_DEPENDENCY_MAP.md`](THEOREM_DEPENDENCY_MAP.md);
- active surface: [`ACTIVE_MATHEMATICAL_SURFACE.md`](ACTIVE_MATHEMATICAL_SURFACE.md);
- five-support corpus: [`five-support/README.md`](five-support/README.md);
- common-cut localisation: [`five-support/common-cut-circuit-localisation.md`](five-support/common-cut-circuit-localisation.md);
- quartic designs: [`five-support/quartic-witness-designs.md`](five-support/quartic-witness-designs.md);
- quotient phase: [`five-support/route-locked-quotient-phase.md`](five-support/route-locked-quotient-phase.md);
- exact frontier: [`FRONTIER_STATUS.md`](FRONTIER_STATUS.md);
- reliability: [`FORMAL_STATUS.md`](FORMAL_STATUS.md).