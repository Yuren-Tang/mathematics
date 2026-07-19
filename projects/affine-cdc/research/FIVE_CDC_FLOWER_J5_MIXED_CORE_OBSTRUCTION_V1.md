# A compatible K6-free half-cube obstruction and mixed-core renewal in the flower snark J5

**Programme:** `AffineCDC — Research Lead`  
**Status:** theorem-level graph-homomorphism obstruction plus exact finite root-lift and neighbourhood certificates; not canonical pending Director review and literature audit  
**Parents:** `FIVE_CDC_K6_FREE_HALFCUBE_WARNING_V1.md`, `FIVE_CDC_FIXED_FLOW_GRAPH_LEVEL_SEPARATION_V1.md`, `FIVE_CDC_PETERSEN_ALL_FANO_FLOWS_V1.md`

## 1. Purpose

Earlier compatible-root-lift censuses found only dual `K_6` obstructions. A general graph-homomorphism warning showed that `K_6`-free graphs need not map to the half-cube `\mathscr A_5`, but no compatible dual triangulation witnessing that deeper obstruction had yet been found.

This packet closes that gap.

In the twenty-vertex flower snark `J_5`, an explicit nowhere-zero Fano flow has a two-state reduced gauge fibre in which:

- one lift is obstructed by a dual `K_6`;
- the other lift is `K_6`-free but still does not map to `\mathscr A_5`.

The second obstruction contains

\[
K_2\vee W_5,
\]

where `W_5` denotes the wheel with odd rim `C_5`. Its non-homomorphism has a short human proof using the common neighbourhood of an edge in `\mathscr A_5`.

Thus:

\[
\boxed{
\exists\text{ compatible }T_g:
\quad K_6\nsubseteq T_g,
\qquad
T_g\not\longrightarrow\mathscr A_5.
}
\]

The two gauge states form the first exact **mixed-core renewal atom**:

\[
\boxed{
K_2\vee W_5\text{-type obstruction}
\longleftrightarrow
K_6\text{-type obstruction}.
}
\]

## 2. The common neighbourhood of a half-cube edge

Recall that `\mathscr A_5` is the graph on the sixteen even subsets of a five-set, with two vertices adjacent when their symmetric difference has size two.

### Lemma 2.1 — edge common neighbourhood

For every edge `xy` of `\mathscr A_5`, the induced common-neighbour graph

\[
\mathscr A_5[N(x)\cap N(y)]
\]

is the triangular prism

\[
K_3\square K_2.
\]

In particular it is three-colourable.

#### Proof

Translate so that

\[
x=\varnothing,
\qquad
y=\{1,2\}.
\]

A common neighbour must be a two-set sharing exactly one element with `\{1,2\}`. Hence the six common neighbours are

\[
\{1,3\},\{1,4\},\{1,5\},
\qquad
\{2,3\},\{2,4\},\{2,5\}.
\]

The first three form one triangle, the last three form another, and corresponding pairs with the same second coordinate form a perfect matching. No other cross-edge occurs. ∎

## 3. A general join obstruction

Let `H` be any graph, and let

\[
K_2\vee H
\]

be the join obtained by adding two adjacent vertices, each adjacent to every vertex of `H`.

### Theorem 3.1 — chromatic common-neighbour obstruction

If

\[
\chi(H)\ge4,
\]

then

\[
\boxed{
K_2\vee H
\not\longrightarrow
\mathscr A_5.
}
\]

#### Proof

In any homomorphism, the two vertices of the `K_2` map to adjacent vertices `x,y` of `\mathscr A_5`. Every vertex of `H` is adjacent to both, so its image lies in

\[
N(x)\cap N(y).
\]

By Lemma 2.1 that common-neighbour graph is three-colourable. Composing the restriction `H\to N(x)\cap N(y)` with a three-colouring would three-colour `H`, contradiction. ∎

### Corollary 3.2 — K6-free obstruction family

If

\[
\chi(H)\ge4,
\qquad
\omega(H)\le3,
\]

then `K_2\vee H` is a `K_6`-free graph not mapping to `\mathscr A_5`.

Indeed,

\[
\omega(K_2\vee H)=2+\omega(H)\le5.
\]

Every odd wheel `W_{2r+1}` with `r\ge2` is four-chromatic and has clique number three. Therefore

\[
\boxed{
K_2\vee W_{2r+1}
\not\longrightarrow\mathscr A_5
}
\]

is an infinite `K_6`-free obstruction family.

## 4. The flower-snark witness flow

Use the standard flower snark `J_5` with vertices

\[
a_i,b_i,c_i,d_i,
\qquad i\in\mathbf Z/5\mathbf Z,
\]

and edges

\[
a_ib_i,\ a_ic_i,\ a_id_i,\ b_ib_{i+1},\ c_id_{i+1},\ d_ic_{i+1}.
\]

Order the thirty edges lexicographically after identifying

\[
a_i=i,\quad b_i=5+i,\quad c_i=10+i,\quad d_i=15+i.
\]

The explicit nowhere-zero Fano flow is

\[
\begin{aligned}
(&6,4,2,3,4,7,2,4,6,5,
3,6,2,4,6,\\
&7,1,4,6,3,6,2,5,1,1,
5,7,4,7,3).
\end{aligned}
\]

At every cubic vertex the three incident values sum to zero in `\mathbf F_2^3`; the private verifier checks this directly.

Its reduced root-lift fibre has dimension one and therefore exactly two states.

## 5. The K6-free state

One state has nine support-cycle faces. Its simple dual graph, denoted `D_9`, has:

\[
|V(D_9)|=9,
\qquad
|E(D_9)|=28,
\]

and degree sequence

\[
5,5,5,6,6,6,7,8,8.
\]

Its clique number is

\[
\omega(D_9)=5.
\]

Thus it is `K_6`-free.

Two degree-eight vertices are adjacent and dominate the remaining seven vertices. Inside their common neighbourhood, six vertices contain an odd wheel `W_5`: one hub and a five-cycle rim.

Consequently

\[
K_2\vee W_5\subseteq D_9.
\]

By Theorem 3.1,

\[
\boxed{
D_9\not\longrightarrow\mathscr A_5.
}
\]

This is a human non-homomorphism certificate, independent of the exact backtracking solver.

### Surface data

The nine face lengths are

\[
5,6,6,6,6,6,7,9,9,
\]

summing to sixty. Since

\[
|V(J_5)|=20,
\qquad
|E(J_5)|=30,
\qquad
F=9,
\]

the cycle-face surface has

\[
\chi=-1.
\]

It is nonorientable, hence has nonorientable genus three.

The weighted dual has twenty-six edges of multiplicity one and two edges of multiplicity two.

## 6. The K6 state

The other gauge state has seven support-cycle faces. Its simple dual graph contains a `K_6`; in fact it is `K_7` with one missing edge.

Its face lengths are

\[
6,7,7,9,10,10,11.
\]

The surface has

\[
\chi=20-30+7=-3
\]

and is nonorientable of genus five.

The half-cube clique bound immediately gives

\[
T_g\not\longrightarrow\mathscr A_5.
\]

Thus both states are bad, but for different reasons.

## 7. The mixed-core gauge direction

The unique nonzero reduced gauge word has weight

\[
\boxed{16}.
\]

In zero-based edge numbering its support is

\[
\{1,3,4,6,7,9,11,14,15,17,19,21,23,24,25,26\}.
\]

Applying this code-filtered partial Petrial exchanges the two states:

\[
\boxed{
D_9\supseteq K_2\vee W_5
\quad\longleftrightarrow\quad
K_7-e\supseteq K_6.
}
\]

This is not ordinary clique renewal. The active obstruction species changes under the gauge move.

The correct fixed-flow obstruction library must therefore contain at least:

1. clique cores such as `K_6`;
2. common-neighbour chromatic cores such as `K_2\vee H` with `\chi(H)\ge4`.

## 8. Complete one-step horizontal neighbourhood

The witness flow has exactly

\[
\boxed{712}
\]

distinct genuine connected-cycle switch neighbours.

Their complete reduced-fibre outcomes are

\[
\begin{array}{c|r}
\text{target outcome}&\text{neighbours}\\
\hline
\text{all reduced lifts good}&333\\
\text{some good, some bad}&195\\
\text{all reduced lifts bad}&184.
\end{array}
\]

Thus

\[
\boxed{528/712}
\]

neighbours have at least one good state, an immediate escape proportion of approximately `74.2%`.

An explicit all-good escape uses direction `1` and the connected six-edge cycle word

\[
\{0,1,3,5,15,20\}.
\]

The target flow has a singleton reduced fibre, and that lift is componentwise good.

Hence the witness belongs to the bad-flow set

\[
\mathfrak B(J_5),
\]

but is not horizontally trapped inside it.

## 9. Obstruction census in the wholly-bad neighbours

The `184` wholly-bad target flows split as follows:

\[
\begin{array}{c|c|c|r}
\text{fibre size}&K_6\text{-type lifts}&D_9\text{-type lifts}&\text{flows}\\
\hline
1&1&0&84\\
1&0&1&24\\
2&2&0&32\\
2&1&1&41\\
4&2&2&3.
\end{array}
\]

Thus the one-step wholly-bad neighbourhood contains

\[
195
\]

`K_6`-type lifts and

\[
\boxed{71}
\]

`K_6`-free bad lifts.

Every one of the seventy-one `K_6`-free lifts:

- has nine dual vertices;
- is isomorphic to the same graph `D_9`;
- contains `K_2\vee W_5`;
- has the same human chromatic common-neighbour certificate.

Including the centre flow gives seventy-two local occurrences of one universal deep obstruction type.

No second `K_6`-free compatible obstruction type appears in this complete one-step neighbourhood.

## 10. Mechanism update

The obstruction picture must now be enlarged.

### Previous local picture

In the thirty-vertex neighbourhood, every componentwise-bad lift contained `K_6`. Fixed-flow renewal could be modelled using marked clique occurrence loci.

### New local picture

In `J_5`, wholly-bad fibres can renew between two inequivalent obstruction libraries:

\[
\text{clique obstruction}
\quad\leftrightarrow\quad
\text{common-neighbour chromatic obstruction}.
\]

### New graph-level picture

Petersen has

\[
\mathfrak B(P)=\varnothing,
\]

whereas

\[
\mathfrak B(J_5)\ne\varnothing.
\]

But the displayed `J_5` bad flow has a large one-step boundary leading outside `\mathfrak B(J_5)`.

Thus the emerging hierarchy is:

\[
\boxed{
\begin{array}{c}
\text{Petersen: no bad flows}\[1mm]
\text{Flower }J_5:\text{ bad flows exist but have immediate exits}\[1mm]
\text{counterexample target: every flow bad and horizontally closed}
\end{array}}
\]

## 11. Refined obstruction language

For a target edge `xy` in `\mathscr A_5`, define the common-neighbour capacity

\[
\chi\bigl(\mathscr A_5[N(x)\cap N(y)]\bigr)=3.
\]

A dual graph with an adjacent dominating pair therefore imposes a three-colourability condition on the remainder.

This suggests a broader marked-core library based on target common neighbourhoods:

- one dominating clique in the source forces the remainder into an iterated common neighbourhood of its target image;
- chromatic, clique, or homomorphism obstructions inside that target common neighbourhood certify failure.

The `K_6` obstruction is the first clique-capacity case. The `K_2\vee W_5` obstruction is the first chromatic-capacity case.

## 12. Next targets

### 12.1 Mixed-core occurrence arrangement

For a fixed Fano flow, define marked occurrence loci simultaneously for:

- `K_6` cores;
- `D_9` or `K_2\vee W_5` cores;
- later common-neighbour chromatic cores.

Determine whether the union remains an affine-subspace arrangement or requires a more general finite-state obstruction sheaf over the gauge torsor.

### 12.2 Bad-flow component exploration

Explore the connected component of the witness inside the induced bad-flow subgraph of `J_5`. Determine:

- its size modulo `GL(3,2)` and graph automorphisms;
- whether every bad flow has a one-step good neighbour;
- whether mixed-core renewal is confined to a bounded module.

### 12.3 Human classification of D9

Classify the exact nine-vertex graph `D_9` by its complement and determine whether all compatible common-neighbour obstructions reduce to a short list of joins `K_2\vee H`.

### 12.4 Larger snark laboratories

Search for:

- a bad flow whose entire one-step neighbourhood remains bad;
- a bad component with no immediate good boundary;
- a graph for which every nowhere-zero Fano flow is bad.

## 13. Trust boundary

The half-cube common-neighbour lemma and join obstruction theorem are elementary theorem-level arguments.

The explicit `J_5` flow, two-state fibre, surface data, gauge word, dual graphs, `D_9` certificate, complete 712-neighbour census, obstruction counts, and seventy-one isomorphism checks are exact finite computation reproduced by the private verifier.

The proposed mixed-core obstruction library and bad-flow-component programme are mechanism-level deductions.

No statement here classifies all Fano flows on `J_5`, proves that every bad flow has an immediate exit, finds a horizontally closed bad component, or proves the five-cycle double cover conjecture.
