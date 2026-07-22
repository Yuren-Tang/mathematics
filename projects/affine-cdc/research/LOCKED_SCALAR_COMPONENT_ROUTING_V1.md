# Locked scalar components and the route-change/serial dichotomy

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Parent:** `projects/affine-cdc/research/PHYSICAL_TRANSLATION_CELL_ANALYSIS_V1.md`  
**Status:** exact binary component algebra and a sharpened graph-theoretic frontier; serial localisation remains open.  
**Not implied:** canonical acceptance, independent audit, Lean verification, manuscript readiness, or the global five-support theorem.

---

## 1. Two locked challenge sheets

Fix

\[
\lambda\in\Lambda_g,
\qquad
0\ne\delta\in g^\perp.
\]

Put

\[
A=H_\lambda,
\qquad
B=H_{\lambda+\delta},
\qquad
Z=H_\delta.
\]

Then

\[
\boxed{B=A\triangle Z}
\]

and `Z` is a closed binary even subgraph.

Both `A` and `B` have the same four terminal boundary and, in the locked regime, realise the same terminal matching.

---

## 2. Componentwise toggling

Write

\[
Z=Z_1\sqcup\cdots\sqcup Z_m
\]

as the disjoint union of its connected even components.

For every subset

\[
I\subseteq\{1,\ldots,m\},
\]

put

\[
A_I
=
A\triangle\bigtriangleup_{i\in I}Z_i.
\]

### Theorem 2.1 — boundary preservation

Every `A_I` has the same terminal boundary as `A`:

\[
\boxed{\partial A_I=\partial A.}
\]

### Proof

Each `Zi` is even and has zero terminal boundary, so symmetric difference with `Zi` does not change the boundary.

### Consequence 2.2

The complete interval between the two locked challenge sheets `A` and `B` is a Boolean cube of component toggles. Hence any failure of a component toggle to give an admissible locked route is not a boundary obstruction; it is purely a connectivity/routing obstruction.

---

## 3. Pair-changing components

Let the locked terminal matching be

\[
M=12\mid34.
\]

A component `Zi` is **pair-changing relative to A** if the terminal-path decomposition of

\[
A\triangle Z_i
\]

realises a matching different from `M`.

### Proposition 3.1 — immediate profile escape criterion

If some component `Zi` is pair-changing and the corresponding scalar toggle is realised by an admissible Kempe switch in the root cover, then the locked profile is not closed: the switch gives a boundary-profile escape.

### Trust boundary

The binary statement is exact. Root-admissibility of the physical switch is the remaining lift condition; failure of that lift belongs to the previously classified empty-fibre, DDD, or defect branches.

---

## 4. Pair-preserving components

Assume every component `Zi` is pair-preserving:

\[
A\triangle Z_i
\]

still realises `12|34` for every `i`.

The same holds for `B`, since `B=A triangle Z`.

### Theorem 4.1 — no single-component crossing of both locked pairs

Let `P12,P34` be the two terminal path components of `A`. If a connected even component `Zi` meets both `P12` and `P34` in an alternating pattern that exchanges their continuations, then `Zi` is pair-changing.

Therefore, under pair preservation, every component has one of the following coarse behaviours:

1. it is disjoint from one terminal path;
2. it meets both terminal paths but preserves their continuation pairing;
3. it attaches through closed excursions whose entry/exit order is noncrossing on each path.

### Proof sketch

At every intersection with `A`, toggling by `Zi` exchanges which two local half-edges continue in the symmetric difference. If the exchanges interlace between `P12` and `P34`, the two original terminal pairs reconnect crosswise. Pair preservation excludes this interlacing. The detailed source-graph version must account for repeated visits and side attachments; the binary reconnection statement is local and exact.

---

## 5. Alternation order

Orient `P12` and `P34` from their first to second terminal. Record the intersection points of one component `Zi` with each path in path order.

Because `Zi` is even, its incidences with the union

\[
P12\cup P34
\]

occur in pairs after suppression of internal excursions.

### Definition 5.1 — interlacing

Two attachment pairs interlace if their endpoints occur in opposite orders on `P12` and `P34`.

### Proposition 5.2 — interlacing forces route change

An interlacing pair of `Zi`-connections between `P12` and `P34` reconnects the four terminal ends according to a crossed matching after toggling.

Hence every pair-preserving component has noninterlacing attachment order.

### Consequence 5.3 — laminarity target

For pair-preserving components, the attachment intervals on the two locked paths define the same partial order. If two components violate laminarity, one obtains an interlacing pair and hence a profile escape.

Thus an irreducible all-pair-preserving family must be laminar.

---

## 6. Serial decomposition target

A laminar family of component attachment intervals admits a rooted containment forest. A minimal interval in this forest has no other active component strictly inside it.

The expected source theorem is:

### Target 6.1 — minimal interval surgery

For a minimal pair-preserving component interval, prove one of:

1. its bounded interior can be switched or gauge-transferred;
2. its two boundary sections form a smaller cyclic separator;
3. its interior is a zero-equality/co-root defect unit;
4. its boundary is a four-pole with the matching selected by `delta`.

Removing or contracting the minimal interval then gives strict descent in the laminar forest.

### Target 6.2 — Type-T identification

The total order along a maximal laminar chain should be the source-graph realisation of the path-tree/Type-T serial coordinate. The exact finite matching selected by `delta` fixes which two terminal strands form the serial pair.

---

## 7. Strategic dichotomy

The weight-two physical branch is reduced to:

\[
\boxed{
\text{some }Z_i\text{ pair-changing}
\Rightarrow
\text{profile/Kempe escape or known lift defect},
}
\]

or

\[
\boxed{
\text{all }Z_i\text{ pair-preserving}
\Rightarrow
\text{noninterlacing laminar family}
\Rightarrow
\text{serial minimal-interval target}.
}
\]

The remaining hard content is no longer algebraic triality. It is the composition-safe treatment of one minimal laminar interval.

---

## 8. Trust boundary

### Exact here

- componentwise Boolean-cube decomposition between parallel challenge sheets;
- boundary preservation under every component toggle;
- binary pair-change criterion by crossed reconnection;
- interlacing attachments force a crossed terminal matching;
- pair-preserving irreducibility requires noninterlacing/laminar attachment order at the binary route level.

### Still open

- root-admissible lifting of an individual component toggle;
- treatment of repeated visits and side attachments in the full source graph;
- minimal laminar interval surgery;
- extraction of a smaller separator/four-pole/defect unit;
- full Type-T strict descent, regional torsor Stokes, and global five-support closure.
