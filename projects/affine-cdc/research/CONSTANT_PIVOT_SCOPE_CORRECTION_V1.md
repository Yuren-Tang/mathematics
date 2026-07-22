# Scope correction for the constant-pivot oriented root-section theorem

## Research correction v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `f5cf84469eced9ef03c4d7e6e5bf17b26697593e`  
**Corrected source:** `projects/affine-cdc/research/CONSTANT_PIVOT_ORIENTED_ROOT_SECTION_V1.md`.

---

## 1. Correction

The constant-pivot theorem is exact for the **DDD/co-root Petersen strip**:

\[
F_t=\{s,d_t\}
\]

with one fixed Petersen pivot `s`. It proves that the transported nonpivot endpoint gives the unique simultaneous root section preserving every emitted side-root label.

The concluding prose of `CONSTANT_PIVOT_ORIENTED_ROOT_SECTION_V1.md` overstates its scope where it presents the entire equality/DDD frontier as reduced to pivot-change DDD states.

The correct statement is:

\[
\boxed{
\text{DDD constant-pivot strips}
\longrightarrow
\text{root-valued rank-two sections};
}
\]

hence the residual **DDD** obstruction is supported on pivot-change states.

It does **not** by itself eliminate the zero/equality full-channel lock, whose quadratic fibre is

\[
\{0,r\}
\]

rather than a Petersen root/co-root state

\[
\{d,d+r\}.
\]

---

## 2. Correct current local frontier

After the exact results through the corrected source, the local frontier is:

1. **DDD branch:** pivot-change incidence and crossed-resolution composition only;
2. **equality branch:** the oriented six-channel `K_{2,3}` lock;
3. **global packaging:** a well-founded ordering of graph descent, cut gluing, and horizontal rescue.

The equality branch may later reduce to DDD or rank-two/Tait structure, but that requires a separate physical theorem.

---

## 3. Preserved theorem content

No correction is made to the following exact statements of the original dossier:

- `tau_z` fixes the constant pivot;
- `tau_z` transports the nonpivot endpoint;
- the nonpivot sheet is the unique root-admissible sheet;
- every constant-pivot DDD run has a unique root section;
- every side-root output is preserved;
- DDD pivot changes force opposite crossed resolutions.

Only the claimed coverage of the equality branch is withdrawn.

---

## 4. Trust boundary

This correction does not alter canonical status and does not claim the equality lock, DDD pivot-change composition, or the global five-support theorem.
