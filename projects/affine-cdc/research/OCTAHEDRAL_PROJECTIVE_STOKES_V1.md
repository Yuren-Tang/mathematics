# Projective octahedral Stokes map and canonical matching residue

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Standing input head:** `034bf45d76d89a667cc3e7503e7d3b16047bd117`  
**Parents:**

- `projects/affine-cdc/research/OCTAHEDRAL_CURVATURE_NORMAL_FORM_V1.md`;
- `projects/affine-cdc/research/OCTAHEDRAL_AFFINE_A3_KERNEL_V1.md`;
- `projects/affine-cdc/research/FLAT_TRANSLATION_TRIALITY_V1.md`.

**Status:** exact finite state-space Stokes theorem modulo global complement; physical source-graph pullback and the remaining complement bit are open.  
**Not implied:** canonical acceptance, independent audit, Lean verification, manuscript readiness, or the global five-support theorem.

---

## 1. The indexed octahedral faces

Let

\[
\mathcal O=L(K_4)
\]

be the octahedral overlap-state graph. Its six vertices are the edges of a four-set

\[
I=\{1,2,3,4\}.
\]

The eight triangular faces split into two natural `S4`-orbits. For `i in I`, define

\[
S_i=\{ij:j\in I\setminus\{i\}\},
\]

the star face at `i`, and

\[
T_i=E(K_{I\setminus\{i\}}),
\]

the triangle face on the complementary three-set.

The faces `S_i` and `T_i` are opposite faces of the octahedron. Thus the eight faces are naturally indexed by

\[
I\times\{S,T\}.
\]

The `S4` action permutes the index `i` and preserves the two face orbits.

---

## 2. The projective four-bit module

Let

\[
M=\mathbf F_2^I
\]

with standard basis `e_i`, and let

\[
\mathbf 1=\sum_{i\in I}e_i.
\]

Define the projective challenge module

\[
\overline M=M/\langle\mathbf1\rangle.
\]

Because `|I|=4`, total parity descends to a well-defined map

\[
\operatorname{par}:\overline M\to\mathbf F_2,
\qquad
\operatorname{par}([x])=\sum_i x_i.
\]

Indeed, adding `mathbf1` changes weight by four and hence preserves parity.

### Definition 2.1 — face label

Assign to both opposite faces with index `i` the same projective label

\[
\boxed{
\varphi(S_i)=\varphi(T_i)=\overline e_i.
}
\]

This assignment is `S4`-equivariant and does not require choosing which face orbit is the positive or negative side convention.

---

## 3. Filling independence

Let

\[
D\in C_2(\mathcal O;\mathbf F_2)
\]

be a mod-two set of triangular faces. Put

\[
\Phi(D)=\sum_{F\subset D}\varphi(F)
\in\overline M.
\]

### Theorem 3.1 — projective filling independence

If `D` and `D'` have the same boundary, then

\[
\boxed{
\Phi(D)=\Phi(D').
}
\]

### Proof

The octahedral two-sphere has one nonzero mod-two two-cycle, namely the sum `Sigma` of all eight faces. The two faces `S_i,T_i` occur once for each `i`, hence

\[
\Phi(\Sigma)
=\sum_{i\in I}(\overline e_i+\overline e_i)
=0.
\]

Therefore adding the full sphere to a filling does not change `Phi`.

### Definition 3.2 — projective Stokes word

For a closed octahedral state walk `gamma`, choose any face filling `D` with

\[
\partial D=\gamma
\]

and define

\[
\boxed{
\overline\Theta_{\mathcal O}(\gamma)=\Phi(D).
}
\]

Theorem 3.1 makes this independent of the filling.

The map is additive under mod-two sum of state cycles.

---

## 4. Scalar curvature shadow

Every face label has odd parity:

\[
\operatorname{par}(\overline e_i)=1.
\]

Hence:

### Theorem 4.1 — projective regional Stokes law

For every closed state walk `gamma` and every filling `D`,

\[
\boxed{
\operatorname{par}
\bigl(\overline\Theta_{\mathcal O}(\gamma)\bigr)
=|D|\pmod2.
}
\]

By the octahedral area-parity theorem,

\[
|D|\equiv\kappa(\pi_\gamma)\pmod2,
\]

so

\[
\boxed{
\operatorname{par}
\bigl(\overline\Theta_{\mathcal O}(\gamma)\bigr)
=\kappa(\pi_\gamma).
}
\]

Thus the internal-twist curvature is the scalar quotient of one vector-valued projective Stokes word.

---

## 5. Bounded cells

### 5.1 Doubled face

Traversing one triangular face twice gives zero in mod-two state homology. Equivalently, the same face label occurs twice:

\[
\boxed{
\overline\Theta_{\mathcal O}(2F)=0.
}
\]

This is the projective shadow of the braid/doubled-face Coxeter relation.

### 5.2 Equatorial square

An equatorial square separates the octahedral sphere into two four-face hemispheres. In either hemisphere the four face indices are exactly the four elements of `I`, once each. Therefore

\[
\overline\Theta_{\mathcal O}(\square)
=\sum_{i\in I}\overline e_i
=\overline{\mathbf1}
=0.
\]

Hence

\[
\boxed{
\text{every equatorial flat square has zero projective Stokes word.}
}
\]

The full four-bit lift may still differ by the global-complement word `1111`; visible octahedral geometry cannot distinguish that central bit.

### 5.3 Paired curvature cells

Suppose an identity-transport hexagon decomposes into two distinct triangular faces with indices `i` and `j`. Then

\[
\boxed{
\overline\Theta_{\mathcal O}(\gamma)
=\overline e_i+\overline e_j.
}
\]

This has even parity and determines the unordered partition

\[
\{i,j\}\mid I\setminus\{i,j\}.
\]

Complementary pairs define the same class because

\[
\overline e_i+\overline e_j
=\sum_{k\notin\{i,j\}}\overline e_k.
\]

Therefore a paired-curvature translation cell canonically selects one of the three perfect matchings of the four challenge points.

---

## 6. Agreement with affine `A3` matching triality

The identity-transport kernel of the full frame lift is

\[
Q(A_3)\cong\mathbf Z^3.
\]

After mod-two reduction and quotient by the global-complement direction, the previous flat-translation theorem gives

\[
Q(A_3)/(2Q(A_3)+\langle\mathbf1\rangle)
\cong\mathbf F_2^2.
\]

The three nonzero elements are the three perfect matchings of the four challenge points.

### Theorem 6.1 — projective translation identification

Restricted to identity-transport words, the projective Stokes map factors through

\[
Q(A_3)/(2Q(A_3)+\langle\mathbf1\rangle)
\]

and is the matching-triality identification.

### Proof

The complete word presentation of the identity kernel is generated by:

1. backtracks;
2. commuting squares;
3. doubled-face braid cells;
4. three paired-curvature translation hexagons.

The first three families map to zero by Section 5. Each translation hexagon maps to the two-point class of its two face indices. The three translation directions generate `Q(A3)`, and their two-point classes generate the two-dimensional matching quotient. Hence the induced map is exactly the projective translation quotient.

### Consequence 6.2

The visible octahedral state word already determines the support-unordered matching residue of an identity-holonomy period. Full frame/side data are needed only to decide the remaining central complement bit.

---

## 7. Curvature and flat sectors in one projective module

The parity decomposition of `overline M` gives:

- even classes:
  \[
  E_4/\langle\mathbf1\rangle\cong\mathbf F_2^2,
  \]
  the three matching directions plus zero;
- odd classes: the affine coset detected by nonzero DDD curvature.

Thus:

\[
\boxed{
\text{even projective Stokes word}
\Longleftrightarrow
\text{flat matching sector},
}
\]

and

\[
\boxed{
\text{odd projective Stokes word}
\Longleftrightarrow
\text{DDD curvature sector}.
}
\]

This is a vector-valued refinement of the scalar octahedral Gauss law, canonical modulo the global-complement convention.

---

## 8. What remains physical

The finite regional Stokes problem is now closed modulo global complement. The source-graph problem splits into two bounded obligations.

### Target 8.1 — physical pullback

For a physical overlap region with state word `gamma`, construct its four scalar-sheet side monodromy and prove that its image in

\[
\mathbf F_2^I/\langle\mathbf1\rangle
\]

equals

\[
\overline\Theta_{\mathcal O}(\gamma).
\]

Failure of a local face or square comparison should expose a bounded order obstruction, smaller separator, or DDD/defect unit.

### Target 8.2 — complement-bit dichotomy

After Target 8.1, the only undetermined part of the full four-bit physical word is the constant word `1111`. Prove that it is either:

1. removable by a separated `g`-potential gauge;
2. represented by an all-four-sheet common cut;
3. or localised to a bounded DDD/defect interface.

### Target 8.3 — matching-to-routing theorem

For an even nonzero projective word, prove that its selected perfect matching is the same matching realised by the physical four-pole routing automaton. Then obtain serial/Type-T descent or a bounded four-pole separator.

---

## 9. Trust boundary

### Exact here

- the natural indexing of octahedral faces by `I x {S,T}`;
- the `S4`-equivariant projective face label;
- filling independence;
- the vector-valued projective Stokes theorem;
- recovery of scalar DDD curvature by parity;
- vanishing on equatorial squares and doubled faces;
- matching classes from paired-curvature cells;
- identification with affine-`A3` translation triality modulo global complement.

### Still open

- equality with physical scalar-sheet side monodromy;
- physical gauge treatment of the `1111` complement bit;
- conversion of a matching class into strict serial/four-pole source reduction;
- horizontal/global induction and the global five-support theorem.
