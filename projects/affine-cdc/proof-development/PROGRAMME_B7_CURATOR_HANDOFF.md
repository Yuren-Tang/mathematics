# CURATION-HANDOFF — AffineCDC Programme B7

**Project:** AffineCDC  
**Prepared by:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Live source branch:** `Yuren-Tang/mathematics:proof-development/affine-cdc-rigour-v1`  
**Immutable mathematical checkpoint:** `164f7655f9ec7c0e0a73d49303cf66230fb26487`  
**Included packet:** B7.1, B7.2, consolidated B7 map, and DAG at the immutable checkpoint  
**Controlling canonical base:** `main@960c92b7ff231c78b387894149779083060a75eb`  
**Classification:** `PROOF-DEVELOPMENT / PROGRAMME-B7 / READY-FOR-CURATOR / AC-RL-GAPS-EXPLICIT / GLOBAL-COMPOSITION-OPEN`  
**Independent-review state:** not independently audited  
**Live branch continues:** yes; B8+ commits are excluded unless separately handed off  
**Staging authorized:** dedicated Curator branch only  
**Default-branch movement:** not authorized

## 1. Accepted theorem layer

The packet proves:

1. rank one is impossible in the universally route-locked quotient;
2. rank two is a Tait colouring;
3. every rank-two plane through the terminal colour has a root-triangle section;
4. the resulting root lift has boundary state `A` and escapes Type H;
5. full rank has an exact flat/nonflat curvature dichotomy;
6. flatness is equivalent to an eight-state affine potential with the exact edge law;
7. nonflatness is equivalent to one common `g`-edge set that is a cut in all four scalar sheets;
8. its terminal cut word has odd parity and represents the nonzero class in `F₂⁴/E₄`.

## 2. Localisation boundary

The packet does not prove that:

- the common scalar-sheet cut is a graph cut in the underlying four-pole;
- it has bounded or connected support;
- it gives a composition-safe DDD/Whitney/transition-matroid factor;
- the odd terminal bit is the physical `D₈` cohomology class;
- the flat potential fibres have bounded transfer semantics;
- Type T routing yields serial decomposition.

## 3. Exact AC-RL returns

Recorded in issue #8 comment `5019455976`:

- `AC-RL-TYPE-T-SERIALISATION`;
- `AC-RL-FLAT-POTENTIAL-INTERFACE`;
- `AC-RL-COMMON-CUT-LOCALISATION`;
- `AC-RL-TYPE-H-COMMON-WITNESS`.

Earlier BBD returns remain separately active.

## 4. Required corpus treatment

1. Promote the rank-two escape and full-rank primal/dual curvature theorems.
2. Preserve the graph-localisation statements as open.
3. Do not identify scalar-sheet cuts with source graph cuts without a comparison theorem.
4. Do not treat finite potential range as a bounded-interface theorem.
5. Link the exact AC-RL gaps rather than replacing them with broad frontier prose.
6. Exclude B8+ commits.

## 5. Success test

The exact B7 checkpoint remains fixed; positive rank/curvature theorems are integrated; all four localisation gaps remain explicit; no global five-support theorem, formalization, release, publication, or `main` movement is implied.

Staging is authorized; canonical movement is not.