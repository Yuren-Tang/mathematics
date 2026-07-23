# Oriented inverse-dipole locks contain no odd pivot-closed subtrack

## Research Lead confluence hardening v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `f637d25c718c3c9dd5129b1db631faeca9d778fe`.

**Parents:**

- `ORIENTED_CHANNEL_LOCK_BOUNDARY_CALIBRATION_V1.md`;
- `FORCED_DDD_BACKBONE_BINARY_TRANSPORT_V1.md`;
- `PETERSEN_RESOLUTION_PARITY_V1.md`.

**Purpose:** close the double-lap ambiguity in the contextual-confluence argument. An odd Petersen cycle exchanges the resolution sheet after one lap, but an abstract two-sheeted cover would allow two laps to return. The physical oriented cap excludes the first odd lap as a pivot-closed subpath, so no double-lap recurrence is available.

**Status:** exact authorial strengthening of the odd-core exclusion. It does not depend on the full state returning after one lap; it excludes every odd pivot-closed segment inside an oriented lock.

---

## 1. Two distinct double covers

A DDD atom state is one Petersen edge

\[
F=\{s,t\},
\]

with two crossed root resolutions `s,t`.

Traversing one pivot-change state exchanges these two resolution demands. Therefore an abstract pivot path of length `m` has resolution holonomy

\[
\operatorname{Hol}_{\mathrm{res}}=m\pmod2.
\]

This defines the canonical bipartite double cover of the Petersen graph. An odd base cycle is not closed in one lap but its double traversal is closed in that abstract cover.

Separately, a crossed terminal matching has two oriented blocks. The original two cap vertices distinguish these blocks. This gives the physical route-orientation cover of the inverse-dipole lock.

The two covers agree on the forced-backbone transport character: every pivot change toggles the demanded crossed block.

---

## 2. Physical admissibility kernel

Fix the original cap matching and distinguish one of its two vertex blocks as positive.

Every repair channel in a blocked oriented lock:

1. contains the two marked reconnection edges in one component;
2. cuts open in the original cap order;
3. returns the distinguished positive block to itself.

Consequently every physical transport word `g` generated inside the lock belongs to the stabiliser of the oriented block:

\[
D\le\ker\nu,
\]

where `nu` is `kappa` or `kappa+chi` according to the selected crossed route.

Equivalently,

\[
\boxed{
\nu(g)=0
}
\]

for every pivot-closed physical transport segment in the oriented lock.

This is an admissibility restriction on the physical state graph, not a choice made only after completing a loop.

---

## 3. Odd pivot-closed segments are impossible

Let

\[
\gamma=s_0,F_1,s_1,\ldots,F_m,s_m
\]

be one forced-backbone segment contained in the oriented lock, and assume

\[
s_m=s_0.
\]

The resolution-parity theorem gives

\[
\nu(\gamma)=m\pmod2.
\]

The physical admissibility kernel gives

\[
\nu(\gamma)=0.
\]

Therefore

\[
\boxed{m\equiv0\pmod2.}
\]

### Theorem 3.1 — no odd pivot-closed subtrack

Every pivot-closed forced-backbone segment inside an oriented inverse-dipole lock has even length.

In particular, neither a simple Petersen `C5` nor a simple Petersen `C9` can occur as a completed subsegment of one physical token track.

---

## 4. Why a double lap does not evade the theorem

Consider the abstract double traversal of an odd base cycle.

After its first lap:

1. the pivot has returned to its initial value;
2. the demanded crossed-route block has changed to its antipode.

Thus the first lap is already an odd pivot-closed segment. Theorem 3.1 excludes it from the physical oriented-lock state graph.

It is not legitimate to retain the antipodal endpoint as a second admissible state and continue around the cycle once more. The cap supplies one distinguished physical block, and the antipodal endpoint violates that fixed boundary orientation.

### Corollary 4.1 — no odd double-lap recurrence

A recurrent full-state token cycle cannot project to two or any even number of traversals of one odd Petersen cycle. The first odd traversal is already inadmissible.

---

## 5. Correct cycle extraction in the sink argument

Let a persistent token walk in an oriented lock repeat a pivot. Choose a shortest positive-length pivot-closed subpath. After deleting immediate backtracks, its projection is a simple Petersen cycle.

By Theorem 3.1 its length is even. Since the simple Petersen cycle lengths are

\[
5,6,8,9,
\]

it must be

\[
\boxed{C_6\text{ or }C_8.}
\]

No assumption that the complete enriched state already returned at the two endpoints is needed. Pivot closure plus physical cap orientation is enough.

This is the exact form required by the no-sink-SCC theorem.

---

## 6. Interface with even-core descent

The remaining recurrent cores are:

- primitive `C6`, handled by the relative root NNI to the canonical star and equal-face cancellation;
- `C8`, reduced to two seam-compatible `C6` cells.

Thus every recurrent token track in the physical oriented state graph has a strict cancellation exit.

---

## 7. PDL obligations

PDL should verify explicitly:

1. the identification of the resolution flip character with the oriented crossed-block character on forced-backbone transitions;
2. that the cap distinguishes one terminal block throughout every descendant context;
3. that every physical transport word lies in the corresponding orientation kernel;
4. that a pivot-closed subsegment is itself a physical transport word to which the kernel condition applies;
5. that shortest repeated-pivot reduction preserves the forced-backbone and fixed-route hypotheses.

These points, not the abstract double-cover parity alone, exclude odd recurrence.

---

## 8. Trust boundary

### Exact authorial claim

- every physical pivot-closed segment in an oriented lock has even length;
- odd `C5/C9` subtracks are excluded before full-state return is considered;
- double traversal of an odd core is not an admissible recurrence.

### Not added

- independent verification of the orientation calibration;
- even-core source movie verification;
- complete contextual confluence, global five-CDC acceptance, Lean verification, manuscript, release, or publication status.
