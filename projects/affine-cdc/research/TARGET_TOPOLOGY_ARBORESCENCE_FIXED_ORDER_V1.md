# Fixed-order target topology arborescence

## Research Lead scheduling lemma v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`

**Parent:** `ROOT_NORMALIZED_CONTEXTUAL_TRANSFER_MASTER_V5.md` v5.1.

**Status:** exact ordinary-topology scheduling theorem. At one fixed original-prefix level, every nonexit topology produced by the order-restoring inverse table belongs to the same finite ordinary `2--2` move component as the required original topology. Choosing a rooted spanning tree of that component gives a canonical parent move. Every successful root-valued parent move strictly lowers tree distance; every unsuccessful parent move is exactly a local zero/co-root first failure or an accepted category/route exit. Therefore no scheduling cycle can consist solely of root-valued states.

The theorem is uncoloured at the arborescence-existence layer. It does not assume that every tree edge is root-admissible. Root admissibility is tested only when the selected parent edge is attempted.

---

## 1. Fixed incidence universe

Fix:

- one original-prefix level `ell`;
- the predecessor order
  \[
  N=|V(C_\ell)|;
  \]
- the ordered exterior incidence set, cap shore and distinguished cap block;
- a labelled set of `N` source-vertex slots.

Alternative inverse insertions reuse the labelled vertex slots of the original predecessor neighbourhood. In the five-leaf borrowing rows, the two reinserted vertices and the borrowed adjacent vertex are the same three labelled vertices on every local topology; only their internal tree topology changes.

Let

\[
\mathfrak T_{N,\ell}
\]

be the set of finite labelled cubic multigraph topologies on this incidence universe which occur as:

1. `C_ell` itself;
2. an order-restoring local inverse output;
3. a local critical-overlap normalization output;
4. an intermediate or boundary topology in one of the imported relative Ptolemy, strip or annulus movies.

Only topology is retained here; root labels and singular values are forgotten.

Because the vertex and incidence sets are finite,

\[
\boxed{|\mathfrak T_{N,\ell}|<\infty.}
\]

---

## 2. Ordinary move graph

Form the undirected graph

\[
\Gamma_{N,\ell}
\]

whose vertices are `mathfrak T_(N,ell)` and whose edges are ordinary labelled `2--2` replacements on two adjacent cubic vertices with the same four exterior branches.

The edge definition is purely combinatorial. It does not require either endpoint to carry a root flow and does not require the replacement to remain in the prime connected/bridgeless category.

If an attempted edge creates a loop, bridge, parallel bounded degeneration or accepted separator, the contextual proof exits through the established category branch. Hence including such an ordinary edge in the ambient topology graph does not assert that it is an internal admissible move.

---

## 3. Local connectivity of every inverse output

### 3.1 Inverse `2--2`

The restored predecessor topology and both crossed alternatives are the three vertices of one ordinary NNI triangle. Therefore:

- root success is already the predecessor topology;
- the zero alternative is one ordinary edge from it;
- the co-root discrepancy topology is one of the same three local resolutions.

All lie in one component of `Gamma_(N,ell)`.

### 3.2 Quadruple equality alternative insertion

On the borrowed five-leaf region, the original predecessor and alternative root insertion are

\[
T_0=BC\mid A\mid DE,
\qquad
T_3=AE\mid C\mid BD.
\]

They are joined in the ordinary five-leaf pentagon by

\[
T_0-T_4-T_3.
\]

The intermediate root validity is irrelevant for ordinary connectivity.

### 3.3 Good doubled-disjoint alternative insertion

The same labelled topologies `T_0,T_4,T_3` occur. Thus the alternative insertion is in the predecessor component independently of the returned support labels.

### 3.4 Missing-index doubled-disjoint

The missing-index state occurs on the same ordinary topology `T_4` in the same five-leaf pentagon. Full-defect-tree normalization uses one further local NNI on the same labelled incidence neighbourhood. Hence every resulting one-atom topology remains in the predecessor component.

### 3.5 Critical overlaps

A first-failure atom meeting one adjacent root move is supported on a bounded three-vertex tree. The good branches commute or relocate the atom through one NNI. The unique bad branch creates a three-vertex two-co-root tree and immediately applies the category-safe root-lowering NNI. Forgetting labels, every stage is connected by the displayed local `2--2` edges.

### 3.6 Strip and annulus movies

Every canonicalisation cell in the open strip or closed annulus is a relative root-preserving NNI or identity step on fixed exterior branches. Hence every source topology appearing in these movies lies in the same ordinary component as its boundary topology.

### Theorem 3.1 — component containment

Every topology in `mathfrak T_(N,ell)` which is reachable from the current inverse-transfer obligation without an accepted exit lies in the ordinary `2--2` component of the target topology `C_ell`.

### Proof

The initial topology is `C_ell`. Sections 3.1--3.6 show that each generating nonexit macro changes topology by a finite path of ordinary labelled `2--2` edges. Component membership is preserved under concatenation. ∎

---

## 4. Rooted spanning tree

Let

\[
\Gamma^0_{N,\ell}
\]

be the component of `C_ell` in `Gamma_(N,ell)`.

It is finite and connected. Choose once and for all a spanning tree

\[
\mathcal A_{N,\ell}
\]

rooted at `C_ell`.

For every nonroot topology `T`, let:

- `p(T)` be its unique parent;
- `d_top(T)` be its tree distance to `C_ell`.

Then

\[
\boxed{d_{\rm top}(p(T))=d_{\rm top}(T)-1.}
\]

The choice may be made by any fixed deterministic ordering of labelled topology codes. No root labels enter the choice.

---

## 5. Attempting one parent edge

Let the current complete state be fully root-valued on topology `T neq C_ell`. Attempt the unique ordinary parent replacement

\[
T\to p(T).
\]

Expose its four exterior branch roots. Their three pairing sums have one of the established patterns

\[
(0,0,0),\quad(0,2,2),\quad(0,4,4),\quad(2,2,4).
\]

Exactly one of the following occurs.

### Root success

The forced parent diagonal is a root. Perform the parent move. All unchanged source labels and exterior data remain fixed, and

\[
d_{\rm top}\text{ decreases by }1.
\]

### Zero failure

The forced parent diagonal is zero. The first-failure theorem gives one zero atom. The alternative-root NNI or direct alternative inverse-insertion theorem normalizes it locally. The scheduler enters a same-order discrepancy macro; it does not pretend that the parent move succeeded.

### Co-root failure

The forced parent diagonal is a co-root. The state enters the one-atom forced-backbone grammar with both crossed root resolutions and complete side data retained.

### Category or route exit

If the ordinary replacement is not an internal connected loopless bridgeless fixed-route move, the category-safe theorem exposes a bounded degeneration, separator or route/profile escape.

### Theorem 5.1 — parent-edge alternative

Every selected parent edge yields:

\[
\boxed{
\text{strict topology-distance descent}
\quad\text{or}\quad
\text{one normalized co-root discrepancy}
\quad\text{or}\quad
\text{accepted exit}.}
\]

No fourth outcome occurs.

---

## 6. Exclusion of pure-root scheduling cycles

Consider the canonical scheduler which, whenever the state is fully root-valued and not on `C_ell`, attempts only the parent edge of `mathcal A_(N,ell)`.

### Corollary 6.1

A directed cycle of canonical normalized states cannot consist solely of successful root-valued parent moves.

### Proof

Every such edge lowers the nonnegative integer `d_top` by one. A positive-length directed cycle would strictly lower and restore the same value, impossible. ∎

Therefore every nonexit scheduling cycle contains at least one zero/co-root first-failure event. After local zero normalization, every unbounded cycle contains one full-labelled co-root singular track and is subject to the closed/open/periodic track theorems.

---

## 7. Why this does not assume coloured connectivity

The arborescence exists in the ordinary uncoloured topology graph. It does not assert:

- that every ordinary move is root-valued;
- that two root-coloured topologies are joined by an all-root path;
- that arbitrary root flows are Kempe equivalent;
- that a balanced or coloured Pachner connectivity theorem applies.

A non-root parent edge is exactly the event which creates the normalized singular locus studied by R2.7. Thus the topology tree supplies scheduling, while the root-track machinery supplies admissibility repair.

---

## 8. Assurance boundary

### Exact here

- finiteness of the fixed labelled topology universe;
- ordinary `2--2` component containment of every order-restoring local output;
- explicit five-leaf connectivity of equality, good-disjoint and missing-index rows;
- existence of the target-rooted spanning tree;
- strict descent of every successful root parent move;
- complete root/zero/co-root/category alternative for an attempted parent edge;
- exclusion of pure-root canonical scheduling cycles.

### Imported authorial mathematics

- order-restoring local inverse table;
- first-failure pairing-sum classification;
- category-safe local NNI theorem;
- source topology of critical-overlap, strip and annulus movies.

### Not claimed

- root-admissibility of all arborescence edges;
- PDL reconstruction or independent audit;
- complete R2 beyond the conditional v5.1 assembly;
- global five-CDC, Lean, manuscript, curation, release or publication status.
