# A fixed rescue channel gives a switch-invariant strict rank for every oriented DDD lock

## Research Lead theorem v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workstream:** `AC-RL-PURE-NNI-02`  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`

**Controlling parents:**

- `DDD_LOCK_OMEGA_PLATEAU_ORBIT_TRANSPORT_SCOPE_CORRECTION_V1.md`;
- `DDD_LOCK_STRICT_OMEGA_AMBIENT_NNI_TRICHOTOMY_V1.md`;
- `PURE_NNI_PRESCRIBED_PARENT_PHASE_C_ALL_INDEX_AMBIENT_ESCAPE_FRONTIER_V2.md`;
- `PURE_NNI_PRESCRIBED_PARENT_STATE_INTERFACE_NORMAL_FORM_V1.md`;
- the exact equal-face three-matching lemma;
- the exact root-NNI category and terminal ledger.

**Conclusion.** Every complete prime oriented DDD full-channel lock has a finite source-faithful same-order escape using only ordinary root-valued `2--2` NNIs, legal closed support-component switches in one fixed rescue channel, and exact terminal consumers. No `2--0` cancellation, lower-order root-flow call, orbit-minimum comparison, co-root track, or zero-overlap normalization is used.

The proof introduces a new nonnegative integer potential which is invariant under the entire physical switch component, including its exterior vertices. It therefore repairs exactly the defect isolated by `DDD_LOCK_OMEGA_PLATEAU_ORBIT_TRANSPORT_SCOPE_CORRECTION_V1.md`.

---

## 1. Fixed-channel frame

Let the current ordered marked disjoint roots be

\[
p,q,
\qquad p\cap q=\varnothing,
\]

and let `m` be the unused support index. In a complete oriented full-channel lock, each of the four roots meeting both `p` and `q` is a locked rescue channel.

Choose one such channel and retain it throughout the source movie; call it

\[
h_\star.
\]

There is a unique support bijection

\[
\eta
\]

with

\[
\eta(p)=12,
\qquad
\eta(q)=34,
\qquad
\eta(m)=5,
\qquad
\eta(h_\star)=14.
\]

Indeed `h_\star` selects one support from `p` and one from `q`; send those selected supports to `1,4`, the other two to `2,3`, and the unused support to `5`.

This is the **transported `H_14` frame**. It is a complete-state coordinate, not a quotient by support permutations.

### Frame transport through a nonexit `H_{h_\star}` switch

Let `Z` be one closed component of `H_{h_\star}`.

- If `Z` contains neither marked root occurrence, keep `eta`.
- If it separates the two marked roots, the standard rescue switch makes the prescribed parent root-valued and is consumed immediately.
- If the state remains a lock, a marked component contains both marked root occurrences. In canonical coordinates both marked roots are transposed by `tau_14`; transport the frame by the same transposition:
  
  \[
  \eta' = \tau_{14}\circ\eta.
  \]

The unused support remains `5`, and the same physical channel is again represented by `14`.

Every later category-safe ambient NNI keeps the marked roots and hence keeps the transported frame. If any move breaks the channel lock, enters `K_i`, realizes the literal parent, or produces a named cut/bounded category, the appropriate existing consumer applies before continuation.

---

## 2. The switch-invariant vertex weight

For a canonical root triangle `T`, define

\[
\begin{array}{c|cccccccccc}
T&123&124&125&134&135&145&234&235&245&345\\
\hline
\xi(T)&1&0&1&0&0&0&1&2&1&0.
\end{array}
\]

Equivalently,

\[
\xi^{-1}(2)=\{235\},
\qquad
\xi^{-1}(1)=\{123,125,234,245\},
\]

and all other triangle types have weight zero.

The transposition `tau_14` has triangle orbits

\[
123\leftrightarrow234,
\qquad
125\leftrightarrow245,
\qquad
135\leftrightarrow345,
\]

and fixes `124,134,145,235`. Hence

\[
\boxed{\xi(\tau_{14}T)=\xi(T)}
\]

for every root triangle `T`.

For one complete fixed-order closed root state `S`, define

\[
\boxed{
\Xi(S)=\sum_{v\in V(G)}\xi\bigl(\eta(\Delta_v)\bigr).}
\]

The sum is over the complete labelled closed graph, including any fixed cap vertices. Thus its domain is unchanged by every allowed same-order move.

It is a nonnegative integer and satisfies

\[
0\le\Xi(S)\le2|V(G)|.
\]

---

## 3. Exact invariance under the whole physical component

### Lemma 3.1 — closed `H_{h_\star}` switches preserve `Xi`

Let `S^Z` be obtained by switching one legal closed `H_{h_\star}` component `Z`, and suppose the move does not already leave the locked prime state class. Then

\[
\boxed{\Xi(S^Z)=\Xi(S).}
\]

### Proof

Work first in the canonical frame.

At every vertex of `Z`, the two selected incident roots are translated by `h_\star`; the root triangle is therefore changed by `tau_14`. At every vertex outside `Z`, it is unchanged.

If `Z` contains no marked root occurrence, the frame is unchanged, so invariance follows directly from

\[
\xi\circ\tau_{14}=\xi.
\]

If `Z` contains both marked root occurrences, the target frame is also transported by `tau_14`. Thus:

- a vertex in `Z` is acted on twice and returns to its old canonical triangle;
- a vertex outside `Z` is acted on once by `tau_14`;

and `xi` is unchanged in either case.

The remaining possibility is a component separating the marked roots, which is an absorbing parent-repair output rather than a nonexit locked transition. ∎

### Consequence

Unlike the quarantined `Omega`-orbit argument, this lemma does not discard exterior component contributions. Each exterior triangle is checked explicitly by the `tau_14` invariance of `xi`. There is no minimization over two different switch orbits.

---

## 4. Six strict ordinary-NNI rows

Call

\[
\mathcal B=\{123,234,125,245\}
\]

the set of **bad channel types**.

For a vertex of type `123` or `234`, select its root-`23` incidence. For a vertex of type `125` or `245`, select its root-`25` incidence. Neither `23` nor `25` is a DDD boundary root, since the boundary roots in the transported frame are `12,34`. Hence the selected incidence is always an internal edge of the DDD carrier.

There are only three root triangles containing a fixed root. The complete distinct-neighbour table is therefore:

\[
\begin{array}{c|c|c|c|c}
\text{central root}&\text{source pair}&\text{opposite NNI pair}
&\Xi_{\rm source}&\Xi_{\rm target}\\
\hline
23&123+234&124+134&2&0\\
23&123+235&125+135&3&1\\
23&234+235&245+345&3&1\\
25&125+245&124+145&2&0\\
25&125+235&123+135&3&1\\
25&245+235&234+345&3&1.
\end{array}
\]

Every displayed opposite pair consists of root triangles, and every row satisfies

\[
\boxed{\Delta\Xi=-2.}
\]

### Lemma 4.1 — distinct bad neighbour gives strict descent or an exit

If one selected bad-type incidence has a distinct neighbouring triangle, perform the displayed ordinary root NNI.

After the exact graph-category and route/profile test, exactly one of the following occurs:

1. a channel-lock break and prescribed-parent rescue;
2. a cap-compatible `K_i` state;
3. a named `2/3/4`-cut or bounded terminal;
4. another complete prime oriented lock with `Xi` smaller by two.

The parent topology, cap block, dart ancestry and stored-prefix identity are retained literally by the ordinary NNI move contract.

---

## 5. Equal bad neighbour: a direct root-only macro

Suppose the selected internal edge has the same bad triangle on both ends.

### Root-`23` equality

The equal pair is `123+123` or `234+234`. Its central root `23` is absent from `H_14`, while both exterior roots at each endpoint belong to `H_14`.

### Root-`25` equality

The equal pair is `125+125` or `245+245`. Its central root `25` is absent from `H_14`, while both exterior roots at each endpoint belong to `H_14`.

Thus the exact equal-face three-matching lemma applies in all four cases.

### Theorem 5.1 — equal bad-face escape macro

From one equal bad face, there is a finite source movie with exactly one of the following outcomes:

1. the equal-face branch swap changes the oriented `H_14` route and breaks the lock;
2. a legal component switch reaches a separating channel, `K_i`, or a named terminal;
3. a category-safe ordinary root NNI reaches another locked state with `Xi` smaller by two.

### Proof

The three-matching lemma first gives either an immediate oriented-route change or a branch placement in which the two local `H_14` passages lie in distinct closed components. Move to that placement by zero or one root-valued equal-face branch-swap NNI.

Switch either one of the two displayed components.

- If the switch separates the marked roots or reaches another absorbing output, consume it.
- Otherwise the switched state remains a complete root-valued lock, and Lemma 3.1 says that `Xi` is unchanged.

Locally the switch changes exactly one of the two equal triangles by `tau_14`. Hence the local source pair becomes

\[
123+234
\quad\text{or}\quad
125+245.
\]

Perform the corresponding root NNI from Section 4:

\[
123+234\longrightarrow124+134,
\]

or

\[
125+245\longrightarrow124+145.
\]

It lowers `Xi` by two. The usual category test gives an absorbing result or a strict locked descent. ∎

### Zero-overlap boundary

Every endpoint and every intermediate state in this macro is root-valued. No quadruple-equality zero insertion and no co-root atom is produced. Consequently the zero-overlap defect recorded in the scope correction is not invoked or bypassed; it is absent from this route.

---

## 6. The zero-weight alphabet cannot carry the locked channel

Assume that a complete prime oriented lock contains no bad channel type. Its triangle alphabet is then contained in

\[
\mathcal R_{14}=\{124,134,135,145,235,345\}.
\]

Consider an `H_14` boundary path beginning at one of the two boundary root-`12` occurrences.

A root triangle containing boundary root `12` is one of

\[
123,124,125.
\]

The bad types `123,125` are absent, so the first vertex is necessarily type `124`. Its two `H_14` roots are

\[
12,24.
\]

The root-`24` incidence is internal. The only root triangles containing `24` are

\[
124,234,245.
\]

The latter two are bad and absent, so the next vertex is again `124`. Repeating alternately across roots `24` and `12`, the entire component consists only of type-`124` vertices and roots `12,24`.

Therefore this component can meet boundary root `12`, but it cannot meet boundary root `34`.

In an oriented DDD full-channel lock, each of the two `H_14` boundary paths has the prescribed locked route and joins one `12` terminal to one `34` terminal. This is impossible.

### Theorem 6.1 — no bad-free full-channel lock

Every complete oriented DDD full-channel lock contains at least one vertex of type

\[
123,234,125,245
\]

in its transported `H_14` frame.

---

## 7. Well-founded fixed-channel escape

### Theorem 7.1 — `H_14` switch-invariant DDD-lock escape

Starting from any complete prime oriented DDD full-channel lock, repeatedly apply the following deterministic alternative.

1. By Theorem 6.1 choose one bad-type vertex and its selected internal root `23` or `25`.
2. If its neighbour is distinct, apply Lemma 4.1.
3. If its neighbour is equal, apply Theorem 5.1.

Every nonabsorbing iteration returns another complete prime oriented lock and lowers

\[
\Xi
\]

by exactly two. Since `Xi` is a nonnegative integer, only finitely many such iterations are possible.

Hence a finite source-faithful history ends in exactly one of:

1. a separating rescue channel followed by the literal prescribed-parent NNI;
2. a cap-compatible `K_i` route/profile state;
3. a named cyclic `2/3/4`-cut or bounded terminal;
4. a root flow on the literal prescribed-parent topology.

No nonterminal full-channel lock can be closed under this move alphabet.

### Quantitative bound

Because `Xi<=2|V(G)|` and every nonabsorbing macro lowers it by two, the history contains at most

\[
|V(G)|
\]

strict macros before absorption, in addition to their bounded branch-swap and component-switch collars.

---

## 8. All-index fidelity

The proof does not freeze the initial missing index or the initial ordered four-root word.

A common-component `H_{h_\star}` switch may change both marked roots and hence migrate the displayed co-root parent data. The transported channel frame is updated exactly as in Section 1, and `Xi` remains invariant by Lemma 3.1. The complete fields

\[
(m,\pi,\sigma,\mathcal H,\kappa,\tau,P,\alpha)
\]

are recomputed after every switch and every NNI.

The physical channel `h_\star`, prescribed-parent identity `P`, cap block and prefix map `alpha` remain literal source coordinates. Thus the theorem applies inside the corrected all-index transition object rather than only to the initial four-channel word.

### Corollary 8.1 — no closed all-index DDD-lock SCC

The prime nonterminal part of the complete all-index horizontal state graph contains no strongly connected component all of whose states are oriented DDD full-channel locks and which is disjoint from parent success, `K_i`, and the named terminal set.

---

## 9. Reproducible finite certificate

Use the canonical JSON object consisting of:

1. the ten `xi` values;
2. the ten assertions `xi(T)=xi(tau_14 T)`;
3. the six strict NNI rows of Section 4.

Serialized with sorted keys and no whitespace, its SHA-256 digest is

`b901ef3bfb41803e48e8a17efd9eb37c5fe48bd37ea0e771fd2f5ffed1a9a25a`.

No graph-isomorphism quotient, search heuristic, or unrecorded computation enters the proof. The finite certificate may be reproduced by enumerating the ten three-subsets of `[5]` and the three triangles containing each selected root `23` or `25`.

---

## 10. Relation to the quarantined `Omega` master attempt

The present theorem does not use:

- the false assertion that a physical component switch changes energy only at two local vertices;
- a bijection between source and target support-switch orbits;
- an orbit minimum;
- any of the exterior `Omega` summands;
- the five-row `Omega` plateau descent;
- a zero/co-root critical-overlap rectangle.

Instead, the weight `xi` is chosen to be invariant under the actual support transposition on every vertex of the complete component. The exterior contribution is exactly zero, vertex by vertex.

The still-valid local three-matching lemma and exact category consumers are retained. The old scope correction remains correct as a rejection of the former `Omega` argument, but it is no longer a blocker.

---

## 11. Trust boundary

### Proved here at Research Lead authorial level

- the transported fixed-channel frame;
- a complete physical-component switch invariant;
- the six exhaustive strict NNI rows;
- a root-only equal-face macro with no zero overlap;
- the bad-free route-sector contradiction;
- finite pure-NNI/support-switch escape from every oriented DDD lock;
- all-index fidelity of the descent.

### Required downstream

- PDL source-level reconstruction of the frame transport, six-row table and route contradiction;
- independent audit of the fixed-channel rank and every category consumer;
- downstream integration only after those roles accept the theorem.

### No status claimed

No Lean theorem, Curator/canonical movement, manuscript, release, tag, arXiv, DOI, peer-review, publication, or already established five-CDC theorem is asserted here.
