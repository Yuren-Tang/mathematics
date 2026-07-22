# Octahedral antipodal switches and the triangle/star Kempe-decomposition obstruction

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `54819ee04bd251b705a7646b51e5ea4ea8513217`  
**Parents:**

- `projects/affine-cdc/research/CONNECTED_CYCLE_FLEXIBLE_SWITCH_NORMAL_FORM_V1.md`;
- `projects/affine-cdc/research/PETERSEN_IDENTITY_HEXAGON_TRANSVERSE_CHANNEL_TRANSVERSAL_V1.md`;
- `projects/affine-cdc/research/DDD_ROUTE_ORIENTATION_COVER_V1.md`;
- `projects/affine-cdc/five-support/route-locked-quotient-phase.md`.

**Status:** exact decomposition theorem for a co-root/antipodal connected-cycle switch. The switch is a composition of two ordinary support-pair Kempe switches exactly when one opposite-edge pair of the active `K4` is absent from the cycle label set. Failure has a three-label transversal certificate, and the eight minimal certificates are exactly the four triangles and four stars of `K4`. This is the same index-two triangle/star class previously found in Type-X and oriented-route lifting.  
**Not implied:** that an indecomposable antipodal switch is compositionally irreducible in the full source graph, bounded localisation of nonconsecutive transversal labels, strict route/profile progress, canonical acceptance, Lean verification, manuscript readiness, or the global five-support theorem.

---

## 1. Antipodal cycle sector

Fix a support index

\[
i\in[5]
\]

and put

\[
J=[5]\setminus\{i\}.
\]

Let

\[
q_i=\mathbf1+e_i
\]

be the co-root supported on `J`.

Suppose a connected cycle `C` in a root-valued flow satisfies

\[
\lambda(e)\in E(K_J)
\qquad(e\in C).
\]

Then the co-root shift

\[
\lambda^{\mathrm{opp}}
=
\lambda+q_i1_C
\]

is root-valued and replaces every `K4` edge label by its opposite edge.

Let

\[
X_C
=\{\lambda(e):e\in C\}
\subseteq E(K_J)
\]

be the distinct cycle label set.

---

## 2. The three perfect-matching decompositions

The co-root `q_i` has exactly three decompositions into two disjoint roots:

\[
\boxed{
q_i=s+t,
}
\]

one for each perfect matching

\[
M=\{s,t\}
\]

of `K_J\cong K_4`.

### Lemma 2.1 — first Kempe factor criterion

Fix one decomposition

\[
q_i=s+t
\]

with `s,t` opposite `K4` edges. The root shift

\[
\lambda\longmapsto\lambda+s1_C
\]

is root-valued if and only if

\[
\boxed{X_C\cap\{s,t\}=\varnothing.}
\]

### Proof

Inside `K4`, the unique root disjoint from `s` is its opposite edge `t`. A root shift by `s` is admissible on a label `x` exactly when `x` meets `s` and `x != s`. Thus every cycle label admits the shift exactly when neither forbidden label `s` nor `t` occurs. ∎

### Lemma 2.2 — second factor is then automatic

If the shift by `s` is root-valued, then the subsequent shift by `t` is root-valued and

\[
(\lambda+s1_C)+t1_C
=
\lambda+q_i1_C.
\]

### Proof

The final antipodal flow `lambda+q_i1_C` is root-valued. Since the intermediate flow is root-valued by assumption and the difference between intermediate and final flows is `t1_C`, connected-cycle correction rigidity gives the stated second Kempe switch. Edgewise, for each label `x`,

\[
(x+s)+t=x+q_i
\]

is a root. ∎

### Theorem 2.3 — exact two-Kempe decomposition criterion

The antipodal switch is a composition of two ordinary support-pair Kempe component switches if and only if there exists one perfect matching

\[
M=\{s,t\}
\]

of `K4` such that

\[
\boxed{X_C\cap M=\varnothing.}
\]

Equivalently:

\[
\boxed{
\text{decomposable}
\iff
X_C\text{ misses one complete opposite-edge pair}.}
\]

---

## 3. Indecomposability is a transversal condition

The three perfect matchings of `K4` partition its six edges into three opposite-edge pairs

\[
M_1,M_2,M_3.
\]

### Theorem 3.1 — matching-hitting criterion

The antipodal switch is not decomposable into two ordinary Kempe switches if and only if

\[
\boxed{
X_C\cap M_j\ne\varnothing
\qquad(j=1,2,3).}
\]

Thus indecomposability means exactly that the cycle label set hits every opposite-edge pair.

### Corollary 3.2 — three-label certificate

If the antipodal switch is indecomposable, choose

\[
x_j\in X_C\cap M_j
\qquad(j=1,2,3).
\]

Then

\[
\boxed{
T=\{x_1,x_2,x_3\}
}
\]

is a transversal of the three opposite-edge pairs and already certifies indecomposability.

Hence every indecomposable antipodal cycle has a coefficient certificate involving only three cycle labels.

---

## 4. Triangles and stars

A transversal of the three perfect matchings of `K4` chooses one edge from each opposite pair. There are

\[
2^3=8
\]

such transversals.

### Theorem 4.1 — transversal classification

Every opposite-pair transversal is exactly one of:

1. the three edges of a triangle `K3` in `K4`;
2. the three edges of a star `K1,3` in `K4`.

There are four triangles and four stars.

### Proof

Let `T` be a three-edge transversal. No two selected edges are opposite.

If the three edges have a common endpoint, they form a star. Otherwise choose two meeting edges `ab,ac`. The third selected edge cannot be opposite either one, so it must meet both. Without using the common endpoint `a`, the only possibility is `bc`, giving the triangle on `{a,b,c}`. These alternatives are exclusive and exhaust all transversals. ∎

### Corollary 4.2 — exact finite census

The inclusion-minimal label sets preventing every two-Kempe decomposition are the eight three-edge transversals:

\[
\boxed{
4\text{ triangles}
+
4\text{ stars}.}
\]

Under `S4`, they form two orbits of cardinality four.

---

## 5. The orientation-parity identification

Orient each opposite-edge pair and encode a transversal by

\[
\epsilon=(\epsilon_1,\epsilon_2,\epsilon_3)
\in\mathbf F_2^3.
\]

Changing all three pair orientations adds

\[
111.
\]

The parity

\[
\vartheta(T)=\epsilon_1+\epsilon_2+\epsilon_3
\]

changes under global orientation reversal, but the partition into the two four-element classes is canonical up to exchanging their names.

### Theorem 5.1 — triangle/star index-two class

After one orientation convention is fixed, one parity class consists of the four triangles and the other consists of the four stars.

The even subgroup

\[
S_4
\subset
C_2^3\rtimes S_3
\]

preserves the triangle/star classes, while an odd orientation flip exchanges them.

### Consequence 5.2

The obstruction to decomposing an antipodal cycle switch into two ordinary Kempe switches is not a new bit. Its minimal certificate carries exactly the same index-two triangle/star class already appearing in:

- the Type-X oriented channel transversal;
- the oriented-route exact sequence;
- the DDD orientation-cover obstruction.

This is now an equality of concrete cycle-label mechanisms, not merely a representation-theoretic analogy.

---

## 6. Revised antipodal-switch trichotomy

### Theorem 6.1

For every co-root/antipodal connected-cycle switch, exactly one of the following holds.

#### Missing matching pair

Some opposite-edge pair `M={s,t}` is absent from `X_C`. Then

\[
q_i=s+t
\]

and the antipodal switch is the composition of two ordinary Kempe component switches.

#### Triangle certificate

The label set contains one `K4` triangle transversal. The antipodal switch is indecomposable into two root shifts and carries the triangle parity class.

#### Star certificate

The label set contains one `K1,3` transversal. The antipodal switch is indecomposable into two root shifts and carries the star parity class.

There is no fourth coefficient-level antipodal mechanism.

---

## 7. Source-side implications

### Decomposable branch

The co-root move can be implemented through two genuine support-pair Kempe switches. The remaining question is whether either intermediate cover supplies route/profile progress or whether both moves are gauge-internal.

### Triangle branch

The three certificate roots form a Tait root triangle. Their occurrences should feed the rank-two/Tait route-resolution or Type-H triangle machinery.

### Star branch

The three certificate roots sum to the complementary co-root. Their occurrences should feed the DDD/co-root defect and orientation-holonomy machinery.

The words “should feed” are mechanism targets: the certificate labels may occur at nonconsecutive source positions, and their external side attachments remain to be controlled.

---

## 8. Trust boundary

### Exact here

- the three perfect-matching decompositions of `q_i`;
- the missing-opposite-pair criterion for two-Kempe decomposition;
- the matching-hitting criterion for indecomposability;
- the three-label certificate theorem;
- the triangle/star classification and `4+4` census;
- identification with the existing index-two transversal parity.

### Still open

- route/profile progress from both factors in the decomposable branch;
- localisation of nonconsecutive triangle/star labels;
- graph-level equality between this parity and the physical DDD blossom class in arbitrary regions;
- minimal laminar interval replacement and separator extraction;
- strict side-signature descent;
- horizontal/global induction and the global five-support theorem.