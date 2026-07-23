# Root-normalized contextual transfer with periodic endpoint discharge

## Research Lead master theorem v5.1 — repaired R2.7 assembly

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`

**Supersedes for controlling Research Lead authorial use:**

- `ROOT_NORMALIZED_CONTEXTUAL_TRANSFER_MASTER_V4.md`;
- `CONTEXTUAL_TRANSFER_REPAIR_FRONTIER_V2.md` as an open-frontier description;
- v5.0 of this file;
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

Every original inverse step is crossed once. A forward equal-face cancellation is not used as a recursive lower-order exit: its smaller graph is only a common contraction witness. Under the returned flow, the inverse step is immediately normalized at predecessor order to the original root insertion, a root-valued alternative insertion, or one missing-index co-root discrepancy state.

At fixed original-prefix level, choose once and for all a finite ordinary topology arborescence rooted at the required original topology. A fully root-valued state attempts only its unique parent flip. Root success strictly lowers topology-tree distance; failure produces the sole persistent singular type, one nonbranching co-root track. Internal closed tracks erase, normalized-endpoint open tracks erase, and repeated unresolved outer endpoints discharge by the marked root-seam theorem. Hence the finite canonical macro-state graph has no nonterminal sink strongly connected component. Contextual transfer is well founded on the finite original-history prefix, without graph-order induction and without arbitrary-flow inverse weld.

This file is not PDL acceptance, independent audit, curation, Lean verification, manuscript integration, release, arXiv, DOI, peer review, publication, or a declaration that the universal five-CDC theorem is established.

---

## 1. Input history and complete contextual states

Let

\[
\mathcal H:C_0\longrightarrow C_1\longrightarrow\cdots\longrightarrow C_m
\]

be one finite source history. Every forward step is either:

1. a root-valued `2--2` Pachner NNI; or
2. an equal-face `2--0` cancellation.

Fix a cap-compatible root state on `C_m`.

A complete contextual state records:

- the ordered cubic source topology and every exterior incidence;
- every root label and, when unresolved, one normalized co-root atom;
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

has been consumed. When `ell>0`, the next required original topology is `C_(ell-1)`.

The current normalized source topology may differ from `C_ell` by a same-order discrepancy, but that discrepancy is discharged before another original step is consumed.

### Rule 2.1 — cross the original step first

Attempt the inverse of

\[
C_{\ell-1}\to C_\ell.
\]

Restore the predecessor local incidence pattern before testing the forced central value. Therefore the original step has been crossed whether the returned coefficient is root, zero or co-root, and the original-prefix coordinate becomes

\[
\boxed{\ell-1.}
\]

The remaining task is same-order normalization relative to `C_(ell-1)`.

---

## 3. Order-restoring inverse table

### 3.1 Inverse `2--2`

For the forced old diagonal:

\[
\begin{array}{c|c}
\text{value}&\text{same-order disposition}\\
\hline
\text{root}&\text{retain the restored root topology}\\
0&\text{use the other crossed root NNI}\\
\text{co-root}&\text{retain the oriented discrepancy atom and its two root resolutions}.
\end{array}
\]

The first-failure theorem gives only one non-root edge. Normalized critical overlaps never create more than one persistent atom.

### 3.2 Inverse equal-face cancellation

Let the two reconnecting roots in the returned smaller state be `a,b`.

\[
\begin{array}{c|c}
\text{relation of }a,b&\text{order-restoring disposition}\\
\hline
\text{distinct intersecting}&\text{original root-valued insertion}\\
a=b&\text{direct root-valued alternative insertion}\\
a\perp b,\ \text{good borrowing}&\text{direct root-valued alternative insertion}\\
a\perp b,\ \text{missing-index borrowing}&\text{one normalized }(Q_i,Q_j,ij)\text{ transport state}.
\end{array}
\]

Loop, parallel-edge, insufficient-borrow and separator identifications are accepted bounded/category exits.

### Lemma 3.1 — the smaller graph is not a recursive state

In every nonexit row, the output again has the vertex order of `C_(ell-1)`.

### Proof

- Root success inserts the original equal-face pair.
- Equality and good-disjoint insert a neighbouring root-valued equal-face pair. Its cancellation is exactly the current smaller graph, so two vertices are restored.
- Missing-index borrowing is a same-order five-leaf discrepancy. Full-defect-tree normalization leaves one co-root transport atom but does not leave the smaller graph as the current state.

Thus the smaller graph is only a common contraction witness for two predecessor-order insertions. ∎

### Corollary 3.2 — fixed-order macro normalization

Before global scheduling, every original cancellation step is replaced by one predecessor-order macro:

- original root insertion;
- alternative root insertion;
- finite same-order co-root discrepancy;
- or accepted exit.

No normalized transfer state is lower-order merely because the original step was a cancellation.

---

## 4. Finite topology universe and target arborescence

Fix one prefix level `ell`, target topology `C_ell` and target order `N`.

Let `T_(N,ell)` be the finite set of labelled predecessor-order source topologies which can occur after the local macros of Section 3 and the established relative `2--2` comparisons, with the fixed exterior incidence universe retained.

Every alternative insertion lies in the same ordinary `2--2` topology component as the required original insertion: on the borrowed five-leaf region the two three-vertex trees are joined by the displayed pentagon path. Likewise every normalized critical-overlap topology is joined to its target by its finite local Ptolemy comparison.

Choose a spanning tree of each relevant ordinary topology component and orient it toward the required target `C_ell`. Write

\[
p(T)
\]

for the unique parent of a non-target topology `T`, and

\[
d_{\rm top}(T)
\]

for its tree distance to `C_ell`.

### Target-directed rule

If the current state is fully root-valued and its topology is not `C_ell`, attempt only the single `2--2` comparison

\[
T\longrightarrow p(T).
\]

- If the forced new central value is a root, perform the move and strictly lower `d_top`.
- If it is zero, use the local alternative root NNI and record the resulting same-order discrepancy.
- If it is a co-root, enter the normalized one-track grammar.
- If category or route data exits, leave immediately.

This removes arbitrary root-flip wandering from the global scheduler. A cycle consisting only of successful root moves is impossible because `d_top` strictly decreases.

---

## 5. Finite canonical macro-state graph

Let

\[
\mathcal S_{N,\ell}
\]

be the complete normalized states at fixed `N,ell`, with transitions generated only by:

1. the target-directed rule of Section 4;
2. one local first-failure normalization macro;
3. full-labelled co-root track transport and its constant-pivot/backtrack normalization;
4. accepted route/profile, bounded or separator exits;
5. one finite continuation episode at an unresolved outer endpoint.

Transient two-co-root three-vertex trees occur only inside one local macro and are not vertices of `S_(N,ell)`.

### Lemma 5.1 — finiteness

\[
\boxed{|\mathcal S_{N,\ell}|<\infty.}
\]

### Proof

At fixed finite order there are finitely many labelled cubic multigraph topologies and incidence identifications. Edge roots range over ten values; the one atom ranges over five co-roots, finitely many positions and two resolutions. Support transports, side-root data, cap blocks, route orientations and bounded flags all range over finite labelled sets.

History words are transition witnesses, not state coordinates. Two occurrences with the same complete current data are the same normalized state even if reached by different histories. ∎

All raw `2--0` excursions have already been absorbed into predecessor-order macros. Hence every directed cycle in the nonexit part of `S_(N,ell)`:

- cannot consist only of successful root moves, by strict decrease of `d_top`;
- therefore contains at least one normalized co-root singular track;
- and is represented by a fixed-order full-state history cylinder.

---

## 6. Singular-locus classification

After immediate defect-tree normalization, the singular locus is nonbranching. Every component is one of:

1. an internal closed co-root track;
2. an open co-root track with both endpoints root-normalized or accepted;
3. an open co-root track meeting the unresolved original cap/full-channel boundary.

There is no persistent zero component:

- inverse-flip zero uses the other crossed root NNI;
- inverse-cancellation equality uses a direct alternative insertion;
- good doubled-disjoint uses a direct alternative insertion.

### Theorem 6.1 — internal closed-track erasure

Every internal closed track is impossible or removable while fixing the complete labelled outer boundary:

- no pivot change: unique side-preserving root section;
- normalized immediate backtrack: source-faithful deletion;
- reduced `C5/C9`: forbidden by the oriented cap character;
- reduced `C6/C8`: root-annulus replacement.

### Theorem 6.2 — normalized-endpoint open-strip erasure

If both short endpoint sides are root-normalized or accepted boundary cells, the open track has a singularity-free root strip preserving all four labelled sides.

Neither theorem uses equal-face cancellation as a progress edge.

---

## 7. Unresolved outer endpoints

Let

\[
\mathcal E_{N,\ell}\subseteq\mathcal S_{N,\ell}
\]

be the finite states whose sole track reaches the unresolved original cap/full-channel boundary.

From one `E` a finite continuation gives exactly one of:

1. horizontal support-pair separation and cap rootification;
2. route/profile escape;
3. bounded theta/direct or separator/category exit;
4. another state of `E_(N,ell)`.

The first three are exits.

### Fixed-order condition

A raw forward episode may contain equal-face cancellations. It defines an endpoint edge only after every inverse cancellation in its return has been normalized by Section 3. Thus every endpoint edge is a predecessor-order full-state macro history, not a nested lower-order state. Only such normalized episodes may be closed into periodic cylinders.

---

## 8. Periodic endpoint discharge

Suppose a complete endpoint state

\[
E\in\mathcal E_{N,\ell}
\]

returns to itself through a nonexit episode.

By `PERIODIC_OUTER_ENDPOINT_ROOT_SEAM_DISCHARGE_V1.md` v1.1:

1. identify the equal endpoint collars and form a fixed-order history cylinder;
2. retain the return seam as a marked transverse position;
3. reduce closed singular cores disjoint from the mark, strictly lowering closed-track complexity;
4. when the marked position is met, obtain an explicit root seam from a constant-pivot root section, source-faithful backtrack normalization or `C6/C8` canonicalisation movie;
5. cut at the root seam;
6. the residual track now has root-normalized endpoint sides;
7. erase it by Theorem 6.2.

The resulting rectangle preserves the long histories and complete exterior context, but replaces two unresolved occurrences of `E` by root-valued short sides.

### Theorem 8.1 — no neutral endpoint cycle

A boundary-minimal normalized continuation diagram contains no repeated unresolved endpoint state.

### Proof

Let `U(D)` count unresolved outer endpoint occurrences. The marked close--reduce--cut--strip replacement preserves global input and accepted output, introduces no unresolved endpoint and removes two occurrences. Hence

\[
U(D')\le U(D)-2,
\]

contradicting minimality. ∎

### Theorem 8.2 — endpoint discharge

Every reachable endpoint state has a finite path to cap rootification, route/profile escape, or a bounded/separator/category exit.

### Proof

If a reachable sink strongly connected component of the finite endpoint graph had no exit, it would contain a directed cycle. Concatenating the cycle gives a repeated complete endpoint episode, contradicting Theorem 8.1. ∎

This is an existence-of-exit theorem, not a claim that every arbitrary nondeterministic choice terminates.

---

## 9. Fixed-prefix discrepancy discharge

### Theorem 9.1

At fixed `N,ell`, every complete normalized macro state has a finite source-faithful path to one of:

1. a root state on `C_ell`;
2. a cap-compatible strict-prefix terminal;
3. route/profile escape;
4. bounded direct/theta terminal;
5. separator/category exit.

### Proof

Every vertex of a finite directed graph reaches some sink strongly connected component. Let `K` be a reachable sink SCC of the canonical macro graph.

- If every transition in `K` is a successful target-directed root move, `d_top` strictly decreases around a directed cycle, impossible.
- Otherwise a cycle in `K` contains a co-root singular component.
- An internal closed component is erased by Theorem 6.1.
- An open component with normalized endpoints is erased by Theorem 6.2.
- A component meeting an unresolved outer endpoint is discharged by Theorem 8.2.

Each case contradicts a nonterminal sink SCC. Hence every reachable sink is terminal, proving the existence of a finite path to the displayed outcomes. ∎

---

## 10. Contextual inverse transfer

At `ell>0`:

1. cross the next original inverse step, lowering `ell` to `ell-1`;
2. apply the order-restoring table of Section 3;
3. discharge the fixed-prefix discrepancy by Theorem 9.1;
4. continue with the next original step or leave through an accepted exit.

### Theorem 10.1 — root-normalized contextual transfer v5.1

Every cap-compatible terminal root state on `C_m` transfers through the finite mixed Pachner/cancellation history to a cap-compatible root state on `C_0`, or leaves through an accepted route/profile, bounded direct/theta, or separator/category exit.

### Proof

Induct on the finite original-prefix coordinate `ell`.

- At `ell=0`, Theorem 9.1 reaches `C_0` or an accepted exit.
- For `ell>0`, Rule 2.1 crosses one original step, so `ell` strictly decreases. Section 3 returns immediately to predecessor order, and Theorem 9.1 removes every same-prefix discrepancy before the next original step.

No branch restores a larger original-prefix coordinate, and no graph-order recursive obligation occurs. ∎

---

## 11. Resolution of cancellation re-entry

The invalid macro was

\[
\text{cancel}\to N-2\to\text{arbitrary lower-order flow}\to\text{inverse weld}\to N\text{ token}.
\]

The v5.1 proof never performs it. Under the actual returned flow:

\[
\begin{array}{c|c}
\text{returned relation}&\text{normalized predecessor-order state}\\
\hline
B\text{ (intersecting)}&\text{original root insertion}\\
A\text{ (equal)}&\text{alternative root insertion}\\
C\text{ (disjoint), good}&\text{alternative root insertion}\\
C\text{ (disjoint), missing index}&\text{one co-root discrepancy track}.
\end{array}
\]

The sole unbounded row is consumed at the same prefix level by the closed/open/periodic track theorems. Cancellation cannot reset the transfer induction.

---

## 12. R2.7 classification and downstream boundary

### Closed at Research Lead authorial level

- complete inverse-cancellation source table;
- elimination of persistent zero rows;
- isolation of one missing-index co-root track;
- predecessor-order normalization of every original cancellation;
- finite complete macro-state semantics with history words excluded from state;
- target-topology arborescence excluding pure-root scheduling loops;
- internal closed-track erasure;
- normalized-endpoint open-strip erasure;
- marked periodic endpoint root-seam discharge;
- exclusion of every nonterminal fixed-prefix sink SCC;
- contextual transfer without graph-order recursion.

### Required before assurance promotion

PDL must reconstruct independently:

1. full-labelled forced-backbone exhaustiveness;
2. distinguished-cap-block transport and odd pivot-closed exclusion;
3. source-faithful immediate-backtrack normalization;
4. `C6/C8` root-annulus and open-strip canonicalisations;
5. the marked-seam periodic discharge;
6. finite normalized state semantics and the topology arborescence;
7. the branch table and fixed-order endpoint condition.

An independent auditor must then verify the assembled dependency graph and every imported source theorem.

### Not established by this file

- PDL completion or independent audit;
- one-cross cap restoration beyond the conditional R2 consumer;
- global simple-edge extension or universal five-CDC acceptance;
- Lean verification;
- manuscript integration;
- curation, release, arXiv, DOI, peer review or publication.
