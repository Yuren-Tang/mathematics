# V7 reverse dependency and no-circularity audit

## Research Lead dependency audit v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `840658abeaead5ad8cec6d93a9f7b150165a762b`

**Audited controlling package:**

- `ROOT_NORMALIZED_CONTEXTUAL_TRANSFER_MASTER_V7_FIRST_CANCELLATION_RETURN.md`;
- `ROOT_NORMALIZED_CONTEXTUAL_TRANSFER_MASTER_V7_1_SCOPE_AND_ALPHABET_ADDENDUM.md`;
- `FIRST_CANCELLATION_TARGET_CAP_TERMINALISATION_V1.md`;
- `FIRST_CANCELLATION_SINGLE_POP_TARGET_TOPOLOGY_SCOPE_CORRECTION_V1.md`;
- `FIRST_CANCELLATION_FIXED_ORDER_NO_REOPENING_V1.md`;
- `ONE_CROSS_PROOF_DAG_AND_SUPERSESSION_INDEX_V5.md`.

**Question audited:** does any theorem used to prove the order-`N` cap-restoration proposition invoke the same order-`N` proposition, an equivalent universal cap theorem, or a mixed-order child-history theorem whose termination presupposes the desired result?

**Authorial answer:** no such call appears in the v7 dependency graph. Every order-lowering use is an ordinary proposition `P_m` with `m<N`; every same-order use is structural, finite-state, fixed-order, or a local/cut construction whose recursive completions are strictly smaller. The prior v6 variable-order machinery is not a v7 dependency.

This is a branch-internal dependency audit, not independent mathematical assurance.

---

## 1. Induction statement

Let `P_N` denote:

> every connected loopless bridgeless cubic multigraph with at most `N` vertices carries a root-valued `E_5` flow.

The v7 induction step assumes only:

\[
P_m\qquad(m<N)
\]

and proves `P_N`.

The cap-restoration unit used in this step is not separately assumed. It is proved from lower `P_m` and fixed-order mathematics.

---

## 2. R1 valid-cross theorem is nonrecursive

`ONE_CROSS_RECONNECTION_EXISTENCE_V1.md` uses only:

- connectedness and bridgelessness of the original graph;
- cubic degree;
- component incidence counts after deleting two adjacent vertices;
- nonbridge status of the two new cross edges;
- laminarity of bridge cuts in the exterior graph;
- incompatibility of the two crossing terminal partitions;
- elementary loop/bridge incidence arguments.

It does not invoke:

- a root flow;
- lower `P_m`;
- cap restoration;
- cut gluing;
- Type T/H;
- R2.4--R2.7.

Its output is one valid cross closure of order `N-2`.

Only after the structural theorem is complete does the induction hypothesis `P_{N-2}` supply a root flow on that cross closure.

---

## 3. One-cross boundary reduction is same-graph finite algebra

`ONE_CROSS_SINGULAR_FIXED_ROUTE_REDUCTION_V1.md` consumes one specified cross flow and the exact ten-state route table.

It uses:

- finite boundary trace classification;
- physical Kempe component connectivity;
- route matching of one selected challenge;
- horizontal rescue when the challenge separates.

It makes no lower-order call and assumes no cap-restoration theorem.

Its output is immediate cap gluing/rescue or one equality/DDD fixed-route lock.

---

## 4. Equality and DDD potentials are finite forward descent

The equality and DDD no-local-minimum theorems are finite local tables on the current root-labelled cross flow.

Internal accepted steps are root-valued `2--2` NNIs with strict decrease of:

\[
(E,\Phi,|V|)
\quad\text{or}\quad
(\Omega,|V|).
\]

No theorem of root solubility is invoked to obtain the next move.

V7 stops before the first cancellation, so the potential phase contains no lower-order recursion.

---

## 5. Parallel target testing has no same-order solution assumption

The cross NNI is root-valued, but the parallel target need not carry a flow.

The target test uses the purely topological NNI alternative:

- valid connected loopless bridgeless cubic output; or
- cyclic two-cut in the current target; or
- bounded acyclic/parallel low-port degeneration.

The structural alternative does not use `P_N`.

If a cut/bounded branch occurs, its **solution** uses only the strict-lower completions audited in Section 9 below.

---

## 6. First-cancellation child target is strictly smaller

At the selected first cancellation, `CHILD_CONTEXT_FIDELITY_AFTER_ROOT_CANCELLATION_V1.md` distinguishes:

1. disconnected child cross output -> parent cut/bounded branch;
2. invalid parallel child target -> parent cut/bounded branch;
3. child route/cap state;
4. valid child target cap closure
   \[
   \widehat G^-=P^-\cup C_i
   \]
   with
   \[
   |V(\widehat G^-)|=N-2.
   \]

The graph-category statement is structural. In the genuine child case, ordinary `P_{N-2}` applies to the actual target cap closure.

No lower witnessed `Q_{N-2}` or inherited-flow extension theorem is invoked.

---

## 7. Arbitrary-flow single pop is local

The inverse-cancellation table depends only on:

- the two actual roots on the stored child output lineages;
- the exact root intersection/equality/disjointness relation;
- a bounded adjacent three-vertex borrowing neighbourhood;
- the missing-index Petersen combinatorics.

Its outcomes are:

- original root insertion;
- equality alternative root insertion;
- good-disjoint alternative root insertion;
- one standard missing-index atom;
- bounded/small-cut local terminal.

The theorem does not assume a path from the inherited child flow to the selected lower target flow. It does not invoke `P_N`.

Alternative source topologies are normalized by same-order target scheduling, not by another cancellation.

---

## 8. Fixed-order return is order-preserving

The target-rooted topology arborescence is constructed in a finite uncoloured ordinary `2--2` move component.

It uses no root-solubility theorem. Root labels are tested only after one parent edge is selected.

The fixed-order state graph contains:

- root states;
- at most one normalized co-root atom;
- complete ordered cap/route/incidence data.

The internal alphabet contains no `2--0/0--2` move.

### R2.4

The full-state forced-backbone theorem is a finite local/combinatorial reduction of one atom track to:

- rootification;
- exact exit;
- or one forced Petersen pivot chain.

No lower graph is solved.

### R2.5

The oriented odd-core exclusion uses the fixed physical cap block and the resolution/block-exchange character. It excludes odd pivot-closed cores at the same order.

No lower graph is solved.

### R2.6

The repaired cellwise theorem uses:

- local `(0,2,2)` pivot-change root seams;
- identity subdivision;
- uniqueness of the nonpivot root section on constant runs;
- identity-product strips;
- complete-state seam gluing;
- legal fixed-order periodic crosscuts.

No graph-order descent or lower theorem occurs.

Thus the fixed-order return terminates or exits without invoking `P_N` or any `P_m`.

---

## 9. Small-cut and bounded consumers use only strict-lower inputs

### Two-cut

Each shore completion adds one edge and is strictly smaller than the order-`N` graph. Lower `P_m` solves both completions. One support permutation aligns the completion roots.

### Three-cut

Each cyclic shore completion adds one cubic vertex and is strictly smaller. Lower `P_m` solves both completions. One support permutation aligns the boundary root triangles.

### Four-cut

Each proper cyclic shore cap completion adds two cap vertices while replacing the opposite cyclic shore, hence is strictly smaller. Lower `P_m` supplies all three cap profiles on each shore.

The finite disjoint-profile classification reduces a hypothetical mismatch to Type T or Type H.

- Type T is eliminated by disjoint-support route invariance.
- Type H is eliminated by the same physical commutation law in the BBD and DDD triangle policies.

Neither Type T nor Type H invokes R2-v7, cap restoration, or `P_N`.

### Acyclic low-port shore

The cubic degree formula gives exactly one vertex at three ports or two vertices at four ports. These are explicit bounded gadgets.

### Loop/bridge/theta

These are direct outer-shell or explicit root-triangle constructions.

Therefore every same-order terminal is consumed using only lower `P_m` or direct finite mathematics.

---

## 10. Route/cap terminals are root states, not recursive claims

A route/profile event yields a root-valued boundary state in `K_i` on the current four-pole. Gluing the physical cap gives a root flow on the current target topology.

The fixed-order pure-NNI theorem then transfers that supplied root state back to the original topology.

No theorem asserting cap restoration from an arbitrary cross flow is used at this point; the current cap already glues root-valuedly.

---

## 11. Complete dependency order

One topological ordering of the v7 proof DAG is:

1. finite root/support arithmetic and ten-state boundary table;
2. graph structural lemmas and R1 one-cross survival;
3. cut completion category and Type T/H physical eliminations;
4. equality/DDD local potential tables;
5. root-NNI and first-cancellation target-category lemmas;
6. arbitrary-flow inverse insertion tables;
7. first-failure/critical-overlap local grammar;
8. fixed-order topology arborescence;
9. R2.4 forced backbone;
10. R2.5 odd-core exclusion;
11. repaired R2.6 cellwise even-track erasure;
12. pure fixed-order no-reopening return;
13. first-cancellation terminalisation;
14. one-cross cap restoration `R_N`;
15. ordinary induction `P_{<N}->P_N`;
16. general loop/bridge outer shell.

No arrow points from an earlier node to node 14 or 15.

---

## 12. Superseded cyclic dependencies

The following potential circularities belong only to the noncontrolling mixed-history route:

- lower `Q_n` history witnesses;
- child-history weld lifting;
- nested bubble compression;
- variable-order recurrence and call SCCs;
- terminal frame-stack semantics.

V7 deletes those edges from the controlling DAG by stopping at the first cancellation and using ordinary `P_{N-2}` on the actual child target.

---

## 13. Remaining audit risk

No dependency cycle was found. The remaining risks are mathematical correctness of individual acyclic nodes:

1. equality and DDD potential tables;
2. parallel target NNI/cancellation category maps;
3. arbitrary-flow insertion rows;
4. target-topology containment of alternative insertions;
5. R2.4/R2.5 finite classifications;
6. cellwise seam/run and periodic-crosscut realization;
7. Type T/H finite mismatch elimination;
8. exact terminal census.

These require PDL reconstruction and independent audit.

---

## 14. Classification

### Authorial audit result

\[
\boxed{
\text{V7 CONTROLLING DEPENDENCY DAG ACYCLIC AT AUTHORIAL LEVEL}.}
\]

### Required assurance

- PDL line-by-line reconstruction;
- independent reverse-DAG audit;
- canonical receiver decision.

### Not claimed

- accepted cap restoration;
- established five-support/five-CDC theorem;
- Lean verification;
- Curator/canonical corpus movement;
- manuscript, release, arXiv, DOI, peer review, or publication status.
