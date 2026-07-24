# AC-5CDC-AUD-V741 — induction, prefix, terminal and outer-shell audit

## 1. Graph-order accounting

Let `P_N` denote root solubility through order `N` for connected loopless bridgeless cubic multigraphs.

The candidate uses lower induction in two distinct places:

1. **Upstream R1 input.**  Deleting a simple edge gives a valid cross closure of order `N-2`; `P_{N-2}` supplies the specified initial cross flow.
2. **Inside the return module.**  If the synchronized prefix reaches a genuine first cancellation, the actual target cap closure has order `N-2`; `P_{N-2}` supplies an arbitrary flow on that target.

Thus the phrase “unique lower-order call” is correct only as a module-local statement: after entry with the specified cross flow, the return module opens one fresh target call.  Globally, strong induction is instantiated twice on order-`N-2` graphs.  This is not circular and is not itself a defect.

Every reviewed cut consumer also calls only strictly smaller completions.  No same-order root-solubility invocation was found in the named terminal ledger.

## 2. First cancellation and single pop

The first-cancellation file correctly separates:

- target synchronization during root-valued prefix NNIs;
- target-invalid moves returned as current-target cut/bounded terminals;
- the first genuine equal-face cancellation;
- the arbitrary root flow subsequently chosen on the actual smaller target.

The inverse-pop table is algebraically exhaustive:

```text
distinct intersecting roots -> root insertion
equal roots -> five-leaf root insertion
doubled disjoint, good index -> five-leaf root insertion
missing index -> one standard co-root atom
local coincidence/separator -> exact terminal.
```

Fresh enumeration gives 180 ordered doubled-disjoint borrowing data, partitioned into 120 good and 60 missing-index rows.  The displayed missing-index NNI removes one of the two transient co-root edges and leaves exactly one standard atom.  No second lower-order call occurs in the pop.

## 3. Exact one-atom interface failure

The controlling state-walk theorem proves coherence for a **supplied finite comparison**:

- at most one persistent atom;
- constant-pivot identity strips;
- root-valued six-port seams at genuine pivot changes;
- two-seam backtrack corridors;
- closed and normalized-open gluing;
- a periodic crosscut when the same complete unresolved endpoint has already occurred twice in a constructed comparison.

It explicitly does not prove that an arbitrary one-atom state has a continuation or that a periodic/root short side realizes the prescribed parent.  Its exact unresolved obligations are:

```text
construction of a finite continuation comparison from every arbitrary one-atom target-parent failure;
prescribed-parent endpoint realization rather than another root detour;
a well-founded pure-NNI target scheduler.
```

The v7.2 terminal census consequently marks the zero/co-root discrepancy as a nonterminal blocked interface and states that ordinary induction is conditional on pure-NNI target reinsertion.

The v7.4.1 integration nevertheless writes, in substance:

```text
one atom remains
-> apply one-token coherence
-> complete root-valued prescribed-parent state or terminal.
```

This conclusion is stronger than the retained theorem.  No new continuation theorem appears in the v7.4.1 delta.  The v7.3 and v7.4 files merely assert that the first-failure grammar “supplies a finite complete comparison”; R2.3 itself closes only bounded local confluence and lists global continuation/return as open.

### Required missing theorem

A valid repair must prove a theorem of at least the following strength.

> **ONE-ATOM-COMPLETE-ENDPOINT-TOTALITY.**  For every complete labelled contextual state arising from the single inverse pop with at most one standard co-root atom and with a literal live prescribed parent, cap block, route/profile, support transport, stable darts and prefix ancestry, there is a finite source-faithful same-order history ending either in (i) a complete root-valued crossed endpoint carrying those same fields, or (ii) an exact current-descendant terminal.  The construction must be total and well-founded without same-order root solubility, generic NNI connectivity, finite-state/SCC recurrence, or counting track erasure as prescribed-parent progress.

The present packet contains local cells that such a theorem may use, but not the theorem.

## 4. Parent-value table and component-chain fibres

At an actual complete root endpoint, the parent central value is indeed exhaustively `root`, `co-root` or `zero`.

- The root row performs the literal stored NNI.
- The co-root row is valid after the exact #82 two-marked-arc constructor.
- The zero row is valid after the exact #82 active-cell constructor.

The scoped component chain and the final local consumers are therefore not rejected.  They are conditional upon reaching the complete endpoint.  The missing theorem in Section 3 prevents the table from being universally entered after an arbitrary lower-target flow.

## 5. Prefix and rank discipline

Conditional upon a parent obligation being reached, the active control

```text
(L,C)
```

is adequate:

- `L` is the number of stored source NNIs remaining;
- `C` is the remaining length of the one currently fixed connector list;
- each nonterminal component-chain move strictly lowers `C`;
- no channel or path replacement occurs while `L` is fixed;
- the final matching is consumed immediately into a literal parent or terminal;
- only literal parent success lowers `L` and allows a new local chain.

This rules out the previously dangerous reset of an inner rank while its enclosing parent obligation remains unchanged.  It does not supply the missing transition from the one-atom state to the complete parent obligation.

## 6. Terminal consumers

The reviewed terminal ledger distinguishes the exact graph and whether a flow is supplied.  The following consumers have no detected order defect:

- cap-compatible `K_i` and route outputs;
- separating support-channel repair;
- cyclic two-cut completion by one edge;
- cyclic three-cut completion by one cubic vertex;
- cyclic four-cut completion by the exact cap/profile mechanism;
- loop, parallel, triangle, theta, direct-matching and acyclic low-port bases;
- single-pop local coincidences and unavailable-borrow rows.

All recursive graph calls in these consumers are strictly smaller.  Bounded uncoloured bases receive explicit existential root assignments rather than an alleged inherited recolouring.  No terminal consumer applies to an unresolved ordinary one-atom discrepancy; that discrepancy is correctly nonterminal in the v7.2 census.

## 7. Ordinary induction

The claimed induction step would require:

```text
specified cross flow
-> finite synchronized prefix
-> actual-target lower flow
-> single inverse pop
-> complete prescribed-parent endpoint or terminal
-> root/co-root/zero table
-> return through every stored prefix edge
-> root flow on G.
```

The fourth arrow is unavailable in general.  Therefore the induction is not closed even though all graph-order calls are strictly lower and the later `(L,C)` measure is well-founded in its own domain.

## 8. Outer shell

The outer-shell implication is valid as a conditional theorem.

1. Remove loops.
2. Replace every degree-`d>=2` vertex by a cycle of `d` ports, using two parallel internal edges for `d=2`.
3. The expansion is loopless, cubic and bridgeless.
4. Apply the cubic five-support theorem componentwise with the same five indices.
5. Project each support memberwise through the port collapse; cut parity descends because fibre edges do not cross inverse-image cuts.
6. Exact double multiplicity descends edge by edge.
7. Add every original loop to two fixed support indices.

This preserves at most five even-subgraph members.  It proves

```text
cubic five-support theorem -> finite bridgeless five-CDC.
```

It does not prove the antecedent and cannot repair the missing return step.

## 9. Induction-cone verdict

```text
R1 structural reduction: passes
finite boundary and inverse-pop algebra: passes
first-cancellation target discipline: no blocker found
one-atom local coherence: passes in stated supplied-comparison scope
arbitrary one-atom continuation: MATERIAL GAP
parent table and scoped fibres: conditional
prefix return: blocked
ordinary cubic induction: blocked
outer shell: valid conditional implication
five-CDC conclusion: not established.
```
