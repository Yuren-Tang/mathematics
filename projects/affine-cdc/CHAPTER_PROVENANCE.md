# AffineCDC chapter provenance

## 1. Recovery authority

Historical five-support packets remain recoverable from

`research/affine-cdc-five-cdc-v1@dad218dd18ed05d1b7cb730c2dc2431b4db5ec9c`.

Proof-development B3–B8 dossiers remain exact at:

- B3 `d806168bb579dbc13f267f44f631e07de909b706`;
- B4 `345074690b7a8658c1208ae84f10d709f8b74bcf`;
- B5 `274970ef9c56cafdbfceeed3c0cc08238d3dfd40`;
- B6 `404f7511f16d1225e066a91842a57e2084943c72`;
- B7 `164f7655f9ec7c0e0a73d49303cf66230fb26487`;
- B8 `989cb002598fd91786029be201c2747c697bb476`.

A source name identifies provenance, not necessarily current controlling theorem status.

## 2. `five-support/surfaces-and-halfcube.md`

### Controlling sources

- cycle-face/full-dual surface packets and B1.4;
- `FIVE_CDC_HALFCUBE_CLIQUE_LINK_CAPACITY_V1.md`;
- `FIVE_CDC_DOMINATING_CLIQUE_EXACT_CAPACITY_V1.md`;
- `FIVE_CDC_HALFCUBE_SUBGRAPH_CLASSIFICATION_V1.md`;
- source-dependent factorable compression packets;
- unused-matching compression and orbit packets;
- factorable bad-core and ideal-pivot packets;
- componentwise scope correction;
- B3.1–B3.3 and the B3 scope map.

### Current roles

- clique links/capacity: valid target-graph theorems;
- eight-vertex criterion: valid old-colour-factorable theorem;
- unused-root/core/pivot: factorable theorem family;
- flower full-dual no-go: theorem conditional on explicit dual certificate;
- numerical neighbourhood/core counts: certificate axis.

### Correction

`FIVE_CDC_UNUSED_MATCHING_ORBITS_V1.md` remains valid except for one displayed representative. The controlling all-parallel representative is `\{01,23,45\}`; orbit sizes `28,168,224` remain unchanged.

## 3. `five-support/gauge-and-reconfiguration.md`

### Controlling sources

- gauge as piecewise root translation;
- gauge/partial-Petrial correspondence;
- support-cycle pivot and flow reconfiguration;
- harmonic quotient surgery;
- admissible switch image;
- internal/external switch dichotomy;
- B4.1–B4.3 and B4 reconfiguration map.

### Current roles

- vertical torsor and partial Petrials: theorem;
- connected-cycle switch decomposition: theorem;
- support pivot and used-root update: theorem;
- new-fibre recomputation: theorem-level scope correction;
- internal/external endpoint formulas: theorem;
- `7737`/`2801`, ranks, surface counts, and neighbour outcomes: certificate axis.

## 4. `five-support/cuts-four-poles-and-routing.md`

### Controlling sources

- three-cut reduction;
- four-edge boundary signatures;
- cap forcing;
- Kempe pairing alignment;
- routing weights and holonomy dichotomy;
- small four-pole census;
- B5.1–B5.3 and B5 map.

### Current roles

- local law, gluing, cap forcing, pairing alignment, routing weights, uniform-routing elimination: theorem;
- four mismatch kernels, policies, Type T/H classification, monodromy, and small census: finite/certificate layer;
- full-cap containment and residual source realization: open.

## 5. `five-support/holonomy-defects-and-atoms.md`

### Controlling sources

- individual affine holonomy and root-admissibility packets;
- genuine rainbow path-family correction;
- Tait-resolution and Type H escape packets;
- DDD atom/triality/route-lock packets;
- B6.1–B6.4 and B6 map;
- B7.1–B7.2 and B7 map.

### Unconditional current roles

- individual-loop norm and cyclic classification;
- root-fibre local system;
- genuine switch-flow and Tait equivalence;
- Type H soluble-branch escape;
- DDD atom triality and unique bad route;
- rank-one/rank-two escape;
- full-rank curvature and flat-potential equivalence.

### Conditional or superseded roles

`FIVE_CDC_BBD_GLOBAL_HOLONOMY_AND_K6_DEFECT_STRIPS_V1.md` and related synthesis packets no longer control an unconditional simultaneous-origin theorem. That chain is conditional on `AC-RL-BBD-GROUPOID-CLOSURE`.

`FIVE_CDC_DEFECT_MINIMAL_FOREST_PETERSEN_TRANSPORT_V1.md` does not control a nontrivial active forest theorem on the stated fixed-terminal variation domain. The forest conclusion is superseded pending `AC-RL-BBD-VARIATION-SLICE`. Local `K_6`/Petersen geometry remains conditional mathematics when a defect strip is independently supplied.

## 6. `five-support/frontier-localisation.md`

Controlling open returns:

- `AC-RL-BBD-GROUPOID-CLOSURE`;
- `AC-RL-BBD-VARIATION-SLICE`;
- `AC-RL-TYPE-T-SERIALISATION`;
- `AC-RL-FLAT-POTENTIAL-INTERFACE`;
- `AC-RL-COMMON-CUT-LOCALISATION`;
- `AC-RL-TYPE-H-COMMON-WITNESS`.

The frontier chapter is controlled by B6/B7 corrections and does not use the former unconditional BBD/forest chain.

## 7. `five-support/finite-laboratories-and-certificates.md`

Controlling source:

- B8 assurance ledger plus exact historical packets and named finite refs.

Current roles are classified as `F-PROVED`, `F-CERT-PUBLIC`, `F-CERT-PRIVATE`, `F-CENSUS`, `CODE-PARTIAL`, or `AFFECTED`.

Correction propagation:

- BBD monodromies do not imply groupoid closure;
- defect/Petersen tables do not repair the variation-domain defect;
- orthogonal finite tables do not support the false `2r` hierarchy;
- `7737` and `2801` are different switch populations;
- the all-parallel matching display is corrected.

## 8. `five-support/equivalent-formulations-and-proof-families.md`

This chapter retains independent roles for singular, quadratic, Schur, cographic, stress/Fourier, surface, interface, holonomy, and projection methods. It does not override the controlling B3–B8 scope and correction layers.

## 9. Historical classification and recovery

Retired source files remain absent from the active tree but recoverable through ordinary Git ancestry. A packet can remain valuable provenance while its theorem status is narrowed, made conditional, or superseded.

For any retired `FILE`:

```text
git show dad218dd18ed05d1b7cb730c2dc2431b4db5ec9c:projects/affine-cdc/research/FILE
```

See `SOURCE_RECOVERY_AUDIT.md`, `RETIRED_SOURCE_CLASSIFICATION.md`, and `SUPERSESSION_MAP.md`.