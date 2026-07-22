# AC-OR1 provenance and assurance boundary

## 1. Exact source genealogy

### Controlling integrated base

`curation/affine-cdc-programme-a-b1-b8-unified-v1@ec765cd03271abd3588ec36faec3d53d0f8aa03b`.

### Authorial proof-development source

`proof-development/affine-cdc-rigour-v1@9dc0b3a5c906e51f8f1816e00b85f7aa2a744b1b`.

Controlling OR1 files:

- `AC_PD_OR1_1_SURFACE_AND_ORIENTATION_CLASS.md`;
- `AC_PD_OR1_2_GAUGE_FIBRE_AND_DUALITY.md`;
- `AC_PD_OR1_3_K4_AND_OUTER_SHELL_TRANSPORT.md`;
- `AC_PD_OR1_ORIENTATION_OBSTRUCTION_MAP.md`.

### Dependency registration

`29657f08253df87baa37ad09c88cce25904c189a` changes the PDL obligation DAG after the mathematical checkpoint. It is consumed only as dependency/frontier metadata.

### Checked reconstruction boundary

`Yuren-Tang/affine-cdc:main@ebd7098a7a8b824e8c0a511d3c71f61705672aa8`.

### Triggering audit input

Issue #49 is retained only as the trigger that caused AC-PDL to reconstruct the theory. The canonical mathematics is controlled by the PDL proofs above, not by the audit return.

## 2. Canonical successor chapters

| Mathematical content | Canonical chapter |
|---|---|
| retained face occurrences, dart rotations, surface, $\omega(g)$ | `orientation/surface-and-fixed-lift-obstruction.md` |
| $\Lambda_f$, gauge law, $\Omega_f$, torsor/coset, orientation stress | `orientation/fixed-fibre-gauge-and-duality.md` |
| exact $K_4$, support-only loss, enriched collapse, loops | `orientation/k4-and-oriented-collapse.md` |
| dependency and open frontier | `AC_OR1_DEPENDENCY_AND_FRONTIER_MAP.md` |
| source intake and TeX correction | `AC_OR1_INTEGRATION_MAP.md` |

## 3. Assurance classes

### Authorial proof

The following are `AUTHORIAL / COMPLETE-DRAFT / CURATOR-INTEGRATED`:

- retained-data surface reconstruction;
- the fixed-lift class $\omega(g)$ and its orientability criterion;
- gauge/partial-Petrial translation of twist words;
- the fixed-fibre class $\Omega_f$;
- labelled empty-or-torsor and unlabelled Petrial-coset classifications;
- the dual orientation-stress criterion;
- the exact $K_4$ same-fibre theorem;
- enriched directed collapse and opposite loop-dart reinsertion.

### Independent audit

No dedicated independent fixed-corpus audit has yet been completed for OR1. Curator integration does not upgrade authorial proof to `AUDITED`.

The candidate is suitable to become the immutable input of such an audit.

### Lean

Machine checked at the exact boundary:

- indexed dart supports;
- edge-reversal closure;
- exact two-support membership;
- unique same-vertex partner;
- partner involution;
- explicit rotations $\rho$ and $\rho^{-1}$;
- graph-level support extraction and generic undirected decomposition.

Not machine checked at that boundary:

- construction of the cellular surface as an orientability object;
- $w(g)$, $\omega(g)$, or $\Omega_f$;
- the gauge law in orientation-cochain form;
- orientation stress;
- the $K_4$ projective-plane/sphere fibre classification;
- enriched oriented collapse;
- loop-dart opposite-direction reinsertion;
- either global orientation-existence obligation.

The existing graph-level Lean theorem discards the rotation witness before generic decomposition. It therefore cannot be cited as an oriented-CDC theorem.

## 4. Counterexample assurance

The $K_4$ result is a direct finite proof, not a code census:

- $g_0$ has three four-cycle faces and Euler characteristic $1$;
- $g_1$ has four triangular faces and Euler characteristic $2$;
- both lie above the same fixed flow;
- $\Lambda_f(k)=\mathbf 1_E$ connects them.

It refutes only per-lift automaticity. Since $g_1$ is orientable, the same example proves $\Omega_f=0$ rather than nonvanishing.

## 5. Source/rendering defect

The named `PROGRAMME_OR1_CURATOR_HANDOFF.md` file is absent from the exact mathematical checkpoint and DAG registration ref. The complete epoch remains recoverable from the four dossiers and registration diff.

This is returned to AC-PDL as a non-blocking packaging defect.

The malformed control character in PDL OR1.2 Corollary 5.1 is corrected in the canonical successor. It changes no mathematical statement.

## 6. Non-supersession boundaries

OR1 does not supersede:

- Programme A's ordinary CDC theorem;
- the support-only collapse theorem as the controlling ordinary-CDC composition interface;
- B1--B8 five-support mathematics;
- the six existing five-support frontier obligations;
- the partial Lean anchor.

OR1 adds a conditional oriented refinement and its own two open existence obligations.

## 7. External/projection status

This intake creates no:

- manuscript acceptance or correspondence claim;
- peer review;
- publication or submission authorization;
- release or tag;
- arXiv or DOI action;
- novelty or priority determination;
- canonical `main` movement.

## 8. Final assurance phrase

`INTEGRATED ORIENTATION-OBSTRUCTION CANDIDATE / AUTHORIAL FIXED-FIBRE CLASSIFICATION / READY-FOR-INDEPENDENT FIXED-CORPUS AUDIT / LEAN RECONSTRUCTION INGREDIENTS ONLY / GLOBAL ORIENTED EXISTENCE OPEN`.
