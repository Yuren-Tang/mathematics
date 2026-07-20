# Flat translation parity, global complement, and matching triality

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Parent:** `projects/affine-cdc/research/AFFINE_A3_FLAT_CODE_BRIDGE_V1.md`  
**Status:** exact finite quotient theorem; physical gauge and serial-cut interpretation remain open.  
**Not implied:** canonical acceptance, independent audit, Lean verification, manuscript readiness, or the global five-support theorem.

---

## 1. Evaluation model for the flat code

Let

\[
V\cong\mathbf F_2^3
\]

and fix a nonzero terminal colour

\[
g\in V.
\]

The four locked challenges are

\[
\Lambda_g
=
\{\lambda\in V^*:\lambda(g)=1\}
\cong AG(2,2).
\]

For `v in V`, define

\[
f_v:\Lambda_g\to\mathbf F_2,
\qquad
f_v(\lambda)=\lambda(v).
\]

### Theorem 1.1 — canonical evaluation isomorphism

\[
\boxed{
V
\xrightarrow{\sim}
\operatorname{Aff}(\Lambda_g,\mathbf F_2),
\qquad
v\mapsto f_v.
}
\]

### Proof

The map is linear. If `f_v=0`, then every covector in the affine plane `Lambda_g` annihilates `v`. Differences of points of `Lambda_g` span the two-dimensional annihilator of `g`, while any one point has value one on `g`; together they span `V*`. Hence `v=0`. Both spaces have dimension three.

Under the previous affine-`A3` bridge, this identifies

\[
Q(A_3)/2Q(A_3)
\cong V.
\]

---

## 2. Weight classification

### Theorem 2.1

The evaluation words have exactly three types:

\[
\boxed{f_0=0000,}
\]

\[
\boxed{f_g=1111,}
\]

and, for

\[
v\notin\{0,g\},
\]

\[
\boxed{|f_v|=2.}
\]

### Proof

The first two identities follow from the definition of `Lambda_g`. If `v` is neither zero nor `g`, the restrictions `lambda -> lambda(v)` and `lambda -> lambda(g)=1` are independent affine coordinates on the four-point plane, so exactly two of the four points evaluate to one.

Thus every nonzero flat translation is either:

1. the constant all-four word `1111`;
2. a two-of-four word defining a `2|2` partition of the challenge plane.

---

## 3. Complement gauge

For every `v in V`,

\[
\boxed{
f_{v+g}=f_v+\mathbf1.}
\]

Indeed, every `lambda in Lambda_g` satisfies `lambda(g)=1`.

Therefore `v` and `v+g` produce complementary four-bit words and determine the same unordered `2|2` partition.

### Theorem 3.1 — quotient by global complement

\[
\boxed{
V/\langle g\rangle
\cong
\operatorname{Aff}(\Lambda_g,\mathbf F_2)/\langle\mathbf1\rangle
\cong\mathbf F_2^2.
}
\]

The three nonzero quotient elements correspond bijectively to the three parallel classes of `AG(2,2)`, equivalently the three perfect matchings of its four points.

### Proof

The evaluation isomorphism sends `g` to the constant-one word. Quotienting affine functions by constants leaves the two-dimensional linear-function space on the translation plane of `AG(2,2)`. Its three nonzero elements have the three distinct two-point kernels, i.e. the three parallel classes.

---

## 4. Flat translation triality

Combining the affine-`A3` translation theorem with Theorem 3.1 gives:

### Theorem 4.1

After mod-two reduction and removal of the global-complement direction,

\[
\boxed{
Q(A_3)/\bigl(2Q(A_3)+\langle g\rangle\bigr)
\cong\mathbf F_2^2.
}
\]

Its three nonzero classes are naturally the three route/matching directions.

Thus the finite flat identity-holonomy residue contains no additional support-unordered state beyond:

1. zero;
2. the pure all-four complement direction;
3. one of three matching directions.

### Relation to DDD triality

The same three-element projective line appears in:

- the three nonzero elements of `H1(K2,3;F2)`;
- the three root/co-root DDD ambiguity directions;
- the three terminal perfect matchings;
- the three nonzero elements of `V/<g>`.

The present theorem gives an exact finite identification on the flat-translation side. A physical theorem is still required to identify the actual graph-side complement gauge and matching separator with these quotient classes.

---

## 5. Composition targets

### Target 5.1 — constant-word gauge

Show that a physical period with word `1111` is either:

- removable by adding the terminal colour `g` to a separated potential region;
- a common-cut/full-sheet reversal;
- or a bounded defect/DDD interface if the required region is not separable.

### Target 5.2 — weight-two serial split

For a physical period with a weight-two affine word, use its canonical `2|2` matching to prove one of:

- nested/serial terminal linkage;
- a cyclic four-cut with that matching;
- a profile-expanding Kempe move;
- or a smaller DDD/defect unit.

### Target 5.3 — compatibility with Type T and Type H

Prove that the matching class selected by a nonconstant flat period is the same matching recorded by the four-pole routing automaton. This would identify:

- path/serial translation with Type T;
- failure of consistent matching orientation with the Type H/DDD branch.

---

## 6. Trust boundary

### Exact here

- the evaluation isomorphism `V -> Aff(Lambda_g,F2)`;
- the `0 / 1111 / weight-two` classification;
- complement relation `f_(v+g)=f_v+1`;
- the quotient `V/<g> ≅ F2^2`;
- identification of its three nonzero classes with the three affine parallel classes/perfect matchings.

### Still open

- physical gauge triviality of the constant-one period;
- conversion of a weight-two period into a serial or four-pole source reduction;
- equality with the matching recorded by the Type-T/Type-H automata;
- horizontal/global induction and the global five-support theorem.
