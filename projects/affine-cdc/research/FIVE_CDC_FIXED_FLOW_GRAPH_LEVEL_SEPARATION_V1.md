# Fixed-flow renewal versus graph-level obstruction

**Programme:** `AffineCDC — Research Lead`  
**Status:** exact finite certificates and mechanism-level scope correction; not canonical pending Director review and literature audit  
**Parents:** `FIVE_CDC_UNIVERSAL_RENEWAL_CUBE_TEMPLATE_V1.md`, `FIVE_CDC_UNIVERSAL_SIX_CUBE_MODULE_V1.md`, `FIVE_CDC_FOUR_POLE_KEMPE_CLOSURE_V1.md`, `FIVE_CDC_SMALL_FOUR_POLE_PROFILE_CENSUS_V1.md`

## 1. Purpose

The universal three- and six-dimensional renewal modules were found by fixing a nowhere-zero Fano flow and studying its complete root-lift / gauge-Petrial fibre.

The four-pole programme, by contrast, studies the existence of an arbitrary five-support cycle double cover of the underlying graph.

These are different obstruction levels. This packet makes the separation explicit and verifies it on the thirty-vertex fixed-flow laboratory.

The strongest certificate is:

\[
\boxed{
\text{the thirty-vertex source graph is properly three-edge-colourable.}
}
\]

Consequently it has a three-support cycle double cover. The universal renewal cubes are therefore not graph-level counterexample atoms; they are bad fibres on a graph which already has a much smaller cover through another flow.

## 2. Three obstruction levels

Let `G` be a bridgeless cubic graph.

### Graph level

The graph is bad when it has no five-support cycle double cover at all.

Equivalently, no choice of support labels, Fano flow, root lift, cycle-face embedding, and half-cube map succeeds.

### Fixed-flow level

Fix a nowhere-zero Fano flow

\[
f:E(G)\to\mathbf F_2^3\setminus\{0\}.
\]

The flow is bad when every compatible root lift in its reduced gauge fibre has

\[
T_g\not\longrightarrow\mathscr A_5.
\]

A graph may possess both good and bad Fano flows.

### Fixed-lift level

Fix one root lift `g`. Its dual triangulation may be obstructed even when another gauge-equivalent lift or another Fano flow succeeds.

The renewal modules describe the transition system among fixed-lift obstructions inside one fixed-flow fibre.

## 3. The explicit three-edge-colouring certificate

Order the forty-five source edges as in the fixed certificate. Assign the three labels

\[
01,\qquad02,\qquad12
\]

by the exact sequence recorded in the private verifier.

At every one of the thirty source vertices, the incident labels are precisely

\[
01,\quad02,\quad12.
\]

Thus the assignment is a proper three-edge-colouring.

Define three supports by support index:

- support `0` contains the edges labelled `01` or `02`;
- support `1` contains the edges labelled `01` or `12`;
- support `2` contains the edges labelled `02` or `12`.

At every cubic vertex each support has degree two, and each graph edge belongs to exactly two supports. Therefore these three supports form a cycle double cover.

Padding with two empty supports gives an indexed five-support cover.

### Computational Theorem 3.1

The displayed certificate verifies exactly that the thirty-vertex graph is three-edge-colourable and has a three-support cycle double cover.

No root-lift or half-cube search is needed for this graph-level conclusion.

## 4. Common minimum circuit of the universal three-cubes

The five Fano flows realizing the universal three-dimensional renewal cube each have a unique weight-six gauge word.

Exact regeneration gives the same edge word in all five fibres:

\[
S=\{0,2,13,15,39,40\}
\]

in zero-based certificate edge numbering.

The harmonic quotient is

\[
Q_S\cong2K_3.
\]

Removing `S` splits the source graph into three connected components of sizes

\[
\boxed{22,\quad6,\quad2.}
\]

The vertex sets are recorded by the verifier. Each quotient component has four boundary edges, two to each of the other two components.

Thus the universal cube is driven by one fixed three-four-pole `2K_3` interface shared by all five source flows.

## 5. Unrestricted four-pole profiles

Forget the selected Fano flow and ask for arbitrary five-support boundary covers of the three quotient components.

With one common boundary labelling, their exact complete profiles are:

\[
\boxed{
\Sigma(P_{22})=\mathcal S,
}
\]

\[
\boxed{
\Sigma(P_6)=\mathcal S\setminus\{B_1\},
}
\]

and

\[
\boxed{
\Sigma(P_2)=\mathcal K_1
=\{B_0,B_2,D_0,D_2\}.
}
\]

These are three of the eight profile types in the small four-pole census. Each contains the complete cap set `\mathcal K_1`.

They are not any of the four Kempe-stable mismatch kernels.

Under the explicit graph-level three-edge-colouring certificate, the three component boundary states are

\[
\boxed{B_0,\quad A,\quad B_0.}
\]

The support labels agree on every one of the six intercomponent edges, giving a global cover.

## 6. Scope correction for the universal renewal modules

The universal three-cube has eight fixed-flow gauge states, each with one private dual `K_6`. The universal six-cube has sixty-four fixed-flow states with private point renewal and two redundant `K_4` lines.

These remain valid and useful exact modules. Their interpretation is now sharper:

\[
\boxed{
\text{they model how a poor fixed Fano flow can remain obstructed under all of its gauge Petrials.}
}

They do **not** model an underlying graph for which every Fano flow is bad.

The thirty-vertex graph has:

- the original fixed obstruction flow with two bad lifts;
- five nearby universal-cube bad flows;
- many horizontally adjacent flows having good lifts;
- an explicit proper three-edge-colouring and three-support CDC.

The large horizontal escape boundary is therefore not an incidental numerical feature. It is the mechanism by which a graph-level cover is reached from a bad fixed-flow laboratory.

## 7. Bad-flow set and graph-level counterexamples

Let

\[
\mathfrak B(G)
\]

be the set of nowhere-zero Fano flows on `G` whose entire compatible root-lift fibre is componentwise bad.

Then:

- the renewal modules describe the vertical structure above vertices of `\mathfrak B(G)`;
- connected-cycle switches give horizontal edges between Fano flows;
- a graph-level five-support cover exists as soon as one reachable Fano flow lies outside `\mathfrak B(G)`.

For a genuine graph-level counterexample, every Fano flow must be bad:

\[
\boxed{
G\text{ has no five-support CDC}
\Longrightarrow
\mathfrak B(G)
=
\{\text{all nowhere-zero Fano flows on }G\}.
}
\]

Conversely, a five-support cover assigns five support indices to five distinct points of `\mathbf F_2^3`; taking pairwise differences along edges produces a nowhere-zero Fano flow with a compatible good lift. Hence equality of the bad-flow set with the full flow set is also sufficient for graph-level failure.

Thus graph-level obstruction is an **all-horizontal-states** phenomenon, not merely a closed vertical fibre.

## 8. Revised mechanism map

The complete mechanism now has two orthogonal directions.

### Vertical direction

\[
f
\longrightarrow
B_f
\longrightarrow
\text{partial-Petrial orbit}
\longrightarrow
\text{private }K_6\text{ renewal module}.
\]

This studies one Fano flow.

### Horizontal direction

\[
f
\longrightarrow
f+a\mathbf1_C.
\]

This changes the gauge code, four-pole affine slice, and renewal module. It may leave the bad-flow set.

### Graph-level quantifier

\[
\boxed{
\text{counterexample}
\iff
\text{every horizontal flow state supports only bad vertical fibres}.
}
\]

The decomposition programme and the four Kempe kernels concern this graph-level quantifier. The universal cubes concern individual vertical fibres.

## 9. Relation to four-pole kernels

The four Kempe-stable mismatch kernels remain legitimate candidates for a cyclic four-cut in a graph-level minimal counterexample.

The universal `2K_3` cube does not realize them. Its unrestricted three-component profiles are broad and compatible, and the graph is three-edge-colourable.

Therefore the proposed identification

\[
\text{universal cube}
\stackrel?=\
\text{coupled four-pole mismatch kernel}
\]

is false without an additional **fixed-flow compatibility restriction**.

A correct refined interface would have to distinguish:

1. the unrestricted graph-level profile `\Sigma(P)`;
2. the subset or affine data compatible with a chosen Fano flow and root-lift fibre.

Horizontal switches change the second while leaving the first unchanged.

## 10. Existing mechanism and remaining obstacle

### Now understood

- why the universal cubes can be wholly bad while the graph is easy: the obstruction is fixed-flow relative;
- why horizontal escape is abundant: other flows expose an already existing graph-level cover;
- why the universal `2K_3` components do not match the four abstract kernels: their unrestricted profiles contain full cap sets;
- why decomposition and renewal must not be conflated without tracking quantifier level.

### Remaining graph-level obstacle

A genuine counterexample would require:

1. every Fano flow to belong to `\mathfrak B(G)`;
2. every fixed-flow fibre to renew its private cores completely;
3. horizontal switches never to reach a good fibre;
4. every cyclic four-pole interface to maintain one of the four Kempe-stable mismatches.

This is far more rigid than the existence of one universal cube.

## 11. Refined next targets

### 11.1 Fixed-flow boundary profile

Define a coloured or affine four-pole boundary object

\[
\Sigma_f(P)
\]

recording the root/Fano compatibility data retained by one fixed flow. Determine how its projection to ordinary `\Sigma(P)` loses the renewal obstruction.

### 11.2 Bad-flow reconfiguration graph

Study the induced subgraph on `\mathfrak B(G)` under connected-cycle switches. Prove that an all-bad horizontal component forces a bounded cut or four-pole kernel.

### 11.3 Full-cap-profile theorem

At graph level, eliminate the four Kempe kernels by proving every cap-forced shore profile contains a full `\mathcal K_i`.

### 11.4 Use harder laboratories

Future computational laboratories should include non-three-edge-colourable bridgeless cubic graphs. The current certificate remains valuable for testing fixed-flow machinery but is too easy at graph level to model a minimal counterexample.

## 12. Trust boundary

The common weight-six word, `2K_3` component sets, three unrestricted profiles, explicit three-edge-colouring, and boundary states `B_0,A,B_0` are exact finite certificates.

The bad-flow-set formulation and quantifier separation are theorem-level logical reorganizations of the framework.

No statement here proves connectivity of the Fano-flow reconfiguration graph, eliminates all bad-flow components, proves the full-cap-profile theorem, or proves the five-cycle double cover conjecture.
