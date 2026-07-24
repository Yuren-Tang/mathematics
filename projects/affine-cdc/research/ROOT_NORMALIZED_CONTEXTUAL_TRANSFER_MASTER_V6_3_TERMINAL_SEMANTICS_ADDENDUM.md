# Controlling terminal-semantics addendum to contextual transfer v6--v6.2

## Research Lead v6.3 — framewise terminal unwind and solution-valued return

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `1b23b773c5c09dae92ac26274b494b4d2a81c166`

**Controls together with:**

- `ROOT_NORMALIZED_CONTEXTUAL_TRANSFER_MASTER_V6.md`;
- `ROOT_NORMALIZED_CONTEXTUAL_TRANSFER_MASTER_V6_1_ADDENDUM.md`;
- `ROOT_NORMALIZED_CONTEXTUAL_TRANSFER_MASTER_V6_2_R2_6_ADDENDUM.md`;
- `LEVEL_SENSITIVE_TERMINAL_COLLAPSE_AND_OUTERMOST_UNWIND_V1.md` v1.1;
- `R2_TO_R1_CAP_RESTORATION_AND_OUTER_SHELL_INTERFACE_V1.md` read through this addendum.

**Supersedes exactly:**

- v6 Theorems 9.1 and 10.1 insofar as their external conclusion was `root state or accepted exit` without a theorem consuming every exit to a solution of the original target;
- v6.1's inherited use of that result type;
- the external `Q_N` result type in `AC_PD_5CDC_R2_7_MUTUAL_INDUCTION_HISTORY_WITNESS.md`;
- the claim in `AC_PD_5CDC_R2_7_CHILD_CONTEXT_FIDELITY.md` that every child route/bounded/separator/category exit is automatically a parent exit;
- the intermediate-exit stopping rule in `TERMINAL_UNWIND_FROM_CHILD_SEPARATOR_SOLUTION_V1.md`.

**Status:**

`R2.6 CLOSED AT RL AUTHORIAL LEVEL / R2.7 COMPLETE AUTHORIAL CANDIDATE (v6+v6.1+v6.2+v6.3) / PDL RECONSTRUCTION AND INDEPENDENT ASSURANCE REQUIRED`.

The word `complete` here is authorial and dependency-conditional. No accepted cap-restoration theorem, universal five-support theorem, Lean theorem, curation, manuscript, release, or publication status is asserted.

---

## 1. Internal control values versus external theorem values

The contextual state machine may internally expose:

- a continuing witnessed return;
- a cap-compatible descendant root state;
- a bounded direct/theta certificate;
- a separator or category certificate;
- a route/profile event.

These are not all external theorem conclusions.

The external proposition must return a root flow on the original target. Internal terminal values are consumed according to the level at which they occur.

### Continuing mode

A child history beginning at the inherited cancellation output is lifted source-faithfully and resumes the parent strategy.

### Terminal mode

Once any child result is terminal, the inherited continuation is abandoned permanently. The proof switches to framewise terminal unwind and never returns to continuing mode.

---

## 2. Corrected witnessed proposition

For every order `N`, define `Q_N^solve` as follows.

Let `G=P union cap_i` be a connected loopless bridgeless cubic graph of order at most `N`. Let `G_j=P union E_j` be one valid smaller cross closure and let `lambda` be any specified inherited root flow on `G_j`.

### Proposition `Q_N^solve`

There exists a root-valued `E_5` flow on `G`.

Moreover the proof provides either:

1. a finite decorated contextual history from `lambda` to an original-cap-compatible root state; or
2. a finite terminal-unwind certificate which abandons the inherited continuation, pops the stored call frames level by level, and ends in an exact outermost cap/bounded/small-cut construction producing a root flow on `G`.

A naked accepted-exit token is not a possible output.

---

## 3. Continuing resolved-call graph

The v6 resolved-call graph and rank

\[
d_N(x)=\operatorname{dist}_{M_N}(x,\mathcal X_N)
\]

continue to control only the continuing mode.

A continuing call edge consists of:

1. one selected parent cancellation;
2. a lower-order witnessed execution beginning at the inherited child flow;
3. a source-faithful child return;
4. labelled bubble compression;
5. an actual root/alternative/one-atom parent pop.

Every chosen continuing macro lowers `d_N`. Variable-order cycles are excluded by innermost-call elimination followed by the v6.2 fixed-order cellwise disposition.

If the child result is terminal, it is not represented as a continuing edge of `M_N`; the proof leaves this graph and enters terminal mode.

---

## 4. Terminal call stack

Suppose terminal mode begins inside a finite nested execution. Retain only the live stored cancellation frames.

For each frame `F_j` record:

- exact child target `H_j`;
- exact required parent target `G_j`;
- ordered output edge lineages `e_j,f_j`;
- labelled parent vertex slots;
- cap block, route, support, side-output, crossed-resolution, incidence, and surviving-mark data.

Every proper parent order in the stack is strictly less than the outer order `N`.

At the innermost live child target choose an ordinary root flow using the already available lower-order proposition `P_n`. This is permitted because terminal mode never resumes the inherited continuation.

---

## 5. One frame pop

Given a root flow on `H_j`, evaluate the actual roots

\[
p=\nu(e_j),\qquad q=\nu(f_j)
\]

and apply the exact insertion table:

- intersecting: original root insertion;
- equal: alternative root insertion;
- good disjoint: alternative root insertion;
- missing index: one standard atom;
- local degeneration: exact parent-level category outcome.

Then restore the required parent topology using only the pure fixed-order alphabet:

- ordinary target-arborescence `2--2` moves;
- local zero normalization;
- one-atom first-failure grammar;
- cellwise pivot-change seams and constant-run identity strips;
- normalized endpoint collars;
- periodic root crosscut.

No new cancellation call is opened inside one frame restoration.

The fixed-order process terminates by target-tree distance and the v6.2 no-neutral-recurrence theorem.

---

## 6. Proper lower-order reset

If the required parent order is `m<N`, then `P_m` is already available.

- If frame restoration reaches a root flow on the exact parent target, retain it.
- If it reaches a descendant cap state or any route/bounded/separator/category value, discard that value and invoke `P_m` on the exact parent target.

Use the resulting root flow as the child solution for the next enclosing frame.

Thus intermediate terminal data are not transported through the stack. In particular:

- no child cut-size persistence is assumed;
- no child route is identified with an ancestor route;
- no bounded child graph is identified with an ancestor graph;
- no intermediate exit is returned externally.

Only root flows on exact stored target graphs pass between frames.

---

## 7. Outermost order

At the final order-`N` frame, `P_N` is unavailable. Every result must therefore be consumed exactly.

1. **Root flow on the original target:** done.
2. **Cap-compatible descendant root state:** continue pure fixed-order restoration; internal moves preserve the ordered `K_i` boundary word; glue the original cap at the original topology.
3. **Zero-vertex direct matching:** bridge-plus-loops outer-shell case or explicit theta root triangle.
4. **Cyclic two-cut:** smaller edge completions, root alignment, gluing.
5. **Cyclic three-cut:** smaller one-vertex completions, triangle alignment, gluing.
6. **Cyclic four-cut:** smaller cap completions, physical profile intersection, Type-T/Type-H elimination.
7. **Acyclic low-port shore:** explicit one-vertex or two-vertex bounded gadget.
8. **Loop/bridge/singleton cut:** loop reinsertion or outer-shell decomposition.

A generic `category-safe` label is not an absorbing theorem. PDL must attach every admitted outermost category to one item in this census.

---

## 8. Terminal rank

Terminal mode is ranked by

\[
(r,\rho_{\rm fix}),
\]

where `r` is the number of live frames and `rho_fix` is the terminating fixed-order rank inside the current frame.

- `rho_fix` terminates one frame restoration.
- Completion or lower-order reset removes that frame.
- Therefore `r` strictly decreases.

Terminal mode is finite and cannot return to continuing mode.

---

## 9. Corrected mutual induction

Assume `P_n` and `Q_n^solve` for all `n<N`.

### First prove `Q_N^solve`

- Execute the specified inherited-flow strategy.
- Continuing calls use lower `Q_n^solve` only through their witnessed-history branch and are ranked by `(N,d_N)`.
- Any terminal result switches to framewise unwind.
- Proper lower levels use available `P_m` resets.
- The outermost level uses the exact terminal census.

Every branch yields a root flow on the original target.

### Then prove `P_N`

- Theta is explicit when no simple edge exists.
- Otherwise R1 supplies a valid smaller cross closure.
- Lower `P` supplies one initial root flow on it.
- `Q_N^solve` supplies a root flow on the original graph.

There is no exit-to-solution coercion.

---

## 10. Corrected contextual-transfer theorem

### Theorem 10.1 v6.3 — solution-valued contextual return

Let

\[
C_0\to C_1\to\cdots\to C_m
\]

be one finite mixed root-NNI/equal-face source history, and let a cap-compatible root state be given on `C_m`.

The controlling strategy produces a root-valued state on the original target `C_0` which glues the required cap, or an exact outermost bounded/small-cut construction which itself produces a root flow on the original cap closure.

The proof certificate is either:

- a complete continuing decorated inverse history; or
- a complete framewise terminal-unwind certificate.

No intermediate route/profile, bounded, separator, or category token is the final conclusion.

---

## 11. Impact on R2-to-R1

The corrected R2 consumer needed by R1 is now literal:

> from every inherited root flow on the selected valid cross closure, produce a root flow on the original cubic graph.

The four old result types become internal cases:

- Type I: continuing witnessed macro;
- Type II: cap-compatible root state, continued to the original topology;
- Type III: bounded direct/category case, absorbed only at the outermost level;
- Type IV: child separator/category trigger, collapsed to lower-order root flows and unwound framewise.

Only their final root-flow output is exported to R1.

---

## 12. PDL reconstruction obligations

PDL must reconstruct:

1. the solution-valued external statement `Q_N^solve`;
2. the irreversible mode switch from continuing to terminal;
3. exact frame-stack data and strict order of every proper parent target;
4. availability of `P_m` at all proper parent levels;
5. actual-root evaluation of every insertion;
6. pure fixed-order, no-new-call restoration in each frame;
7. v6.2 termination of one-atom restoration;
8. lower-level reset by exact-target `P_m` rather than terminal propagation;
9. continuation of descendant `K_i` root states to the required topology;
10. the complete outermost terminal census;
11. finite frame-count termination;
12. compatibility with suspended marks and full-labelled genealogy;
13. the corrected `Q_N^solve -> P_N` implication;
14. the final R2-to-R1 root-flow statement.

PDL should return either a complete-draft synthesis or one exact obstruction.

---

## 13. Assurance boundary

### Authorially closed here

- result-type correction;
- continuing/terminal mode split;
- lower-order reset semantics;
- framewise actual insertion and fixed-order restoration;
- outermost-only terminal absorption;
- terminal rank;
- solution-valued mutual induction and contextual return;
- exact R2-to-R1 output type.

### Still required

- PDL reconstruction of v6.2 and v6.3;
- final cap/route/category line audit;
- independent audit of all local movies, ranks, frame semantics, terminal consumers, and the complete dependency DAG.

### Not promoted

- PDL completion;
- independently assured R2.7 or cap restoration;
- universal five-support/five-CDC theorem;
- Lean, manuscript, curation, release, arXiv, DOI, peer review, or publication status.
