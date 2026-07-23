# Five-support closure from one cross flow

## Research dossier v6 — finite-condensation controlling spine

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `228ccfb4eb2693a6c8b8ecdc9bf969db2e902d7c`.

**Supersedes for controlling architectural use:** `FIVE_SUPPORT_GLOBAL_ONE_CROSS_CLOSURE_V5.md`.

**Controlling modules:**

1. root-flow equivalence, triangle law, root triality, and bridge-zero;
2. `ONE_CROSS_RECONNECTION_EXISTENCE_V1.md`;
3. `ONE_CROSS_SINGULAR_FIXED_ROUTE_REDUCTION_V1.md`;
4. `SINGULAR_CARRIER_DISCRETE_MORSE_UNIFICATION_V1.md`;
5. terminal normalisation and first-failure one-token grammar;
6. `ORIENTED_ODD_PETERSEN_SUBTRACK_EXCLUSION_V1.md`;
7. the full-state `C6/C8` source movies;
8. `SINGULAR_ROOT_TRIALITY_CONFLUENCE_MASTER_THEOREM_V3.md`;
9. `ONE_CROSS_CAP_RESTORATION_THEOREM_V1.md`;
10. `SIMPLE_EDGE_FIVE_SUPPORT_REDUCIBILITY_V1.md`;
11. the general-graph outer shell.

**Mechanism interpretations and scope boundaries:**

- `SINGLE_DEFECT_DIRECT_AUGMENTATION_BOUNDARY_V1.md`;
- `COLOURED_PACHNER_RELATIVE_WELD_INTERPRETATION_V1.md`.

**Status:** shortest current correction-aware authorial candidate. It remains unverified by Proof Development Lead reconstruction and independent audit.

---

## 1. Intrinsic theorem

Put

\[
E_5=\{x\in\mathbf F_2^5:\sum_i x_i=0\},
\qquad
R_5=\{e_i+e_j:i<j\}.
\]

Five indexed even supports covering every edge exactly twice are equivalent to a flow

\[
\lambda:E(G)\to R_5.
\]

At every cubic source vertex the three root labels are the three edges of one triangle of `K_5`.

Equivalently, the dual triangle pseudocomplex has a proper vertex coloring by the five support indices.

---

## 2. Structural reduction at one simple edge

Let `G` be a finite connected loopless bridgeless cubic multigraph.

- If `G` has no simple edge, cubic degree and connectedness force `G` to be the two-vertex theta multigraph.
- Theta has the explicit root triangle
  \[
  12,13,23.
  \]
- Otherwise choose any simple edge `uv`.

Delete `u,v`. The four exposed incidences admit two cross pairings. The one-cross graph theorem proves that at least one cross closure is:

- connected;
- loopless;
- bridgeless;
- cubic;
- smaller by exactly two vertices.

The proof uses only the exterior-component `2+2` dichotomy, laminarity of bridge cuts, crossing of the two terminal bipartitions, and the incompatibility of cross loops with the opposite bridge partition.

No low-cut gluing theorem and no second reconnection flow is required.

By induction, the selected cross closure has a root-valued flow.

---

## 3. The one-cross boundary trichotomy

Let the two new cross edges carry roots

\[
p,q\in R_5.
\]

Exactly one of:

1. `p,q` are distinct intersecting roots: the deleted cap restores immediately;
2. `p=q`: the central insertion value is zero and the selected boundary state is `A`;
3. `p,q` are disjoint: the central insertion value is one co-root and the selected state is `C_j`.

Assume the original cap is blocked.

### Equality outer path

The six relevant challenge rows force the selected equality orbit into

\[
A-B_i-C_i
\]

with physical route `M_i`.

### DDD outer path

The corresponding rows force the selected co-root orbit into

\[
C_j-D_i-C_k
\]

with the same physical route `M_i`.

A separating Kempe component repairs the cap. If no such component exists, the residual state is one **oriented full-channel singular lock**.

Only these six labelled rows are controlling. The complete ten-state profile classification is an optional finite strengthening.

---

## 4. One singular-carrier Morse theorem

Equality and DDD are the zero and nonzero singular fibers of the same root triality.

For the normalized equality boundary use the positive triangle weights

\[
(4,5,7,3,3,3,3,3,3,1),
\]

and for the normalized DDD boundary use

\[
(4,1,2,4,1,2,2,4,4,4),
\]

in triangle order

\[
123,124,125,134,135,145,234,235,245,345.
\]

Every nonempty singular carrier contains either:

- a root-valued `2--2` Pachner NNI strictly lowering its additive Morse sum; or
- an equal-face `2--0` cancellation strictly lowering the same sum.

Thus every locked carrier has a finite forward root-surgery history.

Equality and DDD are two finite orbit certificates for one theorem, not two global architectures.

---

## 5. Why defect minimality does not replace return

A first failed inverse move already creates exactly one zero/co-root edge. Large-defect-tree descent reaches the same one-edge normal form.

A root-valued alternative NNI may remove the defect, but it changes the source topology

\[
G\longmapsto G'.
\]

A root flow on `G'` does not imply a root flow on the original `G`; inverse NNI may recreate exactly one zero/co-root edge.

Therefore the argument

\[
\text{minimise defects}
\to
\text{perform root NNI}
\to
\text{declare }G\text{ solved}
\]

is circular. The final arrow is contextual return itself.

A true bypass would require either:

1. a fixed-topology simulation of every root NNI; or
2. a theorem selecting an extendable root-flow orbit on some valid cross closure.

Neither theorem is presently available.

---

## 6. Terminal normalisation

A finite forward history has only the following useful outcomes.

### Route terminal

A route change on a surgery descendant produces a state compatible with the original cap on that descendant. It is a terminal input for contextual return, not yet a state on the original four-pole.

### Direct matching terminal

Every zero-vertex direct matching is converted to a root-soluble theta terminal. The same-matching bridge topology is changed to theta by one crossed zero-to-root resolution.

### Cancellation

An equal-face cancellation lowers the closed cap-context target order by two. Root-valued NNI and the normalized root outputs are automatically category-safe by the bridge-zero law.

---

## 7. First-failure token

Start with an arbitrary root flow on a terminal descendant and reverse the finite history.

At the first failed inverse move:

- every old edge remains root-valued;
- exactly one new central edge is non-root;
- its value is
  \[
  0\quad\text{or}\quad Q_i;
  \]
- the ordered external root word, cap matching, distinguished cap block, and physical route data remain present.

Zero is immediately rootified inside a pure same-order flip block. Every persistent same-order token is therefore one co-root atom with two crossed root resolutions.

Complete labelled critical overlaps move the token without branching.

---

## 8. Relative colored-Pachner interpretation

The root-flow triangle pseudocomplex is properly five-colored.

- root NNI is a color-preserving `2--2` bistellar flip;
- equal-face cancellation is the relevant colored two-face weld;
- zero/co-root first failure is an improper inverse weld;
- the co-root token records relative projectivity along a sequence of colored flips.

Known colored Pachner connectivity compares two triangulations after both are already properly colored; it does not create a coloring on the original target topology. Relative coloring extension colors a subdivision, but undoing the subdivision is precisely the singular weld problem.

Thus the present theorem is a special **relative five-colored weld theorem** with an ordered four-port boundary. The interpretation unifies the mechanism but does not delete the confluence obligation.

---

## 9. Orientation-hardened recurrence classification

At fixed target order, a persistent co-root token gives a forced Petersen pivot walk after:

- full-state resolution of constant-pivot runs;
- removal of immediate backtracks;
- retention of all side-root and support-transport data.

The original cap distinguishes one physical route block. Every pivot-closed physical subtrack must stabilize that block. The route-orientation character equals pivot-length parity, hence every pivot-closed physical subtrack has even length.

This excludes `C5,C9`, including a proposed double traversal: its first odd lap is already an inadmissible pivot-closed physical segment.

The only primitive recurrent cores are:

- `C6`, one root NNI from a canonical star with an equal-face dipole;
- `C8`, decomposing into two seam-compatible `C6` source cells.

Both give genuine cancellation and strict target-order descent.

---

## 10. Finite-condensation contextual return

Fix one forward history and one target order `N`. Form the complete finite directed state graph containing:

- every inverse-history prefix level;
- every complete root-valued state;
- every normalized one-token state;
- all source topology, incidence, support, side-root, route, cap-block, and critical-neighborhood data;
- all root-prefix, token-relocation, terminal, and cancellation transitions.

Prefix level never increases and is constant on every strongly connected component.

A nonterminal sink SCC cannot contain a root state: a root state either crosses the next inverse move, first-fails into a token state, or is already terminal. Hence every bad sink SCC would consist entirely of persistent co-root states.

The orientation-hardened recurrence theorem extracts an even `C6/C8` core, and its source movie supplies a cancellation exit. Therefore no bad sink SCC exists.

Collapse SCCs. The finite condensation DAG supplies a canonical same-order rank. From every state there is a path to:

1. an original-context root terminal;
2. a normalized cap/theta terminal;
3. a genuine cancellation to target order `N-2`;
4. an accepted bounded/category discharge.

Only target order is an explicit induction parameter. No separate induction on history length is required.

---

## 11. Restore the edge

The finite-condensation theorem returns the cap-compatible terminal to the original four-pole. Glue the original two-vertex cap and recover a root-valued flow on `G`.

Thus every simple edge is five-support reducible:

\[
G/e\text{ root-soluble}
\Longrightarrow
G\text{ root-soluble}.
\]

Theta plus induction on vertex number proves the connected loopless cubic theorem.

---

## 12. General bridgeless multigraphs

Apply the cubic theorem componentwise. For an arbitrary finite bridgeless multigraph:

1. delete loops;
2. apply port-cycle cubic expansion;
3. obtain five even supports on the cubic expansion;
4. project each same indexed support memberwise to the original edges;
5. reinsert every loop into two fixed supports.

Every edge is covered exactly twice. Hence every finite bridgeless multigraph has a five-cycle double cover in the standard even-subgraph sense.

---

## 13. Four controlling PDL packages

### A — root language

- root-flow/support equivalence;
- `K_5` triangle law;
- root triality;
- bridge-zero.

### B — structural reducibility

- simple edge or theta;
- one valid cross closure.

### C — relative colored edge extension

- cross trichotomy and six route rows;
- horizontal rescue;
- positive singular Morse descent;
- route/theta terminal normalisation;
- first-failure one-token grammar;
- full-state forced backbone;
- distinguished-block odd exclusion;
- `C6/C8` source movies;
- finite-condensation no-sink theorem;
- target-order induction.

### D — induction and outer shell

- simple-edge reducibility;
- theta base and cubic induction;
- componentwise assembly;
- expansion/collapse and loop reinsertion.

---

## 14. Noncontrolling corpus

The current main line does not require:

- two-, three-, or four-cut gluing;
- all-three reconnections;
- complete ten-state blocked-profile classification;
- Type T/Type H four-cut mismatch elimination;
- cyclically five-edge-connected reduction;
- large defect-tree descent;
- affine `A_3`, flat-code, octahedral Stokes, or reflection-supported `D_8` programmes;
- abstract tube-to-history lifting;
- a universal partition-function identity on the ten support-unordered state counts.

These remain side results, certificates, alternate routes, exploration history, or future bypass directions.

---

## 15. Assurance boundary

This dossier gives one minimal, mechanism-aware, correction-aware authorial proof architecture.

It does not claim:

- successful PDL reconstruction of the structural or extension theorem;
- independent mathematical acceptance;
- Lean formalisation;
- manuscript integration;
- release, arXiv, DOI, peer review, publication;
- or established truth of the five-cycle double-cover conjecture.
