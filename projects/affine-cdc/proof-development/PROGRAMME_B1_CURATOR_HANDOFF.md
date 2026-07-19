# CURATION-HANDOFF — AffineCDC Programme B1

**Project:** AffineCDC  
**Prepared by:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Authority basis:** research-workbench issue #37; persistent proof-development policy; AC-PDL charter  
**Live source branch:** `Yuren-Tang/mathematics:proof-development/affine-cdc-rigour-v1`  
**Immutable source checkpoint SHA:** `778b09ac8260192e022f512f24cdef1d04871f37`  
**Included packet/file range:** `AC_PD_B1_1_*.md` through `AC_PD_B1_4_*.md`, `AC_PD_B1_EQUIVALENCE_AND_SCOPE_MAP.md`, and `OBLIGATION_DAG.md` at the immutable checkpoint  
**Controlling canonical base:** `Yuren-Tang/mathematics:main@960c92b7ff231c78b387894149779083060a75eb`  
**Packet classification:** `PROOF-DEVELOPMENT / PROGRAMME-B1 / READY-FOR-CURATOR`  
**Mathematical completeness:** complete for the root-flow/fixed-plane/fixed-lift equivalence and scope layer  
**Independent-review state:** not independently audited  
**Reliability/trust classification:** complete authorial proofs plus two corpus corrections and two scope corrections; no claim of global five-support existence  
**Live branch may continue beyond checkpoint:** yes; all B2+ commits are excluded unless separately handed off  
**Staging authorized:** yes, on a dedicated Curator branch only  
**Merge/default-branch authority:** no  
**Next disposition receiver:** `Mathematics — Curator` (`MATH-CUR`), then AffineCDC governance for any canonical movement

## 1. Intake objective

Integrate the exact B1 object and quantifier layer into the rolling five-support corpus. The goal is not merely to add proofs, but to correct the active statements so that graph-level existence, fixed-flow factorability, fixed-lift same-embedding compression, and old-colour quotient compression are no longer conflated.

## 2. Accepted mathematical content

The packet proves:

1. indexed five-support even covers are canonically equivalent to $R_5$-valued $E_5$ flows and $K_5$-triangle labellings;
2. the exact matching/four-flow theorem uses even supports $B,D$, matching $M=B\cap D$, and a nowhere-zero $\mathbf F_2^2$-flow on $G-M$;
3. eliminating $D$ requires an explicit component endpoint-parity/$T$-join condition;
4. for fixed $(f,W)$, global five-coordinate factorability is equivalent to the local affine obstruction, one/all outside-colour cut parities, distinguished-support existence, and quotient-colour Eulerianity;
5. graph-level five-support existence is equivalent to existential $(f,W)$ with an empty plane profile;
6. compatible root lifts are equivalent to properly coloured cycle-face surfaces and dual triangular cellulations;
7. full-dual half-cube potentials give componentwise same-embedding compression;
8. an external root flow integrates on a fixed dual exactly when all dual cycle holonomies vanish;
9. $J_g\to\mathscr A_5$ is precisely the old-colour-factorable subclass;
10. graph-level five-support existence is equivalent to existence of some cycle-face embedding whose dual maps to the even half-cube.

## 3. Required corpus corrections

1. **Matching correction.** A fixed support-coordinate inverse image is even, not a matching. A fixed root-label inverse image is a matching.
2. **Four-flow converse correction.** Bare matching plus four-flow is insufficient; the $(B,D)$ or component-parity datum is required.
3. **Fixed-lift scope correction.** The fixed-$g$ biconditional must mean componentwise relabelling of the same dual surface; it is not arbitrary cover existence on $G$.
4. **Holonomy boundary.** Local triangular conservation does not guarantee integration on one prescribed dual graph.
5. **Factorability boundary.** $J_g$ classifies only maps constant on old-colour fibres.
6. **Half-cube parity correction.** Singleton words lie in the odd component; the even component requires an odd translation.

## 4. Recommended destinations

The Curator should stage coherent edits to:

- `five-support/root-flow-lifting.md`;
- `five-support/equivalent-formulations-and-proof-families.md`;
- `five-support/surfaces-and-halfcube.md`;
- `THEOREM_DEPENDENCY_MAP.md`;
- `MATHEMATICAL_ARCHITECTURE.md` and `FORMAL_STATUS.md` only where status/scope synchronization is required;
- retained proof-development provenance for the complete dossiers.

The recovered research packets should remain cited as provenance, especially the matching theorem, fixed-flow criterion, colour-cut refinement, surface scope correction, and displayed-table erratum.

## 5. Exclusions

- no assertion of the global five-support theorem;
- no B2–B9 material;
- no promotion of finite certificates to universal proof;
- no claim that the $K_6/K_8-C_5$ theorem classifies the full dual;
- no claim of formal verification or independent audit;
- no `main`, release, manuscript, DOI, or publication action.

## 6. Curator success test

The intake succeeds when:

1. the immutable SHA remains the consumed source;
2. all graph/fixed-flow/fixed-lift quantifiers are explicit;
3. the matching/four-flow statement includes the missing datum;
4. the full-dual and colour-quotient targets are separated;
5. the even-halfcube parity convention is corrected;
6. the dual-holonomy criterion is visible where fixed-surface converse language occurs;
7. every equivalence arrow has a recoverable B1 proof pointer;
8. no later branch delta is silently consumed;
9. any mathematical defect returns to AC-PDL as a repair unit.

## 7. Stop conditions

Return rather than guess if integration reveals a contradiction with a later controlling packet, a need to change the graph model, an unrecorded fixed-data hypothesis, an ambiguity between even supports and post-decomposition circuits, or a need to consume B2+ work.

Staging is authorized; canonical movement is not.