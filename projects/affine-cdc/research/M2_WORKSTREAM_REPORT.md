# M2 workstream report — Binary Eight-Flow audit

**Conversation / worker:** AffineCDC — M2 Binary Eight-Flow Audit  
**Direct supervisor:** AffineCDC — Director  
**Repository:** `Yuren-Tang/mathematics`  
**Owned branch:** `research/affine-cdc-binary-eight-flow-v1`  
**Base SHA:** `749e0579581fcc838685138b3582f4de306b8e72`  
**Lifecycle result:** bounded unit closed at a necessary convention correction

## 1. Deliverables

Created:

- `projects/affine-cdc/research/BINARY_EIGHT_FLOW_AUDIT_V1.md`
- `projects/affine-cdc/research/M2_WORKSTREAM_REPORT.md`

No canonical file, M1 file, Lean file, public Statement, or engineering architecture was modified.

## 2. Audit result

The proposed classical route is valid for the graph constructed by M1:

\[
\text{finite loopless bridgeless multigraph}
\to
\text{integer 6-flow}
\to
\text{integer 8-flow}
\to
\mathbf F_2^3\text{-flow}.
\]

The exact reductions are:

1. apply Seymour independently to each edge-bearing connected component;
2. keep the same integer circulation, since \(0<|\varphi(e)|<6\) implies \(0<|\varphi(e)|<8\);
3. apply Tutte's existence theorem for the arbitrary abelian group \((\mathbb Z/2\mathbb Z)^3\) of order eight;
4. forget orientation because \(-a=a\) in characteristic two and the graph is loopless.

Parallel edges, including M1's two-edge fibre cycles, are supported by the audited source convention. Connectedness is not needed in the project interface.

## 3. Decisive correction

M1 Corollary 4.3 must be restricted to **loopless** multigraphs when its conclusion is read as `Port.NowhereZeroFlow`.

A standard oriented group flow cancels a loop as \(f(e)-f(e)=0\). The AffineCDC port sums over the edge set `incidenceSet v`, where a loop occurs once and contributes \(f(e)\). Hence the one-vertex one-loop graph is bridgeless in the standard cut-edge sense but admits no nowhere-zero port flow.

This is a genuine convention counterexample, not an editorial preference.

## 4. Further wording correction

M1 External Theorem 4.2 should separate:

- existence equivalence between integer \(k\)-flows and flows over any finite abelian group of order \(k\);
- equality of the numbers of group flows for equal-order groups.

The counting theorem is not required and is not an equality with the number of bounded integer flows.

## 5. Verdicts on M1

- **Theorem 1.1:** correct as written, using the corrected classical interface.
- **External Theorem 4.1:** correct after connectedness, loop, and parallel-edge conventions are stated explicitly.
- **External Theorem 4.2:** sufficient but requires the existence/counting split.
- **Corollary 4.3:** correct after adding “loopless, parallel edges allowed, not necessarily connected”; false under a loop-allowing reading of the current port convention.

## 6. Recommended project interface

Expose one external theorem:

> Every loopless multigraph with finite active edge set and no singleton cut admits a nowhere-zero \(\mathbf F_2^3\)-valued edge function whose unoriented incidence sum is zero at every active vertex.

Do not expose integer flows, orientations, \(\mathbb Z/8\mathbb Z\), or flow counts to the affine core.

At the current finite-ambient Lean checkpoint, this should produce the already-defined `Port.NowhereZeroFlow`. Seymour's theorem, Tutte's theorem, and the oriented-to-unoriented adapter remain outside the formalized boundary.

## 7. Availability findings

- Current Mathlib's `Graph α β` supports loops and parallel edge objects and supplies the necessary multigraph substrate.
- No reusable graph-level nowhere-zero flow interface, Tutte theorem, or Seymour theorem was located in the inspected public Mathlib checkpoint.
- `Yuren-Tang/affine-cdc` already defines the correct consumer structure `Port.NowhereZeroFlow` and the cubic-flow CDC theorem, but not the bridgeless-to-flow producer.

## 8. Sources audited

Primary theorem sources used:

- P. D. Seymour, “Nowhere-zero 6-flows”, *J. Combin. Theory Ser. B* **30** (1981), 130–135.
- W. T. Tutte, “A contribution to the theory of chromatic polynomials”, *Canadian J. Math.* **6** (1954), 80–91.
- M. DeVos, E. Rollová, R. Šámal, “A new proof of Seymour's 6-flow theorem”, arXiv:1512.06214.
- M. DeVos, J. McDonald, K. Nurse, “Another proof of Seymour's 6-flow theorem”, arXiv:2302.08625.

The modern primary proofs make their loop, parallel-edge, orientation, and integer/modular conventions explicit and were used to pin down the interface.

## 9. Stop reason

The issue requested stopping at the first decisive audit closure. Closure is reached:

- the route is verified;
- a necessary correction is identified with an explicit counterexample;
- the weakest project interface is specified;
- the remaining formalization boundary is isolated.

No child workstream was started.

## 10. Higher possibility found

**Yes, but not pursued.** A generic oriented finite-abelian-group flow API plus a characteristic-two loopless adapter would be reusable and convention-safe. It belongs to a later formal-engineering workstream.
