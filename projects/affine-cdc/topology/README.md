# Archived embedding and surface programme

This directory records the boundary of the active mathematical corpus. The
2026-07-14 snapshot in
[`../snapshots/2026-07-14/`](../snapshots/2026-07-14/) preserves filenames,
sizes, and cryptographic hashes for an older embedding, Petrial, transition,
and surface programme. The corresponding manuscript bodies are not present in
the current repository tree.

Consequently, this directory is an inventory and restoration protocol, not a
reconstruction of missing theorems.

## 1. Mathematical themes named by the snapshot

The manifest names source documents concerning:

- gauge choices and compatible embeddings or rotation systems;
- code-filtered partial Petrials and surface state sums;
- finite orientability and genus censuses;
- syndrome and transition invariants;
- transition-matroid or delta-matroid slices;
- two-edge and three-edge factorization;
- earlier quotient-sheaf, tensor-complex, determinant, higher-rank, and
  $K_{3,3}$ formulations.

It also names computational scripts, CSV or JSON outputs, navigation files,
research logs, handoffs, architecture freezes, and archive indices.

## 2. Material already absorbed into the active corpus

The following mathematical content has a complete active replacement:

| Snapshot theme | Canonical active location |
|---|---|
| quotient sheaf and index duality | [`../core/affine-incidence-and-obstruction.md`](../core/affine-incidence-and-obstruction.md) and [`../reduction/incidence-to-tensor-complex.md`](../reduction/incidence-to-tensor-complex.md) |
| flow tensor complex | [`../reduction/incidence-to-tensor-complex.md`](../reduction/incidence-to-tensor-complex.md) and [`../tensor/code-flag-complex.md`](../tensor/code-flag-complex.md) |
| Fano basis-packing determinant | [`../tensor/exact-sequences-and-functoriality.md`](../tensor/exact-sequences-and-functoriality.md) and [`../tensor/torsion-and-rigidity.md`](../tensor/torsion-and-rigidity.md) |
| higher-rank obstruction | [`../rank-hierarchy/transgression-and-dual-fano-residue.md`](../rank-hierarchy/transgression-and-dual-fano-residue.md) |
| rank-four $K_{3,3}$ counterexample | [`../rank-hierarchy/rank-four-first-obstruction.md`](../rank-hierarchy/rank-four-first-obstruction.md) |
| two-edge and three-edge algebraic sewing laws | [`../gauge/interface-gluing.md`](../gauge/interface-gluing.md) |

This absorption concerns the active theorem content actually available in the
repository. It does not prove that every lemma or computation in the absent
source bodies has been recovered.

## 3. Material not reconstructed

The following themes remain outside the audited active corpus because their
source bodies are absent:

- the exact gauge–embedding correspondence;
- definitions and coefficients of the code-filtered Petrial polynomial;
- detailed surface-census tables and their verification scripts;
- the exact syndrome-transition universal invariant;
- the precise transition-matroid or delta-matroid comparison;
- any topological lemma not already restated in an active theorem document.

The conditional polynomial notation in
[`../gauge/interface-gluing.md`](../gauge/interface-gluing.md) preserves only the
algebraic sewing multiplicity. It does not claim to reconstruct the missing
state-space definition.

## 4. Restoration protocol

If the source bodies are restored, each file must be read and classified as one
of:

1. **fully absorbed** — all mathematical content is already present in a
   canonical active chapter;
2. **additional theorem or example** — extract it into the appropriate active
   chapter with proof and hypotheses;
3. **computational evidence** — preserve it as data or verification, not as a
   theorem;
4. **research programme** — retain it here with explicit conjectural status;
5. **obsolete or false** — leave it only in Git history and the cryptographic
   snapshot.

No restored file should return automatically to the active exposition merely
because it existed historically.

## 5. Historical preservation

Git commits, the dated snapshot, and the manifest preserve discovery history and
priority evidence. The active tree is free to use the current mathematical
structure. This separation allows historical evidence to survive without
forcing obsolete ontology into the present theorem corpus.