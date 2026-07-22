# Five-leaf contextual return circuits: even `C6` erases and odd `C5` cannot close

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `bbd25d7477d6c44dda667f2bbaa92e0ab4d6da01`.

**Parents:**

- `FIVE_LEAF_ROOT_TOPOLOGY_CYCLE_CLASSIFICATION_V1.md`;
- `FIVE_LEAF_PACHNER_PENTAGON_ROOT_INTERVAL_V1.md`;
- `PETERSEN_RESOLUTION_PARITY_V1.md`;
- `PETERSEN_CYCLE_MONODROMY_V1.md`;
- `ORIENTED_CHANNEL_LOCK_BOUNDARY_CALIBRATION_V1.md`;
- `PACHNER_FIRST_FAILURE_CRITICAL_OVERLAP_V1.md`.

**Status:** exact disposition of the only two closed five-leaf root-reconfiguration circuits. For a support-five-cycle boundary, the five root-valued topologies are canonically the five pivots of one Petersen `C5`; each topology edge is one DDD switch state and its third resolution is the co-root missing from the two pivot roots. A full lap has odd resolution parity and exchanges the ordered cap shore, so it cannot close inside an oriented full-channel lock. For a triangle-plus-double boundary, the root sector is `C6`; every topology has a unique internal root assignment, and a full six-step lap returns exactly to the same labelled graph, flow, and resolution sheet. It is therefore an erasable identity subhistory. Hence a normalized one-atom contextual-transfer schedule has no nontrivial local return circuit.

**Not implied:** that every global mixed surgery history is generated only by one isolated five-leaf critical circuit without a coherence argument, complete contextual-transfer synthesis, final proof-DAG closure, canonical acceptance, independent audit, Lean verification, manuscript integration, release, publication, or the global five-support theorem.

---

## 1. Generic two-resolution bit on an NNI edge

Fix four rooted branches with conserved root boundary. Whenever two of the three binary resolutions are root-valued, the third resolution is zero or co-root.

Call the two root-valued resolutions the two **sheets** of that singular triality. Traversing the NNI edge from one root topology to the other exchanges the two sheets.

This agrees with the established DDD resolution fibre when the third value is a co-root. In the zero branch it is the same two-root-resolution involution for the `(0,2,2)` pairing-sum pattern.

Thus every edge of a root-valued topology graph carries one canonical sheet flip.

### Lemma 1.1 — circuit parity

Along a root-valued topology circuit of length `n`, the composite sheet action is

\[
\boxed{n\pmod2.}
\]

An even circuit preserves the sheet and an odd circuit exchanges it.

---

## 2. The support-five-cycle boundary

Let the five boundary roots be the edges of one simple support cycle

\[
e_0,e_1,e_2,e_3,e_4,e_0
\]

in `K_5`, ordered so consecutive `e_j` meet.

The root-topology classification gives exactly five valid five-leaf trees. Each is uniquely determined by its singleton, i.e. the unique boundary root not belonging to either cherry.

### Lemma 2.1 — singleton topology

For every boundary root `e_j`, there is exactly one root-valued topology whose singleton is `e_j`.

### Proof

Deleting `e_j` from the support cycle leaves a four-edge path. The only way to partition those four boundary edges into two root-valued cherries is to pair the two adjacent edges at each end of the path. Each cherry sum is a root, and conservation gives the central root triangle. Uniqueness follows because the alternate pairing uses one disjoint pair. ∎

---

## 3. The topology `C5` is exactly a Petersen pivot cycle

Two singleton topologies differ by one root-valued NNI exactly when their singleton roots are disjoint.

On the five edges of a support `C5`, disjointness is the complement of adjacency. The complement of `C5` is again `C5`.

Choose the disjointness order

\[
s_0,s_1,s_2,s_3,s_4,s_0.
\]

### Theorem 3.1 — canonical Petersen dictionary

The map

\[
\boxed{
T_j\longmapsto s_j
}
\]

from a root topology to its singleton root is a graph isomorphism

\[
\boxed{
C_5^{\mathrm{top}}
\cong
C_5^{\mathrm{Petersen}}
\subset KG(5,2).}
\]

Hence:

- topology vertices are Petersen pivots;
- root NNI edges are Petersen switch states;
- the topology circuit is one of the twelve simple Petersen five-cycles.

---

## 4. The five singular neighbours are the five DDD co-roots

Let adjacent topology pivots be the disjoint roots

\[
s_j,s_{j+1}.
\]

Their union contains four support indices. Let

\[
i_j=[5]\setminus(s_j\cup s_{j+1})
\]

be the omitted index.

The third NNI resolution has central value

\[
s_j+s_{j+1}.
\]

Since the roots are disjoint,

\[
\boxed{
s_j+s_{j+1}=Q_{i_j}.}
\]

### Theorem 4.1 — co-root rim

Every edge of the topology `C5` carries exactly the DDD state

\[
F_j=\{s_j,s_{j+1}\}
\]

with co-root third resolution

\[
Q_{i_j}.
\]

The five omitted indices are pairwise distinct, so the five outside singular neighbours are exactly

\[
\boxed{Q_1,Q_2,Q_3,Q_4,Q_5}
\]

up to support relabelling.

Thus the topology five-cycle and the Petersen/DDD five-cycle are the same finite resolution object, not merely cycles of the same length.

---

## 5. Odd return cannot close in an oriented cap lock

By the resolution-parity theorem, every DDD switch exchanges the two root-resolution sheets. Therefore the five-edge circuit satisfies

\[
\boxed{
\operatorname{Hol}_{\mathrm{res}}(C_5)=1.}
\]

Equivalently, the type-`41` Petersen support monodromy exchanges the two endpoints of the initial DDD state.

In the physical inverse-dipole setting, the deleted cap distinguishes the two blocks of the locked terminal matching. The oriented-channel-lock theorem states that physical transport preserves this distinguished block; the transport subgroup lies in the appropriate no-block-exchange kernel.

### Theorem 5.1 — no oriented `C5` return

A first-failure co-root atom cannot be relocated once around the topology `C5` and return to the same oriented outer lock.

### Proof

The five local exchanges toggle the resolution sheet an odd number of times. A completed lap would return the labelled source topology and root boundary but send the distinguished cap shore to the opposite resolution sheet. Oriented cap transport forbids that exchange. ∎

### Corollary 5.2

A normalized atom relocation entering the `C5` sector must, before completing a lap, produce one of:

1. route/profile change and cap escape;
2. separator/category exit;
3. a smaller recursive target;
4. termination of the inverse transfer.

It cannot be a closed scheduling circuit.

---

## 6. Triangle-plus-double boundary and the topology `C6`

Assume the boundary support multigraph is one triangle plus one doubled root, and that the doubled root is not the complementary edge disjoint from the triangle. The root-topology classification gives one cycle

\[
\boxed{C_6^{\mathrm{top}}.}
\]

For a fixed labelled boundary word, every five-leaf topology has at most one possible internal root assignment: each cherry edge is forced to be the sum of its two boundary roots, and the central labels are then forced by conservation.

### Lemma 6.1 — uniqueness of the local root flow

Every root-valued topology in the `C6` sector carries exactly one internal root labelling extending the fixed ordered boundary word.

---

## 7. A full `C6` lap is the identity

Traverse all six root NNI edges of the topology cycle. The final labelled topology is the initial labelled topology. By Lemma 6.1, its internal root labelling is also the initial one.

The sheet action is the product of six transpositions, hence is trivial.

### Theorem 7.1 — even identity return

The complete six-step topology lap acts trivially on:

1. the five labelled external incidences;
2. the source tree topology;
3. every internal root value;
4. the singular-resolution sheet.

Therefore it is the identity transformation of the complete local contextual-transfer state.

### Corollary 7.2 — erasable `C6` lap

If a normalized surgery/return schedule contains one complete local `C6` lap, delete the six moves. The schedule has the same input graph, output graph, root flow, boundary word, and resolution demand, but strictly shorter length.

Hence no length-minimal transfer schedule contains a complete `C6` lap.

This is the source-level identity-return counterpart of the even Petersen/identity sector; no affine or route residue survives because the full labelled local state, not only support monodromy, has returned exactly.

---

## 8. Complete circuit disposition

The complete five-leaf root-topology theorem says that every nonempty local root sector is `C5` or `C6`.

### Theorem 8.1 — no nontrivial local return circuit

In a length-minimal normalized contextual-transfer schedule:

- a `C5` lap is impossible by oriented resolution parity;
- a `C6` lap is removable and therefore absent.

Thus a one-atom relocation cannot return locally to its starting enriched state through any five-leaf Pachner circuit.

There is no third local circuit type.

---

## 9. Consequence for the final scheduling theorem

Together with:

- strict commutation of disjoint moves;
- the root-interval theorem on every overlapping pentagon;
- immediate normalization of the only bad co-root overlap;
- strict target-order descent of genuine equality/DDD recursive calls;
- cap escape from every route-changing matching flip;
- complete disposition of the zero-vertex direct-pairing terminal;

Theorem 8.1 removes the last bounded circuit candidate in one-atom transfer scheduling.

What remains is a proof-combinatorial coherence statement:

> every closed global rescheduling loop of local NNI/cancellation moves contains a disjoint square or an overlapping five-leaf circuit, so the preceding local relations reduce it.

Once that standard local-to-global coherence statement is established in the present cubic incidence setting, contextual inverse transfer is well founded.

---

## 10. Trust boundary

### Exact here

- singleton classification of root five-leaf topologies for support-cycle boundaries;
- graph isomorphism between topology `C5` and the Petersen disjointness `C5`;
- identification of topology edges with DDD switch states;
- identification of the five failed resolutions with the five co-roots `Q_i`;
- odd resolution parity and contradiction with ordered cap-shore preservation;
- uniqueness of the internal root flow for fixed five-leaf topology and boundary;
- complete identity action of one topology `C6` lap;
- erasability of every complete `C6` lap;
- complete local disposition of the only two five-leaf root circuits.

### Still open

- local-to-global coherence for arbitrary overlapping Pachner/cancellation histories on the triangle pseudocomplex;
- complete contextual-transfer synthesis from that coherence theorem;
- final proof-DAG audit and well-founded packaging;
- canonical acceptance, independent audit, Lean verification, manuscript integration, release, publication;
- the global five-support theorem.
