# CURATION-HANDOFF — AffineCDC Programme B3

**Project:** AffineCDC  
**Prepared by:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Authority basis:** research-workbench issue #37; persistent proof-development policy; AC-PDL charter  
**Live source branch:** `Yuren-Tang/mathematics:proof-development/affine-cdc-rigour-v1`  
**Immutable mathematical checkpoint:** `d806168bb579dbc13f267f44f631e07de909b706`  
**Included packet:** repaired B3.1, repaired B3.2, B3.3 audit, consolidated B3 target/scope map, and DAG at the immutable checkpoint  
**Controlling canonical base:** `main@960c92b7ff231c78b387894149779083060a75eb`  
**Classification:** `PROOF-DEVELOPMENT / PROGRAMME-B3 / READY-FOR-CURATOR / PROVENANCE-REPAIRED`  
**Independent-review state:** not independently audited  
**Live branch continues:** yes; all B4+ commits are excluded unless separately handed off  
**Staging authorized:** dedicated Curator branch only  
**Default-branch movement:** not authorized

## 1. Intake objective

Integrate the exact target hierarchy and scope map while preserving the separation among:

- full dual triangulation $T_g^{(1)}$;
- old-colour quotient $J_g$;
- half-cube target $\mathscr A_5$;
- factorable unused-root/defect-core dynamics;
- full-dual compatible obstruction certificates.

## 2. Accepted theorem package

The packet proves or validates:

1. the general quadratic common-link formula;
2. the exact half-cube link table;
3. exact dominating-clique capacity for ranks two through five;
4. the exact eight-vertex classification by forbidden $K_6$ and $K_8-C_5$;
5. source-dependent factorable compression through $J_g$;
6. unused-matching sufficient compression;
7. the factorable two-apex/pentagon core theorem;
8. the factorable ideal-pivot depth theorem;
9. the full-dual/factorable scope hierarchy;
10. the conditional human obstruction proof for the flower $D_9$ certificate.

## 3. Provenance repair

Early B3.1/B3.2 drafts incorrectly attributed false statements to nonexistent controlling packet names and alleged a positive $K_8-C_5$ certificate. Those drafts were repaired before handoff, and issue #37 comment `5017021539` was corrected in place.

The controlling recovered packets are valid:

- `FIVE_CDC_HALFCUBE_CLIQUE_LINK_CAPACITY_V1.md`;
- `FIVE_CDC_DOMINATING_CLIQUE_EXACT_CAPACITY_V1.md`;
- `FIVE_CDC_HALFCUBE_SUBGRAPH_CLASSIFICATION_V1.md`.

No source packet is superseded on this ground.

## 4. Actual corpus correction

`FIVE_CDC_UNUSED_MATCHING_ORBITS_V1.md` has one erroneous displayed representative. The alleged all-parallel matching

$$
\{05,14,23\}
$$

has directions $5,5,1$. Replace it by, for example,

$$
\boxed{\{01,23,45\}},
$$

with three copies of direction $1$. The theorem of three orbits and sizes $28,168,224$ remains valid.

## 5. Scope normalization

Curator integration must use the following terminology.

- `componentwise same-embedding compressible`: $T_g^{(1)}\to\mathscr A_5$;
- `old-colour-factorably compressible`: $J_g\to\mathscr A_5$;
- `factorably bad core`: unused-root two-apex or pentagon core;
- `ideal target pivot`: abstract target update, not guaranteed source realization.

Failure of the factorable quotient does not imply failure of the full dual.

## 6. Certificate boundary

The flower flow, reduced fibres, explicit duals, face lengths, neighbourhood counts, and large censuses remain exact finite certificate data with their original refs. AC-PDL validated the mathematical implications conditional on those data, not the private computations themselves.

The 88 unmarked two-apex graph types likewise remain computational evidence; the count of 100 marked types is theorem-level.

## 7. Recommended destinations

- `five-support/surfaces-and-halfcube.md`;
- `five-support/equivalent-formulations-and-proof-families.md` where target scope is summarized;
- target/defect portions of `five-support/gauge-and-reconfiguration.md`;
- `THEOREM_DEPENDENCY_MAP.md`;
- `MATHEMATICAL_ARCHITECTURE.md`;
- `CHAPTER_PROVENANCE.md`, `SUPERSESSION_MAP.md`, and certificate ledgers;
- retained proof-development provenance.

## 8. Success test

1. Exact B3 SHA remains fixed.
2. $T_g$ and $J_g$ are never conflated.
3. Valid recovered target packets remain valid.
4. The matching representative is corrected without changing the orbit theorem.
5. Factorable defect-core statements are explicitly scoped.
6. Numerical certificate data remain on the certificate axis.
7. No B4+ material is consumed.
8. No `main`, release, manuscript, DOI, or publication action is implied.

## 9. Stop conditions

Return rather than guess if integration requires promoting a factorable theorem to the full dual, changing a finite certificate without its verifier, or consuming later branch work.

Staging is authorized; canonical movement is not.