# Horizontal neighbourhoods of the universal renewal cube

**Programme:** `AffineCDC — Research Lead`  
**Status:** exact finite computational evidence plus elementary arrangement deductions; not canonical pending Director review and literature audit  
**Parents:** `FIVE_CDC_UNIVERSAL_RENEWAL_CUBE_TEMPLATE_V1.md`, `FIVE_CDC_INTRINSIC_RENEWAL_CUBE_COORDINATES_V1.md`, `FIVE_CDC_RENEWAL_SKELETON_AND_RESERVE_CODE_CENSUS_V1.md`

## 1. Purpose

The universal renewal cube is a fixed-flow obstruction module: its eight gauge states are all componentwise bad, each state has one private dual `K_6`, and the eight weighted-dual types carry intrinsic affine coordinates.

The next question is horizontal rather than vertical:

> Is the universal cube locally trapped in the connected-cycle reconfiguration graph of nowhere-zero Fano flows, or does one horizontal switch usually escape it?

This packet performs the complete one-step connected-cycle census from each of the five source flows realizing the universal cube. It then deduplicates all wholly bad target flows and analyzes their complete marked-`K_6` renewal arrangements.

The principal conclusion is:

\[
\boxed{
\text{the cube has a large immediate escape boundary, while the residual bad region remains point-like.}
}
\]

Essential renewal dimension grows as high as six, but no marked obstruction occurrence locus of dimension two or more appears. The only positive-dimensional persistence is one universal weight-six `K_4` reserve-line atom.

## 2. Horizontal move population

For a nowhere-zero Fano flow `f` and a nonzero direction `a`, a genuine one-step horizontal move is

\[
f\longmapsto f+a\mathbf 1_C,
\]

where `C` is one connected source cycle avoiding the colour class `f^{-1}(a)`.

For each of the five universal-cube source flows, every such connected-cycle move is enumerated exactly. The target reduced root-lift torsor is solved completely, and every lift is tested against the true componentwise criterion

\[
T_g\longrightarrow\mathscr A_5.
\]

The fibre outcome is classified as:

- **all:** every reduced lift is componentwise good;
- **some:** at least one but not all reduced lifts are good;
- **none:** the entire reduced fibre is bad.

## 3. Exact one-step escape counts

The five source flows have the following complete connected-neighbour counts.

\[
\begin{array}{c|r|r|r|r|r}
\text{cube source}&\text{neighbours}&\text{all}&\text{some}&\text{none}&\text{at least one good}\\
\hline
0&4763&2521&1488&754&4009\\
1&4763&2521&1488&754&4009\\
2&7007&3861&2147&999&6008\\
3&3407&1693&1092&622&2785\\
4&4675&2451&1467&757&3918
\end{array}
\]

Counting neighbours with source multiplicity gives

\[
24615
\]

horizontal moves, of which

\[
\boxed{20729}
\]

lead to a target flow having at least one componentwise-good reduced lift. Thus the one-step escape proportion is

\[
\frac{20729}{24615}\approx0.8421.
\]

The five source-specific proportions lie between approximately `81.7%` and `85.7%`.

### Interpretation

The universal cube is not a locally closed trap. Most connected-cycle directions leave the wholly bad region immediately.

This does not prove that every cube admits a bounded escape path in an arbitrary graph. It is exact evidence for the complete one-step neighbourhoods of the five displayed realizations.

## 4. Deduplicated residual bad region

Different universal cubes may share horizontal neighbours. After deduplication, the wholly bad targets form a set of

\[
\boxed{3653}
\]

distinct nowhere-zero Fano flows.

Their membership multiplicities among the five source neighbourhoods are:

\[
\begin{array}{c|r}
\text{number of source-cube neighbourhoods containing the target}&\text{target flows}\\
\hline
1&3503\\
2&98\\
3&28\\
4&17\\
5&7
\end{array}
\]

The `3653` target flows contain

\[
\boxed{14330}
\]

reduced root lifts in total. Every one remains componentwise bad because its dual triangulation contains a `K_6`. No `K_6`-free deeper half-cube obstruction appears anywhere in this complete one-step bad neighbourhood.

This is still local evidence, not a theorem that all compatible bad triangulations contain `K_6`.

## 5. Gauge dimension and essential renewal dimension

For each wholly bad target flow, compute:

- the reduced gauge dimension `\dim B_f`;
- the complete marked-`K_6` occurrence arrangement;
- the common lineality space;
- the essential renewal dimension `d_{\mathrm{ren}}`.

The joint distribution is:

\[
\begin{array}{c|c|r}
\dim B_f&d_{\mathrm{ren}}&\text{target flows}\\
\hline
0&0&420\\
1&0&108\\
1&1&1499\\
2&1&36\\
2&2&972\\
3&3&461\\
4&4&132\\
5&5&23\\
6&6&2
\end{array}
\]

Thus common invisible gauge directions occur only in

\[
108+36=144
\]

flows of full gauge dimension one or two. Every target with full gauge dimension at least three has trivial common lineality.

The essential-dimension distribution is:

\[
\begin{array}{c|r}
d_{\mathrm{ren}}&\text{target flows}\\
\hline
0&528\\
1&1535\\
2&972\\
3&461\\
4&132\\
5&23\\
6&2
\end{array}
\]

Hence horizontal motion creates renewal modules of dimension up to six.

## 6. The occurrence geometry stays one-dimensional

Despite essential dimensions up to six, the marked-core occurrence loci remain extremely small.

### Computational Theorem 6.1

Among the `3653` wholly bad targets:

\[
\boxed{3574}
\]

have pure point-renewal arrangements: every nonempty descended marked-core locus is a singleton.

The remaining

\[
\boxed{79}
\]

targets have some positive-dimensional marked-core locus, but in every case:

\[
\boxed{
\max_C\dim\overline A_C=1.
}
\]

No affine plane or higher-dimensional occurrence locus appears.

Moreover, whenever more than one line occurs in one essential quotient, the lines are disjoint. There are no intersecting line networks.

### Complete codimension patterns

The exact patterns are:

\[
\begin{array}{c|l|r}
d_{\mathrm{ren}}&\text{proper occurrence loci}&\text{flows}\\
\hline
0&1\text{ point}&528\\
1&2\text{ points}&1535\\
2&4\text{ points}&966\\
2&1\text{ line}+2\text{ points}&6\\
3&8\text{ points}&411\\
3&1\text{ line}+6\text{ points}&30\\
3&1\text{ line}+8\text{ points}&18\\
3&2\text{ disjoint lines}+4\text{ points}&2\\
4&16\text{ points}&119\\
4&2\text{ disjoint lines}+12\text{ points}&8\\
4&2\text{ disjoint lines}+16\text{ points}&5\\
5&32\text{ points}&15\\
5&1\text{ line}+32\text{ points}&8\\
6&2\text{ disjoint lines}+64\text{ points}&2
\end{array}
\]

In rows where all points already occur, the displayed lines are redundant members of the full marked-core arrangement. They record persistence of additional marked cliques but are unnecessary for covering the quotient.

## 7. The universal reserve-line atom

The `79` non-point arrangements contain

\[
\boxed{96}
\]

distinct affine line loci.

For every one of these lines, let `\lambda` be its unique nonzero direction word. Exact computation gives:

\[
\boxed{
\operatorname{wt}(\lambda)=6,
\qquad
Q_{\operatorname{supp}\lambda}\cong K_4.
}
\]

Thus every line is generated by the same canonical weight-six `K_4` harmonic circuit.

No `4K_2`, `2K_3`, `2C_4`, or larger quotient generates a positive-dimensional marked-core locus in this horizontal bad neighbourhood.

### Essential versus redundant lines

The `96` lines split exactly as follows.

\[
\begin{array}{c|c|c|r}
\text{line role}&|R_C|&R_C\text{ relative to }\operatorname{supp}\lambda&\text{lines}\\
\hline
\text{essential}&6&R_C=\operatorname{supp}\lambda&56\\
\text{redundant}&7&\operatorname{supp}\lambda\subset R_C&40
\end{array}
\]

For an essential line, the marked `K_6` avoids exactly the six source edges of the `K_4` harmonic cut. The line supplies two essential states not already covered by private point cores.

For a redundant line, the reserve contains the same six-edge circuit and exactly one additional source edge. Both states of the line already carry private point cores, so the persistent clique does not contribute to a minimal cover.

This distinction is an exact census fact. It suggests that the one spare edge is the threshold between an essential interface and a superimposed redundant persistence mode, but no universal theorem asserting that threshold is yet proved.

## 8. Mechanism map

The current local-to-horizontal mechanism can now be represented as follows.

### Layer 1 — fixed-lift obstruction

\[
T_g\not\longrightarrow\mathscr A_5
\]

is witnessed in the present neighbourhood by a dual `K_6`.

### Layer 2 — vertical Petrial action

Every marked clique has an affine occurrence locus determined by its reserve-shortened gauge code

\[
B_f\cap\mathbf F_2^{R_C}.
\]

Small reserves usually force private point cores. A weight-six `K_4` circuit fitting exactly inside the reserve creates the only observed line-persistence mode.

### Layer 3 — renewal geometry

The full bad region in one gauge fibre is almost always a cube of private replacement cliques. High essential dimension means more private states, not larger obstruction subspaces.

### Layer 4 — horizontal reconfiguration

A connected-cycle switch changes the Fano flow, the gauge code, all shortened reserve codes, and therefore the renewal skeleton. Approximately `84.2%` of the complete moves from the five universal cubes immediately reach a fibre with a good state.

The remaining moves transport the system to renewal quotients of dimensions zero through six, but their occurrence geometry remains points plus disjoint `K_4` lines.

## 9. Existing mechanism versus surviving obstruction

### Mechanism now explained

1. **Local clique destruction:** exposure rank decides whether one marked clique can survive a Petrial.
2. **Clique privacy:** the reserve-shortened code and its distance explain why most cores belong to one state only.
3. **Line persistence:** every observed line is one weight-six `K_4` harmonic quotient living in the reserve.
4. **High-dimensional renewal:** dimensions up to six arise by assembling many private point cores, not by forming high-dimensional persistent blocks.
5. **Horizontal escape:** most one-step connected-cycle moves break complete renewal coverage.

### Obstruction still alive

The surviving difficulty is an organized assignment

\[
q\longmapsto\{\text{private }K_6\text{ cores at }q\}
\]

on a high-dimensional affine cube, occasionally decorated by disjoint `K_4` reserve lines.

Thus the current obstruction is closer to a finite affine cellular automaton than to a general subspace arrangement.

The missing theorem is not merely to destroy one core or one line. It is to show that this statewise replacement rule cannot remain closed under all horizontal connected-cycle moves unless the source graph admits a canonical decomposition or gluing interface.

## 10. Refined next targets

### 10.1 Point-renewal module classification

Classify the two essential-dimension-six flows and representative pure point modules in dimensions four and five. Determine whether their state-to-weighted-dual maps admit intrinsic parity coordinates generalizing the universal three-cube.

### 10.2 `K_4` reserve-interface theorem

Give a conceptual topological description of a six-edge `K_4` harmonic cut lying exactly in the reserve of six mutually adjacent faces. Explain why one extra reserve edge makes the same line redundant in the observed census.

### 10.3 Horizontal update law

Derive an update rule for:

- private point cores;
- `K_4` reserve lines;
- the intrinsic parity coordinates of a renewal module

under one connected-cycle flow switch.

### 10.4 Global dichotomy

The desired form is:

\[
\boxed{
\text{some reachable renewal quotient has an uncovered state}
}

or

\[
\boxed{
\text{persistent point-and-line renewal forces a bounded decomposition interface}.
}
\]

## 11. Trust boundary

All counts, dimension distributions, line-locus classifications, harmonic quotient signatures, and reserve sizes in this packet are exact finite computations reproduced by the private dependency-light verifier.

The description as an affine cellular automaton and the proposed decomposition alternative are mechanism-level interpretations of those exact facts.

No statement here proves a universal escape theorem, excludes compatible deeper half-cube obstructions outside the displayed neighbourhood, or proves the five-cycle double cover conjecture.
