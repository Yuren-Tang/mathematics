# Scope correction: an open root strip requires root-normalized endpoint sides

## Research Lead correction-quarantine v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Corrects the global reading of:**

- `PETERSEN_OPEN_TRACK_ROOT_STRIP_REPLACEMENT_V1.md`.

**Retains exactly:**

- the `120/120` side-root intersection theorem;
- the canonical root star on every nonbacktracking open pivot-change cell;
- the relative `(0,2,2)` table;
- linear gluing along an open chain;
- root-valued rectangle replacement when both short endpoint sides are already root-normalized or accepted boundary cells.

**Correction:** an open co-root track may terminate at the unresolved original cap/full-channel boundary. At such an endpoint the short side of a regular neighbourhood is not yet a root-valued normalization cell. The two long sides remain root-valued and the interior canonical cells remain valid, but the rectangular replacement theorem cannot be applied while fixing an unresolved co-root endpoint pointwise. Thus the file does not by itself eliminate the final boundary-reaching arc in contextual inverse transfer.

**Status:** exact scope correction. The sole remaining global interface is now one co-root track with at least one endpoint on the original unresolved cap boundary.

---

## 1. Three endpoint types

Let `gamma` be one open nonbranching co-root track in a lifted Ptolemy comparison.

Its endpoints may lie at:

1. **root-normalized local cells:**
   a failed move has an alternative root NNI or root-valued inverse insertion;
2. **accepted exits:**
   route/profile change, bounded theta/direct terminal, or separator/category boundary;
3. **unresolved outer target:**
   the track reaches the original cap-context boundary while still carrying one co-root atom.

The first two types have root-valued or already discharged short sides. The third does not.

---

## 2. Exact retained strip theorem

### Theorem 2.1 — interior/normalized-endpoint strip

If both endpoints of an open co-root track are of Types 1--2, then the canonical-cell construction of `PETERSEN_OPEN_TRACK_ROOT_STRIP_REPLACEMENT_V1.md` gives a root-valued rectangular replacement fixing the complete labelled boundary.

The proof remains unchanged:

- consecutive side roots are distinct intersecting;
- every cell canonicalises to one star;
- adjacent cells share fixed turn corollas;
- the open chain has no cyclic holonomy;
- both endpoint sides are root-valued and fixed by the relative movies.

---

## 3. Why the unresolved outer endpoint is different

Suppose one endpoint lies on the original target context `C_0` and still carries a co-root edge `Q_i`.

A sufficiently small neighbourhood of the endpoint meets the outer comparison boundary in a local side whose central edge is non-root-valued. Although the two histories immediately adjacent to the track are root-valued away from that edge, the short side itself is not one of the root cross/star topologies of the `(z,z,w,w)` relative table.

Therefore the implication

\[
\text{interior canonical stars glue linearly}
\Longrightarrow
\text{the complete rectangle has root-valued boundary}
\]

fails at this endpoint unless an additional cap-boundary rootification theorem is supplied.

One may not simply freeze the co-root endpoint and call the resulting strip root-valued.

---

## 4. Remaining exact target

The final transfer obstruction is now:

### Target 4.1 — outer co-root endpoint discharge

Let one full-state co-root track reach the original oriented fixed-route cap context. Prove one of:

1. a horizontal support-pair component separates the marked edges and gives an immediate cap lift;
2. the endpoint route differs from the fixed cap route and gives profile escape;
3. the endpoint lies in a bounded direct/theta or separator branch;
4. the track can be continued through a new finite equality/DDD forward descent;
5. continuation returns to a previous complete endpoint state, in which case the resulting periodic track admits a source-level root/cancellation disposition with a strict global rank.

Items 1--4 are existing local/full-channel alternatives. Item 5 is the sole remaining well-foundedness issue.

---

## 5. Relation to closed-track erasure

`PTOLEMY_CLOSED_DEFECT_TRACK_ERASURE_V1.md` removes closed components lying in the interior of one fixed comparison diagram.

If an outer-reaching track is continued through another full-channel episode and later returns to the same complete endpoint state, identifying the repeated states converts its trajectory into a closed track on a history cylinder.

However, erasing that closed track as a two-dimensional root annulus does not automatically prove strict progress of the repeated outer endpoint state. A separate macro-rank or cap-profile consequence is still required.

Thus closed-track erasure controls monodromy but does not alone complete boundary endpoint discharge.

---

## 6. Correct impact on contextual transfer v4

`ROOT_NORMALIZED_CONTEXTUAL_TRANSFER_MASTER_V4.md` remains noncontrolling for two reasons:

1. its disjoint inverse-cancellation row requires the later borrowing dichotomy correction;
2. its fixed-order termination step assumes that all open discrepancy arcs are discharged, which is not yet proved for an unresolved outer endpoint.

A v5 master must explicitly consume Target 4.1 before restoring global R2.7 closure.

---

## 7. Assurance boundary

### Exact here

- classification of open-track endpoint types;
- preservation of the root-strip theorem for normalized/accepted endpoints;
- identification of the unresolved cap endpoint as a genuinely different boundary condition;
- isolation of the remaining periodic outer-endpoint well-foundedness problem.

### Not claimed

- failure of the open-strip local construction;
- impossibility of outer endpoint discharge;
- repaired contextual transfer;
- one-cross cap restoration or global five-support closure;
- PDL reconstruction, independent audit, Lean verification, manuscript integration, release, arXiv, DOI, peer review, or publication.
