# Singular root-triality confluence — finite-condensation master theorem

## Research Lead master theorem v3

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `530b89123185166344c93b0913258e34a880b670`.

**Supersedes for controlling use:** `SINGULAR_ROOT_TRIALITY_CONFLUENCE_MASTER_THEOREM_V2.md`.

**Purpose:** remove the auxiliary lexicographic induction on history length. For one fixed forward history, all root states, first-failure states, history-prefix levels, and same-order token moves form one finite directed graph. The condensation DAG supplies the complete same-order rank. Only target order remains as an explicit induction parameter.

**Status:** exact abstract confluence theorem conditional on the same concrete full-labelled hypotheses as v2. It adds no independent assurance to those hypotheses.

---

## 1. Fixed target and fixed forward history

Let

\[
\mathcal H:
C_0\longrightarrow C_1\longrightarrow\cdots\longrightarrow C_m
\]

be one finite root-surgery history, consisting of root-valued `2--2` flips and equal-face `2--0` cancellations.

The transfer target is the original ordered cap context `C_0`. Let

\[
N=N(C_0)
\]

be its closed cap-context vertex order.

A transfer obligation has a **prefix level**

\[
\ell\in\{0,1,\ldots,m\},
\]

meaning that inverse transfer has already crossed the suffix after `C_ell`, while the prefix

\[
C_0\to\cdots\to C_\ell
\]

remains to be consumed.

Successful inverse transfer lowers `ell`. Same-order token motion never increases it. A genuine inverse-cancellation recursion lowers `N` by two.

---

## 2. Complete contextual state

A state records all data required to determine the next physical moves:

1. prefix level `ell`;
2. current ordered source multipole and all incidence identifications;
3. complete exterior root word;
4. either a root-valued flow or one normalized zero/co-root token;
5. token position and its labelled critical neighbourhood;
6. support transport and side-root attachments;
7. distinguished cap matching and distinguished cap block;
8. physical route orientation;
9. the current cap-compatible terminal obligation.

Coefficient-only, pivot-only, or support-unordered quotients are not states of the controlling graph.

---

## 3. The fixed-order contextual graph

For the fixed history `H` and target order `N`, let

\[
\mathscr X_N(\mathcal H)
\]

be the directed graph of all reachable complete contextual states before a genuine order-lowering cancellation.

Its edges are:

### Root-prefix edges

If the next inverse history move is root-valued, perform it and lower

\[
\ell\mapsto\ell-1.
\]

### First-failure edges

If the inverse move fails, replace the root state by the unique normalized one-edge zero/co-root state at the same prefix level.

### Same-level token edges

- immediate zero-to-root resolution;
- co-root relocation through a complete labelled critical overlap;
- constant-pivot full-state resolution;
- horizontal repair;
- root-valued alternative NNI;
- route/theta terminal normalisation.

### Exits

- `ell=0` with a cap-compatible root state;
- another cap-compatible original-context terminal;
- a genuine cancellation to target order `N-2`;
- an already accepted bounded/category discharge.

---

## 4. Finiteness

### Hypothesis S+

For fixed `N`, fixed exterior incidence set, five support labels, one token, and finitely many marks, there are only finitely many complete contextual states.

Indeed:

1. there are finitely many cubic multigraph types of order at most `N` on a fixed finite incidence set;
2. every edge/semiedge label lies in a finite alphabet;
3. the token, route, cap block, critical position, and prefix level have finite choices;
4. the forward history has finite length.

Hence

\[
\boxed{\mathscr X_N(\mathcal H)\text{ is finite}.}
\]

---

## 5. Local singular hypotheses

The controlling concrete hypotheses are unchanged.

### F — first-failure localisation

The first failed inverse move creates exactly one central edge labelled

\[
0\quad\text{or}\quad Q_i,
\]

and preserves all exterior and cap-orientation data.

### L — one-token grammar

Zero is immediately rootified unless it belongs to the inverse-cancellation strict-order layer. Every persistent same-order token is one co-root atom. Critical overlaps move it without branching.

### P — forced-backbone reduction

In a terminal-free recurrent token component:

1. constant-pivot runs are resolved with full side data retained;
2. immediate inverse backtracks are removable;
3. every repeated pivot contains a shortest positive pivot-closed subtrack projecting to a simple Petersen cycle of length `5,6,8,9`.

### O+ — oriented odd exclusion

The cap distinguishes one route block on every descendant. Every pivot-closed physical subtrack has zero orientation character, while that character equals pivot-length parity. Therefore every such subtrack has even length.

### E — even-core strict exit

Every full-state `C6` has the relative root-NNI-to-star movie and equal-face cancellation. Every `C8` decomposes into two seam-compatible `C6` source cells. Both leave the fixed-order graph through a genuine cancellation.

---

## 6. Prefix monotonicity

### Lemma 6.1

No edge of `X_N(H)` increases prefix level `ell`.

- root-valued inverse transfer lowers `ell`;
- first failure and token relocation preserve `ell`;
- terminal and cancellation edges leave the graph.

Consequently `ell` is constant on every strongly connected component.

### Corollary 6.2

A sink SCC containing a root-valued state is terminal.

If its constant level is positive, the next inverse step either:

1. succeeds and gives an outgoing lower-level edge; or
2. first fails and gives an outgoing token edge.

If its level is zero, the root state is already an original-context terminal.

Thus a nonterminal sink SCC must consist entirely of persistent token states at one fixed positive level.

---

## 7. No nonterminal sink SCC

### Theorem 7.1

Under F, L, P, O+, and E, the finite graph

\[
\mathscr X_N(\mathcal H)
\]

has no sink strongly connected component disjoint from all terminal and strict-order exits.

### Proof

Assume `K` is such a sink SCC.

By Corollary 6.2 it contains only persistent co-root token states at one prefix level.

Hypothesis P gives a shortest repeated-pivot simple Petersen subtrack. Hypothesis O+ makes its length even, so it is `C6` or `C8`. Hypothesis E supplies a genuine cancellation edge leaving the fixed-order graph.

This is an outgoing exit from `K`, contradicting sinkness. ∎

---

## 8. Condensation rank

Collapse every SCC of `X_N(H)` to one vertex. The result is a finite directed acyclic graph

\[
\operatorname{Cond}(\mathscr X_N(\mathcal H)).
\]

By Theorem 7.1, every sink of this DAG is a terminal or strict-order exit.

For an SCC `K`, define

\[
\operatorname{rk}(K)
\]

to be the maximum length of a directed path from `K` to a sink in the condensation DAG. This is a finite nonnegative integer.

### Proposition 8.1 — canonical same-order progress measure

From every nonterminal state there is an allowed transition which either:

1. leaves the fixed-order graph; or
2. enters an SCC of strictly smaller condensation rank.

Thus the condensation rank replaces all hand-written same-order scheduling and history-length bookkeeping.

No uniqueness of the progress path or Church--Rosser normal form is required.

---

## 9. Cover-independent transfer with one induction parameter

### Theorem 9.1 — finite-condensation contextual transfer

Assume for every cap-context order at most `N`:

1. finite singular-carrier Morse reduction;
2. F, L, S+, P, O+, and E;
3. route/direct terminal conversion;
4. componentwise recursion after genuine cancellation.

Then every cap-compatible terminal root state on `C_m` transfers to a cap-compatible root state on `C_0`.

### Proof

Induct only on target order `N`.

For the fixed history `H`, begin at its terminal root state in `X_N(H)`. Proposition 8.1 supplies a finite path through decreasing condensation rank to one of:

1. a root-valued original-context terminal;
2. an accepted cap/route/theta terminal which normalizes to the first case;
3. a genuine cancellation to target order `N-2`;
4. an already accepted bounded/category discharge.

In Case 3 apply the induction hypothesis on target order. No separate induction on `m` is used. ∎

---

## 10. Relation to v2

Version 2 used lexicographic induction on

\[
(N,m).
\]

Version 3 retains the finite history as part of the state data but replaces `m` as an explicit proof order by the canonical condensation rank of the complete fixed-order state graph.

The mathematical input is unchanged. The improvement is structural:

\[
\boxed{
\text{one outer induction on target order}
+
\text{one finite DAG reachability theorem}.}
\]

This is the preferred PDL formulation.

---

## 11. Concrete hypothesis map

### Singular Morse reduction

- `SINGULAR_CARRIER_DISCRETE_MORSE_UNIFICATION_V1.md`.

### F

- `PACHNER_HISTORY_FIRST_FAILURE_ONE_EDGE_ATOM_V1.md`.

### L

- root triality and zero removal;
- `PACHNER_FIRST_FAILURE_CRITICAL_OVERLAP_V1.md`;
- `FIRST_FAILURE_NORMALIZATION_AUTOMATIC_CATEGORY_SAFETY_V1.md`;
- route and theta terminal normalization.

### S+, P

- complete full-state contextual graph construction;
- `CONSTANT_PIVOT_FULL_STATE_CONTEXTUAL_CONSUMPTION_V1.md`;
- forced Petersen backbone and full-state corrections.

### O+

- `ORIENTED_CHANNEL_LOCK_BOUNDARY_CALIBRATION_V1.md`;
- `FORCED_DDD_BACKBONE_BINARY_TRANSPORT_V1.md`;
- `PETERSEN_RESOLUTION_PARITY_V1.md`;
- `ORIENTED_ODD_PETERSEN_SUBTRACK_EXCLUSION_V1.md`.

### E

- `PETERSEN_C6_CANONICAL_STAR_SECTION_V1.md`;
- `PETERSEN_C6_RELATIVE_STAR_MOVIE_DESCENT_V1.md`;
- `PETERSEN_C6_AUTOMATIC_CATEGORY_SAFETY_V1.md`;
- `PETERSEN_C8_TWO_C6_HISTORY_FILLING_REDUCTION_V1.md`.

---

## 12. PDL reconstruction target

PDL should reconstruct the theorem in this order:

1. define the complete state and prefix level;
2. prove finiteness without quotienting away source or cap data;
3. prove prefix monotonicity;
4. prove the orientation-hardened no-sink theorem;
5. pass to the condensation DAG;
6. use only target-order induction after genuine cancellation.

The proof should not reintroduce a second recursive theorem on history length.

---

## 13. Assurance boundary

### Proved abstractly here

- prefix level is SCC-constant;
- nonterminal sink SCCs reduce to persistent token SCCs;
- O+ and E eliminate those SCCs;
- the finite condensation DAG supplies a canonical same-order rank;
- contextual transfer needs only target-order induction.

### Not proved anew

- concrete first-failure or critical-overlap hypotheses;
- forced-backbone exhaustiveness;
- orientation calibration;
- `C6/C8` source movies;
- one-cross cap restoration;
- PDL acceptance, Lean verification, manuscript integration, release, peer review, publication, or established truth of five-CDC.
