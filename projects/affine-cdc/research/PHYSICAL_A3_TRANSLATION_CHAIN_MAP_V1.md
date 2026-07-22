# The physical curvature-side chain is exactly the affine `A3` translation word

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `12d76d7f632a6616b7e4c9997af45391ee23102c`.

**Parents:**

- `OCTAHEDRAL_OVERLAP_TRANSPORT_V1.md`;
- `OCTAHEDRAL_AFFINE_A3_KERNEL_V1.md`;
- `AFFINE_A3_FLAT_CODE_BRIDGE_V1.md`;
- `PHYSICAL_TRANSLATION_WORD_STOKES_V1.md`;
- `ROUTE_LOCKED_QUOTIENT_PHASE.md` / `five-support/route-locked-quotient-phase.md`;
- `PHYSICAL_TRANSLATION_CELL_ANALYSIS_V1.md`.

**Status:** exact physical chain-map theorem. In a chosen affine `A3` frame, only occurrences of the affine generator `s0` contribute to the root-lattice translation cocycle. At such an occurrence the mod-two translation increment is exactly the actual physical side-root emitted by the overlap transport. Summing those distinguished side roots gives a canonical physical curvature-side chain `C_phys(w)`. For each of the four locked scalar challenges, the parity with which its scalar sheet contains the distinguished side edges is evaluation on `C_phys(w)`. The affine-Weyl cocycle formula gives `C_phys(w)=bar mu(w)`, hence the actual four-challenge physical word equals the previously defined frame translation word for every identity-return overlap word. This closes the missing flat translation comparison map, not merely its three generator cases.

**Not implied:** automatic serial contraction of every weight-two word, physical triviality of the constant-one class, torsor-valued treatment of odd curvature with arbitrary side attachments, final rank-three source reduction, global five-support theorem, canonical acceptance, independent audit, Lean verification, manuscript integration, release, or publication.

---

## 1. Affine frame convention

Use the standard affine `A3` generators

\[
s_1=(12),\qquad s_2=(23),\qquad s_3=(34),
\]

and the affine reflection `s0`, whose finite linear part is

\[
(14)
\]

and whose translation increment is

\[
\theta=e_1-e_4\in Q(A_3).
\]

Modulo two,

\[
\boxed{\bar\theta=e_1+e_4=14,}
\]

viewed as a root edge on the four active support names.

Let

\[
w=s_{i_1}s_{i_2}\cdots s_{i_n}
\]

be one physical overlap frame word. Write

\[
g_k\in S_4
\]

for the finite frame after the first `k` letters, with `g_0=1`.

At the `k`-th step the physical side-root output is

\[
r_k=g_{k-1}(\rho(s_{i_k})),
\]

where the root attached to a finite generator is its transposition edge. In particular, when

\[
i_k=0,
\]

the actual side root is

\[
\boxed{r_k=g_{k-1}(14)=g_{k-1}(\bar\theta).}
\]

---

## 2. The physical curvature-side chain

### Definition 2.1

For any overlap frame word `w`, define

\[
\boxed{
C_{\mathrm{phys}}(w)
=
\sum_{k:\,i_k=0} r_k
\in E_4.
}
\]

The sum is mod two. Thus only the physical side edges emitted at affine-generator occurrences are retained.

This definition is source-side:

- each `r_k` is an actual root label of a physical side edge;
- the selected occurrences are exactly the local affine-curvature crossings in the chosen frame;
- changing the global support frame acts simultaneously on all selected roots.

### Theorem 2.2 — chain equals translation

Let

\[
\mu(w)\in Q(A_3)
\]

be the affine translation part of `w`. Then

\[
\boxed{
C_{\mathrm{phys}}(w)=\bar\mu(w)
\in Q(A_3)/2Q(A_3)\cong E_4.
}
\]

### Proof

The affine cocycle formula is

\[
\mu(w)
=
\sum_{k:\,i_k=0}g_{k-1}\theta.
\]

Reducing modulo two gives

\[
\bar\mu(w)
=
\sum_{k:\,i_k=0}g_{k-1}\bar\theta.
\]

At every selected step,

\[
g_{k-1}\bar\theta=r_k
\]

is precisely the physical side-root output. Summing gives the result. ∎

---

## 3. Four locked challenges

Let the terminal colour be

\[
0\ne g\in V\cong\mathbf F_2^3
\]

and let

\[
\Lambda_g
=
\{\lambda\in V^*:\lambda(g)=1\}
\cong AG(2,2)
\]

be the four locked scalar challenges.

For one challenge `lambda`, its scalar relative even subgraph is

\[
H_\lambda
=
\{e:\lambda(c(e))=1\}.
\]

Therefore an actual side edge of root value `r` belongs to `H_lambda` exactly when

\[
\lambda(r)=1.
\]

### Definition 3.1 — actual physical challenge word

For an identity-return overlap word `w`, define

\[
\boxed{
B_{\mathrm{phys}}(w)(\lambda)
=
\sum_{k:\,i_k=0}\lambda(r_k)
\qquad(\lambda\in\Lambda_g).
}
\]

Equivalently, `B_phys(w)(lambda)` is the parity with which the scalar sheet `H_lambda` contains the distinguished curvature-side edges of the physical overlap word.

This is a four-bit function on the actual locked challenge plane.

---

## 4. Exact comparison theorem

The finite affine translation word is

\[
\Theta_{\mathrm{fr}}(w)
\in
\operatorname{Aff}(\Lambda_g,\mathbf F_2),
\]

defined by evaluating the mod-two translation vector:

\[
\Theta_{\mathrm{fr}}(w)(\lambda)
=
\lambda(\bar\mu(w)).
\]

### Theorem 4.1 — physical translation comparison

For every identity-transport physical overlap word,

\[
\boxed{
B_{\mathrm{phys}}(w)
=
\Theta_{\mathrm{fr}}(w).
}
\]

### Proof

For every `lambda in Lambda_g`,

\[
\begin{aligned}
B_{\mathrm{phys}}(w)(\lambda)
&=
\sum_{k:\,i_k=0}\lambda(r_k)\\
&=
\lambda\left(\sum_{k:\,i_k=0}r_k\right)\\
&=
\lambda(C_{\mathrm{phys}}(w))\\
&=
\lambda(\bar\mu(w))\\
&=
\Theta_{\mathrm{fr}}(w)(\lambda).
\end{aligned}
\]

Theorem 2.2 gives the fourth equality. ∎

### Corollary 4.2 — image is the affine/even code

\[
\boxed{
B_{\mathrm{phys}}(w)
\in
\operatorname{Aff}(\Lambda_g,\mathbf F_2)
=
\{b\in\mathbf F_2^4:\sum b=0\}.
}
\]

Thus an identity-return physical overlap cannot produce the odd/non-affine curvature coset. Odd curvature remains a torsor branch represented by one bounded DDD face core.

---

## 5. Additivity and frame covariance

### Theorem 5.1 — concatenation law

For identity-transport words `u,v`,

\[
\boxed{
C_{\mathrm{phys}}(uv)
=C_{\mathrm{phys}}(u)+C_{\mathrm{phys}}(v),
}
\]

and

\[
\boxed{
B_{\mathrm{phys}}(uv)
=B_{\mathrm{phys}}(u)+B_{\mathrm{phys}}(v).
}
\]

### Proof

The finite frame at the end of `u` is the initial frame, so the selected physical roots in `v` are read in the same frame. Alternatively use the affine cocycle law and Theorem 2.2. Evaluation is linear. ∎

### Theorem 5.2 — `S4` covariance

Changing the active support frame by

\[
h\in S_4
\]

sends

\[
C_{\mathrm{phys}}(w)
\longmapsto
hC_{\mathrm{phys}}(w)
\]

and transports the challenge word by the corresponding affine permutation of `Lambda_g`.

Hence the equality `B_phys=Theta_fr` is independent of the chosen standard coordinate frame.

---

## 6. Coxeter cell invariance

### Backtrack

A consecutive `s_i s_i` has zero affine translation. Its two selected curvature-side contributions, if `i=0`, are equal and cancel. Thus

\[
B_{\mathrm{phys}}(s_i^2)=0.
\]

### Commuting square

For disjoint generators `s,t`, the two words `st` and `ts` have the same affine group element. Therefore their physical curvature chains agree after identifying the endpoints:

\[
C_{\mathrm{phys}}(st)=C_{\mathrm{phys}}(ts).
\]

The side-root order may reverse, but the four challenge parities are unchanged.

### Braid

For adjacent generators,

\[
sts=tst
\]

in the affine Weyl group. Hence

\[
C_{\mathrm{phys}}(sts)=C_{\mathrm{phys}}(tst)
\]

and the corresponding challenge words agree. The physical three-side-root order reversal does not change the distinguished curvature-side parity.

### Corollary 6.1

The physical word is invariant under the bounded backtrack, square, and braid relations required by the affine-kernel generator theorem.

No separate enumeration of their challenge words is necessary.

---

## 7. Translation generators

The three translation hexagons have physical side-root words

\[
\begin{aligned}
u_1&:(12,13,14,12,24,23),\\
u_2&:(23,13,24,23,34,12),\\
u_3&:(34,24,14,34,13,23).
\end{aligned}
\]

Each contains one affine-generator occurrence. Its distinguished physical side root is respectively

\[
12,\qquad23,\qquad34.
\]

Therefore

\[
\boxed{
C_{\mathrm{phys}}(u_1)=12,
\quad
C_{\mathrm{phys}}(u_2)=23,
\quad
C_{\mathrm{phys}}(u_3)=34.
}
\]

These are exactly

\[
1100,\qquad0110,\qquad0011
\]

in the even four-coordinate code and form a basis.

### Corollary 7.1 — bounded generator calibration

The three physical translation cells realise the three basis words of the affine challenge code. Together with Section 6, the finite generator criterion independently recovers Theorem 4.1 for all identity-return words.

---

## 8. Flat-class consequences

By the evaluation classification, exactly three physical identity-return types occur.

### Zero

\[
C_{\mathrm{phys}}(w)=0
\quad\Longleftrightarrow\quad
B_{\mathrm{phys}}(w)=0000.
\]

### Global complement

\[
C_{\mathrm{phys}}(w)=g
\quad\Longleftrightarrow\quad
B_{\mathrm{phys}}(w)=1111.
\]

### Matching class

If

\[
C_{\mathrm{phys}}(w)=v\notin\{0,g\},
\]

then `B_phys(w)` has weight two. Modulo global complement, the classes `v` and `v+g` determine one of the three terminal matching directions.

The exact source-side difference object of that matching is the closed quotient Kempe system

\[
H_{\delta_v}
\]

from `PHYSICAL_TRANSLATION_CELL_ANALYSIS_V1.md`.

Thus the finite affine translation lattice, the actual physical challenge bits, and the scalar matching direction are now canonically the same object.

---

## 9. Regional Stokes

For a physical region tiled by overlap cells, define the curvature-side chain by summing the transported distinguished side roots of all affine-curvature crossings. Internal selected side incidences occur twice and cancel when two regions are glued.

Hence boundary summation gives:

### Theorem 9.1 — physical mod-two Stokes

For every finite identity-curvature physical region `R`,

\[
\boxed{
C_{\mathrm{phys}}(\partial R)
=
\sum_{F\subset R}C_{\mathrm{phys}}(F),
}
\]

and after evaluation on the challenge plane,

\[
\boxed{
B_{\mathrm{phys}}(\partial R)
=
\sum_{F\subset R}B_{\mathrm{phys}}(F).
}
\]

For odd curvature, choosing one bounded DDD face core supplies an affine origin of the odd torsor; changing the chosen core changes the remainder by the flat word given above. No canonical absolute odd representative is asserted.

---

## 10. Consequence for the rank-three frontier

The missing physical comparison map from the affine `A3` translation lattice to locked four-challenge side words now exists and is explicit:

\[
\boxed{
Q(A_3)/2Q(A_3)
\xrightarrow{\;C_{\mathrm{phys}}\;}
E_4
\xrightarrow{\;\mathrm{evaluation}\;}
\operatorname{Aff}(\Lambda_g,\mathbf F_2).
}
\]

It agrees with the finite frame map and with the actual scalar-sheet incidences.

The remaining rank-three work is no longer identification of the repeated rank-three modules. It is physical consumption of the three exact output classes:

1. `0000`: removable identity/gauge class;
2. `1111`: global-complement/common-cut class;
3. weight two: the canonical closed scalar component system `H_(delta_v)` and its serial/four-pole/escape alternatives;
4. odd curvature: one bounded DDD torsor core plus a flat remainder.

---

## 11. Trust boundary

### Exact here

- physical curvature-side chain `C_phys`;
- equality `C_phys=bar mu`;
- actual scalar-sheet definition of `B_phys`;
- theorem `B_phys=Theta_fr` for every identity-return word;
- additivity and `S4` covariance;
- backtrack/square/braid invariance;
- exact three-generator side-root calibration;
- physical mod-two Stokes in the flat identity sector;
- canonical match between weight-two translation classes and scalar matching directions.

### Still open

- source reduction for every zero/constant-one/weight-two physical class;
- composition-safe separation of one odd DDD torsor core from its flat remainder;
- strict serial or four-pole descent for every pair-preserving scalar component;
- integration with the hyperbolic dual-rank-three carrier and prime cap response;
- reverse proof-DAG audit and global theorem packaging;
- canonical acceptance, independent audit, Lean verification, manuscript integration, release, publication;
- the global five-support theorem.
