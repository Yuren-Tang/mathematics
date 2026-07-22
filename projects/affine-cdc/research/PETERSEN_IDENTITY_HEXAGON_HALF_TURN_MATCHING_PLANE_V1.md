# Petersen identity hexagons: half-turn defect and the canonical DDD matching plane

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `4fa36fa9238570a0eb62450eb141fc5b4c397a7b`  
**Parents:**

- `projects/affine-cdc/research/PETERSEN_IDENTITY_HEXAGON_HALF_DISCREPANCY_V1.md`;
- `projects/affine-cdc/research/SIX_OUTPUT_FULL_STATE_CYCLE_CORRECTION_V1.md`;
- `projects/affine-cdc/research/PHYSICAL_TRANSLATION_WORD_STOKES_V1.md`.

**Status:** exact support/affine decomposition for every Petersen identity hexagon. After comparison by the canonical support half-turn, the intrinsic algebraic residue lies in one canonical four-element DDD matching plane. Physical control of the half-turn semantic defect remains open.

**Not implied:** physical half-turn realisability, source-graph replacement, canonical acceptance, Lean verification, manuscript readiness, or the global five-support theorem.

---

## 1. Identity hexagon and its two involutions

Let

\[
C=(F_0,F_1,F_2,F_3,F_4,F_5,F_0)
\]

be a Petersen identity hexagon in the full state graph `L(P)`, where `P=KG(5,2)`.

The identity-hexagon theorem gives an omitted-index word

\[
(a,b,c,a,b,c)
\]

up to cyclic reindexing and reversal, and two three-transition half paths

\[
H_1:F_0\to F_1\to F_2\to F_3,
\qquad
H_2:F_3\to F_4\to F_5\to F_0.
\]

Both halves have the same support monodromy `sigma`, which is a transposition.

There is also a unique support half-turn `alpha` satisfying

\[
\alpha(F_j)=F_{j+3}\qquad(j\bmod 6).
\]

### Theorem 1.1 — disjoint-involution structure

For every Petersen identity hexagon,

\[
\boxed{\alpha\text{ and }\sigma\text{ are disjoint transpositions}.}
\]

Consequently

\[
\alpha\sigma=\sigma\alpha,
\]

and there is a unique support index `i` fixed by both while belonging to neither moved pair.

### Proof

The ten Petersen identity hexagons form one `S_5` orbit. For the representative

\[
(\{12,34\},\{12,35\},\{14,35\},\{14,23\},\{15,23\},\{15,34\})
\]

one has

\[
\alpha=(13),\qquad \sigma=(24),
\]

with common fixed index `5`. Conjugation by `S_5` preserves disjointness, commutation, and the number of common fixed indices. ∎

### Exact finite certificate

Enumeration of all seventy six-cycles of `L(P)` isolates the ten identity hexagons and verifies for every one:

- `alpha` and `sigma` both have cycle type `2 1^3`;
- their moved supports are disjoint;
- they commute;
- they have exactly one common fixed support index;
- `alpha sigma` has cycle type `2^2 1`.

---

## 2. The canonical matching plane

Write

\[
\alpha=(u\ v),\qquad \sigma=(x\ y),
\]

with disjoint moved pairs, and let `i` be the fifth support index.

Define the two disjoint roots

\[
r_\alpha=e_u+e_v,
\qquad
r_\sigma=e_x+e_y.
\]

Their sum is the co-root

\[
q_i=r_\alpha+r_\sigma=\mathbf 1+e_i.
\]

### Definition 2.1 — identity-hexagon matching plane

\[
\boxed{
M_C=\langle r_\alpha,r_\sigma\rangle
=\{0,r_\alpha,r_\sigma,q_i\}\subset E_5.
}
\]

The two roots form one Petersen-edge/DDD state; the third nonzero element is its associated co-root.

### Theorem 2.2 — image of the involution sum

On

\[
E_5=\{z\in\mathbf F_2^5:\sum_j z_j=0\},
\]

one has

\[
\boxed{\operatorname{Im}(\alpha+\sigma)=M_C.}
\]

### Proof

In characteristic two,

\[
\alpha+\sigma=(1+\alpha)+(1+\sigma).
\]

For a transposition `(u v)`,

\[
(1+\alpha)z=(z_u+z_v)r_\alpha,
\]

and similarly

\[
(1+\sigma)z=(z_x+z_y)r_\sigma.
\]

Hence the image is contained in `M_C`. The two coefficients may be prescribed independently, using the common fixed coordinate `i` to enforce the even-weight condition. Thus every element of `M_C` occurs. ∎

---

## 3. Affine half-turn defect

Suppose a physical realisation of the two half paths gives affine holonomies with common linear part `sigma` and translation parts

\[
z_1,z_2\in E_5.
\]

The complete identity-return displacement is

\[
d=z_2+\sigma z_1.
\]

### Definition 3.1 — half-turn semantic defect

\[
\boxed{\eta_C=z_2+\alpha z_1.}
\]

This measures the failure of the second physical half to equal the canonical support-half-turn image of the first.

### Theorem 3.2 — matching-plane decomposition

\[
\boxed{d=\eta_C+(\alpha+\sigma)z_1.}
\]

Therefore

\[
\boxed{d\in \eta_C+M_C,}
\qquad
\boxed{[d]_{E_5/M_C}=[\eta_C]_{E_5/M_C}.}
\]

### Proof

In characteristic two,

\[
z_2+\sigma z_1=(z_2+\alpha z_1)+(\alpha z_1+\sigma z_1).
\]

The first term is `eta_C`, and Theorem 2.2 places the second in `M_C`. ∎

---

## 4. Consequences

### Corollary 4.1 — physical half-turn realisation

If the physical source semantics respects the canonical half-turn,

\[
z_2=\alpha z_1,
\]

then

\[
\boxed{d\in M_C=\{0,r_\alpha,r_\sigma,q_i\}.}
\]

Thus the identity hexagon has only four intrinsic displacement classes: zero, either crossed root, or their co-root sum. There is no arbitrary four-dimensional flat translation residue.

### Corollary 4.2 — exact source of every quotient obstruction

Any displacement component outside `M_C` is exactly the physical half-turn semantic defect:

\[
[d]_{E_5/M_C}=[\eta_C]_{E_5/M_C}.
\]

Hence coefficient holonomy is not responsible for any quotient obstruction. Such an obstruction can arise only from source-graph semantics distinguishing the two coefficient-identical halves: side-component incidence, route order, root-fibre choice, or a regional separator.

### Corollary 4.3 — DDD triality interface

The three nonzero elements of `M_C` are one root/root/co-root triality:

\[
\{r_\alpha,r_\sigma,q_i\}.
\]

This has the same three-element shape as the nonzero triality code `H^1(K_{2,3};F_2)^×`. The present theorem supplies a canonical bounded matching plane; a functorial identification with the three physical repair channels remains to be proved.

---

## 5. Revised physical target

The identity-hexagon frontier is now a quotient statement, not a full equality problem.

It is enough to prove one of the following:

1. **half-turn compatibility:** `eta_C=0`;
2. **matching-plane compatibility:** `eta_C in M_C`;
3. **quotient obstruction alternative:** if `eta_C notin M_C`, then the failure forces route/profile escape, a smaller separator/common cut, or a bounded root-fibre defect.

The old target `z_1=z_2` was frame-dependent and stronger than necessary. The canonical target is control of

\[
[\eta_C]\in E_5/M_C,
\]

a two-dimensional quotient defect.

---

## 6. Position in the five-support proof

This theorem reconnects the previously flat identity-hexagon sector to the DDD architecture:

\[
\text{identity hexagon}
\longrightarrow
\text{half-turn semantic defect}
\longrightarrow
\text{canonical DDD matching plane}
\longrightarrow
\begin{cases}
0,\\
r_\alpha,\\
r_\sigma,\\
q_i,
\end{cases}
\]

provided the quotient defect is eliminated.

The remaining mathematical problem is physical/combinatorial rather than finite algebraic:

> compare the two coefficient-identical three-step halves through square, braid, or regional-Stokes moves, and show that any failure to realise the support half-turn already gives a strict source-side obstruction or descent.

This does not yet prove 5-CDC, but it reduces the identity sector from an unrestricted `E_5` translation problem to a two-dimensional quotient obstruction with a canonical DDD target.