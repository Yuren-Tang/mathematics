# Petersen identity hexagons and the half-discrepancy decomposition

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `e3a70b201f618923ab3d55a4bb908c1913171f09`  
**Parents:**

- `projects/affine-cdc/research/SIX_OUTPUT_FULL_STATE_CYCLE_CORRECTION_V1.md`;
- `projects/affine-cdc/research/PHYSICAL_TRANSLATION_WORD_STOKES_V1.md`;
- `projects/affine-cdc/research/PETERSEN_CYCLE_MONODROMY_V1.md`.

**Status:** exact support/combinatorial half-period theorem for the ten identity hexagons of `L(P)`, together with an exact affine decomposition of any physical realisation into one root-line norm term plus one half-semantic discrepancy. Equality of the two physical half translations remains open.  
**Not implied:** vanishing of the physical identity displacement, source-graph replacement, canonical acceptance, Lean verification, or the global five-support theorem.

---

## 1. Identity hexagon sector

Let

\[
P=KG(5,2)
\]

and let

\[
C=(F_0,F_1,F_2,F_3,F_4,F_5,F_0)
\]

be a simple six-cycle in `L(P)` whose six transition pivots are distinct.

The short-cycle correction theorem identifies exactly ten such cycles. They are the edge cycles induced by the ten simple six-cycles of the Petersen graph and form one `S5` orbit.

Their full support monodromy is identity.

---

## 2. Repeated omitted-index and side-root words

For a state `F`, let

\[
i(F)=[5]\setminus\bigcup F
\]

be its omitted support index. Write

\[
i_j=i(F_j).
\]

### Theorem 2.1 — doubled omitted word

For every Petersen identity hexagon there are three distinct support indices `a,b,c` such that, after cyclic reindexing and possible reversal,

\[
\boxed{
(i_0,i_1,i_2,i_3,i_4,i_5)
=(a,b,c,a,b,c).
}
\]

Consequently the emitted side-root word is two identical copies of one root triangle:

\[
\boxed{
(ab,bc,ca,ab,bc,ca)
}
\]

up to cyclic orientation.

### Representative

For

\[
C=(\{12,34\},\{12,35\},\{14,35\},\{14,23\},\{15,23\},\{15,34\}),
\]

one has

\[
(i_0,\ldots,i_5)=(5,4,2,5,4,2)
\]

and side word

\[
45,24,25,45,24,25.
\]

---

## 3. Equal half monodromies

Split the hexagon into the two three-transition paths

\[
H_1:F_0\to F_1\to F_2\to F_3,
\]

\[
H_2:F_3\to F_4\to F_5\to F_0.
\]

Let their support monodromies be

\[
\sigma_1,
\qquad
\sigma_2.
\]

### Theorem 3.1 — half-period support theorem

\[
\boxed{
\sigma_1=\sigma_2=\sigma,
}
\]

where `sigma` is a single transposition. Hence

\[
\sigma^2=1
\]

and the full support monodromy is identity.

### Proof

The omitted-index word of each half is the same cyclic triple

\[
a,b,c,a.
\]

Therefore each half has the same product

\[
(c\ a)(b\ c)(a\ b),
\]

which is a transposition. Squaring gives identity. ∎

### Representative

For the displayed hexagon,

\[
\sigma=(2\ 4).
\]

---

## 4. Unique support half-turn

### Theorem 4.1 — half-turn symmetry

For every identity hexagon there is a unique support permutation

\[
\alpha\in S_5
\]

such that

\[
\boxed{
\alpha(F_j)=F_{j+3}
\qquad(j\bmod6).
}
\]

The permutation `alpha` has order two. It exchanges the two equal coefficient halves of the state cycle.

For the representative,

\[
\alpha=(1\ 3).
\]

The half-turn `alpha` need not equal the half-path monodromy `sigma`; in the representative `alpha=(13)` and `sigma=(24)`.

Thus support symmetry of the state cycle and transport along one half are distinct pieces of data.

---

## 5. Affine half holonomies

Suppose a physical realisation of the two half paths gives affine holonomies

\[
A_1=(\sigma,z_1),
\qquad
A_2=(\sigma,z_2)
\]

in the relevant coefficient module `M`.

With the semidirect-product convention

\[
(\mu,g)(\nu,h)=(\mu+g\nu,gh),
\]

the full identity-return hexagon has translation

\[
\boxed{
d=z_2+\sigma z_1.}
\]

Define the **half-semantic discrepancy**

\[
\boxed{
\varepsilon=z_2+z_1.
}
\]

### Theorem 5.1 — half-discrepancy decomposition

\[
\boxed{
 d
 =
 \varepsilon
 +(1+\sigma)z_1.
}
\]

The second summand is a cyclic norm term; the first is the difference between two half paths having identical support and side-root words.

### Proof

In characteristic two,

\[
z_2+\sigma z_1
=(z_2+z_1)+(z_1+\sigma z_1).
\]

This is exactly the displayed formula. ∎

---

## 6. The root-line norm

Let the half monodromy be the transposition

\[
\sigma=(u\ v).
\]

On the even support module `E5`,

\[
\operatorname{Im}(1+\sigma)
=\langle e_u+e_v\rangle.
\]

### Theorem 6.1 — root-line confinement

For every coefficient `z`,

\[
\boxed{
(1+\sigma)z
\in
\{0,e_u+e_v\}.
}
\]

Thus, if the two physical half translations agree,

\[
\varepsilon=0,
\]

then the complete identity-hexagon displacement is either zero or one root:

\[
\boxed{
 d\in\{0,e_u+e_v\}.
}
\]

### Interpretation

- `d=0` is the removable/flat-zero branch;
- a nonzero root displacement selects one bounded matching/Type-T direction;
- no co-root or arbitrary four-bit displacement can arise from the norm term alone.

---

## 7. The exact remaining physical datum

The two halves have:

- the same support monodromy `sigma`;
- the same omitted-index word;
- the same three emitted side roots in the same order;
- `S5`-equivalent state paths under the unique half-turn `alpha`.

Therefore every contribution to

\[
\varepsilon=z_2+z_1
\]

comes from physical source semantics not determined by the coefficient word itself: side-component incidence, route order, local root-fibre choices, or regional attachment data.

### Corollary 7.1 — minimal identity Stokes comparator

The Petersen identity hexagon is the smallest bounded identity-return cell in which the physical translation theorem reduces to comparison of two coefficient-identical three-step halves.

The source-graph task is no longer to classify an arbitrary identity word. It is to prove one of:

1. **half agreement:** `epsilon=0`, giving zero or root-line displacement;
2. **weight-two descent:** the root-line value is nonzero and feeds one matching/Type-T reduction;
3. **order discrepancy:** the two halves differ by a square/braid side-order move already isolated in the finite Stokes programme;
4. **separator/common cut:** the side-component mismatch producing `epsilon` localises to a bounded cut;
5. **root-fibre defect:** one half fails by an empty fibre or relation.

---

## 8. Relation to the affine translation hexagons

The affine-`A3` frame theorem reduces all identity-return words to three six-step translation generators plus square and braid cells.

The Petersen identity hexagons have exactly the same bounded length and the same identity support return. The present theorem does not yet identify each Petersen hexagon with one standard affine-`A3` generator.

The correct comparison target is:

\[
\boxed{
\text{Petersen half discrepancy }\varepsilon
\quad\longleftrightarrow\quad
\text{physical side-order/Stokes discrepancy}.
}
\]

Once this comparison is proved, the root-line norm gives the frame translation component and `epsilon` is accounted for by bounded regional cells.

---

## 9. Wolfram certificate

Exact enumeration of all ten identity hexagons verifies:

- both three-step half monodromies are equal;
- their common cycle type is `2 1^3`;
- the two three-root side words are identical;
- each hexagon has exactly one support permutation mapping state `j` to state `j+3`;
- the full support monodromy is identity.

There are no exceptional hexagons.

---

## 10. Trust boundary

### Exact here

- the doubled omitted-index word `abcabc`;
- repetition of the side-root triangle;
- equality and transposition type of the two half monodromies;
- uniqueness of the support half-turn;
- the affine formula `d=z2+sigma z1`;
- the decomposition into half discrepancy plus root-line norm;
- one-dimensional root confinement of `Im(1+sigma)`.

### Still open

- equality `z1=z2` for actual source realisations;
- identification of `epsilon` with the established square/braid/regional Stokes cells;
- conversion of nonzero root displacement into strict graph descent;
- source-incidence-preserving replacement and separator transfer;
- horizontal induction and the global five-support theorem.
