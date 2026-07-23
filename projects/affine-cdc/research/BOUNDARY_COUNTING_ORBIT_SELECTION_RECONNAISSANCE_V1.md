# Boundary-counting orbit selection — reconnaissance and scope boundary

## Research Lead exploratory note v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `0f7922f7169b0e6c4ce3822e093d82ce9e6b41ff`.

**Purpose:** record the first exploration of Target O from `SINGLE_DEFECT_DIRECT_AUGMENTATION_BOUNDARY_V1.md`: can one avoid contextual confluence by proving that the root-flow space of a smaller cross closure necessarily contains an extendable boundary orbit?

**Status:** noncontrolling reconnaissance only. No exhaustive certificate, reproducible finite corpus, universal identity, or theorem is claimed here.

---

## 1. The proposed counting shortcut

For an ordered four-pole `P`, let

\[
Z_s(P)
\]

be the number of root-valued flows whose support-unordered boundary state is

\[
s\in\mathcal S,
\qquad |\mathcal S|=10.
\]

A strong orbit-selection theorem might follow from a universal identity or inequality among

\[
(Z_s(P))_{s\in\mathcal S}
\]

forcing positive mass in the original cap profile whenever one cross profile has positive mass.

Candidate mechanisms include:

1. a linear identity among the ten counts;
2. a quadratic Grassmann--Plücker or matchgate identity;
3. a positivity inequality;
4. a relation comparing the two cross terminal orderings;
5. a tensor identity before quotienting by support permutations.

Only the first two naked support-unordered possibilities were explored in the initial reconnaissance.

---

## 2. Early false linear patterns

Small and structurally biased examples produced apparent proportionalities among selected state counts. Those relations failed after including more varied simple bridgeless cubic instances and terminal orderings.

### Scope conclusion 2.1

No universal linear relation on the naked ten-component count vector was obtained.

The early relations must be treated as sample artefacts, not conjectures or finite certificates.

No statement about the actual linear span is asserted without a committed reproducible computation.

---

## 3. Low-degree quadratic reconnaissance

For restricted samples with one fixed terminal presentation, degree-two monomials in the ten counts also exhibited apparent dependencies reminiscent of Pluecker/matchgate relations.

Those dependencies did not persist after enlarging the sample family and varying terminal order.

### Scope conclusion 3.1

No credible universal quadratic identity in the ten support-unordered counts survived the exploratory tests.

This does **not** prove that no such identity exists. In particular:

- the sample was not an exhaustive set of four-poles;
- no exact full-rank certificate was committed;
- support-unordered counts discard physical route information;
- terminal reordering changes which tensor contraction is being observed;
- signed or oriented counts were not classified.

---

## 4. Why naked counts are structurally too coarse

The current one-cross proof distinguishes data invisible to the ten numbers `Z_s(P)`:

1. which physical Kempe component realizes one route;
2. the cyclic endpoint order of that component;
3. the distinguished cap block;
4. support-label transport along root Pachner histories;
5. side-root attachments at a co-root token;
6. orientation character on a pivot-closed subtrack.

Two four-poles may have the same support-unordered boundary count vector while differing in these labelled route and projectivity data.

Therefore a successful Target O theorem is more likely to use an enriched boundary object.

---

## 5. Better orbit-selection objects

### 5.1 Labelled boundary tensor

Count flows by the full ordered five-support terminal trace rather than by its ten-state orbit.

This retains support permutations and may admit representation-theoretic identities under `S_5`.

### 5.2 Route-refined tensor

For every full complementary support-pair challenge, retain which terminal matching is realised and, where needed, its oriented block.

This is the minimum enrichment visible to the current fixed-route theorem.

### 5.3 Two-cross transfer matrix

Rather than count the states of one four-pole alone, form the matrix whose rows and columns are labelled states on the two cross closures. A positivity or rank theorem might force one cap-compatible entry.

### 5.4 Signed projectivity partition function

Weight a root flow by the orientation/projectivity character of its induced coloured triangle pseudocomplex. Cancellation between odd sectors may expose an even extendable contribution.

No such invariant has yet been defined or proved composition-safe.

---

## 6. Exact current conclusion

The exploration does not support the shortcut

\[
\text{ten naked counts}
\Longrightarrow
\text{universal linear or elementary quadratic orbit selection}.
\]

It also does not refute the broader Target O.

The correct frontier is:

\[
\boxed{
\text{any plausible counting bypass must retain labelled route/projectivity data}.}
\]

Until an enriched tensor theorem is formulated and proved, finite-condensation contextual return remains controlling.

---

## 7. Requirements before promotion

No counting statement should enter the proof spine until there is:

1. an exact definition of the enriched tensor;
2. a reproducible enumeration program or human derivation;
3. a complete finite certificate for every claimed identity;
4. proof of covariance under support and terminal permutations;
5. proof that the identity implies an extendable cross-flow orbit;
6. compatibility with multigraph coincidences and the ordered cap context.

---

## 8. Assurance boundary

### Recorded safely

- small-sample naked linear patterns were unstable;
- restricted quadratic patterns were also unstable under broader presentations;
- support-unordered counts omit data used essentially by the current proof;
- enriched labelled/route tensors remain a legitimate future research direction.

### Not claimed

- a universal no-go theorem for all counting methods;
- full linear or quadratic rank of the set of realizable count vectors;
- a committed computational certificate;
- failure of signed, oriented, representation-theoretic, or two-cross identities;
- PDL acceptance, Lean verification, manuscript integration, release, peer review, publication, or established truth of five-CDC.
