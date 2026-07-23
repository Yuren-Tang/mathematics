# Five-support closure from one cross flow

## Research dossier v5 — current minimal authorial spine

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `3af8dc81ec9a7512659c6c1d188b0c416dae50b0`.

**Supersedes for controlling architectural use:** every earlier global closure dossier through `FIVE_SUPPORT_GLOBAL_ONE_CROSS_CLOSURE_V4.md`.

**Controlling modules:**

1. root-flow equivalence and root triality;
2. `ONE_CROSS_RECONNECTION_EXISTENCE_V1.md`;
3. `ONE_CROSS_SINGULAR_FIXED_ROUTE_REDUCTION_V1.md`;
4. `SINGULAR_CARRIER_DISCRETE_MORSE_UNIFICATION_V1.md`;
5. `SINGULAR_ROOT_TRIALITY_CONFLUENCE_MASTER_THEOREM_V2.md`;
6. `ONE_CROSS_CAP_RESTORATION_THEOREM_V1.md`;
7. the general-graph outer shell.

**Status:** shortest current authorial candidate. It remains unverified by PDL and independent audit.

---

## 1. Root formulation

Let

\[
E_5=\{x\in\mathbf F_2^5:\sum_i x_i=0\},
\qquad
R_5=\{e_i+e_j:i<j\}.
\]

Five indexed even supports covering each edge twice are equivalent to an `R_5`-valued flow. At every cubic vertex the three root labels form one triangle of `K_5`.

The cubic theorem is therefore:

> every finite connected loopless bridgeless cubic multigraph admits an `R_5`-valued flow.

---

## 2. Minimal counterexample and one simple edge

Assume a minimum-order cubic counterexample `G`.

The two-vertex theta graph is root-soluble. Every connected loopless cubic multigraph with more than two vertices has a simple edge `uv`; otherwise cubic degree forces the whole connected graph to be theta.

Delete `u,v` and retain the four other incidences. Of the two cross reconnection closures, at least one is connected, loopless, bridgeless, cubic, and has two fewer vertices.

The graph proof uses only:

- the `2+2` exterior component dichotomy;
- cycles through new cross edges;
- laminarity of bridge cuts versus the two crossing terminal partitions;
- incompatibility of cross loops with each other and with the opposite bridge partition.

Minimality supplies a root flow on one selected cross closure.

No cut reduction or second reconnection flow is used.

---

## 3. Three boundary possibilities and six route rows

Let the two cross edges carry roots `p,q`.

- If `p,q` are distinct and intersect, the original cap glues immediately.
- If `p=q`, the insertion defect is zero and the selected boundary state is `A`.
- If `p,q` are disjoint, the insertion defect is a co-root and the selected state is `C_j`.

Assume the original cap profile `K_i` is blocked.

### Equality orbit

At `A`, the two non-`M_i` route targets lie in `K_i`. Blocking forces route `M_i` and the outer path

\[
A-B_i-C_i.
\]

### DDD orbit

At `C_j`, the two non-`M_i` targets lie in `K_i`. Blocking forces route `M_i` and the outer path

\[
C_j-D_i-C_k.
\]

The relevant rows at the three states of each path keep every locked challenge on that path. A separating Kempe component repairs the cap immediately; otherwise one obtains an oriented singular full-channel lock.

The complete ten-state profile and all-three reconnection classification are unnecessary.

---

## 4. One singular carrier termination theorem

Equality and DDD are the two singular root-triality boundary orbits.

For the equality orbit use the positive triangle weights

\[
(4,5,7,3,3,3,3,3,3,1),
\]

and for the DDD orbit use

\[
(4,1,2,4,1,2,2,4,4,4),
\]

in triangle order

\[
123,124,125,134,135,145,234,235,245,345.
\]

In either orbit every nonempty carrier has a root `2--2` move or equal-face `2--0` cancellation strictly decreasing the corresponding positive additive Morse sum.

Thus both locked carriers admit finite forward histories. They are two finite certificates for one termination theorem, not two global proof architectures.

---

## 5. Terminal normalisation

A forward history can produce only:

1. a route change, which is a cap-compatible state on the current descendant;
2. a zero-vertex direct matching, converted to the root-soluble theta terminal;
3. a genuine equal-face cancellation, lowering target order.

Root-valued NNI is automatically bridgeless by the bridge-zero law. Cancellation is componentwise lower-order descent.

---

## 6. Singular contextual confluence

An arbitrary root flow on a terminal descendant is transported backwards.

The first failed inverse move creates exactly one zero/co-root edge. Zero disappears immediately. A co-root token moves through labelled critical overlaps without branching.

At fixed target order the complete labelled token graph is finite. Constant-pivot runs have unique full-state root sections. Any recurrent token path has a shortest pivot-closed Petersen subtrack.

The original cap distinguishes one route block. Hence every physical pivot-closed subtrack has zero orientation character and therefore even length. This excludes `C5,C9` and also excludes any double traversal of an odd core: its first lap is already an inadmissible odd pivot-closed segment.

The remaining cores are:

- `C6`, one root NNI from a canonical star with an equal-face dipole;
- `C8`, two seam-compatible `C6` source cells.

Both force strict cancellation.

There is therefore no terminal-free sink SCC. Lexicographic induction on

\[
(	ext{target order},	ext{remaining history length})
\]

returns every cap-compatible terminal to the original four-pole.

---

## 7. Restore the edge

The returned state lies in the original cap profile. Glue the cap to recover a root-valued flow on `G`, contradicting minimality.

Thus every connected loopless bridgeless cubic multigraph has five indexed even supports covering each edge twice.

---

## 8. General graphs

Apply the cubic theorem componentwise. For an arbitrary finite bridgeless multigraph, use port-cycle cubic expansion, project the same five supports memberwise back to the original graph, and insert every deleted loop into two fixed supports.

Hence every finite bridgeless multigraph has a `5`-cycle double cover in the standard even-subgraph sense.

---

## 9. Four controlling proof packages for PDL

### A — local algebra

- root-flow/support equivalence;
- `K_5` triangle law;
- root triality;
- bridge-zero law.

### B — one-cross graph theorem

- simple-edge existence;
- exterior component dichotomy;
- bridge-cut laminarity;
- loop/bridge incompatibility.

### C — singular edge restoration

- cross boundary trichotomy;
- six route rows and horizontal rescue;
- two-orbit Morse termination;
- terminal normalisation;
- first-failure token grammar;
- orientation-hardened odd exclusion;
- `C6/C8` source movies;
- singular confluence induction.

### D — outer shell

- componentwise assembly;
- cubic expansion/collapse;
- loop reinsertion.

---

## 10. Noncontrolling corpus

The current main line does not require:

- any two-, three-, or four-cut gluing theorem;
- all-three reconnections;
- complete ten-state profile classification;
- Type T or Type H mismatch elimination;
- cyclically five-edge-connected reduction;
- affine `A_3`, flat-code, octahedral Stokes, or reflection-supported `D_8` programmes;
- abstract tube-to-history lifting.

These remain side theorems, finite certificates, alternate routes, or discovery history.

---

## 11. Assurance boundary

This dossier claims one minimal, correction-aware authorial proof architecture. It does not claim successful PDL reconstruction, independent verification, Lean formalisation, manuscript acceptance, release, peer review, publication, or established truth of the 5-CDC conjecture.
