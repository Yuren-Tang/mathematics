# AC-PD-5CDC EQ-RETURN 2 — partial root-flow extension and `R_5`-connectedness target

**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**State:** `RESEARCH TARGET / PRECEDENT-ALIGNED / NOT PROVED`.

---

## 1. Why the marked-weld problem is a partial-flow problem

Cutting the two reconnecting edges after an equal-face cancellation gives four marked semiedges with boundary word

\[
W=(z,z,w,w),
\qquad z\ne w,
\qquad z+w\in R_5.
\]

The return theorem asks for an `R_5`-valued flow on the lower-order relative context extending this admissible prescribed boundary, up to one global support permutation.

This is not merely ordinary root-flow existence. It is a partial root-flow extension problem.

---

## 2. A root-orbit analogue of group connectivity

Let

\[
E_5=\mathbf F_2^5,
\qquad
R_5=\{x\in E_5:\operatorname{wt}(x)=2\}.
\]

### Definition 2.1 — relative `R_5`-extendability

A finite cubic multipole `P` with prescribed semiedge word `b` is `R_5`-extendable if there exists a Kirchhoff flow

\[
\lambda:E(P)\cup\partial P\to R_5
\]

whose restriction to the ordered semiedges is `b`.

### Definition 2.2 — orbit-relative extendability

If only the global `S_5` orbit of `b` is prescribed, `P` is orbit-relatively `R_5`-extendable when it extends some `\pi b`, `\pi\in S_5`.

The marked weld requires the orbit-relative extension of one ordered adjacent-pair word `(z,z,w,w)`.

---

## 3. Exact relation with the prime two-edge target

Let `H` be the lower-order connected cubic graph and let `e,f` be the two reconnecting edges. Cut their interiors to obtain a four-pole `P_(e,f)`.

Then the following are equivalent.

1. `H` has a root flow with `lambda(e),lambda(f)` distinct and intersecting.
2. `P_(e,f)` extends an ordered word `(z,z,w,w)` with `z,w` distinct and intersecting.
3. `P_(e,f)` is orbit-relatively `R_5`-extendable for the marked-weld orbit.

Thus Repair C is exactly the two-mark instance of relative `R_5`-extendability.

---

## 4. Closest established precedent

### Partial nowhere-zero `4`-flow extension

Hong-Jian Lai, *Extending a partial nowhere-zero 4-flow*, Journal of Graph Theory 30 (1999), 277--288, DOI

`10.1002/(SICI)1097-0118(199904)30:4<277::AID-JGT3>3.0.CO;2-D`.

The theorem has the structurally relevant form:

- prescribe a partial nowhere-zero group flow on an edge cut;
- under strong spanning-tree/collapsibility hypotheses, extend it to the whole graph;
- otherwise contract to a finite list of exceptional configurations.

This strongly resembles the required prime/bounded dichotomy.

### Flow-critical and prescribed-local-flow work

A. S. Árnadóttir, Z. Dvořák, B. Lidický, B. Moore, E. Smith-Roberge and R. Šámal, *Flow-critical graphs*, arXiv:2502.01451, revised 2026.

This work extends prescribed local nowhere-zero `3`-flow results under high connectivity and studies minimal obstructions to partial-flow extension.

### Group connectivity

Jaeger--Linial--Payan--Tarsi group connectivity and its later developments establish choosability-style extension results for unrestricted nonzero values in sufficiently large abelian groups.

---

## 5. Why these theorems cannot be imported

The present codomain restriction is nonlinear:

\[
\lambda(e)\in R_5,
\]

not merely

\[
\lambda(e)\in E_5\setminus\{0\}.
\]

A general `E_5` group flow may use weight-one, weight-three, weight-four or weight-five values. Group connectivity therefore does not imply root-orbit connectivity.

Likewise an ordinary nowhere-zero `4`-flow theorem concerns the three nonzero elements of `\mathbf F_2^2`, all of which form one admissible orbit; in `E_5`, the ten roots are only one subset of the thirty-one nonzero elements.

The external results supply proof architecture and exception philosophy, not the missing theorem.

---

## 6. Proposed prime theorem

### Target 6.1 — prime partial root-flow extension

Let `P` be the four-pole obtained by cutting two distinguished edges of a connected root-soluble cubic graph in the prime branch after accepted bounded and small-cut reductions. Then `P` is orbit-relatively `R_5`-extendable for the adjacent-pair word, or the marked instance exposes an accepted separator/bounded contraction.

Equivalently, some root flow gives the two distinguished edges distinct intersecting values.

The finite scout shows that the bounded exceptions are necessary and that the target holds for all edge pairs in Petersen, Möbius--Kantor, Heawood, Pappus and Desargues.

---

## 7. Candidate proof architecture

A precedent-aligned proof should have three layers.

### Layer A — root-Kempe separation

Starting from any root flow:

- if a relevant support-pair cycle separates the marked edges, switch it and reach the adjacent orbit;
- otherwise obtain a two-edge full-channel lock.

### Layer B — contractible/prime dichotomy

Show that a full-channel lock either:

- contracts to a finite bounded rooted configuration;
- exposes a small edge cut or transition sum;
- or induces an `R_5`-connected prime core.

### Layer C — prime extension

On the prime core, prove one of:

- a root-valued cycle correction separates the marks;
- an octahedral antipodal correction reaches a separating Kempe state;
- the rigid connected-cycle root geometry forces a bounded carrier or separator.

This is the root-orbit analogue of partial group-flow extension.

---

## 8. Relation to `MWR`

If Target 6.1 is proved at every lower target order, then after a canonical cancellation:

1. solve the lower-order graph by the inductive theorem;
2. apply prime partial root-flow extension to the two marked reconnecting edges;
3. obtain the adjacent root orbit, or an accepted bounded/separator exit;
4. globally relabel to the stored weld word;
5. reinsert the equal-face pair root-valuedly.

This closes cancellation re-entry without extruding the exact edge names through the whole prior history.

Thus Target 6.1 is potentially narrower than full arbitrary-frozen-boundary `MWR`.

---

## 9. Trust boundary

### Exact here

- equivalence between marked weld and two-edge adjacent-orbit extension;
- distinction between `R_5`-extendability and ordinary group connectivity;
- relevance and nonapplicability of partial-flow extension precedents;
- precise prime theorem and proof architecture.

### Not proved

- prime partial root-flow extension;
- finite exceptional-contraction classification;
- marked-weld return;
- global contextual return or five-CDC.