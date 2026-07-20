# AC-UNIFIED-01 final curation audit

## 1. Exact controls

- controlling packet: `Yuren-Tang/research-workbench#24`, comment `5024901875`;
- fixed base: `curation/affine-cdc-programme-b3-b8-v1@0100895d57aab7d21153c580fa9bdc45fafc832e`;
- immutable Programme A source: `proof-development/affine-cdc-rigour-v1@8bee16780b549f51e1f29343671a059961ec4172`;
- Independent Audit A: `audit/affine-cdc-complete-cdc-spine-v1@2fac31f4e76c819dd42a179a2772501c50ee93ad`;
- immutable Programme A repair source: `proof-development/affine-cdc-rigour-v1@06bce656dcf5bfd6491ec08f51a702ea56d2470d`;
- unified branch: `curation/affine-cdc-programme-a-b1-b8-unified-v1`;
- exact repair splice: `a35da6ba6e4908c70f970f3cadf5fcf4b582dae4`.

The exact final candidate SHA is recorded in the authoritative issue #24 return.

## 2. Splice and ancestry audit

The repair splice has two parents, in order:

1. accepted B1–B8 base `0100895d57aab7d21153c580fa9bdc45fafc832e`;
2. repair checkpoint `06bce656dcf5bfd6491ec08f51a702ea56d2470d`.

Its tree adds exactly one source path:

`projects/affine-cdc/proof-development/AC_PD_A_AUDIT_A_EXPLICITNESS_REPAIRS.md`.

The candidate is a normal fast-forward descendant of the splice. No rebase, squash, force update, or history rewrite occurred.

## 3. Source-blob audit

The retained repair dossier has blob

`15ab169648b678e3ce0d1288aa41c6b982af0eae`,

identical to the immutable repair checkpoint.

Relative to the splice, the Curator alignment modifies only Programme A/unified entrypoint, provenance, dependency, assurance, and status paths. It modifies no file under `proof-development/`, no `five-support/` chapter, and no B3–B8 dossier or certificate ledger.

## 4. Candidate-delta audit

Before this final audit file:

- fixed base to candidate: `7` commits ahead, `0` behind;
- changed paths: `17`;
- exact source paths: `1`;
- Curator alignment paths: `16`.

Splice to candidate:

- `1` Curator commit ahead;
- `0` behind;
- exactly `16` Programme A/unified paths;
- no proof-development or five-support substantive path.

This final audit adds one control path only.

## 5. Repair 1 — Seymour convention

The active repair chapter now states without convention gap:

- finite connected loopless multigraph;
- parallel edge objects permitted;
- no isthmus / 2-edge-connected source convention;
- componentwise application to all edge-bearing components;
- isolated vertices and the empty graph inert;
- loops already removed by A1.

There is no hidden simple-graph or connectedness assumption.

Seymour’s nowhere-zero six-flow theorem remains the sole non-elementary external logical input. Integral eight-flow inclusion, modular reduction, and equal-order transport to `F_2^3` remain internal Programme A results.

## 6. Repair 2 — A4 reverse reconstruction

The active repair chapter contains a complete proof that every even local triple of affine lines of directions

$$
h_1+h_2+h_3=0
$$

has unique pairwise intersection points and a unique deleted point

$$
m=x_{12}+h_3
$$

such that

$$
\begin{aligned}
L_1&=\{m+h_2,m+h_3\},\\
L_2&=\{m+h_1,m+h_3\},\\
L_3&=\{m+h_1,m+h_2\}.
\end{aligned}
$$

Thus every even family is uniquely `Phi_v(m)`. The proof is not replaced by an eight-row enumeration and works over every finite-dimensional ambient `F_2`-space used by A4.

## 7. Repair 3 — historical Tutte route

The active corpus contains a prominent notice that §§4.1–4.2 of `reduction/outer-shell-and-binary-flow.md` are historical provenance only.

The controlling route is A3:

$$
\text{Seymour six-flow}
\to
\text{integral eight-flow}
\to
\mathbf Z/8\mathbf Z\text{-flow}
\to
\mathbf F_2^3\text{-flow},
$$

with internal equal-order transport. No active Programme A theorem depends on the older Tutte route.

## 8. Audit A status audit

The original Programme A theorem spine retains the Independent Audit A result:

`VERIFIED SUBJECT TO NAMED EXTERNAL THEOREMS / NON-BLOCKING EXPLICITNESS REPAIRS`.

The three returned items are now:

`CLOSED / EXPOSITORY-REPAIR / NO-THEOREM-CHANGE / NO-NEW-MATHEMATICS`.

The repairs change no theorem statement, hypothesis, conclusion, or dependency. Their Curator integration does not itself constitute a second independent re-audit of the repaired prose.

## 9. B1–B8 preservation audit

No substantive `five-support/` path changed relative to the fixed base.

The candidate therefore preserves:

- B1 object and quantifier boundaries;
- B2 witness hierarchy and orthogonal correction;
- B3 full-dual/factorable distinction and target results;
- B4 vertical/horizontal and connected/composite distinctions;
- B5 interface theorems and finite-certificate boundary;
- B6 groupoid/variation corrections;
- B7 rank/curvature theorems and global-composition boundary;
- B8 assurance classes and correction propagation.

The global five-support theorem remains open.

## 10. Six exact frontier obligations

Unchanged:

- `AC-RL-BBD-GROUPOID-CLOSURE`;
- `AC-RL-BBD-VARIATION-SLICE`;
- `AC-RL-TYPE-T-SERIALISATION`;
- `AC-RL-FLAT-POTENTIAL-INTERFACE`;
- `AC-RL-COMMON-CUT-LOCALISATION`;
- `AC-RL-TYPE-H-COMMON-WITNESS`.

No obligation is silently closed, renamed, broadened, or replaced.

## 11. B9 and later-work exclusion

The live PDL branch is two commits beyond the fixed repair checkpoint. Its later delta contains only:

- a later `OBLIGATION_DAG.md` registration;
- `PROGRAMME_A_AUDIT_A_REPAIR_CURATOR_HANDOFF.md`.

Neither path is imported. The candidate also excludes:

- `AC_PD_B9_CORRECTED_GLOBAL_FRONTIER_ASSEMBLY.md` and all B9 handoffs;
- AC-RL working-ahead commits and hyperbolic/rank-three frontier material;
- any later moving-branch source state.

## 12. Repository isolation

Verified unchanged:

- `main@960c92b7ff231c78b387894149779083060a75eb`;
- Programme A branch `68715fb29bb4b6555e2bc3e089603c5390d01566`;
- Programme B1 branch `4d7b9c74ea4377a58e219a7c6c3cb569a8229276`;
- Programme B2 branch `08b662ecc31848456b9904f4d5b85c3801d090a1`;
- accepted B1–B8 branch `0100895d57aab7d21153c580fa9bdc45fafc832e`;
- Audit A branch `2fac31f4e76c819dd42a179a2772501c50ee93ad`;
- AC-RL branch `936eb8c4a445a0eacaa882d5fa81e355fab99260`.

The PDL branch was not written by Curator. No branch was deleted or renamed. No force-push, rebase, squash, public-history rewrite, Lean/manuscript mutation, release, publication, arXiv, DOI, or tag action occurred.

## 13. Stop-condition audit

No stop condition was triggered.

- the three repair items are exact and mutually consistent;
- no theorem-strength change is required;
- no B claim or frontier obligation must be altered;
- no later B9/RL mathematics is needed;
- no hidden external premise is introduced;
- the source and fixed base remain recoverable;
- all assurance axes can be represented without ambiguity.

## 14. Unified assurance classification

The candidate is:

`CURATOR-INTEGRATED / PROGRAMME A INDEPENDENTLY AUDITED WITH CLOSED NON-BLOCKING REPAIRS / B1–B8 CORRECTION-AWARE / FIVE-SUPPORT GLOBAL THEOREM OPEN`.

More precisely:

- Programme A original theorem spine: independently audited;
- Programme A repaired prose: closed and integrated, not separately re-audited;
- B1–B8: accepted authorial/correction/assurance surface, pending Audit B;
- Lean: partial anchor only, no end-to-end upgrade;
- manuscript/publication/release/arXiv/DOI: unchanged;
- canonical `main`: unchanged.

## 15. AC-DIR disposition questions

1. accept or revise this exact unified candidate as the fixed Programme A + B1–B8 rolling corpus;
2. decide whether a separate owner control point should authorize ancestry-preserving `main` movement;
3. retarget Audit B to the fixed unified candidate without reopening Programme A theorem truth;
4. fix the exact repaired Programme A projection input for Lean and Paper A;
5. retain B9 and AC-RL working-ahead material outside the candidate until a later coherent intake.

No mathematical ambiguity requires pre-disposition escalation.