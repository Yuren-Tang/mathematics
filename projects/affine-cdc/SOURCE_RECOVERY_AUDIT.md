# AffineCDC source-recovery and source-fidelity audit

## 1. Exact source lineage

The public five-support checkpoint is

`dad218dd18ed05d1b7cb730c2dc2431b4db5ec9c`.

The source interval from `main@749e0579581fcc838685138b3582f4de306b8e72` contains exactly eighty-two commits and seventy-eight packet files under `projects/affine-cdc/research/`. Every packet body remains recoverable through ordinary Git history.

## 2. Recovery completeness versus classification fidelity

Two distinct claims are controlled separately.

1. **Git/body recovery completeness:** all seventy-eight packet files, their exact paths, blobs, and chronology are recoverable.
2. **Source-classification fidelity:** the packet-to-theorem attribution must match the actual body of each packet.

Audit B found that the fixed unified candidate satisfied the first claim but not the second for the orthogonal-root packet. The present replacement corrects that migration defect.

## 3. Corrected packet placement

The packet

`FIVE_CDC_UNIVERSAL_ORTHOGONAL_ROOT_LIFT_V1.md`

at blob `2043ada9d28789ecc5f4f0028e62133f37835bc1` is a theorem-level fixed-dimensional source for $H_8$, the Hamming kernel and moment map, $O^+(6,2)$, twenty-eight roots, rank-three compatible lifts, and five-coordinate $O^-(4,2)$ slices. It is one of the thirty-nine controlling theorem/mechanism packets.

It contains no arbitrary-rank $\Gamma\oplus\Gamma^*$ model, no $d_h(a)=([a],\operatorname{ev}_a)$ formula, and no universal $O^+(2r,2)$ tower.

## 4. Separate source-unreconstructed proposition

No earlier exact committed source was recovered for the arbitrary-rank tower. Its classification is

`SOURCE-UNRECONSTRUCTED / INFERRED-EXTRAPOLATION OR UNCOMMITTED DRAFT / MATHEMATICALLY REFUTED BY B2.3`.

It is not one of the seventy-eight packets. The first recoverable committed text displaying it as an earlier theorem is the original PDL B2.3 correction layer; that does not retroactively place it in the historical packet population.

The mathematical correction remains self-contained:

- $\dim V\ge q-2$;
- deleted permutation module of dimension $q-2$;
- impossibility of a $2r$ complete-root model for $r\ge4$;
- rank-three exceptionality.

## 5. Exact packet accounting

After packet-by-packet placement, the classes are

$$
39+10+18+10+1=78.
$$

The extrapolation is outside the equation. The alternative partitions that counted the named packet as a false-theorem packet are superseded.

## 6. Recovery procedures

Recover one source body:

```text
git show dad218dd18ed05d1b7cb730c2dc2431b4db5ec9c:projects/affine-cdc/research/FILE
```

Restore one packet into a worktree without rewriting history:

```text
git restore --source=dad218dd18ed05d1b7cb730c2dc2431b4db5ec9c -- projects/affine-cdc/research/FILE
```

Inspect the complete source surface:

```text
git ls-tree -r --name-only dad218dd18ed05d1b7cb730c2dc2431b4db5ec9c projects/affine-cdc/research
```

Recover chronology:

```text
git log --reverse -- projects/affine-cdc/research
```

## 7. No-loss criteria

A packet is retired only after its exact source is known, its current role is named, independent proof/certificate/correction value is preserved, assurance is not silently upgraded, and its body remains recoverable. All seventy-eight packets satisfy these criteria under the corrected classification.

The non-packet extrapolation is handled honestly as an unreconstructed proposition rather than being assigned to an unrelated source packet.

## 8. Scope and assurance conclusion

The active tree may omit the seventy-eight packet bodies without source or priority loss, subject to the corrected provenance ledgers. This source-fidelity correction preserves Programme A, B1, B3–B8, all six frontier obligations, B9 exclusion, and the open global five-support theorem.

The corrected candidate must undergo the separately bounded B2/B8 source-fidelity re-audit required by AC-DIR. No canonical movement, independent acceptance, Lean, manuscript, publication, release, arXiv, DOI, or tag status follows from this audit.