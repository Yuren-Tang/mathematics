# Pure-NNI prescribed-parent return: all-index ambient escape is closed by a fixed-channel switch-invariant rank

## Research Lead master theorem v3

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workstream:** `AC-RL-PURE-NNI-02`  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact theorem input:** `DDD_LOCK_H14_SWITCH_INVARIANT_DESCENT_THEOREM_V1.md@a80c3e202375367c2761c30f5827ac29f1abec10`

**Supersedes for controlling status:**

- the blocked-frontier conclusion of `PURE_NNI_PRESCRIBED_PARENT_PHASE_C_ALL_INDEX_AMBIENT_ESCAPE_FRONTIER_V2.md`;
- the quarantined completion claim of `DDD_LOCK_OMEGA_PLATEAU_ESCAPE_MASTER_THEOREM_V1.md`;
- `DDD-PLATEAU-PRODUCTIVE-ROW-ESCAPE` as an open implication;
- `FC-PURE-NNI-ALL-INDEX-AMBIENT-ESCAPE` as an open node.

The scope correction `DDD_LOCK_OMEGA_PLATEAU_ORBIT_TRANSPORT_SCOPE_CORRECTION_V1.md` remains correct: the former `Omega` orbit-minimum proof is invalid. The present proof does not repair that argument; it replaces it.

---

## 1. Exact theorem

### Theorem `FC-PURE-NNI-ALL-INDEX-AMBIENT-ESCAPE`

Let

\[
S=(N,G,\delta,\lambda,\chi,P,\mathfrak B,\kappa,
\mathscr H,\mathfrak a,\tau,\alpha)
\]

be a complete nonterminal fixed-order state produced by the v7.2 arbitrary-flow single pop. Assume:

1. the live prescribed parent central value is one co-root `Q_m`;
2. the two crossed root sheets and the literal parent topology have passed the exact current graph-category test, with every failed test already returned as a named terminal;
3. all ten support-pair switches, missing-index migrations, active crossed NNIs and one-atom coherence macros have been interpreted with the complete all-index state fields;
4. the state has not already reached parent success, a cap-compatible `K_i` state, or a named cut/bounded terminal.

Then there is a finite source-faithful same-order history using only:

- ordinary root-valued `2--2` NNIs;
- legal closed support-component switches;
- exact route/cut/bounded terminal consumers;

and using no `2--0` cancellation and no lower-order root-flow call, which ends in exactly one of:

1. a separating rescue channel followed by the literal prescribed-parent NNI;
2. a cap-compatible `K_i` route/profile state;
3. a named cyclic `2/3/4`-cut or bounded terminal;
4. a root flow on the literal prescribed-parent topology.

Equivalently, the prime nonterminal part of the complete all-index state graph has no closed SCC disjoint from all four absorbing outputs.

---

## 2. Reduction of a hypothetical closed SCC to a full-channel lock

Suppose a prime nonterminal SCC `C` is disjoint from all four absorbing outputs.

At every state of `C`:

- no rescue channel separates the marked parent roots, since its component switch would rootify the parent;
- no rescue channel changes the prescribed oriented route, since that is the Phase-B route escape;
- no boundary/profile is in `K_i`;
- no category flag is terminal.

Therefore every state in `C` is a complete oriented DDD full-channel lock relative to its current marked disjoint roots, current missing index and exact route orientation.

The all-index migrations do not invalidate this statement. They merely replace the displayed ordered data by another co-root frame and require recomputation of

\[
(m,\pi,\sigma,\mathcal H,\kappa,\tau,P,\alpha).
\]

Choose one physical rescue channel at one state. The fixed-channel frame of `DDD_LOCK_H14_SWITCH_INVARIANT_DESCENT_THEOREM_V1.md` transports it through every nonexit switch and root NNI.

---

## 3. Fixed-channel descent inside the SCC

In the transported frame the marked roots, missing support and selected channel are

\[
12,34,5,14.
\]

The vertex weight is

\[
\begin{array}{c|cccccccccc}
T&123&124&125&134&135&145&234&235&245&345\\
\hline
\xi(T)&1&0&1&0&0&0&1&2&1&0,
\end{array}
\]

and

\[
\Xi(S)=\sum_v\xi(\Delta_v).
\]

Three exact facts control the proof.

### A. Physical component invariance

For every nonexit closed `H_14` component switch,

\[
\Xi(S^Z)=\Xi(S).
\]

This includes every exterior vertex of the switched component and the frame transport when both marked roots migrate. It is the point at which the old `Omega` argument failed and the new proof is exact.

### B. Every bad type supplies strict descent

Every lock contains one of

\[
123,234,125,245.
\]

At its selected internal root `23` or `25`:

- a distinct neighbouring triangle gives one of six ordinary NNIs, each with `Delta Xi=-2`;
- an equal neighbouring triangle gives zero or one root branch swap, one legal `H_14` component switch, and one of the same six ordinary NNIs, again with total `Delta Xi=-2`.

Every category or route failure along the macro is already an absorbing output.

### C. Bad-free route contradiction

If the four bad types were absent, every `H_14` path beginning at a boundary `12` occurrence would consist only of type-`124` vertices and roots `12,24`. It could never reach a boundary `34` occurrence, contradicting the oriented full-channel route.

Thus every nonabsorbing macro within `C` lowers the nonnegative integer `Xi` by exactly two. A closed SCC cannot contain an infinite strict descent. Contradiction.

This proves the theorem.

---

## 4. Exact source movie alphabet

Every strict macro has one of two forms.

### Distinct-neighbour form

```text
one category-tested ordinary root NNI
    -> parent / K_i / terminal / locked Xi-descent
```

### Equal-neighbour form

```text
zero or one equal-face root branch-swap
    -> one legal closed H_14 component switch
    -> one category-tested ordinary root NNI
    -> parent / K_i / terminal / locked Xi-descent
```

All states are complete labelled source states. The movies retain:

- the literal prescribed-parent topology `P`;
- the cap block and oriented route field;
- stable exterior dart identities;
- current missing-index and trace-assignment fields;
- support transport;
- the stored-prefix identity map `alpha`.

No coefficient-only transition is used.

---

## 5. Why both defects in the scope correction are absent

### Exterior component energy

The proof does not compare source and target minima of `Omega`. The new weight is invariant under the actual transposition on every vertex of the selected component. Exterior contributions vanish individually rather than being assumed to cancel.

### Zero overlap

The equal-face macro begins at a root endpoint, switches one complete root-valued component, and ends with an ordinary root NNI. The local pairs are

\[
123+234
\quad\text{or}\quad
125+245,
\]

not a quadruple-equality zero insertion. No co-root track or endpoint collar is required.

---

## 6. Effect on `FC-PURE-NNI-ESCAPE`

The original DDD-lock formulation is an immediate special case:

\[
\boxed{\texttt{FC-PURE-NNI-ESCAPE holds at RL authorial level}.}
\]

The stronger all-index formulation also holds because the transported channel frame follows common-component migrations without freezing the initial missing index or boundary word.

The verified `G_14` movie remains a model case, but it is no longer a provider for universality. The universal provider is the switch-invariant rank `Xi`.

---

## 7. Effect on v7.2

The theorem closes the exact proof-development blocker

\[
\texttt{AC-PD-V7.2-PURE-NNI-TARGET-REINSERTION}
\]

at Research Lead authorial level.

Combined with the already retained v7.2 units, the fixed-order return is now:

```text
actual smaller target
    -> arbitrary lower target root flow
    -> one inverse pop
    -> root / one-atom normalization
    -> complete all-index horizontal state
    -> fixed-channel Xi escape from every nonterminal SCC
    -> literal prescribed-parent root state or exact terminal
    -> state-walk seam/run return through the stored pure-NNI prefix
```

Consequently the RL branch again supplies a complete authorial candidate for ordinary strong-induction closure:

\[
P_{<N}\Longrightarrow P_N.
\]

This is a research theorem/candidate boundary only. PDL must reconstruct the repaired fixed-channel proof and the end-to-end v7.2 dependency chain before any independent audit or theorem acceptance.

---

## 8. Dependency ledger

### Used

- exact root/support arithmetic in `R_5`;
- complete all-index state tuple and move contracts;
- support-component switches as genuine closed root-flow involutions;
- the equal-face three-matching route-or-split lemma;
- ordinary root-NNI category testing;
- Phase-B separating-channel and `K_i` consumers;
- exact cut/bounded terminal ledger;
- literal cap, dart and prefix identities.

### Not used

- an actual equal-face `2--0` cancellation;
- a lower-order call during fixed-order return;
- the quarantined `Omega` plateau-orbit inequality;
- orbit minima or finite-state distance;
- a zero/co-root atom in the lock escape;
- generic Kempe/root/NNI connectivity;
- `Q_N`, `M_N`, `d_N`, nested bubbles or terminal frames;
- topology-only spanning-tree reachability.

---

## 9. Reproducibility and quantitative bound

The finite local certificate is the ten-entry `xi` table, its `tau_14` invariance, and the six strict NNI rows. Its canonical SHA-256 digest is

`b901ef3bfb41803e48e8a17efd9eb37c5fe48bd37ea0e771fd2f5ffed1a9a25a`.

At fixed order `N`,

\[
0\le\Xi\le2N,
\]

and every nonabsorbing strict macro lowers `Xi` by two. Hence at most `N` strict macros occur before absorption.

---

## 10. Required downstream reconstruction

PDL should reconstruct, in this order:

1. uniqueness and transport of the fixed `H_14` frame;
2. component-wise `xi` invariance in the unmarked and common-marked cases;
3. the six exhaustive distinct-neighbour rows;
4. the four equal-neighbour root-only macros;
5. the bad-free `12/24` route contradiction;
6. exact category consumers and literal state-field preservation;
7. the all-index SCC exclusion;
8. insertion into the v7.2 fixed-order return and ordinary-induction DAG.

Independent audit must subsequently recompute the same items and verify that the horizontal-to-ambient interface is exhaustive.

---

## 11. Final Research Lead disposition

\[
\boxed{
\texttt{[READY-FOR-PDL-REPAIR AC-RL-PURE-NNI-02]}}
\]

The exact repair is the fixed-channel switch-invariant theorem, not the quarantined `Omega` plateau master attempt.

### Assurance boundary

Completed at RL authorial level:

- `DDD-PLATEAU-PRODUCTIVE-ROW-ESCAPE` by a stronger theorem;
- `FC-PURE-NNI-ESCAPE`;
- `FC-PURE-NNI-ALL-INDEX-AMBIENT-ESCAPE`;
- the exact v7.2 target-reinsertion repair interface.

Still required:

- PDL reconstruction;
- independent mathematical audit;
- downstream Director, Curator and Owner dispositions.

No established five-support/five-CDC theorem, Lean theorem, canonical movement, manuscript, release, tag, arXiv, DOI, peer-review or publication status is claimed.
