# The arbitrary-edge reconnection hypotheses match the full-channel cap-lift theorem exactly

## Research dossier v1 — authorial interface hardening

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `ebc4713a69bdffcc6e9e42d64449e120f77a6309`.

**Parents:**

- `ARBITRARY_EDGE_THREE_RECONNECTION_CATEGORY_V1.md`;
- `THREE_RECONNECTION_FIXED_ROUTE_REDUCTION_V1.md`;
- `ORIENTED_FULL_CHANNEL_LOCK_ELIMINATION_SYNTHESIS_V1.md`;
- `FOUR_POLE_CAP_LIBRARY_TEN_STATE_PROFILES_V1.md`;
- `five-support/cuts-four-poles-and-routing.md`;
- `FIVE_SUPPORT_GLOBAL_MINIMAL_COUNTEREXAMPLE_CLOSURE_V1.md`.

**Status:** exact compatibility theorem for the final global interface. Deleting the endpoints of one edge of a prime minimal counterexample produces one ordered four-pole `P` whose three zero-vertex reconnection closures give precisely the three profile-intersection hypotheses `Sigma(P) cap J_r != empty` required by the full-channel theorem. The original deleted two-vertex neighbourhood is precisely the cap of the direct shore matching, with profile `K_i`. A common support-unordered state in `Sigma(P) cap K_i` canonically permits a support permutation aligning the complete five labelled boundary traces, hence a root-valued gluing back to the original graph. No cap-forcing or global theorem is invoked at the original graph order.

**Not implied:** independent verification of the imported full-channel theorem, canonical acceptance, Lean verification, manuscript integration, release, publication, or DOI status.

---

## 1. The ordered arbitrary-edge interface

Let `G` be a connected bridgeless cubic loopless multigraph in the prime branch after the established cut and bounded-degeneration reductions. Choose an edge

\[
uv\in E(G).
\]

Let the other two incidences at `u` be

\[
a,b
\]

and the other two incidences at `v` be

\[
c,d.
\]

Delete `u`, `v`, and their incident edges, retaining the four exposed semiedges in the fixed order

\[
\boxed{a,b\mid c,d.}
\]

Call the resulting ordered cubic four-pole

\[
P=G-\{u,v\}.
\]

There are three perfect matchings of these four terminals. Write

\[
M_i=ab\mid cd,
\qquad
M_j=ac\mid bd,
\qquad
M_k=ad\mid bc.
\]

The distinguished matching `M_i` is not chosen after the fact: it is the partition of the four external incidences by the two deleted vertices.

---

## 2. Zero-vertex reconnections and the original cap

For each

\[
r\in\{i,j,k\},
\]

let `E_r` be the zero-vertex reconnection consisting of two independent edges joining the two terminal pairs of `M_r`, and put

\[
G_r=P\cup E_r.
\]

The original deleted neighbourhood is a different gadget. Let `cap_i` be the two-vertex cubic cap whose terminal blocks are `ab` and `cd`, with one central edge joining its two vertices. Then

\[
\boxed{G=P\cup cap_i.}
\]

Thus the final inverse step compares:

- three **smaller zero-vertex closures** `G_i,G_j,G_k`;
- one **same-order original cap closure** `P cup cap_i=G`.

This distinction is essential for noncircularity.

---

## 3. Exact category output

The simultaneous arbitrary-edge category theorem gives the following alternative.

1. All three `G_r` are connected bridgeless cubic multigraphs with
   \[
   |V(G_r)|=|V(G)|-2;
   \]
2. `G` has a cyclic cut of size at most four;
3. `G` lies in a bounded loop, parallel-edge, triangle, theta, acyclic, or low-port degeneration.

In the prime minimal-counterexample branch, alternatives 2 and 3 have already been discharged. Therefore every `G_r` is a smaller valid inductive input and has a root-valued `E_5` flow.

### Theorem 3.1 — simultaneous soluble reconnections

For the one ordered four-pole `P` determined by `uv`, all three zero-vertex closures are smaller soluble inputs.

No change of terminal ordering, shore matching, or four-pole convention occurs between the category theorem and the cap-lift theorem.

---

## 4. Restriction gives exactly the three `J_r` hypotheses

Let a root-valued flow on `G_r` assign roots

\[
p,q\in R_5
\]

to the two new matching edges of `E_r`.

Cutting those two edges leaves the same root at the two terminals of each block of `M_r`. The three possibilities for the ordered pair `(p,q)` are:

1. `p=q`;
2. `p,q` are distinct intersecting roots;
3. `p,q` are disjoint roots.

Their support-unordered boundary states are respectively

\[
A,
\qquad
B_r,
\qquad
C_r.
\]

Hence the complete profile of the zero-vertex reconnection is

\[
\boxed{
\Sigma(E_r)=J_r=\{A,B_r,C_r\}.
}
\]

Restricting any root flow on `G_r=P cup E_r` to `P` therefore gives

\[
\boxed{
\Sigma(P)\cap J_r\ne\varnothing.
}
\]

Applying this independently to the three smaller closures gives

\[
\boxed{
\Sigma(P)\cap J_i\ne\varnothing,
\qquad
\Sigma(P)\cap J_j\ne\varnothing,
\qquad
\Sigma(P)\cap J_k\ne\varnothing.
}
\]

### Trust note

These three intersections need not be witnessed by one common flow on `P`. The full-channel theorem requires only existence of a profile state in each `J_r`, and therefore consumes exactly the information supplied by the three independent smaller covers.

---

## 5. The original cap gives exactly `K_i`

The complete support-unordered profile of the standard two-vertex cap of matching `M_i` is

\[
\boxed{
\Sigma(cap_i)=K_i=\{B_s,D_s:s\ne i\}.
}
\]

Therefore a root-valued reconstruction of the original graph is equivalent to

\[
\boxed{
\Sigma(P)\cap K_i\ne\varnothing.
}
\]

Indeed a common state is realised on both the outside four-pole and the deleted two-vertex cap.

The cap index in the full-channel theorem is consequently the same distinguished index `i` defined by the original endpoint partition `ab|cd`; no permutation of the three terminal matchings is hidden in the final application.

---

## 6. Why old cap forcing is not used here

For a proper shore of a cyclic four-edge cut, adjoining any standard two-vertex cap gives a graph strictly smaller than the putative minimal counterexample. Vertex minimality then proves the usual cap-forcing conditions

\[
\Sigma(P)\cap K_r\ne\varnothing
\qquad(r=i,j,k).
\]

The arbitrary-edge four-pole is different. For its distinguished cap,

\[
P\cup cap_i=G,
\]

so the closure has the original graph order and is precisely the graph whose solubility is being proved. Minimality cannot supply

\[
\Sigma(P)\cap K_i\ne\varnothing.
\]

### Proposition 6.1 — no cap-forcing shortcut

The proper-shore cap-forcing theorem is not an input to the original-cap conclusion at an arbitrary edge.

The proof must instead use:

\[
\text{three smaller zero-vertex covers}
\Longrightarrow
\text{fixed-route equality/DDD analysis}
\Longrightarrow
\Sigma(P)\cap K_i\ne\varnothing.
\]

This is exactly the content of `ORIENTED_FULL_CHANNEL_LOCK_ELIMINATION_SYNTHESIS_V1.md`.

Consequently the final minimal-counterexample argument does not obtain the desired cap state by applying minimality to the original graph in disguise.

---

## 7. Exact theorem matching

The full-channel lock-elimination theorem has the following input.

- `P` is an ordered cubic four-pole;
- `cap_i` is one fixed two-vertex cap;
- all three zero-vertex reconnection closures are smaller connected bridgeless cubic graphs with root-valued `E_5` flows.

Its output is

\[
\boxed{
\Sigma(P)\cap K_i\ne\varnothing.
}
\]

Sections 1--5 show that the arbitrary-edge construction satisfies these hypotheses literally:

\[
\begin{array}{c|c}
\text{global construction}&\text{full-channel input}\\
\hline
G-\{u,v\}&P\\
ab\mid cd&M_i\\
\text{two deleted vertices and }uv&cap_i\\
P\cup E_r&G_r\\
\text{smaller root flow on }G_r&\Sigma(P)\cap J_r\ne\varnothing.
\end{array}
\]

There is no strengthening, weakening, relabelling, or simultaneous-witness assumption between the two theorem statements.

### Theorem 7.1 — exact interface compatibility

The simultaneous arbitrary-edge category theorem and vertex minimality supply every hypothesis of the full-channel cap-lift theorem for the same ordered four-pole and the same distinguished cap.

---

## 8. From a common support-unordered state to labelled gluing

It remains to justify that

\[
\Sigma(P)\cap K_i\ne\varnothing
\]

really produces a root-valued flow on `G`, not merely equality of orbit labels.

Let

\[
\sigma\in\mathcal S
\]

be a common state. Choose:

- one root-valued flow `lambda_P` on `P` whose boundary state is `sigma`;
- one root-valued flow `lambda_C` on `cap_i` whose boundary state is `sigma`.

For a labelled flow, each of the five support coordinates has one even terminal trace

\[
S_1,\ldots,S_5\subseteq\{a,b,c,d\}.
\]

Equality of support-unordered states means that the two multisets of five traces are equal. Therefore there is a permutation

\[
\pi\in S_5
\]

such that, after applying `pi` to every support index of `lambda_C`,

\[
S_t^{P}=S_t^{C}
\qquad(t=1,\ldots,5).
\]

At each terminal, the root label is exactly the pair of support indices whose traces contain that terminal. Coordinatewise equality of the five traces consequently gives equality of the root labels at every terminal.

Glue each pair of corresponding semiedges. The joined edge receives this common root. All old cubic vertex equations are unchanged, and the two cap vertex equations already hold.

### Theorem 8.1 — labelled gluing from state intersection

A common support-unordered state of two ordered four-pole profiles is sufficient for a root-valued coordinatewise gluing after one global support permutation on one side.

No terminal permutation is required, because the terminal order was fixed throughout. No independent support permutation may vary from edge to edge; one global element of `S_5` aligns all five traces simultaneously.

---

## 9. Final arbitrary-edge contradiction

Let `G` be a prime vertex-minimal counterexample and choose any edge `uv`.

1. The three reconnection closures are smaller soluble graphs.
2. Their flows give all three intersections `Sigma(P) cap J_r != empty`.
3. The full-channel theorem gives `Sigma(P) cap K_i != empty`.
4. The labelled-gluing theorem reconstructs a root-valued `E_5` flow on `G`.

This contradicts the definition of `G`.

### Theorem 9.1 — authorial final-interface closure

Once the imported cut/base reductions and the full-channel theorem are granted in their stated scopes, the final passage from an arbitrary edge to a contradiction is exact and noncircular.

---

## 10. Disconnected extension

Let `G` be any finite bridgeless cubic multigraph, not necessarily connected. Each connected component is bridgeless and cubic. Apply the connected theorem to every component using the same global support index set

\[
\{1,2,3,4,5\}.
\]

For each `t`, take the union of the `t`-th even support over all components. A disjoint union of even edge sets is even, and every edge still belongs to exactly two supports.

### Corollary 10.1

The connected five-support theorem implies the corresponding theorem for every finite bridgeless cubic multigraph, componentwise.

The empty graph is covered by the empty five-tuple.

---

## 11. Authorial dependency boundary

### Exact in this dossier

- the ordered arbitrary-edge four-pole and distinguished cap agree across all parent theorems;
- the three smaller reconnection covers yield exactly the three `J_r` profile intersections;
- no simultaneous flow witness is required;
- the original cap has exactly profile `K_i`;
- proper-shore cap forcing is inapplicable to the same-order original cap and is not used;
- the full-channel theorem's hypotheses and outputs match the global construction literally;
- support-unordered state equality gives one global support permutation aligning all labelled boundary traces;
- the final gluing preserves every root and cubic conservation law;
- the connected theorem extends componentwise to disconnected bridgeless cubic multigraphs.

### Imported authorial mathematics

- simultaneous category validity of all three reconnection closures;
- the finite three-reconnection fixed-route classification;
- equality/DDD full-channel lock elimination;
- contextual inverse transfer and its well-foundedness;
- cut and bounded-category reductions.

### Still outside this role checkpoint

- proof-development expansion of every imported theorem;
- independent mathematical audit;
- curation or canonical movement;
- Lean verification;
- manuscript integration;
- release, arXiv, DOI, peer review, or publication.