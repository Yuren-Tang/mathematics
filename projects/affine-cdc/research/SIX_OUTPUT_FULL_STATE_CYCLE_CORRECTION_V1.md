# Six-output full-state cycle correction and the complete short-cycle census in `L(P)`

## Research correction dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `6f83575b4025c6df21b7f3886d4b6061dee88a32`  
**Parents:**

- `projects/affine-cdc/research/NONCROSSING_SIDE_SIGNATURE_WINDOW_V1.md`;
- `projects/affine-cdc/research/PETERSEN_PIVOT_RESOLUTION_V1.md`;
- `projects/affine-cdc/research/PETERSEN_BACKTRACK_TYPE_T_REDUCTION_V1.md`;
- `projects/affine-cdc/research/PETERSEN_CYCLE_MONODROMY_V1.md`;
- `projects/affine-cdc/research/PETERSEN_STAR_REFLECTION_V1.md`;
- `projects/affine-cdc/research/SIX_OUTPUT_RETURN_CELL_NORMAL_FORM_V1.md`.

**Status:** exact correction of the six-output return-cell cycle classification. The earlier five-change ceiling applies only to an open linear collapsed pivot path. It does not classify a closed full state walk in `L(P)`. The complete simple-cycle census through six outputs has four `S5`-orbits, including two previously omitted six-cycle sectors.  
**Supersedes:** every claim that a six-output return cell has only one possible cyclic full-state core, namely a Petersen five-cycle, or that six- and identity-cycle cores are excluded solely by the bound `m <= 6`.  
**Not implied:** graph-side realisability of every abstract state cycle, source replacement, canonical acceptance, Lean verification, or the global five-support theorem.

---

## 1. The indexing error

Let

\[
F_0,F_1,\ldots,F_m
\]

be a state walk in the line graph

\[
L(P),
\qquad
P=KG(5,2),
\]

where each transition emits one side root. A six-output window gives

\[
m\le6.
\]

For each transition define the pivot

\[
s_t=F_{t-1}\cap F_t.
\]

Partition the pivot word into maximal constant runs.

### Open linear path

If the state walk is treated as an open linear path and there are `r` maximal pivot runs, the collapsed pivot path has

\[
r-1
\]

edges.

### Closed state cycle

If

\[
F_m=F_0
\]

and the pivot runs are read cyclically, the collapsed pivot cycle has

\[
r
\]

edges, not `r-1`.

In particular, a closed six-state cycle may have six distinct pivots and a six-edge pivot cycle.

### Correction 1.1

The old inequality

\[
k\le m-1\le5
\]

is valid only for an open linear collapsed pivot path. It cannot exclude a closed six-cycle in `L(P)`.

This is the exact source of the omitted identity hexagon sector.

---

## 2. Full state graph versus pivot skeleton

A state vertex of `L(P)` is a Petersen edge

\[
F=\{a,b\}.
\]

A transition

\[
F^-\to F^+
\]

has pivot

\[
s=F^-\cap F^+.
\]

Collapsing a constant-pivot run preserves its rank-two root-resolution data but does **not** preserve its support monodromy.

The smallest counterexample is the star triangle:

\[
\{s,x\}\to\{s,y\}\to\{s,z\}\to\{s,x\}.
\]

Its pivot skeleton collapses to one vertex, while its full support monodromy is a nontrivial reflection.

Therefore:

\[
\boxed{
\text{collapsed pivot skeleton}
\text{ does not determine full support holonomy.}
}
\]

Any affine or support classification of a bounded return cell must retain the support transport inside constant-pivot runs.

---

## 3. Complete simple-cycle census through length six

Exact enumeration in the fifteen-vertex state graph `L(P)` gives:

\[
\begin{array}{c|c}
\text{length}&\text{number of unoriented simple cycles}\\
\hline
3&10\\
4&0\\
5&12\\
6&70.
\end{array}
\]

The cycles split into exactly four `S5`-orbits.

### Theorem 3.1 — short full-state cycle classification

Every simple cycle of `L(P)` with at most six transitions belongs to exactly one of the following four sectors.

#### Sector A — star triangle

\[
\ell=3,
\qquad
\#=10,
\qquad
\text{orbit size }10.
\]

Pivot-run pattern:

\[
(3).
\]

Support monodromy:

\[
2\,1^3.
\]

This is the constant-pivot rank-two star reflection.

#### Sector B — Petersen pentagon

\[
\ell=5,
\qquad
\#=12,
\qquad
\text{orbit size }12.
\]

Pivot-run pattern:

\[
(1,1,1,1,1).
\]

Support monodromy:

\[
4\,1.
\]

These are exactly the edge cycles induced by the twelve five-cycles of the Petersen graph.

#### Sector C — star-expanded pentagon

\[
\ell=6,
\qquad
\#=60,
\qquad
\text{orbit size }60.
\]

Pivot-run pattern:

\[
(2,1,1,1,1).
\]

Support monodromy:

\[
2^2\,1.
\]

Each such cycle is obtained from a Petersen pentagon by choosing one of its five pivots and inserting the third Petersen edge incident at that pivot. Hence

\[
12\cdot5=60.
\]

The inserted two-transition constant-pivot run changes the total support monodromy from type `41` to type `2^2 1`.

#### Sector D — Petersen hexagon

\[
\ell=6,
\qquad
\#=10,
\qquad
\text{orbit size }10.
\]

Pivot-run pattern:

\[
(1,1,1,1,1,1).
\]

Support monodromy:

\[
1^5.
\]

These are exactly the edge cycles induced by the ten six-cycles of the Petersen graph.

No simple four-cycle occurs.

---

## 4. Structural proof of the two six-cycle families

Let `C` be a simple six-cycle in `L(P)`. Read its six state vertices as six edges of `P`, with consecutive state edges sharing one pivot vertex.

Because `P` is cubic and triangle-free, there are two possibilities.

### 4.1 Six distinct pivots

If all six transition pivots are distinct, the six state edges form one simple six-cycle in `P`. This is Sector D.

The Petersen graph has ten simple six-cycles, forming one `S5` orbit. Their support monodromy is identity.

### 4.2 Five distinct pivots

If exactly one pivot occurs twice consecutively in the cyclic pivot word, three consecutive state edges pass through one cubic Petersen vertex. Removing the middle, third incident edge collapses the state cycle to a simple five-cycle of `P`.

Conversely, for every Petersen five-cycle and every one of its five pivot vertices, insert the unique third edge incident at that pivot. This produces a simple six-cycle of `L(P)`.

Thus Sector C is canonically

\[
\boxed{
\{\text{Petersen five-cycle}\}
\times
\{\text{chosen pivot on that cycle}\}.
}
\]

This gives `12*5=60` cycles and one transitive `S5` orbit.

---

## 5. Corrected six-output normal form

A six-output return window may contain backtracks and repeated state vertices. After deleting immediate backtracks, every nonempty closed simple core extracted from the full state walk has length at most six.

### Theorem 5.1 — corrected bounded cyclic sectors

The complete list of possible simple cyclic full-state cores through six outputs is:

\[
\boxed{
\begin{array}{c|c}
\text{core}&\text{support monodromy}\\
\hline
\text{star triangle}&2\,1^3\\
\text{Petersen pentagon}&4\,1\\
\text{star-expanded pentagon}&2^2\,1\\
\text{Petersen hexagon}&1^5.
\end{array}
}
\]

There is no fifth sector.

### Consequence 5.2

The six-output ceiling still reduces the physical problem to a finite bounded list, but the list has four cyclic sectors rather than one.

The previous rank-two-run plus pivot-skeleton factorisation remains useful as a coefficient decomposition. It must not be used by itself to infer the total support or affine monodromy.

---

## 6. Revised affine calibration obligations

The four sectors require different treatment.

### 6.1 Star triangle

This is the minimal reflection sector. Its support action is a single transposition in one DDD stabiliser. The affine detector is the normalised reflection value

\[
0\quad\text{or}\quad q_i.
\]

### 6.2 Petersen pentagon

This is the type-`41` rotation sector. Its affine class is invisible on the rotation subgroup alone and needs a compatible reflection comparison.

### 6.3 Star-expanded pentagon

This mixed sector has total support type

\[
2^2\,1.
\]

It cannot be classified by assigning the pentagon rotation and then declaring the inserted constant-pivot run holonomy-free. The inserted run contributes essential support transport.

The correct target is to express its total affine cocycle as the composition of:

1. the pentagon rotation transport;
2. one open two-transition star segment;
3. the boundary comparison identifying the expanded and collapsed cells.

This is a new bounded calibration, not a corollary of the pure `D8` reflection test.

### 6.4 Petersen hexagon

This sector has identity support monodromy. Its complete obstruction is a pure affine/side-semantic displacement and belongs to the regional Stokes / flat translation branch.

It is the smallest identity-return cyclic core that actually fits inside the six-output ceiling.

---

## 7. Exact Wolfram certificate

The Petersen graph was constructed as

\[
KG(5,2),
\]

and its line graph was enumerated directly.

The exact outputs are:

\[
|V(L(P))|=15,
\qquad
|E(L(P))|=30.
\]

Simple cycles:

\[
10x^3+12x^5+70x^6+\cdots.
\]

Orbit and monodromy table through length six:

\[
\begin{array}{c|c|c|c|c}
\ell&\text{orbit size}&\text{stabiliser}&\text{pivot runs}&\text{monodromy}\\
\hline
3&10&12&(3)&2\,1^3\\
5&12&10&(1^5)&4\,1\\
6&60&2&(2,1,1,1,1)&2^2\,1\\
6&10&12&(1^6)&1^5.
\end{array}
\]

The computation independently verifies the structural classification above. The human proof identifies the two length-six constructions and explains the counts.

---

## 8. Governance correction

Until the relevant dossiers are revised, consumers must read the following statements with this correction:

- `SIX_OUTPUT_RETURN_CELL_NORMAL_FORM_V1.md` classifies a collapsed pivot skeleton, not the complete full-state support holonomy;
- the exclusion of six-cycle cores is withdrawn;
- the phrase “the only cyclic core is one Petersen five-cycle” is false for full state cycles in `L(P)`;
- the odd-DDD / even-flat split remains valid for simple pivot cycles of `P`, but is not a complete classification of six-output state cycles;
- constant-pivot rank-two resolvability does not mean support-monodromy triviality.

No canonical, formal, manuscript, release, or publication status follows from this correction.

---

## 9. Revised next step

The finite physical programme is now:

1. star reflection calibration;
2. pure pentagon rotation plus reflection calibration;
3. mixed star-expanded pentagon calibration of type `2^2 1`;
4. identity hexagon projective/affine Stokes displacement;
5. bounded source composition or separator extraction for each sector.

The immediate priority is Sector C, because it is the exact interaction between the rank-two star mechanism and the DDD pentagon mechanism that the collapsed-skeleton treatment erased.

---

## 10. Trust boundary

### Exact here

- correction of `r-1` versus cyclic `r` collapsed edges;
- nontrivial support monodromy inside constant-pivot runs;
- complete simple-cycle census of `L(P)` through length six;
- four `S5` orbits and their sizes;
- structural classification of the sixty mixed six-cycles as star-expanded pentagons;
- identity classification of the ten pure Petersen hexagons;
- support monodromy types of all four sectors;
- withdrawal of the unique-five-cycle full-state claim.

### Still open

- physical realisability of every abstract state cycle in a return cell;
- affine translation of the mixed `2^2 1` sector;
- identity-hexagon side displacement;
- source-incidence-preserving replacement and separator transfer;
- strict local descent, horizontal induction, and the global five-support theorem.
