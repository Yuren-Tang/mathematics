# Canonical compatible root-star sections on the Petersen identity `C6`

## Research dossier v1 — local lift table and overlap theorem

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `1986123d61504d9234665d7ee5b017280b9a717d`.

**Parents:**

- `PTOLEMY_ROOT_TUBE_HISTORY_LIFT_SCOPE_CORRECTION_V1.md`;
- `PIVOT_CHANGE_SIX_PORT_STAR_COMPLETION_V1.md`;
- `PETERSEN_PIVOT_RESOLUTION_V1.md`;
- `PETERSEN_IDENTITY_HEXAGON_SIX_CHANNEL_TRIALITY_V1.md`;
- `SIX_LEAF_NNI_ROOT_EXCHANGE_V1.md`;
- `PETERSEN_C8_TWO_C6_HISTORY_FILLING_REDUCTION_V1.md`.

**Status:** exact local-section theorem for the sole primitive even-track orbit. Let `p_0,...,p_5` be a simple Petersen six-cycle and let `z_i` be the third Petersen neighbour of `p_i` outside the cycle. The side word is one repeated root triangle. For every two-turn six-port pivot cell there is exactly one root-valued three-cherry star completion whose three internal roots are that fixed side triangle. Its terminal matching and internal labels admit uniform closed formulas. Consecutive cells induce literally the same root-labelled corolla on their common turn, and antipodal cells induce the same side-triangle corolla. Thus the six local root sections have no history-vertex labelling conflict.

**Assurance boundary:** this dossier does **not** yet supply a coherent relative NNI/cancellation movie from the original lifted Ptolemy cell boundaries to the canonical star sections. Port reassignment inside a star is real. Consequently history-edge compatibility and the full annular tube-lift theorem remain open. This theorem closes the local root-completion and endpoint-overlap part of that obligation without repeating the earlier unsupported jump from a static filling to a history lift.

---

## 1. Identity-hexagon notation

Let

\[
P=KG(5,2)
\]

be the Petersen graph on the ten roots `R_5`, with adjacency given by disjointness.

Fix a simple six-cycle

\[
\boxed{
p_0,p_1,p_2,p_3,p_4,p_5,p_0
}
\]

with indices read modulo six.

At `p_i`, the two cycle neighbours are `p_(i-1),p_(i+1)`. Let

\[
\boxed{
z_i
=N_P(p_i)\setminus\{p_{i-1},p_{i+1}\}
}
\]

be its emitted side root.

The Petersen identity-hexagon theorem gives, after support permutation and cyclic reindexing,

\[
\boxed{
(z_0,z_1,z_2,z_3,z_4,z_5)
=(a,b,c,a,b,c),
}
\]

where

\[
\boxed{a+b+c=0.}
\]

Hence

\[
\boxed{z_{i+3}=z_i}
\]

and every consecutive triple

\[
(z_i,z_{i+1},z_{i+2})
\]

is the same `K_5` root triangle in cyclic order.

The controlling local Petersen relation is

\[
\boxed{
p_{i-1}+p_{i+1}=z_i.}
\]

Indeed the three neighbours of one Petersen vertex form the root triangle on the complementary three support indices.

---

## 2. The six-port cell at two consecutive turns

Consider the pivot-change cell using the consecutive pivots

\[
p_i,\quad p_{i+1}
\]

and their adjacent turns. In the notation of the six-port star theorem, put

\[
s=p_i,
\qquad x=p_{i-1},
\qquad z=z_i,
\]

and

\[
w=z_{i+1},
\qquad t=p_{i+1},
\qquad y=p_{i+2}.
\]

Its complete ordered six-root boundary is

\[
\boxed{
B_i
=(p_i,p_{i-1},z_i
\mid
z_{i+1},p_{i+1},p_{i+2}).}
\]

The two turn equations are

\[
p_{i-1}+p_{i+1}=z_i,
\]

and

\[
p_i+p_{i+2}=z_{i+1}.
\]

The original four-vertex path in the failed history cell has three co-root internal edges. A root-valued local replacement must therefore use a different six-leaf topology.

---

## 3. Canonical cross matching

Define the cross matching

\[
\boxed{
\mathfrak m_i^\star:
\begin{cases}
p_i\longleftrightarrow p_{i+2},\\
p_{i-1}\longleftrightarrow p_{i+1},\\
z_i\longleftrightarrow z_{i+1}.
\end{cases}}
\]

The three forced internal star roots are:

\[
\begin{aligned}
p_i+p_{i+2}&=z_{i+1},\\
p_{i-1}+p_{i+1}&=z_i,\\
z_i+z_{i+1}&=z_{i+2}.
\end{aligned}
\]

Thus:

### Theorem 3.1 — canonical star section

The matching `m_i^star` gives a root-valued three-cherry star completion of `B_i`. Its three internal spokes are

\[
\boxed{
(z_{i+1},z_i,z_{i+2}),}
\]

and its central vertex carries the fixed side-root triangle

\[
\boxed{
\{z_i,z_{i+1},z_{i+2}\}=\{a,b,c\}.}
\]

### Proof

The first two identities are the two Petersen turn relations. The third follows from the repeated triangle side word. All three matched boundary pairs therefore have root sums, and those sums form a root triangle. Apply the star-completion criterion. ∎

---

## 4. Uniqueness of the fixed-triangle section

The six-port star theorem gives four root-valued cross matchings, namely all matchings avoiding the disjoint pivot pair

\[
p_i-p_{i+1}.
\]

Among them, only `m_i^star` has all three internal spokes in the fixed side triangle

\[
T=\{a,b,c\}.
\]

### Theorem 4.1 — uniqueness

For every identity-hexagon cell `B_i`, `m_i^star` is the unique root-valued star matching whose internal-root set is `T`.

### Proof

By `S_5` symmetry it suffices to inspect one representative identity hexagon. Take

\[
(p_0,p_1,p_2,p_3,p_4,p_5)
=(12,35,14,23,15,34),
\]

with side word

\[
(z_0,\ldots,z_5)
=(45,24,25,45,24,25).
\]

For `i=0`, the boundary is

\[
(12,34,45\mid24,35,14).
\]

The four root-valued star matchings have internal-root triples

\[
(14,45,15),
\]

\[
(14,13,34),
\]

\[
(24,23,34),
\]

and

\[
\boxed{(24,45,25).}
\]

Only the last is the fixed side triangle

\[
T=\{24,25,45\},
\]

and it is exactly the matching

\[
12-14,
\qquad34-35,
\qquad45-24.
\]

This is `m_0^star`. The identity-hexagon stabiliser is transitive on the six turns, and `S_5` is transitive on the ten identity hexagons. ∎

### Exact finite certificate

Direct enumeration verifies the uniqueness statement for all:

- ten simple Petersen `C6` cycles;
- six turns of each cycle;
- four root-valued star matchings at each turn.

There are no exceptional cells.

---

## 5. The shared turn corollas

Define the root-labelled cubic corolla

\[
\boxed{
R_i
=(p_{i-1},p_{i+1},z_i).}
\]

It is root-valued because

\[
p_{i-1}+p_{i+1}=z_i.
\]

In the canonical star for `B_i`, the two pivot-pair outer vertices are:

\[
(p_{i-1},p_{i+1};z_i)=R_i,
\]

and

\[
(p_i,p_{i+2};z_{i+1})=R_{i+1}.
\]

Therefore:

### Theorem 5.1 — adjacent-cell overlap compatibility

The canonical sections of consecutive cells `B_i` and `B_(i+1)` induce literally the same labelled corolla

\[
\boxed{R_{i+1}}
\]

on their common turn.

The equality is not merely up to support permutation: the two boundary pivot roots, the side root, and their three incidence labels agree term by term.

### Proof

The right pivot-pair outer vertex of the `i`-th star is

\[
(p_i,p_{i+2},z_{i+1}).
\]

The left pivot-pair outer vertex of the `(i+1)`-st star is the same triple. ∎

### Corollary 5.2 — cyclic compatibility

The six canonical star sections glue cyclically at the level of all turn-corolla labels:

\[
R_0,R_1,\ldots,R_5,R_0.
\]

There is no vertex-label monodromy around the identity hexagon.

---

## 6. The side-triangle corollas

The third outer vertex of the `i`-th star pairs the two side ports

\[
z_i,\quad z_{i+1}
\]

and has internal spoke

\[
z_{i+2}.
\]

Denote it by

\[
\boxed{
D_i=(z_i,z_{i+1},z_{i+2}).}
\]

Since `z_(i+3)=z_i`, one has:

### Theorem 6.1 — antipodal side compatibility

\[
\boxed{D_{i+3}=D_i}
\]

as a completely root-labelled corolla, up to reversal of the two displayed exterior side ports.

Thus the two occurrences of each side-triangle chart on opposite halves of the identity hexagon have identical root data.

This is exactly the static half-turn agreement absent from the older support-only identity-hexagon discussion: it is proved here for the canonical local star section, not asserted for the original physical half histories.

---

## 7. The internal equality dipole

Let `O_i` be the central vertex of the `i`-th star. Its incident roots are

\[
(z_{i+1},z_i,z_{i+2}),
\]

which is the same unordered root triangle as `D_i`.

The edge joining `O_i` to `D_i` has value

\[
z_{i+2}.
\]

Hence:

### Theorem 7.1 — canonical equality pair

The two vertices

\[
O_i,\quad D_i
\]

are equal support triangles joined along the root `z_(i+2)`. They form a legal equal-face dipole.

Cancelling that dipole preserves all six exterior roots of the star and leaves the two turn corollas `R_i,R_(i+1)` root-valued.

### Significance

Each canonical star section contains its own strict-order exit. The star is therefore not a new irreducible six-port carrier. Once a coherent relative movie reaches this section, one equal-face cancellation lowers the cap-context order by two or exposes the established category alternative.

The missing issue is reaching all six canonical sections coherently from the original Ptolemy annulus, not disposing of the sections after they are reached.

---

## 8. The canonical section complex

Define `T_C6^star` by taking six copies of the canonical star charts and recording the overlap identifications

\[
R_{i+1}^{(i)}=R_{i+1}^{(i+1)}
\qquad(i\bmod6).
\]

Also record the antipodal side-chart identities

\[
D_{i+3}=D_i.
\]

### Theorem 8.1 — static section consistency

`T_C6^star` assigns one unambiguous root label to every source incidence appearing in more than one canonical local chart.

In particular:

1. all consecutive-turn overlaps agree;
2. all repeated side-triangle charts agree;
3. every local central equation is root-valued;
4. every local chart preserves its complete six-port boundary word;
5. the ordered exterior side-root word remains
   \[
   (a,b,c,a,b,c).
   \]

Thus the canonical sections solve the **local-cell root-completion** and **history-vertex endpoint compatibility** parts of the corrected tube-lift target.

---

## 9. What remains for a coherent history lift

The original co-root four-vertex path and the canonical star have the same six labelled boundary ports but different assignments of those ports to internal source vertices.

Consequently one must still construct, for every `i`, a relative root-valued movie

\[
\boxed{
\text{original boundary lift near }B_i
\rightsquigarrow
S_i^\star
}
\]

using:

- root-preserving six-leaf NNI moves;
- equal-face insertion/cancellation;
- or one explicitly normalized critical transition;

while fixing the overlap corollas already shared with neighbouring cells.

The complete six-leaf root sector for a pivot boundary is connected, so an unrestricted boundary-preserving root-NNI path to `S_i^star` exists whenever one root topology is available. What is not yet proved is the **relative** version fixing both overlap corollas throughout the path and making the six local movies agree at every intermediate history state.

### Revised primitive target

The sole remaining even-track theorem is now:

> **Relative `C6` star-movie theorem.** The six canonical sections `S_i^star` admit relative root-valued NNI/cancellation movies from the two boundary lifts of the Ptolemy annulus, with the shared turn corollas `R_i` fixed throughout and with compatible intermediate states on every overlap.

Once this theorem holds:

1. every canonical star exposes an equal-face cancellation;
2. the `C6` track enters strict target-order descent;
3. every `C8` track reduces to two `C6` cells by `PETERSEN_C8_TWO_C6_HISTORY_FILLING_REDUCTION_V1.md`;
4. all even closed tracks are consumed;
5. contextual inverse transfer becomes unconditional at this interface.

---

## 10. Exact progress relative to the scope correction

The correction `PTOLEMY_ROOT_TUBE_HISTORY_LIFT_SCOPE_CORRECTION_V1.md` required:

1. local cell parametrisation;
2. history-vertex compatibility;
3. history-edge compatibility;
4. exterior identity;
5. boundary identity;
6. equivalence with cycle solutions.

For the only primitive even orbit, this dossier establishes:

- an explicit canonical local root completion at every cell;
- uniqueness of that completion under the fixed side-triangle condition;
- complete compatibility on shared turn vertices;
- complete compatibility on repeated side-triangle charts;
- preservation of all exterior six-port root words;
- one built-in equality cancellation per canonical cell.

It does **not** yet establish:

- relative history-edge movies from the original cell lifts;
- compatibility of their intermediate states;
- the converse classification of every coherent lift;
- unconditional even-track removal.

This is a strict reduction of the gap, not a restoration of the earlier overclaimed tube theorem.

---

## 11. Trust boundary

### Exact here

- uniform formula for every canonical `C6` star matching;
- root-valuedness and internal side-triangle labels;
- uniqueness among the four admissible star completions;
- all adjacent turn-corolla overlap identities;
- all antipodal side-corolla identities;
- the internal equal-face dipole in every canonical section;
- construction of the static section complex `T_C6^star`;
- reduction of the coherent-lift gap to relative star movies.

### Still open

- the relative `C6` star-movie theorem;
- graph/category-safe execution or separator extraction for its NNI paths;
- simultaneous compatibility of all six intermediate movies;
- unconditional even-track removal;
- unconditional contextual inverse transfer, full-channel lock elimination, and global closure;
- downstream proof development, curation, formalisation, manuscript, release, and publication layers.
