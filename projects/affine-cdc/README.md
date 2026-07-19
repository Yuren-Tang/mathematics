# AffineCDC

AffineCDC studies affine incidence geometry attached to nowhere-zero binary flows, its complete Cycle Double Cover consequence, and the stronger open problem of compressing the compatible cover to five indexed supports.

The project now has two explicitly separated theorem lines.

## 1. Complete Cycle Double Cover spine

The paper-level mathematical chain is:

$$
\boxed{
\begin{array}{c}
\text{bridgeless multigraph with finite active edge set}\\
\downarrow\;\text{delete loops}\\
\text{finite loopless bridgeless core}\\
\downarrow\\
\text{cubic expansion with nowhere-zero }\mathbf F_2^3\text{ flow}\\
\downarrow\\
\text{rank-three affine compatibility}\\
\downarrow\\
\text{graph-level multiset even double cover}\\
\downarrow\\
\text{cut-even collapse transport}\\
\downarrow\\
\text{one circuit decomposition and loop reinsertion}\\
\downarrow\\
\text{cycle double cover.}
\end{array}}
$$

The natural external theorem is:

> Every multigraph with finite active edge set and no bridges has a cycle double cover.

Loops are allowed; a singleton loop is a cut-even circuit. The current companion Lean declaration remains an earlier loopless ambient-finite checkpoint and is not yet the final theorem.

Start with:

- [`MATHEMATICAL_ARCHITECTURE.md`](MATHEMATICAL_ARCHITECTURE.md);
- [`core/affine-incidence-and-obstruction.md`](core/affine-incidence-and-obstruction.md);
- [`core/rank-three-fano-compatibility.md`](core/rank-three-fano-compatibility.md);
- [`reduction/even-cover-and-collapse.md`](reduction/even-cover-and-collapse.md);
- [`reduction/outer-shell-and-binary-flow.md`](reduction/outer-shell-and-binary-flow.md).

## 2. Five-support strengthening

An indexed five-support cover is equivalently a root-valued flow

$$
E(G)\longrightarrow R_5\subset E_5.
$$

Above a Fano flow, the rank-three theorem always gives a compatible eight-support root lift. The strengthening asks whether some flow and some compatible lift can be represented componentwise in the five-coordinate half-cube.

For a fixed compatible lift $g$, the controlling criterion is

$$
\boxed{T_g^{(1)}\longrightarrow\mathscr A_5,}
$$

where $T_g$ is the full dual triangulation of the cycle-face surface. The older quotient criterion $J_g\to\mathscr A_5$ describes only global-index-factorable maps.

The global five-support theorem remains open.

Read the reconstructed corpus in this order:

1. [`five-support/root-flow-lifting.md`](five-support/root-flow-lifting.md);
2. [`five-support/surfaces-and-halfcube.md`](five-support/surfaces-and-halfcube.md);
3. [`five-support/gauge-and-reconfiguration.md`](five-support/gauge-and-reconfiguration.md);
4. [`five-support/cuts-four-poles-and-routing.md`](five-support/cuts-four-poles-and-routing.md);
5. [`five-support/holonomy-defects-and-atoms.md`](five-support/holonomy-defects-and-atoms.md);
6. [`five-support/frontier-localisation.md`](five-support/frontier-localisation.md).

Alternate proofs and finite evidence are consolidated in:

- [`five-support/equivalent-formulations-and-proof-families.md`](five-support/equivalent-formulations-and-proof-families.md);
- [`five-support/finite-laboratories-and-certificates.md`](five-support/finite-laboratories-and-certificates.md).

## 3. Current frontier

The local and finite universes are largely classified. The missing theorem is global localisation and composition.

The sharpest endpoint begins with a blocked one-edge co-root atom. Unique-bad-route reduction gives a locked quotient flow with four scalar circuit partitions. Rank two escapes through a Tait lift. In full rank:

- nonzero curvature gives a support-minimal common-cut witness with odd terminal parity;
- zero curvature gives an eight-state affine potential.

Neither output has yet been converted universally into a bounded replacement, smaller separator, transition split, or gluing theorem. See [`FRONTIER_STATUS.md`](FRONTIER_STATUS.md).

## 4. Navigation and audit

- [`CURRENT_BEST.md`](CURRENT_BEST.md) — compact mathematical state;
- [`THEOREM_DEPENDENCY_MAP.md`](THEOREM_DEPENDENCY_MAP.md) — dependency graph for both theorem lines;
- [`FRONTIER_STATUS.md`](FRONTIER_STATUS.md) — exact open boundary and intake rule;
- [`SUPERSESSION_MAP.md`](SUPERSESSION_MAP.md) — controlling corrections and retained historical formulations;
- [`MIGRATION_LEDGER.md`](MIGRATION_LEDGER.md) — source-to-corpus destinations;
- [`FORMAL_STATUS.md`](FORMAL_STATUS.md) — assurance and formalization boundary;
- [`RECONSTRUCTION_MANIFEST.md`](RECONSTRUCTION_MANIFEST.md) — exact reconstruction provenance and self-audit.

## 5. Source preservation

All inherited `research/FIVE_CDC_*.md` packets remain in the repository with their exact history. They record discovery order, priority, finite certificates, counterexamples, corrections, and intermediate proof families. They are no longer the primary reading path.

The reconstructed chapters synthesize the public mathematical content without deleting the source surface or upgrading its assurance status.