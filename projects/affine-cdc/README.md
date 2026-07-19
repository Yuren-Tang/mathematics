# AffineCDC

AffineCDC studies affine incidence geometry attached to nowhere-zero binary flows, its complete Cycle Double Cover consequence, and the stronger open problem of compressing the compatible cover to five indexed supports.

The active current-best surface is listed in [`ACTIVE_MATHEMATICAL_SURFACE.md`](ACTIVE_MATHEMATICAL_SURFACE.md).

## 1. Complete Cycle Double Cover spine

The paper-level mathematical chain is:

$$
oxed{
egin{array}{c}
	ext{bridgeless multigraph with finite active edge set}\
\downarrow\;	ext{delete loops}\
	ext{finite loopless bridgeless core}\
\downarrow\
	ext{cubic expansion with nowhere-zero }\mathbf F_2^3	ext{ flow}\
\downarrow\
	ext{rank-three affine compatibility}\
\downarrow\
	ext{graph-level multiset even double cover}\
\downarrow\
	ext{cut-even collapse transport}\
\downarrow\
	ext{one circuit decomposition and loop reinsertion}\
\downarrow\
	ext{cycle double cover.}
\end{array}}
$$

The natural external theorem is:

> Every multigraph with finite active edge set and no bridges has a cycle double cover.

Loops are allowed; a singleton loop is a cut-even circuit. The companion Lean declaration remains an earlier loopless ambient-finite checkpoint and is not yet the final theorem.

Start with:

- [`MATHEMATICAL_ARCHITECTURE.md`](MATHEMATICAL_ARCHITECTURE.md);
- [`core/affine-incidence-and-obstruction.md`](core/affine-incidence-and-obstruction.md);
- [`core/rank-three-fano-compatibility.md`](core/rank-three-fano-compatibility.md);
- [`reduction/outer-shell-and-binary-flow.md`](reduction/outer-shell-and-binary-flow.md);
- [`reduction/even-cover-and-collapse.md`](reduction/even-cover-and-collapse.md).

## 2. Five-support strengthening

An indexed five-support cover is equivalently a root-valued flow

$$
E(G)\longrightarrow R_5\subset E_5.
$$

Above a Fano flow, the rank-three theorem always gives a compatible eight-support root lift. The strengthening asks whether some flow and compatible lift have a cycle-face dual triangulation admitting

$$
oxed{T_g^{(1)}\longrightarrow\mathscr A_5.}
$$

The older quotient criterion `J_g -> A_5` describes only global-index-factorable maps. The global five-support theorem remains open.

Read:

1. [`five-support/root-flow-lifting.md`](five-support/root-flow-lifting.md);
2. [`five-support/surfaces-and-halfcube.md`](five-support/surfaces-and-halfcube.md);
3. [`five-support/gauge-and-reconfiguration.md`](five-support/gauge-and-reconfiguration.md);
4. [`five-support/cuts-four-poles-and-routing.md`](five-support/cuts-four-poles-and-routing.md);
5. [`five-support/holonomy-defects-and-atoms.md`](five-support/holonomy-defects-and-atoms.md);
6. [`five-support/frontier-localisation.md`](five-support/frontier-localisation.md);
7. [`five-support/equivalent-formulations-and-proof-families.md`](five-support/equivalent-formulations-and-proof-families.md);
8. [`five-support/finite-laboratories-and-certificates.md`](five-support/finite-laboratories-and-certificates.md).

## 3. Current frontier

The local algebra, target geometry, gauge structure, finite interfaces, and principal finite laboratories are largely classified. The sharp endpoint is graph-level localisation and composition of full-rank route-locked defects.

- nonzero curvature gives a support-minimal common-cut witness with odd terminal parity;
- zero curvature gives an eight-state affine potential;
- neither output has yet been converted universally into a bounded replacement, smaller separator, transition split, or gluing theorem.

See [`FRONTIER_STATUS.md`](FRONTIER_STATUS.md).

## 4. Provenance, retirement, and recovery

The seventy-eight discovery-order `research/FIVE_CDC_*.md` packets were read at exact checkpoint

`dad218dd18ed05d1b7cb730c2dc2431b4db5ec9c`.

After substantive migration they are retired from the current tip. Their public commits, priority, bodies, counterexamples, and finite certificates remain recoverable through ordinary Git ancestry.

- [`CHAPTER_PROVENANCE.md`](CHAPTER_PROVENANCE.md) — source packets by active chapter;
- [`MIGRATION_LEDGER.md`](MIGRATION_LEDGER.md) — source-to-successor transfer;
- [`RETIRED_SOURCE_CLASSIFICATION.md`](RETIRED_SOURCE_CLASSIFICATION.md) — exhaustive 78-file retirement classification;
- [`SOURCE_RECOVERY_AUDIT.md`](SOURCE_RECOVERY_AUDIT.md) — exact ancestry and recovery commands;
- [`SUPERSESSION_MAP.md`](SUPERSESSION_MAP.md) — controlling corrections and negative boundaries.

## 5. Reliability and audit

- [`CURRENT_BEST.md`](CURRENT_BEST.md) — compact current mathematical state;
- [`THEOREM_DEPENDENCY_MAP.md`](THEOREM_DEPENDENCY_MAP.md) — dependency graph;
- [`FORMAL_STATUS.md`](FORMAL_STATUS.md) — theorem, finite, open, formal, and review boundaries;
- [`RECONSTRUCTION_MANIFEST.md`](RECONSTRUCTION_MANIFEST.md) — final reconstruction and no-loss manifest.

Current-best inclusion does not create Lean, independent-review, peer-review, manuscript, publication, release, arXiv, or DOI status.