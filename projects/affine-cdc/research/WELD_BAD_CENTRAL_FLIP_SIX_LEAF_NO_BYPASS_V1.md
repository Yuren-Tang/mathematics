# A bad central weld flip has no adjacent root-valued six-leaf bypass

## Research Lead finite local obstruction dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `ac36f924c88fd03dad7ab7f5a2ae57622c708aeb`.

**Parents:**

- `WELD_RELATION_FIRST_EXIT_V1.md`;
- `WELD_MARK_EQUAL_FACE_OVERLAP_V1.md`;
- `SIX_LEAF_NNI_ROOT_EXCHANGE_V1.md`;
- `FIVE_LEAF_PACHNER_PENTAGON_ROOT_INTERVAL_V1.md`.

**Status:** exact negative local theorem with a reproducible Wolfram certificate. When one coordinate of a weld-admissible pair undergoes its unique bad central Pachner flip, the resulting inverse-weld topology has one co-root central edge. For the complete six-root boundary of this overlap, neither orientation of the bad topology has any root-valued NNI neighbour. The root-valued sector is connected, but lies at NNI distance two from the bad topology and every shortest path enters a non-root topology at the first step. Therefore the first bad central weld exit is a genuine singular atom. It cannot be removed by one canonical root-preserving NNI or by the full-root branch of the five-leaf pentagon theorem.

---

## 1. Standard coordinates

Let the current weld-admissible pair be

\[
\boxed{
p=ab,
\qquad
q=ac,}
\]

where `a,b,c` are distinct. Let

\[
\{d,e\}=[5]\setminus\{a,b,c\}.
\]

The unique bad central flip of the first marked coordinate is

\[
\boxed{p=ab\longmapsto p'=de.}
\]

The new pair is disjoint:

\[
p'\perp q,
\]

and

\[
p'+q=de+ac=Q_b.
\]

Thus inverse weld after the flip has one co-root central edge with missing index `b`.

---

## 2. The complete six-root boundary

The lower-order root flip on `p=ab` comes from adjacent root triangles

\[
\{a,b,d\},
\qquad
\{a,b,e\}.
\]

Their four exterior branch roots are

\[
ad,\ bd,\ ae,\ be.
\]

The second weld edge `q=ac` contributes two equal boundary incidences. Hence the complete conserved six-root boundary is

\[
\boxed{
(ad,bd,ac,ac,ae,be).
}
\]

The total sum is zero.

---

## 3. Root topology before the bad flip

Insert the equal-face weld before changing the `p` diagonal. The four internal vertices form a path whose three internal roots are

\[
\boxed{
(ab,\ bc,\ ab).
}
\]

The two end cherries have boundary pairs

\[
(ad,bd),
\qquad
(ae,be),
\]

and the two middle side branches both carry `ac`.

Every internal edge is a root. This is one root-valued six-leaf topology for the displayed boundary.

---

## 4. Topology after the bad flip

Perform the lower-order flip first. The two end cherries become

\[
(ad,ae),
\qquad
(bd,be),
\]

with central diagonal

\[
de.
\]

Attempting the weld insertion gives the internal path values

\[
\boxed{
(de,\ Q_b,\ de).
}
\]

Only the middle edge is non-root.

There are two orientations according to which copy of the `ac` boundary lies on each side of the path. Both have the same coefficient disposition.

---

## 5. Complete six-leaf enumeration

An unrooted labelled binary tree on six leaves is determined by three compatible nontrivial splits. There are

\[
\boxed{105}
\]

such topologies.

For the fixed boundary

\[
(ad,bd,ac,ac,ae,be),
\]

exact enumeration gives:

\[
\boxed{18}
\]

root-valued tree topologies.

Their induced root-preserving NNI graph has

\[
\boxed{
18\text{ vertices},
\qquad
27\text{ edges},
\qquad
\deg=3,
}
\]

and is connected.

### Theorem 5.1 — no one-move root bypass

For either orientation of the bad flipped-plus-weld path:

1. the topology is not root-valued;
2. all six NNI neighbours are non-root-valued;
3. its distance in the full 105-tree NNI graph to the root-valued sector is exactly two.

Hence every NNI path from the bad topology to a root topology begins with another non-root topology.

---

## 6. Why the standard local shortcuts do not apply

### Unique root-preserving NNI

`SIX_LEAF_NNI_ROOT_EXCHANGE_V1.md` begins with a root-valued topology and gives its unique root-valued NNI alternative at one internal edge.

The bad topology is not root-valued and has no root-valued neighbour. Therefore that theorem gives no direct bypass here.

### Five-leaf pentagon full-root branch

The full-root pentagon commutation theorem requires both branch endpoints of the critical pair to be root-valued for the same boundary word.

Here the flipped-plus-weld endpoint is non-root-valued. The hypotheses of the full-root three-step pentagon path are absent.

The applicable pentagon disposition is only the one-atom relocation branch.

### Six-port star completion

The existence of other root-valued six-leaf topologies does not by itself give a legal source move from the bad topology. The profile sector is connected internally, but separated from the bad state by a non-root first layer.

---

## 7. Consequence for cancellation repair

A first `B`-exit caused by the unique bad central flip must be retained as a genuine co-root atom with its complete six-port envelope.

It cannot be replaced by:

- one root NNI;
- one local star completion adjacent to the bad path;
- or one full-root pentagon commutation.

Any successful repair must use at least one of:

1. shorter-prefix token transport;
2. an exterior Kempe/route event changing the six-root boundary;
3. a separator exposed by the source incidence;
4. a nested history-stack rank;
5. a larger source movie containing more than the immediate six-leaf NNI neighbourhood.

---

## 8. Exact next theorem

### Target 8.1 — singular weld-exit scheduling

Take the co-root atom produced by the bad central weld flip together with:

- its ordered boundary `(ad,bd,ac,ac,ae,be)`;
- the marked old/new diagonal envelope;
- the strictly shorter history prefix supplied by `WELD_RELATION_FIRST_EXIT_V1.md`;
- outer cap and route data.

Prove that its subsequent transport either:

1. reaches a route/profile terminal;
2. reaches a separator;
3. returns to a weld-admissible `B` state on a strictly shorter frame;
4. or enters a nested cancellation frame governed by a well-founded stack rank.

The coefficient topology alone supplies no further local reduction.

---

## 9. Trust boundary

### Exact here

- standard coordinates of the unique bad central flip;
- exact six-root boundary;
- root internal path before the flip;
- co-root internal path after the flip;
- complete 105-topology enumeration;
- eighteen root-valued topologies for this boundary;
- connected cubic root-sector graph;
- zero root-valued NNI neighbours of either bad topology;
- distance two from each bad topology to the root sector;
- failure of the one-NNI and full-root-pentagon shortcuts.

### Not proved

- global consumption of the resulting co-root atom;
- the nested history-stack rank;
- cancellation macro-return;
- R2 global return, cap restoration, or global five-support closure;
- independent audit, curation, Lean verification, manuscript integration, release, arXiv, DOI, peer review, or publication.
