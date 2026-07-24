# First-cancellation single-pop target-topology scope correction

## Research Lead correction v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `f4b92f6eb11893f2161560ac898222fa38525f67`

**Corrects:**

- Section 6 and the first sentence of Section 7 of `FIRST_CANCELLATION_TARGET_CAP_TERMINALISATION_V1.md`;
- any reading of Section 5 of `ROOT_NORMALIZED_CONTEXTUAL_TRANSFER_MASTER_V7_FIRST_CANCELLATION_RETURN.md` under which an equality or good-disjoint alternative insertion is literally the original predecessor topology.

**Status:** exact scope correction. The single inverse cancellation produces a predecessor-**order** contextual state with a recorded target topology. Only the distinct-intersecting row necessarily inserts the original equal-face pair on the original predecessor topology. The equality and good-disjoint rows may insert an equal-face pair in a neighbouring five-leaf placement. They are root-valued, same-order source states with the same complete exterior boundary, but need not be the literal original predecessor graph. The missing-index row is likewise one standard atom on a same-order alternative local topology. The fixed-order target arborescence and R2.4--R2.6 consumer are precisely what restore the required predecessor topology before the pure source prefix is crossed.

No theorem status is promoted.

---

## 1. Exact output type of one inverse cancellation

Let

\[
\widehat G^-
\]

be the smaller target cap closure at the first cancellation and let

\[
\widehat G_s
\]

be the required predecessor target topology.

Choose any root flow on `\widehat G^-` and evaluate the roots `a,b` on the two stored output lineages.

The output is a complete contextual state

\[
X
]

at vertex order `N`, together with the target field

\[
\operatorname{target}(X)=\widehat G_s.
\]

Exactly one of:

1. **Original root insertion.** If `a,b` are distinct and intersecting, the original equal-face pair inserts root-valuedly. In this row the source topology of `X` is literally `\widehat G_s`.
2. **Equality alternative insertion.** If `a=b`, the five-leaf borrowing theorem gives a root-valued alternative inverse insertion. The source topology of `X` may differ locally from `\widehat G_s`, while its complete five-leaf exterior incidence word is identical.
3. **Good-disjoint alternative insertion.** If `a\perp b` and a good borrow exists, the source topology of `X` is a root-valued neighbouring insertion topology with the same complete exterior boundary.
4. **Missing-index atom.** If `a\perp b` and the borrow is missing-index, `X` carries exactly one normalized `(Q_i,Q_j,ij)` atom on a same-order local topology with the same exterior boundary.
5. **Local terminal.** A loop/parallel/insufficient-borrow/separator identification gives one exact bounded or small-cut outcome at the current target level.

Thus the correct trichotomy is

\[
\boxed{
\begin{array}{c}
\text{root-valued predecessor-order contextual state with target }\widehat G_s,\\
\text{one-atom predecessor-order contextual state with target }\widehat G_s,\\
\text{exact current-target terminal}.
\end{array}}
\]

It is not

\[
\text{root or atom literally on }\widehat G_s
\]

in every row.

---

## 2. Required same-order normalization before source-prefix inversion

From the contextual state `X`, first run the target-rooted fixed-order normalization to the required topology `\widehat G_s`.

- In a root sector, use the ordinary target topology arborescence.
- A forced NNI whose old diagonal is zero uses the alternative crossed root NNI.
- A forced NNI whose old diagonal is a co-root creates/retains the unique standard atom.
- Critical overlaps preserve the one-atom bound.
- R2.4--R2.6 consume every closed, normalized-open, or repeated-endpoint singular track.
- A route event gives a `K_i` cap lift.
- A category/bounded event is consumed by its exact theorem.

Only after the required predecessor topology has been reached does one cross the next source NNI of the pure prefix.

Equivalently, each prefix stage has two coordinates:

\[
(\ell,d_{\rm top}),
\]

where:

- `ell` is the number of source NNIs still to invert;
- `d_top` is the current fixed-order distance to the predecessor topology for that stage.

Fixed-order normalization terminates at constant `ell`; crossing the source NNI lowers `ell` by one.

No graph-order recursion occurs.

---

## 3. Corrected pure-prefix theorem

### Theorem 3.1

Let

\[
T_0\to T_1\to\cdots\to T_s
\]

be a finite source history consisting only of internal `2--2` NNIs with fixed ordered cap boundary.

Given at the order of `T_s` either:

- a root-valued complete contextual state; or
- a complete state with one normalized co-root atom;

and with `T_s` recorded as the target topology, the inverse contextual procedure alternates:

1. same-order target normalization to the required predecessor topology;
2. crossing exactly one source NNI.

It finitely produces a root flow on the original cap target, or one exact cap/small-cut/bounded/outer-shell construction which produces such a flow.

No cancellation call is opened.

---

## 4. Consequence for v7

The first-cancellation simplification is unchanged.

At the unique order-lowering step:

1. solve the actual child target cap closure by lower `P`;
2. perform one actual inverse-cancellation insertion;
3. regard its output as a predecessor-order contextual state with target `\widehat G_s`;
4. normalize at fixed order;
5. cross the pure NNI prefix stage by stage.

The alternative insertion does not need to preserve the original local predecessor topology pointwise. It needs only:

- the same vertex order;
- the same complete exterior incidence boundary;
- a root or one-atom state;
- the recorded target topology;
- fixed-order R2.4--R2.6 termination.

These are exactly the proved inputs.

---

## 5. PDL audit points

PDL must distinguish:

1. original insertion topology;
2. equality alternative topology;
3. good-disjoint alternative topology;
4. missing-index one-atom topology;
5. the required predecessor target topology.

It must prove literal exterior-boundary equality, then invoke target normalization. It must not identify all five topologies merely because they cancel to the same smaller neighbourhood.

---

## 6. Trust boundary

### Exact here

- corrected output type of the single pop;
- distinction between source topology and target topology;
- same-order target normalization before prefix inversion;
- lexicographic `(ell,d_top)` organization without order recursion;
- preservation of the v7 first-cancellation simplification.

### Still required

- PDL reconstruction;
- independent audit of each five-leaf insertion row and fixed-order target normalization.

### Not claimed

- PDL completion;
- independently accepted cap restoration;
- established five-support/five-CDC theorem;
- Lean, Curator, manuscript, release, or publication status.
