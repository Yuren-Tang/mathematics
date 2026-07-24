# Pure-NNI zero-parent escape in the `(0,2,2)` fibre

## Research Lead master theorem v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workstream:** `AC-RL-PURE-NNI-03`  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `cd1b70931c3aa644782a28be112017dcbba9d83b`

**Primary inputs:**

- `ZERO_PARENT_HEAWOOD_H35_ESCAPE_SOURCE_CERTIFICATE_V1.md`;
- `FIXED_CHANNEL_COMPONENT_CHAIN_ROOT_NNI_THEOREM_V1.md`;
- `ZERO_PARENT_EQUALITY_FIXED_FRAME_LINEAR_RANK_V1.md`;
- the complete zero-parent state/interface returned by PDL at `fee97446...`;
- the exact root-NNI category, cap, route and terminal consumers.

**Conclusion.** `FC-PURE-NNI-ZERO-PARENT-ESCAPE` holds at Research Lead authorial level.  The proof is same-order and source-faithful.  It uses ordinary root NNIs to contract a witnessed physical fixed-channel component chain, then one legal closed support switch and one literal parent NNI.  It uses no `2--0` cancellation, lower-order call, track erasure, finite-state inference, SCC distance, or retired mixed-order machinery.

---

## 1. Complete zero-parent normal form

Let

\[
S=(N,G,\delta,\lambda,\chi,P,\mathfrak B,\kappa,
\mathscr H,\mathfrak a,\tau,\alpha)
\]

be a complete fixed-order state produced by the arbitrary-flow single-pop table in the equality row.

After one support permutation and ordered active-dart relabelling, put

\[
\boxed{
(A,B,C,D)=(13,13,23,23).
}
\]

The two root crossed topologies are

\[
AC\mid BD,
\qquad
AD\mid BC,
\]

both with central root

\[
r=12.
\]

The literal prescribed parent is

\[
AB\mid CD
\]

with central value

\[
13+13=23+23=0.
\]

The complete state retains the literal parent topology, both crossed sheets, the cap block, stable darts, route/profile, graph category, support components, missing-index data and stored-prefix map.

---

## 2. Fixed rescue channel

Choose the physical support pair

\[
\boxed{h=35.}
\]

Both active roots meet `35` once, while the crossed central root `12` is absent from `H_35`.

Delete the interiors of the two active vertices, retaining the four ordered branch semiedges.  Let `R` be the resulting rooted complementary carrier.

### Lemma 2.1 — category-safe carrier connectivity

If `R` is disconnected, one of its components receives at most two of the four active semiedges.  Its attachment to the complete graph is therefore:

- a bridge/singleton attachment;
- an exact two-edge cut; or
- a bounded low-port shore.

These are named category outputs.  Hence every complete prime nonterminal zero-parent state has connected `R`.

---

## 3. Immediate horizontal outcomes

The selected graph `H_35 cap R` has four terminal incidences `A,B,C,D`.  Its physical terminal matching is one of the three perfect matchings.

### Crossed matching

If the physical matching is

\[
AC\mid BD
\quad\text{or}\quad
AD\mid BC,
\]

choose the crossed root sheet with the same local matching, using zero or one active equal-face root branch-swap.

The closed `H_35` system then has two components, each containing one `13` active branch and one `23` active branch.  Switch either component by `35`.  Up to ordered symmetry the word becomes

\[
(15,13,25,23),
\]

and the literal parent NNI has central root `35`.

This is the exact horizontal separating-channel rescue.

### Route/profile or category output

If the current route/profile is cap-compatible, or if either crossed graph/category test returns a named cut or bounded object, use the existing exact consumer.

### Residual full lock

The only nonabsorbed physical matching is therefore

\[
\boxed{AB\mid CD.}
\]

This is the genuine zero-parent full-channel lock: the outside `H_35` paths connect the two equal `13` terminals and the two equal `23` terminals.

The two crossed active NNIs alone do not change this outside matching and are not counted as target progress.

---

## 4. Component-chain escape from the full lock

In the residual lock, `H_35 cap R` has two distinguished terminal paths

\[
P_{13}:A--B,
\qquad
P_{23}:C--D,
\]

and possibly closed channel cycles.  The unique channel-inactive triangle is

\[
I_{35}=124.
\]

Form the connected quotient `mathcal Q_35(R)` whose nodes are:

- nontrivial `H_35` components;
- individual `124` inactive vertices;

and whose edges are witnessed physical non-`H_35` edges.

Choose a shortest physical quotient path

\[
\mathfrak c:P_{13}=X_0,X_1,\ldots,X_ell=P_{23}.
\]

### Theorem 4.1 — strict physical progress

Every nonterminal step before the final connector lowers

\[
\boxed{\Lambda_{35}=\ell}
\]

by one.

- If `X_1` is a `124` vertex, the exact active/inactive root NNI absorbs it into the distinguished path.
- If `X_1` is a closed `H_35` cycle, the exact active/active root NNI or equal branch swap merges it into the path.
- A failed graph/cap/route test is a named absorbing output.

When `ell=1`, the final physical edge joins the two terminal paths.  Its root alternative changes their matching from `AB|CD` to exactly one crossed matching.

### Proof

This is Theorem 5.1 and the zero-parent corollary of `FIXED_CHANNEL_COMPONENT_CHAIN_ROOT_NNI_THEOREM_V1.md`.  Every move contracts the first physical edge of the retained quotient path.  The final active/active root NNI cross-connects two terminal paths and therefore cannot preserve their pairing. ∎

---

## 5. Parent realization after the final connector

Let the new outside matching be `AC|BD` or `AD|BC`.  Choose the equal-face crossed root sheet with the same matching, using zero or one root branch-swap on the active central edge `12`.

The closed `H_35` system now splits into two cycles.  Switch either cycle by `35`.

Exactly one `13` branch and one `23` branch are translated:

\[
13\mapsto15,
\qquad
23\mapsto25.
\]

Hence, after ordered relabelling if necessary, the active word is

\[
(15,13,25,23)
\]

and

\[
15+13=25+23=35.
\]

Perform the literal parent NNI with central root `35`.  The stored topology is exactly `AB|CD`; all stable outside darts and the stored-prefix identity are preserved by the actual source movie.

---

## 6. Universal theorem

### Theorem `FC-PURE-NNI-ZERO-PARENT-ESCAPE`

Every complete category-safe fixed-order state in the zero-parent `(0,2,2)` fibre has a finite source-faithful same-order history using only:

- ordinary root-valued `2--2` NNIs and equal-face root branch swaps;
- one legal closed support-component switch after a crossed outside matching has been exposed;
- exact route/cut/bounded consumers;

and ending in exactly one of:

1. a root flow on the literal prescribed-parent topology;
2. a cap-compatible route/profile state;
3. a named cyclic `2/3/4`-cut or bounded terminal.

No actual `2--0` cancellation and no lower-order root-flow call occurs.

### Quantitative bound

If no earlier output occurs, the number of ambient chain NNIs is at most the initial physical quotient distance

\[
\Lambda_{35}(S).
\]

It is followed by at most:

- one active crossed root NNI;
- one closed `H_35` switch;
- one literal parent NNI.

This bound is witnessed on the source graph.  It is not a finite-state or SCC-distance argument.

---

## 7. All-index and support-permutation fidelity

For a general zero-parent word

\[
(a,a,b,b)
\]

with distinct intersecting roots `a,b`, let

\[
r=a+b.
\]

Choose one support bijection carrying

\[
(a,b,r)
\]

to

\[
(13,23,12).
\]

The remaining two support indices give a physical rescue pair corresponding to `35`.  Transport the complete state, cap, route, dart and prefix data through this support bijection; apply the canonical theorem; transport back.

No initial missing index or literal support name is frozen.  The theorem is about the physical channel and the literal prescribed topology.

---

## 8. Equality rank supplement

The complete-graph linear rank

\[
Z=2N_1+N_2
\]

from `ZERO_PARENT_EQUALITY_FIXED_FRAME_LINEAR_RANK_V1.md` is invariant under the complementary-channel support transpositions and gives a unique decreasing orientation to every distinct root NNI.

In the productive active collar,

\[
123+125\longrightarrow135+235
\]

has strict drop

\[
Z:6\to3.
\]

This is a finite arithmetic certificate and may shorten PDL case checks.  Universal source totality, however, is supplied by the physical component-chain rank, so the proof does not assume that an arbitrary remote equal face is productive.

---

## 9. Mandatory Heawood model

`ZERO_PARENT_HEAWOOD_H35_ESCAPE_SOURCE_CERTIFICATE_V1.md` verifies the issue-#77 movie:

```text
remote equal-face branch swap at 13-14
    -> physical H_35 split
    -> switch 1-2-3-4-13-1
    -> active word (15,13,25,23)
    -> literal parent NNI with central root 35.
```

Its graph-category audit gives cyclic connectivity

\[
6\to5\to5
\]

for the initial, post-remote-NNI and final parent topologies.  It is a model of immediate outside-matching change; the universal proof also covers arbitrarily long connector chains.

---

## 10. Interaction with the co-root audit

Independent audit `AC-AUDIT-XI-01` found that the former arbitrary remote equal-face route-or-split lemma is false.  The zero-parent theorem does not reuse it.

The same component-chain construction also repairs the co-root same-arc defect; this is recorded separately in

`CO_ROOT_XI_EQUAL_NEIGHBOUR_AUDIT_CORRECTION_AND_CHAIN_REPAIR_V1.md`.

Thus the controlling totality provider for both singular fibres is now the physical channel-component chain, while `Xi` and `Z` remain verified local arithmetic shortcuts.

---

## 11. Effect on v7.3

At Research Lead authorial level, the inverse-parent table is now:

```text
co-root / DDD row
    -> fixed-channel marked-arc component chain
    -> route/separation -> literal parent or exact terminal

zero-parent / equality row
    -> fixed-channel terminal-path component chain
    -> crossed outside matching
    -> one switch -> literal parent or exact terminal.
```

Combined with the retained arbitrary-flow single-pop, one-atom normalization, state-walk seam/run coherence and terminal ledger, this restores a complete RL authorial ordinary-induction candidate.

The earlier PDL candidate `fee97446...` is not independently accepted as a full inverse-parent proof because the co-root audit invalidated its equal-neighbour totality step.  PDL must reconstruct both chain corollaries before a new independent audit.

---

## 12. Nondependencies

The controlling proof does not use:

- an equality `2--0` cancellation;
- a lower-order call during fixed-order return;
- the false arbitrary equal-face matching lemma;
- the quarantined `Omega` orbit-minimum theorem;
- `Xi` as an unconditional source-selection theorem;
- track erasure as target progress;
- generic root/NNI connectivity;
- finite-state recurrence or SCC distance;
- `Q_N`, `M_N`, `d_N`, nested bubbles or terminal frames.

---

## 13. Research Lead disposition

\[
\boxed{
\texttt{FC-PURE-NNI-ZERO-PARENT-ESCAPE: CLOSED AT RL AUTHORIAL LEVEL.}
}
\]

Still required:

- PDL independent reconstruction;
- focused independent audit of the component-chain theorem;
- full v7.3 terminal and ordinary-induction integration audit;
- Director and later Curator/Owner dispositions.

No established five-support/five-CDC theorem, Lean theorem, canonical movement, manuscript, release, tag, arXiv, DOI, peer-review or publication status is claimed.