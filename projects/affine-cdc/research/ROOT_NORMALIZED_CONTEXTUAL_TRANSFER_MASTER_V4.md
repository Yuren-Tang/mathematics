# Root-normalized contextual transfer at fixed order

## Research Lead master theorem v4 — post-cancellation repair

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Supersedes for controlling authorial use:**

- `SINGULAR_ROOT_TRIALITY_CONFLUENCE_MASTER_THEOREM_V2.md`;
- `SINGULAR_ROOT_TRIALITY_CONFLUENCE_MASTER_THEOREM_V3.md`;
- the cancellation-exit portions of `CONTEXTUAL_TRANSFER_REPAIRED_AUTHORITY_V2.md`;
- Sections 8--10 of `ROOT_FLOW_PTOLEMY_CONTEXTUAL_COHERENCE_V1.md`, only insofar as they used local five-leaf circuits or target-order descent without the later corrections.

**New repair inputs:**

- `PTOLEMY_CONTEXTUAL_COHERENCE_SCOPE_CORRECTION_V1.md`;
- `PETERSEN_EVEN_TRACK_ROOT_ANNULUS_REPLACEMENT_V1.md`;
- `PTOLEMY_CLOSED_DEFECT_TRACK_ERASURE_V1.md`;
- `QUADRUPLE_EQUALITY_THREE_VERTEX_BORROWING_ROOTIFICATION_V1.md`;
- the inverse-flip zero and co-root triality theorems;
- full-state constant-pivot, orientation, and forced-backbone theorems.

**Status:** complete repaired authorial master theorem, conditional on the listed concrete source-level inputs. Every failed inverse move is normalized at the same graph order to a fully root-valued alternative topology or an accepted bounded/category exit. In particular, inverse-cancellation quadruple equality is consumed by a two-NNI five-leaf movie and is not recursive. The remaining discrepancy is recorded in the Ptolemy history, where every internal closed defect track is diagrammatically erased: constant-pivot loops rootify, odd Petersen cores are forbidden, and even cores have root-annulus replacements. A finite normalized fixed-order scheduling process therefore has no nonempty repeated state. Contextual transfer is well founded using only the finite remaining original-history prefix and the finite normalized scheduling rank; no target-order cancellation induction is used.

**Assurance boundary:** this is a research-branch theorem, not PDL reconstruction, independent acceptance, curation, Lean verification, manuscript integration, release, or publication.

---

## 1. Finite source history and original-prefix level

Let

\[
\mathcal H:
C_0\longrightarrow C_1\longrightarrow\cdots\longrightarrow C_m
\]

be one finite source-surgery history. Every forward step is:

1. a root-valued `2--2` Pachner NNI; or
2. an equal-face `2--0` cancellation.

Let a cap-compatible root state be given on `C_m`.

A transfer state records an integer

\[
\ell\in\{0,\ldots,m\},
\]

meaning that the original suffix

\[
C_m\to\cdots\to C_\ell
\]

has already been consumed, while the target original prefix is

\[
C_0\to\cdots\to C_\ell.
\]

A state also records:

- the current root-valued source topology, which may differ from `C_ell` by a finite Ptolemy discrepancy word;
- complete edge roots and exterior incidences;
- the cap matching, distinguished cap block, and physical route;
- all support transport and side attachments;
- the target topology `C_ell`.

A **normalized state** is fully root-valued. Zero/co-root edges are allowed only transiently inside one local normalization macro.

---

## 2. Consume one original inverse step

Assume

\[
\ell>0.
\]

Attempt the inverse of

\[
C_{\ell-1}\longrightarrow C_\ell
\]

on the current returned root flow.

Topologically restore the old local source topology first. Thus, whether root admissibility succeeds or fails, the original-history step has been crossed and the new target prefix level is

\[
\boxed{\ell-1.}
\]

The only issue is normalizing the forced old central value.

---

## 3. Complete local inverse table

### 3.1 Root success

If the restored central value is a root, retain the resulting root flow on the restored topology. No discrepancy remains locally.

### 3.2 Inverse `2--2`, zero value

The four exterior roots are

\[
a,a,b,b
\]

with `a,b` distinct intersecting. Either crossed topology has central root

\[
a+b.
\]

Perform the unique root alternative NNI. This is one same-order root normalization.

### 3.3 Inverse `2--0`, equal reconnecting roots

If the two reconnecting edges both have root `a`, the restored pair has one zero edge and local boundary

\[
a,a,a,a.
\]

Apply `QUADRUPLE_EQUALITY_THREE_VERTEX_BORROWING_ROOTIFICATION_V1.md`:

- in the ordinary branch borrow one adjacent root vertex `(a,d,e)`;
- perform the two-NNI five-leaf movie
  \[
  aa\mid a\mid de
  \to
  ae\mid d\mid aa
  \to
  ae\mid a\mid ad;
  \]
- obtain a fully root-valued connected bridgeless topology;
- or solve the bounded two-vertex parallel/theta exception explicitly.

No recursive equality call is made.

### 3.4 Co-root value

If the restored central value is one co-root, the local four-root triality has exactly two crossed root topologies. Choose the resolution prescribed by the oriented cap sheet and retain all side/source data.

The category-safe root NNI theorem gives a connected loopless bridgeless root-valued output, or one accepted separator/bounded degeneration.

### Theorem 3.1 — local root normalization

Every attempted inverse history step has exactly one of:

1. a root-valued restored topology;
2. a root-valued alternative topology after at most two local NNIs;
3. an accepted route, separator, or bounded exit.

There is no persistent zero state and no inverse-cancellation recursive call.

---

## 4. The discrepancy word

When local normalization uses an alternative topology, the current source topology need not equal the target original topology `C_(ell-1)`.

Record the difference by one finite path in the ordinary Ptolemy flip groupoid of the fixed marked triangle surface. The endpoints are:

- the current normalized root topology;
- the target topology `C_(ell-1)`.

At fixed graph order, discrepancy scheduling uses:

- root Pachner flips;
- inverse root flips;
- involution deletion;
- disjoint-square commutation;
- five-leaf pentagon replacement;
- the local normalization macro of Section 3 whenever a comparison edge first fails;
- route, separator, or bounded exits.

No equal-face cancellation is required as a progress edge in the normalized fixed-order layer.

---

## 5. Local Ptolemy relations

The exact local relations are:

### Involution

A root flip followed by its inverse deletes literally, including complete source labels and cap data.

### Far commutativity

Disjoint source surgeries commute. A transient first-failure atom meets at most one support and normalizes without branching.

### Pentagon

For one conserved five-root boundary, the root-valid topologies form one cyclic interval. Therefore:

1. if both comparison endpoints are root-valued, the opposite pentagon path is root-valued;
2. if a short comparison first fails, the failure moves monotonically to one interval endpoint;
3. every zero endpoint is normalized by Section 3;
4. every co-root endpoint retains one oriented resolution sheet;
5. no local cell creates two persistent discrepancies.

Thus every local relation has a root-normalized lift or an accepted exit.

---

## 6. Global discrepancy tracks

In a lifted Ptolemy comparison, the transient first-failure loci form nonbranching tracks after immediate local normalization.

The old local-to-global error was the assumption that every closed track stayed in one five-leaf neighbourhood. The controlling full-state chain is instead:

1. resolve maximal constant-pivot runs with all side data retained;
2. delete immediate pivot backtracks;
3. extract a shortest simple Petersen core of length `5,6,8,9`;
4. exclude `C5,C9` by the oriented cap character;
5. replace `C6,C8` by singularity-free root annuli.

### Theorem 6.1 — closed-track erasure

Every internal closed discrepancy track in a lifted fixed-order Ptolemy diagram is impossible or removable while fixing the complete labelled outer boundary.

This is `PTOLEMY_CLOSED_DEFECT_TRACK_ERASURE_V1.md`.

---

## 7. No normalized fixed-order loop

A **normalized fixed-order scheduling loop** is a nonempty closed sequence of normalized contextual states in which:

- immediate inverse pairs have been deleted;
- disjoint moves are in the chosen canonical order;
- pentagon comparisons use the selected root interval path;
- every zero/co-root first failure has been normalized by Section 3;
- all removable closed defect tracks have been erased.

### Theorem 7.1 — no nonempty normalized loop

No normalized fixed-order scheduling loop exists under a fixed outer route and cap block, unless the loop contains an accepted route/profile, separator, or bounded exit.

### Proof

Project the alleged loop to the ordinary Ptolemy groupoid and choose a finite van Kampen reduction by involutions, squares, and pentagons.

Lift the reduction using Section 5. The singular locus is nonbranching. Every internal closed component is erased by Theorem 6.1. Under the no-exit assumption the lifted diagram reduces to the empty root-normalized history.

This contradicts that the original loop was nonempty and normalized. ∎

The proof uses the global forced-backbone classification and root-annulus replacement; it does not reduce a global track to one local five-leaf circuit.

---

## 8. Finite fixed-order scheduling rank

Fix:

- the target graph order;
- one prefix level `ell`;
- the finite exterior incidence set;
- five support labels;
- the cap matching and block;
- the finite target topology `C_ell`.

There are finitely many normalized contextual states and finite Ptolemy discrepancy words after canonical reduction.

Orient each allowed normalized macro by one deterministic rule:

1. first reduce involutions, disjoint inversions, and the chosen pentagon normal forms;
2. then attempt the next target-directed comparison flip;
3. normalize any first failure by Section 3;
4. take a route/separator/bounded exit immediately when exposed.

If the procedure did not terminate, one complete normalized state would repeat. The intervening segment would be a nonempty normalized fixed-order loop, contradicting Theorem 7.1.

Hence the finite normalized transition graph is acyclic. Let

\[
\operatorname{rk}_{\mathrm{norm}}
\]

be any reverse topological rank on this finite DAG.

### Theorem 8.1 — fixed-order discrepancy termination

At one fixed prefix level, every normalized discrepancy schedule reaches after finitely many steps:

1. a root flow on the target topology `C_ell`;
2. a cap-compatible strict-prefix terminal;
3. a route/profile lift;
4. a separator/category exit;
5. a bounded direct/theta terminal.

There is no cancellation-recursion outcome.

---

## 9. Contextual inverse transfer

Order transfer obligations lexicographically by

\[
\boxed{
\bigl(\ell,\operatorname{rk}_{\mathrm{norm}}\bigr).
}
\]

- Consuming one original inverse step lowers `ell`, whether the restored value was root, zero, or co-root.
- Scheduling at fixed `ell` lowers `rk_norm`.
- Route, separator, and bounded outcomes leave the obligation.

### Theorem 9.1 — repaired contextual transfer

Every cap-compatible terminal root state on `C_m` transfers through the finite mixed Pachner/cancellation history to a cap-compatible root state on `C_0`, or exits through an already accepted route/profile, separator/category, or bounded direct/theta branch.

The proof uses no induction on graph order and never treats an equal-face cancellation as an automatically completed lower-order exit.

### Proof

Induct on `(ell,rk_norm)`.

If `ell=0`, the target original context has been reached. For `ell>0`, consume the next inverse original step and normalize it by Theorem 3.1, lowering `ell`. Apply Theorem 8.1 to eliminate the finite discrepancy at the new prefix. Every resulting branch lowers the lexicographic pair or exits. ∎

---

## 10. Resolution of the cancellation re-entry gap

The former problematic macro was

\[
\text{cancel}
\to
N-2
\to
\text{choose arbitrary flow}
\to
\text{attempt inverse weld}
\to
N\text{ token re-entry}.
\]

The repaired proof never performs this macro.

When an inverse cancellation is encountered under the actual returned flow, apply the complete local table directly:

\[
\begin{array}{c|c}
\text{reconnecting roots}&\text{same-order disposition}\\
\hline
\text{distinct intersecting}&\text{inverse insertion succeeds}\\
\text{equal}&\text{two-NNI borrowing rootification}\\
\text{disjoint}&\text{oriented co-root resolution}.
\end{array}
\]

Therefore arbitrary lower-order flow selection and marked-weld return are unnecessary for contextual transfer.

`MARKED_WELD_RELATIVE_CONTEXTUAL_RETURN_TARGET_V1.md` remains a mathematically sufficient alternative repair target, but it is no longer the preferred controlling route.

---

## 11. Consequence for one-cross cap restoration

Assume the previously retained packages:

1. one valid smaller cross closure for every simple edge;
2. selected-cross boundary trichotomy;
3. six exact route rows;
4. horizontal equality/DDD rescue or one oriented fixed-route lock;
5. finite equality/DDD current-flow Morse descent;
6. route and direct-terminal normalization.

Apply Theorem 9.1 to every cap-compatible descendant terminal produced by the current-flow descent. It returns the terminal through the complete finite history without target-order recursion.

Thus the formerly blocked R2.7 interface is repaired at the authorial theorem level, conditional only on reconstruction of the concrete source-level inputs listed at the head of this file.

No claim of downstream acceptance is made here.

---

## 12. PDL reconstruction target

PDL should reconstruct v4 in this order:

1. define original-prefix level and fully root-normalized states;
2. independently verify the quadruple-equality two-NNI borrowing theorem;
3. verify category safety of all local normalization macros;
4. reconstruct local involution/square/pentagon lifts;
5. reconstruct full-state closed-track reduction;
6. prove the two-sided `C6/C8` root-annulus replacement;
7. prove closed-track erasure in a minimal lifted diagram;
8. define one deterministic normalized scheduling rule;
9. obtain the finite acyclic rank;
10. induct only on `(remaining original prefix, normalized rank)`.

PDL must not reintroduce:

- cancellation as an automatic `N-2` exit;
- token-only SCCs without treating mixed root/token states;
- global-track reduction to one local pentagon;
- abstract tube words as source-history lifts.

---

## 13. Assurance boundary

### New exact authorial claims

- every inverse-history failure has a same-order root normalization of length at most two or an accepted exit;
- quadruple equality is nonrecursive;
- internal closed discrepancy tracks erase globally by full-state Petersen reduction and root annuli;
- no nonempty normalized fixed-order scheduling loop survives;
- the normalized finite state graph is acyclic;
- contextual inverse transfer is well founded on `(original prefix, normalized rank)`;
- no target-order cancellation induction is needed.

### Imported authorial mathematics

- root triangle/Pachner dictionary;
- first-failure localisation;
- inverse-flip zero classification;
- co-root triality and oriented resolution;
- five-leaf root interval theorem;
- Ptolemy groupoid presentation;
- full-state track/backbone identification;
- constant-pivot root sections;
- odd orientation exclusion;
- even root-annulus replacement;
- route and direct-terminal conversion.

### Not yet supplied

- PDL reconstruction of v4;
- independent mathematical audit;
- canonical curation;
- Lean verification;
- manuscript integration;
- restored global closure status on controlling summary files;
- release, arXiv, DOI, peer review, or publication.
