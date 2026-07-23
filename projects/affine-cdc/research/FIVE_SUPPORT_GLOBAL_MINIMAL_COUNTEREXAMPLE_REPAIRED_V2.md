# Global five-support minimal-counterexample closure — repaired theorem

## Research dossier v2 — controlling authorial endpoint

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `ba6c7f090f8a5fbcad6f1e9d005e9c48ece92671`.

**Supersedes for controlling use:** `FIVE_SUPPORT_GLOBAL_MINIMAL_COUNTEREXAMPLE_CLOSURE_V1.md`.

**Load-bearing parents:**

- `five-support/root-flow-lifting.md`;
- `GLOBAL_SMALL_CUT_COMPLETION_AND_GLUING_V1.md`;
- `TYPE_T_PHYSICAL_COMMUTATION_ELIMINATION_V1.md`;
- `TYPE_H_PHYSICAL_COMMUTATION_ELIMINATION_V1.md`;
- `ARBITRARY_EDGE_THREE_RECONNECTION_CATEGORY_V1.md`;
- `GLOBAL_CAP_LIFT_INTERFACE_COMPATIBILITY_V1.md`;
- `ORIENTED_FULL_CHANNEL_LOCK_ELIMINATION_REPAIRED_V2.md`;
- `CONSTANT_PIVOT_FULL_STATE_CONTEXTUAL_CONSUMPTION_V1.md`;
- `GENERAL_BRIDGELESS_FIVE_CDC_OUTER_SHELL_V1.md`.

**Status:** complete repaired authorial candidate. Every finite connected loopless bridgeless cubic multigraph admits a root-valued `E_5` flow. Equivalently, it admits five indexed even supports covering every edge exactly twice. Componentwise assembly and the port-cycle expansion/collapse outer shell then give a five-cycle double cover for every finite bridgeless multigraph. The proof uses a vertex-minimal cubic counterexample, exact two-/three-/four-cut gluing, all-three arbitrary-edge reconnection, and the repaired full-channel cap-lift theorem. All known scope corrections affecting the main spine are consumed explicitly: constant-pivot runs are physically root-sectioned without discarding support holonomy; contextual target order drops only after genuine cancellation; global Ptolemy tracks are not reduced from local cells alone; even Petersen cores are not treated as four-poles; abstract longitudinal tube words are not treated as pointwise history lifts; and full-state short-cycle sectors are retained.

**Assurance boundary:** this is the completed Research Lead authorial candidate, not an accepted project theorem or established result. It has not passed PDL reconstruction, independent audit, curation, Lean verification, manuscript integration, release, arXiv, DOI, peer review, or publication.

---

## 1. Cubic root-flow statement

Put

\[
E_5=\left\{x\in\mathbf F_2^5:\sum_{i=1}^5x_i=0\right\}
\]

and

\[
R_5=\{e_i+e_j:1\le i<j\le5\}.
\]

### Theorem 1.1 — cubic five-support candidate

Let `G` be a finite connected loopless bridgeless cubic multigraph. Then there exists

\[
\boxed{\lambda:E(G)\to R_5}
\]

satisfying Kirchhoff conservation at every vertex.

Equivalently, there are five indexed even edge sets

\[
(F_1,F_2,F_3,F_4,F_5)
\]

such that every edge belongs to exactly two of them.

The equivalence is exact: the two indices containing one edge are its root label, and coordinatewise flow conservation is evenness of each support.

---

## 2. Minimal counterexample

Assume Theorem 1.1 false and choose a counterexample `G` with minimum vertex number.

Every smaller finite connected loopless bridgeless cubic multigraph has a root-valued flow.

A loop cannot occur in `G`: at a cubic loop vertex the unique nonloop incident edge is a bridge. Thus the loopless hypothesis is also automatic for a connected bridgeless cubic counterexample.

The theta multigraph has the explicit root triangle

\[
12,13,23.
\]

`K_4` has the same three roots on its three perfect-matching colour classes. These are the bounded bases.

---

## 3. Exact small-cut reductions

The unified cubic-shore degree formula says that a connected acyclic cubic shore with `k` boundary incidences and `n` vertices satisfies

\[
3n=2(n-1)+k,
\qquad
\boxed{n=k-2.}
\]

Hence for cuts of size at most four:

- no nonempty acyclic two-cut shore exists;
- an acyclic three-cut shore is one vertex;
- an acyclic four-cut shore is one two-vertex cap.

All other proper shores contain cycles, and their standard completions are connected, loopless, bridgeless, cubic, and strictly smaller.

### Two-edge cut

Complete each cyclic shore by one edge. Minimality gives root flows; an `S_5` support permutation aligns the two completion-edge roots. Delete the completion edges and glue.

### Three-edge cut

Complete each cyclic shore by one cubic vertex. The three boundary roots form one support triangle. A global support permutation aligns the two ordered boundary triangles and glues the shores.

### Four-edge cut

For a four-pole `P`, let

\[
\Sigma(P)\subseteq\mathcal S
\]

be the exact ten-state support-unordered profile. Two shores glue iff their profiles intersect.

Minimality of the three cap completions makes each proper shore profile meet all three cap sets. The finite disjoint-profile classification leaves only Type T and Type H mismatch kernels. Physical disjoint-support route invariance eliminates Type T; the physical BBD/DDD commutation theorem eliminates Type H. Hence the profiles intersect.

Therefore a minimal counterexample has no cyclic edge cut of size at most four and no bounded acyclic/parallel degeneration.

---

## 4. All three reconnections at an arbitrary edge

Choose any edge

\[
uv\in E(G).
\]

Delete `u,v`, exposing four ordered incidences

\[
a,b\mid c,d.
\]

Let `P_0=G-\{u,v\}` and form the three zero-vertex closures

\[
M_i=ab\mid cd,
\qquad
M_j=ac\mid bd,
\qquad
M_k=ad\mid bc.
\]

The simultaneous reconnection theorem gives exactly:

1. all three closures are connected loopless bridgeless cubic multigraphs with two fewer vertices; or
2. `G` has a cyclic cut of size at most four; or
3. `G` lies in a bounded loop/parallel/acyclic degeneration.

Sections 2--3 exclude the last two alternatives. Hence all three closures are smaller valid inputs and have root-valued flows by minimality.

Restricting those flows to `P_0` gives

\[
\boxed{
\Sigma(P_0)\cap J_r\ne\varnothing
\qquad(r=i,j,k),}
\]

where

\[
J_r=\{A,B_r,C_r\}
\]

is the direct-reconnection profile.

---

## 5. The original cap

The deleted vertices and edge form the original two-vertex cap `cap_i`. Its exact profile is

\[
K_i=\{B_r,D_r:r\ne i\}.
\]

The repaired full-channel theorem applies to `P_0` because all three reconnection closures are smaller soluble inputs. It gives

\[
\boxed{
\Sigma(P_0)\cap K_i\ne\varnothing.}
\]

Choose one common support-unordered state realised by `P_0` and `cap_i`. A single global permutation of the five support indices aligns all five labelled boundary traces, not merely the state name. Glue coordinatewise.

The result is a root-valued flow on the original graph `G`, contradicting minimality.

Therefore no cubic minimal counterexample exists.

---

## 6. What the repaired full-channel theorem actually uses

For clarity, its controlling order is:

1. three-reconnection profile forcing;
2. blocked-cap classification to `J_i` or `J_i union L_i` and one fixed physical route `M_i`;
3. root/equality/DDD cap trichotomy;
4. immediate horizontal Kempe rescue where available;
5. terminating equality or DDD current-flow descent on one reconnection closure;
6. route-changing descendant states treated as `K_i` terminals and returned contextually;
7. all zero-vertex direct matchings converted to cap-compatible theta terminals, including the same-matching bridge via one zero-to-root NNI;
8. first failure in reverse transfer localised to one zero/co-root atom;
9. zero atoms immediately rootified;
10. constant-pivot runs resolved by their unique physical nonpivot root section, retaining all support transport and side attachments;
11. recurrent pivot-change tracks reduced to simple Petersen cycles;
12. odd `C5,C9` excluded by oriented resolution parity;
13. even `C6` consumed by a relative `(0,2,2)` NNI to a canonical star and equal-face cancellation;
14. `C8` reduced to two seam-compatible `C6` cells;
15. genuine cancellation lowers cap-target order by two.

No step treats an abstract coefficient filling as an automatically realised history movie.

---

## 7. Full-state and category safeguards

### Full-state safeguard

A collapsed pivot skeleton does not determine support holonomy. Accordingly:

- closed constant-pivot star triangles are physically root-sectioned, not declared support-trivial;
- star-expanded pentagons retain their reflection monodromy but reduce to an odd pivot core and cannot close the oriented resolution sheet;
- even pivot cores keep all resolved constant-run carriers as fixed rooted attachments during the relative star movie.

### Category safeguard

Once a local output is root-valued, every edge is nonzero. A bridge in a group-valued flow must carry zero. Hence:

- root Pachner NNI is automatically connected and bridgeless;
- equal-face cancellation gives componentwise bridgeless strict descent;
- co-root atom relocation and two-co-root normalization are also bridgeless because roots and co-roots are nonzero;
- zero atoms are rootified before persistent transport.

Thus no descendant category-return obligation is hidden inside the contextual move alphabet.

---

## 8. Noncircularity and well-foundedness

The proof uses three nested finite orders.

### Outer order

The number of vertices of a closed cubic graph. It supplies smaller root covers for:

- completed small-cut shores;
- all three arbitrary-edge reconnection closures;
- recursive cap contexts after a genuine cancellation.

### Forward equality/DDD orders

The equality potential is

\[
(E,\Phi,|V|),
\]

and the DDD potential is

\[
(\Omega,|V|).
\]

Root NNI strictly lowers the same-order part; cancellation lowers vertex order. No positive-vertex DDD bounded residual survives.

### Same-order contextual order

At fixed target order the contextual state graph is finite. It has no nonterminal sink:

- constant-pivot components rootify;
- immediate backtracks cancel;
- odd pivot cycles cannot return;
- even pivot cycles force cancellation.

A cancellation enters the strictly lower outer order. Hence nested contextual transfer is well founded.

The full-channel theorem never assumes the cubic conclusion on a same-order graph.

---

## 9. Componentwise cubic extension

The connected theorem extends to every finite loopless bridgeless cubic multigraph by applying it to each connected component and uniting equal-index supports across components.

The same global index set

\[
\{1,2,3,4,5\}
\]

is used for every component, so the result still has exactly five family members.

---

## 10. General finite bridgeless multigraphs

Let `X` be any finite bridgeless multigraph; parallel edges and loops are allowed.

1. Delete loops, obtaining a finite loopless graph `X_0` with no singleton cut.
2. Perform the port-cycle expansion. This gives a finite loopless bridgeless cubic multigraph `H` and edge lift
   \[
   \lambda:E(X_0)\hookrightarrow E(H).
   \]
3. Apply the cubic theorem componentwise to obtain exactly five vertex-even supports on `H`.
4. Since `H` is loopless, these supports are cut-even.
5. Project each of the same five supports memberwise through `lambda`. Cut parity and exact double coverage are preserved.
6. Add every deleted loop to two fixed support members, say `F_1,F_2`. Loops cross no cut, so parity remains valid and every loop is covered exactly twice.

### Theorem 10.1 — full finite 5-CDC candidate

Every finite bridgeless multigraph has five even subgraphs

\[
\boxed{F_1,F_2,F_3,F_4,F_5}
\]

such that every edge belongs to exactly two of them.

Equivalently, every finite bridgeless multigraph has a `5`-cycle double cover in the standard even-subgraph sense.

---

## 11. Supersession and authority

### Do not use as direct controlling conclusions

- the unconditional global-history conclusions of the original local Ptolemy dossier;
- the direct four-pole-potential treatment of even Petersen cores;
- the pointwise history interpretation of abstract longitudinal tube roots;
- the original immediate route-lift sentence on a surgery descendant;
- the original same-matching bridge/category terminal sentence;
- any claim that collapsing constant-pivot runs preserves full support monodromy.

### Use instead

- `CONTEXTUAL_TRANSFER_REPAIRED_AUTHORITY_V2.md`;
- `CONSTANT_PIVOT_FULL_STATE_CONTEXTUAL_CONSUMPTION_V1.md`;
- `PETERSEN_C6_RELATIVE_STAR_MOVIE_DESCENT_V1.md`;
- `PETERSEN_C6_AUTOMATIC_CATEGORY_SAFETY_V1.md`;
- `FIRST_FAILURE_NORMALIZATION_AUTOMATIC_CATEGORY_SAFETY_V1.md`;
- `ROUTE_CHANGE_TERMINAL_CONTEXTUAL_TRANSFER_V1.md`;
- `DIRECT_PAIRING_BRIDGE_TO_THETA_ZERO_RESOLUTION_V1.md`;
- `ORIENTED_FULL_CHANNEL_LOCK_ELIMINATION_REPAIRED_V2.md`;
- the present global dossier.

---

## 12. Current authorial status

### Claimed on this research branch

- one complete repaired candidate proof for finite connected loopless bridgeless cubic multigraphs;
- exact extension to disconnected cubic multigraphs;
- exact support-count-preserving outer shell to all finite bridgeless multigraphs;
- a correction-aware dependency spine with no presently declared mathematical branch left open inside this architecture.

### Not claimed

- acceptance by the project Director or PORT-DIR;
- proof-development reconstruction;
- independent mathematical verification;
- curated canonical status;
- Lean formalisation;
- manuscript-quality exposition;
- peer review;
- release, arXiv, DOI, or publication;
- established theorem status in the mathematical literature.

The next downstream assurance stages remain outside the Research Lead role. Within AC-RL, remaining work is authorial consolidation, expansion of terse imported lemmas, and response to any concrete defect returned by receivers.
