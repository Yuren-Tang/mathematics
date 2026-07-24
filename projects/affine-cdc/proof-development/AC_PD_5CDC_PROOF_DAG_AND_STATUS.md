# AC-PD-5CDC — v7.4 component-chain proof DAG and status

**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**PDL branch:** `proof-development/affine-cdc-rigour-v1`  
**Frozen RL source:** `research/affine-cdc-five-cdc-v1@02b37476198e9eaa2b4cd8d2a2edd76782bdcd49`  
**Permanent negative audit:** `audit/affine-cdc-xi-co-root-v1@53be22a0f65b85068b11e5f781579618967db9dd`  
**Classification:** `V7.4 COMPLETE PROOF-DEVELOPMENT CANDIDATE / READY FOR NEW INDEPENDENT FULL AUDIT / NOT AN ACCEPTED THEOREM`.

The old v6/v6.1 candidate `1f57422...` remains blocked.  The v7.3 claim that
`Xi` alone gives co-root totality is also withdrawn: audit #78 produced a valid
same-arc equal-face counterexample.  The new totality theorem for both singular
inverse-parent fibres is the physical component-chain theorem.

---

## 1. Controlling proof DAG

```text
R0 root-flow / indexed five-support equivalence
        |
R1 one valid connected loopless bridgeless cross closure (order N-2)
        |
R2.1 exact boundary / ten states / fixed physical route
        |
R2.2 target-synchronised forward root-NNI prefix
        |
route/category terminal OR first equal-face cancellation
        |
actual smaller target cap closure (order N-2)
        |
one arbitrary lower target root flow
        |
one inverse pop
        |
root state / one standard co-root atom / exact terminal
        |
one-atom state-walk, run, seam and backtrack coherence
        |
complete root-valued prescribed-parent state
        |
        +---------------- root parent
        |                     |
        |             literal stored root NNI
        |
        +---------------- co-root / DDD (4,2,2)
        |                     |
        |             Phase-B nonlocked consumer
        |                     |
        |             cut two marked H_h edges
        |                     |
        |        witnessed marked-arc component chain
        |                     |
        |       final matching change / separation
        |                     |
        |          K_i or switch + literal parent
        |
        +---------------- zero parent (0,2,2)
                              |
                        fixed physical H_h
                              |
                  remove active-cell interiors
                              |
             witnessed terminal-path component chain
                              |
                    crossed outside matching
                              |
             crossed-sheet alignment + one switch
                              |
                  literal parent central root h
                              |
                 lower stored-prefix length
                              |
                  ordinary strong induction
                              |
               cubic five-support candidate
                              |
             accepted conditional outer shell
                              |
             finite bridgeless five-CDC candidate
```

Exactly one principal order-lowering event occurs at the first cancellation
target.  Every inverse-parent repair after the pop is same-order and terminates
by a finite inherited physical connector list.

---

## 2. Retained audited/reconstructed units

| Unit | Status | Controlling source |
|---|---|---|
| R0 root-flow equivalence | retained exact | indexed five even supports = root-valued `E_5` flow |
| R1 valid cross | prior audit accept | one connected loopless bridgeless cross closure; theta base |
| R2.1 boundary/fixed route | prior audit accept | 640 boundaries, ten states, exact `J_i/K_i` rows |
| R2.2 forward descent | retained | equality/DDD current-flow descent to first cancellation or exit |
| synchronized prefix | PDL complete draft | v7.2 target-synchronised pure root-NNI prefix |
| actual smaller target | PDL complete draft | exact cap closure/order and cut/bounded alternatives |
| arbitrary-flow single pop | PDL complete draft | intersecting/equality/good-disjoint/missing-index rows |
| one-atom coherence | PDL complete draft | nonbranching state walk, maximal runs, seams, two-seam backtracks |
| Phase-B horizontal consumer | PDL complete draft | all nonlocked co-root states give parent/route/terminal |
| terminal census | PDL complete draft | exact cap, route, cyclic `2/3/4` cut and bounded consumers |
| general outer shell | independently accepted conditional implication | cubic five-support -> finite bridgeless 5-CDC |

---

## 3. New v7.4 load-bearing unit

### `FC-COMPONENT-CHAIN-ROOT-NNI`

For one fixed physical channel `H_h`:

1. every source vertex has channel degree zero or two;
2. the unique inactive triangle is `[5]\setminus h`;
3. the connected physical quotient has nodes for channel components and
   individual inactive vertices, with stable nonchannel physical edges as
   witnessed quotient edges;
4. one active/inactive root NNI absorbs an inactive singleton;
5. one active/active root NNI or equal root branch swap absorbs a closed cycle;
6. one initially selected shortest simple connector chain is retained literally;
7. every nonterminal move deletes its first stable connector;
8. the final connector between two distinguished terminal paths changes their
   ordered terminal matching.

Controlling PDL files:

- `AC_PD_V7_4_COMPONENT_CHAIN_THEOREM_RECONSTRUCTION.md`;
- `AC_PD_V7_4_COMPONENT_CHAIN_ROW_AND_DART_TABLES.md`;
- `AC_PD_V7_4_INHERITED_CHAIN_AND_FINAL_MATCHING.md`.

### Exact falsification-point dispositions

- inactive entry/exit at one modified singleton: handled by stable next-dart
  inheritance;
- next connector after absorption: unchanged stable edge/root and still
  nonchannel;
- active-cycle entry/exit at one modified vertex: impossible because an active
  cubic vertex has exactly one nonchannel incidence;
- equal final branch swap preserving matching: impossible for two distinct
  named terminal components;
- chain shortening by recomputed distance: not used; rank is remaining length of
  one inherited connector list.

---

## 4. Co-root/DDD fibre after audit #78

### Permanent negative boundary

The Heawood equal bad face `9-14:23` remains a counterexample to:

> arbitrary equal bad face => route exit or one-sided component after zero/one
> branch swap.

The old arbitrary-equal-face theorem and unconditional `Xi` totality are false
and retired.

### Repaired theorem

Cut the two actual marked `H_h` edges.  Their common component becomes two
marked terminal arcs.  Contract a physical component chain between those arcs.
The final connector gives either:

- the separated marked-edge matching, hence a separating rescue channel; or
- the opposite common-cycle route, hence `K_i`/cap-compatible progress.

Apply the existing Phase-B consumer.

In the audit Heawood graph, stable edge `6-7:23` is the direct connector.  The
root NNI

\[
123+234\to124+134,
\qquad23\to14
\]

changes route `(1,2)|(3,6)` to `(1,3)|(2,6)` while preserving the graph category.

Controlling file:

`AC_PD_V7_4_CO_ROOT_COMPONENT_CHAIN_COROLLARY.md`.

`Xi` frame/invariance/six strict rows remain valid optional arithmetic, but no
`Xi` source-selection or totality claim is controlling.

---

## 5. Zero-parent fibre

Normalize

\[
(A,B,C,D)=(13,13,23,23),\qquad h=35.
\]

A disconnected active-cell complement is a bridge/two-cut/bounded output.  In
a connected residual lock, the outside matching is `AB|CD`, giving terminal
paths `A--B` and `C--D`.  Contract a physical component chain between them.
The final connector exposes `AC|BD` or `AD|BC`.

Align the active crossed root sheet, switch one closed `H_35` component, and
perform the literal parent NNI with central root `35`.

The complete Heawood movie was independently reconstructed:

```text
remote branch swap at stable edge 13-14
    -> H_35 components Z_0,Z_1
    -> switch Z_0 by 35
    -> active word (15,13,25,23)
    -> literal AB|CD parent NNI, central root 35.
```

Every intermediate graph is connected, simple, cubic and bridgeless; cyclic
edge-connectivity is `6,5,5,5` for the four displayed stages.

Controlling file:

`AC_PD_V7_4_ZERO_PARENT_COMPONENT_CHAIN_COROLLARY.md`.

---

## 6. Complete inverse-parent table

The sum of two roots has weight `0,2` or `4`, so the table is exhaustive:

| value | disposition |
|---|---|
| root | literal stored root NNI |
| co-root | marked-arc component chain + Phase-B consumer |
| zero | terminal-path component chain + alignment + one switch + literal parent |
| route/category | exact existing consumer |

There is no unresolved fourth row.

Controlling integration file:

`AC_PD_V7_4_COMPLETE_INVERSE_PARENT_AND_INDUCTION.md`.

---

## 7. Ordinary induction closure

The fixed-order return uses the nested structural measures:

1. graph order for actual smaller targets;
2. number of stored source NNIs remaining;
3. remaining connector count in the currently inherited component chain.

No same-order root-solubility call occurs.  After each literal parent return the
stored-prefix length falls.  Therefore the ordinary induction

\[
P_{<N}\Longrightarrow P_N
\]

is closed at PDL proof-development level with no known internal gap.

The resulting cubic five-support and general bridgeless five-CDC statements are
complete proof-development candidates, not independently accepted theorems.

---

## 8. Antecedent and novelty control

Controlling ledger:

`AC_PD_V7_4_COMPONENT_CHAIN_ANTECEDENT_AND_NOVELTY_LEDGER.md`.

It finds no prior theorem with the same quantifiers.  Retained antecedents
supply local root NNI arithmetic, labelled dart contracts, one-atom strip
coherence and terminal consumers.  Historical strip, annulus, Pachner and raw-
insertion machinery does not supply physical component-chain totality.

---

## 9. Supersession ledger

### Permanently retired as controlling totality

1. v6/v6.1 mixed-order `Q_N/P_N` architecture;
2. `M_N`, `d_N`, nested bubbles and terminal frames;
3. target-boundary wording as proof of target realization;
4. track erasure/periodic crosscut as parent progress;
5. finite-state or SCC distance without reachability;
6. arbitrary-equal-face route-or-split;
7. `Omega` orbit-minimum proof;
8. `Xi` as unconditional source selector or totality rank;
9. unconditional at-most-`N` `Xi` macro bound;
10. generic root/NNI connectivity;
11. equality cancellation during fixed-order return.

### Retained only in exact limited scopes

- `Xi` frame, whole-component invariance and six strict rows;
- equality/DDD Pachner potentials for forward current-flow descent;
- constant-pivot runs, seams and strip gluing for one-atom coherence;
- raw-insertion genealogy as historical labelled-dart mathematics;
- equality annulus/carrier reductions as noncontrolling topology.

### New controlling totality

- physical fixed-channel quotient;
- active/inactive absorption;
- active/active cycle contraction;
- inherited stable connector chain;
- final ordered matching change;
- co-root and zero-parent component-chain corollaries.

---

## 10. Current exact classification

\[
\boxed{
\begin{array}{c}
\text{first cancellation / actual target / single pop: reconstructed}\\
+\ \text{one-atom state-walk coherence: reconstructed}\\
+\ \text{component-chain source theorem: reconstructed}\\
+\ \text{co-root prescribed-parent fibre: reconstructed}\\
+\ \text{zero-parent prescribed-parent fibre: reconstructed}\\
+\ \text{complete inverse table and ordinary induction: reconstructed}\\
\hline
\text{NO KNOWN PDL GAP / READY FOR NEW INDEPENDENT V7.4 AUDIT.}
\end{array}}
\]

This status does not authorize canonical movement, Lean theorem status,
manuscript integration, release, arXiv, DOI, peer-review or publication claims.