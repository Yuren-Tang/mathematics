# AC-CUR-OR1 final curation audit

## 1. Exact controls

- role: `Mathematics — Curator` (`MATH-CUR`);
- intake code: `AC-CUR-OR1`;
- controlling inbox: `Yuren-Tang/research-workbench#24`, comment `5049999050`;
- ACK: issue #24 comment `5050156347`;
- candidate branch: `curation/affine-cdc-orientation-obstruction-v1`;
- exact base: `ec765cd03271abd3588ec36faec3d53d0f8aa03b`;
- exact authorial PDL checkpoint: `9dc0b3a5c906e51f8f1816e00b85f7aa2a744b1b`;
- DAG registration metadata: `29657f08253df87baa37ad09c88cce25904c189a`;
- checked Lean boundary: `Yuren-Tang/affine-cdc@ebd7098a7a8b824e8c0a511d3c71f61705672aa8`.

The exact final candidate SHA is recorded in the authoritative issue #24 return because a commit cannot contain its own SHA.

## 2. Source and branch audit

The target branch was absent before intake and was created exactly from `ec765cd...`.

The PDL source diverges from the unified base and contains unrelated B2/B8 source-fidelity material. The candidate therefore consumes only the four OR1 dossiers and the later OR1 DAG registration metadata. It does not merge or copy the whole PDL branch.

Before this audit file, the candidate was:

- `16` commits ahead of the exact base;
- `0` behind;
- merge base exactly `ec765cd03271abd3588ec36faec3d53d0f8aa03b`;
- `16` changed paths.

This final audit adds one control path only.

## 3. Complete candidate path inventory

### New orientation chapters

1. `projects/affine-cdc/orientation/README.md`;
2. `projects/affine-cdc/orientation/surface-and-fixed-lift-obstruction.md`;
3. `projects/affine-cdc/orientation/fixed-fibre-gauge-and-duality.md`;
4. `projects/affine-cdc/orientation/k4-and-oriented-collapse.md`.

### New OR1 controls

5. `projects/affine-cdc/AC_OR1_INTEGRATION_MAP.md`;
6. `projects/affine-cdc/AC_OR1_DEPENDENCY_AND_FRONTIER_MAP.md`;
7. `projects/affine-cdc/AC_OR1_PROVENANCE_AND_ASSURANCE.md`;
8. `projects/affine-cdc/AC_OR1_FINAL_AUDIT.md`.

### Synchronized existing controls

9. `projects/affine-cdc/README.md`;
10. `projects/affine-cdc/CURRENT_BEST.md`;
11. `projects/affine-cdc/MATHEMATICAL_ARCHITECTURE.md`;
12. `projects/affine-cdc/THEOREM_DEPENDENCY_MAP.md`;
13. `projects/affine-cdc/FORMAL_STATUS.md`;
14. `projects/affine-cdc/ACTIVE_MATHEMATICAL_SURFACE.md`;
15. `projects/affine-cdc/CHAPTER_PROVENANCE.md`;
16. `projects/affine-cdc/SUPERSESSION_MAP.md`;
17. `projects/affine-cdc/FRONTIER_STATUS.md`.

No `proof-development/`, `complete-cdc/`, `five-support/`, `reduction/`, Lean, manuscript, release, workflow, tag, or DOI path is modified.

## 4. Retained-data surface reconstruction

The candidate keeps the exact occurrence distinctions:

- empty indexed supports remain empty indices but contribute no face;
- different connected components of one support are different face occurrences;
- equal supports at different affine indices remain different occurrences;
- no generic circuit decomposition replaces the retained occurrences.

The checked dart ingredients

$$
(M_a,\operatorname{partner}_a,\sigma,\rho_a,\rho_a^{-1})
$$

reconstruct the indexed cycle-face surface $S_g$. The graph-level Lean theorem discards $\rho$ before a generic undirected support decomposition and is not used as orientation theorem authority.

## 5. Fixed-lift obstruction audit

For chosen vertex-disc orientations, the edge-band twist word is $w(g)\in C^1(G)$. Vertex-disc reversal adds a coboundary, so

$$
\omega(g)=[w(g)]\in C^1(G)/\operatorname{Cut}(G)
$$

is intrinsic to the fixed lift.

The candidate retains the exact equivalence:

$$
S_g\text{ orientable}
\iff
w(g)\in\operatorname{Cut}(G)
\iff
\omega(g)=0
\iff
\langle w(g),z\rangle=0\ (z\in Z_1(G))
$$

and the equivalent statement that the retained face occurrences traverse every edge in opposite directions.

## 6. Gauge and fixed-fibre audit

The integrated B4 vertical torsor supplies $H_f^0$ and

$$
\Lambda_f:H_f^0\to C^1(G),
\qquad
\mathcal B_f=\operatorname{im}\Lambda_f.
$$

The chain-level law is

$$
w(g^k)=w(g)+\Lambda_f(k)
$$

for transported local orientations, and the quotient law holds modulo cuts.

The labelled orientable lifts form either the empty set or

$$
k_0+\ker\Lambda_{\mathrm{or}}.
$$

The fixed-fibre class is

$$
\Omega_f\in C^1(G)/(\operatorname{Cut}(G)+\mathcal B_f),
$$

with orientable-lift existence exactly equivalent to $\Omega_f=0$.

The unlabelled orientable Petrial words form either the empty set or

$$
\lambda_0+\bigl(\mathcal B_f\cap\operatorname{Cut}(G)\bigr).
$$

The labelled torsor and unlabelled coset are not conflated.

## 7. TeX/control-character repair

The PDL source of OR1.2 Corollary 5.1 contains a backspace/control character before the intended `\bigl` command.

The canonical successor contains the valid formula

$$
\boxed{
\mathcal P_g=\varnothing
\quad\text{or}\quad
\lambda_0+\bigl(\mathcal B_f\cap\operatorname{Cut}(G)\bigr).
}
$$

The repair changes no theorem or quantifier.

## 8. Duality audit

The orientation-stress space is

$$
\operatorname{Stress}_{\mathrm{or}}(f)
=Z_1(G)\cap\mathcal B_f^\perp.
$$

The fixed fibre contains an orientable lift if and only if $w(g)$ annihilates this space.

This is explicitly separated from Programme A compatibility stress:

- compatibility stress tests nonemptiness of the compatible-lift fibre;
- orientation stress tests whether that fibre meets the orientable locus.

No identification or implication is inferred solely from Fano self-duality.

## 9. Exact $K_4$ audit

For the standard $K_4$ rank-three flow:

- $g_0$ has three Hamiltonian four-cycle faces, $\chi=1$, and gives the projective plane;
- the field $k_u=u$ has $\Lambda_f(k)=\mathbf 1_E$;
- $g_1$ has four triangular faces, $\chi=2$, and gives the tetrahedral sphere.

Thus one fixed fibre contains both orientability types.

Exact conclusion:

- per-lift automatic orientability is false;
- the gauge action changes $\omega(g)$;
- this example has $\Omega_f=0$ and is not a fixed-fibre counterexample.

## 10. Outer-shell audit

The ordinary Programme A support-only route retains cut parity and exact multiplicity but discards directions, partner maps, and rotations before generic decomposition. It does not transport an orientation witness.

The enriched theorem retains directed face occurrences, projects each to an empty word or directed closed trail, and decomposes trails into directed circuits without reversing edges. Therefore every original edge remains once in each direction downstairs.

Deleted loops are reinserted as two singleton-loop occurrences in opposite dart directions under the explicit loop convention.

The open theorem is orientable-lift existence, not collapse transport.

## 11. Exact frontier audit

Five-support obligations remain unchanged:

- `AC-RL-BBD-GROUPOID-CLOSURE`;
- `AC-RL-BBD-VARIATION-SLICE`;
- `AC-RL-TYPE-T-SERIALISATION`;
- `AC-RL-FLAT-POTENTIAL-INTERFACE`;
- `AC-RL-COMMON-CUT-LOCALISATION`;
- `AC-RL-TYPE-H-COMMON-WITNESS`.

Orientation obligations are exactly:

- `AC-RL-OR-FIXED-FIBRE-VANISHING`;
- `AC-RL-OR-GRAPH-EXISTENCE`.

No obligation is silently closed, renamed, broadened, or inferred from the $K_4$ example.

## 12. Handoff packaging defect

The intake-named path

`projects/affine-cdc/proof-development/PROGRAMME_OR1_CURATOR_HANDOFF.md`

is absent at both exact PDL refs. The four dossiers and DAG registration contain the complete mathematical and dependency packet, so no mathematical stop condition is triggered.

Return to AC-PDL:

`AC-PDL-OR1-HANDOFF-FILE-MISSING / PACKAGING DEFECT / NON-MATHEMATICAL / NON-BLOCKING`.

The Curator does not invent or backfill a PDL-authored file.

## 13. Assurance audit

- OR1 mathematical proofs: authorial PDL complete-draft, Curator-integrated;
- independent OR1 audit: not yet performed;
- Lean: retained reconstruction ingredients and support-level extraction only;
- issue #49: triggering audit input, not accepted theorem authority;
- global oriented existence: open;
- ordinary CDC theorem and five-support state: unchanged.

The candidate is suitable as an immutable input for an independent fixed-corpus audit.

## 14. Repository isolation

Only `Yuren-Tang/mathematics:curation/affine-cdc-orientation-obstruction-v1` is written.

Unchanged by this intake:

- the exact unified base branch and commit;
- `mathematics:main`;
- the PDL branch and exact source checkpoint;
- DAG registration commit;
- `Yuren-Tang/affine-cdc:main` and all Lean files;
- all manuscript, review, release, tag, workflow, publication, arXiv, and DOI surfaces.

No force-push, rebase, squash, merge, PR, branch deletion, rename, source rewrite, or canonical movement occurs.

## 15. Stop-condition audit

No genuine stop condition is triggered.

- source ancestry and exact refs are recoverable;
- no writer collision exists;
- the four dossiers are mutually consistent;
- the malformed TeX is a local rendering defect with an unambiguous correction;
- no missing mathematical implication is silently supplied;
- support-only and enriched collapse are honestly separated;
- authorial, audit, and Lean statuses remain distinct;
- the missing handoff file is a non-blocking packaging defect;
- owner-only actions are not required to complete the candidate.

## 16. Final classification

`INTEGRATED ORIENTATION-OBSTRUCTION CANDIDATE / READY-FOR-INDEPENDENT FIXED-CORPUS AUDIT / GLOBAL ORIENTED EXISTENCE OPEN`.

This classification does not imply independent acceptance, end-to-end Lean verification, manuscript correspondence, peer review, publication, release, arXiv, DOI, novelty, priority, or canonical `main` status.
