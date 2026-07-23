# Every Petersen `C8` filling reduces to two compatible `C6` identity fillings

## Research dossier v1 — exact combinatorial and side-root reduction

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `44c37660786535ecc8d95fd16c30ad96a635f680`.

**Parents:**

- `PTOLEMY_ROOT_TUBE_HISTORY_LIFT_SCOPE_CORRECTION_V1.md`;
- `PETERSEN_SIMPLE_CYCLE_OUTPUT_CLASSIFICATION_V1.md`;
- `PETERSEN_IDENTITY_HEXAGON_SIX_CHANNEL_TRIALITY_V1.md`;
- `PETERSEN_PIVOT_RESOLUTION_V1.md`;
- `PTOLEMY_EVEN_TRACK_ROOT_TUBE_FILLING_V1.md`.

**Status:** exact reduction of the even-track history-lift obligation. Every simple eight-cycle in the Petersen graph omits one Petersen edge `rr'`. Using either omitted endpoint `r`, the eight-cycle is the symmetric difference of two simple six-cycles sharing the two-edge path `a-r-b`, where `a,b` are the two neighbours of `r` on the eight-cycle. The emitted side-root data of the two six-cycles agree with the eight-cycle away from `a,b`; their two emissions at the shared middle vertex `r` are both `r'`; and at each endpoint `a,b` the two six-cycle emissions together with the eight-cycle emission form one root triangle. Consequently any exterior-preserving coherent history lift for the two `C6` identity cells glues, through one internal `r'` identification and two root-triangle seam vertices, to an exterior-preserving coherent lift of the original `C8` cell. Hence the annular Ptolemy tube-lift problem for even simple tracks reduces to the single primitive `C6` identity-cell realisation problem.

**Assurance boundary:** this dossier does not itself prove the primitive coherent `C6` history-cell lift. It therefore does not yet restore unconditional contextual inverse transfer or the global five-support candidate. It removes the need for a separate primitive `C8` lift theorem.

---

## 1. Petersen notation and emitted side roots

Let

\[
P=KG(5,2)
\]

be the Petersen graph. Its vertices are the ten roots

\[
R_5=\{ij:1\le i<j\le5\},
\]

and two vertices are adjacent exactly when the corresponding roots are disjoint.

Let

\[
C=(v_0,v_1,\ldots,v_{m-1},v_0)
\]

be a simple cycle in `P`. At one cycle vertex `v_i`, the Petersen graph has exactly three neighbours. Two are the cycle neighbours

\[
v_{i-1},v_{i+1}.
\]

Define the emitted side root of `C` at `v_i` to be the third neighbour

\[
\boxed{
\zeta_C(v_i)
=
N_P(v_i)\setminus\{v_{i-1},v_{i+1}\}.}
\]

The neighbour set of one Petersen vertex `v` consists of the three two-subsets of the complementary three-set `[5]\setminus v`. These three roots form one support triangle and sum to zero.

Thus at every pivot:

\[
\boxed{
\text{previous pivot}
+
\text{next pivot}
+
\text{emitted side root}
=0.}
\]

This is the Petersen transition/root-triangle law.

---

## 2. The complement of a simple `C8`

Let

\[
C\subset P
\]

be one simple eight-cycle. Exactly two Petersen vertices do not lie on `C`; call them

\[
r,r'.
\]

### Lemma 2.1 — the omitted vertices are adjacent

\[
\boxed{r\perp r'.}
\]

Equivalently, `{r,r'}` is one Petersen edge.

### Proof

Suppose instead that `r,r'` are nonadjacent. In the Kneser model they are intersecting roots. Two intersecting roots have exactly one common Petersen neighbour: the unique root on the two support indices outside their union.

That common neighbour lies on `C`, since only `r,r'` are omitted. It would then be incident with:

- its two cycle edges in `C`;
- one edge to `r`;
- one edge to `r'`.

This gives degree at least four, contradicting cubicity of the Petersen graph. Therefore `r,r'` are adjacent. ∎

### Corollary 2.2 — eight-cycles and omitted Petersen edges

The map

\[
C\longmapsto P-V(C)
\]

sends every simple `C8` to one edge of `P`.

There are fifteen Petersen edges and fifteen unoriented simple eight-cycles. Exact enumeration shows the map is bijective. Equivalently, for every Petersen edge `{r,r'}` there is exactly one simple eight-cycle on the other eight vertices.

The human argument below needs only adjacency; the exact `15/15` bijection is a finite certificate and makes the `S_5` orbit structure transparent.

---

## 3. Two canonical six-cycle decompositions

Fix one omitted vertex `r`. Its three Petersen neighbours are:

\[
r',a,b,
\]

where `a,b` lie on `C`.

The two vertices `a,b` split the eight-cycle into two internally disjoint arcs

\[
A_+,
\qquad
A_-
\]

from `a` to `b`.

### Lemma 3.1 — both arcs have length four

Each arc contains exactly four cycle edges.

### Proof

By `S_5` transitivity on Petersen edges, normalize

\[
r=12,
\qquad
r'=34.
\]

The remaining eight vertices carry the unique simple eight-cycle

\[
13,25,14,35,24,15,23,45,13.
\]

The two neighbours of `12` on this cycle are `35,45`, and they are antipodal: each arc has length four.

The statement is invariant under the `S_5` action. ∎

A purely graph-theoretic alternative is to use the exact uniqueness of the `C8` complementary to one edge and inspect one normalized edge.

Add the path

\[
a-r-b
\]

to each arc. Since each arc has length four, this gives two simple six-cycles:

\[
H_+=A_+\cup\{a-r,r-b\},
\]

\[
H_-=A_-\cup\{a-r,r-b\}.
\]

### Theorem 3.2 — canonical `C8=C6 triangle C6` decomposition

\[
\boxed{
E(C)=E(H_+)\mathbin\triangle E(H_-).}
\]

The two six-cycles share exactly the two-edge path

\[
\boxed{a-r-b.}
\]

The same construction using the other omitted vertex `r'` gives a second canonical decomposition.

### Standard representative

For

\[
C=(13,25,14,35,24,15,23,45),
\]

choose

\[
r=12,
\qquad
r'=34,
\qquad
a=35,
\qquad b=45.
\]

Then

\[
H_+=(12,35,14,25,13,45),
\]

\[
H_-=(12,35,24,15,23,45).
\]

Their shared path is

\[
35-12-45,
\]

and their symmetric difference is exactly `C`.

Exact enumeration of all ten Petersen `C6` cycles and all fifteen `C8` cycles gives three unordered `C6`-pair decompositions of every `C8`; the two omitted-vertex constructions are the two decompositions with a connected two-edge intersection. Only one is needed below.

---

## 4. Side-root agreement away from the seam

Let

\[
v\in V(C)\setminus\{a,b\}.
\]

Then `v` belongs to exactly one of the two arcs and hence to exactly one of `H_+,H_-`. Its two neighbours in that six-cycle are the same as its two neighbours in `C`.

Therefore:

### Lemma 4.1 — unchanged exterior emissions

\[
\boxed{
\zeta_{H_\pm}(v)=\zeta_C(v)
\qquad(v\ne a,b).}
\]

Thus every side-root occurrence away from the seam endpoints is literally unchanged by the two-hexagon decomposition.

---

## 5. The shared middle output

At the inserted pivot `r`, both six-cycles have the same two cycle neighbours `a,b`. The third Petersen neighbour of `r` is `r'`.

### Lemma 5.1 — middle emissions agree

\[
\boxed{
\zeta_{H_+}(r)
=
\zeta_{H_-}(r)
=
r'.}
\]

Hence the two identity-hexagon cells have one equal side-root occurrence `r'` along their common interior. These occurrences may be identified as one internal root-labelled edge; they do not appear on the exterior `C8` boundary.

In the normalized representative, both middle emissions are `34`.

---

## 6. Root-triangle seams at the two endpoints

At endpoint `a`, write its two neighbours on the original eight-cycle as

\[
a_+\in A_+,
\qquad
a_-\in A_-.
\]

The complete Petersen neighbour set of `a` is

\[
\boxed{N_P(a)=\{r,a_+,a_-\}.}
\]

Indeed `a` is adjacent to `r` and to its two cycle neighbours; cubicity leaves no fourth neighbour.

The emitted roots are therefore:

\[
\zeta_{H_+}(a)=a_-,
\]

\[
\zeta_{H_-}(a)=a_+,
\]

\[
\zeta_C(a)=r.
\]

Since the three neighbours of one Petersen vertex form the root triangle on the complementary three-set,

\[
\boxed{
a_-+a_++r=0.}
\]

### Theorem 6.1 — endpoint seam triangle

The two six-cycle side roots at `a` and the required exterior eight-cycle side root at `a` are exactly the three incident roots of one root-valued cubic vertex.

The identical statement holds at `b`.

### Standard representative

At `a=35`:

- `H_+` emits `24`;
- `H_-` emits `14`;
- `C` emits `12`;

and

\[
24+14+12=0.
\]

At `b=45`:

- `H_+` emits `23`;
- `H_-` emits `13`;
- `C` emits `12`;

and

\[
23+13+12=0.
\]

These are exact root triangles.

---

## 7. Composition theorem for coherent history cells

Use the phrase **coherent `C6` identity-cell lift** for a root-valued lift of one complete Petersen `C6` history cell which:

1. realises every history vertex and history edge of that cell;
2. fixes every emitted side-root incidence;
3. is the identity on all data outside the cell;
4. returns the same ordered outer state and resolution sheet after the six-step circuit.

This is precisely the primitive history-space assertion still missing after `PTOLEMY_ROOT_TUBE_HISTORY_LIFT_SCOPE_CORRECTION_V1.md`.

### Theorem 7.1 — two-hexagon gluing

Assume coherent identity-cell lifts are available for `H_+` and `H_-` with their exact side-root words. Then they glue to a coherent root-valued filling of the `C8` boundary data.

### Construction

1. Glue the two history cells along the common two-edge pivot path `a-r-b`.
2. Identify their equal middle side-root incidences `r'` at `r`; this becomes internal.
3. At `a`, attach one root-triangle seam vertex to the two six-cell emissions and the required exterior root `zeta_C(a)=r`.
4. Do the same at `b`.
5. Along every other boundary position, use Lemma 4.1 to identify the six-cell side root directly with the corresponding `C8` exterior side root.

Every new source vertex introduced by the seam is root-valued by Theorem 6.1. Every internal identification joins equal root labels. All history vertices and edges inside the two component identity cells remain legal by hypothesis.

Therefore the resulting composite:

- fixes the complete exterior `C8` side word;
- changes no outside source edge or root label;
- preserves the ordered cap route and shore data;
- contains no co-root track on its interior boundary;
- supplies a coherent root history filling of the original eight-cycle track.

### Corollary 7.2 — no independent `C8` primitive is needed

\[
\boxed{
\text{coherent Petersen }C6\text{ identity lift}
\Longrightarrow
\text{coherent Petersen }C8\text{ lift}.}
\]

This implication is `S_5`-equivariant and covers every simple `C8`.

---

## 8. Relation to the abstract longitudinal filling

The earlier abstract `C8` tube word

\[
(25,45,35,25,15,35,45,15)
\]

correctly solves the cycle-multipole equations for the standard `C8` side word. The history-lift correction observed that this does not automatically label all source graphs in the original Ptolemy annulus.

The present theorem does not attempt that unsupported pointwise relabelling. It instead factors the eight-cycle history cell into two smaller history cells whose complete coherent lifts are treated as the primitive input, and glues them using only:

- equality of one internal emitted root;
- two ordinary root-triangle seam vertices;
- unchanged side incidences elsewhere.

Thus it is a genuine composition reduction rather than a reinterpretation of the abstract longitudinal roots as original atom resolutions.

---

## 9. Revised exact tube-lift target

The missing annular history theorem can now be sharpened.

### Old target

Construct coherent history lifts separately for arbitrary even `C6` and `C8` tracks.

### Revised target

Prove one primitive theorem:

> Every simple Petersen `C6` first-failure track has an exterior-preserving coherent identity-cell lift.

Then:

- odd `C5,C9` tracks remain excluded by orientation parity;
- `C6` tracks are removed by the primitive theorem;
- `C8` tracks are removed by Theorem 7.1.

### Theorem 9.1 — one-orbit reduction

The entire even-track part of `AC-RL-PTOLEMY-TUBE-LIFT` reduces to one `S_5` orbit of Petersen identity hexagons.

There are ten such hexagons, one for every root, and `S_5` acts transitively. Hence one fully labelled representative history-cell construction, together with equivariance, is sufficient.

---

## 10. Exact finite certificates

Direct enumeration of the Petersen graph gives:

\[
\boxed{
\#C_6=10,
\qquad
\#C_8=15.}
\]

For every simple `C8`:

1. its omitted vertices form one Petersen edge;
2. each omitted endpoint gives one pair of `C6` cycles sharing a two-edge path;
3. hence there are two canonical connected-seam decompositions;
4. including the disconnected-edge decomposition, there are exactly three unordered `C6`-pair symmetric-difference representations;
5. the side-root identities of Sections 4--6 hold exactly.

For the standard representative the words are:

\[
\zeta_C=(24,34,23,12,13,34,14,12),
\]

\[
\zeta_{H_+}=(34,24,23,34,24,23),
\]

\[
\zeta_{H_-}=(34,14,13,34,14,13),
\]

with cyclic starting points chosen according to the displayed pivot orders.

The finite certificate checks the combinatorics; the neighbour-set/root-triangle proof is controlling.

---

## 11. Consequence for proof status

### Unconditionally closed here

- complete structural classification of a `C8` complement;
- canonical decomposition into two `C6` cycles with a connected two-edge seam;
- exact preservation of all nonseam side roots;
- equality of the two middle seam roots;
- root-triangle compatibility at both seam endpoints;
- reduction of coherent `C8` history filling to coherent `C6` identity filling.

### Still conditional

- existence of the primitive coherent `C6` identity-cell lift;
- removal of every even closed multi-cell defect track;
- same-order no-sink theorem;
- complete contextual inverse transfer;
- full-channel lock elimination;
- global minimal-counterexample closure.

The branch must continue to read `PTOLEMY_ROOT_TUBE_HISTORY_LIFT_SCOPE_CORRECTION_V1.md` as controlling until the primitive `C6` theorem is supplied.

---

## 12. Trust boundary

### Exact here

- all Petersen graph and side-root identities stated above;
- the two-hexagon composition theorem as a conditional gluing statement;
- the reduction from two even orbit types to one primitive identity-hexagon orbit.

### Not claimed

- that the existing abstract `C6` cycle-multipole filling is already a coherent history lift;
- that an identity support monodromy alone supplies the primitive cell;
- that every root flow on an identity-hexagon source graph realises the required history movie;
- any downstream assurance, formalisation, manuscript, release, or publication status.
