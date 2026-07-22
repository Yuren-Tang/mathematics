# AC-PD-B2.3 — source-fidelity repair and propagation ledger

**State:** `COMPLETE-DRAFT / SOURCE-FIDELITY-REPAIR / READY-FOR-CURATOR`  
**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Controlling intake:** `Yuren-Tang/research-workbench#37`, comment `5028845743`  
**Audit trigger:** `Yuren-Tang/mathematics:audit/affine-cdc-five-support-corpus-v1@110f014c551d4ce0f109ca5559d234ddb124d8f1`  
**Persistent branch:** `proof-development/affine-cdc-rigour-v1`  
**Fixed candidate:** `curation/affine-cdc-programme-a-b1-b8-unified-v1@ec765cd03271abd3588ec36faec3d53d0f8aa03b` — read-only and unchanged  
**Classification:** `SOURCE-RECONSTRUCTION COMPLETE / ATTRIBUTION RETRACTED / EXTRAPOLATION CLASSIFIED / MATHEMATICS PRESERVED`

## 1. Exact source question

The disputed proposition is the alleged arbitrary-rank theorem asserting a canonical additive anisotropic-root representation for all unordered pairs of the `2^r` points of `Γ=F_2^r` in a quadratic space of dimension `2r`, described by:

\[
V=\Gamma\oplus\Gamma^*,
\qquad
d_h(a)=([a],\operatorname{ev}_a),
\]

and presented as a universal `O^+(2r,2)` tower extending the rank-three eight-support model.

The repair question was whether an exact committed source of this proposition exists. If not, the proposition had to be classified as an extrapolation, inferred hierarchy, or uncommitted draft rather than attributed to `FIVE_CDC_UNIVERSAL_ORTHOGONAL_ROOT_LIFT_V1.md`.

## 2. Final source classification

No exact committed source of the disputed proposition was recovered within the bounded search described in §3.

The exact classification is:

\[
\boxed{
\texttt{SOURCE-UNRECONSTRUCTED / INFERRED-EXTRAPOLATION OR UNCOMMITTED DRAFT}.}
\]

The most plausible reconstruction of the error is a conflation of two genuine but distinct source lines:

1. the **all-rank transgression/residue hierarchy**, which works over `F_2^r` but explicitly identifies rank three as the unique balanced quadratic-Lagrangian case; and
2. the **rank-three universal eight-index orthogonal packet**, which realizes the twenty-eight roots of `K_8` in `O^+(6,2)` and includes five-coordinate `O^-(4,2)` slices.

The accidental numerical equality

\[
2^3-2=6=2\cdot3
\]

makes the rank-three model look like a `2r` pattern. It does not supply a theorem in arbitrary rank.

The first recoverable committed text located that explicitly displays the disputed formula while describing it as an earlier theorem is the original AC-PDL B2.3 correction layer included in checkpoint `d62974704d6dac77aaa00275a595fedf7f70cfd2`. No earlier theorem-bearing commit, path, or blob was found.

## 3. Complete bounded search boundary

### 3.1 Historical canonical and rank-hierarchy line

Inspected:

- `main@960c92b7ff231c78b387894149779083060a75eb`;
- `projects/affine-cdc/rank-hierarchy/transgression-and-dual-fano-residue.md`;
- its introducing/integration commit `79e6a7ae12293c06f853e1b4f0291ea88d99a88e`;
- associated rank-three, rank-four, residue, tensor, and dual-Fano history identified by commit-message and path searches.

Finding: the all-rank line proves support-polynomial and transgression/residue identities. It explicitly says rank three is the unique balanced quadratic member. It contains no complete-root `2r` tower and no disputed formula.

### 3.2 Complete five-support source population

The source interval was fixed as:

- starting canonical ancestor: `main@749e0579581fcc838685138b3582f4de306b8e72`;
- public five-support checkpoint: `research/affine-cdc-five-cdc-v1@dad218dd18ed05d1b7cb730c2dc2431b4db5ec9c`;
- source population: eighty-two commits and seventy-eight packet files under `projects/affine-cdc/research/`.

The exact source inventory, recovery audit, Audit B claim/source matrix, and all plausible orthogonal/root/rank packets were checked. The principal inspected packets were:

- `FIVE_CDC_UNIVERSAL_ORTHOGONAL_ROOT_LIFT_V1.md`;
- `FIVE_CDC_ANISOTROPIC_RANK_FOUR_FLOW_V1.md`;
- `FIVE_CDC_SINGULAR_QUOTIENT_LIFT_V1.md`;
- `FIVE_CDC_AFFINE_PLANE_K4_RESIDUE_V1.md`;
- `FIVE_CDC_ROOT_FLOW_TRIANGLE_COMPLEX_V1.md`;
- `FIVE_CDC_ROOT_LIFT_FOURIER_STRESS_DUALITY_V1.md`;
- `FIVE_CDC_QUADRATIC_CYCLE_EQUATION_V1.md`;
- `FIVE_CDC_SCHUR_QUOTIENT_CRITERION_V1.md`;
- `FIVE_CDC_UNIVERSAL_SIX_CUBE_MODULE_V1.md`;
- `FIVE_CDC_UNIVERSAL_RENEWAL_CUBE_TEMPLATE_V1.md`;
- the source-dependent half-cube and fixed-flow/root-lift packets that consume the rank-three root module.

Finding: none contains `Γ⊕Γ*`, `d_h(a)=([a],ev_a)`, or a universal `O^+(2r,2)` complete-root theorem.

### 3.3 Exact named packet

Exact source:

- path: `projects/affine-cdc/research/FIVE_CDC_UNIVERSAL_ORTHOGONAL_ROOT_LIFT_V1.md`;
- checkpoint: `dad218dd18ed05d1b7cb730c2dc2431b4db5ec9c`;
- blob: `2043ada9d28789ecc5f4f0028e62133f37835bc1`;
- introducing commit: `a172b2acb13fc0b042ecb099a08b9631ab1db59a`.

Its stated scope is the universal **eight-index** cover module, Hamming Lagrangian quotient, and five-coordinate minus-type slices. It fixes `Γ=F_2^3` throughout the eight-support construction.

### 3.4 Later authorial, Curator, and audit layers

Inspected:

- PDL B2.3, B2 formulation map, B2 handoff, B8 assurance ledger, and DAG;
- accepted B2 Curator checkpoint `08b662ecc31848456b9904f4d5b85c3801d090a1`;
- fixed unified candidate `ec765cd03271abd3588ec36faec3d53d0f8aa03b`;
- Audit B branch `110f014c551d4ce0f109ca5559d234ddb124d8f1` and all three audit deliverables;
- current project Director state and status records.

Finding: the false attribution propagates from the PDL correction/handoff into the Curator migration and assurance layers. Audit B correctly detects that propagation but does not identify an earlier theorem source.

### 3.5 Search signatures

Repository path, source inventory, commit-message, and exact-text searches used the distinctive signatures:

- `Gamma direct dual`, `Γ⊕Γ*`, `Gamma^*`;
- `d_h(a)`;
- `ev_a`, `evaluation`;
- `2r`, `2r-dimensional`;
- `O^+(2r,2)`;
- `universal orthogonal`, `orthogonal root lift`;
- `root module`, `complete graph roots`, `triangle addition`;
- `rank-free`, `all-rank`, `rank hierarchy`, `higher-rank`.

The only exact orthogonal-root source found is the rank-three/eight-index packet above. The all-rank commits concern transgression/residue rather than a complete-root tower.

## 4. Restored exact provenance

### 4.1 Valid rank-three/eight-support source role

The named packet is a valid theorem-level historical source for:

- the even-weight module `H_8` on the eight points of `F_2^3`;
- the Hamming kernel and rank-three moment map;
- the six-dimensional quotient `V_8=H_8/⟨1⟩`;
- the plus-type quadratic structure `O^+(6,2)`;
- the twenty-eight anisotropic roots corresponding to the edges of `K_8`;
- the root-flow/eight-index even-double-cover equivalence;
- the rank-three AffineCDC compatible-family/root-lift equivalence;
- the five-coordinate `O^-(4,2)` slices;
- the omitted-triple anisotropic-plane orthogonality and eight-to-five compression formulation.

### 4.2 Valid all-rank source role

The historical rank hierarchy remains valid for:

- support-polynomial degree `r-1`;
- degree-lowering Fano transgression;
- affine level-set identities;
- global outside-plane parity;
- legal dual configurations and the cross-bit;
- dual-Fano residue identities and their exact rank dependence.

It does not imply a `2r` complete-root representation.

### 4.3 Valid B2.3 correction role

B2.3 remains the authorial source for:

- the point-potential reduction `r_{ab}=p_a+p_b`;
- the Gram matrix `J+I`;
- the sharp lower bound `dim V≥q-2`;
- impossibility of dimension `2r` for `q=2^r`, `r≥4`;
- the deleted permutation module `E_I/⟨1_I⟩`;
- rank-three exceptionality.

These results are self-contained and do not depend on locating the original extrapolation.

## 5. Authorial propagation surfaces repaired in this epoch

The following PDL-owned surfaces must carry the corrected classification and are repaired as part of the final checkpoint:

1. `AC_PD_B2_3_ORTHOGONAL_ROOT_MODULE_CORRECTION.md`;
2. `AC_PD_B2_FORMULATION_AND_WITNESS_MAP.md`;
3. `PROGRAMME_B2_CURATOR_HANDOFF.md`;
4. `AC_PD_B8_CERTIFICATE_ASSURANCE_LEDGER.md`;
5. `OBLIGATION_DAG.md`;
6. this source-fidelity dossier;
7. the dedicated B2/B8 source-fidelity Curator handoff.

No B1, B3–B7, B9, Programme A, or AC-RL theorem surface changes.

## 6. Downstream propagation surfaces for Curator replacement

The following read-only candidate/Curator surfaces are affected and must be repaired in a later authorized replacement candidate. They are **not** modified by AC-PDL in this epoch.

### 6.1 Substantive five-support chapters

- `projects/affine-cdc/five-support/b2-formulation-and-witness-hierarchy.md`;
- `projects/affine-cdc/five-support/root-flow-lifting.md`;
- `projects/affine-cdc/five-support/equivalent-formulations-and-proof-families.md`;
- any B8 finite-assurance passage that repeats the packet-wide false classification.

Required action: retain the mathematical refutation of the extrapolated tower, restore the packet's exact valid theorems, and separate the two provenance records.

### 6.2 Provenance, migration, and supersession

- `CHAPTER_PROVENANCE.md`;
- `MIGRATION_LEDGER.md`;
- `RETIRED_SOURCE_CLASSIFICATION.md`;
- `SUPERSESSION_MAP.md`;
- `SOURCE_RECOVERY_AUDIT.md`;
- `RECONSTRUCTION_MANIFEST.md`, if it repeats exhaustive source-fidelity acceptance;
- any Programme B2 integration map or final audit that names the packet as the false theorem source.

Required action: remove the packet-wide `FALSE THEOREM / HISTORICAL ONLY` class; add a separate non-packet item for the source-unreconstructed extrapolation; recompute the seventy-eight-packet class partition; repair the stale `39+10+18+10+1=78` equation after the classification is fixed.

### 6.3 Dependency, assurance, and status

- `THEOREM_DEPENDENCY_MAP.md`;
- `MATHEMATICAL_ARCHITECTURE.md`;
- `ACTIVE_MATHEMATICAL_SURFACE.md`;
- `CURRENT_BEST.md`;
- `FORMAL_STATUS.md`;
- unified Programme A+B1–B8 entrypoint/status maps;
- B8 certificate/source-assurance ledgers.

Required action: preserve the `q-2` theorem and deleted permutation module while replacing the false source attribution with `SOURCE-UNRECONSTRUCTED / INFERRED-EXTRAPOLATION` and restoring exact packet provenance.

### 6.4 Public warning

`Yuren-Tang/mathematics` public issue #2 is outside the PDL write boundary and is not modified. The Director's append-only supersession comment already states the correct interim public rule. A later public change, if any, remains Director/owner-controlled.

## 7. Corrected source-class accounting rule

The packet population remains exactly seventy-eight. The named packet remains one of those seventy-eight packets and must be classified by its actual valid contents, not as an extra false-theorem class.

The source-unreconstructed extrapolation is **not** a recovered packet and therefore must not be counted as one of the seventy-eight. It belongs in a separate authorial correction/provenance ledger outside the packet partition.

Consequently neither of the currently propagated partitions

\[
39+10+18+10+1=78
\]

or

\[
38+10+18+10+1+1=78
\]

may be retained merely by relabelling the named packet. Curator must recompute the exact packet classes from the corrected classification table. AC-PDL does not guess the final counts because concrete category placement belongs to the replacement-candidate migration architecture.

## 8. Stop-condition assessment

No stop condition is triggered.

- The mathematical correction is proved internally.
- The exact historical packet is recoverable and its valid role is known.
- The absence of an earlier committed source can be honestly classified under the controlling intake.
- No new frontier mathematics is required.
- No prohibited surface must be mutated to produce an authorial repair checkpoint.

Therefore the proper return is `READY-FOR-CURATOR`, not `BLOCKED-SOURCE`.

## 9. Acceptance test

The repair is complete exactly when:

1. the PDL branch no longer attributes the false tower to the named packet;
2. the `q-2` theorem and deleted permutation module remain unchanged;
3. the packet's exact rank-three/eight-support and five-slice roles are restored;
4. the genuine all-rank transgression hierarchy remains distinct;
5. all authorial propagation surfaces are corrected;
6. all downstream Curator surfaces are enumerated without being modified;
7. the source-unreconstructed extrapolation is not counted as one of the seventy-eight packets;
8. the global five-support theorem and six B9 frontier obligations remain unchanged;
9. no fixed candidate, audit, Curator, `main`, public issue #2, Lean, manuscript, release, publication, arXiv, DOI, tag, or Research Lead surface is modified.