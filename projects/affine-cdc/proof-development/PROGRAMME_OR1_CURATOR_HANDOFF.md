# CURATION-HANDOFF — AC-PD-OR1 orientation obstruction

**Prepared by:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Authority:** research-workbench issue #37 comment `5049496439`  
**Branch:** `Yuren-Tang/mathematics:proof-development/affine-cdc-rigour-v1`  
**Safe boundary / exact base for this unit:** `9ce8de5ca5b7b41e139be4c94572de7725446046`  
**Authorial mathematical checkpoint:** `9dc0b3a5c906e51f8f1816e00b85f7aa2a744b1b`  
**DAG registration:** `29657f08253df87baa37ad09c88cce25904c189a`  
**Controlling integrated input:** `curation/affine-cdc-programme-a-b1-b8-unified-v1@ec765cd03271abd3588ec36faec3d53d0f8aa03b`  
**Checked reconstruction input:** `Yuren-Tang/affine-cdc:main@ebd7098a7a8b824e8c0a511d3c71f61705672aa8`  
**Classification:** `READY-FOR-CURATOR / FIXED-FIBRE CLASSIFICATION COMPLETE / COUNTEREXAMPLE TO PER-LIFT AUTOMATICITY / GLOBAL ORIENTED EXISTENCE OPEN`

## 1. Execution decision

AC-PDL consumed the priority insert directly. At activation, the persistent branch was exactly identical to the previous coherent handoff `9ce8de5c...`; no proof unit was in motion. Therefore direct execution did not interrupt Programme A/B dependency work, and no bounded child worker or branch was created.

## 2. Source and assurance discipline

Issue #49 return comment `5048974400` and AC-DIR disposition `5049236646` are triggering review/control inputs only. They are not promoted as accepted mathematics.

OR1 rederives every load-bearing claim from:

- the integrated Programme-A Fano solution torsor and retained-output boundary;
- the integrated Programme-B root-lift/surface and gauge/partial-Petrial theorems;
- the exact Lean definitions and theorems for `Msupp`, `partnerD`, `rho`, `rhoInv`, and `exists_indexed_dart_cover`;
- elementary signed-rotation, cochain, annihilator, and directed-trail arguments.

The result is authorial proof development. It is not an independent audit and is not end-to-end Lean verification.

## 3. Included files

- `AC_PD_OR1_1_SURFACE_AND_ORIENTATION_CLASS.md`;
- `AC_PD_OR1_2_GAUGE_FIBRE_AND_DUALITY.md`;
- `AC_PD_OR1_3_K4_AND_OUTER_SHELL_TRANSPORT.md`;
- `AC_PD_OR1_ORIENTATION_OBSTRUCTION_MAP.md`;
- `OBLIGATION_DAG.md` at the registered checkpoint.

Later PDL commits are excluded unless separately handed off.

## 4. Accepted authorial theorem package

### 4.1 Reconstruction

The indexed dart supports, unique same-vertex partners, edge reversal, and rotations reconstruct the exact cycle-face surface and its individual face occurrences. The current graph-level Lean `cubic_flow_cdc` theorem cannot substitute for this step because it explicitly discards the rotation and invokes generic undirected decomposition.

### 4.2 Fixed-lift obstruction

For a fixed compatible lift `g`, choosing vertex-disc orientations gives a twist word `w(g) in C^1(G)`. Its intrinsic class is

\[
\omega(g)=[w(g)]\in C^1(G)/Cut(G).
\]

The following are equivalent:

- the cycle-face surface is orientable;
- `omega(g)=0`;
- every source-cycle twist holonomy vanishes;
- the retained indexed face occurrences can be oriented so every edge is traversed once in each direction.

### 4.3 Gauge law and fixed fibre

For `k in H_f^0`, define `Lambda_f(k)` by

\[
k_u+k_v=\Lambda_f(k)_e f(e).
\]

Then

\[
w(g^k)=w(g)+\Lambda_f(k)
\]

for transported local orientations, and the quotient law holds modulo cuts.

The base-independent fixed-fibre class is

\[
\Omega_f
\in
C^1(G)/(Cut(G)+B_f),
\qquad B_f=im\Lambda_f.
\]

The orientable labelled lifts form either the empty set or one coset of `ker Lambda_or`. The fixed fibre contains an orientable lift exactly when `Omega_f=0`.

### 4.4 Dual criterion

Put

\[
Stress_{or}(f)=Z_1(G)\cap B_f^\perp.
\]

Then orientable-lift existence is equivalent to

\[
\langle w(g),z\rangle=0
\quad
(z\in Stress_{or}(f)).
\]

This orientation stress is distinct from the Programme-A compatibility stress.

### 4.5 Exact nonautomaticity

For the standard `K_4` Tait/Fano flow, one compatible lift has three quadrilateral faces and Euler characteristic one, while an all-edge gauge translation gives the tetrahedral sphere. Thus one fixed fibre contains both nonorientable and orientable lifts.

This refutes only **per-lift** automatic orientability. It does not refute universal fixed-fibre existence.

### 4.6 Outer shell

The current support-only collapse/decomposition route loses the orientation witness. OR1 proves the corrected enriched theorem:

- project each directed face circuit through the collapse datum;
- delete auxiliary edges to obtain directed closed trails;
- decompose them into directed circuits without reversing edges;
- preserve once-in-each-direction coverage of every original edge.

Under the explicit dart convention, removed loops can be reinserted as two oppositely directed singleton occurrences.

## 5. Exact open obligations

OR1 returns two genuine new-mathematics questions.

1. `AC-RL-OR-FIXED-FIBRE-VANISHING`: decide whether `Omega_f=0` for every nowhere-zero rank-three flow on every finite bridgeless cubic multigraph, or give an exact fixed-fibre counterexample.
2. `AC-RL-OR-GRAPH-EXISTENCE`: if the first statement fails, decide whether every such graph has some Fano flow with `Omega_f=0`.

Neither is closed or suggested as a corollary.

## 6. Recommended Curator destinations

Curator should integrate OR1 as a distinct orientation refinement, not into the ordinary CDC theorem statement without a separate packet. Natural destinations are:

- one orientation-obstruction chapter adjacent to the cycle-face/gauge material;
- the theorem dependency map, separating compatibility, ordinary CDC extraction, and oriented-lift existence;
- the assurance/formal-status surfaces, recording the exact Lean reconstruction boundary;
- the frontier map, recording the two orientation existence obligations;
- an outer-shell note distinguishing support-only collapse from enriched directed collapse.

The `K_4` example should be retained as an exact theorem/counterexample, not as census evidence.

## 7. Curator success test

A correct integration must visibly preserve:

1. fixed-lift `omega(g)` versus fixed-fibre `Omega_f`;
2. labelled-lift torsor versus unlabelled Petrial-word coset;
3. compatibility stress versus orientation stress;
4. per-lift nonautomaticity versus still-open fixed-fibre/global existence;
5. retained face occurrences versus generic support decomposition;
6. support-only collapse data loss versus the enriched oriented-collapse theorem;
7. loopless theorem scope and the explicit loop-dart reinsertion convention;
8. authorial, independent-audit, and Lean status as separate axes.

## 8. Exclusions

This handoff does not authorize or imply:

- an oriented CDC theorem for all bridgeless graphs;
- a change to Programme A ordinary CDC truth or Paper A;
- consumption of moving AC-RL work;
- mutation of the fixed candidate, Curator branch, audit branches, `main`, public issue #2, Lean, manuscript, release, publication, arXiv, DOI, tag, or workflow surfaces;
- a literature novelty or publication claim.

Only `projects/affine-cdc/proof-development/**` on the persistent PDL branch is changed.
