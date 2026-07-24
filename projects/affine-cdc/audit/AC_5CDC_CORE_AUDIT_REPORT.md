# AC-5CDC-AUDIT-CORE-01 — independent structural/core audit report

**Role:** `AffineCDC — Independent 5-CDC Structural/Core Auditor` (`AC-5CDC-AUDIT-CORE-01`)  
**Controlling issue:** `Yuren-Tang/research-workbench#68`  
**Fixed candidate:** `proof-development/affine-cdc-rigour-v1@1f57422e0e415d8902d56eb294183815c0a0b640`  
**Frozen Research Lead source:** `research/affine-cdc-five-cdc-v1@71a10f9ba86c1d2b8b7885e78fa9baa303c77818`  
**Read-only post-snapshot guide:** `proof-development/affine-cdc-rigour-v1@2679f098e6c596083d671a67d2630d5c58c6280f`  
**Owned branch:** `audit/affine-cdc-five-cdc-core-v1`  
**Branch base:** exactly `1f57422e0e415d8902d56eb294183815c0a0b640`

## 1. Audit boundary and method

This audit treats the six units required by issue #68 as ordinary mathematics. It does not infer correctness from completion labels, branch ancestry, the Research Lead narrative, the Proof Development Lead narrative, prior Lean work, Curator material, Paper A, or unreproduced computations.

The finite claims were independently recomputed from the definitions:

- roots are the ten two-subsets of `[5]` with addition by symmetric difference;
- conserved ordered four-boundaries are enumerated directly in `R_5^4`;
- route challenges are generated from all complementary support pairs and all three terminal matchings;
- root-triangle flips are enumerated from the thirty adjacent sides of the ten three-subsets of `[5]`;
- Petersen transitions and six-port matchings are enumerated independently from disjointness in `KG(5,2)`.

No candidate computation was used as an oracle. The exact algorithms and outputs are recorded in the finite-check ledger.

## 2. Unit verdicts

| Unit | Required subject | Verdict |
|---|---|---|
| A / R0 | five supports and root flow | `ACCEPT` |
| B / R1 | one-cross structural reduction | `ACCEPT` |
| C / R2.1 | finite boundary and route certificate | `ACCEPT` |
| D / R2.2 | equality/DDD Morse descent | `ACCEPT` |
| E / R2.3 | first failure and critical overlaps | `BLOCKED-PROOF` |
| F / R2.4 | full-state forced backbone | `BLOCKED-PROOF` |

The non-accepts are proof-interface failures, not discovered counterexamples to the underlying five-CDC statement.

## 3. Unit A — R0 five supports / root flow

### Verdict: `ACCEPT`

Let `(F_1,...,F_5)` be indexed vertex-even edge sets in a finite loopless cubic multigraph, with every edge contained in exactly two indexed supports. Assign to an edge in `F_i,F_j` the root `e_i+e_j`.

Coordinatewise vertex-evenness is exactly Kirchhoff conservation in

\[
E_5=\{x\in\mathbf F_2^5:\sum_i x_i=0\}.
\]

Conversely, a root-valued `E_5` flow recovers `F_i` by taking the edges whose `i`-th coordinate is one. Weight two gives exact edge multiplicity two, and conservation gives vertex-evenness in every coordinate. The constructions are mutually inverse edgewise.

At a cubic vertex, three roots sum to zero. If two were equal, the third would be zero, impossible. For two distinct roots `A,B`, the third is `A triangle B`; its weight is two exactly when `|A intersect B|=1`. Hence the three labels are precisely the three edges of one triangle on three support indices.

No distinctness or nonemptiness assumption on the five supports is used. Empty supports and equal support edge sets at different indices are compatible with the indexed formulation. Parallel source edges remain distinct edge objects.

## 4. Unit B — R1 one-cross reduction

### Verdict: `ACCEPT`

The proof in `AC_PD_5CDC_R1_ONE_CROSS_STRUCTURAL_REDUCTION.md` survives independent reconstruction.

Let `e=uv` be a simple edge, delete `u,v`, and label the four remaining incidences `a,b` at `u` and `c,d` at `v`. Every component of the exterior `H` contains at least two terminal incidences: a component with one terminal would make that terminal edge a bridge of the original graph. Therefore `H` is connected or has exactly two components with two terminals each.

In the disconnected case, either cross matching different from the component partition joins the two components by two new nonloop edges. Each new edge lies on a cycle using the other new edge. An old bridge inside one component is bypassed when the two terminals lie on opposite shores; if both terminals lie on one shore, the terminal-free shore would already make the edge a bridge of the original graph. Thus a joining cross is connected, loopless, and bridgeless.

In the connected case, an old edge can remain a bridge after closure only if its bridge cut separates the four terminals exactly into the two blocks of that closure matching. Bridge cuts in one graph are compatible, whereas the two cross partitions `ac|bd` and `ad|bc` cross in all four intersections. Hence at most one cross closure has an old bridge.

The two cross closures cannot both contain loops: one loop in each forces three terminal incidences to share one exterior cubic vertex, making the fourth terminal edge the unique edge leaving `{u,v,x}` and hence a bridge. If one cross has a loop, the opposite matching separates the two coincident incidences and therefore cannot be induced by an old bridge cut. Thus one cross is simultaneously connected, loopless, and bridgeless.

Finally, a connected loopless cubic multigraph with no simple edge has only one neighbour at every vertex; degree three then forces exactly two vertices joined by three parallel edges. This is the theta base.

## 5. Unit C — R2.1 boundary and route certificate

### Verdict: `ACCEPT`

Independent exhaustion gives exactly `640` ordered conserved root quadruples. Their routing-weight triples and ordered-word counts are:

| State | `(omega_0,omega_1,omega_2)` | Count |
|---|---:|---:|
| `A` | `(0,0,0)` | 10 |
| `B_0,B_1,B_2` | permutations of `(0,1,1)` | 60 each |
| `C_0,C_1,C_2` | permutations of `(0,2,2)` | 30 each |
| `D_0,D_1,D_2` | permutations of `(2,1,1)` | 120 each |

Direct reconnection at matching `M_i` has profile

\[
J_i=\{A,B_i,C_i\}.
\]

The two-vertex cap at `M_i` has profile

\[
K_i=\{B_j,B_k,D_j,D_k\},\qquad \{i,j,k\}=\{0,1,2\},
\]

and therefore `J_j intersect K_i={B_j}` for `j != i`.

All `1680` labelled complementary-support challenges collapse to exactly sixteen support-unordered route rows, matching the candidate table. For each fixed route, the undirected transition graph is

\[
P_3\;sqcup\;C_4\;sqcup\;P_3.
\]

For an original cap route `M_i`, every equality row in `J_i` and every relevant DDD row outside `K_i` has exactly one route target outside `K_i`, namely `M_i`. The certificate is only conditional on the physically realised terminal matching. It does not itself prove that a desired interior route exists; the candidate states this boundary correctly.

## 6. Unit D — R2.2 Morse descent

### Verdict: `ACCEPT`

The thirty unordered adjacent root-triangle sides were independently enumerated.

For the equality potential, the primary `nu` change has the exact split

\[
9\text{ decreasing},\quad12\text{ neutral},\quad9\text{ increasing}.
\]

On the twelve neutral sides, the secondary `phi` contribution has six decreasing and six increasing cases, with no tie. Whenever the primary contribution decreases, the secondary contribution does not increase. The displayed positive scalar weight therefore gives fifteen decreasing and fifteen increasing flips, with no tie.

The candidate's complete equality nondecreasing-side table is exact. Assuming no equal adjacent pair and no decreasing flip, its elimination argument removes all ten triangle types; boundary occurrences are used only for root `12`, exactly as required. Hence no nonempty equality local minimum exists.

For DDD boundary `12,12,34,34`, the displayed positive weight independently gives fifteen decreasing and fifteen increasing flips, with no tie. The candidate's DDD nondecreasing-side table is exact. Empty nonboundary rows `25` and `45`, followed by the `23`, `35`, `13`, `14`, and `24` restrictions, eliminate every triangle type. Hence no nonempty DDD local minimum exists.

Every chosen root `2--2` move remains connected; its nonzero root flow forbids a bridge. An equal-face cancellation is a declared strict-order/recursive exit rather than a move that must remain in the same loopless category. No positive local terminal is omitted from the stated current-flow termination theorem.

## 7. Unit E — R2.3 first failure / critical overlaps

### Verdict: `BLOCKED-PROOF`

### 7.1 Independently accepted subclaims

The one-edge first-failure statement is correct. At the first failed inverse step every pre-existing edge keeps its root value; the restored central value is the sum of two roots and therefore has weight `0`, `2`, or `4`. Failure is exactly zero or one co-root.

For inverse `2--2` failure:

- zero gives boundary `a,a,b,b`; because the current crossed topology is root-valued, `a,b` are distinct intersecting roots, and the other crossed topology is root-valued as well;
- co-root gives two distinct perfect matchings of the four-set complementary to one missing support index, hence one standard nondegenerate co-root atom with two crossed root resolutions.

Quadruple equality cannot occur in the inverse-flip row. It occurs exactly in inverse cancellation with equal reconnected roots; all three pairings then have central value zero. The candidate correctly isolates this as a separate recursive/contextual branch rather than falsely rootifying it locally.

For a standard co-root atom `Q_i` meeting a root surgery, the displayed dichotomy is correct. If the far triangle roots both avoid `i`, the token relocates through root alternatives. If both contain `i`, the unique bad overlap produces the transport state `(Q_i,Q_j,ij)`. At the resulting co-root cherry, exactly one of the two candidate NNIs is root-valued, according as the cherry root avoids or contains `j`; the transient two-token tree reduces to at most one token. The bridge-zero argument proves category safety for persistent nonzero root/co-root states.

### 7.2 Exact blocking defect E-MI-1

The candidate does not prove the normalization of the inverse-cancellation **doubled-disjoint / missing-index row** into the standard one-atom alphabet.

Take

\[
p=12,\qquad q=34,\qquad Q_5=p+q=1234.
\]

A failed inverse equal-face insertion with reconnected roots `p,q` has the raw two-vertex boundary

\[
(12,34\mid12,34)
\]

and central co-root `Q_5`. Its three terminal pairings have central values

\[
Q_5,\quad0,\quad Q_5.
\]

Thus it is the degenerate atom with equal endpoint matchings, not the standard nondegenerate Petersen-edge atom used by R2.4. It has no immediate root-valued crossed resolution.

`AC_PD_5CDC_R2_3_FIRST_FAILURE_AND_LOCAL_CONFLUENCE.md` proves critical-overlap normalization only after a standard atom is already adjacent to an ordinary root move. It contains no lemma that starts from the displayed degenerate insertion, handles the bounded theta/parallel-edge cases, selects a legal borrow, and returns either a root state, an accepted exit, or one standard atom while preserving ordered darts, cap block, route, and support data.

The downstream files assume this missing result:

- R2.4 excludes “doubled-disjoint raw insertions” from its state vertices;
- R2.6 repeats the same exclusion;
- the later fixed-order compatibility file states a “doubled-disjoint borrowing dichotomy” but gives no source-level construction or exact dependency proving it.

### 7.3 Required repair

Add a standalone bounded normalization lemma for the raw word `(p,q|p,q)` with `p perpendicular q`. It must include:

1. the exact graph cases when the borrow edge returns to the other atom vertex, including the theta/bounded terminal;
2. the ordinary-root far-vertex cases;
3. the good-borrow and missing-index two-co-root movies;
4. literal maps on every source vertex, edge, ordered dart, boundary root, cap block, route, and support transport;
5. a proof that the output is root-valued, accepted, or one **nondegenerate** standard atom.

Until that lemma exists, the persistent-state alphabet is not exhaustive.

## 8. Unit F — R2.4 full-state forced backbone

### Verdict: `BLOCKED-PROOF`

### 8.1 Independently accepted finite/coefficient claims

For a nondegenerate atom, the two endpoint matchings are distinct perfect matchings of the four-set complementary to one missing index. The omitted third matching consists of two disjoint roots `s,t`; these are exactly the two root-valued crossed resolutions. Hence standard atoms are canonically Petersen edges.

A constant-pivot transition

\[
\{s,x\}\longrightarrow\{s,y\}
\]

has side root `z=x+y`, and the unique root-admissible simultaneous choice is the pair of nonpivot endpoints `x,y`. All sixty ordered constant-pivot transitions satisfy this.

For every ordered nonbacktracking four-pivot word

\[
x-s-t-y,
\]

there are side roots `z=x+t` and `w=s+y`, with `z != w` and `|z intersect w|=1`. All `120` cases satisfy this. In the associated six-port table, four of the six left-right matchings are root-valued star completions and exactly two are non-root; the two non-root matchings are exactly those containing the disjoint pair `s--t`.

These finite statements do not by themselves prove the full-state source theorem.

### 8.2 Exact blocking defect F-SOURCE-1 — star table to physical route

Normalize one genuine change cell to

\[
s=12,\quad t=34,\quad x=35,\quad y=15,
\]

so

\[
z=45,\quad w=25.
\]

The six ports are

\[
(12,35,45\mid25,34,15).
\]

The two forbidden matchings are

\[
12-34,\ 35-25,\ 45-15
\]

and

\[
12-34,\ 35-15,\ 45-25.
\]

The other four are coefficient-valid root stars. R2.4 then asserts that a composition-compatible star gives a replacement, otherwise a route/separator/category exit occurs, and otherwise every compatible matching contains `12--34`.

What is missing is the graph theorem connecting **physical source composition** to this six-element matching table. No complete definition of “composition-compatible” is followed by a proof that exclusion of the four root stars forces precisely a route change or one of the declared exits. The coefficient table classifies possible labels; it does not classify which matching is realised by the exterior source components.

### 8.3 Exact blocking defect F-SHEET-1 — no independent route bit

R2.4 states that the two residual pairings are transported canonically and therefore one initial crossed sheet determines the entire forced chain. The unordered Petersen-edge transport is clear. The required ordered statement is stronger: the physical cap-oriented route sheet, ordered terminal blocks, and dart incidences must be shown to transport without an independent local flip at each consecutive cell.

No explicit transition map on ordered sheets is given, and no cocycle/monodromy calculation proves that its composition agrees with the retained cap orientation. Consequently the assertion “there is not an independent binary choice at each cell” is not independently established at full-state level.

### 8.4 Exact blocking defect F-BIGON-1 — source-faithful backtrack filling

For the minimal immediate backtrack

\[
12\longrightarrow34\longrightarrow12,
\]

R2.4 gives the coefficient shore word

\[
(34,12,12,34)
\]

and then invokes an unspecified “local involution/square/pentagon lift” together with a “canonical disjoint-doubled root square”. No exact source file, theorem statement, finite move sequence, or ordered-boundary gluing map is identified in the R2.4 dossier.

The coefficient `abba` identity is explicitly insufficient. Without the actual labelled two-cell movie, the claimed bigon replacement has not been checked for source topology, ordered darts, side roots, cap block, route, support transport, or marks. Therefore Theorem 6.1 (“no backtrack in a minimal lift”) is not presently an ordinary-mathematics proof.

### 8.5 Complete-data preservation

The file repeatedly says that side roots and source attachments are retained, but the needed boundary maps are not written. This is consequential, not cosmetic: R2.6 and R2.7 consume literal complete-state seam equality, not merely equality of root coefficients.

### 8.6 Required repair

R2.4 needs one source-level dossier containing:

1. a precise full-state cell object with ordered darts and route sheets;
2. the complete critical-overlap table as source movies, not only coefficient alternatives;
3. the six-port composition theorem proving the star/route/separator trichotomy;
4. the ordered-sheet transition map and proof of global route-bit uniqueness;
5. an explicit labelled bigon filling for `s-t-s` with every intermediate source graph and root assignment;
6. literal boundary-identification lemmas for side roots, cap block, route, support transport, and marks.

## 9. Final return

\[
\boxed{\texttt{MATERIAL CORE GAP — NO 5-CDC ACCEPTANCE}}
\]

Units A–D are independently accepted. Unit E omits a load-bearing first-failure normalization case, and Unit F does not yet bridge its verified finite coefficient geometry to the complete physical source theorem required by downstream track erasure and contextual return.

No counterexample to the five-CDC conjecture or to the accepted A–D mathematics was found. The result of this audit creates no Lean, Curator, manuscript, release, DOI, or publication status.
