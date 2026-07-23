# Five-CDC proof mechanism and compressed architecture

## Research Lead synthesis v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `dfcb64fb06cb3531aa25c533f5ad840628a91033`.  
**Controlling endpoint consumed:** `FIVE_SUPPORT_GLOBAL_MINIMAL_COUNTEREXAMPLE_REPAIRED_V2.md`.

**Purpose:** extract the mathematical mechanism of the repaired five-support candidate, separate indispensable proof obligations from discovery-era machinery, and provide a compressed architecture suitable for Proof Development Lead reconstruction and independent audit.

**Status:** authorial mechanism synthesis. This document does not add assurance to the candidate proof. It states what the current proof is really doing, which modules appear logically essential, which are presently auxiliary, and where a genuine conceptual simplification may replace a large technical packet.

---

## 1. What would count as a proof existing?

The current branch contains a complete authorial proof candidate: every arrow needed by the controlling global dossier has a named proposed theorem and no known scope correction is silently ignored.

That is not yet the same as an established proof.

A five-CDC proof may responsibly be said to exist only after a complete rigorous reconstruction verifies that:

1. every load-bearing statement is correctly formulated with the required quantifiers;
2. every invocation satisfies the hypotheses of the invoked theorem;
3. every finite classification has a reproducible certificate or a human proof;
4. the nested descent is genuinely well founded and noncircular;
5. the contextual-return theorem acts on the complete labelled source state, not merely on coefficient data;
6. no correction or exceptional graph category has been omitted.

Proof development is therefore not clerical formatting. It is the stage that determines whether the authorial candidate really expands into a proof. If reconstruction succeeds and independent attempts to break it find no fatal omission, then the mathematical proof exists even before Lean formalisation or publication.

---

## 2. The theorem in its natural language

Put

\[
E_5=\left\{x\in\mathbf F_2^5:\sum_i x_i=0\right\}
\]

and let

\[
R_5=\{e_i+e_j:i<j\}
\]

be the ten weight-two roots.

A five-support cycle double cover is exactly a flow

\[
\lambda:E(G)\to R_5
\]

satisfying Kirchhoff conservation at every cubic vertex.

Equivalently:

- roots are the edges of `K_5`;
- the three labels at every cubic source vertex are the three edges of one triangle of `K_5`.

Thus the problem is not fundamentally about five separately drawn cycles. It is:

> label every edge of a bridgeless cubic graph by an edge of `K_5` so that every source vertex maps to a triangle of `K_5`.

This root-flow language should be the main proof language. Support sets are recovered coordinatewise only at the beginning and end.

---

## 3. The entire proof in six moves

The repaired candidate can be compressed to six conceptual moves.

### Move I — reduce to a highly connected cubic counterexample

Assume a vertex-minimal connected bridgeless cubic counterexample `G`.

Exact two-, three-, and four-cut completion and gluing remove all proper small cyclic cuts. Acyclic shores of size at most four are explicit bounded gadgets.

The result is a minimal counterexample in which every local two-vertex deletion has no unresolved low-cut escape.

### Move II — delete one arbitrary edge and solve all three reconnections

Delete the endpoints of an arbitrary edge. The complement is an ordered four-pole `P_0` with three terminal matchings

\[
M_i,M_j,M_k.
\]

Closing `P_0` by each zero-vertex matching gives three graphs with two fewer vertices. The simultaneous reconnection theorem says that, after the small-cut reductions, all three are connected bridgeless cubic graphs. Minimality gives a root flow on each.

Therefore the boundary profile of `P_0` meets all three direct-reconnection sets

\[
J_i,J_j,J_k.
\]

### Move III — finite boundary rigidity forces one route

The original deleted edge is a two-vertex cap with profile `K_i`.

If `P_0` already has a boundary state in `K_i`, the cap glues and the proof ends.

Assume it does not. The complete ten-state boundary transition graph then forces

\[
\Sigma(P_0)=J_i
\quad\text{or}\quad
\Sigma(P_0)=J_i\cup L_i,
\]

and every admissible Kempe challenge uses the same physical terminal matching `M_i`.

This finite theorem is the boundary-combinatorial heart of the proof:

\[
\boxed{
\text{three smaller reconnections}
+
\text{blocked original cap}
\Longrightarrow
\text{one globally fixed route}.}
\]

### Move IV — one attempted cap insertion creates at most one singular edge

Take a root flow on one cross reconnection and formally restore the original cap. If the two reconnection roots are `p,q`, the new central value is

\[
p+q.
\]

There are only three possibilities:

1. `p,q` intersect: `p+q` is a root and the cap lifts;
2. `p=q`: the new edge is zero;
3. `p,q` are disjoint: the new edge is a co-root.

Hence every obstruction is one singular edge, of exactly two species:

\[
0
\quad\text{or}\quad
Q_i.
\]

There is no larger local alphabet.

### Move V — a single singular edge cannot remain trapped

Kempe switches are horizontal augmentations. If a repair component separates the two marked incidences, the singular edge becomes a root and the cap lifts.

If every repair channel is locked, root Pachner moves and equal-face cancellations produce a finite reduction history. An arbitrary root flow on the terminal graph is then transported backwards. Its first failure is again exactly one zero/co-root edge.

The defect behaves as one token:

- zero is immediately rootified;
- a co-root token moves through bounded critical overlaps without branching;
- constant-pivot stretches possess a unique root-valued nonpivot section;
- a recurrent token yields a closed Petersen-state core;
- odd cores reverse the oriented resolution sheet and cannot close;
- the primitive even `C6` core is one root NNI away from a canonical star containing an equal-face dipole;
- `C8` decomposes into two seam-compatible `C6` cells.

Thus every same-order recurrence either disappears or forces a genuine cancellation. Cancellation lowers the target order by two. Contextual return is therefore well founded.

### Move VI — glue the original cap and restore general graphs

The terminal cap-compatible state returns to `P_0`, producing

\[
\Sigma(P_0)\cap K_i\ne\varnothing.
\]

The original cap glues, contradicting minimality.

Finally, componentwise assembly and port-cycle expansion/collapse pass from loopless cubic multigraphs to all finite bridgeless multigraphs while retaining exactly five indexed supports.

---

## 4. The single local algebra behind the proof

Many dossiers appear to use different local gadgets. They are manifestations of one four-branch triality.

Let four branch values satisfy

\[
A+B+C+D=0.
\]

The three binary resolutions have central values

\[
A+B,
\qquad
A+C,
\qquad
A+D,
\]

whose sum is zero.

For root branches, their weights have only the patterns

\[
(0,0,0),
\quad
(0,2,2),
\quad
(0,4,4),
\quad
(2,2,4).
\]

The proof uses only the following consequence:

> if one resolution is root-valued, exactly one alternative is root-valued; the third is zero or co-root.

This one fact simultaneously explains:

- root-preserving NNI;
- inverse-dipole insertion;
- equality atoms;
- DDD atoms;
- the two crossed resolutions of a co-root;
- zero-to-theta resolution;
- the canonical relative `C6` star movie.

The local algebra should therefore be presented once as the **root triality theorem**. Equality and DDD are the two singular fibres of the same triality, not two unrelated theories.

---

## 5. The single global mechanism: termination plus singular confluence

The deepest part of the proof is best understood as a rewriting theorem.

### Objects

An object is an ordered root-labelled four-pole together with its complete exterior boundary and route data.

### Regular moves

- root-valued `2-2` Pachner NNI;
- equal-face `2-0` cancellation.

### Singular fibres

When an inverse move fails, it creates one edge labelled

\[
0
\quad\text{or}\quad
Q_i.
\]

### Termination

The equality and DDD potentials prove that forward regular reduction cannot continue indefinitely. Their detailed formulas may remain separate in the proof, but logically they serve one role:

\[
\boxed{
\text{the root-surgery rewrite system terminates}.}
\]

### Local singular confluence

Disjoint moves commute. Every overlapping critical pair transports at most one singular token. The token never branches into an unbounded defect cloud.

### Global singular confluence

A trapped token would determine a recurrent walk in a finite enriched state graph. The Petersen graph is not an additional mysterious method: it is exactly the state graph of co-root resolutions, because co-root states are disjoint pairs of `K_5` roots.

The cycle analysis proves:

- odd monodromy cannot preserve the oriented cap sheet;
- even monodromy contains an explicit cancellable root movie.

Hence no nonterminal recurrent class exists.

This suggests the conceptual master theorem:

### Proposed master theorem — defect-confluence criterion

Let a terminating root-triality rewrite system have:

1. one-edge first-failure localisation;
2. bounded, nonbranching critical-pair transport;
3. canonical resolution of constant-pivot runs;
4. no admissible odd token holonomy;
5. a strict cancellation on every even identity-return core.

Then every cap-compatible terminal root state transfers to the original context.

If formulated and proved cleanly, this theorem can replace the appearance that the proof needs an independent global Ptolemy theory, Petersen theory, equality theory, and DDD theory. Those become verification of its five hypotheses.

---

## 6. What each technical language is really doing

### `K_5` roots / `E_5` flow

This is the intrinsic statement language.

### Ten-state four-pole profile

This is the finite boundary quotient. It records only the information visible to a two-vertex cap and its three terminal matchings.

### Kempe components

These are augmenting paths. A separating component directly repairs the singular cap insertion; a full lock is the analogue of an augmenting system with no exposed endpoint.

### Equality and DDD potentials

These prove termination of two singular boundary fibres. They need not define two separate global proof architectures.

### Triangle pseudocomplex and Pachner moves

This is the source-level rewrite system. It keeps graph topology, root labels, and local triality in one object.

### Ptolemy histories

These compare two reduction histories. Their essential role is confluence bookkeeping, not a second geometric theorem about the original graph.

### Petersen graph

Its vertices are roots and its edges are disjoint root pairs. Therefore a co-root atom is a Petersen edge, and movement of the atom is a walk in the line graph of the Petersen graph. Petersen cycles classify possible defect monodromy.

### Relative `C6` star movie

This is the primitive even confluence 2-cell. It replaces the invalid abstract-tube argument by an actual source-level NNI followed by cancellation.

### Bridge-zero law

This removes most category bookkeeping after a move becomes root-valued: a bridge in a group-valued flow has value zero, whereas every root is nonzero.

---

## 7. The compressed theorem spine

The candidate should eventually be reconstructed around five principal theorems.

### Theorem A — root-flow equivalence and local triality

1. five indexed even supports are equivalent to an `R_5`-valued flow;
2. cubic vertices are `K_5` triangles;
3. every four-branch triality is root/root/singular.

### Theorem B — minimal-counterexample reduction and three reconnections

1. exact low-cut completion and gluing;
2. after low-cut reduction, all three reconnections of any deleted edge are smaller connected bridgeless cubic inputs.

### Theorem C — finite boundary rigidity

If one four-pole profile meets all three `J_r` but misses `K_i`, then it is `J_i` or `J_i\cup L_i`, and every physical challenge uses route `M_i`.

This theorem should be displayed by one labelled ten-state diagram rather than distributed across repeated tables.

### Theorem D — one-defect normalisation / contextual confluence

In a fixed-route cap lock, every equality or DDD singular insertion either:

1. is horizontally repaired;
2. produces a cap-compatible route/theta terminal;
3. or enters a terminating surgery history whose first-failure token cannot recur and therefore forces strict cancellation.

Consequently every terminal state returns and the original cap lifts.

### Theorem E — outer shell

The cubic theorem extends componentwise and through port-cycle expansion/collapse to all finite bridgeless multigraphs while preserving five indexed supports.

Everything else should be a lemma, finite certificate, or appendix supporting A--E.

---

## 8. Simplifications that appear safe now

### 8.1 Merge equality and DDD at the architectural level

Their boundary words and local potentials differ, so a rigorous proof may still need two termination sublemmas. But they should enter and leave one common theorem:

\[
\boxed{
\text{one singular triality fibre}
\Longrightarrow
\text{one fixed-route normalisation problem}.}
\]

There is no reason for the final exposition to carry two parallel global narratives.

### 8.2 Replace abstract tube language by the primitive confluence cell

The old longitudinal `C6/C8` tube equations remain valid algebraic certificates, but they are not the source-level proof.

The controlling source statement is now:

\[
\text{fixed rooted branches}
\longrightarrow
\text{one relative root NNI}
\longrightarrow
\text{canonical star}
\longrightarrow
\text{equal-face cancellation}.
\]

The tube dossiers should be demoted to discovery history or algebraic motivation.

### 8.3 Package category safety once

After a state is root-valued, use the bridge-zero law globally. Do not repeat separate bridge analyses for every root NNI, star, and cancellation.

Only the graph-only all-three-reconnection theorem needs an independent category analysis before a root flow is known.

### 8.4 Replace repeated finite tables by one boundary graph

For a fixed route `M_i`, the ten-state graph is

\[
P_3\sqcup C_4\sqcup P_3,
\]

with outer paths `J_i,L_i` and middle cycle `K_i`.

Three-reconnection forcing plus avoidance of `K_i` immediately places the profile in the outer sector and fixes the route. This picture should replace many pages of state-by-state prose, while a certificate remains in an appendix.

### 8.5 Demote noncontrolling exploratory machinery

The current repaired global spine does not directly require the earlier:

- affine `A_3` translation chain;
- Type-X selector plane;
- flat-code and octahedral Stokes packages;
- reflection-supported `D_8` cohomology programme;
- abstract tube-to-history assertion;
- large side-signature exploration preceding the relative-star repair.

These files may contain useful independent structure and audit certificates, but they should not be presented as necessary stages of the current proof unless PDL discovers a hidden dependency.

### 8.6 Move the general-graph shell out of the main argument

The intellectual theorem is cubic. Componentwise assembly, port-cycle expansion, collapse, and loop reinsertion should be one final section or appendix.

---

## 9. Simplifications that remain conjectural

### 9.1 One universal potential

It may be possible to replace the equality potential `(E,\Phi,|V|)` and DDD potential `(\Omega,|V|)` by one potential on a compactified singular-triality complex containing both diagonal equality states and Petersen-edge DDD states.

This would be a real proof shortening, not merely exposition. It is not yet established and must not be assumed by PDL.

### 9.2 A direct single-defect augmentation theorem

The current proof eliminates one singular edge by surgery histories and contextual confluence. A stronger theorem might say directly:

> in a cyclically five-edge-connected cubic graph, a defect-minimal `E_5` flow cannot have exactly one zero or co-root edge.

Such a theorem would bypass most of full-channel transfer. No current proof of this direct statement is known. The existing machinery should be regarded as one constructive proof of it, not evidence that the bypass is already valid.

### 9.3 Abstract Newman-type packaging

Termination plus local confluence normally implies global confluence. Here the terminal root flow is arbitrary and inverse moves may enter singular fibres, so ordinary Newman's lemma does not apply verbatim.

A carefully formulated relational or singular version may compress the Ptolemy/history argument substantially. This is a promising conceptual target, but it requires a theorem whose objects include complete boundary profiles and labelled source histories.

---

## 10. What is genuinely irreducible at present

The following burdens cannot presently be dismissed as bookkeeping.

1. **All-three reconnection category theorem.** It is what turns one arbitrary deleted edge into three valid smaller inputs.
2. **Ten-state physical-profile rigidity.** Abstract coefficient closure is insufficient; the route must be physical.
3. **Termination of locked equality and DDD carriers.** Some well-founded measure is required.
4. **Cover-independent contextual return.** The smaller graph supplies an arbitrary root flow, not the flow used to create the reduction history.
5. **Full labelled critical-pair analysis.** Coefficient agreement alone does not imply a source movie.
6. **Even-core source realisation.** The relative `C6` movie and the seam-compatible `C8` reduction must be checked at every shared incidence.
7. **Nested noncircularity.** Same-order motion and lower-order recursion must not invoke one another circularly.

These are the proper audit targets.

---

## 11. Recommended Proof Development Lead handoff

PDL should not reconstruct the 200-plus-file discovery chronology. It should build a new theorem DAG around A--E.

### Package A — language and local algebra

- root-flow equivalence;
- triangle law;
- four-root triality;
- bridge-zero lemma.

### Package B — global graph reduction

- bounded bases;
- two-/three-/four-cut gluing;
- all-three arbitrary-edge reconnections.

### Package C — finite four-pole theorem

- ten boundary states;
- direct and cap profiles `J_i,K_i`;
- Kempe transition graph;
- fixed-route classification.

### Package D — singular normalisation

- horizontal repair;
- equality termination;
- DDD termination and absence of residual bounded carriers;
- first-failure one-edge localisation;
- critical-overlap nonbranching;
- constant-pivot root section;
- odd-cycle exclusion;
- relative `C6` cancellation;
- `C8`-to-two-`C6` reduction;
- route and theta terminal return;
- complete well-foundedness proof.

### Package E — closure and outer shell

- full-channel cap lift;
- arbitrary-edge contradiction;
- componentwise cubic extension;
- port-cycle expansion/collapse;
- loop reinsertion.

For every package PDL should supply:

1. theorem statement with exact graph category and boundary labels;
2. proof with no reliance on research-status prose;
3. dependency list containing only earlier packages;
4. finite certificate where applicable;
5. explicit edge cases for loops, parallel edges, disconnected outputs, and coincident terminals;
6. a statement of whether the theorem is human-proved, computed, or both.

---

## 12. Recommended exposition order

A readable paper should not follow the historical discovery order.

1. State five-CDC as an `A_4`/`K_5` root-flow theorem.
2. Prove the root triality lemma.
3. Introduce four-pole profiles and display the ten-state route graph.
4. Perform minimal-counterexample and all-three-reconnection reduction.
5. Derive the fixed-route lock in one finite theorem.
6. State the one-defect normalisation theorem abstractly.
7. Prove its termination and critical-pair hypotheses in separate subsections.
8. Deduce the cap lift and contradiction.
9. Add the general-graph outer shell.
10. Put finite enumerations, Petersen cycle census, and discovery-era alternative formulations in appendices.

The motivational sentence is:

> Three smaller reconnections force enough boundary states that a blocked cap has only one possible route; along that route every failed lift is one movable singular edge, and termination plus parity prevents that edge from returning without cancellation.

That is the proof in one sentence.

---

## 13. Research Lead next programme

The Research Lead should now work in the following order.

1. Draw and verify the single ten-state boundary graph used by Theorem C.
2. Formulate the defect-confluence master theorem independently of equality/DDD coordinates.
3. Map every current load-bearing dossier to one hypothesis of that theorem.
4. Test whether equality and DDD potentials admit a common compactified potential.
5. Search for a direct defect-minimal augmentation proof that bypasses contextual histories.
6. Produce a minimal authoritative dependency ledger and demote noncontrolling discovery files.
7. Hand the compressed A--E DAG to PDL and reserve AC-RL for conceptual simplification or responses to concrete reconstruction failures.

---

## 14. Assurance boundary

This synthesis claims:

- a compressed account of the current repaired candidate;
- identification of one local algebra and one global defect-confluence mechanism;
- a proposed five-theorem proof spine;
- a concrete separation between essential modules, auxiliary certificates, and conjectural simplifications.

It does not claim:

- that the PDL reconstruction will succeed;
- that a universal potential already exists;
- that ordinary Newman's lemma applies without modification;
- that the contextual history can presently be deleted from the proof;
- independent verification, Lean verification, curation, manuscript readiness, or established theorem status.
