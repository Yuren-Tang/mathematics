# Minimal laminar interval surgery: boundary signatures and descent invariant

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Parent:** `projects/affine-cdc/research/LOCKED_SCALAR_COMPONENT_ROUTING_V1.md`  
**Status:** exact bounded-interface reduction for one minimal laminar interval; admissible replacement remains open.  
**Not implied:** canonical acceptance, independent audit, Lean verification, manuscript readiness, or the global five-support theorem.

---

## 1. Minimal laminar interval

Let

\[
A=P_{12}\sqcup P_{34}\sqcup C
\]

be one locked scalar challenge sheet, where `P12,P34` are the two terminal paths and `C` is a union of closed components.

Let

\[
Z_i\subseteq H_\delta
\]

be one connected pair-preserving component whose attachment intervals on `P12` and `P34` are minimal in the laminar containment order.

After suppressing excursions disjoint from `P12 cup P34`, let the first and last attachment points on the two paths be

\[
a_1,a_2\in P_{12},
\qquad
b_1,b_2\in P_{34}.
\]

Let `R_i` be the source subgraph bounded by the two path subsegments

\[
P_{12}[a_1,a_2],
\qquad
P_{34}[b_1,b_2]
\]

and the part of `Zi` connecting their attachment sets.

Minimality means that no other active pair-preserving component has all its attachments strictly inside both path intervals.

---

## 2. Boundary signature

The interaction of `Ri` with the remainder of the locked route system is carried by at most four ordered ports:

\[
a_1,a_2,b_1,b_2.
\]

Any additional edge leaving `Ri` is a side attachment from the original root-valued source graph.

### Definition 2.1 — external side signature

Let

\[
\Sigma(R_i)
\]

be the multiset of external side-root labels together with their incident port interval.

The binary locked-route interface is the terminal matching

\[
M_i=a_1a_2\mid b_1b_2.
\]

### Theorem 2.2 — four-port reduction

At the binary scalar level, toggling `Zi` changes only the internal pairing data inside `Ri`; the remainder of the source graph sees the same four ordered ports and the same scalar boundary.

Hence every minimal laminar interval is a four-port replacement problem, regardless of its internal size.

### Proof

`Zi` has zero scalar boundary. Outside the two minimal attachment intervals, `A` and `A triangle Zi` coincide. Pair preservation keeps the same pairing of the four external continuations. All changes are supported in `Ri`.

---

## 3. Side-attachment alternatives

The exact binary reduction leaves the side-root signature `Sigma(Ri)` as the only unbounded datum.

There are three structural cases.

### Case I — separated signature

All external side attachments of `Ri` lie on components contained in `Ri` or meet the rest of the graph through one side of the four-port interface.

Then `Ri` is a candidate for gauge transfer, replacement, or contraction.

### Case II — split signature

The external attachments divide into two classes separated by a cut of size at most four through the ports.

Then the cut is a smaller cyclic separator or a genuine four-pole interface with matching `Mi`.

### Case III — crossing signature

Some external component connects attachment regions in an order incompatible with the laminar order of `a1,a2,b1,b2`.

Then this external component supplies an interlacing route. At the binary level it produces a pair-changing toggle; in the root-valued lift it must give either a Kempe/profile escape or one of the known DDD/defect lift failures.

### Consequence 3.1

A support-minimal counterexample to interval surgery must lie in Case I or Case II. Case III is not a new irreducible obstruction.

---

## 4. Descent invariant

Define the interval complexity

\[
\mathcal C(R_i)
=
\bigl(
 |V(R_i)|,
 |\Sigma(R_i)|,
 \beta(R_i),
 \#\text{internal defect edges}
\bigr)
\]

with lexicographic order, where `beta` is cycle rank.

### Target 4.1 — replacement descent

Construct, in Case I, an admissible replacement with the same four-port root boundary and strictly smaller `C(Ri)`, unless `Ri` is already one of:

- a bounded DDD atom;
- a zero-equality unit;
- a single co-root defect edge with its two crossed resolutions;
- a finite four-pole kernel already covered by Type T/Type H analysis.

### Target 4.2 — separator descent

In Case II, cut along the split signature and replace the original interval by two smaller source instances. The sum of their interval complexities is strictly smaller than the original one in the multiset extension of the lexicographic order.

---

## 5. Why four ports are the correct ceiling

The earlier six-channel blocker theorem gives a maximal minimal certificate size of four. The present minimal-interval reduction independently produces four ordered route ports.

These are not yet proved to be the same four coordinates, but they are compositionally compatible candidates:

- channel side: four fundamental-cut coordinates of a spanning tree of `K2,3`;
- route side: four boundary ports of one minimal laminar interval.

### Target 5.1 — coordinate identification

Show that the four channel cut coordinates restrict on `Ri` to the four port-side incidence functions. If so, the path-tree orbit gives serial Type T, while failure of orientability returns to the DDD/Type H branch.

---

## 6. Strategic reduction

The weight-two branch is reduced to one bounded-interface theorem:

\[
\boxed{
\text{minimal laminar interval}
\Longrightarrow
\begin{cases}
\text{admissible smaller replacement},\\
\text{four-pole/separator split},\\
\text{bounded DDD/defect atom},\\
\text{profile escape}.
\end{cases}
}
\]

The internal size of the interval no longer affects its external binary route interface; only the side-root signature prevents immediate contraction.

Thus the next mathematical problem is to control `Sigma(Ri)` by root-fibre and co-root-strip methods, not to enlarge the routing state space.

---

## 7. Trust boundary

### Exact here

- a minimal laminar component changes the locked route only inside two path intervals;
- its binary external interface has at most four ordered ports;
- crossing external attachments return to the pair-changing/escape branch;
- every irreducible interval-surgery obstruction must be separated or four-port;
- a lexicographic interval complexity suitable for a strict-descent theorem.

### Still open

- existence of a root-admissible replacement in the separated case;
- proof that the split signature gives a composition-safe cyclic separator;
- identification of channel cut coordinates with the four route ports;
- control of arbitrary side-root attachments by the enriched co-root transducer;
- Type-T strict descent, regional torsor Stokes, horizontal/global induction, and the global five-support theorem.
