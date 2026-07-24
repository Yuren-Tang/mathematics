# Oriented DDD locks escape by `Omega` descent modulo complete fixed-order plateaus

## Research Lead master theorem v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workstream:** `AC-RL-PURE-NNI-02`  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `0c7a6cdca733a54a16840f8287fed9ae1eb0c0a2`

**Parents:**

- `DDD_LOCK_STRICT_OMEGA_AMBIENT_NNI_TRICHOTOMY_V1.md`;
- `DDD_LOCK_GLOBAL_PACHNER_POTENTIAL_V1.md`;
- `PURE_NNI_PRESCRIBED_PARENT_PHASE_B_SUPPORT_CHANNEL_TRANSITION_OBJECT_V1.md`;
- `WELD_INSERTION_SUPPORT_SWITCH_LIFT_V1.md`;
- `SWITCH_POP_COLLAR_ROOT_SHORT_SIDE_V1.md`;
- `CELLWISE_ROOT_SEAM_AND_CONSTANT_RUN_TRACK_ERASURE_V1.md`;
- the exact root-NNI/support-switch critical-overlap table and terminal ledger.

**Conclusion:** `FC-PURE-NNI-ESCAPE` holds at Research Lead authorial level. No `2--0` cancellation and no lower-order root-flow call occurs in the constructed source history. The equal-face cancellation from the older mixed surgery proof is replaced by a finite root-valued plateau orbit, five exact equal-face exit macros, and a residual `H_13/H_14` route-sector contradiction.

This theorem is not independently reconstructed or audited.

---

## 1. Complete root endpoint plateau

Fix one complete prime oriented DDD full-channel prescribed-parent state

\[
S=(N,G,\delta,\lambda,\chi,P,\mathfrak B,\kappa,\mathscr H,\mathfrak a,\tau,\alpha)
\]

from `FC-PURE-NNI-ESCAPE`. Its two marked roots are disjoint, and every crossed rescue channel has the oriented prescribed route `M_i`.

A **root endpoint plateau edge** is one of the following reversible fixed-order source certificates, provided neither endpoint is already parent-successful or terminal:

1. one legal closed support-pair component switch;
2. one root NNI whose two endpoint states have equal `Omega` in the displayed DDD normalisation, including an equal-face branch-swap;
3. one bounded root-to-root critical-overlap rectangle obtained from a one-atom comparison after applying the switch--pop endpoint collars and the complete seam/run track-erasure theorem;
4. one literal identity subdivision or complete-state inverse of one of the preceding edges.

Only the root-valued short sides are vertices of the plateau graph. A zero/co-root edge used inside a certified rectangle is an interior singularity, not an additional endpoint state.

A move which reaches:

- a separating rescue channel;
- `K_i`;
- the literal prescribed parent;
- or a named route/cut/bounded terminal

leaves the plateau and is consumed immediately.

Let

\[
\mathscr P(S)
\]

be the connected component of `S` in this reversible nonterminal root-endpoint graph.

### Finiteness

At fixed labelled order `N` there are finitely many:

- cubic incidence tables on the fixed vertex/dart slots;
- root assignments;
- crossed sheets;
- cap/route/support-component partitions;
- atom endpoint orientations;
- prefix-identity maps.

Thus `mathscr P(S)` is finite. This fact will be used only to choose an energy-minimising endpoint, never to infer a terminal or progress edge.

---

## 2. Gauge-independent plateau energy

For one plateau endpoint `X`, let `Norm(X)` be the four support bijections which carry its ordered marked disjoint roots to

\[
12,34
\]

while retaining the ordered cap blocks and sending the unused support to `5`.

For `eta in Norm(X)`, calculate the established DDD energy

\[
\Omega_\eta(X)=\sum_v\omega(\eta\Delta_v)
\]

with

\[
\begin{array}{c|cccccccccc}
T&123&124&125&134&135&145&234&235&245&345\\
\hline
\omega(T)&3&0&1&3&0&1&1&3&3&3.
\end{array}
\]

Define

\[
\overline\Omega(X)=\min_{\eta\in Norm(X)}\Omega_\eta(X)
\]

and the plateau energy

\[
\boxed{
\mu(\mathscr P)=\min_{X\in\mathscr P}\overline\Omega(X).}
\]

This is a nonnegative integer. A global support relabelling does not change `mu`, because it only permutes the compatible normalisations.

Choose one endpoint `X_0 in mathscr P` and one compatible normalisation `eta_0` realising `mu(mathscr P)`.

---

## 3. Relative switch/NNI transport across one equal face

Let two adjacent vertices of `X_0` carry the same root triangle

\[
T=\{x,y,z\}
\]

and let their central edge be `r`. The four exterior branches are two copies of the other two roots. Let `h` be a rescue root such that:

- the central root `r` is absent from `H_h`;
- both exterior roots belong to `H_h`.

Then the equal-face branch-swap is a root-valued `2--2` NNI and is a two-break of the local `H_h` transition system.

### Lemma 3.1 — route exit or one-sided component

Exactly one of:

1. the branch-swap changes the oriented terminal matching of `H_h`, hence breaks the full-channel lock;
2. in one of the two equal-face branch placements, the two local `H_h` passages lie in distinct closed components.

### Proof

Suppress every degree-two part of the outside `H_h` system and retain only the perfect matching `O` induced on the four local ports. The two equal-face branch placements give two of the three perfect matchings `L_0,L_1`.

- If `O` is the third matching, both `O union L_0` and `O union L_1` are one cycles with opposite cyclic port orders. Changing `L_0` to `L_1` changes the oriented route.
- If `O=L_0` or `O=L_1`, the matching equal to `O` closes as two components, one through each local passage.

No fourth matching exists. ∎

In the nonexit branch, switch either one of those two closed components. Exactly one local triangle is transported by the support transposition `tau_h`; call it

\[
U=\tau_h(T).
\]

The local pair is now `T,U`, while every exterior change is carried by the witnessed closed component.

---

## 4. Complete plateau-orbit conjugacy

The preceding one-sided switch is global along its physical component. To compare plateau minima, its outside transport must not be discarded. The correct statement is relative orbit conjugacy, not a coefficient-only local replacement.

### Theorem 4.1 — equal-face plateau transport rectangle

Fix one of the equal-face macros in Section 5. Let `mathscr P_-` be the source root-endpoint plateau and `mathscr P_+` the plateau after its displayed local root endpoint is installed.

There is a bijection

\[
\Phi:\mathscr P_-\longrightarrow\mathscr P_+
\]

between complete root endpoints, preserving literally:

- every exterior source dart and its ancestor identity;
- the cap block and oriented route field;
- the live prescribed-parent topology;
- all side attachments and support transport outside the two-vertex cell;
- graph order and the named terminal flags;

and changing the normalised triangle multiset only by the displayed two-vertex source row.

Consequently

\[
\boxed{
\mu(\mathscr P_+)
\le
\mu(\mathscr P_-)+\Delta_{\rm local}.}
\]

The reverse local macro gives the inverse endpoint correspondence whenever no exit has occurred.

### Proof

Take one witnessed plateau word from a source endpoint to another source endpoint and commute the bounded equal-face macro across it one generator at a time.

1. **Disjoint generators.**  
   A disjoint root NNI, component switch, identity subdivision, or seam/run rectangle commutes literally with the local cell.

2. **The selected `H_h` component.**  
   Lemma 3.1 gives the complete three-matching transition square. Component incidence vectors on the two branch placements correspond by symmetric difference. The outside selected edge set is retained as a witnessed physical component; only one local passage changes shore.

3. **A support switch meeting the local insertion.**  
   `WELD_INSERTION_SUPPORT_SWITCH_LIFT_V1.md` lifts the switch as one even predecessor-order correction. All noncentral edges remain roots and at most one central zero/co-root atom appears.

4. **A root NNI meeting the local cell.**  
   The exact tetrahedral critical-overlap table either commutes root-valuedly, gives a named category exit, or leaves one standard zero/co-root atom. No second atom is created.

5. **Atom continuation.**  
   The singular locus is nonbranching. Both sides of this comparison are specified root endpoints, so the birth and death collars have genuine root-valued short sides. `CELLWISE_ROOT_SEAM_AND_CONSTANT_RUN_TRACK_ERASURE_V1.md` replaces the complete intervening atom track by a root rectangle fixing its four labelled sides.

Thus every source plateau word has a transported target plateau word with the same complete exterior endpoint data. Reversing the local movie supplies the inverse correspondence. Since all transported exterior vertex triangles agree after applying the corresponding compatible support normalisation, the energy difference is exactly the finite two-vertex row. Taking minima proves the inequality. ∎

### Why this does not repeat the v7.2 gap

The theorem compares two **specified root endpoint states** and has root-normalised short sides at both ends. It does not claim that a root crosscut realizes an algebraically nonroot prescribed pairing. The prescribed parent remains an exterior obligation throughout; it is discharged only after an actual channel break or `K_i` entry.

---

## 5. Five productive equal-face rows

The following table is complete for the rows needed below. `T,T` denotes the source equal pair; the displayed switch is the one-sided component switch of Lemma 3.1. A category or route failure at any arrow is an accepted exit.

\[
\begin{array}{c|c|c|c|c|c}
T&r&h&\text{after one-sided switch}&\text{optional root NNI endpoint}&\Delta_{\rm local}\\
\hline
123&23&14&123+234&\text{none}&-2\\
125&25&14&125+245&124+145&-1\\
235&25&13&235+125&\text{none}&-2\\
245&25&14&245+125&\text{none}&-2\\
345&45&13&345+145&\text{none}&-2
\end{array}
\]

For example, in the only two-step row,

\[
2\omega(125)=2,
\qquad
\omega(124)+\omega(145)=1.
\]

The complete coefficient checks are:

- `23` is disjoint from `14`, and the two exterior roots of `123` are both `H_14`-eligible;
- `25` is disjoint from `14`, and the exterior roots of `125` are `H_14`-eligible;
- `25` is disjoint from `13`, and the exterior roots of `235` are `H_13`-eligible;
- `25` is disjoint from `14`, and the exterior roots of `245` are `H_14`-eligible;
- `45` is disjoint from `13`, and the exterior roots of `345` are `H_13`-eligible.

Every intermediate and endpoint triangle is one of the ten root triangles.

### Corollary 5.1 — strict plateau descent

If a `mu`-minimising locked endpoint contains any one of the five displayed equal faces, then either:

- a branch-swap/component/NNI arrow breaks the lock or enters a named terminal; or
- the target plateau satisfies
  
  \[
  \boxed{\mu(\mathscr P_+)<\mu(\mathscr P_-).}
  \]

---

## 6. Finite residual triangle classification

Assume that a `mu`-minimising prime locked plateau has:

- no strict `Omega`-lowering distinct-triangle NNI;
- none of the five productive equal faces of Section 5;
- no route/cut/bounded exit.

### Lemma 6.1 — five types are impossible

The triangle types

\[
123,125,235,245,345
\]

cannot occur.

### Proof

Inspect the following nonboundary root incidence in each type:

\[
\begin{array}{c|c|c}
T&\text{selected incidence}&\text{every distinct neighbouring type gives NNI energy change}\\
\hline
123&23&-1\text{ or }-5\\
125&25&-1\text{ or }-3\\
235&25&-1\text{ or }-2\\
245&25&-3\text{ or }-2\\
345&45&-1\text{ or }-2.
\end{array}
\]

Only roots `12,34` are boundary roots of the DDD carrier, so each displayed incidence belongs to an internal edge. A distinct triangle on its other endpoint would be a strict `Omega`-lowering NNI, contrary to hypothesis. Hence its other endpoint must have the same type, producing exactly the productive equal face in the corresponding row of Section 5. Contradiction. ∎

Therefore every source vertex belongs to the residual set

\[
\boxed{\mathcal R=\{124,134,135,145,234\}.}
\]

### Reproducible finite certificate

Enumerate the ten three-subsets of `[5]`. For each selected type and root incidence, enumerate the two other three-subsets containing that root. Replace the adjacent pair by the opposite pair in its four-support tetrahedron and calculate the two-vertex weight difference. The five rows above are the complete negative-neighbour certificate. No graph isomorphism or ambient search is used.

---

## 7. Residual route-sector contradiction

In the residual alphabet, the no-lowering hypothesis also forbids the two distinct adjacencies

\[
134\mathbin{-}_{14}145,
\qquad
134\mathbin{-}_{34}234,
\]

whose opposite root flips lower `Omega` by one.

All other relevant residual adjacencies are equal-type edges or the nondecreasing pairs

\[
124\mathbin{-}_{14}134,
\quad
124\mathbin{-}_{14}145,
\quad
124\mathbin{-}_{24}234,
\quad
134\mathbin{-}_{13}135,
\quad
135\mathbin{-}_{15}145.
\]

### `H_13` sectors

The two selected roots at each residual type are

\[
\begin{array}{c|cc}
124&12&14\\
134&14&34\\
135&15&35\\
145&14&15\\
234&23&34.
\end{array}
\]

The forbidden `134-234` root-`34` adjacency leaves exactly two disjoint type sectors:

\[
\boxed{\{124,134,135,145\}}
\qquad\text{and}\qquad
\boxed{\{234\}}.
\]

A boundary `12` incidence can occur only at type `124`. In an oriented full lock, each `H_13` boundary path joins one `12` terminal to one `34` terminal. Starting in the first sector, such a path can reach a `34` boundary only at type `134`. Hence both `34` boundary darts must be incident with type `134` vertices.

### `H_14` sectors

Here the selected roots are

\[
\begin{array}{c|cc}
124&12&24\\
134&13&34\\
135&13&15\\
145&15&45\\
234&24&34.
\end{array}
\]

Again using the forbidden `134-234` adjacency, the sectors are

\[
\boxed{\{124,234\}}
\qquad\text{and}\qquad
\boxed{\{134,135,145\}}.
\]

Every `12` boundary path starts at type `124`, now in the first sector. To end at a `34` terminal with the locked route, it must end at type `234`. Hence both `34` boundary darts must be incident with type `234` vertices.

The same two labelled `34` boundary darts cannot be incident simultaneously with type `134` and type `234`. This contradicts the assumption that both `H_13` and `H_14` have the common oriented full-lock route.

### Theorem 7.1 — no residual locked plateau

No complete prime oriented DDD full-channel lock can satisfy all of:

- no strict `Omega`-lowering root NNI;
- no productive equal-face plateau macro;
- no route/cut/bounded exit.

---

## 8. `Omega`-plateau escape theorem

### Theorem 8.1 — plateau exit

Every nonterminal root-endpoint plateau of an oriented DDD full-channel lock has one of:

1. a channel-lock break and the Phase-B prescribed-parent repair;
2. a cap-compatible `K_i` endpoint;
3. a named `2/3/4`-cut or bounded terminal;
4. a strict transition to a plateau of smaller `mu`.

### Proof

Move within the finite reversible plateau to an endpoint and normalisation realising `mu`.

- If it has a strict `Omega`-lowering distinct-triangle NNI, use the strict ambient-NNI trichotomy; a surviving locked output has smaller target plateau energy.
- Otherwise the DDD potential theorem supplies an equal-face pair.
- If one of the productive rows is present, Corollary 5.1 gives an exit or strict plateau descent.
- If none is present, Lemma 6.1 restricts all vertices to `mathcal R`, contradicting Theorem 7.1.

Thus one of Items 1--4 occurs. ∎

Finiteness has supplied only the minimising endpoint and a witnessed plateau path to it. Progress is supplied by the strict NNI table, the five explicit equal-face macros, or the route-sector contradiction.

---

## 9. Master theorem `FC-PURE-NNI-ESCAPE`

### Theorem 9.1

Let `S` be any complete prime fixed-order prescribed-parent state satisfying the six lock hypotheses in `PURE_NNI_PRESCRIBED_PARENT_PHASE_C_ARCHITECTURE_DECISION_V1.md`.

Then there is a finite source-faithful history using only:

- root-valued ordinary `2--2` NNIs;
- legal closed support-component switches;
- bounded one-atom normalization and root endpoint seam/run rectangles;
- exact route/cut/bounded terminal moves;

and using no actual `2--0` cancellation and no lower-order root-flow call, which ends in one of:

1. a separating DDD channel followed by the Phase-B parent movie;
2. a cap-compatible `K_i` state;
3. a named `2/3/4`-cut or bounded terminal;
4. a root flow on the literal prescribed-parent topology.

### Proof

Apply Theorem 8.1. In Item 4, `mu` strictly decreases. Since `mu` is a nonnegative integer, only finitely many strict plateau descents occur. The terminal plateau therefore has Item 1, 2, or 3. Items 1--2 discharge the prescribed parent by the existing exact source consumers; Item 3 is consumed by the terminal ledger. Every intermediate history is at the original graph order. ∎

---

## 10. Effect on v7.2

The theorem closes the unique PDL blocker

\[
\texttt{AC-PD-V7.2-PURE-NNI-TARGET-REINSERTION}.
\]

Combined with the already reconstructed v7.2 units, it supplies the missing fixed-order return after an arbitrary-flow single pop:

\[
\text{single pop}
\to
\text{root/one-atom normalisation}
\to
\text{pure-NNI prescribed-parent return}
\to
\text{stored prefix return}.
\]

Accordingly, the RL branch now has a complete authorial candidate for ordinary strong-induction closure. This remains subject to PDL reconstruction and independent assurance. No established five-support or five-CDC theorem is claimed here.

---

## 11. Exact dependency and nondependency ledger

### Used

- DDD `15/15` strict flip table and no-local-minimum theorem;
- exact NNI category/terminal rows;
- Phase-B separating-channel parent repair;
- support-switch lift with at most one atom;
- switch--pop root endpoint collars;
- one-token nonbranching and cellwise seam/run erasure;
- complete state/dart/cap/route/prefix coordinates.

### Not used

- an actual equal-face `2--0` cancellation;
- a lower-order root-flow choice;
- generic root/Kempe/NNI connectivity;
- topology-only spanning-tree reachability;
- `Q_N`, `M_N`, `d_N`;
- nested bubbles or terminal frames;
- shortest Petersen cores, global `C6/C8` annuli, or Type-T graph contraction;
- finiteness as a substitute for a progress edge.

---

## 12. Trust boundary

### Completed at RL authorial level

- strict ambient `Omega` descent;
- complete root-endpoint plateau definition;
- gauge-independent plateau energy;
- equal-face route/one-sided-component lemma;
- full source-level plateau-orbit transport rectangle;
- five productive equal-face macros;
- exact five-type residual certificate;
- `H_13/H_14` residual route contradiction;
- `FC-PURE-NNI-ESCAPE` and its exact v7.2 repair effect.

### Still required

- independent PDL reconstruction of every critical-overlap transport row and the plateau-energy argument;
- independent theorem audit;
- downstream integration only after those roles accept the repair.

### No status claimed

No Lean theorem, Curator/canonical movement, manuscript, release, tag, arXiv, DOI, peer-review, publication, or established five-CDC result is asserted.
