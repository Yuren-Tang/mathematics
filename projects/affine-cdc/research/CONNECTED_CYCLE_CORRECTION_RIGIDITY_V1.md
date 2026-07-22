# Connected-cycle correction rigidity and the four minimal root blockers

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `53223262d9b8cbc3ffc21c74e69cd8437a9b3cef`  
**Parents:**

- `projects/affine-cdc/research/CONNECTED_KEMPE_CYCLE_ROOT_LIFT_CERTIFICATE_V1.md`;
- `projects/affine-cdc/research/TYPE_X_SELECTOR_RANK_REDUCTION_V1.md`;
- `projects/affine-cdc/five-support/root-flow-lifting.md`;
- `projects/affine-cdc/five-support/gauge-and-reconfiguration.md`.

**Status:** exact connected-support rigidity theorem. Every `E5`-flow correction supported on one connected binary cycle is a constant coefficient shift. A root-valued cycle has no nonzero root-valued correction if and only if its set of root labels is simultaneously an edge cover of `K5` and a dominating set of the Petersen graph. Every inclusion-minimal rigid label set has size four or five and belongs to one of four `S5` orbits: `K1,4`, `K3 sqcup K2`, the bull graph, or `C5`.  
**Not implied:** that a coefficient-rigid label set occurs on a bounded consecutive source segment, admissible replacement preserving a prescribed four-pole route, separator extraction, strict descent, canonical acceptance, Lean verification, manuscript readiness, or the global five-support theorem.

---

## 1. Corrections supported on a connected cycle are constant

Let

\[
C=e_0e_1\cdots e_{n-1}e_0
\]

be a connected binary cycle in a graph or multipole. Let

\[
h:E(G)\to E_5
\]

be an `E5`-valued flow whose support is contained in `C`.

### Theorem 1.1 — connected-cycle correction rigidity

There is one coefficient

\[
s\in E_5
\]

such that

\[
\boxed{h=s1_C.}
\]

### Proof

At every vertex of `C`, the only possibly nonzero values of `h` are those on the two incident cycle edges. Kirchhoff conservation gives

\[
h(e_{i-1})+h(e_i)=0,
\]

hence

\[
h(e_{i-1})=h(e_i).
\]

Connectivity propagates this equality around the whole cycle. ∎

### Corollary 1.2 — complete cycle-supported root-flow criterion

Let

\[
\lambda:E(G)\to R_5
\]

be root-valued. A second root-valued flow `lambda'` which agrees with `lambda` off `C` exists exactly when there is

\[
0\ne s\in E_5
\]

such that

\[
\boxed{
\lambda(e)+s\in R_5
\qquad(e\in C).}
\]

Then necessarily

\[
\lambda'=\lambda+s1_C.
\]

Thus constant shifts are not merely sufficient: they are the complete class of corrections with support contained in one connected cycle.

---

## 2. Root and co-root shifts in the `K5` model

Identify the ten roots with the ten edges of `K5`. Let

\[
X_C=\{\lambda(e):e\in C\}\subseteq E(K_5)
\]

be the set of distinct root values appearing on the cycle. Repetition does not affect the common-shift condition.

### Lemma 2.1 — root-shift criterion

Let

\[
s=ab\in R_5.
\]

For a root edge `x`,

\[
x+s\in R_5
\]

if and only if

1. `x != s`; and
2. the two `K5` edges `x,s` meet.

### Proof

If `x=s`, the sum is zero. If distinct roots meet in one support index, their sum is the third root of the corresponding `K5` triangle. If they are disjoint, their sum is a co-root. ∎

### Lemma 2.2 — co-root-shift criterion

Let

\[
q_i=\mathbf1+e_i
\]

be the co-root missing support index `i`. For a root edge `x`,

\[
x+q_i\in R_5
\]

if and only if `x` is not incident with `i`.

### Proof

If `x` avoids `i`, its two support coordinates cancel two of the four ones of `q_i`, leaving a root on the other two coordinates. If `x` meets `i`, addition produces weight four rather than weight two. ∎

---

## 3. Edge-cover plus Petersen-domination criterion

The Petersen graph is

\[
P=KG(5,2),
\]

whose vertices are the root edges of `K5`, with adjacency given by disjointness.

### Theorem 3.1 — exact full-shift rigidity criterion

The cycle label set `X_C` admits no nonzero common shift

\[
s\in E_5\setminus\{0\}
\]

if and only if both conditions hold:

1. `X_C` is an edge cover of `K5`:
   \[
   \bigcup_{x\in X_C}x=[5];
   \]
2. `X_C` is a dominating set of the Petersen graph `P`.

Equivalently, every root edge outside `X_C` is disjoint from at least one edge of `X_C`.

### Proof

By Lemma 2.2, a co-root shift `q_i` is common-admissible exactly when vertex `i` is missed by every edge of `X_C`. Thus all five co-root shifts are killed exactly when `X_C` is an edge cover of `K5`.

By Lemma 2.1, a root shift `s` is common-admissible exactly when `s` is not itself in `X_C` and meets every edge of `X_C`. Thus every root shift is killed exactly when each root vertex `s` of the Petersen graph either lies in `X_C` or has a Petersen neighbour in `X_C`; this is precisely domination. ∎

### Corollary 3.2

Root-flow rigidity of a connected cycle is an exact finite graph property of the set of `K5` edge labels:

\[
\boxed{
\text{cycle-rigid}
\iff
\text{edge-cover in }K_5
+
\text{dominating set in }KG(5,2).}
\]

---

## 4. Inclusion-minimal rigid root sets

Call

\[
X\subseteq E(K_5)
\]

**minimal rigid** if it satisfies Theorem 3.1 and no proper subset does.

### Theorem 4.1 — size bound

Every minimal rigid set has size

\[
\boxed{|X|=4\text{ or }5.}
\]

There are exactly

\[
15
\]

minimal rigid four-sets and

\[
72
\]

minimal rigid five-sets.

### Theorem 4.2 — four `S5` orbits

Under the natural `S5` action on `K5`, the minimal rigid sets form exactly four orbits.

#### Orbit `R_{4,\star}` — four-edge star

Representative:

\[
\boxed{
\{12,13,14,15\}=K_{1,4}.}
\]

Degree sequence:

\[
(4,1,1,1,1).
\]

Orbit cardinality:

\[
5.
\]

The sum of the four root vectors is the co-root

\[
q_1=2345.
\]

#### Orbit `R_{4,\triangle+e}` — triangle plus disjoint edge

Representative:

\[
\boxed{
\{12,13,23,45\}=K_3\sqcup K_2.}
\]

Degree sequence:

\[
(2,2,2,1,1).
\]

Orbit cardinality:

\[
10.
\]

The triangle sums to zero, so the total root sum is the isolated edge `45`.

#### Orbit `R_{5,\mathrm{bull}}` — bull graph

Representative:

\[
\boxed{
\{12,13,23,14,25\}.}
\]

This is a triangle with two pendant edges attached at two distinct triangle vertices.

Degree sequence:

\[
(3,3,2,1,1).
\]

Orbit cardinality:

\[
60.
\]

Its total root sum is the co-root on the four odd-degree vertices.

#### Orbit `R_{5,C_5}` — five-cycle

Representative:

\[
\boxed{
\{12,13,24,35,45\}=C_5.}
\]

Degree sequence:

\[
(2,2,2,2,2).
\]

Orbit cardinality:

\[
12.
\]

The total root sum is zero.

### Exact finite certificate

Exhaustive enumeration of all subsets of the ten `K5` edges verifies:

\[
\boxed{
87\text{ minimal rigid sets}
=
15\text{ of size }4
+
72\text{ of size }5.}
\]

Canonicalisation under all `120` support permutations gives the four displayed orbits, with cardinalities

\[
5,\ 10,\ 60,\ 12.
\]

### Proof

Theorem 3.1 reduces the problem to a ten-vertex finite classification. Enumerate all edge subsets, retain those that are both `K5` edge covers and Petersen dominating sets, and impose inclusion-minimality. The resulting degree sequences and component structures identify the four ordinary graph isomorphism types above. Their orbit cardinalities sum to `87`, proving completeness. ∎

---

## 5. Bounded rigidity certificate on every cycle

### Theorem 5.1 — five-label rigidity certificate

If a connected root-valued cycle `C` admits no nonzero root-valued correction supported on `C`, then its root-value set contains a minimal rigid subset

\[
X_0\subseteq X_C
\]

with

\[
\boxed{|X_0|\le5.}
\]

Moreover `X_0` is one of the four geometries in Theorem 4.2.

### Proof

Choose an inclusion-minimal subset of `X_C` that still kills all nonzero shifts. Theorem 4.2 applies. ∎

### Corollary 5.2 — no unbounded coefficient rigidity alphabet

An arbitrarily long connected scalar/Kempe cycle has only two coefficient-level outcomes:

1. a nonzero constant shift gives a second root-valued flow differing only on the cycle;
2. at most five distinct cycle root values form one of four rigidity certificates.

Long cycle length can survive only through the source positions, route incidence, and side attachments of these bounded labels, not through new coefficient states.

---

## 6. Relation to the six-channel certificate

Fixing an active root `r` and restricting shifts to its six repair roots `S_r` gives the sharper four-edge channel certificate of

`CONNECTED_KEMPE_CYCLE_ROOT_LIFT_CERTIFICATE_V1.md`.

The two levels should be distinguished:

- **six-channel failure:** no shift in `S_r`; certificate size at most four, with triangle/star/pentagon geometry;
- **full cycle rigidity:** no nonzero shift in all of `E5`; certificate size at most five, with star, triangle-plus-edge, bull, or five-cycle geometry.

A six-channel blocker may still admit a root or co-root shift outside `S_r`; this is a genuine reslicing/horizontal-motion candidate. Full rigidity is the exact obstruction to every correction supported only on the connected cycle.

---

## 7. Revised composition frontier

The rank-one invisible component branch now has an exact first dichotomy.

### Flexible cycle

A common nonzero shift exists. Then

\[
\lambda'=\lambda+s1_C
\]

is an actual root-valued alternative with identical exterior data. The remaining task is to determine whether its internal route change gives profile escape, serial simplification, or an immediately gluable four-pole state.

### Rigid cycle

No common shift exists. Then at most five root labels on the cycle form one of:

\[
K_{1,4},
\qquad
K_3\sqcup K_2,
\qquad
\text{bull},
\qquad
C_5.
\]

The remaining graph theorem should localise their occurrences:

1. `K1,4` and bull certificates should enter the co-root/DDD defect branch through their co-root total;
2. `K3 sqcup K2` should separate a Tait triangle from one residual root direction;
3. `C5` should enter the established Petersen pentagon/reflection branch;
4. separated occurrences should expose a smaller cyclic interval or quotient cut.

These are mechanism targets, not yet theorems.

---

## 8. Trust boundary

### Exact here

- every correction supported on one connected cycle is constant;
- the complete common-shift criterion;
- the edge-cover plus Petersen-domination characterisation;
- the size-four-or-five bound for minimal rigidity;
- the `15+72` census;
- the four `S5` orbit classification;
- the five-label certificate theorem.

### Still open

- conversion of a flexible cycle shift into strict route/profile progress in every external context;
- localisation of nonconsecutive rigid labels on a bounded source interval;
- composition-safe treatment of the four rigidity geometries;
- minimal laminar interval replacement and separator extraction;
- strict side-signature descent;
- horizontal/global induction and the global five-support theorem.