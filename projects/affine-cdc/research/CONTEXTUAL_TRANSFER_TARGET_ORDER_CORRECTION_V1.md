# Correction: reduced-closure order does not automatically lower the cap-context target

## Research dossier v1 — correction quarantine

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `37c4f5336f7754f9512907816bd7988017342abc`.

**Corrects the scope of:**

- `EQUALITY_RECURSION_VERTEX_DESCENT_V1.md`;
- `DDD_RECURSION_VERTEX_DESCENT_V1.md`;
- any checkpoint sentence asserting that every contextual equality/DDD recursive return automatically lowers the original cap-target vertex number by two.

**Retains:**

- every local four-root pairing classification in those dossiers;
- impossibility of quadruple equality at an inverse `2--2` flip;
- the inverse-cancellation equality/DDD trichotomy;
- exact localisation to one zero/co-root edge atom;
- strict order decrease measured on the reconnection-closure stages;
- all current-flow Pachner potentials and bounded terminal theorems.

**Status:** exact bookkeeping correction. Forward descent is constructed on a reconnection closure, whereas the root state to be transferred back lives on the original cap closure. The two graph families differ by the fixed two-vertex cap. A first failed contextual inverse step therefore targets the cap-attached stage, not automatically the smaller reconnection stage used in the earlier vertex count. If the forward prefix contains a cancellation, target order does decrease; a pure Pachner prefix may remain at the same cap-target order. The remaining same-order case is exactly the one-atom scheduling/coherence problem treated by the new critical-overlap and five-leaf circuit dossiers.

**Not implied:** failure of the overall proof route, invalidity of the local equality/DDD descent theorems, existence of an actual counterexample, complete contextual transfer, final proof-DAG closure, canonical acceptance, Lean verification, manuscript integration, release, publication, or the global five-support theorem.

---

## 1. Two closures of one four-pole

Let `P` be the ordered four-pole obtained by deleting the two vertices of one target inverse-dipole cap.

There are two different ways to close its four terminals.

### Reconnection closure

Choose one direct matching `E` of the four terminals and put

\[
\boxed{G(P)=P\cup E.}
\]

The matching contributes no new cubic vertices. This is the smaller graph on which minimality supplies a root-valued flow and on which the equality/DDD current-flow descent is constructed.

### Cap closure

Attach the original two-vertex cubic cap `C_i` and put

\[
\boxed{\widehat G(P)=P\cup C_i.}
\]

This graph contains two more vertices:

\[
\boxed{|V(\widehat G(P))|=|V(G(P))|+2.}
\]

It is the target graph whose five-support cover must ultimately be produced.

The two closures have the same four exterior incidences but are not the same graph and do not carry the same arbitrary root flows.

---

## 2. Forward current-flow descent

Let

\[
P_0\longrightarrow P_1\longrightarrow\cdots\longrightarrow P_m
\]

be a sequence of internal root Pachner flips and equal-face cancellations selected from a root-valued flow on the reconnection closure

\[
G_j=G(P_j)=P_j\cup E.
\]

Every forward move preserves the ordered four-pole boundary. Define the parallel cap-closure family

\[
\widehat G_j=\widehat G(P_j)=P_j\cup C_i.
\]

The current root flow used to choose the forward move is a flow on `G_j`. It need not extend to `widehat G_j`, because continued cap blocking is precisely the obstruction under study.

The bounded terminal and matching-flip theorems may produce a root flow on a later cap closure

\[
\widehat G_m.
\]

The contextual inverse-transfer problem is to move that cap-compatible flow through

\[
\widehat G_m\longrightarrow\widehat G_{m-1}\longrightarrow\cdots\longrightarrow\widehat G_0.
\]

It is not merely the inverse problem on the reconnection closures `G_j`.

---

## 3. Correct target of a failed contextual inverse step

Suppose the inverse step

\[
\widehat G_j\longrightarrow\widehat G_{j-1}
\]

first fails root-valuedly. Restoring the old local topology gives exactly one zero/co-root edge atom, by the first-failure theorem.

The graph carrying that contextual atom is

\[
\boxed{\widehat G_{j-1}=P_{j-1}\cup C_i.}
\]

The earlier recursion packets instead compared the reduced stage

\[
G_{j-1}=P_{j-1}\cup E
\]

with the outer target `widehat G_0`. The inequality

\[
|V(G_{j-1})|\le |V(G_0)|=|V(\widehat G_0)|-2
\]

is correct. But adding the fixed cap gives

\[
\boxed{
|V(\widehat G_{j-1})|
=|V(G_{j-1})|+2
\le |V(\widehat G_0)|.}
\]

This proves only nonincrease of the cap-context target order in general, not a strict drop by two.

---

## 4. When strict vertex descent is still valid

Let `c(j-1)` be the number of equal-face cancellations among the forward moves

\[
P_0\to\cdots\to P_{j-1}.
\]

Each such cancellation removes two vertices, whereas root Pachner flips preserve order. Therefore

\[
|V(P_{j-1})|
=|V(P_0)|-2c(j-1).
\]

Consequently

\[
\boxed{
|V(\widehat G_{j-1})|
=|V(\widehat G_0)|-2c(j-1).}
\]

### Theorem 4.1 — corrected order alternative

A first failed contextual inverse transfer satisfies exactly one of:

1. **cancellation has occurred:**  
   \[
   c(j-1)\ge1,
   \]
   and the cap-context target order is at least two smaller;

2. **pure Pachner prefix:**  
   \[
   c(j-1)=0,
   \]
   and the cap-context target may have the same vertex order as the outer target.

Thus strict vertex descent remains exact for every recursion reached behind at least one cancellation. The only unaccounted case is same-order first failure across a flip-only causal cone.

---

## 5. Scope correction to the equality recursion packet

The following statements from `EQUALITY_RECURSION_VERTEX_DESCENT_V1.md` remain exact:

- an inverse Pachner zero failure is the nonsingular doubled-intersecting branch;
- quadruple equality occurs only when reversing an equal-face cancellation;
- the failed local topology is one equality inverse-dipole atom;
- its reduced reconnection stage has order at most `|V(widehat G_0)|-2`.

The stronger sentence

> every contextual recursive equality target has at least two fewer vertices than the outer cap target

requires the additional hypothesis that the returned recursive object is the reduced closure `G_(j-1)` rather than the cap-attached stage `widehat G_(j-1)`, or that an earlier cancellation has already occurred.

Without that hypothesis it is quarantined.

---

## 6. Scope correction to the DDD recursion packet

The local DDD statements remain exact:

- inverse-flip co-root failure is one oriented DDD atom;
- inverse-cancellation equality/DDD trichotomy is complete;
- every stage of the reduced reconnection history has order at most the outer target minus two;
- mutual equality/DDD recursion cannot cycle if recursion is genuinely taken on those reduced closed graphs.

For contextual cap transfer, however, a co-root first failure behind only root Pachner flips may live on a cap-attached graph of the same order as the outer cap target.

Therefore the blanket common measure

\[
N=|V(\text{target graph})|
\]

is not yet a complete contextual-transfer measure unless `target graph` is explicitly the reduced reconnection closure. It cannot be silently applied to the cap-attached target.

---

## 7. The corrected residual frontier

After this correction, contextual inverse transfer has a clean dichotomy.

### Strict-order branch

If the failed atom lies behind at least one cancellation, recurse or invoke induction at strictly smaller cap-target order.

### Same-order branch

If the causal prefix consists only of root Pachner flips, the atom must be transported through a same-order flip history. This is exactly the frontier now controlled locally by:

1. `PACHNER_FIRST_FAILURE_CRITICAL_OVERLAP_V1.md`;
2. `FIVE_LEAF_PACHNER_PENTAGON_ROOT_INTERVAL_V1.md`;
3. `FIVE_LEAF_ROOT_TOPOLOGY_CYCLE_CLASSIFICATION_V1.md`;
4. `FIVE_LEAF_C5_C6_CONTEXTUAL_RETURN_V1.md`.

Those dossiers prove:

- disjoint critical moves commute;
- overlapping critical moves have one pentagon relation;
- a first-failure atom never branches;
- every local closed root sector is `C5` or `C6`;
- an oriented `C5` lap cannot close;
- a `C6` lap is the identity and is erasable.

Hence the correction does not reopen the finite or coefficient theory. It identifies the exact reason the final coherence theorem is necessary.

---

## 8. Correct well-founded measure target

A valid final contextual measure must begin with

\[
\boxed{
\bigl(
|V(\widehat G)|,
N_{\mathrm{cancelled\ before\ atom}},
\text{same-order Pachner scheduling data}
\bigr),}
\]

or an equivalent lexicographic ordering.

- any genuine cancellation lowers the first coordinate for the next cap-context problem;
- within a fixed order, the Pachner scheduling datum must decrease;
- route change exits through cap-profile escape;
- category failure exits through separator/degeneration;
- direct-pairing termination exits through bridge or soluble theta.

The remaining theorem is therefore a same-order Pachner coherence/scheduling theorem, not a missing equality/DDD recursion classification.

---

## 9. Trust boundary

### Exact here

- distinction between reconnection closure and cap closure;
- exact two-vertex order difference;
- identification of the cap-attached stage as the contextual inverse-transfer target;
- correction from strict decrease to nonincrease in a pure Pachner prefix;
- exact strict decrease after one or more cancellations;
- preservation of all local first-failure classifications;
- localisation of the remaining gap to same-order Pachner coherence.

### Quarantined

- unconditional use of `|V(G_(j-1))|<=|V(widehat G)|-2` as a count for the cap-attached contextual target;
- unconditional claim that every equality/DDD contextual recursive call lowers cap-target order by two;
- unconditional global acyclicity based solely on that vertex count.

### Still open

- local-to-global Pachner coherence in the root-valued triangle pseudocomplex;
- one strict same-order scheduling measure;
- complete contextual-transfer synthesis;
- final proof-DAG audit and well-founded packaging;
- canonical acceptance, independent audit, Lean verification, manuscript integration, release, publication;
- the global five-support theorem.
