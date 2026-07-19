# Every Petersen Fano flow has a componentwise-good root lift

**Programme:** `AffineCDC — Research Lead`  
**Status:** exact finite computational theorem with explicit topological classification; not canonical pending Director review and literature audit  
**Parents:** `FIVE_CDC_FIXED_FLOW_GRAPH_LEVEL_SEPARATION_V1.md`, `FIVE_CDC_COLORED_SURFACE_DUAL_HALFCUBE_V1.md`, `FIVE_CDC_GAUGE_PARTIAL_PETRIAL_CORRESPONDENCE_V1.md`

## 1. Purpose

The thirty-vertex fixed-flow laboratory is three-edge-colourable. It is valuable for testing vertical gauge/Petrial obstruction, but it is not a suitable graph-level model of a snark.

This packet moves to the Petersen graph and performs a complete census of:

- all nowhere-zero `\mathbf F_2^3` flows;
- all compatible reduced root lifts;
- the associated cycle-face surfaces and weighted dual graphs;
- componentwise half-cube goodness;
- the full connected-cycle flow-switch graph.

The central exact result is stronger than the existence of one five-support cover:

\[
\boxed{
\text{every nowhere-zero Fano flow on the Petersen graph has a compatible five-support root lift.}
}
\]

Equivalently, its bad-flow set is empty:

\[
\boxed{
\mathfrak B(P)=\varnothing.
}
\]

Some fixed-flow fibres contain one bad projective-plane lift, but no fibre is wholly bad.

## 2. Exact Fano-flow population

Use the standard ten-vertex, fifteen-edge Petersen graph. Its binary cycle-space dimension is

\[
15-10+1=6.
\]

Enumerating three binary cycle coordinates and excluding edgewise zero values gives exactly

\[
\boxed{28560}
\]

nowhere-zero `\mathbf F_2^3` flows.

Every one spans all of `\mathbf F_2^3`. There is no rank-two nowhere-zero binary flow, consistently with non-three-edge-colourability.

The group

\[
GL(3,2)
\]

acts freely on the flow set. Since

\[
|GL(3,2)|=168,
\]

there are exactly

\[
\boxed{170}
\]

coordinate-free `GL(3,2)` flow orbits.

Quotienting further by the Petersen automorphism group gives exactly

\[
\boxed{5}
\]

flow types.

## 3. Complete reduced-fibre classification

For each of the `170` `GL(3,2)` representatives, solve the root-lift affine system exactly and enumerate the complete reduced gauge fibre.

The results are:

\[
\begin{array}{c|c|r}
\text{fibre size}&\text{componentwise-good lifts}&\text{flow orbits}\\
\hline
1&1&80\\
2&2&60\\
2&1&20\\
4&3&10
\end{array}
\]

Thus:

\[
\boxed{
140/170
}
\]

flow orbits have every reduced lift good, and the remaining

\[
\boxed{30/170}
\]

have exactly one bad lift.

There is no orbit with zero good lifts.

Restoring Fano coordinates multiplies every orbit count by `168`:

\[
\begin{array}{c|r}
\text{flow-fibre outcome}&\text{flows}\\
\hline
\text{all lifts good}&23520\\
\text{some good, one bad}&5040\\
\text{all lifts bad}&0.
\end{array}
\]

Hence

\[
\boxed{
\mathfrak B(P)=\varnothing.
}
\]

## 4. Three surface types

Across the `170` coordinate-free flows there are

\[
280
\]

reduced root lifts in total. Every dual simple graph is complete and exactly three weighted surface types occur.

### Type T — torus / `K_5`

The cycle-face surface is orientable with

\[
\chi=0.
\]

It has five faces, and the simple dual graph is

\[
K_5.
\]

The ten dual edge multiplicities are

\[
1^6,\quad2^3,\quad3^1,
\]

and the five face lengths are

\[
\boxed{5,5,5,6,9.}
\]

There are

\[
\boxed{100}
\]

such lifts modulo `GL(3,2)`.

### Type K — Klein bottle / `K_5`

The surface is nonorientable with

\[
\chi=0.
\]

It again has five faces and simple dual graph `K_5`.

The dual edge multiplicities are

\[
1^5,\quad2^5,
\]

and the face lengths are

\[
\boxed{5,5,6,6,8.}
\]

There are

\[
\boxed{150}
\]

such lifts modulo `GL(3,2)`.

### Type P — projective plane / `K_6`

The surface is nonorientable with

\[
\chi=1.
\]

It has six pentagonal faces. Every pair of faces shares exactly one source edge, so the weighted and simple dual graphs are both

\[
K_6.
\]

There are

\[
\boxed{30}
\]

such lifts modulo `GL(3,2)`.

The total reduced-lift distribution with coordinates restored is therefore

\[
\begin{array}{c|r}
\text{surface type}&\text{root lifts}\\
\hline
\text{torus }K_5&16800\\
\text{Klein bottle }K_5&25200\\
\mathbb{RP}^2\ K_6&5040
\end{array}
\]

for a total of

\[
47040
\]

reduced coordinate-labelled lifts.

## 5. Componentwise goodness is exactly the surface transition

The target half-cube graph `\mathscr A_5` has clique number five.

Hence:

- every `K_5` dual maps to `\mathscr A_5`;
- no `K_6` dual maps to `\mathscr A_5`.

Therefore:

\[
\boxed{
\text{torus and Klein-bottle lifts are good};
\qquad
\mathbb{RP}^2\text{ lifts are bad}.
}
\]

Every mixed fibre contains exactly one projective-plane state and all remaining states are `K_5` states.

Thus Petersen vertical escape has the exact form

\[
\boxed{
\mathbb{RP}^2/K_6
\xrightarrow{\text{nontrivial admissible Petrial}}
T^2/K_5
\quad\text{or}\quad
\text{Klein}/K_5.
}
\]

In the two-dimensional mixed fibres, the unique projective-plane core is private: each of the three nonzero gauge moves destroys it and reaches a good state.

## 6. Five automorphism-flow types

Under

\[
\operatorname{Aut}(P)\times GL(3,2),
\]

the complete flow set consists of five types:

\[
\begin{array}{c|r|l|c}
\text{type}&\text{flows}&\text{reduced surface fibre}&\text{good fraction}\\
\hline
I&10080&\{\text{Klein}\}&1/1\\
II&10080&\{\text{torus},\text{Klein}\}&2/2\\
III&1680&\{\mathbb{RP}^2,3\times\text{Klein}\}&3/4\\
IV&3360&\{\mathbb{RP}^2,\text{torus}\}&1/2\\
V&3360&\{\text{torus}\}&1/1
\end{array}
\]

The five types are complete: every Fano flow is equivalent to exactly one row.

This is substantially smaller than the `170` coordinate-free flows and gives a finite topological state language for the Petersen laboratory.

## 7. Full horizontal reconfiguration

For every flow `f`, every nonzero direction `a`, and every connected binary cycle in

\[
P-f^{-1}(a),
\]

perform the rank-one connected-cycle switch

\[
f\longmapsto f+a\mathbf1_C.
\]

The exact switch graph on all

\[
28560
\]

coordinate-labelled Fano flows is connected.

Every flow has between

\[
91
\quad\text{and}\quad
116
\]

distinct connected-cycle neighbours. The total degree is

\[
3092880,
\]

so the undirected switch graph has

\[
1546440
\]

edges.

Thus the five automorphism-flow types are not separate horizontal components. Connected-cycle switching moves among one connected global flow space.

## 8. Mechanism interpretation

The Petersen graph separates the vertical and horizontal mechanisms particularly cleanly.

### Vertical fact

For every Fano flow, its root-lift fibre already contains a good state:

\[
\mathfrak B(P)=\varnothing.
\]

Horizontal movement is unnecessary for existence.

### Local obstruction

The only bad lift is the canonical six-face projective-plane geometry:

\[
\mathbb{RP}^2
\longleftrightarrow
K_6
\longleftrightarrow
\text{six pentagonal faces of Petersen}.
\]

### Petrial escape

Gauge freedom converts that six-face geometry into one of two five-face `\chi=0` geometries. The obstruction is never renewed at every gauge state.

### Horizontal coherence

All Fano flows lie in one connected switch graph, but every horizontal vertex is already vertically soluble.

The complete picture is therefore

\[
\boxed{
\text{connected horizontal flow space}
\quad+\quad
\text{no wholly bad vertical fibre}.
}
\]

## 9. Comparison with the thirty-vertex laboratory

The thirty-vertex graph contains many wholly bad Fano-flow fibres, including universal three- and six-dimensional renewal modules, despite being graph-level three-edge-colourable.

Petersen exhibits the opposite balance:

- it is not three-edge-colourable;
- nevertheless every Fano flow is vertically good;
- its bad lifts are isolated projective-plane states rather than renewal modules.

Therefore neither graph-level edge-colourability nor snark status alone predicts the size of `\mathfrak B(G)`.

The relevant invariant is the interaction among:

- the chosen Fano flow;
- the gauge code;
- the allowed Petrial orbit;
- the surface dual obstruction.

## 10. New theorem-level target

The Petersen census suggests the following vertical-solubility property.

### Universal-flow solubility

Call a bridgeless cubic graph **Fano-universally soluble** when

\[
\boxed{
\mathfrak B(G)=\varnothing.
}
\]

Petersen is Fano-universally soluble. The thirty-vertex laboratory is not.

This property is strictly stronger than having a five-support CDC and logically independent of three-edge-colourability.

The next structural questions are:

1. characterize graphs or cyclic connectivity regimes which force universal-flow solubility;
2. find the smallest snark with a genuinely wholly bad Fano-flow fibre;
3. determine whether a minimal graph-level counterexample must have a large, horizontally closed bad-flow set;
4. relate the appearance of private projective-plane `K_6` states to the gauge-code dimension and cyclic edge cuts.

## 11. Updated mechanism map

The research programme now has three calibrated laboratories.

### Easy graph, hard fixed flows

The thirty-vertex graph is three-edge-colourable but has large fixed-flow renewal modules.

### Snark, universally soluble flows

Petersen is not three-edge-colourable, yet every Fano flow has a good root lift.

### Genuine graph-level obstruction target

A counterexample would require

\[
\mathfrak B(G)
=
\{\text{all nowhere-zero Fano flows}\},
\]

not merely one large renewal module.

The next computational laboratory should therefore be a larger non-three-edge-colourable cubic graph and should measure the bad-flow set directly, rather than beginning from one selected flow.

## 12. Trust boundary

The flow counts, orbit counts, five flow types, complete reduced fibres, surface orientability, weighted dual types, empty bad-flow set, and connected full switch graph are exact finite computations reproduced by the private dependency-free verifier.

The terminology “Fano-universally soluble” and the proposed structural programme are new organizational definitions and conjectural directions.

No statement here characterizes all such graphs, finds a graph-level counterexample, or proves the five-cycle double cover conjecture.
