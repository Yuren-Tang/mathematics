# Scope correction: local Ptolemy relations do not yet prove global atom coherence

## Research dossier v1 — correction quarantine

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `c3a7499e6c809797edfb9e3f4d4d943928ae0f99`.

**Corrects:** `ROOT_FLOW_PTOLEMY_CONTEXTUAL_COHERENCE_V1.md`.

**Retains exactly:**

- reduction of every prime fixed-order root NNI block to flips on a fixed marked triangle surface;
- the standard external Ptolemy-groupoid presentation by involution, far commutativity, and pentagon;
- root involutivity;
- strict contextual commutation of disjoint moves;
- the one-pentagon root-interval theorem;
- nonbranching of one first-failure atom inside one pentagon;
- complete disposition of one local five-leaf `C5` or `C6` circuit;
- separation of strict cancellation descent from same-order Pachner scheduling.

**Quarantines:** the unconditional global conclusions labelled Theorems 8.1, 9.1, and 10.1 in the corrected dossier.

**Status:** exact logical correction. A van Kampen disk for the uncoloured flip history exists, but lifting its 2-cells one by one with one defect token requires a global flatness theorem. Local nonbranching inside every square or pentagon does not by itself imply that a closed defect track stays inside one five-leaf neighbourhood. The track may cross several 2-cells before returning. Therefore the local `C5/C6` classification does not yet exclude every global atom loop. The missing object is precisely a multi-cell DDD/equality transport backbone, already anticipated by the forced-backbone and Petersen-cycle programme.

**Not implied:** invalidity of the Ptolemy reduction, failure of the overall proof route, existence of a counterexample, canonical acceptance, Lean verification, manuscript integration, release, publication, or the global five-support theorem.

---

## 1. What the standard Ptolemy theorem supplies

For the underlying uncoloured marked surface, every closed flip history bounds a finite van Kampen diagram whose 2-cells are:

1. involution digons;
2. disjoint commutativity squares;
3. adjacent-flip pentagons.

This is sufficient to compare ordinary triangulation histories.

It does not automatically compare histories enriched by:

- root-admissibility restrictions;
- one zero/co-root first-failure atom;
- a resolution sheet;
- an ordered cap shore;
- route/profile semantics.

To lift the diagram, one needs a coherent transport rule for this enriched datum across all cells.

---

## 2. Exact local lift already proved

The following cellwise statements are exact.

### Involution

A flip followed by its inverse restores the same graph and root values.

### Disjoint square

Disjoint root surgeries commute. A defect atom disjoint from a move is unchanged, and a move meeting only one local support cannot create a second persistent atom after normalization.

### One pentagon

For one fixed five-root boundary:

- root topologies form one interval on the pentagon;
- failure does not leave and later re-enter the root interval;
- one atom moves to one interval endpoint without branching;
- a complete local `C5` has odd oriented resolution parity and cannot close;
- a complete local `C6` is an erasable identity lap.

Thus every individual Ptolemy 2-cell has a finite local contextual analysis.

---

## 3. The unsupported implication

The earlier dossier asserted:

> if a defect atom returns to the same enriched state during a lifted van Kampen reduction, its closed sector is one local `C5` or `C6`.

This implication is not established.

A token path may enter one pentagon, leave through a neighbouring square, pass through a second pentagon supported on a different five-leaf neighbourhood, and close only after traversing many cells. Its projection to the source graph or coefficient state graph can therefore be longer than five or six.

Local degree two of the track proves only that the defect locus is nonbranching. It does not bound the length or support of a closed component.

Consequently:

- local `C5/C6` disposition does not alone prove trivial global monodromy;
- finite-state repetition cannot yet be ruled out from those local facts;
- the unconditional fixed-order termination theorem is not yet available.

---

## 4. Correct global object

Along a co-root critical overlap, the atom changes by

\[
Q_i\longleftrightarrow Q_j
\]

through the root transport edge

\[
ij.
\]

Along a zero overlap, the zero atom moves through a scalar/rank-two root carrier without proliferating.

Therefore a multi-cell defect track carries exactly the data already isolated in the earlier programme:

- one binary resolution sheet;
- a sequence of pivots/root resolutions;
- constant-pivot rank-two runs;
- DDD pivot changes;
- Type-T backtracks;
- a possible closed Petersen pivot skeleton.

This is not a new kind of object. It is the forced DDD/equality backbone expressed in the Ptolemy van Kampen diagram.

---

## 5. Corrected next theorem

The missing bridge is:

### Target 5.1 — Ptolemy-track/backbone identification

Given one closed nonbranching first-failure track in a lifted Ptolemy diagram, construct canonically:

1. its sequence of co-root missing indices and root transport edges;
2. its reduced Petersen pivot skeleton after deleting constant-pivot runs and Type-T backtracks;
3. its resolution holonomy;
4. its ordered cap-route return.

Prove that the track enters one of:

- a pair-changing route/profile escape;
- a small separator/category exit;
- a strict cancellation/shorter target;
- a bounded identity/DDD carrier;
- one simple Petersen cycle already in the established `5/6/8/9` classification.

Then consume the simple-cycle outputs using the existing orientation, annulus, Möbius, identity-hexagon, and DDD-octagon modules.

---

## 6. Correct status of the Ptolemy dossier

`ROOT_FLOW_PTOLEMY_CONTEXTUAL_COHERENCE_V1.md` should now be read as:

- an exact reduction from arbitrary same-order flip relations to local Ptolemy cells;
- an exact catalogue of the contextual behaviour of each individual cell;
- a proposed van Kampen assembly;
- **not yet** a proof that every global defect track is trivial.

Its Sections 1--7 and the external-input boundary remain usable. Sections 8--10 require Target 5.1 before their conclusions become unconditional.

---

## 7. Trust boundary

### Exact here

- identification of the missing logical implication;
- preservation of all local Ptolemy relation theorems;
- distinction between nonbranching and globally contractible defect tracks;
- identification of the multi-cell track with the forced-backbone data type;
- precise corrected next theorem.

### Quarantined

- unconditional no-monodromy theorem for every lifted van Kampen diagram;
- unconditional finite-state termination derived solely from local `C5/C6` circuits;
- unconditional contextual-transfer synthesis in `ROOT_FLOW_PTOLEMY_CONTEXTUAL_COHERENCE_V1.md`.

### Still open

- Ptolemy-track/backbone identification;
- consumption of every global closed track;
- complete contextual-transfer synthesis;
- final proof-DAG audit and global well-founded packaging;
- canonical acceptance, independent audit, Lean verification, manuscript integration, release, publication;
- the global five-support theorem.
