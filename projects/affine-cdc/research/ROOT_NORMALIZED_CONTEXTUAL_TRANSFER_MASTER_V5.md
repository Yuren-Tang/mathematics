# Root-normalized contextual transfer with periodic endpoint discharge

## Research Lead master theorem v5.2 — repaired R2.7 assembly

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`

**Supersedes for controlling Research Lead authorial use:**

- `ROOT_NORMALIZED_CONTEXTUAL_TRANSFER_MASTER_V4.md`;
- `CONTEXTUAL_TRANSFER_REPAIR_FRONTIER_V2.md` as an open-frontier description;
- v5.0--v5.1 of this file;
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
- `PERIODIC_OUTER_ENDPOINT_ROOT_SEAM_DISCHARGE_V1.md` v1.2;
- `TARGET_TOPOLOGY_ARBORESCENCE_FIXED_ORDER_V1.md`.

**Status:** `COMPLETE AUTHORIAL R2.7 CANDIDATE / PDL RECONSTRUCTION AND INDEPENDENT ASSURANCE REQUIRED`.

Every original inverse step is crossed once. A forward equal-face cancellation is not used as a recursive lower-order exit: its smaller graph is only a common contraction witness. Under the returned flow, the inverse step is immediately normalized at predecessor order to the original root insertion, a root-valued alternative insertion, or one missing-index co-root discrepancy state.

At fixed original-prefix level, choose a finite ordinary topology arborescence rooted at the required original topology. A fully root-valued state attempts only its unique parent flip. Root success strictly lowers topology-tree distance; failure produces the sole persistent singular type, one nonbranching co-root track. Internal closed tracks erase, normalized-endpoint open tracks erase, and a repeated unresolved outer endpoint closes to a root-valued history cylinder whose legal `1`-skeleton contains a root crosscut. Cutting there replaces the periodic episode by a fully root-valued rectangle. Hence the finite canonical macro-state graph has no nonterminal sink strongly connected component. Contextual transfer is well founded on the finite original-history prefix, without graph-order induction and without arbitrary-flow inverse weld.

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

## 4. Target topology arborescence

Fix one prefix level `ell`, target topology `C_ell` and target order `N`.

By `TARGET_TOPOLOGY_ARBORESCENCE_FIXED_ORDER_V1.md`, every nonexit order-restoring output lies in the same finite ordinary labelled `2--2` topology component as `C_ell`.

Choose a spanning tree of that component rooted at `C_ell`. For every non-target topology `T`, let `p(T)` be its parent and let

\[
d_{\rm top}(T)
\]

be its tree distance to `C_ell`.

### Target-directed rule

If the current state is fully root-valued and its topology is not `C_ell`, attempt only

\[
T\longrightarrow p(T).
\]

- Root success performs the parent move and lowers `d_top` by one.
- Zero uses the local alternative root normalization.
- Co-root enters the one-track grammar.
- Category or route failure exits.

The arborescence is ordinary and uncoloured. It does not assert that every parent edge is root-admissible. A non-root parent edge is exactly the event which creates the singular locus.

Consequently a directed scheduling cycle cannot consist solely of successful root-valued moves.

---

## 5. Finite canonical macro-state graph

Let

\[
\mathcal S_{N,\ell}
\]

be the complete normalized states at fixed `N,ell`, with transitions generated only by:

1. the target-directed parent rule;
2. one local first-failure normalization macro;
3. full-labelled co-root transport and constant-pivot/backtrack normalization;
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

All raw `2--0` excursions have already been absorbed into predecessor-order macros. Hence every directed nonexit cycle:

- cannot consist only of root successes, by strict decrease of `d_top`;
- contains at least one normalized co-root singular component;
- is represented by a fixed-order full-state history cylinder.

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

By `PERIODIC_OUTER_ENDPOINT_ROOT_SEAM_DISCHARGE_V1.md` v1.2:

1. identify the equal endpoint collars and form a fixed-order history cylinder;
2. the outer-reaching co-root arc closes to one internal full-state singular component;
3. erase that complete component by the closed-track theorem, obtaining a finite connected root-valued history cylinder with the same two boundary histories;
4. the cylinder's legal root-history `1`-skeleton is connected;
5. choose a shortest `1`-skeleton path between the boundary vertex sets; it is a genuine root-valued crosscut;
6. cut the root cylinder along that crosscut.

The result is a fully root-valued rectangle with the same long histories and complete exterior context, but with root-valued short sides instead of the two unresolved copies of `E`.

### Theorem 8.1 — no neutral endpoint cycle

A boundary-minimal normalized continuation diagram contains no repeated unresolved endpoint state.

### Proof

Let `U(D)` count unresolved endpoint occurrences. The root-cylinder cut replacement preserves global input and accepted output, introduces no unresolved endpoint and removes two occurrences. Hence

\[
U(D')\le U(D)-2,
\]

contradicting minimality. ∎

### Theorem 8.2 — endpoint discharge

Every reachable endpoint state has a finite path to cap rootification, route/profile escape, or a bounded/separator/category exit.

### Proof

If a reachable sink strongly connected component of the finite endpoint graph had no exit, it would contain a directed cycle. Concatenating the cycle gives a repeated complete endpoint episode, contradicting Theorem 8.1. ∎

This proves existence of an exit path, not termination of every arbitrary nondeterministic choice.

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

- A cycle consisting only of successful target-directed root moves is impossible because `d_top` strictly decreases.
- Otherwise a cycle in `K` contains a co-root singular component.
- An internal closed component is erased by Theorem 6.1.
- An open component with normalized endpoints is erased by Theorem 6.2.
- A component meeting an unresolved endpoint is discharged by Theorem 8.2.

Each case contradicts a nonterminal sink SCC. Hence every reachable sink is terminal, proving the existence of a finite path to the displayed outcomes. ∎

---

## 10. Contextual inverse transfer

At `ell>0`:

1. cross the next original inverse step, lowering `ell` to `ell-1`;
2. apply the order-restoring table of Section 3;
3. discharge the fixed-prefix discrepancy by Theorem 9.1;
4. continue with the next original step or leave through an accepted exit.

### Theorem 10.1 — root-normalized contextual transfer v5.2

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

The v5.2 proof never performs it. Under the actual returned flow:

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
- periodic root-cylinder crosscut discharge;
- exclusion of every nonterminal fixed-prefix sink SCC;
- contextual transfer without graph-order recursion.

### Required before assurance promotion

PDL must reconstruct independently:

1. full-labelled forced-backbone exhaustiveness;
2. distinguished-cap-block transport and odd pivot-closed exclusion;
3. source-faithful immediate-backtrack normalization as used by closed-track erasure;
4. `C6/C8` root-annulus and open-strip canonicalisations;
5. fixed-order closure of periodic endpoint episodes;
6. the root-cylinder `1`-skeleton crosscut lemma;
7. finite normalized state semantics and the topology arborescence;
8. the branch table and fixed-order endpoint condition.

An independent auditor must then verify the assembled dependency graph and every imported source theorem.

### Not established by this file

- PDL completion or independent audit;
- one-cross cap restoration beyond the conditional R2 consumer;
- global simple-edge extension or universal five-CDC acceptance;
- Lean verification;
- manuscript integration;
- curation, release, arXiv, DOI, peer review or publication.
