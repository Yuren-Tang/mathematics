# Support-pair switches lift through a weld or return one central first-exit atom

## Research Lead source-pop theorem v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`

**Parents:**

- `WELD_B_ORBIT_SWITCH_AND_MOBILE_MARK_GRAPH_V1.md`;
- `WELD_RELATION_FIRST_EXIT_V1.md`;
- `WELD_MARK_EQUAL_FACE_OVERLAP_V1.md`;
- `TWO_BOUNDARY_KEMPE_COMPATIBILITY_AND_DEFECT_EXCHANGE_V1.md`.

**Status:** exact source-level lift/pop theorem for one lower-order support-pair component switch at an inverse-weld boundary. The local formula is universal. If the lower-order switch toggles the two reconnecting output roots with bits `epsilon_p,epsilon_q`, then after inverse insertion the central edge must carry

\[
r'=p'+q'=r+(\epsilon_p+\epsilon_q)h.
\]

If `r'` is a root, the switched edges form a genuine union of support-channel components in the expanded graph and the pop is fully root-valued. If `r'` is zero or a co-root, the child switch has nevertheless been completed legally on the lower-order graph and inverse insertion returns exactly one central zero/co-root atom on the parent graph. No second defect, component-identification assumption or new coefficient type is needed.

This supplies source fidelity for support-switch successful pops and first-`A/C` pops. It does not by itself prove the parent continuation rank or the complete nested return theorem.

---

## 1. One weld triangle

Let the two lower-order reconnecting output edges carry distinct intersecting roots

\[
p,q\in R_5,
\qquad
p+q=r\in R_5.
\]

Inverse equal-face insertion splits both output edges and inserts two vertices joined by the central root `r`. Both new vertices carry the root triangle

\[
\boxed{(p,q,r).}
\]

Retain the four ordered output incidences throughout.

Fix one support-pair channel

\[
h\in R_5.
\]

On the lower-order graph, choose any union of connected components of the ordinary `h`-eligible even subgraph and switch it. Let

\[
\epsilon_p,\epsilon_q\in\mathbf F_2
\]

record whether the selected union contains the marked output edge `p` or `q`.

The switched output roots are

\[
\boxed{
p'=p+\epsilon_p h,
\qquad
q'=q+\epsilon_q h.
}
\]

Because the lower switch is legal, every changed marked root remains in `R_5`.

---

## 2. The forced central value

After splitting the switched output edges, Kirchhoff at either inserted vertex forces the central value

\[
\begin{aligned}
r'
&=p'+q'\\
&=p+q+(\epsilon_p+\epsilon_q)h\\
&=\boxed{r+(\epsilon_p+\epsilon_q)h}.
\end{aligned}
\]

This equation is independent of the global component decomposition.

### Lemma 2.1 — complete relation test

The inverse insertion after the switch is:

1. root-valued exactly when `(p',q')` is in `B`;
2. zero-valued exactly when `p'=q'`;
3. co-root-valued exactly when `p'` and `q'` are disjoint.

### Proof

The central edge is the sum `p'+q'` of two roots. For two roots in `E_5`, that sum has weight:

- two when they are distinct intersecting;
- zero when they are equal;
- four when they are disjoint.

These are exactly the three stated cases. ∎

No weight-one, weight-three or weight-five value can occur.

---

## 3. Root-valued lift when `B` is preserved

Assume

\[
r'\in R_5.
\]

Consider the expanded graph after inverse insertion. Mark every edge whose value differs from the pre-switch expanded state by `h`:

- outside the inserted pair, use exactly the selected lower-order component union;
- on the four split output half-edges, use the same bit as their lower-order parent edge;
- use the central edge exactly when
  \[
  \epsilon_r=\epsilon_p+\epsilon_q=1.
  \]

### Lemma 3.1 — local evenness at the inserted vertices

At each inserted vertex the number of marked incident edges is even.

### Proof

The three local toggle bits are

\[
\epsilon_p,
\qquad
\epsilon_q,
\qquad
\epsilon_r=\epsilon_p+\epsilon_q,
\]

whose sum in `F_2` is zero. ∎

Every marked edge is `h`-eligible because its old and new values are roots differing by `h`. Outside the inserted pair, the marked set was already an even union of complete `h`-components. Lemma 3.1 supplies evenness at the two new vertices.

Hence the marked set is an even subgraph of the expanded cubic graph. Every even subgraph is a disjoint union of cycles, equivalently a union of connected components of the `h`-eligible subgraph.

### Theorem 3.2 — root support-switch lift

If the lower-order switch preserves the weld relation `B`, then it lifts to an ordinary root-valued `h`-component switch on the predecessor-order expanded graph.

The lifted switch:

- realizes exactly the prescribed changes on every lower-order exterior edge;
- preserves the four ordered weld incidences;
- changes the central root from `r` to `r'` when necessary;
- creates no zero or co-root edge;
- uses no assumption that the channel-component partition is unchanged by insertion.

### Important special cases

1. **Both or neither marked output switched.** Then `epsilon_p=epsilon_q`, so `r'=r`; the central edge is unchanged.
2. **Exactly one marked output switched, but the other root is not `h`-eligible.** Then the central root is `h`-eligible and switches with the marked output; the pair may remain in `B`.
3. **Component merger or splitting under insertion.** It is harmless: the local parity assignment joins only strands carrying the same switch bit, so it still descends to complete expanded components.

---

## 4. First `A/C` exit

Assume the lower-order component switch is legal but the switched pair leaves `B`.

By Lemma 2.1, the forced central value is

\[
\boxed{r'=0\quad\text{or}\quad r'=Q_i.}
\]

All lower-order edges remain root-valued because the child component switch was legal. Splitting the two output edges preserves those roots on all four half-edges. The only non-root value is the inserted central edge `r'`.

At both inserted vertices,

\[
p'+q'+r'=0,
\]

so the complete predecessor-order coefficient assignment is still an `E_5` flow.

### Theorem 4.1 — support-switch first-exit pop

A legal lower-order support-pair component switch which first changes the weld relation from `B` to `A` or `C` returns, after inverse insertion, exactly one parent-order first-failure atom:

\[
\boxed{
A\longmapsto 0,
\qquad
C\longmapsto Q_i.
}
\]

Every other edge is a root and every ordered exterior/cap incidence is unchanged.

The child switch has already been performed. Therefore the returned atom belongs after that child-history step, not before it.

---

## 5. Exact common-eligibility table

For the standard weld triangle

\[
p=ab,
\qquad
q=ac,
\qquad
r=bc,
\]

the three channels eligible on both `p` and `q` are

\[
\boxed{bc,\ ad,\ ae.}
\]

If exactly one marked output is switched, then:

\[
\begin{array}{c|c|c}
h&r+h&\text{weld outcome}\\
\hline
bc&0&A\\
ad&Q_e&C\\
ae&Q_d&C.
\end{array}
\]

Thus the earlier `1 A + 2 C` census is recovered directly from the central-value formula.

The theorem is more general than this table: it also covers channels eligible on exactly one marked root, for which the central edge switches root-valuedly and `B` is preserved.

---

## 6. Relation to the crossed two-boundary kernel

Suppose the child support switch is chosen to repair one outer `A/C` obligation while the internal weld pair is initially in `B`.

`TWO_BOUNDARY_KEMPE_COMPATIBILITY_AND_DEFECT_EXCHANGE_V1.md` gives:

1. in every compatible component partition, choose expanded component switches which repair the outer pair and keep the weld in `B`; Theorem 3.2 makes the parent pop root-valued;
2. in the unique crossed partition, any one-sided outer repair switches exactly one weld output; Theorem 4.1 places the unique defect on the central parent weld edge.

Hence the crossed kernel has a complete source-level pop interpretation:

\[
\boxed{
(\text{child outer defect},\text{parent weld regular})
\longrightarrow
(\text{child solved},\text{parent central atom}).
}
\]

No second atom survives.

---

## 7. Continuation semantics

The numerical child-history step has been consumed before the pop:

- the lower-order component switch is a completed legal root move;
- ordered output incidences are current data, not reconstructed genealogy;
- the inverse insertion is then evaluated on the actual switched roots `p',q'`;
- the parent receives either a root expansion or one central atom.

Thus this theorem supplies the physical content required for:

- a successful child pop;
- a first-`A/C` child pop;
- the one-defect exchange branch of the two-boundary theorem.

A global stack theorem must still decide how the returned parent atom is ranked relative to the stored parent continuation. The present theorem does not identify a child prefix length with a parent prefix coordinate.

---

## 8. Source-category boundary

### Root-valued branch

Topology is unchanged by a support switch. Every edge remains nonzero. Connectivity, cubicity and looplessness are unchanged; a connected graph carrying a nonzero group flow on every edge is bridgeless.

### First-exit branch

The topology is the ordinary inverse-insertion expansion. The unique non-root central edge may be zero or co-root and is retained as the established local atom. All other edges remain roots. Loop/parallel or separator degenerations at the insertion boundary are the already accepted bounded/category exits.

---

## 9. Assurance boundary

### Exact here

- the universal central formula `r'=r+(epsilon_p+epsilon_q)h`;
- root-valued component-switch lifting whenever the switched pair remains in `B`;
- independence from preservation of the lower component partition;
- exactly one central zero/co-root atom at first `B -> A/C` exit;
- source-level interpretation of the crossed two-boundary defect exchange;
- completion of the child support-switch step before pop.

### Not claimed

- a numerical parent-frame rank for the returned atom;
- the exchange-frame pop theorem in its global continuation form;
- mark-consuming cancellation continuation normalization;
- a complete finite mixed-state local rank;
- R2.7 completion, cap restoration or universal five-CDC;
- PDL reconstruction, independent audit, Lean verification, manuscript integration, curation, release, arXiv, DOI, peer review or publication.
