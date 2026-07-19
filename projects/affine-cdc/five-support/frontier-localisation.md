# The current five-support frontier: localisation and composition

## 1. What is closed and what is not

The active source surface contains complete theorem blocks for:

- existence and structure of compatible eight-support root lifts;
- exact global formulations of five-support covers;
- the fixed-plane lifting obstruction;
- the root-lift/surface/dual correspondence;
- the componentwise half-cube criterion;
- large classes of target links and marked obstruction cores;
- gauge/Petrial occurrence arrangements;
- three-cut gluing and the full ten-state four-edge interface;
- routing reduction to Type T and Type H;
- Tait elimination of the soluble Type H branch;
- BBD simultaneous linearisation and defect geometry;
- atom route-lock, rank-two escape, and the full-rank curvature dichotomy;
- common-cut circuit localisation;
- the singleton/transition/quartic trichotomy;
- the quotient Tait-phase model and Kempe sheet differences;
- pairwise ribbon transition skeletons;
- the canonical quartic terminal nucleus and abstract split-or-peel recursion.

The missing result is not another local identity or a larger census. It is a strict **physical localisation/composition theorem** converting the residual algebraic split or nucleus peel into a smaller graph, a bounded four-pole transfer, or an escaping state.

## 2. The global quantifier

For a bridgeless cubic graph `G`, let `\mathfrak B(G)` be the set of nowhere-zero Fano flows whose whole compatible root-lift fibre is bad.

The global five-support statement is equivalent to

$$
\boxed{
\mathfrak B(G)
\ne
\operatorname{NZFlow}(G;\mathbf F_2^3)
}
$$

for every bridgeless cubic `G`.

A proof may succeed by either route:

1. **escape:** find one Fano flow and one gauge state with
   $$
   T_g^{(1)}\longrightarrow\mathscr A_5;
   $$
2. **decomposition:** show that every horizontally and vertically persistent bad region forces an interface across which smaller five-support covers glue.

Neither route has been completed in full generality.

## 3. The source-composition gap

For a fixed flow and a finite marked obstruction library `\mathscr L`, the bad locus is a finite affine arrangement

$$
\operatorname{Bad}_f(\mathscr L)
=
\bigcup_C A_C
\subseteq B_f.
$$

This finite layer is explicit, but two bridges remain distinct:

1. **target completeness:** compress all compatible non-homomorphisms into a controlled certificate language;
2. **source composition:** turn persistent certificates into strict progress on the original graph.

The present sharp frontier is source composition. Enlarging the target census before the source mechanism requires it is not the recommended order.

## 4. Four-pole routing frontier

After three-cut reduction, a cyclic four-edge cut is governed by two shore profiles in the ten-state boundary alphabet. Cap forcing and Kempe closure reduce every abstract disjoint pair to deterministic routing. Uniform routing is eliminated. The residual automata are

$$
P_5\mid P_5
\qquad\text{or}\qquad
P_4\mid C_3.
$$

### Type T target

Prove that the acyclic unique-routing policy forces nested terminal linkages, a serial decomposition, a smaller separator, or a bounded replacement with an explicit decreasing measure.

### Type H target

The soluble zero-norm branch is eliminated by Tait escape. The remaining data must be converted into strict progress through ambient translation, an empty edge or vertex relation, component holonomy, a zero network, or co-root defect structure.

The family theorem still needed is:

> if every physical lift is obstructed, all obstruction signatures share one geometric witness that yields decomposition or orbit escape.

## 5. Defect-forest pruning

The canonical or energy-minimal `E_5` flow has a defect forest with equality leaves, one-factor leaves, co-root paths, zero branches, and all-zero branches. Co-root strips carry an `L(\mathrm{Petersen})` state walk together with a side-root output word.

The required pruning theorem should prove one of:

1. an equality leaf or zero network gives a serial four-pole factor or bounded replacement;
2. a co-root strip endpoint admits one of its two Petersen root resolutions in a composition-safe manner;
3. a repeated enriched Petersen state yields a replaceable segment with matching side semantics;
4. failure of all reductions produces the unique DDD `D_8` affine class.

State repetition without matching side semantics is insufficient.

## 6. The route-locked atom endpoint

A nondegenerate co-root atom has two crossed root resolutions. If one full challenge takes a crossed route, the atom becomes root-valued. If both resolutions are blocked, every challenge uses the original pairing and the safe orbit is `K_{2,4}`.

At a locked `C`-state, quotienting produces a full-rank-or-rank-two `\mathbf F_2^3` flow with all terminal values equal.

The rank-two sector is closed by Tait escape. The residual endpoint has two full-rank branches.

### 6.1 Nonflat branch: exact circuit localisation

For `\Omega(c)\ne0`, choose a support-minimal witness

$$
\eta\subseteq E_g.
$$

It is simultaneously a cut in all four scalar circuit partitions and has odd terminal parity. The active common-cut theorem proves that `\eta` is a curvature-odd circuit in the closed-component incidence matroid and that exactly one of the following holds:

1. `|\eta|=1`, a bounded enriched `g`-edge atom;
2. one closed scalar component meets `\eta` in two edges, giving a marked transition interval;
3. `|\eta|=4k+1`, giving a quartic near-resolution core.

The scalar-common-cut witness need not be a cut in the underlying four-pole. That earlier expectation is false.

### 6.2 Physical enrichment of the quartic core

For the quartic branch, quotient by `\langle g\rangle` and write

$$
c(e)=\sigma(e)g+\bar c(e),
\qquad
\bar c(e)\in\mathbf F_2^2.
$$

Then:

- the zero set of `\bar c` is exactly `E_g`;
- away from `E_g`, `\bar c` is a Tait colouring;
- the binary phase `\sigma` reconstructs the full flow;
- the four scalar sheets form an affine plane;
- their three nonzero differences are quotient Kempe cycle systems;
- every endpoint selector is affine;
- every `g`-edge has one of nine ordered endpoint labels;
- aligned and crossed edges have the exact three-switch signatures
  $$
  (0,0),(1,1),(1,1)
  $$
  and
  $$
  (0,1),(1,0),(1,1),
  $$
  respectively.

For every pair of sheets, the witness edges form a connected bipartite ribbon transition skeleton with two terminal leaves, block degrees four, cycle rank `2k`, and a terminal Euler trail.

### 6.3 Canonical terminal nucleus

Let `X=\eta`, and let `e_i` be the unique terminal witness edge in sheet `i`. For each sheet, sum all four-element closed-component block vectors:

$$
s_i
=
1_X+e_i.
$$

The four vectors `s_i` span a canonical nondegenerate minus-type four-space

$$
S\cong O^-(4,2).
$$

Its five nonzero singular points

$$
s_0,s_1,s_2,s_3,s_\infty
$$

and ten anisotropic pair sums form an intrinsic `E_5/K_5` geometry. The fixed route matching on the four sheet labels has coordinate stabiliser

$$
D_8\le S_4.
$$

The odd side-word quotient is canonically carried by

$$
\boxed{
S/s_\infty^\perp\cong\mathbf F_2.
}
$$

Thus curvature is no longer merely known to have the same one-dimensional representation type as the DDD exception. It has a canonical incidence-level `D_8` carrier inside the same minus-type geometry. The remaining open step is the physical comparison with the DDD cocycle.

### 6.4 Split-or-peel theorem

In one sheet, the other three omitted points are distributed among its four-element blocks in exactly one of the patterns

$$
3,\qquad2+1,\qquad1+1+1.
$$

A block containing one or two of those terminal points projects to an anisotropic root of the canonical nucleus.

Hence every abstract quartic core satisfies exactly one of:

1. **root-exposed split:** some sheet has type `2+1` or `1+1+1`, exposing two or three root-projected blocks;
2. **concentrated peel:** every sheet has type `3`; if `k\ge2`, the four distinguished blocks peel off the canonical nucleus and the remaining blocks form a quartic witness design of level `k-1`.

The five-point nucleus is the recursion base, and concentrated extension is the exact inverse construction. The previously unbounded quartic ladder is iterated nucleus extension.

This gives the strict abstract decrease

$$
\boxed{k\longmapsto k-1}
$$

but not yet strict progress in the original graph.

### 6.5 Immediate physical theorem

The current central target is:

$$
\boxed{
\begin{array}{c}
\text{root-exposed quartic split}
\quad\text{or}\quad
\text{concentrated }D_8\text{ nucleus peel}
\\[2mm]
\Downarrow
\\[2mm]
\text{bounded four-pole transfer, smaller separator,}\
\text{transition-matroid split, root escape, or physical }D_8\text{ factor.}
\end{array}
}
$$

For the concentrated branch, one must show that the abstract peel is respected by:

- cyclic orders on the scalar components;
- the three quotient Kempe cycle systems;
- aligned/crossed endpoint labels;
- intervening non-`g` paths and phases;
- the fixed `12\mid34` terminal route.

If these data descend, induction on `k` becomes available. If they do not descend, the failure should expose a bounded crossed interface and hence the DDD class.

### 6.6 Flat branch

If `\Omega(c)=0`, there is an eight-state potential

$$
p:V(Q)\to\mathbf F_2^3
$$

with

$$
p(u)+p(v)\in\{0,c(e)+g\}.
$$

Edges between distinct potential fibres have forced colours; same-fibre subgraphs may carry unbounded internal semantics. The needed theorem must extract a finite interface and prove a proper split, smaller separator, repeated-fibre replacement, or bounded transfer state.

Flatness is structure, not yet solution.

## 7. Horizontal escape or coherent bad-flow component

The calibrated laboratories show:

- a graph may be easy while some fixed flows are hard;
- a snark may have every Fano flow vertically soluble;
- a graph may have bad flows with many one-step exits.

The unresolved graph-level possibility is a horizontally closed component of wholly bad flows, or ultimately a graph for which every Fano flow is bad.

A useful theorem form is

$$
\boxed{
\text{bad-flow component}
\Longrightarrow
\text{good boundary edge}
\quad\text{or}\quad
\text{coherent decomposition certificate}.
}
$$

The certificate must survive simultaneous changes of gauge code, surface, and obstruction library under horizontal switches.

## 8. Full-cap and four-pole realizability

The abstract four-edge state universe is closed, but realizability by arbitrary cubic four-poles is not.

Two concrete targets remain:

1. **full-cap-profile theorem:** every admissible shore contains one complete `\mathcal K_i`;
2. **realizability classification:** determine which Kempe-stable abstract profiles occur beyond the small exhaustive census.

A counterexample should be converted into transfer data rather than added as an isolated profile.

## 9. Target-side open boundary

The target theory is complete for dominating-clique rank at least two. The first unresolved link is rank one:

$$
H\longrightarrow L(K_5).
$$

More generally, compatible dual triangulations may contain non-dominating obstructions not covered by the current library. The flower `J_5` shows that clique-only theory is insufficient.

The target programme is:

1. classify common-neighbour and iterated-link capacities;
2. find structural certificates for non-homomorphism of closed triangulations;
3. determine whether every compatible obstruction has a bounded marked certificate or a canonical decomposition.

## 10. Secondary open programmes

These remain mathematically meaningful but are not the current closure bottleneck.

### 10.1 Planar Fano-line flattening

A Tait colouring is a constant Fano line field. Cycle switches pivot local Fano lines. A monotone planar flattening theorem would offer a new Four Colour architecture, but no such theorem is presently known.

### 10.2 Orientable good lifts

The orientable locus is an affine slice of the gauge torsor. An orientable five-support cover yields a nowhere-zero `\mathbf Z_5` flow. Universal orientable lifting would give a strong route to five-flow theory, but it may be stronger than the present theorem requires.

### 10.3 Coefficient holonomy

Rainbow `S_5` monodromy preserves no common affine `\mathbf F_5` structure on support names. This obstructs canonical coefficient transport around the reconfiguration loop, not extraction of a five-flow from one final orientable cover.

## 11. Recommended proof order

The present dependencies suggest:

1. **Physical quartic split-or-peel:** transport the root-exposed split or canonical nucleus peel to the original four-pole.
2. **Singleton and transition composition:** resolve the bounded aligned/crossed atom and two-edge scalar interval.
3. **DDD comparison:** identify the canonical curvature carrier with the physical `D_8` cocycle.
4. **Flat interface:** extract finite transfer data from the eight-state potential.
5. **Forest pruning:** combine atom resolution with the induced defect forest and Petersen transducer.
6. **Four-pole composition:** express the transfer data in the ten-state boundary language and prove strict replacement/gluing.
7. **Horizontal theorem:** force one of these interfaces from a persistent bad-flow component.
8. **Target completeness:** enlarge the certificate library only where the source theorem requires it.

This order follows the sharpest current endpoint and avoids returning to broad census or superseded quotient-only classifications.

## 12. Stop conditions for future consolidation

A future theorem should not be promoted as closing the programme unless it supplies all of:

- exact hypotheses and graph model;
- a valid transfer from the local algebraic object to the original incidence graph;
- a strictly decreasing parameter or an explicit gluing theorem;
- compatibility with componentwise half-cube semantics;
- no reliance on hidden private computation;
- a clear separation from formal, independent-review, and publication status.

## 13. Current conclusion

The mathematical frontier is sharply localized:

$$
\boxed{
\text{abstract quartic localisation now has strict split-or-peel progress;}
\quad
\text{physical composition remains missing.}
}
$$

The immediate task is no longer to bound an arbitrary common-cut witness. It is to make the canonical `O^-(4,2)`/`D_8` nucleus recursion or the root-exposed terminal split visible and composition-safe in the original four-pole.

No active source proves the global five-support cycle-double-cover statement.
