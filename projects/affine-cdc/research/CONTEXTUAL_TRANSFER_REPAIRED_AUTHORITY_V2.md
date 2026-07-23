# Repaired authority chain for contextual inverse transfer

## Research dossier v2 — post-tube-correction synthesis

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `082404dd7521e71a8886942a36a7d83fde6c5ee2`.

**Controlling correction:** `PTOLEMY_ROOT_TUBE_HISTORY_LIFT_SCOPE_CORRECTION_V1.md`.

**New repair inputs:**

- `PETERSEN_C6_CANONICAL_STAR_SECTION_V1.md`;
- `PETERSEN_C6_RELATIVE_STAR_MOVIE_DESCENT_V1.md`;
- `PETERSEN_C8_TWO_C6_HISTORY_FILLING_REDUCTION_V1.md`;
- `CONTEXTUAL_TRANSFER_TARGET_ORDER_CORRECTION_V1.md`;
- `ROUTE_CHANGE_TERMINAL_CONTEXTUAL_TRANSFER_V1.md`;
- `DDD_BOUNDED_RESIDUAL_ELIMINATION_V1.md`.

**Status:** exact authorial restoration of the even-track branch by a new source-level descent. The abstract longitudinal `C6/C8` tube words remain valid algebraic cycle-multipole flows but are not used as history lifts. A primitive Petersen `C6` annular cell is instead reduced relative to its two fixed turn corollas to a `(0,2,2)` triality. Every root-valued boundary restriction is the canonical star or one root NNI away from it. The star contains an equal-face dipole, so the track reaches strict cap-target order descent or a category exit. Every `C8` reduces to two compatible `C6` cells and inherits the same exit. Combined with odd-cycle orientation exclusion, no closed reduced Petersen track survives in a nonterminal same-order sink. Finite-state reachability and induction after a genuine cancellation therefore restore contextual inverse transfer at the authorial theorem level.

**Assurance boundary:** this is a research-branch synthesis, not downstream proof development, independent audit, curation, Lean verification, manuscript integration, release, or publication.

---

## 1. What remains quarantined

The following implication remains invalid and must not be used:

\[
\boxed{
\text{root flow on the abstract dual cycle multipole}
\Longrightarrow
\text{pointwise coherent lift of the original Ptolemy annulus}.}
\]

In particular, the longitudinal words printed in `PTOLEMY_EVEN_TRACK_ROOT_TUBE_FILLING_V1.md` do not become original atom-resolution pairs merely because they satisfy

\[
x_i+x_{i+1}=z_i.
\]

Sections of older dossiers which use that pointwise identification remain superseded by the scope correction.

The retained algebraic facts are:

- the side-root words of simple `C6` and `C8` tracks;
- the existence of root-valued abstract cycle multipoles with those words;
- the Petersen cycle classification;
- odd resolution parity.

The repaired proof below does not rely on the unsupported history interpretation.

---

## 2. Same-order contextual state graph

Fix:

- one cap-context vertex order `N`;
- the ordered outer four-port incidences;
- the oriented fixed cap route;
- the connected bridgeless cubic category with separator and bounded exits retained.

A same-order contextual state consists of one root flow or one normalized co-root atom state, together with its active history position, outer boundary, and resolution sheet.

There are finitely many such states at order `N`.

Allowed same-order transitions include:

- successful inverse root Pachner moves;
- horizontal root/Kempe rescue;
- disjoint critical commutations;
- normalized one-atom relocations;
- relative root NNIs inside a primitive Petersen cell.

A transition exits the same-order graph when it gives:

1. complete transfer;
2. a route/profile terminal;
3. a separator/category branch;
4. a bounded direct-pairing terminal;
5. an equal-face cancellation and hence lower cap-target order.

---

## 3. Persistent tracks

The retained first-failure and forced-backbone theorems give:

1. zero atoms do not persist in a pure same-order flip block;
2. every persistent atom is co-root/DDD;
3. the defect locus is nonbranching;
4. after deleting constant-pivot runs and history backtracks, a recurrent track contains a simple Petersen cycle;
5. the only simple cycle lengths are
   \[
   5,6,8,9.
   \]

Odd cycles `C5,C9` reverse the oriented resolution sheet and cannot close in one oriented cap lock.

Thus only `C6,C8` require a same-order disposition.

---

## 4. Repaired `C6` disposition

For one primitive `C6` cell, the adjacent constant-pivot turns determine fixed root corollas

\[
(x,t,z),
\qquad
(s,y,w).
\]

Relative to those corollas, the unresolved interface is

\[
(z,z,w,w).
\]

The exact three-topology table is:

\[
\boxed{
\text{zero path}
+
\text{root cross path}
+
\text{root canonical star}.}
\]

The two root topologies are joined by the unique root-preserving NNI, fixing all exterior and overlap data.

The canonical star contains two equal root triangles joined along the third side root. Therefore one equal-face cancellation removes two source vertices while preserving the complete local boundary.

Hence a primitive `C6` track gives:

\[
\boxed{
\text{lower cap-target order}
\quad\text{or}\quad
\text{separator/category exit}.}
\]

It is not a same-order return circuit.

---

## 5. Repaired `C8` disposition

Every simple Petersen `C8` is the symmetric difference of two simple `C6` cycles sharing a two-edge seam. Their side-root data satisfy:

- unchanged roots away from the seam;
- one equal internal seam root;
- root-triangle compatibility at the two seam endpoints.

The relative `C6` movie fixes all seam corollas. Apply it in either factor and cancel its internal equal-face dipole.

Therefore every `C8` also gives lower order or a category exit.

No independent abstract `C8` history relabelling is used.

---

## 6. No same-order sink

Assume a nonterminal sink strongly connected component exists in the finite same-order contextual graph.

A recurrent persistent atom track contains one simple Petersen cycle.

- `C5,C9` contradict oriented sheet return.
- `C6,C8` leave the component through strict cancellation or category exit.

Both alternatives contradict sinkness.

### Theorem 6.1 — repaired no-sink theorem

The same-order contextual state graph has no nonterminal sink strongly connected component.

### Corollary 6.2 — same-order progress

From every same-order contextual state, some finite allowed sequence reaches:

1. complete root transfer;
2. a cap-compatible route/profile terminal;
3. separator/category exit;
4. bounded direct-pairing completion;
5. strict target-order descent.

Existence of one progress path is sufficient; confluence is not required.

---

## 7. Strict-order induction

`CONTEXTUAL_TRANSFER_TARGET_ORDER_CORRECTION_V1.md` distinguishes:

- pure Pachner prefixes, which may remain at the same cap-target order;
- histories lying behind at least one genuine equal-face cancellation, whose cap-target order is lower by at least two.

Use induction on cap-target vertex order.

At one fixed order, apply Corollary 6.2. If the process reaches an actual cancellation, invoke the induction hypothesis. All other outcomes are terminal exits.

### Theorem 7.1 — repaired contextual inverse transfer

Every cap-compatible terminal root state produced by the equality or oriented DDD forward descent transfers to the original cap context, unless the instance is discharged by:

\[
\boxed{
\text{cap/profile lift},
\quad
\text{separator/category reduction},
\quad
\text{bounded direct-pairing completion}.}
\]

Nested contextual recursion is well founded.

---

## 8. Route-changing terminals

A route change occurring on a surgery descendant does not immediately prove membership in the original profile.

The exact ten-state route table first gives a state in the original cap set `K_i` on the descendant four-pole. Treat it as a cap-compatible terminal and apply Theorem 7.1. Only after the return may one conclude

\[
\Sigma(P_0)\cap K_i\ne\varnothing.
\]

This is the controlling interpretation from `ROUTE_CHANGE_TERMINAL_CONTEXTUAL_TRANSFER_V1.md`.

Initial horizontal rescue performed on `P_0` itself remains an immediate lift.

---

## 9. Forward endpoint alphabet

The equality and DDD current-flow descents now have the same exact nonrecursive endpoint classes:

1. cap-compatible root/profile terminal;
2. separator/category branch;
3. zero-vertex direct matching.

`DDD_BOUNDED_RESIDUAL_ELIMINATION_V1.md` removes the old generic “bounded DDD residual” placeholder. Every positive-vertex route-preserving DDD carrier still has a decreasing move or an exit.

Thus contextual transfer has no hidden finite family of endpoint sources.

---

## 10. Authoritative dependency chain

Read the contextual-transfer spine as:

\[
\begin{aligned}
&\text{first failure = one zero/co-root atom}\\
&\Downarrow\\
&\text{zero removal / forced Petersen backbone}\\
&\Downarrow\\
&\text{odd cycle orientation exclusion}\\
&\quad\text{or}\quad
\text{relative }C6\text{ star movie + cancellation}\\
&\quad\text{or}\quad
C8\to 2C6\to\text{cancellation}\\
&\Downarrow\\
&\text{no same-order sink}\\
&\Downarrow\\
&\text{strict order induction after cancellation}\\
&\Downarrow\\
&\text{terminal-to-original contextual return}.
\end{aligned}
\]

Do **not** replace the middle of this chain by “abstract longitudinal tube labels automatically lift the Ptolemy annulus.”

---

## 11. Supersession table

### Retained as exact local/algebraic inputs

- `PTOLEMY_CONTEXTUAL_COHERENCE_SCOPE_CORRECTION_V1.md`;
- `PACHNER_FIRST_FAILURE_CRITICAL_OVERLAP_V1.md`;
- `FORCED_DDD_BACKBONE_BINARY_TRANSPORT_V1.md`;
- `PETERSEN_RESOLUTION_PARITY_V1.md`;
- the side-word and cycle-multipole calculations in `PTOLEMY_EVEN_TRACK_ROOT_TUBE_FILLING_V1.md`.

### Controlling correction

- `PTOLEMY_ROOT_TUBE_HISTORY_LIFT_SCOPE_CORRECTION_V1.md`.

### New controlling even-track consumers

- `PETERSEN_C6_CANONICAL_STAR_SECTION_V1.md`;
- `PETERSEN_C6_RELATIVE_STAR_MOVIE_DESCENT_V1.md`;
- `PETERSEN_C8_TWO_C6_HISTORY_FILLING_REDUCTION_V1.md`.

### Read through the repaired chain

- the no-sink and contextual-transfer conclusions of older Ptolemy dossiers;
- Section 8 onward of `ORIENTED_FULL_CHANNEL_LOCK_ELIMINATION_SYNTHESIS_V1.md`;
- the contextual-transfer edge in `FIVE_SUPPORT_GLOBAL_MINIMAL_COUNTEREXAMPLE_CLOSURE_V1.md`.

The conclusions may be used only with the repaired relative-star descent, not with the quarantined abstract-tube implication.

---

## 12. Trust boundary

### Exact at the research-branch authorial level

- finite same-order contextual state space;
- persistent-track reduction to simple Petersen cycles;
- odd-cycle exclusion;
- relative root movie and strict cancellation for `C6`;
- reduction and strict descent for `C8`;
- repaired no-sink theorem;
- induction after genuine cancellation;
- route-terminal return to the original four-pole;
- removal of a generic bounded DDD residual;
- repaired contextual inverse-transfer synthesis.

### Not claimed

- downstream independent reconstruction of the relative annular incidence model;
- canonical corpus acceptance;
- Lean verification;
- manuscript integration;
- release, arXiv, DOI, peer review, or publication.
