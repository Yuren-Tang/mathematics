# Global five-support closure from one cross reconnection

## Research dossier v4 — minimal controlling architecture

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `0eb0007de0a3765def93a70aff7130929225ddab`.

**Supersedes for controlling architectural use:**

- `FIVE_SUPPORT_GLOBAL_MINIMAL_COUNTEREXAMPLE_CLOSURE_V1.md`;
- `FIVE_SUPPORT_GLOBAL_MINIMAL_COUNTEREXAMPLE_REPAIRED_V2.md`;
- `FIVE_SUPPORT_GLOBAL_MINIMAL_COUNTEREXAMPLE_COMPRESSED_V3.md`.

**Load-bearing parents:**

- root-flow equivalence and root triality;
- `ONE_CROSS_RECONNECTION_EXISTENCE_V1.md`;
- `ONE_CROSS_SINGULAR_FIXED_ROUTE_REDUCTION_V1.md`;
- `ONE_CROSS_CAP_RESTORATION_THEOREM_V1.md`;
- `SINGULAR_ROOT_TRIALITY_CONFLUENCE_MASTER_THEOREM_V1.md`;
- the general-graph outer shell.

**Status:** shortest current authorial candidate architecture. A vertex-minimal cubic counterexample is closed using one simple edge, one smaller cross reconnection flow, six outer-route rows, and the singular contextual-confluence theorem. No low-cut gluing, all-three reconnection theorem, complete profile classification, cyclic four-cut analysis, Type T, or Type H theorem is required.

**Assurance boundary:** authorial compression only. The concrete singular-confluence hypotheses remain to be independently reconstructed and audited.

---

## 1. Intrinsic statement

Let

\[
E_5=\{x\in\mathbf F_2^5:\sum_i x_i=0\},
\qquad
R_5=\{e_i+e_j:i<j\}.
\]

A five-support cycle double cover of a cubic graph is exactly a flow

\[
\lambda:E(G)\to R_5
\]

satisfying Kirchhoff conservation.

At every cubic vertex the three incident roots are the three edges of one triangle of `K_5`.

### Cubic target

Every finite connected loopless bridgeless cubic multigraph has an `R_5`-valued flow.

---

## 2. Minimal counterexample has a simple edge

Assume the cubic target false and choose a counterexample `G` with minimum vertex number.

A loop cannot occur in a connected bridgeless cubic graph.

If `G` has two vertices, it is the theta multigraph and has the explicit root triangle

\[
12,13,23.
\]

Assume `|V(G)|>2`.

If every adjacency had multiplicity at least two, cubic degree would force every vertex to belong to one triple-edge two-vertex component. Connectedness would make `G` the theta graph. Therefore `G` has a simple edge

\[
uv.
\]

No edge-cut reduction is used.

---

## 3. One smaller cross closure

Delete `u,v`, retaining the four other incidences

\[
a,b\mid c,d.
\]

The two cross matchings are

\[
M_j=ac\mid bd,
\qquad
M_k=ad\mid bc.
\]

By `ONE_CROSS_RECONNECTION_EXISTENCE_V1.md`, at least one cross closure, say

\[
G_j,
\]

is a connected loopless bridgeless cubic multigraph with

\[
|V(G_j)|=|V(G)|-2.
\]

The proof is purely graph-theoretic:

- one of the cross matchings connects every possible `2+2` exterior component partition;
- bridge cuts of one graph are laminar, while the two cross terminal partitions cross;
- loop coincidence in one cross matching prevents the other cross partition from being a bridge cut;
- two simultaneous cross loops would force a bridge in the original graph.

Minimality gives a root flow on `G_j`.

No second cross flow and no direct-reconnection flow is used.

---

## 4. The selected cross boundary state

Let the two new cross edges carry roots

\[
p,q\in R_5.
\]

Relative to the cross matching `M_j`, the boundary state of the deleted four-pole is one of

\[
J_j=\{A,B_j,C_j\}.
\]

### Intersecting roots

If `p,q` are distinct and intersect, the state is `B_j`. Since

\[
B_j\in K_i,
\]

where `K_i` is the original cap profile, the original cap glues immediately.

### Singular roots

Only two failures remain:

\[
p=q
\quad\Longleftrightarrow\quad A,
\]

or

\[
p\cap q=\varnothing
\quad\Longleftrightarrow\quad C_j.
\]

They are the zero and co-root singular fibres of the same root triality.

---

## 5. Six finite route rows

Assume the original cap is blocked, since otherwise the theorem is already proved.

The complete profile is not classified. Only the Kempe orbit of the selected state is used.

### Equality orbit

Starting from `A`, every relevant challenge has three matching targets

\[
B_i,B_j,B_k.
\]

The latter two lie in `K_i`; blocking forces route `M_i` and target `B_i`.

The two rows at `B_i` and the row at `C_i` then force the outer path

\[
A-B_i-C_i
\]

with route `M_i` throughout.

### DDD orbit

Starting from `C_j`, every crossed challenge has one target on

\[
C_j-D_i-C_k
\]

under `M_i`, while the other two targets lie in `K_i`.

The rows at `D_i,C_k` keep the selected orbit on this outer path with route `M_i`.

Thus one selected cross flow gives exactly one of:

1. immediate cap lift;
2. horizontal Kempe rescue;
3. an oriented equality or DDD full-channel lock with original cap route `M_i`.

The full ten-state profile classification and all-three intersections are unnecessary.

---

## 6. Singular contextual confluence

For a surviving lock:

- the equality potential gives a finite forward history on boundary `r,r,r,r`;
- the DDD potential gives a finite forward history on boundary `p,p,q,q`;
- root NNI is automatically category-safe;
- equal-face cancellation enters lower vertex order.

Every route change gives a cap-compatible terminal. Every zero-vertex matching is converted to the root-soluble theta terminal.

An arbitrary root flow on a terminal descendant is returned by `SINGULAR_ROOT_TRIALITY_CONFLUENCE_MASTER_THEOREM_V1.md`.

Its concrete token theorem says:

1. first inverse failure is one zero/co-root edge;
2. zero disappears immediately;
3. a co-root token moves without branching;
4. constant-pivot runs have unique full-state root sections;
5. odd Petersen cores cannot close the oriented sheet;
6. even `C6` has a root NNI to a cancellable canonical star;
7. `C8` is two seam-compatible `C6` cells.

The induction order is

\[
(	ext{target vertices},	ext{remaining history length}).
\]

Hence the cap-compatible terminal returns to the original four-pole and the original edge `uv` is restored root-valuedly.

---

## 7. Cubic contradiction

The one smaller cross flow therefore gives a root flow on `G` by `ONE_CROSS_CAP_RESTORATION_THEOREM_V1.md`.

This contradicts minimality.

### Theorem 7.1 — cubic five-support candidate

Every finite connected loopless bridgeless cubic multigraph has a root-valued `E_5` flow, equivalently five indexed even supports covering each edge exactly twice.

---

## 8. General graphs

Apply the connected cubic theorem componentwise.

For a general finite bridgeless multigraph:

1. delete loops;
2. perform the standard port-cycle cubic expansion;
3. obtain five indexed supports on the cubic expansion;
4. project the same five supports memberwise to the original edges;
5. add each deleted loop to two fixed support members.

### Theorem 8.1 — full 5-CDC candidate

Every finite bridgeless multigraph has five even edge sets such that every edge belongs to exactly two of them.

---

## 9. Minimal controlling theorem DAG

The current proof architecture is

\[
\boxed{
\begin{array}{c}
\text{root-flow equivalence and local triality}\\
\Downarrow\\
\text{one valid cross reconnection at a simple edge}\\
\Downarrow\\
\text{six-row singular fixed-route reduction}\\
\Downarrow\\
\text{singular contextual confluence}\\
\Downarrow\\
\text{restore the edge and contradict minimality}\\
\Downarrow\\
\text{general-graph outer shell}.
\end{array}
}
\]

---

## 10. Removed from the controlling proof

The following are no longer prerequisites:

- cyclic two-cut gluing;
- cyclic three-cut gluing;
- cyclic four-cut gluing;
- all-three reconnection category theorem;
- complete blocked-profile classification;
- Type T physical mismatch elimination;
- Type H BBD/DDD mismatch elimination;
- cyclically five-edge-connected reduction;
- affine `A_3`, flat-code, Stokes, and `D_8` programmes;
- abstract tube-to-history lifting.

They remain valid side theorems, alternate certificates, or discovery history.

---

## 11. Computational sanity check for the graph lemma

The one-cross graph theorem was checked independently on:

- all connected bridgeless cubic simple graphs available in the NetworkX graph atlas;
- `2,566` randomly generated connected bridgeless cubic simple graphs of orders through `28`;
- `5,000` randomly generated loopless connected bridgeless cubic multigraphs of orders through `16`.

For every tested simple edge, at least one cross closure was connected, loopless, cubic, and bridgeless. No counterexample was found.

This finite check is not part of the proof; the laminar bridge-cut argument is the theorem.

---

## 12. PDL reconstruction packages

### Package A — local algebra

- root-flow/support equivalence;
- `K_5` triangle law;
- root triality;
- bridge-zero law.

### Package B — one-cross graph theorem

- simple-edge existence outside theta;
- exterior component dichotomy;
- new-edge cycle argument;
- laminar bridge-cut incompatibility;
- loop/bridge incidence incompatibility.

### Package C — one-cross cap restoration

- cross boundary trichotomy;
- six route rows;
- horizontal rescue;
- equality/DDD termination;
- terminal normalisation;
- singular confluence.

### Package D — outer shell

- componentwise assembly;
- cubic expansion/collapse;
- loop reinsertion.

---

## 13. Current authorial status

### Claimed

- one four-package candidate architecture;
- a proof route requiring only one smaller cross flow;
- removal of every low-cut and full-profile dependency from the main line.

### Not claimed

- successful independent reconstruction of the one-cross graph theorem;
- successful reconstruction of all singular-confluence hypotheses;
- canonical theorem status;
- Lean verification;
- manuscript, release, or publication status;
- established truth of the 5-CDC conjecture.
