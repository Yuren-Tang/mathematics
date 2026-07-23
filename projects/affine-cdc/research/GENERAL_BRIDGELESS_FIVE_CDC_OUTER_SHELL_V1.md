# The cubic five-support theorem implies the full finite bridgeless 5-CDC theorem

## Research dossier v1 — outer-shell closure

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `7d9e5c9631e87508fbb1a179e1c5bd66061ecd88`.

**Parents:**

- `projects/affine-cdc/reduction/outer-shell-and-binary-flow.md`;
- `projects/affine-cdc/reduction/even-cover-and-collapse.md`;
- `projects/affine-cdc/five-support/root-flow-lifting.md`;
- `GLOBAL_CAP_LIFT_INTERFACE_COMPATIBILITY_V1.md`;
- `FIVE_SUPPORT_GLOBAL_MINIMAL_COUNTEREXAMPLE_CLOSURE_V1.md`.

**Status:** exact authorial reduction from the finite bridgeless cubic five-support candidate to the standard finite bridgeless 5-cycle-double-cover statement. Port-cycle expansion produces a finite loopless bridgeless cubic multigraph. Apply the cubic theorem componentwise to obtain exactly five indexed vertex-even supports. Convert them to cut-even supports, project the same five supports through the collapse map, and reinsert every deleted loop into two fixed supports. Thus the number of support members remains five throughout; no final circuit decomposition that increases the member count is needed.

**Assurance boundary:** this theorem is conditional on the cubic five-support candidate at the exact inherited authorial scope. It does not independently verify that candidate, confer canonical acceptance, or claim Lean/manuscript/release/publication status.

---

## 1. External five-cycle convention

For a finite multigraph, a **cycle** in the cycle-double-cover literature may be taken to mean an even subgraph, not necessarily a connected circuit. A `5-CDC` is a family of five even subgraphs such that every edge belongs to exactly two family members.

This is exactly the project object called an indexed five-support cover:

\[
(F_1,F_2,F_3,F_4,F_5),
\]

where each `F_i` is even and every edge occurs in exactly two supports. Empty and repeated supports are allowed.

On a loopless graph, vertex-evenness and cut-evenness agree. On a graph with loops, cut-evenness is the intrinsic convention because a loop crosses no cut.

No connected-circuit decomposition is required to obtain a 5-CDC. Decomposition is useful for the unrestricted CDC shell, but would generally increase the number of family members and is therefore deliberately omitted here.

---

## 2. Cubic input theorem

Assume the following inherited cubic statement.

### Cubic five-support candidate

Every finite connected loopless bridgeless cubic multigraph `H` admits five indexed vertex-even supports

\[
(F'_1,\ldots,F'_5)
\]

such that every edge of `H` belongs to exactly two of them.

The connected theorem immediately extends componentwise to every finite loopless bridgeless cubic multigraph, using the same global index set `{1,2,3,4,5}`. Isolated vertices are irrelevant and the empty graph has the empty five-tuple.

Equivalently, each connected cubic component admits a root-valued `E_5` flow and the component flows assemble.

---

## 3. Delete loops from the original graph

Let `G` be a multigraph with finite active edge set and no singleton cut. Connectedness is not assumed. Parallel edges and loops are allowed.

Let

\[
L\subseteq E(G)
\]

be the set of loops, and let `G_0` be obtained by deleting all loops.

Loops cross no cut. Therefore:

1. deleting loops preserves every cut on nonloop edges;
2. `G_0` remains loopless and has no singleton cut;
3. `E(G_0)` is finite.

Active degree one cannot occur in `G_0`, because the unique incident nonloop edge would form a singleton cut.

---

## 4. Port-cycle cubic expansion

Choose a cyclic order on the incidence set at every active vertex of `G_0`. Form the port-cycle expansion `H`:

- one port vertex `(v,e)` for every incidence of `e` at `v`;
- one lifted external edge `lambda(e)` for every edge `e` of `G_0`;
- one internal cycle through the ports over each active vertex `v`;
- a degree-two fibre is represented by two distinct parallel internal edges.

The established expansion theorem gives:

\[
\boxed{
H\text{ finite, loopless, cubic, and without singleton cuts}.}
\]

It also gives collapse data

\[
\pi:V(H)\to V(G_0),
\qquad
\lambda:E(G_0)\hookrightarrow E(H),
\]

such that:

1. `lambda(e)` joins the fibres over the endpoints of `e`;
2. every edge joining distinct fibres is one unique lifted original edge;
3. every auxiliary edge lies inside one fibre.

The construction is componentwise. Hence `H` need not be connected, but each edge-bearing component is a finite loopless bridgeless cubic multigraph.

---

## 5. Apply the cubic theorem without changing the index set

Apply the cubic five-support theorem to every connected component of `H` and unite equal-index supports across components. This gives exactly five supports

\[
F'_1,F'_2,F'_3,F'_4,F'_5\subseteq E(H)
\]

such that:

1. every `F'_i` is vertex-even in `H`;
2. every edge of `H` belongs to exactly two of the five supports.

Because `H` is loopless,

\[
F'_i\text{ vertex-even}
\iff
F'_i\text{ cut-even}.
\]

Thus all five `F'_i` are cut-even.

This step uses no rank-three binary-flow choice or eight-support affine family. The port-cycle expansion is flow-independent, and the new cubic five-support theorem is applied directly to `H`.

---

## 6. Project the same five supports through collapse

For each `i in {1,...,5}`, define

\[
F_i^0
=
\operatorname{proj}(F'_i)
:=
\{e\in E(G_0):\lambda(e)\in F'_i\}.
\]

### Theorem 6.1 — memberwise cut-even transport

Every `F_i^0` is cut-even in `G_0`.

### Proof

For every vertex set `S subseteq V(G_0)`, the collapse datum identifies

\[
e\in\delta_{G_0}(S)
\iff
\lambda(e)\in\delta_H(\pi^{-1}S).
\]

Hence `F_i^0 cap delta_(G_0)(S)` and `F'_i cap delta_H(pi^{-1}S)` correspond bijectively. The latter has even cardinality because `F'_i` is cut-even. Therefore the former is even. ∎

### Theorem 6.2 — exact double coverage survives projection

Every nonloop edge `e` of `G` belongs to exactly two of

\[
F_1^0,\ldots,F_5^0.
\]

### Proof

By definition,

\[
e\in F_i^0
\iff
\lambda(e)\in F'_i.
\]

The lifted edge `lambda(e)` belongs to exactly two upstairs supports. Therefore `e` belongs to the same two indexed downstairs supports. ∎

Distinct upstairs supports may project to equal or empty downstairs supports. This is harmless: the five indices remain distinct family occurrences.

Thus

\[
(F_1^0,\ldots,F_5^0)
\]

is a five-member cut-even double cover of the loopless core `G_0`.

---

## 7. Reinsert loops without adding family members

Choose two fixed distinct indices, say `1` and `2`, and put

\[
F_1=F_1^0\cup L,
\qquad
F_2=F_2^0\cup L,
\qquad
F_i=F_i^0\quad(i=3,4,5).
\]

### Lemma 7.1 — loop insertion preserves cut parity

Each `F_i` is cut-even in `G`.

### Proof

Loops lie in no cut. Adding any set of loops to a cut-even support therefore changes no cut intersection. ∎

### Lemma 7.2 — loop coverage

Every loop belongs to exactly the two supports `F_1,F_2`; every nonloop edge retains its exact two-support membership from `G_0`.

Therefore

\[
(F_1,F_2,F_3,F_4,F_5)
\]

is a five-member cut-even double cover of `G`.

The same construction works with any fixed pair of support indices. No singleton-loop circuit occurrences are appended, so the support count remains exactly five.

---

## 8. Full theorem

### Theorem 8.1 — finite bridgeless 5-CDC outer-shell theorem

Assume every finite connected loopless bridgeless cubic multigraph has an indexed five-support even double cover.

Then every multigraph `G` with finite active edge set and no singleton cut has five cut-even edge supports

\[
\boxed{(F_1,F_2,F_3,F_4,F_5)}
\]

such that every edge belongs to exactly two supports.

Equivalently, every finite bridgeless multigraph has a `5`-cycle double cover in the standard even-subgraph sense.

### Proof

Delete loops, perform the port-cycle expansion, apply the cubic theorem componentwise, convert vertex-even supports to cut-even supports upstairs, project all five supports memberwise, and add every loop to two fixed supports. Sections 3--7 prove each step and preserve exact double coverage. ∎

---

## 9. Root-flow corollary on general graphs

From the five supports define for every edge `e`

\[
\lambda_G(e)=e_i+e_j
\]

where `{i,j}` is the pair of support indices containing `e`.

Every value is one root of `R_5`. At every loopless vertex, coordinatewise evenness gives

\[
\sum_{e\ni v}\lambda_G(e)=0.
\]

For a general multigraph the cut-even support formulation is the intrinsic theorem; an oriented boundary convention makes loop contributions cancel. The local `K_5` triangle law is special to cubic vertices and is not asserted for higher-degree vertices.

Thus the cubic root-flow theorem extends globally as a five-support/cut-even theorem, while its triangle-complex geometry remains the cubic proof engine.

---

## 10. Exact dependency spine

The full graph-level implication is

\[
\begin{aligned}
&\text{finite bridgeless multigraph }G\\
&\Downarrow\quad\text{delete loops}\\
&\text{finite loopless bridgeless }G_0\\
&\Downarrow\quad\text{port-cycle expansion}\\
&\text{finite loopless bridgeless cubic }H\\
&\Downarrow\quad\text{cubic five-support theorem, componentwise}\\
&\text{five vertex-even supports on }H\\
&\Downarrow\quad\text{vertex-even }\Leftrightarrow\text{ cut-even}\\
&\text{five cut-even supports on }H\\
&\Downarrow\quad\text{memberwise collapse projection}\\
&\text{five cut-even supports on }G_0\\
&\Downarrow\quad\text{insert loops in two fixed supports}\\
&\text{five cut-even supports on }G.
\end{aligned}
\]

Every arrow is support-count preserving.

---

## 11. Consequence for the present candidate

Combining Theorem 8.1 with the current cubic authorial candidate gives the full research-branch endpoint:

\[
\boxed{
\text{Every finite bridgeless multigraph has a five-cycle double cover.}
}
\]

This is a stronger endpoint statement than the cubic dossier currently prints, but it introduces no new local obstruction theory. Its only additional mathematics is the established expansion/collapse outer shell together with the support-count-preserving loop insertion of Section 7.

The conclusion remains a research-branch candidate until the cubic proof and this outer-shell interface pass the downstream project assurance stages.

---

## 12. Trust boundary

### Exact in this dossier

- standard five-member even-subgraph interpretation of `5-CDC`;
- deletion of loops while preserving nonloop cuts;
- use of the existing finite port-cycle cubic expansion;
- componentwise application of the connected cubic theorem with one common five-index set;
- vertex-even to cut-even conversion on the loopless expansion;
- memberwise projection of exactly five supports;
- preservation of exact double coverage under edge lift/projection;
- reinsertion of all loops into two fixed supports without increasing the family size;
- deduction of the full finite bridgeless-multigraph statement from the cubic theorem.

### Imported authorial mathematics

- the cubic five-support candidate and its complete local/global dependency chain;
- port-cycle expansion and preservation of bridgelessness;
- pure cut-even collapse transport.

### Still outside this checkpoint

- proof-development expansion or repair of imported theorems;
- independent audit;
- curation or canonical movement;
- Lean verification;
- manuscript integration;
- release, arXiv, DOI, peer review, or publication.
