# CURATION-HANDOFF — AffineCDC Programme B4

**Project:** AffineCDC  
**Prepared by:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Live source branch:** `Yuren-Tang/mathematics:proof-development/affine-cdc-rigour-v1`  
**Immutable mathematical checkpoint:** `345074690b7a8658c1208ae84f10d709f8b74bcf`  
**Included packet:** B4.1–B4.3, consolidated B4 map, and DAG at the immutable checkpoint  
**Controlling canonical base:** `main@960c92b7ff231c78b387894149779083060a75eb`  
**Classification:** `PROOF-DEVELOPMENT / PROGRAMME-B4 / READY-FOR-CURATOR / FRONTIER-EXPLICIT`  
**Independent-review state:** not independently audited  
**Live branch continues:** yes; B5+ commits are excluded unless separately handed off  
**Staging authorized:** dedicated Curator branch only  
**Default-branch movement:** not authorized

## 1. Intake objective

Integrate the exact two-level motion laws while separating:

- vertical gauge translation and partial Petrials;
- support-cycle pivots;
- general connected-cycle flow switches;
- disconnected composite switch paths;
- internal fixed-plane correction and external quotient reslicing;
- theorem-level transport formulas from finite census data.

## 2. Accepted theorem package

The packet proves:

1. the labelled root-lift fibre is a torsor under $H_f^0$;
2. on disconnected graphs the reduced kernel is componentwise, giving $H_f^0/\Gamma^{\pi_0(G)}$;
3. gauge bits are exactly face-side swaps and accessible partial Petrials;
4. every exponent-two reconfiguration edge is a constant switch on one connected source cycle;
5. a disconnected binary-cycle switch is a commuting sequence of connected moves;
6. support-cycle pivots give explicit root-level lifts of selected connected switches and preserve the uncoloured embedding;
7. exact used/unused-root update under a pivot;
8. the new gauge fibre after switching must be recomputed and need not preserve dimension;
9. internal fixed-plane switch correction through the Schur boundary and component-incidence code;
10. external reslicing through even supports containing a fixed zero matching.

## 3. Required scope corrections

1. `7737` counts all nonzero admissible switch pairs in the named laboratory; `2801` counts connected-support one-edge neighbours.
2. The linear switch image ranges over all composite same-direction endpoints. Connected-neighbour correction sets need not be linear.
3. “Every even support $B'\supseteq M$” in the external theorem describes composite same-direction reachability; one adjacency additionally requires connected symmetric difference.
4. A support pivot does not explore the new fibre; it supplies one distinguished lift, after which the new gauge system must be solved.
5. Laboratory ranks, fibre sizes, and success counts remain certificate data.

## 4. Recommended destinations

- `five-support/gauge-and-reconfiguration.md`;
- `gauge/gauge-modes-and-circuits.md` where disconnected reduction or topological interpretation is synchronized;
- topology/surface chapters for the Petrial correspondence;
- fixed-plane switch and defect chapters;
- `THEOREM_DEPENDENCY_MAP.md` and `MATHEMATICAL_ARCHITECTURE.md`;
- certificate and provenance ledgers.

## 5. Frontier boundary

The checkpoint does not prove that every fibre or reconfiguration component reaches a good state, that one-star cores always escape, or that a monotone potential exists. These remain genuine global/source questions.

## 6. Success test

1. Exact B4 checkpoint remains fixed.
2. Vertical and horizontal moves remain distinct.
3. Connected adjacency and disconnected paths are never conflated.
4. Internal and external fixed-plane switches retain their different quotient behavior.
5. Finite counts remain on the certificate axis.
6. No B5+ work, formalization, release, publication, or `main` movement is implied.

Staging is authorized; canonical movement is not.