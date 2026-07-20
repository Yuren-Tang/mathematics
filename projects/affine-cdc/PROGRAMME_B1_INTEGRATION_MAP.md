# Programme B1 integration and provenance map

## 1. Exact refs

- integration base: `curation/affine-cdc-programme-a-v1@68715fb29bb4b6555e2bc3e089603c5390d01566`;
- immutable B1 source: `proof-development/affine-cdc-rigour-v1@778b09ac8260192e022f512f24cdef1d04871f37`;
- writable candidate: `curation/affine-cdc-programme-b1-v1`;
- exact splice commit: `35c7a2851f070061175194eef10568c0a456cf8e`;
- splice parents:
  - first parent: `68715fb29bb4b6555e2bc3e089603c5390d01566`;
  - second parent: `778b09ac8260192e022f512f24cdef1d04871f37`.

The splice tree contains exactly the five B1 dossiers and the immutable checkpoint `OBLIGATION_DAG.md`. It does not copy the Programme A handoff or any B2/B3 file.

## 2. Exact B1 units

| Unit | Authorial state | Exact unit checkpoint | Source dossier | Active destination |
|---|---|---|---|---|
| `B1.1` | `COMPLETE-DRAFT` | `ed0288c2485d4eb826b49b8289a0025e1b2c0d64` | `proof-development/AC_PD_B1_1_ROOT_FLOW_TRIANGLE_EQUIVALENCE.md` | `five-support/b1-object-quantifier-and-scope.md`, §§2, 5 |
| `B1.2` | `COMPLETE-DRAFT / CORPUS-CORRECTION` | `24e923bcfcfc3aa2765c3269018c977bd1351403` | `proof-development/AC_PD_B1_2_MATCHING_FOUR_FLOW_EQUIVALENCE.md` | same, §3; `five-support/root-flow-lifting.md` |
| `B1.3` | `COMPLETE-DRAFT` | `dbd01c86059368619a51f9b5252dfec0a2cf7778` | `proof-development/AC_PD_B1_3_FIXED_FLOW_PLANE_CRITERION.md` | same, §4; `five-support/root-flow-lifting.md` |
| `B1.4` | `COMPLETE-DRAFT / SCOPE-CORRECTION` | `a9695a1045bdb157b8d0d8aa1e318302c28e785d` | `proof-development/AC_PD_B1_4_SURFACE_HALFCUBE_SCOPE.md` | same, §§5–10; `five-support/surfaces-and-halfcube.md` |
| B1 aggregate | `READY-FOR-CURATOR` | `73be22f42298470bd9ebaeb519de7ed686c27e41` | `proof-development/AC_PD_B1_EQUIVALENCE_AND_SCOPE_MAP.md` | same, §§10–13; `THEOREM_DEPENDENCY_MAP.md`; `MATHEMATICAL_ARCHITECTURE.md` |

The source dossiers and checkpoint DAG retain exact blob identity after the splice.

## 3. Six controlling corrections

| Correction | Previous unsafe compression | Controlling B1 boundary | Active locations |
|---|---|---|---|
| Support-coordinate versus root-label | a fixed support coordinate was called a matching | support-coordinate inverse image is even; root-label inverse image is a matching | canonical B1 §3; `root-flow-lifting.md` |
| Four-flow converse | bare matching plus four-flow was presented as sufficient | require $(B,D,M)$ or the explicit component endpoint-parity/$T$-join datum | canonical B1 §3; `root-flow-lifting.md`; equivalence chapter |
| Fixed-lift biconditional | fixed $g$ was conflated with arbitrary cover existence on $G$ | $T_g^{(1)}\to\mathscr A_5$ classifies componentwise compression of the same embedding | canonical B1 §6; `surfaces-and-halfcube.md` |
| Dual holonomy | local triangular conservation was treated as global integration | an external root flow integrates on prescribed $T_g$ iff every dual cycle sum vanishes | canonical B1 §7; `surfaces-and-halfcube.md` |
| Full dual versus quotient | $J_g$ was treated as the complete fixed-lift object | $J_g$ classifies only maps constant on old-colour fibres | canonical B1 §8; `surfaces-and-halfcube.md` |
| Half-cube parity | singleton words were used as vertices of the even component | use an odd translate $t+\varepsilon_i$, or explicitly use the odd component | canonical B1 §9; `surfaces-and-halfcube.md` |

## 4. Quantifier map

| Level | Fixed data | Exact theorem | What does not follow |
|---|---|---|---|
| Graph | only $G$ | five supports $\Leftrightarrow$ root flow $\Leftrightarrow$ $K_5$ triangles $\Leftrightarrow$ exact matching/four-flow data $\Leftrightarrow \exists(f,W)$ empty profile $\Leftrightarrow \exists S$ with $T_S^{(1)}\to\mathscr A_5$ | no prescribed flow, lift, or surface is forced |
| Fixed pair | $(f,W)$ | seven equivalent component-obstruction forms | does not imply every $W$ or every $f$ succeeds |
| Fixed flow | $f$, variable $W$ and compatible point-index lift | factorable five-coordinate lift iff some plane profile is empty | failure is not a graph counterexample |
| Fixed lift | $g$ and its surface | same-embedding componentwise compression iff $T_g^{(1)}\to\mathscr A_5$ | not every external cover integrates on this surface |
| Prescribed dual plus external root flow | $T_g$ and $\lambda$ | integration iff all dual cycle holonomies vanish | triangular-face conservation alone is insufficient |
| Old-colour quotient | $J_g$ | factorable maps constant on old-colour fibres | does not classify all maps from the full dual |

## 5. Recovered research provenance

The B1 dossiers retain provenance to the exact public five-CDC checkpoint

`research/affine-cdc-five-cdc-v1@dad218dd18ed05d1b7cb730c2dc2431b4db5ec9c`,

especially:

- `FIVE_CDC_MATCHING_FOUR_FLOW_BRIDGE_V1.md`;
- `FIVE_CDC_FIXED_FLOW_REDUCTION_V1.md`;
- `FIVE_CDC_COLOUR_CUT_REFINEMENT_V1.md`;
- `FIVE_CDC_COLORED_SURFACE_DUAL_HALFCUBE_V1.md`;
- `FIVE_CDC_HALFCUBE_SCOPE_CORRECTION_V1.md` and its displayed-table erratum.

The synthesis errors corrected here arose in compression into the active corpus, not in the controlling stronger source statements.

## 6. Assurance and exclusions

B1 is integrated as complete authorial proof-development mathematics. It is not independently audited and not end-to-end Lean verified.

Excluded:

- every `AC_PD_B2_*` file;
- every `AC_PD_B3_*` file;
- later `OBLIGATION_DAG.md` changes;
- Programme B2/B3 handoffs;
- moving-tip finite-certificate corrections;
- any change to Programme A candidate, `main`, Lean, manuscript, publication, release, arXiv, DOI, or timestamp status.
