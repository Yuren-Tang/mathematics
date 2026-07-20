# CURATION-HANDOFF — AffineCDC Programme B9 corrected frontier

**Project:** AffineCDC  
**Prepared by:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Live source branch:** `Yuren-Tang/mathematics:proof-development/affine-cdc-rigour-v1`  
**Immutable mathematical checkpoint:** `e49a990b9b66de6248cc0733ff53eeeff9ec941e`  
**Included packet:** `AC_PD_B9_CORRECTED_GLOBAL_FRONTIER_ASSEMBLY.md` and `OBLIGATION_DAG.md` at the immutable checkpoint  
**Controlling canonical base:** `main@960c92b7ff231c78b387894149779083060a75eb`  
**Classification:** `PROOF-DEVELOPMENT / PROGRAMME-B9 / BLOCKED-FRONTIER / CORRECTED-ASSEMBLY / AC-RL-DEPENDENT`  
**Global five-support theorem:** not proved  
**Independent-review state:** not independently audited  
**Live branch continues:** yes; only later repair or AC-RL-returned proof packets may extend this frontier  
**Staging authorized:** dedicated Curator branch only  
**Default-branch movement:** not authorized

## 1. Intake objective

Synchronize the rolling corpus with the corrected final dependency frontier. This is not a theorem-completion handoff. It records exactly which outer reductions are closed, which six source arrows remain open, and which future theorem packages would suffice.

## 2. New closed outer reduction

The five-support strengthening for finite-active-edge bridgeless multigraphs is equivalent to the finite loopless bridgeless cubic case.

- loops may be inserted into two fixed indexed supports without changing cut parity;
- port-cycle collapse transports each of the five indexed supports and preserves exact edge multiplicity;
- disconnected components, parallel edges, high degree, and arbitrary ambient vertex carrier add no further five-support obstruction after the cubic case.

This reduction does not prove the cubic statement.

## 3. Exact open obligations

### BBD route

1. `AC-RL-BBD-GROUPOID-CLOSURE`;
2. `AC-RL-BBD-VARIATION-SLICE`.

### Corrected source-localisation route

3. `AC-RL-TYPE-T-SERIALISATION`;
4. `AC-RL-FLAT-POTENTIAL-INTERFACE`;
5. `AC-RL-COMMON-CUT-LOCALISATION`;
6. `AC-RL-TYPE-H-COMMON-WITNESS`.

The corresponding AC-RL returns are in research-workbench issue #8 comments `5019401145` and `5019455976`.

## 4. Minimal sufficient closure packages

Either package below would close the strengthening.

### Escape package

For every finite loopless bridgeless cubic graph, produce some nowhere-zero Fano flow and compatible root lift whose full dual maps to the five-coordinate half-cube.

### Decomposition package

For every persistent bad cubic state, produce a strictly smaller labelled separator/transfer object whose complete five-support profiles glue.

A mixed escape/decomposition theorem also suffices.

## 5. Required corpus status

- Programme A remains a complete paper-level CDC theorem spine.
- B1–B8 remain mature theorem/assurance checkpoints with their recorded corrections.
- B9 must remain `BLOCKED-FRONTIER`; it is neither complete nor abandoned.
- finite certificates close none of the six open arrows;
- the invalid universal orthogonal hierarchy, unconditional BBD common-origin synthesis, and nontrivial fixed-terminal defect forest must not re-enter the active theorem layer.

## 6. Curator success test

1. The immutable B9 checkpoint remains fixed and recoverable.
2. Complete CDC and open five-support strengthening remain distinct.
3. The cubic outer reduction is integrated without implying the cubic theorem.
4. All six exact AC-RL obligations remain visible.
5. No finite census is promoted to a global proof.
6. No Lean, manuscript, release, DOI, publication, or `main` movement is implied.

Staging is authorized; canonical movement is not.