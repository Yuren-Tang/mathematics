# Minimal rigid cycles emit ordinary Kempe intervals

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `8a06c7339611f40ebf8efbf0d2b39d438ebac4f6`  
**Parents:**

- `projects/affine-cdc/research/CONNECTED_CYCLE_CORRECTION_RIGIDITY_V1.md`;
- `projects/affine-cdc/research/CONNECTED_CYCLE_FLEXIBLE_SWITCH_NORMAL_FORM_V1.md`;
- `projects/affine-cdc/research/LOCKED_SCALAR_COMPONENT_ROUTING_V1.md`;
- `projects/affine-cdc/research/MINIMAL_LAMINAR_INTERVAL_SURGERY_V1.md`.

**Status:** exact coefficient-to-source emission theorem. Every inclusion-minimal connected-cycle rigidity certificate contains a label admitting a private **root** shift. The corresponding safe-edge set is an ordinary support-pair Kempe system, so the rigid cycle necessarily emits a genuine global Kempe component through a proper union of cycle intervals. If this component does not give route/profile escape, its intersections enter the previously isolated pair-preserving laminar-interval branch.  
**Not implied:** admissible contraction of a pair-preserving interval, separator extraction, a strictly decreasing global complexity, canonical acceptance, Lean verification, manuscript readiness, or the global five-support theorem.

---

## 1. Global blocker sets of constant shifts

Identify roots in `R5` with edges of `K5`.

For a nonzero coefficient

\[
s\in E_5\setminus\{0\},
\]

define its root blocker set

\[
B(s)=\{x\in R_5:x+s\notin R_5\}.
\]

### Theorem 1.1 — root-shift blocker geometry

Let

\[
s=ab\in R_5.
\]

Then

\[
\boxed{
B(s)=\{ab\}\sqcup E(K_{[5]\setminus\{a,b\}}).
}
\]

Thus `B(s)` is a disjoint union

\[
K_2\sqcup K_3
\]

of four root labels.

### Proof

For a root `x`, the sum `x+s` is a root exactly when `x` is distinct from `s` and meets `s` in one support index. It fails exactly for `x=s` and for the three roots disjoint from `s`, which are the three edges of the complementary `K3`. ∎

### Theorem 1.2 — co-root-shift blocker geometry

Let

\[
s=q_i=\mathbf1+e_i
\]

be the co-root missing index `i`. Then

\[
\boxed{
B(q_i)=\{ij:j\ne i\},
}
\]

the four-edge star `K_{1,4}` at `i`.

### Proof

A root remains a root after addition of `q_i` exactly when it avoids support index `i`. Hence precisely the four roots incident with `i` are blocked. ∎

### Consequence 1.3

Every nonzero constant shift has exactly four forbidden root labels. There is no larger or unstructured edgewise blocker alphabet.

---

## 2. Private shifts inside a minimal rigid certificate

Let

\[
X\subseteq R_5
\]

be inclusion-minimal with the property that no nonzero constant shift is admissible on every element of `X`.

Minimality alone gives, for every `x in X`, some nonzero `s_x` admissible on `X\setminus\{x\}` and blocked by `x`. Such a private shift may be a root or co-root.

The four-orbit rigidity theorem classifies `X` as one of:

\[
K_{1,4},
\qquad
K_3\sqcup K_2,
\qquad
\text{bull},
\qquad
C_5.
\]

### Theorem 2.1 — existence of a private root shift

For every minimal rigid set `X`, there exist

\[
x\in X,
\qquad
s\in R_5
\]

such that

\[
\boxed{
B(s)\cap X=\{x\}.
}
\]

Hence `s` is an ordinary support-pair Kempe direction which is admissible on all certificate labels except one.

### Proof by the four orbit representatives

1. **Star**
   \[
   X=\{12,13,14,15\}.
   \]
   Take `x=s=12`. Every other element of `X` meets `12`, while `12+12=0`. Thus `B(12) cap X={12}`.

2. **Triangle plus disjoint edge**
   \[
   X=\{12,13,23,45\}.
   \]
   Take `x=12` and `s=34`. The roots `13,23,45` all meet `34`, while `12` is disjoint from `34`. Thus `B(34) cap X={12}`.

3. **Bull**
   \[
   X=\{12,13,23,14,25\}.
   \]
   Take `x=s=12`. The four remaining roots all meet `12`, while `12` itself is blocked.

4. **Five-cycle**
   \[
   X=\{12,13,24,35,45\}.
   \]
   Take `x=12` and `s=34`. Every other displayed root meets `34`, while `12` is disjoint from it.

`S5` equivariance gives the result for every member of the four orbits. ∎

### Exact finite certificate

Direct enumeration verifies the stronger labelwise table: for every label of every minimal rigid orbit there is a private shift whose full root blocker set has size four. Some exceptional labels use a co-root private shift, but every orbit has at least one private root shift as in Theorem 2.1.

---

## 3. The safe subgraph is a Kempe system

Fix the private root shift

\[
s=ab
\]

from Theorem 2.1, and let

\[
\lambda:E(G)\to R_5
\]

be the current root-valued flow.

Define the safe-edge subgraph

\[
H_s
=
\{e\in E(G):\lambda(e)+s\in R_5\}.
\]

### Theorem 3.1 — exact support-pair identity

\[
\boxed{
H_s=F_a\triangle F_b.
}
\]

Consequently `H_s` is an even subgraph of the closed source graph and is a disjoint union of connected Kempe cycles.

### Proof

A root label contains support `a` exactly when the edge lies in `F_a`, and similarly for `b`. Addition by `ab` remains root-valued exactly when the original root contains precisely one of `a,b`. This is exactly membership in `F_a triangle F_b`. Both supports are even, so their symmetric difference is even. ∎

### Corollary 3.2 — genuine global switch

For every connected component

\[
Z\subseteq H_s,
\]

the flow

\[
\lambda'=\lambda+s1_Z
\]

is root-valued. This is the ordinary Kempe component switch exchanging supports `a,b` on `Z`.

---

## 4. Emission from a rigid cycle

Let `C` be a connected cycle in the source graph whose distinct label set contains the minimal rigid certificate `X`. Choose `x,s` as in Theorem 2.1.

The certificate contains labels in `X\setminus\{x\}`, all of which are `s`-safe. It also contains the blocked label `x`.

### Theorem 4.1 — proper safe-interval emission

The intersection

\[
H_s\cap C
\]

is nonempty and proper. Therefore it is a union of nonempty path intervals of `C`, and every such interval lies in a genuine global Kempe component of `H_s`.

At every endpoint of one interval, the Kempe component leaves `C` through the third incident source edge.

### Proof

An occurrence of any label in `X\setminus\{x\}` gives a safe edge of `C`, so the intersection is nonempty. An occurrence of `x` is blocked, so it is proper.

At an endpoint vertex of a maximal safe interval, exactly one of the two cycle edges is safe. Since `H_s=F_a triangle F_b` is even, the third incident edge must also be safe. Hence the safe path continues off `C` and belongs to a full connected Kempe cycle. ∎

### Corollary 4.2 — no isolated coefficient rigidity

A minimal rigid coefficient certificate cannot remain confined to the original cycle. It necessarily emits an ordinary Kempe component into the surrounding side-incidence semantics.

Thus coefficient rigidity itself is not a terminal obstruction atom.

---

## 5. Route escape or laminar interval

Now place the emitted Kempe component in a route-locked four-port or scalar-interval environment.

Let `Z` be a connected component of `H_s` meeting `C` in a nonempty proper interval.

### Theorem 5.1 — composition interface dichotomy

Exactly one of the following occurs.

1. **Pair-changing emission.**  
   Switching `Z` changes the terminal pairing or boundary profile. Then one has a genuine Kempe/profile escape, subject only to the already classified boundary-state bookkeeping.

2. **Pair-preserving emission.**  
   Switching `Z` preserves the locked terminal matching. Then the attachment intervals of `Z` to the locked terminal paths are noninterlacing. In a support-minimal family, the pair-preserving components form a laminar containment forest, and a minimal emitted interval is a four-port interval of the type isolated in `MINIMAL_LAMINAR_INTERVAL_SURGERY_V1.md`.

### Proof

The switch is a genuine root-valued Kempe move by Corollary 3.2. If its terminal pairing changes, this is the first branch.

Otherwise the binary route-change theorem applies: interlacing attachments would reconnect the two locked terminal pairs crosswise, contradicting pair preservation. Hence attachments are noninterlacing, and the previously proved laminarity reduction applies. ∎

### Corollary 5.2 — strict-descent frontier

Every connected-cycle rigidity certificate enters the same final composition frontier:

\[
\boxed{
\text{profile escape}
\quad\text{or}\quad
\text{minimal pair-preserving laminar interval}.}
\]

The four rigid coefficient orbits do not require four separate global theories.

---

## 6. What remains

The remaining theorem is now purely source-compositional.

For a minimal pair-preserving interval emitted by Theorem 5.1, prove one of:

1. an admissible replacement with smaller side-signature complexity;
2. an internal two-cut or four-cut, which lifts to a separator of the original source graph;
3. a bounded DDD/co-root/zero defect atom;
4. a second Kempe component crossing the laminar order, giving profile escape;
5. a serial contraction lowering the lexicographic interval measure.

The natural measure remains

\[
\mathcal D(R)
=
\bigl(
 |\Sigma(R)|,
 N_{\mathrm{frame}}(R),
 |V(R)|,
 \beta(R),
 D(R)
\bigr).
\]

What is new is that every coefficient-rigid connected cycle is now proved to supply the actual Kempe interval on which this strict-descent theorem must operate.

---

## 7. Trust boundary

### Exact here

- the four-label blocker geometry for every nonzero shift;
- existence of a private root shift in every minimal rigid orbit;
- identification of its safe subgraph with an ordinary support-pair Kempe system;
- emission of a proper safe interval from every cycle carrying that certificate;
- extension of each emitted interval to a genuine global Kempe component;
- reduction to profile escape or the established pair-preserving laminar-interval branch.

### Still open

- composition-safe replacement of a minimal pair-preserving interval;
- extraction of a two-cut/four-cut from every split side signature;
- treatment of arbitrary external components attached inside the interval;
- proof that one branch strictly lowers `D(R)`;
- horizontal/global induction and the global five-support theorem.
