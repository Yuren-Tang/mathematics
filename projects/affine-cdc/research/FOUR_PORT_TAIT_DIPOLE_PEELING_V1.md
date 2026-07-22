# Universal dipole peeling for four-port Tait cells

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `fb94c47b1b18f3a05f519a4e8a7fbc6287d48d22`  
**Parents:**

- `projects/affine-cdc/research/NEGATIVE_EULER_TAIT_DIPOLE_REDUCTION_V1.md`;
- `projects/affine-cdc/research/LOW_PORT_TAIT_CORE_GLUING_V1.md`;
- `projects/affine-cdc/research/FOUR_POLE_CAP_LIBRARY_TEN_STATE_PROFILES_V1.md`;
- `projects/affine-cdc/research/TYPE_T_KERNEL_SQUARE_ENVELOPE_V1.md`.

**Status:** exact all-size peeling theorem for connected four-port properly three-edge-coloured multipoles. A four-port Tait multipole can never be dipole-free. Repeated cancellation of response-preserving one-dipoles strictly removes two vertices until a bounded two-vertex event is exposed: an open--open matching flip or the double-boundary two-port degeneration. Re-expansion in the complete root cover has only the previously classified root/equality/DDD lift table. Thus no large four-port Tait component is an irreducible composition atom.  
**Not implied:** automatic elimination of the residual matching edge sector, that every bounded matching flip is already compatible with the ambient locked profile, preservation of bridgelessness without recording a separator, canonical acceptance, Lean verification, manuscript readiness, or the global five-support theorem.

---

## 1. Setup

Let `T` be a finite connected cubic multipole with exactly four boundary semiedges and a proper edge colouring by

\[
\{i,j,k\}.
\]

At every source vertex, exactly one incidence of each colour occurs.

For a colour pair, write

\[
T_{ij},\quad T_{ik},\quad T_{jk}
\]

for the corresponding bicoloured residue systems. Each component is an alternating cycle or an alternating boundary-to-boundary path.

An internal colour-`i` edge `uv` is an `i`-dipole when `u,v` lie in distinct components of `T_{jk}`.

---

## 2. Four ports force a one-dipole

### Theorem 2.1 — no dipole-free four-port Tait multipole

Every connected four-port properly three-edge-coloured multipole contains a coloured one-dipole.

### Proof

Assume that `T` contains no one-dipole in any colour.

The connected-residue theorem then gives that each of

\[
T_{ij},\quad T_{ik},\quad T_{jk}
\]

is connected. A connected two-regular multipole residue is either one closed cycle, with no boundary endpoints, or one open path, with exactly two boundary endpoints.

If

\[
(b_i,b_j,b_k)
\]

are the boundary semiedge counts by colour, then

\[
b_i+b_j,\quad b_i+b_k,\quad b_j+b_k\in\{0,2\}.
\]

Summing gives

\[
2(b_i+b_j+b_k)\le6,
\]

so the total boundary size is at most three. This contradicts

\[
b_i+b_j+b_k=4.
\]

Therefore a one-dipole exists. ∎

### Significance

This is an all-size theorem. No finite vertex census is required for four-port Tait cells.

---

## 3. One peeling step

Let `e=uv` be a colour-`i` one-dipole. Let `R_u,R_v` be the two distinct complementary `jk` residues through its endpoints.

Exactly one of the following occurs.

### Type P — response-preserving peel

At most one of `R_u,R_v` is open. Then ordinary colourwise cancellation produces a connected properly coloured four-port multipole

\[
T/e
\]

with

\[
\boxed{|V(T/e)|=|V(T)|-2}
\]

and identical ordered Tait boundary response:

\[
\boxed{\mathfrak R(T/e)=\mathfrak R(T).}
\]

### Type F — open--open matching flip

Both `R_u,R_v` are open. Cancellation preserves the boundary colour word and two of the three bicoloured endpoint matchings. The third matching is changed only on the four endpoints of `R_u,R_v`, where it becomes the other perfect matching produced by colourwise splicing.

Thus the complete response change is one bounded four-port matching flip.

### Type B — double-boundary degeneration

For one of the two colours `j,k`, the incidences paired by cancellation are both boundary semiedges. The two-vertex neighbourhood is already a bounded two-port or four-port carrier and is retained rather than cancelled inside the cubic category.

No fourth local event exists.

---

## 4. Termination of response-preserving peeling

### Theorem 4.1 — first-event decomposition

Starting from any connected four-port Tait multipole, repeatedly cancel a Type-P dipole whenever one is available.

The process terminates after finitely many steps and exposes a first bounded event of Type F or Type B.

### Proof

Every Type-P step decreases the number of source vertices by two and preserves the four boundary semiedges and the complete ordered Tait response.

Suppose the process stopped without a Type-F or Type-B event. The terminal connected four-port multipole would contain no cancellable one-dipole. Since every one-dipole not of Type P is, by definition, Type F or Type B, it would be dipole-free. This contradicts Theorem 2.1. ∎

### Corollary 4.2 — no large irreducible four-port Tait response

Every connected four-port Tait multipole is response-equivalent, through a strictly vertex-decreasing sequence, to a configuration in which one two-vertex neighbourhood carries the only remaining composition event.

Therefore arbitrary internal genus, flat length, or number of Tait vertices cannot produce a new irreducible four-port response language.

---

## 5. Reverse lifting in the root cover

Consider one Type-P cancellation. In the smaller multipole, the two colourwise reconnected edges receive root values

\[
p,q\in R_5.
\]

Reinserting the two cancelled cubic vertices forces the restored dipole edge to have value

\[
r=p+q.
\]

### Theorem 5.1 — complete inverse-peel table

Exactly one of the following occurs.

1. **Root lift**  
   `p,q` are distinct intersecting roots. Then `r=p+q` is the third root of their `K5` triangle and the expansion is root-valued.

2. **Equality cell**  
   `p=q`. Then `r=0`, giving the bounded zero/equality two-vertex unit.

3. **DDD cell**  
   `p,q` are disjoint roots. Then `r=p+q` is a co-root, giving exactly the one-co-root-edge DDD atom and its two crossed root resolutions.

No fourth inverse-peel obstruction exists.

### Corollary 5.2 — iterated lifting

Let

\[
T=T_0\to T_1\to\cdots\to T_m
\]

be a response-preserving peel sequence ending at its first Type-F or Type-B event.

Any root-valued cover of `T_m` can be expanded backwards until either:

1. it reaches a root-valued cover of `T`; or
2. the first failed expansion localises one bounded equality cell; or
3. the first failed expansion localises one bounded DDD cell.

The length of the peel sequence creates no new lift-failure state.

---

## 6. Relation to the cap--square library

The terminal first event lies in the already complete four-port alphabet.

### Type F

An open--open dipole changes one terminal matching on four endpoints. The inverse-peel values fall into the route-sum table:

\[
(0,2,2),\quad(0,4,4),\quad(2,2,4),\quad(0,0,0).
\]

Hence its root-level realisations are carried by:

- a two-vertex cap in the root branch;
- a zero/equality unit;
- a DDD/co-root atom with two crossed resolutions;
- or the Type-T square carrier in the disjoint doubled branch.

### Type B

The double-boundary degeneration is already a two-port carrier. Its root boundary is universal up to one support permutation and glues by the two-cut theorem, unless the degeneration exposes a bridge/separator branch.

### Theorem 6.1 — finite terminal alphabet

Every connected four-port Tait component enters, after strict response-preserving peeling, one of:

\[
\boxed{
\text{root dipole/cap},
\quad
\text{Type-T square},
\quad
\text{zero/equality},
\quad
\text{DDD},
\quad
\text{two-port separator}.}
\]

No additional bounded graph carrier is required.

---

## 7. Strict descent measure

For one four-port Tait component define

\[
\mathcal D_T(T)
=
\bigl(
|V(T)|,
\varepsilon_F(T),
\varepsilon_B(T)
\bigr),
\]

where the last two coordinates record whether a matching-flip or boundary-degeneration event has been exposed.

Before the first event, every peel step strictly lowers `|V|` while preserving the full ordered response. At the first event, the component leaves the unbounded Tait category and enters the finite cap--square--DDD alphabet.

Thus the vertex coordinate alone is a valid well-founded descent on the unbounded four-port Tait sector.

---

## 8. Consequence for the matching-plus-Tait interval

In the side decomposition attached to a private root shift:

- isolated shift-coloured edges form the matching sector;
- every other connected side component is a rank-two Tait multipole.

### Corollary 8.1

No Tait component of a minimal laminar four-port interval can remain as an unbounded irreducible obstruction.

It either:

1. peels strictly;
2. exposes a four-port matching flip;
3. exposes a two-port separator;
4. localises an equality or DDD atom;
5. enters the Type-T square interface.

Therefore the only side-network sector not yet covered by an all-size peeling theorem is the isolated shift-edge matching sector and its interaction with the ordered laminar boundary.

---

## 9. Trust boundary

### Exact here

- every connected four-port properly three-edge-coloured multipole contains a one-dipole;
- response-preserving two-vertex peeling;
- termination at an open--open flip or double-boundary event;
- complete iterated root/equality/DDD inverse-lift table;
- reduction of all-size four-port Tait cells to the existing finite cap--square--DDD alphabet;
- vertex count as a strict measure on the unbounded four-port Tait sector.

### Still open

- composition-safe action on the exposed finite event in every locked ambient profile;
- preservation of bridgelessness under a peel, or extraction of the resulting separator;
- the isolated shift-edge matching sector;
- universal Type-T square-envelope transfer;
- packaging with horizontal/global induction;
- the global five-support theorem.
