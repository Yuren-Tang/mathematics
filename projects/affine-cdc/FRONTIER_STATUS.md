# AffineCDC frontier status

## 1. Two independent open frontiers

AffineCDC currently has two distinct open strengthening problems.

1. **Five-support frontier:** compress compatible covers to five indexed supports.
2. **Orientation frontier:** choose an orientable compatible lift, first in a prescribed rank-three-flow fibre and, if necessary, after choosing the flow.

Neither frontier is a defect in the complete ordinary CDC theorem, and neither may be silently substituted for the other.

## 2. Closed orientation-obstruction layer

Closed at authorial proof level:

- retained partner/rotation data reconstruct the indexed cycle-face surface;
- $\omega(g)\in C^1(G)/\operatorname{Cut}(G)$ is the obstruction of one fixed lift;
- $w(g^k)=w(g)+\Lambda_f(k)$ under transported local orientations;
- $\Omega_f\in C^1(G)/(\operatorname{Cut}(G)+\mathcal B_f)$ is the fixed-fibre obstruction;
- orientable labelled lifts are empty or one kernel torsor;
- orientable unlabelled Petrial words are empty or one coset under $\mathcal B_f\cap\operatorname{Cut}(G)$;
- the dual orientation-stress criterion is exact;
- the standard $K_4$ fibre contains projective-plane and sphere lifts;
- support-only collapse loses orientation witness data;
- enriched directed collapse transports an oriented CDC;
- loops may be reinserted in opposite dart directions under the stated convention.

These results are Curator-integrated but not independently audited or end-to-end Lean verified.

## 3. Exact orientation returns

### `AC-RL-OR-FIXED-FIBRE-VANISHING`

Determine whether

$$
\Omega_f=0
$$

for every nowhere-zero $\mathbf F_2^3$-flow on every finite bridgeless cubic multigraph, or construct an exact fixed-fibre counterexample.

The $K_4$ projective-plane lift is not such a counterexample because the same fixed fibre contains an orientable sphere lift.

### `AC-RL-OR-GRAPH-EXISTENCE`

If universal fixed-fibre vanishing fails, determine whether every finite bridgeless cubic multigraph admits some nowhere-zero rank-three flow $f$ with

$$
\Omega_f=0.
$$

Either the stronger fixed-fibre theorem or this graph-level existence theorem supplies the missing input to the enriched outer route.

## 4. Exact orientation boundary

Not open:

- reconstruction from retained darts;
- the fixed-lift cut quotient;
- fixed-fibre linear classification;
- duality;
- $K_4$ nonautomaticity;
- orientation-preserving collapse under enriched data.

Open:

- universal vanishing in a prescribed fibre;
- existence of a suitable flow/fibre on every graph.

No horizontal monotonicity theorem is inferred from the fixed-fibre classification.

## 5. Controlling five-support correction

The five-support frontier no longer treats BBD simultaneous origin or a nontrivial defect-minimal forest as closed theorem blocks.

- simultaneous BBD origin requires `AC-RL-BBD-GROUPOID-CLOSURE`;
- a nontrivial defect forest requires `AC-RL-BBD-VARIATION-SLICE`.

## 6. Closed five-support layers in exact scope

Closed authorial layers include:

- witness and fixed-data formulations;
- full-dual/factorable target hierarchy;
- target links and eight-vertex factorable classification;
- vertical gauge/Petrial and connected-switch mechanics;
- three-cut and four-pole interfaces;
- cap forcing, pairing alignment, routing weights, and uniform-routing elimination;
- individual-loop holonomy and root-fibre section theory;
- Type H soluble zero-norm escape;
- DDD atom triality and unique bad route;
- rank-one impossibility, rank-two Tait escape, and full-rank curvature duality;
- finite-certificate assurance normalization.

## 7. Six exact five-support returns

### BBD correction

- `AC-RL-BBD-GROUPOID-CLOSURE`;
- `AC-RL-BBD-VARIATION-SLICE`.

### Localization and composition

- `AC-RL-TYPE-T-SERIALISATION`;
- `AC-RL-FLAT-POTENTIAL-INTERFACE`;
- `AC-RL-COMMON-CUT-LOCALISATION`;
- `AC-RL-TYPE-H-COMMON-WITNESS`.

## 8. Nonflat and flat branches

If full-rank curvature is nonzero, one terminal-colour edge set is a cut in all four scalar sheets and has odd terminal parity. Open: compare it with the original source four-pole and extract bounded, connected, composition-safe progress.

If curvature vanishes, an eight-state affine potential satisfies the exact edge law. Open: extract finite transfer semantics, a bounded interface, smaller separator, or replaceable repeated fibre.

## 9. Type T, Type H, and horizontal frontier

Type T requires serialisation or another strict source decomposition. Type H has a complete individual-loop soluble escape theorem, but the family-level obstructed branch still requires one coherent physical witness.

Open also remain:

- full-cap-profile theorem or first realizable counterprofile;
- composition/elimination of residual mismatch kernels;
- a horizontal theorem sending a closed bad-flow component to a good boundary edge or coherent decomposition certificate.

Any horizontal theorem affecting orientation must recompute $H_f^0$, $\mathcal B_f$, and $\Omega_f$ in the new flow fibre; OR1 proves no invariant transport across a change of $f$.

## 10. Certificate boundary

Finite tables close neither frontier. In particular:

- BBD monodromy counts do not prove groupoid closure;
- defect/Petersen tables do not define a valid variation slice;
- `7737` composite endpoints do not prove connected escape;
- small four-pole census does not prove the full-cap theorem;
- scalar-sheet cuts do not prove source localization;
- the $K_4$ pair proves per-lift nonautomaticity but not universal fixed-fibre failure or graph-level existence.

## 11. Global endpoints

Five supports require:

$$
\text{persistent vertically and horizontally bad data}
\Longrightarrow
\text{good escape or strict source progress}.
$$

Oriented AffineCDC requires:

$$
\text{bridgeless cubic graph}
\Longrightarrow
\exists f\text{ with }\Omega_f=0,
$$

or the stronger universal fixed-fibre vanishing theorem.

The candidate is ready for an independent audit of the closed OR1 theory while both global strengthening endpoints remain open.
