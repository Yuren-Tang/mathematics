# Affine A3 translation parity and the four-challenge flat code

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Parents:**

- `projects/affine-cdc/research/OCTAHEDRAL_AFFINE_A3_KERNEL_V1.md`;
- `projects/affine-cdc/research/OCTAHEDRAL_CURVATURE_NORMAL_FORM_V1.md`;
- active corpus route-lock/flat-potential theorem.

**Status:** exact finite representation/code theorem; the physical chain map from overlap translations to locked side-choice words remains open.  
**Not implied:** canonical acceptance, independent audit, Lean verification, manuscript readiness, or the global five-support theorem.

---

## 1. The mod-two translation lattice

Let

\[
Q(A_3)
=
\left\{
(m_1,m_2,m_3,m_4)\in\mathbf Z^4:
\sum_{i=1}^4m_i=0
\right\}.
\]

Reduction modulo two gives:

### Theorem 1.1

\[
\boxed{
Q(A_3)/2Q(A_3)
\cong
E_4
:=
\left\{
\varepsilon\in\mathbf F_2^4:
\sum_{i=1}^4\varepsilon_i=0
\right\}.
}
\]

The isomorphism is equivariant for the natural `S4` action permuting the four coordinates.

### Proof

Every root-lattice vector has even coordinate sum modulo two, giving a map into `E4`. The simple roots

\[
e_2-e_1,
\qquad
e_3-e_2,
\qquad
e_4-e_3
\]

reduce to three independent vectors in `E4`, so the map is surjective. Both spaces have dimension three over `F2`.

### Interpretation

The three integral translation directions in the octahedral affine-Weyl kernel become one canonical three-dimensional binary module. This is the finite residue that remains after local Coxeter moves and before graph-level flat-potential integration.

---

## 2. Affine functions on the four-point plane

Let

\[
\Lambda\cong AG(2,2)
\]

be a four-point affine plane. Write

\[
\mathbf F_2^\Lambda
\]

for all four-bit functions on its points, and let

\[
\operatorname{Aff}(\Lambda,\mathbf F_2)
\]

be the affine Boolean functions.

### Theorem 2.1 — affine code equals the even code

\[
\boxed{
\operatorname{Aff}(AG(2,2),\mathbf F_2)
=
\left\{
f\in\mathbf F_2^\Lambda:
\sum_{x\in\Lambda}f(x)=0
\right\}.
}
\]

Thus the first-order Reed--Muller code on four points is exactly the length-four even-weight code.

### Proof

There are eight affine functions on `F2^2`, so the affine code has dimension three. The zero and one constants have weights zero and four. Every nonconstant affine function is a nonzero linear function or its complement and has weight two. Hence every affine word has even weight. The even code also has dimension three, so the inclusion is equality.

### Equivariance

The affine automorphism group

\[
\operatorname{AGL}(2,2)\cong S_4
\]

acts as the complete permutation group of the four points and preserves this code. Therefore the identification with `E4` is `S4`-equivariant.

---

## 3. Translation/flat-code identification

Choose the natural four-point identification supplied by the local locked four-challenge plane. Combining Theorems 1.1 and 2.1 gives:

### Theorem 3.1 — rank-three bridge

\[
\boxed{
Q(A_3)/2Q(A_3)
\cong
\operatorname{Aff}(\Lambda,\mathbf F_2).
}
\]

Under this identification, the parity class of an affine-Weyl translation is exactly an affine four-bit word on the challenge plane.

This is stronger than a dimension coincidence: both sides are the same natural `S4` permutation submodule of the four-bit function space.

### D8 form

After fixing the bad matching, the DDD stabiliser `D8` preserves:

- the four affine simple/cross-root directions of the `A~3` cycle;
- the four locked challenges;
- the even/affine subcode.

Hence the bridge remains equivariant under the actual local stabiliser used by the DDD atom.

---

## 4. The unique curvature quotient

The total parity map gives a short exact sequence

\[
\boxed{
0
\longrightarrow
Q(A_3)/2Q(A_3)
\longrightarrow
\mathbf F_2^\Lambda
\xrightarrow{\;\operatorname{curv}\;}
\mathbf F_2
\longrightarrow0,
}
\]

where

\[
\operatorname{curv}(f)
=
\sum_{x\in\Lambda}f(x).
\]

Equivalently,

\[
\boxed{
0
\longrightarrow
\operatorname{Aff}(\Lambda,\mathbf F_2)
\longrightarrow
\mathbf F_2^\Lambda
\longrightarrow
\mathbf F_2
\longrightarrow0.
}
\]

### Consequence 4.1

There is exactly one non-affine coset of four-bit challenge words. It is detected by odd total parity.

This is the finite code-theoretic form of the active corpus statement that the parity of the four side bits is the unique non-affine function on `AG(2,2)`.

---

## 5. DDD curvature versus identity translations

The preceding octahedral dossiers give two finite mechanisms:

1. an odd octahedral return carries one triangular DDD curvature cell;
2. an identity-holonomy remainder lies in the affine `A3` translation kernel.

The code theorem now separates them canonically at the binary level.

### Theorem 5.1 — finite flat/curvature dichotomy

After mod-two reduction:

\[
\boxed{
\text{identity translation residue}
\in
\operatorname{Aff}(\Lambda,\mathbf F_2),
}
\]

whereas the scalar DDD curvature occupies the unique odd/non-affine quotient

\[
\boxed{
\mathbf F_2^\Lambda/
\operatorname{Aff}(\Lambda,\mathbf F_2)
\cong\mathbf F_2.
}
\]

Thus the rank-three flat part and the one-bit DDD curvature are the kernel and cokernel of one four-bit exact sequence.

### Trust boundary

This theorem identifies the finite modules. It does not yet prove that a physical overlap translation produces the same four-bit word as the locked side-choice construction. That requires a chain-level comparison respecting side components, cuts, and terminal semantics.

---

## 6. Candidate physical chain map

Let a physical identity-holonomy overlap word determine an affine-Weyl translation

\[
t_\mu,
\qquad
\mu\in Q(A_3).
\]

The required comparison map should have the form

\[
\Theta_{\mathrm{phys}}:
Q(A_3)
\longrightarrow
\mathbf F_2^\Lambda,
\]

and satisfy:

1. `Theta_phys` depends only on the physical overlap region and its four challenge sheets;
2. reduction modulo two factors through `Q(A3)/2Q(A3)`;
3. the reduced image is the affine word corresponding to `mu mod 2` under Theorem 3.1;
4. boundary summation of physical regions maps to addition of challenge words;
5. an odd octahedral curvature cell maps to the non-affine coset rather than to the translation kernel.

If these properties hold, the existing flat-potential theorem would integrate every identity-translation residue, while nonzero curvature would return to the common-cut/DDD branch.

---

## 7. Revised proof target

The finite comparison is complete. The next theorem is no longer “explain the repeated rank three”. It is:

### Target 7.1 — physical translation word theorem

Construct `Theta_phys` directly from the side-root attachments of an overlap word and prove that the three explicit translation hexagons map to a basis of the affine four-bit code.

### Target 7.2 — regional exactness

For a physical region tiled by overlap cells, prove

\[
\operatorname{curv}(\Theta_{\mathrm{phys}}(\partial R))
=
\sum_{F\subset R}\kappa(F).
\]

This would be the graph-level Stokes map joining:

- octahedral face curvature;
- affine-Weyl translations;
- locked four-challenge parity;
- the flat vertex potential.

### Target 7.3 — composition

Use the existing flat-potential equivalence to turn a zero-curvature translation word into one of:

- a serial/gauge reduction;
- a bounded four-pole interface;
- a zero-equality or defect-forest unit;
- an augmenting profile switch.

---

## 8. Trust boundary

### Exact here

- `Q(A3)/2Q(A3)` as the even four-coordinate module;
- the equality of affine Boolean words on `AG(2,2)` with the even code;
- the `S4`-equivariant rank-three identification;
- the short exact flat-code/curvature sequence;
- the finite algebraic separation of identity translations from the unique curvature coset.

### Still open

- the physical chain map from overlap translations to challenge words;
- regional Stokes compatibility in the source graph;
- use of the flat potential for strict source reduction;
- Type T strict descent, Type H closure, horizontal/global induction, and the global five-support theorem.
