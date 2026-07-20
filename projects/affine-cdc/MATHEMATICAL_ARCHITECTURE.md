# AffineCDC mathematical architecture

## 1. Project scopes

1. **Affine compatibility core** — compatible affine families above nowhere-zero binary flows.
2. **Complete Cycle Double Cover theorem** — Programme A.
3. **Five-support strengthening** — five indexed even supports, equivalently an $R_5$-valued flow.

Programme A is complete at paper level. The five-support strengthening remains open and is not used in Programme A.

## 2. Unified alignment

The unified candidate combines:

- accepted B1–B8 base `0100895d57aab7d21153c580fa9bdc45fafc832e`;
- Programme A repair checkpoint `06bce656dcf5bfd6491ec08f51a702ea56d2470d`;
- exact repair splice `a35da6ba6e4908c70f970f3cadf5fcf4b582dae4`.

It absorbs only the three Audit A explicitness/source repairs and does not consume B9 or AC-RL working-ahead material.

## 3. Programme A — complete CDC

Controlling theorem:

> Every multigraph with finite active edge set and no singleton cut has a finite circuit double cover.

The original Programme A candidate `68715fb29bb4b6555e2bc3e089603c5390d01566` passed Independent Audit A at `2fac31f4e76c819dd42a179a2772501c50ee93ad`.

The controlling proof chain is:

```text
finite-active multigraph and circuit semantics
→ loop deletion
→ port-cycle cubic expansion
→ Seymour six-flow on finite connected loopless multigraph components
→ integral eight-flow
→ Z/8Z flow
→ internal equal-order transport to F₂³
→ affine pair complex
→ rank-three compatibility
→ graph/dart indexed support extraction
→ loopless parity adapter
→ cut-even collapse
→ circuit decomposition
→ loop reinsertion.
```

Audit A repairs close:

- explicit parallel-edge/loopless/componentwise Seymour convention;
- complete A4 reverse local-family reconstruction;
- historical, non-controlling status of the old Tutte route.

These repairs change no theorem or dependency.

## 4. B1–B2 foundation

B1 controls exact five-support objects and quantifiers: root flows, $K_5$ triangles, matching/four-flow data, Fano-plane criteria, cycle-face surfaces, prescribed-dual holonomy, and old-colour factorability.

B2 enlarges the witness box to anisotropic $O^-(4,2)$ flows, quadratic cycle solutions, and cographic cycle-continuous maps; it separates fixed singular/Schur criteria and stress/Fourier dual layers. The false universal $2r$ orthogonal theorem remains superseded by the $q-2$ deleted permutation module.

## 5. B3 target hierarchy

For fixed compatible lift $g$:

$$
J_g\to\mathscr A_5
\Longrightarrow
T_g^{(1)}\to\mathscr A_5
\Longrightarrow
\text{five-support cover}.
$$

$T_g^{(1)}$ is the full componentwise dual; $J_g$ is only the old-colour quotient. B3 retains exact link/capacity, eight-vertex factorable, unused-matching/core, ideal-pivot, and conditional flower results.

## 6. B4 motion

Vertical lifts form an $H_f^0$ torsor with reduced code $H_f^0/\Gamma^{\pi_0(G)}$ and partial-Petrial interpretation.

One horizontal edge is one connected-cycle switch. A disconnected switch is a commuting path. A support pivot supplies one explicit new lift; the new fibre must be recomputed. Internal correction and external reslicing classify composite endpoints, not automatically one-step neighbours.

## 7. B5 interfaces

```text
cubic local law
→ cyclic three-cut gluing
→ ten four-pole states
→ exact profile intersection
→ cap forcing
→ Kempe pairing alignment
→ routing weights
→ uniform-routing elimination
→ residual Type T / Type H mechanisms.
```

Cap forcing is not full-cap containment; finite transitions are not source path realizability.

## 8. B6 correction

Unconditional results retain individual-loop holonomy, genuine path families, root-fibre/Tait resolution, Type H soluble escape, DDD atom triality, unique bad route, and conditional local $K_6$/Petersen geometry.

BBD simultaneous origin is conditional on `AC-RL-BBD-GROUPOID-CLOSURE`. The nontrivial defect-minimal forest is removed pending `AC-RL-BBD-VARIATION-SLICE`.

## 9. B7 localization frontier

Rank one is impossible; rank two gives Tait/root-triangle escape; full rank has a flat/nonflat curvature dichotomy. Flatness gives an eight-state potential; nonflatness gives a common scalar-sheet cut with odd terminal parity.

These are not yet source-graph localization or bounded composition theorems. The remaining B7 returns are:

- `AC-RL-TYPE-T-SERIALISATION`;
- `AC-RL-FLAT-POTENTIAL-INTERFACE`;
- `AC-RL-COMMON-CUT-LOCALISATION`;
- `AC-RL-TYPE-H-COMMON-WITNESS`.

## 10. B8 assurance and global frontier

Finite results retain the six classes `F-PROVED`, `F-CERT-PUBLIC`, `F-CERT-PRIVATE`, `F-CENSUS`, `CODE-PARTIAL`, and `AFFECTED`.

The missing global theorem must convert persistent bad data into an escaping good state or strict source progress. B9 remains excluded and blocked on localization/composition.

## 11. Assurance boundary

Programme A’s original theorem spine has passed Audit A; the closed repaired prose is integrated but not separately re-audited. B1–B8 remain pending Audit B. No end-to-end Lean, manuscript, publication, release, arXiv, DOI, novelty, timestamp, or canonical `main` status is created.