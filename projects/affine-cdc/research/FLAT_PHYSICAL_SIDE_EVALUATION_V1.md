# Flat physical side evaluation and the zero-or-triality displacement dichotomy

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Parent:** `projects/affine-cdc/research/OCTAHEDRAL_PROJECTIVE_STOKES_V1.md`  
**Input:** the active-corpus flat-potential equivalence for a full-rank locked quotient.  
**Status:** exact physical side-word theorem in the flat branch; calibration with the octahedral projective Stokes map and strict source reduction remain open.  
**Not implied:** canonical acceptance, independent audit, Lean verification, manuscript readiness, or the global five-support theorem.

---

## 1. Locked quotient and scalar sheets

Let

\[
c:E(Q)\to V\setminus\{0\}
\]

be the full-rank quotient flow, with

\[
V\cong\mathbf F_2^3,
\]

and suppose all four terminals have colour

\[
g\in V\setminus\{0\}.
\]

The four locked challenges form the affine plane

\[
\Lambda_g
=
\{\lambda\in V^*: \lambda(g)=1\}
\cong AG(2,2).
\]

For each `lambda in Lambda_g`, define the scalar even subgraph

\[
C_\lambda
=
\{e\in E(Q):\lambda(c(e))=1\}.
\]

At every internal cubic vertex, `C_lambda` has even degree. Since every terminal edge has colour `g` and `lambda(g)=1`, its boundary is the prescribed four-terminal boundary. In the locked regime every `C_lambda` realises the same terminal route.

---

## 2. Flat potential

Assume the flat branch of the active-corpus theorem. Thus there is a vertex potential

\[
p:V(Q)\to V
\]

with terminal values

\[
0,0,g,g
\]

and, on every internal edge `e=uv`,

\[
\boxed{
p(u)+p(v)\in\{0,c(e)+g\}.}
\]

For each challenge `lambda`, put

\[
s_\lambda(v)=\lambda(p(v)).
\]

### Theorem 2.1 — scalar-component constancy

For every `lambda in Lambda_g`, the function `s_lambda` is constant on every connected component of `C_lambda`.

### Proof

Let `e=uv` belong to `C_lambda`. Then

\[
\lambda(c(e))=1
\]

and

\[
\lambda(g)=1.
\]

If `p(u)+p(v)=0`, then plainly

\[
s_\lambda(u)+s_\lambda(v)=0.
\]

If

\[
p(u)+p(v)=c(e)+g,
\]

then

\[
s_\lambda(u)+s_\lambda(v)
=\lambda(c(e)) + \lambda(g)
=1+1
=0.
\]

Thus `s_lambda` is constant across every edge of `C_lambda`.

### Consequence 2.2 — physical side values

The constants of `s_lambda` on the scalar components give a legitimate simultaneous choice of scalar-sheet side values.

At the four terminals, the values are

\[
0,0,1,1,
\]

because the terminal potential values are `0,0,g,g`. Hence these side values encode the locked terminal pairing.

---

## 3. Local four-bit word on a `g`-edge

Let

\[
E_g=\{e:c(e)=g\}.
\]

This is a matching in the cubic quotient graph.

Let `e=uv in E_g`. The flat edge condition becomes

\[
p(u)+p(v)\in\{0,g+g\}=\{0\}.
\]

Therefore

\[
\boxed{
p(u)=p(v).}
\]

Write the common value as

\[
v_e:=p(u)=p(v).
\]

Every `g`-edge belongs to every scalar sheet because `lambda(g)=1`. Its local four-bit side word is therefore

\[
b_e:\Lambda_g\to\mathbf F_2,
\qquad
b_e(\lambda)=s_\lambda(u)=s_\lambda(v).
\]

### Theorem 3.1 — exact physical evaluation word

\[
\boxed{
b_e(\lambda)=\lambda(v_e).}
\]

Equivalently,

\[
\boxed{b_e=f_{v_e},}
\]

where

\[
f_v(\lambda)=\lambda(v)
\]

is the canonical evaluation model of the affine four-bit code.

### Corollary 3.2 — relative translation word

For two `g`-edges `e,e'`,

\[
\boxed{
b_e+b_{e'}=f_{v_e+v_{e'}}.}
\]

Thus every flat physical relative side word is automatically affine. No additional four-bit word can occur in the flat branch.

---

## 4. Regional boundary word

Let `B` be any finite set of `g`-edges. Define its side boundary word by

\[
\Theta_p(B)
=
\sum_{e\in B}b_e
\in\mathbf F_2^{\Lambda_g}.
\]

### Theorem 4.1 — flat regional evaluation law

\[
\boxed{
\Theta_p(B)
=f_{\sum_{e\in B}v_e}.
}
\]

### Proof

For every challenge `lambda`,

\[
\Theta_p(B)(\lambda)
=\sum_{e\in B}\lambda(v_e)
=\lambda\left(\sum_{e\in B}v_e\right).
\]

### Consequence 4.2

Every flat regional boundary word has even total parity. Hence a physical odd/non-affine four-bit word cannot occur in a region carrying one global flat potential; it belongs to the nonflat/common-cut/DDD branch.

This is the physical flat half of the desired regional Stokes dichotomy.

---

## 5. Complement gauge and matching class

Because every `lambda in Lambda_g` satisfies `lambda(g)=1`,

\[
f_{v+g}=f_v+\mathbf1.
\]

Therefore the support-unordered matching selected by a nonconstant flat word depends only on

\[
[v]\in V/\langle g\rangle.
\]

For two `g`-edges,

\[
\boxed{
[b_e+b_{e'}]
\in
\operatorname{Aff}(\Lambda_g,\mathbf F_2)/\langle\mathbf1\rangle
}
\]

is represented by

\[
\boxed{
[v_e+v_{e'}]
\in V/\langle g\rangle.
}
\]

The three nonzero classes are the three perfect matchings of the four challenge points.

### Trust boundary

The matching class is exact for the chosen flat potential and its induced scalar side choices. Different admissible flat potentials can change the representative evaluation word. The remaining comparison theorem must show that the class selected by the actual overlap/frame transport agrees with the octahedral projective Stokes class, or else that the disagreement exposes a bounded separator or defect unit.

---

## 6. Composition law

Suppose `e_0,e_1,e_2` are `g`-edges connected by successive physical flat periods. Then

\[
(b_{e_0}+b_{e_1})+(b_{e_1}+b_{e_2})
=b_{e_0}+b_{e_2}.
\]

At the potential level,

\[
(v_{e_0}+v_{e_1})+(v_{e_1}+v_{e_2})
=v_{e_0}+v_{e_2}.
\]

Thus flat physical periods form an additive displacement system in `V`, and support-unordered periods form an additive system in

\[
V/\langle g\rangle\cong\mathbf F_2^2.
\]

This is the exact physical analogue of affine-`A3` translation composition after mod-two reduction.

---

## 7. Zero-or-triality image theorem

Let `L` be an `S4`-stable family of realised flat identity periods, closed under concatenation and reversal. Assume each period is assigned its projective displacement

\[
\Delta_p(\gamma)
\in V/\langle g\rangle
\]

from the endpoint `g`-edge potentials.

The module

\[
V/\langle g\rangle
\]

is the natural two-dimensional `GL(2,2)` module; the local `S4` action factors through

\[
S_4\twoheadrightarrow S_3\cong GL(2,2).
\]

It has no nonzero proper invariant subspace.

### Theorem 7.1 — zero-or-full matching image

The subgroup generated by all realised projective displacements is either

\[
\boxed{0}
\]

or

\[
\boxed{V/\langle g\rangle.}
\]

There is no invariant rank-one intermediate matching residue.

### Consequences

1. **Zero image:** every realised flat period has word `0000` or `1111`. The complete physical frontier is the constant complement gauge/common-cut problem.
2. **Full image:** all three matching directions occur. Any nonzero equivariant comparison with the affine-`A3` projective translation module is the unique isomorphism, so one local nonzero translation-cell calibration suffices to identify the complete matching triality.

This reduces the matching-to-routing theorem to one bounded physical translation hexagon, provided the realised family is closed under the local support symmetries.

---

## 8. Revised frontier

### Target 8.1 — one-cell calibration

Choose one explicit paired-curvature translation hexagon. Compute the endpoint flat-potential displacement

\[
[v_e+v_{e'}]\in V/\langle g\rangle
\]

and prove it equals the matching class assigned by the projective octahedral Stokes map.

By Theorem 7.1 and equivariance, one nonzero calibration closes the complete flat matching comparison.

### Target 8.2 — zero-image branch

If every translation cell has zero projective displacement, show that each period is removable by a separated `g`-gauge, or yields an all-four-sheet common cut, bounded DDD interface, or defect unit.

### Target 8.3 — matching source reduction

Once a nonzero projective displacement is calibrated, identify its `2|2` partition with the physical four-pole route and derive serial/Type-T descent, a cyclic four-cut, profile escape, or smaller defect unit.

---

## 9. Trust boundary

### Exact here

- scalar-component constancy of `lambda o p`;
- construction of simultaneous physical side values from a flat potential;
- equality `b_e=f_(v_e)` on every `g`-edge;
- the relative and regional evaluation formulas;
- complement/matching quotient;
- additive composition of flat displacements;
- the zero-or-full image theorem for an `S4`-stable realised family.

### Still open

- calibration with the octahedral projective Stokes map;
- physical uniqueness or canonical choice of flat potential;
- elimination of the constant complement branch;
- conversion of a matching class into strict serial/four-pole source reduction;
- horizontal/global induction and the global five-support theorem.
