# AffineCDC frontier status

This ledger records the exact live five-support frontier corresponding to the rolling-baseline candidate. It is a synchronization and status surface, not an acceptance or audit document.

## 1. Exact live source

- **Repository:** `Yuren-Tang/mathematics`
- **Live branch:** `research/affine-cdc-five-cdc-v1`
- **Checkpoint included in this baseline:** `dad218dd18ed05d1b7cb730c2dc2431b4db5ec9c`
- **Active writer:** `AffineCDC — Research Lead`
- **Writer model:** one writer on the live research branch; the Curator does not write that branch
- **Observed drift at AC-BASELINE-01 intake:** none

At the beginning of this integration, the live branch and the named checkpoint compared as identical: zero commits ahead and zero behind. No later live commit is included silently.

## 2. Frontier question at `dad218dd...`

The current endpoint lies in the full-rank universally route-locked atom sector.

The exact reductions already established are:

1. a crossed full-challenge route rootifies the local co-root defect;
2. if every challenge uses the original pairing, one obtains a canonical nowhere-zero $\mathbf F_2^3$ challenge quotient with all four scalar sheets on route `12|34`;
3. route-lock does not force a graph two-cut;
4. rank one is impossible;
5. rank two admits a Tait root lift and boundary-state escape;
6. only full rank three survives;
7. full-rank curvature has a primal affine-potential form when flat and a dual common-cut witness when nonflat;
8. an explicit full-rank nonflat witness exists.

Choose a support-minimal nonflat dual witness

$$
\eta\subseteq E_g.
$$

The current primary question is:

> Localise $\eta$ to a bounded DDD/Petersen factor, a smaller cyclic separator or reducible transition interval, a transition-matroid two-sum, or the physical $D_8$ class; otherwise give a precise counterexample requiring a weaker localisation theorem.

The flat sector separately requires a composition-safe graph resolution from its affine potential.

**Controlling files:**

- [`research/FIVE_CDC_ATOM_ROUTE_LOCK_CURVATURE_V1.md`](research/FIVE_CDC_ATOM_ROUTE_LOCK_CURVATURE_V1.md);
- [`research/FIVE_CDC_ROUTE_LOCK_RANK_TWO_TAIT_ESCAPE_V1.md`](research/FIVE_CDC_ROUTE_LOCK_RANK_TWO_TAIT_ESCAPE_V1.md);
- [`research/FIVE_CDC_FULL_RANK_CURVATURE_DUAL_CERTIFICATE_V1.md`](research/FIVE_CDC_FULL_RANK_CURVATURE_DUAL_CERTIFICATE_V1.md);
- [`research/FIVE_CDC_CONTEXT_LIMIT_RECOVERY_VERIFICATION_V1.md`](research/FIVE_CDC_CONTEXT_LIMIT_RECOVERY_VERIFICATION_V1.md).

## 3. Status classification

The labels below classify the claims at the included checkpoint. They do not raise independent-review, formal, peer-review, or publication status.

### 3.1 Universal theorem-level statements

The checkpoint presents the following as general proofs within their stated hypotheses:

- root lifts correspond to coloured cycle-face embeddings and dual triangular cellulations;
- the same-embedding five-support criterion is $T_g^{(1)}\to\mathscr A_5$;
- gauge words are exactly the code-filtered partial Petrials available at fixed Fano flow;
- fixed-flow badness and graph-level badness have different quantifiers;
- marked-core occurrence loci are affine shortened-code loci;
- a connected $K_4$ reserve line yields a cyclic three-edge cut and is reducible in a vertex-minimal counterexample;
- four-pole boundary behaviour has a ten-state alphabet and exact signature-intersection gluing;
- cap forcing and support-Kempe moves give finite closure rules;
- dominating-clique ranks two through five have exact half-cube capacity criteria;
- the DDD atom has one co-root and two root-valued resolutions;
- the original atom route is the unique bad route under a full challenge;
- universal route-lock has the stated $\mathbf F_2^3$ challenge quotient;
- rank-two route-lock admits Tait escape;
- nonzero full-rank curvature has a dual witness that is a common cut in all four scalar sheets and carries odd terminal parity.

These statements remain paper-level unless separately formalized.

### 3.2 Closed finite-interface results

Complete within the named finite universe:

- the ten four-pole boundary states and the abstract Kempe/cap closure problem;
- the half-cube clique-link tables and dominating-clique capacity for ranks two through five;
- the `640/280/180` ordered atom census;
- the fixed-fibre lock graph $K_{2,4}$;
- every exhaustive computation over a named finite graph, fixed flow, gauge fibre, or displayed neighbourhood.

“Closed” here means exhaustive for that finite interface, not complete for arbitrary cubic graphs.

### 3.3 Exact graph-specific and finite-verified evidence

- all `28560` nowhere-zero Fano flows of Petersen;
- the thirty-vertex fixed-flow and connected-cycle neighbourhood censuses;
- the displayed $J_5$ witness and one-step renewal neighbourhood;
- explicit rank-two route-lock witnesses with minimum pair-separating cut four;
- the recovered full-rank nonflat witness with curvature class nonzero;
- exact small four-pole profiles and selected cap/Kempe closures.

These are theorems about the displayed finite objects. They do not establish the global five-support statement.

### 3.4 Computational support

Some finite statements are supported by exact Python or Wolfram enumeration. Where a general argument is also written, computation checks the finite instance or identity. Where no universal proof is supplied, the claim stays finite/computational.

The private notebook branch

`Yuren-Tang/research-workbench:research/affine-cdc-five-cdc-notebook-v1`

is mapped provenance and recovery evidence. It is not copied wholesale into the public baseline. Public claims must retain a public source or an explicit finite certificate boundary.

### 3.5 Substantial arguments with named gaps

The checkpoint supplies strong reductions but not complete graph-level transfer for:

- composition-safe use of a crossed atom resolution;
- graph resolution from a flat affine potential;
- localisation of a nonflat common-cut witness;
- realisability/full-cap closure for arbitrary four-poles;
- global horizontal escape or decomposition of all bad-flow components.

These are not to be restated as completed theorems.

### 3.6 False overstrong statements and counterexamples

The following readings are false or unsupported:

- $J_g\to\mathscr A_5$ is the complete fixed-lift criterion;
- every binary-cycle switch is one edge of the flow-reconfiguration graph;
- $K_6$-freeness is sufficient for an arbitrary graph to map to $\mathscr A_5$;
- a bad fixed-flow gauge fibre makes the underlying graph a counterexample;
- universal route-lock forces a graph-theoretic two-edge separation;
- universal route-lock forces zero curvature or automatic affine flatness;
- finite neighbourhood evidence that all residual bad lifts contain $K_6$ is a universal obstruction theorem.

The controlling counterexamples and corrections are linked in [`SUPERSESSION_MAP.md`](SUPERSESSION_MAP.md).

### 3.7 Superseded formulations

Superseded files remain in Git and in `projects/affine-cdc/research/` as priority and discovery records. Their theorem fragments may remain valid under narrowed hypotheses. Navigation must use the controlling successors rather than deleting or silently rewriting historical sources.

### 3.8 Open statements

The global five-support theorem remains open.

The present wider open bridges are:

1. composition-safe resolution of flat and nonflat locked atoms;
2. localisation of a support-minimal common-cut witness;
3. a full-cap-profile/realisability theorem for arbitrary admissible four-poles;
4. classification or exclusion of compatible bad dual triangulations without a dominating clique of rank at least two;
5. graph-level horizontal escape-or-decomposition;
6. a global theorem proving that the finite local mechanisms cover every obstruction.

## 4. Current mechanism layers

The programme should be read in this order:

1. **graph choice:** choose a nowhere-zero Fano flow;
2. **vertical fibre:** explore compatible root lifts through the gauge/partial-Petrial code;
3. **same-embedding test:** seek $T_g^{(1)}\to\mathscr A_5$;
4. **target analysis:** use half-cube links and dominating-clique capacities;
5. **source analysis:** use harmonic reserves, cuts, four-poles, and boundary signatures;
6. **horizontal motion:** use connected-cycle switches to change the Fano flow and the available vertical fibre;
7. **composition:** prove that local escapes and finite interfaces assemble globally.

A fixed-lift, fixed-flow, and graph-level obstruction must never be conflated.

## 5. Next intake trigger

Create a new exact frontier checkpoint for rolling-baseline intake when one of the following occurs:

- a theorem or counterexample changes the full-rank localisation endpoint;
- the flat-potential or nonflat common-cut sector is closed, split, or materially weakened;
- a new universal four-pole or target-capacity theorem changes the mechanism map;
- a graph-level bad-flow escape/decomposition theorem is obtained;
- a correction materially changes a controlling statement already referenced by `CURRENT_BEST.md`;
- the live branch advances before an owner decision on this baseline.

Routine exploratory commits that do not alter the current mechanism, correction map, or open boundary need not trigger immediate re-integration.

## 6. Synchronization rule

This file records checkpoint `dad218dd...` only. The integration branch must not be used as a substitute writer for the live research branch. No research-branch synchronization is authorized before a later owner movement decision. Any later drift must be recorded by exact SHA and reviewed before inclusion.