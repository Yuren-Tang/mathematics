# Finite laboratories and exact certificates

## 1. Role of computation

Exact computation in this programme serves four legitimate purposes:

1. verify a finite object completely;
2. expose a counterexample to an overstrong theorem;
3. discover a structural invariant later proved generally;
4. calibrate which mechanisms occur in concrete graphs.

It does not replace a general proof. Every result below is classified by its finite scope.

## 2. The fixed-flow cube certificate

An explicit cube Fano flow has no compatible five-coordinate slice. For every plane $W\le\mathbf F_2^3$, one component of $G_W$ has odd common outside-colour parity.

This proves exactly:

$$
\boxed{
\text{one fixed Fano flow may require six indexed supports.}
}
$$

It does not prove that the underlying graph lacks a five-support cover through another flow or a non-factorable componentwise map.

## 3. The thirty-vertex laboratory

The selected thirty-vertex cubic graph has an explicit proper three-edge-colouring and therefore a three-support cycle double cover. It is graph-level easy.

Nevertheless, one chosen Fano flow has a two-state bad gauge fibre, and nearby flows realize exact renewal modules.

### Exact vertical facts

- one-dimensional reduced gauge fibre with clique renewal;
- universal three-cube modules in several nearby flows;
- universal six-cube modules with point and line renewal;
- marked-core occurrence loci matching shortened reserve codes;
- complete corrected componentwise census.

### Exact horizontal facts

Among all nonzero binary-cycle switch pairs, only those with connected support are genuine one-step neighbours. The corrected connected-neighbour population is $2801$.

Most connected neighbours possess at least one componentwise-good root lift. The wholly bad neighbours in the displayed census all contain $K_6$, but this is finite neighbourhood evidence, not a universal obstruction theorem.

### Structural lesson

A bad vertical fibre may sit on a graph with a much smaller cover through another flow. Renewal cubes model poor fixed flows, not graph-level counterexamples.

## 4. Petersen: complete Fano-flow classification

For the Petersen graph:

- binary cycle-space dimension: $6$;
- nowhere-zero Fano flows: $28560$;
- coordinate-free $GL(3,2)$ flow orbits: $170$;
- orbits under graph automorphisms and $GL(3,2)$: $5$.

Every Fano flow spans rank three. The complete reduced-fibre table is:

$$
\begin{array}{c|c|c}
\text{fibre size}&\text{good lifts}&\text{flow orbits}\\
1&1&80\\
2&2&60\\
2&1&20\\
4&3&10.
\end{array}
$$

Hence

$$
\boxed{\mathfrak B(P)=\varnothing.}
$$

Every nowhere-zero Fano flow on Petersen has a componentwise-good lift.

### Surface types

Exactly three reduced surface types occur:

1. orientable torus with simple dual $K_5$;
2. Klein bottle with simple dual $K_5$;
3. projective plane with simple dual $K_6$.

The first two are good; the projective-plane state is bad. Mixed fibres contain exactly one projective-plane state and escape under a nontrivial admissible Petrial.

### Horizontal graph

The connected-cycle switch graph on all $28560$ flows is connected. Thus horizontal connectedness and vertical solubility are distinct facts; Petersen is vertically soluble at every horizontal state.

## 5. Flower snark $J_5$

A displayed Fano flow on the flower snark has a two-state reduced gauge fibre.

### State 1

A nine-vertex dual graph $D_9$ is $K_6$-free but contains

$$
K_2\vee W_5.
$$

The common-neighbour graph of a target edge in $\mathscr A_5$ is a three-colourable triangular prism, so $D_9$ cannot map to $\mathscr A_5$.

### State 2

The other dual is $K_7-e$ and contains a $K_6$.

Thus the nonzero gauge word exchanges two distinct obstruction species:

$$
K_2\vee W_5
\longleftrightarrow
K_6.
$$

### Exact one-step neighbourhood

The centre flow has $712$ connected-cycle neighbours. Exactly $528$ have at least one good reduced lift. The displayed bad flow is therefore not horizontally trapped.

Among the wholly bad neighbours, every $K_6$-free bad lift is isomorphic to the same $D_9$ obstruction. This is a complete one-step finite statement, not a classification of all Fano flows on $J_5$.

## 6. Small four-poles

All connected cap-admissible cubic four-poles through six internal vertices were generated and their complete five-support boundary profiles computed.

- underlying multigraph classes: $30$;
- complete profile types: $8$;
- every realized profile contains one full cap set $\mathcal K_i$;
- none realizes one of the four small abstract mismatch kernels.

This proves the lower bound that a shore in a minimal-counterexample cyclic four-cut has at least eight internal vertices.

Larger exploratory samples show the same eight profiles, but those searches are not exhaustive.

## 7. Routing and monodromy tables

The ten-state routing game was enumerated exactly.

- four minimal disjoint cap-forced Kempe-closed profile pairs;
- unique safe route for every state/challenge in each kernel;
- two policy-pair orbits: Type T and Type H;
- sixteen BBD rainbow monodromies, four of each cycle type $2^21,41,32,5$;
- four DDD monodromies in the physical DDD triangle;
- the BBD monodromies generate $S_5$;
- no common affine $\mathbf F_5$ structure on support names is preserved.

These finite tables motivate the holonomy theory. The general algebraic conclusions are proved separately and do not depend on treating the table as a universal graph classification.

## 8. Atom and route-lock certificates

Exact enumeration of ordered root quadruples gives:

$$
640\text{ zero-sum states},\qquad
280\text{ bad states},\qquad
180\text{ co-root-defect states}.
$$

Every bad-state/full-challenge row has one bad route and two rootifying crossed routes. Fixed co-root fibres are $K_{2,4}$.

Two explicit witnesses protect the trust boundary.

### Witness A — no graph two-cut

A rank-two locked four-pole has all scalar sheets routed as $12\mid34$, but the minimum pair-separating edge cut has size four.

### Witness B — nonflat route lock

A full-rank locked four-pole has one terminal-colour edge carrying side word $0100$. No closed scalar component can alter it, so

$$
\Omega(c)\ne0.
$$

These are counterexamples to two tempting but false shortcuts.

## 9. Renewal and reserve-code censuses

Exact gauge-fibre enumeration identifies:

- private point cores;
- $K_4$ reserve lines;
- $2K_3$ interfaces;
- shortened reserve-code dimensions;
- essential quotients after removing invisible directions.

The general theorem is the affine occurrence-locus formula. The detailed point/line/cube distributions remain laboratory-specific.

## 10. Defect and $K_6$ local tables

Exact finite checks support:

- the fifteen nonzero vectors of $E_5$ as the fifteen edges of $K_6$;
- the $20$ triangle and $15$ one-factor zero-sum triples;
- the six local cubic weight patterns;
- the fifteen DDD/co-root atoms;
- the $L(\mathrm{Petersen})$ endpoint transition graph;
- the $D_8$ and $S_5$ cohomology dimensions;
- root-fibre tables for the four rainbow monodromy types.

The accompanying general theorems are proved in the substantive chapters. The computation supplies exact finite verification, not a substitute for those proofs.

## 11. Reproducibility boundary

The public packets state the exact finite objects, counts, certificates, and proof status. Private notebook branches contain supporting code and recovery evidence but are not copied wholesale into the public corpus.

The recovered combined verifier was incomplete. Its publicly reconstructed modules were rerun successfully; the unavailable historical failing assertion remains classified as `CODE-PARTIAL`.

No public theorem may rely solely on hidden notebook state. A finite claim should be supported by at least one of:

- a public explicit certificate;
- a dependency-free reproducible enumeration description;
- a separate mathematical proof.

## 12. What the laboratories do not show

They do not prove:

- every graph has a good Fano flow;
- every bad-flow component has a one-step exit;
- every fixed-flow obstruction is $K_6$-based;
- every $K_6$-free compatible dual is good;
- every four-pole contains a full cap profile;
- every route-locked atom localizes to a bounded factor;
- the global five-support statement.

The laboratories identify mechanisms and falsify overstatements. The remaining proof must use the structural theorems extracted from them.