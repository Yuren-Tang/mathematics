# Root-normalized contextual transfer with periodic endpoint discharge

## Research Lead master theorem v5 — repaired R2.7 assembly

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`

**Supersedes for controlling Research Lead authorial use:**

- `ROOT_NORMALIZED_CONTEXTUAL_TRANSFER_MASTER_V4.md`;
- `CONTEXTUAL_TRANSFER_REPAIR_FRONTIER_V2.md` as an open-frontier description;
- every earlier contextual master which treated an equal-face cancellation as an automatically completed lower-order recursive exit;
- every earlier fixed-order argument which erased internal closed tracks but did not discharge an unresolved outer endpoint.

**Controlling repair inputs:**

- `ROOT_VALUED_ALTERNATIVE_INVERSE_CANCELLATION_INSERTION_V1.md`;
- `DOUBLED_DISJOINT_THREE_VERTEX_BORROWING_DICHOTOMY_V1.md`;
- first-failure one-edge localisation and normalized critical-overlap theorems;
- full-labelled forced-backbone and constant-pivot transport;
- oriented odd pivot-closed exclusion;
- `PTOLEMY_CLOSED_DEFECT_TRACK_ERASURE_V1.md`;
- `OPEN_TRACK_ROOT_STRIP_ENDPOINT_SCOPE_CORRECTION_V1.md` together with the retained local theorem in `PETERSEN_OPEN_TRACK_ROOT_STRIP_REPLACEMENT_V1.md`;
- `PERIODIC_OUTER_ENDPOINT_ROOT_SEAM_DISCHARGE_V1.md` v1.1.

**Status:** `COMPLETE AUTHORIAL R2.7 CANDIDATE / PDL RECONSTRUCTION AND INDEPENDENT ASSURANCE REQUIRED`.

Every original inverse step is crossed once. A forward equal-face cancellation is not used as a recursive lower-order exit: its smaller graph is only a common contraction witness. Under the returned flow, the inverse step is immediately normalized at the predecessor order to the original root insertion, a root-valued alternative insertion, or one missing-index co-root discrepancy state. At fixed original-prefix level, all persistent singularity is one nonbranching co-root track. Internal closed tracks erase; open tracks with normalized endpoints erase; an unresolved outer endpoint either exits or launches another finite episode; and a repeated complete endpoint state is discharged by the marked close--reduce--cut--strip theorem. The finite normalized endpoint graph therefore has no nonexit sink strongly connected component. Contextual transfer is well founded on the finite original-history prefix, without graph-order induction and without arbitrary-flow inverse weld.

This file is not PDL acceptance, independent audit, curation, Lean verification, manuscript integration, release, arXiv, DOI, peer review, publication, or a declaration that the universal five-CDC theorem is established.

---

## 1. Input history and complete contextual data

Let

\[
\mathcal H:
C_0\longrightarrow C_1\longrightarrow\cdots\longrightarrow C_m
\]

be one finite source history. Every forward step is either:

1. a root-valued `2--2` Pachner NNI; or
2. an equal-face `2--0` cancellation.

Fix a cap-compatible root state on `C_m`.

A complete contextual state records:

- the ordered cubic source topology and every exterior incidence;
- every root label and, transiently, one normalized co-root atom;
- both crossed resolutions of that atom;
- support transport, emitted side roots and rooted attachments;
- the cap matching, distinguished cap block and physical route;
- the original target topology and original-prefix position;
- bounded/category flags required by the local exit theorems.

No quotient by coefficient state, collapsed pivot skeleton or support permutation is used.

---

## 2. Original-prefix coordinate

For

\[
0\le \ell\le m,
\]

say that the original suffix

\[
C_m\to\cdots\to C_\ell
\]

has been consumed and that the next required original topology is `C_(ell-1)` when `ell>0`.

The current normalized source topology may differ from `C_ell` by a same-order root/Ptolemy discrepancy, but the discrepancy is resolved before another original step is consumed.

### Rule 2.1 — cross the original step topologically first

Attempt the inverse of

\[
C_{\ell-1}\to C_\ell.
\]

Restore the predecessor local incidence pattern before testing the forced central value. Therefore the original history step has been crossed whether the returned coefficient is root, zero or co-root, and the original-prefix coordinate becomes

\[
\boxed{\ell-1.}
\]

The remaining task is same-order normalization relative to the target topology `C_(ell-1)`.

---

## 3. Order-restoring local inverse table

### 3.1 Inverse `2--2`

For the forced old diagonal:

\[
\begin{array}{c|c}
\text{value}&\text{same-order disposition}\\
\hline
\text{root}&\text{retain the restored root topology}\\
0&\text{use the other crossed root NNI}\\
\text{co-root}&\text{retain one oriented crossed resolution and one discrepancy atom}.
\end{array}
\]

The local first-failure theorem gives only one zero/co-root edge; normalized critical overlaps never create more than one persistent atom.

### 3.2 Inverse equal-face cancellation

Let the two reconnecting roots in the returned smaller state be `a,b`.

\[
\begin{array}{c|c}
\text{relation of }a,b&\text{order-restoring disposition}\\
\hline
\text{distinct intersecting}&\text{original root-valued inverse insertion}\\
a=b&\text{direct root-valued alternative insertion}\\
a\perp b,\ \text{good borrowing}&\text{direct root-valued alternative insertion}\\
a\perp b,\ \text{missing-index borrowing}&\text{one normalized }(Q_i,Q_j,ij)\text{ transport state}.
\end{array}
\]

Loop, parallel-edge, insufficient-borrow and separator identifications are accepted bounded/category exits.

### Lemma 3.1 — the smaller graph is not a recursive state

In every nonexit row, the output again has the vertex order of `C_(ell-1)`.

### Proof

- The root-success row inserts the original equal-face pair.
- In the equality and good-disjoint rows, `ROOT_VALUED_ALTERNATIVE_INVERSE_CANCELLATION_INSERTION_V1.md` inserts a neighbouring equal-face pair into the current smaller graph. Its cancellation is exactly that smaller graph. The output therefore restores two vertices and has predecessor order.
- In the missing-index row, the attempted inverse insertion plus one borrowed adjacent root vertex is represented by a same-order five-leaf discrepancy whose normalized residual is `(Q_i,Q_j,ij)`. No lower-order graph remains as the current state.

Thus the smaller graph is only the common contraction witness which proves that the original and alternative insertions are inverse `2--0` expansions of the same source neighbourhood. ∎

### Corollary 3.2 — fixed-order macro normalization

Every original cancellation step is replaced, before global scheduling, by one predecessor-order macro consisting of:

- a root insertion; or
- a root-valued alternative insertion; or
- a finite same-order co-root discrepancy episode; or
- an accepted exit.

No normalized transfer state has smaller graph order merely because the original step was a cancellation.

---

## 4. Fixed-prefix normalized macro-state graph

Fix one prefix level `ell`, target topology `C_ell` and target vertex order `N`.

Let

\[
\mathcal S_{N,\ell}
\]

be the set of complete normalized macro states after applying Corollary 3.2. A state may be:

1. fully root-valued; or
2. an unresolved outer endpoint carrying exactly one normalized co-root atom.

Transient two-co-root critical-overlap trees occur only inside one local normalization macro and are not vertices of `S_(N,ell)`.

### Lemma 4.1 — finite normalized state set

\[
\boxed{|\mathcal S_{N,\ell}|<\infty.}
\]

### Proof

At fixed finite order there are finitely many labelled cubic multigraph topologies and finite incidence identifications. Every edge value belongs to the ten-element root set, except for the one atom which belongs to the five co-roots and has finitely many positions and two resolutions. Support transports, side-root words, cap blocks, route orientations and bounded flags all range over finite labelled sets.

A Ptolemy or continuation history word is not a state coordinate. It is a finite witness for an edge or path in the macro-state graph. Two occurrences with the same complete current data are the same normalized state even if reached by different histories. ∎

Allowed macro edges are:

- root-preserving relative NNIs and their inverses;
- involution, disjoint-square and five-leaf pentagon comparisons;
- local first-failure normalization;
- constant-pivot root sections and normalized backtrack deletion;
- accepted route/profile, bounded or separator exits;
- finite full-channel continuation episodes at one unresolved outer endpoint.

All original `2--0` steps have already been absorbed into the order-restoring macros of Section 3. Hence every nonexit cycle in `S_(N,ell)` is a fixed-order full-state history cylinder.

---

## 5. Singular-locus classification at fixed order

Lift one finite macro comparison to its full-labelled Ptolemy/history diagram. After immediate defect-tree normalization, the singular locus is nonbranching.

Every connected singular component is one of:

1. an internal closed track;
2. an open track with both endpoints root-normalized or accepted;
3. an open track with at least one endpoint at the unresolved original cap/full-channel boundary.

There is no persistent zero component:

- inverse-flip zero uses the other crossed root NNI;
- inverse-cancellation equality uses a direct alternative insertion;
- good doubled-disjoint uses a direct alternative insertion.

Thus every unbounded component is co-root/DDD.

---

## 6. Internal and normalized-endpoint disposition

### Theorem 6.1 — internal closed-track erasure

Every internal closed co-root component is impossible or removable while fixing the complete labelled outer boundary.

The exact alternatives are:

- no pivot change: unique side-preserving root section;
- normalized immediate backtracks: source-faithful deletion;
- reduced `C5/C9`: forbidden by the oriented cap character;
- reduced `C6/C8`: root-annulus replacement.

This is imported from `PTOLEMY_CLOSED_DEFECT_TRACK_ERASURE_V1.md` with its full source-incidence hypotheses.

### Theorem 6.2 — normalized-endpoint open-strip erasure

If both short endpoint sides of an open co-root track are root-normalized or accepted boundary cells, the track has a singularity-free root-valued strip replacement preserving all four labelled sides.

This is the retained theorem of `PETERSEN_OPEN_TRACK_ROOT_STRIP_REPLACEMENT_V1.md`, read through `OPEN_TRACK_ROOT_STRIP_ENDPOINT_SCOPE_CORRECTION_V1.md`.

Neither theorem uses equal-face cancellation as a progress edge.

---

## 7. The unresolved outer endpoint graph

Let

\[
\mathcal E_{N,\ell}\subseteq\mathcal S_{N,\ell}
\]

be the finite set of normalized states whose sole singular track reaches the unresolved original cap/full-channel boundary.

From one state `E` exactly one of the following finite alternatives is available:

1. a horizontal support-pair separation gives cap-compatible rootification;
2. the physical route or boundary profile changes and gives escape;
3. a bounded theta/direct or separator/category configuration is exposed;
4. a finite equality/DDD current-flow episode returns to another state of `E_(N,ell)`.

The first three are exits. Only the fourth can remain in the endpoint graph.

### Important fixed-order condition

The raw forward episode may contain equal-face cancellations. Before it defines an endpoint edge, every inverse cancellation in its return is normalized by Section 3. Thus the endpoint edge is represented by a predecessor-order full-state macro history, not by a nested lower-order state. This condition is required before any periodic cylinder is formed.

---

## 8. Periodic endpoint discharge

Suppose one complete endpoint state

\[
E\in\mathcal E_{N,\ell}
\]

returns to itself through a nonexit finite episode.

By `PERIODIC_OUTER_ENDPOINT_ROOT_SEAM_DISCHARGE_V1.md` v1.1:

1. identify the equal complete endpoint collars and form a fixed-order history cylinder;
2. retain the return seam as a marked transverse position;
3. reduce closed singular cores disjoint from the mark, strictly lowering closed-track complexity;
4. when the marked position is met, obtain an explicit root seam from a constant-pivot root section, source-faithful backtrack normalization or `C6/C8` canonicalisation movie;
5. cut the cylinder at that root seam;
6. the residual singular component is now an open track with root-normalized endpoint sides;
7. erase it by Theorem 6.2.

The resulting rectangle has the same long labelled histories and complete exterior context, but replaces the two unresolved occurrences of `E` by root-valued short sides.

### Theorem 8.1 — no neutral endpoint cycle

A boundary-minimal normalized continuation diagram contains no repeated unresolved endpoint state.

### Proof

Let `U(D)` be the number of unresolved outer endpoint occurrences. The marked close--reduce--cut--strip replacement changes no global input or accepted output and introduces no new unresolved endpoint. It removes two occurrences, so

\[
U(D')\le U(D)-2.
\]

This contradicts minimality. ∎

---

## 9. No nonexit sink component

Consider the finite directed graph on `E_(N,ell)` whose edges are nonexit continuation episodes.

### Theorem 9.1 — endpoint discharge

Every reachable endpoint state has a finite path to rootification, route/profile escape, or a bounded/separator/category exit.

### Proof

Assume a reachable sink strongly connected component contains no exit. Being finite, it contains a directed cycle. Concatenating the cycle gives a repeated complete endpoint episode at fixed order, contradicting Theorem 8.1. ∎

This is an existence-of-exit theorem. It does not claim that every arbitrary nondeterministic scheduling choice terminates.

---

## 10. Fixed-prefix contextual normalization

### Theorem 10.1 — fixed-prefix discrepancy discharge

At fixed `N,ell`, every complete normalized macro state reaches after finitely many source-faithful moves one of:

1. a root state on the target original topology `C_ell`;
2. a cap-compatible strict-prefix terminal;
3. a route/profile escape;
4. a bounded direct/theta terminal;
5. a separator/category exit.

### Proof

Take a finite sink strongly connected component of the complete macro-state graph.

- An internal closed singular cycle is erased by Theorem 6.1.
- A cycle built from open tracks with normalized endpoints is erased by Theorem 6.2.
- A cycle meeting an unresolved outer endpoint is forbidden by Theorem 9.1.
- A root state with no discrepancy is the target or a declared terminal.

Thus no nonterminal sink component exists. Every finite directed graph path reaches a terminal sink, proving the result. ∎

---

## 11. Contextual inverse transfer

Order the original obligations by the prefix coordinate

\[
\ell=m,m-1,\ldots,0.
\]

At `ell>0`:

1. cross the next original inverse step, lowering `ell` to `ell-1`;
2. apply the order-restoring table of Section 3;
3. discharge the resulting fixed-prefix discrepancy by Theorem 10.1;
4. continue with the next original step or leave through an accepted exit.

### Theorem 11.1 — root-normalized contextual transfer v5

Every cap-compatible terminal root state on `C_m` transfers through the finite mixed Pachner/cancellation history to a cap-compatible root state on `C_0`, or leaves through an already accepted route/profile, bounded direct/theta, or separator/category exit.

### Proof

Induct on the finite original-prefix coordinate `ell`.

- At `ell=0`, Theorem 10.1 reaches the original target context or an accepted exit.
- For `ell>0`, Rule 2.1 crosses one original step, so the prefix coordinate strictly decreases. Section 3 returns immediately to predecessor order. Theorem 10.1 eliminates every same-prefix discrepancy before the next original step is consumed.

No branch restores a larger original-prefix coordinate, and no graph-order recursive obligation occurs. ∎

---

## 12. Exact resolution of the cancellation re-entry gap

The invalid macro was:

\[
\text{cancel}
\to
N-2
\to
\text{choose arbitrary lower-order flow}
\to
\text{attempt inverse weld}
\to
N\text{ token re-entry}.
\]

The v5 proof never performs it.

For the actual returned flow, every inverse cancellation is immediately converted into:

\[
\begin{array}{c|c}
\text{returned relation}&\text{current normalized state}\\
\hline
B\text{ (intersecting)}&\text{original predecessor root insertion}\\
A\text{ (equal)}&\text{alternative predecessor-order root insertion}\\
C\text{ (disjoint), good}&\text{alternative predecessor-order root insertion}\\
C\text{ (disjoint), missing index}&\text{one predecessor-order co-root discrepancy track}.
\end{array}
\]

The sole unbounded row is consumed by the closed/open/periodic track theorems at the same original-prefix level.

Hence cancellation does not create a recursive lower-order state and cannot reset the transfer induction.

---

## 13. R2.7 classification and downstream boundary

### Closed at Research Lead authorial level

- complete inverse-cancellation source table;
- elimination of every persistent zero row;
- isolation of one missing-index co-root track;
- order-restoring normalization of every original cancellation;
- finite complete fixed-order macro-state semantics;
- internal closed-track erasure;
- normalized-endpoint open-strip erasure;
- marked periodic endpoint root-seam discharge;
- exclusion of every nonexit fixed-prefix sink component;
- contextual transfer without graph-order recursion.

### Required before assurance promotion

PDL must reconstruct independently:

1. full-labelled forced-backbone exhaustiveness;
2. distinguished-cap-block transport and odd pivot-closed exclusion;
3. source-faithful immediate-backtrack normalization;
4. `C6/C8` root-annulus and open-strip canonicalisations;
5. the marked-seam periodic discharge;
6. the finite normalized endpoint graph without history words as hidden state;
7. the complete branch table and fixed-order normalization condition in Sections 3 and 7.

An independent auditor must then verify the assembled dependency graph and every imported source theorem.

### Not established by this file

- PDL completion or independent audit;
- one-cross cap restoration beyond the conditional R2 consumer;
- global simple-edge extension or universal five-CDC acceptance;
- Lean verification;
- manuscript integration;
- curation, release, arXiv, DOI, peer review or publication.
