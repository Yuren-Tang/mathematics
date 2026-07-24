# AC-PD-5CDC — v7.2 proof DAG, supersession and current status

**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**PDL branch:** `proof-development/affine-cdc-rigour-v1`  
**Frozen Research Lead input:** `research/affine-cdc-five-cdc-v1@094ca09f6d3982b785a3f3428d9ec079dbba0855`  
**Classification:** `V7.2 BOUNDED RECONSTRUCTION / BLOCKED-PROOF AT PURE-NNI TARGET REINSERTION`.

The old fixed candidate

`proof-development/affine-cdc-rigour-v1@1f57422e0e415d8902d56eb294183815c0a0b640`

is blocked by the accepted independent audits in research-workbench issues
#68, #69 and #70.  Its v6/v6.1 mixed-order route is not a complete proof draft
and is not controlling here.

---

## 1. Controlling v7.2 spine

\[
\begin{array}{c}
R_0\text{ root-flow/five-support equivalence}\\
\Downarrow\\
R_1\text{ one valid smaller cross closure}\\
\Downarrow\\
R_{2.1}\text{ one-cross boundary and fixed route}\\
\Downarrow\\
R_{2.2}\text{ route-preserving monotone root-NNI prefix}\\
\Downarrow\\
\text{route/category terminal or first equal-face cancellation}\\
\Downarrow\\
\text{actual smaller target cap closure}\\
\Downarrow\ P_{<N}\\
\text{one arbitrary-flow inverse pop}\\
\Downarrow\\
\text{pure fixed-order NNI/one-atom return}\\
\Downarrow\\
\text{ordinary strong induction }P_N\\
\Downarrow\\
\text{accepted general-graph outer shell}.
\end{array}
\]

Exactly one graph-order descent is allowed: the first cancellation.  Everything
after the pop must remain at predecessor order and use only the pure `2--2`
fixed-order alphabet.

---

## 2. Reconstructed units

| Unit | State | Controlling PDL file/result |
|---|---|---|
| `R0` | retained audited input | root-valued `E_5` flow = five indexed even supports on loopless cubic graphs |
| `R1` | `ACCEPT` from old audit | one valid connected loopless bridgeless cross closure of order `N-2`; theta base |
| `R2.1` | `ACCEPT` from old audit | 640 boundaries, ten states, exact `J_i/K_i`, fixed-route rows |
| `R2.2` | `ACCEPT` from old audit and retargeted | positive equality/DDD potentials; no local minimum before an equal-face pair or exit |
| synchronized prefix | `COMPLETE-DRAFT` | `AC_PD_5CDC_V7_2_FIRST_CANCELLATION_AND_SINGLE_POP.md`: pure root-NNI prefix, parallel target test, route/category stopping |
| first-cancellation target | `COMPLETE-DRAFT` | disconnected cross gives parent 2/4-cut/bounded; invalid target gives cut <=4/bounded; otherwise actual target order `N-2` |
| arbitrary-flow pop | `COMPLETE-DRAFT` | all intersecting/equality/good-disjoint/missing-index rows source-level; exact five exterior darts retained |
| doubled-disjoint missing index | `COMPLETE-DRAFT` | explicit `(Q_1,Q_5,15)` three-vertex object and root NNI `34+Q_5=12` leave exactly one standard `Q_5` atom |
| narrow R2.4 interface | `COMPLETE-DRAFT` | one atom, two crossed resolutions, complete nonbranching state walk; no shortest-core/route-bit dependency |
| maximal runs/switches | `COMPLETE-DRAFT` | `AC_PD_5CDC_V7_2_STATE_WALK_CELLWISE_RECONSTRUCTION.md` |
| six-port seams | `COMPLETE-DRAFT` | all 120 nonbacktracking cells; `(z,z,w,w)` has `(0,2,2)`; literal turn-corolla and dart maps |
| reduced backtracks | `COMPLETE-DRAFT` | two genuine switch seams plus physical middle constant-run identity strip; no abstract `abba` deletion |
| closed/normalized-open track erasure | `COMPLETE-DRAFT IN STATED SCOPE` | seam/run identity gluing; supplied periodic endpoint crosscut |
| terminal census | `COMPLETE-DRAFT` | `AC_PD_5CDC_V7_2_TERMINAL_CENSUS_AND_ORDINARY_INDUCTION_BOUNDARY.md` |
| outer shell | retained `ACCEPT` from issue #70 | conditional cubic-to-general finite bridgeless 5-CDC implication |

Fresh finite checks:

- doubled-disjoint borrowing: `180 = 120 good + 60 missing-index`;
- six-port switch cells: `120/120` have distinct intersecting side roots and
  pairing pattern `(0,2,2)`.

---

## 3. Unique current blocker

### `AC-PD-V7.2-PURE-NNI-TARGET-REINSERTION`

The fixed-order source proves local one-atom continuation and erasure of a
**supplied** finite singular track.  It does not prove that the root short side
produced by a periodic crosscut realizes the prescribed ordinary arborescence
parent topology.

The minimal witness is

\[
(A,B,C,D)=(12,34,13,24).
\]

For the required parent pairing `AB|CD`, the central value is

\[
12+34=Q_5,
\]

while the two crossed topologies have root values

\[
12+13=23,
\qquad
12+24=14.
\]

Thus a fixed-boundary pure-NNI scheduler may alternate the two root crossed
states while the prescribed parent pairing remains co-root.  Cellwise erasure
or a periodic root crosscut supplies a root detour between crossed side
histories; no frozen theorem identifies that detour with a root state on the
parent pairing or a state of smaller target distance.

Controlling obstruction dossier:

`AC_PD_5CDC_V7_2_PURE_NNI_TARGET_REINSERTION_OBSTRUCTION.md`.

A repair must prove prescribed-parent realization, a strict complete-state
measure, a target-side relative cellwise theorem, or an exact ambient terminal
forced by the displayed cycle.

---

## 4. Conditional units

The following statements are valid only after the blocker is closed:

1. pure-NNI no-reopening return through the entire stored prefix;
2. exhaustiveness of the terminal census for every fixed-order execution;
3. ordinary strong-induction closure `P_{<N} => P_N`;
4. cubic five-support theorem;
5. application of the accepted general-graph outer shell.

No `rho_atom` rank is currently accepted: the v7 no-reopening file names it but
does not construct a strictly decreasing quantity for the displayed two-state
cycle.

---

## 5. Supersession ledger

### Retired as controlling mathematics

1. simultaneous witnessed `Q_N/P_N` induction;
2. arbitrary lower child-history lifts through a weld;
3. nested cancellation bubbles and variable-order compression;
4. suspended ancestor marks as a global recursion device;
5. resolved-call graph `M_N` and distance `d_N`;
6. terminal-frame/outermost-child unwind;
7. child-prefix versus parent-prefix comparisons;
8. the old claim that target-boundary wording alone makes track erasure realize
   the selected parent topology;
9. R2.5 odd `C5/C9` exclusion as a critical dependency;
10. shortest Petersen-core extraction and `C6/C8` annuli;
11. Type-T graph contraction or abstract `abba` deletion;
12. the historical ambient six-port assertion that one of four star matchings
    must be admitted by the original locked graph;
13. any classification of `1f57422...` as a complete proof draft.

### Retained but noncontrolling stronger mathematics

- R2.5 orientation/odd-core results;
- bounded `C6/C8` movies;
- marked genealogy and bubble-lift calculations;
- finite channel/profile algebra;
- the old outer shell, conditional on a cubic theorem.

### Retained on the v7.2 critical path

- audited R0/R1/R2.1/R2.2;
- source-level first-failure and critical-overlap tables;
- target-synchronized first-cancellation stopping;
- actual target category theorem;
- arbitrary-flow single pop;
- narrow full-state one-atom track interface;
- local seams, run identity strips and two-seam backtracks;
- explicit 2/3/4-cut and bounded consumers.

---

## 6. Current exact classification

\[
\boxed{
\begin{array}{c}
\text{v7.2 through first cancellation and single pop: reconstructed}\\
+\ \text{state-walk/seam/run/backtrack layer: reconstructed}\\
+\ \text{terminal census: reconstructed}\\
\hline
\text{pure-NNI prescribed-parent return: BLOCKED-PROOF}.
\end{array}}
\]

Therefore the branch is:

- **not** `COMPLETE-DRAFT`;
- **not** ready for independent full-theorem audit;
- ready only for focused independent verification of the reconstructed units and
  for Research Lead repair of the named blocker;
- not canonical, Lean-verified, manuscript-ready, release-ready, or a public
  five-CDC theorem.
