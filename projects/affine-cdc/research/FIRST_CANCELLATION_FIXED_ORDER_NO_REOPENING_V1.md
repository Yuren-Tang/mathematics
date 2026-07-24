# Fixed-order return after the first cancellation opens no new cancellation

## Research Lead v7 closure lemma v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `2c20f3a023894dbdd4e387b30f14127e2ad51e39`

**Controls with:**

- `FIRST_CANCELLATION_TARGET_CAP_TERMINALISATION_V1.md`;
- `FIRST_CANCELLATION_SINGLE_POP_TARGET_TOPOLOGY_SCOPE_CORRECTION_V1.md`;
- `TARGET_TOPOLOGY_ARBORESCENCE_FIXED_ORDER_V1.md`;
- the inverse root/zero/co-root `2--2` table;
- the full-state first-failure/critical-overlap grammar;
- `CELLWISE_ROOT_SEAM_AND_CONSTANT_RUN_TRACK_ERASURE_V1.md` and its interface audit.

**Status:** exact authorial alphabet closure. After the first cancellation has been replaced by one lower target solution and one inverse pop, the return to the original target may be carried out entirely in the fixed-order `2--2`/one-atom alphabet. The appearance of an equal adjacent root-triangle pair during this return does not force or authorize a new `2--0` call. Equal-face cancellation is a possible source move in the forward monotone phase, but it is not a generator of the target-rooted fixed-order arborescence. Therefore v7 contains exactly one order-lowering event.

No theorem status is promoted.

---

## 1. Two different uses of an equal-face pair

An edge whose endpoint source triangles have the same support triangle has two logically distinct roles.

### Forward monotone descent

In the selected cross-flow equality/DDD carrier, an equal-face pair is the stopping event. V7 cancels the **first** such pair and immediately invokes lower-order ordinary solubility on the parallel target cap closure.

### Fixed-order inverse return

After the single inverse pop, the proof is no longer following the forward monotone descent. It is solving a target-normalization problem at one fixed labelled vertex order.

The scheduler is defined by a rooted spanning tree in the ordinary topology graph whose edges are only labelled `2--2` NNIs. Root labels are tested after the ordinary parent edge has been selected.

Hence an equal-face pair present in the current root flow is not a command to contract it.

---

## 2. Fixed-order generator alphabet

At one source-prefix level `ell`, the target normalization state records:

- a labelled cubic source topology on the fixed predecessor vertex slots;
- the required predecessor topology `C_ell`;
- a root flow or one normalized co-root atom;
- both crossed resolutions;
- the complete cap, route, support, side-output, incidence, and mark boundary data.

The internal generator alphabet is exactly:

1. ordinary target-tree `2--2` parent edges;
2. alternative crossed root `2--2` moves for zero failure;
3. bounded critical-overlap normalization with at most one atom;
4. local pivot-change root seams;
5. constant-pivot identity strips;
6. normalized endpoint collars;
7. periodic root crosscuts;
8. identity gluing of complete states.

Excluded from the internal alphabet:

- `2--0` cancellation;
- inverse `0--2` insertion other than the already completed single outer pop;
- a lower-order call;
- a raw support-switch cell;
- a second independent atom.

---

## 3. Equal-face occurrence under a selected parent NNI

Let the current complete state be root-valued and let the target arborescence select one ordinary parent NNI.

Expose the four exterior branch roots. The forced new diagonal has one of:

- a root;
- zero;
- a co-root.

### Root

Perform the parent NNI and lower target-tree distance.

### Zero

Use the other crossed root NNI or the exact bounded zero normalization. No cancellation occurs.

### Co-root

Enter the standard one-atom forced-backbone state. No cancellation occurs.

If the local current flow happens also to contain an equal-face pair, that fact does not change the selected ordinary parent edge or add a fourth output row.

### Lemma 3.1 — no equal-face forcing

At fixed order, equal adjacency of two current root triangles is merely a property of the current colouring. It does not force the scheduler to contract their edge. Every selected parent edge remains governed by the root/zero/co-root/category table.

---

## 4. One-atom consumption without order descent

Every persistent nonroot state is one normalized co-root atom.

The repaired fixed-order consumer:

1. reduces to the full-state forced backbone;
2. excludes oriented odd cores;
3. inserts a local root seam at every pivot change;
4. replaces each constant-pivot run by the identity product of its unique nonpivot root history;
5. glues on literal complete endpoint states;
6. consumes normalized open endpoints and repeated periodic endpoints.

All internal cells are root-NNI/Ptolemy cells or identity strips. A root-valued equality of adjacent source triangles may occur in a boundary history, but no cell contracts it.

### Theorem 4.1 — fixed-order no-reopening

Every nonexit fixed-order target-normalization episode generated after the v7 single pop has a boundary-equivalent execution using no `2--0/0--2` cell.

It ends at:

- the required predecessor topology with a root state;
- a `K_i` route/cap lift;
- an exact bounded/small-cut/outer-shell terminal.

There is no output “first failure behind another cancellation”.

---

## 5. Lexicographic return rank

Let:

- `ell` be the number of pure source NNIs still to invert;
- `d_top` be the target-tree distance at the current prefix stage;
- `rho_atom` be the finite one-atom disposition rank supplied by the full-state track consumer.

Use

\[
\boxed{(\ell,d_{\rm top},\rho_{\rm atom})}
\]

lexicographically, with `rho_atom=0` in a root state.

- successful target normalization lowers `d_top`;
- one-atom normalization lowers `rho_atom` or exits;
- reaching the required predecessor topology permits crossing one source NNI and lowers `ell`;
- no move changes graph order.

The unique graph-order descent in v7 is the selected first cancellation already completed before this rank begins.

---

## 6. Consequence for v7

The controlling proof has three nested but noncircular measures:

1. equality/DDD forward potential until route exit or first cancellation;
2. ordinary target vertex number at the single lower target;
3. fixed-order `(ell,d_top,rho_atom)` return.

No variable-order call graph, mixed-history SCC, child-prefix rank, or cancellation stack is needed.

---

## 7. PDL obligations

PDL must verify:

1. the target arborescence contains only ordinary `2--2` edges;
2. the chosen normalized scheduler never selects a `2--0` edge;
3. equal-face adjacency does not add an output row to the forced NNI table;
4. zero normalization remains root-NNI/local and same-order;
5. co-root normalization remains one-atom and same-order;
6. the repaired cellwise R2.6 consumer uses no hidden cancellation;
7. every fixed-order terminal is explicitly consumed;
8. the lexicographic return rank is well founded.

Return one exact obstruction if any claimed fixed-order macro necessarily contracts an equal-face pair.

---

## 8. Trust boundary

### Exact here

- separation of forward first-cancellation stopping from fixed-order return;
- fixed-order generator alphabet;
- no equal-face forcing at fixed order;
- no-reopening theorem;
- fixed-order return rank;
- uniqueness of the v7 order descent.

### Still required

- PDL reconstruction;
- independent audit of the fixed-order scheduler and cellwise consumer.

### Not claimed

- PDL completion;
- independently accepted cap restoration;
- established five-support/five-CDC theorem;
- Lean, Curator, manuscript, release, or publication status.
