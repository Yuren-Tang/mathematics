# AffineCDC current-best rolling baseline

This file is the default mathematical entrypoint for the temporary rolling-baseline candidate

`integration/affine-cdc-best-baseline-dad218dd-v1`.

It combines two exact public sources without upgrading either source's assurance status:

- accepted outer-shell MP2: `0927011177cabac20f06a57fa5e57476d6f13dee`;
- complete public five-support frontier checkpoint: `dad218dd18ed05d1b7cb730c2dc2431b4db5ec9c`.

Inclusion here means **current mathematical relevance and exact provenance**. It does not mean independent line-by-line audit, Lean verification, peer review, publication readiness, or acceptance of a global five-cycle-double-cover theorem.

## 1. Two related but distinct theorem lines

### 1.1 Complete CDC existence spine at paper level

The accepted outer-shell line targets the full finite-active-edge multigraph theorem:

> Every multigraph with finite active edge set and no bridges has a cycle double cover.

Its present paper-level architecture is

$$
\begin{array}{c}
\text{bridgeless multigraph with finite active edge set}\\
\downarrow\;\text{delete loops}\\
\text{loopless bridgeless core}\\
\downarrow\\
\text{cubic rank-three flow object}\\
\downarrow\\
\text{rank-three affine compatibility}\\
\downarrow\\
\text{graph-level multiset even double cover}\\
\downarrow\\
\text{cut-even collapse transport}\\
\downarrow\\
\text{one circuit decomposition}\\
\downarrow\;\text{reinsert two singleton circuits per loop}\\
\text{cycle double cover}.
\end{array}
$$

Two exact outer routes are retained:

1. expansion first, then an isolated classical binary-eight-flow input;
2. adaptive flow first, then a flow-preserving cubic expansion.

The adaptive route is the preferred concise Paper A proof; the expansion-first route is the selected first Lean implementation route. Neither route, the outer shell, Seymour--Tutte input, nor the unconditional endpoint currently inherits Lean status.

**Controlling files:**

- [`reduction/outer-shell-and-binary-flow.md`](reduction/outer-shell-and-binary-flow.md);
- [`reduction/even-cover-and-collapse.md`](reduction/even-cover-and-collapse.md);
- [`core/affine-incidence-and-obstruction.md`](core/affine-incidence-and-obstruction.md);
- [`core/rank-three-fano-compatibility.md`](core/rank-three-fano-compatibility.md);
- [`FORMAL_STATUS.md`](FORMAL_STATUS.md);
- [`PUBLICATION_PROGRAM.md`](PUBLICATION_PROGRAM.md).

### 1.2 Five-support strengthening

For a bridgeless cubic graph $G$, choose a nowhere-zero Fano flow $f$. Compatible affine root lifts form gauge/Petrial fibres. A root lift $g$ determines a cycle-face embedding and a closed dual triangulation $T_g$.

The current five-support criterion is

$$
\boxed{T_g^{(1)}\longrightarrow\mathscr A_5,}
$$

where $\mathscr A_5$ is the even half-cube. Existence of such a map gives a five-support cycle double cover. The programme asks whether some choice of flow and compatible lift always succeeds.

No file in this candidate proves that global statement.

## 2. Current five-support mechanism diagram

$$
\boxed{
\begin{array}{c}
G\text{ bridgeless cubic}\\
\downarrow\\
\text{nowhere-zero Fano flows }f\\
\downarrow\\
\text{fixed-flow gauge/partial-Petrial fibres }B_f\\
\downarrow\\
\text{compatible cycle-face embeddings and duals }T_g\\
\downarrow\\
T_g^{(1)}\to\mathscr A_5\ ?
\end{array}}
$$

Failure is processed through two interacting structural channels.

### Target channel

$$
\text{dominating clique}
\longrightarrow
\text{half-cube link}
\longrightarrow
\text{exact capacity test}.
$$

### Source-decomposition channel

$$
\text{harmonic reserve / marked core}
\longrightarrow
\text{edge-cut or four-pole interface}
\longrightarrow
\text{finite boundary-signature compatibility}.
$$

A connected-cycle switch changes the Fano flow and hence changes the available partial-Petrial code and both channels. A gauge move keeps the Fano flow fixed and changes the embedding by an admissible partial Petrial. A support-cycle pivot keeps the uncoloured dual triangulation fixed and changes its old support colouring.

**Controlling synthesis:**
[`research/FIVE_CDC_MECHANISM_CLOSURE_MAP_V1.md`](research/FIVE_CDC_MECHANISM_CLOSURE_MAP_V1.md).

## 3. Universal theorem backbone

The following statements are presented in the checkpoint as universal theorem-level mathematics, rather than conclusions extrapolated from one laboratory.

### 3.1 Root lifts, surfaces, and the true compression object

- root lifts are equivalent to properly face-coloured cycle-face embeddings;
- dually they give properly vertex-coloured closed triangular cellulations;
- the correct same-embedding test is $T_g^{(1)}\to\mathscr A_5$;
- the older colour-quotient test $J_g\to\mathscr A_5$ is exactly the stricter global-index-factorable subclass.

**Files:**

- [`research/FIVE_CDC_COLORED_SURFACE_DUAL_HALFCUBE_V1.md`](research/FIVE_CDC_COLORED_SURFACE_DUAL_HALFCUBE_V1.md);
- [`research/FIVE_CDC_HALFCUBE_SCOPE_CORRECTION_V1.md`](research/FIVE_CDC_HALFCUBE_SCOPE_CORRECTION_V1.md);
- [`research/FIVE_CDC_GAUGE_PARTIAL_PETRIAL_CORRESPONDENCE_V1.md`](research/FIVE_CDC_GAUGE_PARTIAL_PETRIAL_CORRESPONDENCE_V1.md).

### 3.2 Fixed-flow and graph-level obstruction are different quantifiers

A bad lift, or even an entirely bad gauge fibre over one Fano flow, is not a bad graph. Graph-level failure would require every nowhere-zero Fano flow to have an entirely bad lift fibre. The thirty-vertex fixed-flow laboratory is explicitly three-edge-colourable and therefore has a three-support CDC despite containing several bad fixed-flow fibres.

**File:**
[`research/FIVE_CDC_FIXED_FLOW_GRAPH_LEVEL_SEPARATION_V1.md`](research/FIVE_CDC_FIXED_FLOW_GRAPH_LEVEL_SEPARATION_V1.md).

### 3.3 Finite source interfaces

- every weight-six $K_4$ reserve line behind a connected marked core exposes a cyclic three-edge cut and is therefore excluded from a vertex-minimal counterexample;
- a four-pole has a ten-state support-unordered boundary alphabet;
- gluing across a four-edge cut is signature-set intersection;
- cap forcing and support-Kempe switching impose finite closure rules;
- dominating cliques of ranks two through five are decided by an exact chromatic-capacity formula.

**Files:**

- [`research/FIVE_CDC_K4_RESERVE_LINE_THREE_CUT_REDUCTION_V1.md`](research/FIVE_CDC_K4_RESERVE_LINE_THREE_CUT_REDUCTION_V1.md);
- [`research/FIVE_CDC_FOUR_EDGE_BOUNDARY_SIGNATURES_V1.md`](research/FIVE_CDC_FOUR_EDGE_BOUNDARY_SIGNATURES_V1.md);
- [`research/FIVE_CDC_FOUR_EDGE_CAP_FORCING_KERNELS_V1.md`](research/FIVE_CDC_FOUR_EDGE_CAP_FORCING_KERNELS_V1.md);
- [`research/FIVE_CDC_FOUR_POLE_KEMPE_CLOSURE_V1.md`](research/FIVE_CDC_FOUR_POLE_KEMPE_CLOSURE_V1.md);
- [`research/FIVE_CDC_DOMINATING_CLIQUE_EXACT_CAPACITY_V1.md`](research/FIVE_CDC_DOMINATING_CLIQUE_EXACT_CAPACITY_V1.md).

### 3.4 Atom resolution and the locked sector

For a nondegenerate one-edge co-root atom:

1. its three terminal pairings are one co-root realization and two root-valued resolutions;
2. for every full challenge, the original atom route is the unique route that stays bad;
3. if a crossed route occurs, the defect becomes root-valued;
4. if every challenge uses the original route, the atom is in universal route-lock and has a canonical $\mathbf F_2^3$ challenge quotient;
5. route-lock does not imply a graph-theoretic two-edge separation;
6. rank two forces a Tait three-edge-colouring and admits a root-valued $A$-state escape;
7. only the full-rank locked sector survives;
8. nonzero curvature has a support witness $\eta\subseteq E_g$ that is simultaneously a cut in all four scalar sheets and carries the unique odd terminal parity class.

**Files:**

- [`research/FIVE_CDC_DDD_ATOM_RESOLUTION_TRIALITY_V1.md`](research/FIVE_CDC_DDD_ATOM_RESOLUTION_TRIALITY_V1.md);
- [`research/FIVE_CDC_ATOM_ROUTE_LOCK_CURVATURE_V1.md`](research/FIVE_CDC_ATOM_ROUTE_LOCK_CURVATURE_V1.md);
- [`research/FIVE_CDC_ROUTE_LOCK_RANK_TWO_TAIT_ESCAPE_V1.md`](research/FIVE_CDC_ROUTE_LOCK_RANK_TWO_TAIT_ESCAPE_V1.md);
- [`research/FIVE_CDC_FULL_RANK_CURVATURE_DUAL_CERTIFICATE_V1.md`](research/FIVE_CDC_FULL_RANK_CURVATURE_DUAL_CERTIFICATE_V1.md).

## 4. Closed finite interfaces and exact graph-specific evidence

These results are complete only in their explicitly finite scopes.

### Closed finite interfaces

- the four-pole alphabet has ten states $A,B_i,C_i,D_i$;
- its abstract Kempe/cap closure problem is finite;
- clique links in $\mathscr A_5$ are explicit, and dominating-clique ranks two through five are closed;
- every fixed graph's Fano-flow space and every fixed flow's gauge fibre are finite exact objects.

**Files:**

- [`research/FIVE_CDC_SMALL_FOUR_POLE_PROFILE_CENSUS_V1.md`](research/FIVE_CDC_SMALL_FOUR_POLE_PROFILE_CENSUS_V1.md);
- [`research/FIVE_CDC_HALFCUBE_CLIQUE_LINK_CAPACITY_V1.md`](research/FIVE_CDC_HALFCUBE_CLIQUE_LINK_CAPACITY_V1.md);
- [`research/FIVE_CDC_DOMINATING_CLIQUE_EXACT_CAPACITY_V1.md`](research/FIVE_CDC_DOMINATING_CLIQUE_EXACT_CAPACITY_V1.md).

### Exact finite laboratories

- all `28560` nowhere-zero Fano flows of the Petersen graph were enumerated;
- the selected thirty-vertex fixed-flow neighbourhood has a complete corrected componentwise census;
- the displayed $J_5$ witness and its one-step horizontal neighbourhood have exact finite descriptions;
- the atom state space has `640` ordered zero-sum root states, `280` bad states, `180` co-root-defect states, and fixed lock fibres $K_{2,4}$;
- explicit rank-two route-lock witnesses have pair-separating cut size four;
- an explicit full-rank locked witness has nonzero curvature, disproving automatic flatness.

**Files:**

- [`research/FIVE_CDC_PETERSEN_ALL_FANO_FLOWS_V1.md`](research/FIVE_CDC_PETERSEN_ALL_FANO_FLOWS_V1.md);
- [`research/FIVE_CDC_COMPONENTWISE_PROGRAMME_CHECKPOINT_V1.md`](research/FIVE_CDC_COMPONENTWISE_PROGRAMME_CHECKPOINT_V1.md);
- [`research/FIVE_CDC_FLOWER_J5_MIXED_CORE_OBSTRUCTION_V1.md`](research/FIVE_CDC_FLOWER_J5_MIXED_CORE_OBSTRUCTION_V1.md);
- [`research/FIVE_CDC_HORIZONTAL_RENEWAL_NEIGHBOURHOOD_V1.md`](research/FIVE_CDC_HORIZONTAL_RENEWAL_NEIGHBOURHOOD_V1.md);
- [`research/FIVE_CDC_CONTEXT_LIMIT_RECOVERY_VERIFICATION_V1.md`](research/FIVE_CDC_CONTEXT_LIMIT_RECOVERY_VERIFICATION_V1.md).

Exact computation here is evidence for the stated finite object. It is not a universal graph theorem unless a separate proof is supplied.

## 5. Controlling corrections and negative results

The following corrections control all earlier formulations.

1. **Global quotient versus componentwise dual.**  
   $J_g\to\mathscr A_5$ remains an exact theorem for global-index-factorable maps, but it is not the complete fixed-lift criterion. The controlling object is $T_g^{(1)}\to\mathscr A_5$.

2. **Connected-cycle adjacency.**  
   A connected-cycle switch is one edge of the flow-reconfiguration graph. A disconnected binary-cycle switch is a composition of commuting connected moves, not one neighbour.

3. **Clique evidence is not a complete obstruction theorem.**  
   Every residual bad lift in one corrected neighbourhood contains $K_6$, but $K_6$-freeness does not suffice for an arbitrary graph to map to $\mathscr A_5$.

4. **Fixed-flow modules are not graph counterexamples.**  
   A vertically closed bad fibre may occur on a graph that succeeds through another flow.

5. **Route-lock is not a graph two-cut.**  
   Exact rank-two witnesses have all four scalar sheets on the same route while the minimum pair-separating edge cut has size four.

6. **Route-lock is not automatically flat.**  
   The checkpoint contains an explicit full-rank locked witness with $\Omega(c)\ne0$.

7. **The rank-two locked branch is eliminated algebraically.**  
   It escapes through a Tait root lift, not through an assumed graph separation.

**Controlling files:**

- [`research/FIVE_CDC_HALFCUBE_SCOPE_CORRECTION_V1.md`](research/FIVE_CDC_HALFCUBE_SCOPE_CORRECTION_V1.md);
- [`research/FIVE_CDC_COMPONENTWISE_PROGRAMME_CHECKPOINT_V1.md`](research/FIVE_CDC_COMPONENTWISE_PROGRAMME_CHECKPOINT_V1.md);
- [`research/FIVE_CDC_K6_FREE_HALFCUBE_WARNING_V1.md`](research/FIVE_CDC_K6_FREE_HALFCUBE_WARNING_V1.md);
- [`research/FIVE_CDC_FIXED_FLOW_GRAPH_LEVEL_SEPARATION_V1.md`](research/FIVE_CDC_FIXED_FLOW_GRAPH_LEVEL_SEPARATION_V1.md);
- [`research/FIVE_CDC_ROUTE_LOCK_RANK_TWO_TAIT_ESCAPE_V1.md`](research/FIVE_CDC_ROUTE_LOCK_RANK_TWO_TAIT_ESCAPE_V1.md);
- [`research/FIVE_CDC_CONTEXT_LIMIT_RECOVERY_VERIFICATION_V1.md`](research/FIVE_CDC_CONTEXT_LIMIT_RECOVERY_VERIFICATION_V1.md).

See [`SUPERSESSION_MAP.md`](SUPERSESSION_MAP.md) for the file-level map.

## 6. Current open global bridge

The endpoint at checkpoint `dad218dd...` is not another finite census. It is a localisation/composition problem in the only surviving full-rank locked sector.

Choose a support-minimal nonflat dual witness

$$
\eta\subseteq E_g.
$$

The sharp next task is to prove that it localises to one of the following, or else to produce a precise counterexample forcing a weaker statement:

- a bounded DDD/Petersen atom or factor;
- a smaller cyclic separator or reducible transition interval;
- a transition-matroid two-sum;
- the physical $D_8$ affine class.

The flat branch also still needs a composition-safe graph resolution. At the wider programme level, the missing global bridges are:

1. a realizability/full-cap-profile theorem for arbitrary admissible four-poles;
2. classification or exclusion of compatible bad duals without a dominating clique of rank at least two;
3. horizontal escape-or-decomposition for graph-level bad-flow sets;
4. a theorem showing that the present finite interfaces cover every global obstruction.

**Current endpoint files:**

- [`research/FIVE_CDC_FULL_RANK_CURVATURE_DUAL_CERTIFICATE_V1.md`](research/FIVE_CDC_FULL_RANK_CURVATURE_DUAL_CERTIFICATE_V1.md);
- [`research/FIVE_CDC_CONTEXT_LIMIT_RECOVERY_VERIFICATION_V1.md`](research/FIVE_CDC_CONTEXT_LIMIT_RECOVERY_VERIFICATION_V1.md);
- [`research/FIVE_CDC_MECHANISM_CLOSURE_MAP_V1.md`](research/FIVE_CDC_MECHANISM_CLOSURE_MAP_V1.md).

## 7. Reliability boundary

This rolling baseline deliberately keeps several assurance axes separate.

- **Mathematical source:** accepted MP2 or exact public research checkpoint.
- **Claim type:** universal proof, closed finite interface, exhaustive graph-specific computation, counterexample, substantial argument with a named gap, or open programme.
- **Independent review:** not supplied merely by inclusion here.
- **Formal status:** no five-support frontier theorem and no outer-shell theorem acquires Lean status through this integration.
- **Publication status:** no novelty, peer-review, manuscript, arXiv, release, or DOI status is upgraded.

The global five-support theorem remains open.