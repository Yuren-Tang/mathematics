# AC-5CDC-AUDIT-SHELL-01 — independent cap/shell audit report

**Role:** `AffineCDC — Independent 5-CDC Cap/Shell Auditor`  
**Audit code:** `AC-5CDC-AUDIT-SHELL-01`  
**Controlling issue:** `Yuren-Tang/research-workbench#70`  
**Fixed candidate:** `proof-development/affine-cdc-rigour-v1@1f57422e0e415d8902d56eb294183815c0a0b640`  
**Frozen Research Lead source:** `research/affine-cdc-five-cdc-v1@71a10f9ba86c1d2b8b7885e78fa9baa303c77818`  
**Owned branch:** `audit/affine-cdc-five-cdc-shell-v1`  
**Exact branch base:** `1f57422e0e415d8902d56eb294183815c0a0b640`

## 1. Verdict

| Audit unit | Classification |
|---|---|
| K — R2-to-R1 cap/route consumer | `BLOCKED-PROOF` |
| L — general finite bridgeless outer shell | `ACCEPT` |
| End-to-end global assembly | `BLOCKED-PROOF` |

Final classification:

\[
\boxed{\texttt{MATERIAL CAP/OUTER-SHELL GAP — NO 5-CDC ACCEPTANCE}.}
\]

The material defect is in the cap/return consumer, not in the port-cycle outer shell.  Even granting the separately audited R2 core and contextual-return machinery, the frozen candidate does not prove the witnessed `Q_N` statement it uses in recursive cancellation calls.

## 2. Audit method

I treated the post-snapshot handoff at `2679f098...` only as an attack checklist.  I independently checked:

1. the graph-theoretic one-cross reduction and theta base;
2. the ten-state boundary algebra, including an exhaustive recomputation of the `640` conserved ordered root quadruples, ten state counts, `J_i`, `K_i`, `J_j\cap K_i`, and the sixteen route rows;
3. the exact quantifiers exported by `Q_N`, `P_N`, and `R2.7`;
4. the direct-pairing terminal at the level of the inherited labelled flow, rather than merely as an unlabelled terminal graph;
5. one-global-`S_5` trace alignment;
6. the port-cycle expansion, collapse, loop handling, support count, and standard even-subgraph `5`-CDC convention.

The internal correctness of R2.2--R2.6 and the no-sink proof inside R2.7 belongs to the companion core/return audits.  The present blocker survives even if those units are granted in full.

## 3. Accepted cap/shell interfaces

### 3.1 One selected cross is sufficient

`AC_PD_5CDC_R1_ONE_CROSS_STRUCTURAL_REDUCTION.md`, Theorem 7.1, proves that at every simple edge at least one of the two cross closures is simultaneously connected, loopless, bridgeless, cubic, and smaller by two vertices.  The proof handles connected and disconnected exteriors, old and new bridges, loops, repeated exterior endpoints, and parallel edges.  The induction therefore needs one selected valid cross, not all three reconnections and not a complete profile theorem.

### 3.2 Boundary and route quantifiers

The independent finite recomputation confirms:

\[
J_j=\{A,B_j,C_j\},\qquad
K_i=\{B_j,B_k,D_j,D_k\},\qquad
J_j\cap K_i=\{B_j\}.
\]

For the equality and DDD starting rows, exactly one non-`K_i` route remains, namely the literal original cap matching `M_i`.  Thus the candidate correctly separates:

- immediate `B_j` cap compatibility;
- separating rescue in the original four-pole context;
- the fixed original-cap route before the first route change.

### 3.3 Descendant route terminals

The cap consumer correctly states that a first route change produces a `K_i` terminal on the current descendant only.  It does not identify that state with the original profile before invoking `R2.7`.  This repairs the earlier descendant/original-profile quantifier shift.

### 3.4 One global support permutation

If two boundary states agree as multisets of five even traces, one bijection between equal trace occurrences gives a single permutation `pi in S_5`.  Applying that permutation globally to the cap-side support indices makes all five traces agree coordinatewise.  Since a terminal root is exactly the pair of support indices whose traces contain that terminal, all four terminal root labels then agree simultaneously.  No terminal-wise or edge-wise relabelling is needed.  Empty or repeated traces cause no obstruction: equal occurrences can be matched within their multiplicity classes.

### 3.5 Structural `Q_N`-then-`P_N` order

The phase order

\[
Q_N\quad\text{before}\quad P_N
\]

is formally noncircular: `Q_N` is intended to use only lower-order witnessed `Q_n` calls, while `P_N` uses lower-order `P_n` and same-level `Q_N`.  The theta graph is the exact no-simple-edge base.  This well-founded architecture is acceptable **conditional on actually proving the stated witnessed `Q_N`**.  Defect K-01 shows that the frozen candidate does not do so.

## 4. Material defect K-01 — direct terminal discards the inherited flow

### Exact targets

- `AC_PD_5CDC_R2_TO_R1_CAP_ROUTE_CONSUMER_AUDIT.md`, Section 6 and Theorem 9.1;
- `AC_PD_5CDC_R2_7_MUTUAL_INDUCTION_HISTORY_WITNESS.md`, definition and proof of `Q_N`;
- `AC_PD_5CDC_R2_7_WITNESSED_INNERMOST_BUBBLE_COMPRESSION.md`, strengthened recursive statement and `HW1` requirements;
- `AC_PD_5CDC_R2_7_RESOLVED_CALL_CONTEXTUAL_TRANSFER.md`, Theorem 8.1.

### Required quantifier

The frozen `Q_N` states:

> for **every specified inherited root flow** on the selected cross closure, there is an accepted exit or a finite decorated history **starting at that flow** and ending at a cap-compatible root terminal.

This strengthening is load-bearing: a cancellation child must return a move history from its inherited post-cancellation flow; an unrelated terminal recolouring cannot be lifted through the stored parent cancellation.

### What the direct-terminal proof actually does

When all source vertices disappear, the current direct matching still carries the boundary roots inherited from the specified starting flow and the forward surgery history.  Section 6 does not consume those roots.  Instead it says:

- for a cross matching, assign a root triangle to the resulting theta graph;
- for the same matching, give the two loops newly chosen distinct intersecting roots `p,q`, give the bridge value zero, and cross-resolve to theta.

These assignments prove that the **unlabelled terminal graph admits some root flow**.  They do not produce a declared generator history from the inherited terminal flow to that chosen flow.

### Smallest concrete configuration

Take the equality boundary state

\[
A=(p,p,p,p).
\]

At a cross direct matching, the two inherited matching edges both have root `p`.  After attaching the cap, the forced central value is `p+p=0`; the inherited assignment is not a root-valued theta.  Replacing the three theta-edge labels by an arbitrary triangle `p,q,p+q` changes at least one inherited edge label.  No root NNI, support switch, cancellation, or other declared history step is supplied for that change.

At the same-matching terminal, both inherited loops also carry `p`.  The proposed `(0,2,2)` move first replaces one loop label by a newly chosen intersecting root `q`; only **after that unproved recolouring** does the crossed zero resolution yield the root theta.

The DDD case is analogous: inherited loop or matching roots may be disjoint, so their sum is a co-root, whereas the proof replaces them by an intersecting pair.

### Defect class

`contextual / source-fidelity / quantifier mismatch`.

The local binary calculation

\[
(p,p,q,q)\mapsto(0,p+q,p+q)
\]

is correct when `p,q` are already distinct and intersecting.  The defect is the unsupported passage from the inherited direct-terminal labels to such a chosen pair.

### Downstream impact

This reintroduces the exact arbitrary-terminal-flow gap that witnessed `Q_N` was designed to remove.  In a recursive cancellation child, the returned direct-terminal branch supplies no history beginning at the inherited child flow, so:

1. `HW1` is not proved for every child branch;
2. witnessed bubble compression cannot be invoked on that branch;
3. `Q_N` is not established with its stated universal inherited-flow quantifier;
4. the subsequent `P_N` cubic induction is unavailable.

### Required repair

At least one of the following genuinely new statements is required:

1. a source-faithful direct-terminal theorem transporting the inherited direct-matching labels to a cap-compatible terminal through the declared move alphabet while preserving the complete context;
2. a proof that the problematic equality/DDD direct terminals cannot occur in the chosen witnessed execution;
3. a redesigned recursion that does not require an inherited-flow history, together with a replacement for bubble compression.

Merely retaining the arbitrary theta assignment or renaming it an accepted bounded exit does not repair `Q_N`.

## 5. Defect K-02 — unconsumed accepted-exit disjunction

### Exact targets

- `AC_PD_5CDC_R2_7_MUTUAL_INDUCTION_HISTORY_WITNESS.md`, Proposition `Q_N` and proof of `P_N`;
- `AC_PD_5CDC_R2_7_RESOLVED_CALL_CONTEXTUAL_TRANSFER.md`, Theorem 8.1;
- `AC_PD_5CDC_R2_TO_R1_CAP_ROUTE_CONSUMER_AUDIT.md`, Theorem 9.1 and Section 10.

### Defect

`Q_N` and `R2.7` repeatedly conclude either a cap-compatible terminal **or** an accepted route/profile, bounded, separator, category, theta, or cyclic-two-cut exit.  The proof of `P_N` then applies `Q_N` and immediately states that the terminal history supplies a root flow on the original graph.  It gives no case split and no exact theorem consuming every non-cap disjunct.

Some exits do have visible consumers:

- a descendant `K_i` route terminal is sent through contextual return and cap gluing;
- the cyclic two-cut branch has the standard two-shore completion/gluing disposition;
- a correctly labelled theta is explicit.

But the generic `bounded`, `separator`, and `category` flags are only declared to terminate the state graph.  The frozen shortest route does not provide an enumerated exit table with, for each flag, an exact theorem returning a root flow on the current original cap context.  The phrase “already consumed by the established outer branch” is not itself such a theorem.

### Smallest configuration

One reachable complete contextual state carrying any one of the generic accepted flags is enough: the conclusion of `Q_N` is then the exit disjunct, while the premise needed by `P_N` is existence of a root flow on the order-`N` graph.  The logical implication is absent unless a specific consumer theorem is supplied.

### Defect class and impact

`global theorem-interface / omitted consumer`.

This defect independently blocks the displayed deduction `Q_N => P_N`.  It may be repairable by a finite exact exit ledger if all consumers already exist, but they are not present in the frozen controlling route.

## 6. Unit L — general finite bridgeless outer shell

Unit L is accepted.

### 6.1 Definition

The convention used is the standard CDC convention: a cycle is an even subgraph, possibly disconnected, and a `5`-CDC is a collection of at most five such members covering every edge exactly twice.  Empty indexed supports may be omitted; repeated supports may remain as repeated members of the collection.

### 6.2 Components and loops

The cubic theorem is applied componentwise with one common index set `{1,2,3,4,5}` and supports are united by index.  Loops are deleted before expansion and reinserted into two fixed supports.  Since loops cross no cut and contribute degree two at their incident vertex, evenness and exact multiplicity two are preserved.  Pure-loop components and isolated vertices are covered by the same convention.

### 6.3 Port-cycle expansion

After loop deletion, every active vertex has nonloop degree at least two; a degree-one nonloop edge would be a bridge.  For degree `d>=3`, the ports form a `d`-cycle.  For degree two, two distinct parallel internal edges form the required two-cycle.  Each port has one external and two internal incidences, so the expansion is cubic and loopless.

Every internal edge lies on its fibre cycle.  Every external edge lifts a nonbridge original edge and hence lies on a lifted closed trail, so the expansion is bridgeless.  Parallel original edges and two-cycles cause no exception.

### 6.4 Collapse and projection

For each original vertex set `S`, the external edges crossing `delta_{G_0}(S)` are exactly the lifted external edges crossing `delta_H(pi^{-1}S)`; no fibre edge crosses.  Thus cut parity descends memberwise.  Singleton cuts then give vertex evenness downstairs.  Each original nonloop edge corresponds to one external edge, so its exact two-support multiplicity descends unchanged.  No support decomposition is performed, hence the number of members does not increase.

### 6.5 Scope

The argument covers finite, disconnected, looped, parallel-edge multigraphs under the project convention of bridgelessness.  Empty graphs and isolated vertices are vacuous.  Therefore the cubic five-support theorem, if available, would imply the standard finite bridgeless `5`-CDC theorem exactly as stated.

## 7. End-to-end interface disposition

The shortest advertised route

\[
R0\to R1\to R2.1\to R2.2\to R2.3\to R2.4\to R2.6\to R2.7
\to Q_N/P_N\to\text{outer shell}
\]

has a valid R0/R1/boundary/cap-alignment/outer-shell skeleton.  The phase-bit induction is also structurally well founded.  It nevertheless fails at the exported `R2.7 -> Q_N -> P_N` interface:

1. the direct terminal is solved by an unrelated terminal assignment rather than a history from the inherited flow;
2. the residual accepted-exit disjunction is not wholly consumed before `P_N` is asserted.

Accordingly no universal cubic root-flow theorem, and hence no universal finite `5`-CDC theorem, follows from the frozen candidate.

## 8. Assurance boundary

This report is an independent ordinary-mathematics audit of units K, L, and their global interfaces.  It does not assert a counterexample to the `5`-CDC conjecture.  It gives no Lean, Curator, canonical-corpus, manuscript, release, priority, peer-review, or publication status.