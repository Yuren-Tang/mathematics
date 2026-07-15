# Working Mathematics

A public, evolving notebook for my mathematical work.

This repository records theorem statements, proof mechanisms, calculations,
formalization links, corrections and connections while they develop. Material
may be incomplete, incorrect, superseded, split, merged or moved. Presence here
is not a claim of peer review or final correctness.

## Current projects

- [AffineCDC](projects/affine-cdc/README.md) — affine incidence geometry for
  cubic binary flows, the rank-three Fano compatibility theorem, its natural
  graph-level even-double-cover output, and the programme toward the full theorem
  that every finite bridgeless multigraph has a cycle double cover. Loops are
  handled by deletion and final singleton-circuit reinsertion. Start with its
  [mathematical architecture](projects/affine-cdc/MATHEMATICAL_ARCHITECTURE.md),
  not the chronological research notes.

## Repository organization

- `projects/` — material that belongs to a coherent mathematical project;
- `unfiled/` — material worth preserving publicly before it has a natural home.

Within an active project, files are organized by mathematical dependency and
status. Git history and snapshots preserve discovery order, so the active
exposition may merge repetitions and replace superseded formulations without
carrying the entire research history into the theorem structure.

## Chronology

Ordinary public chronology is preserved through Git history. Pushes that alter
`projects/` or `unfiled/` automatically create canonical manifests and submit
them to OpenTimestamps. Timestamp proofs are stored on the separate
`attestations` branch and upgraded automatically.

A signed and verified Git commit can additionally receive GitHub's persistent
`verified_at` record. This repository does not require every note to be signed,
tagged, released or assigned a DOI.

## Mature outcomes

When a line of work becomes a stable arXiv paper, formal proof release or
archived artifact, the evolving note may become a short pointer or “tombstone”
to that result. Its previous development remains available in Git history.

No general reuse licence has yet been selected for this repository.
