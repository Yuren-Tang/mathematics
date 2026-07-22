# Functoriality correction for equality-lock root rigidity

## Research correction v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `9a3c9df3fdccea46d8c630200f764e522e49dc12`  
**Corrected source:** `projects/affine-cdc/research/EQUALITY_LOCK_S5_ROOT_RIGIDITY_V1.md`.

---

## 1. Correction

The dossier `EQUALITY_LOCK_S5_ROOT_RIGIDITY_V1.md` correctly identifies six physical equality-channel switches whose support permutations are the six transpositions of a connected `K_{2,3}` and hence generate `S_5` abstractly.

It then treats the corresponding affine maps as a physical subgroup of

\[
M_G\rtimes S_5
\]

whose every product sends the initial cover to another root-valued cover. This closure is not yet proved.

The missing point is **physical functoriality under intersecting channel switches**. After switching a component `Z` of `H_t`, the next channel is not represented by its original component. It is spliced according to

\[
H_s(x+t1_Z)
=
\bigl(H_s(x)\setminus Z\bigr)
\cup
\bigl(H_{\tau_t(s)}(x)\cap Z\bigr).
\]

Thus a word in the six abstract support transpositions need not be realised by the product of six fixed affine maps taken at the initial cover. The next physical component depends on the previous switches.

Consequently, the following claims of the corrected dossier are **conditional**, not theorem-level:

- that the six generators form one physical `S_5` affine subgroup;
- that the pure translation kernel is zero by direct reuse of BBD root rigidity;
- that the simultaneous origin must vanish;
- that every equality-lock holonomy is a global support permutation;
- that every relevant `H_s` is necessarily one connected cycle.

They become exact once a functorial equality-channel local system is constructed and shown root-admissible under concatenation.

---

## 2. Exact conditional theorem

Assume in addition that the six equality-channel switches extend to a based affine local system

\[
\mathcal H\le M_G\rtimes S_5
\]

such that:

1. its projection contains the six `K_{2,3}` transpositions;
2. every element of `mathcal H` is represented by a physical root-admissible switch word from the initial cover;
3. concatenation agrees with multiplication in the semidirect product.

Then all root-rigidity arguments in Sections 3--7 of the original dossier are valid:

- the projection is `S_5`;
- the pure translation kernel vanishes;
- the cocycle is a coboundary;
- the edgewise affine-orbit table leaves only `(0,root)` and `(root,0)`;
- flow conservation forces one global branch;
- the fixed branch is incompatible with the marked edges changing;
- hence the origin is zero and every generator component equals the complete `H_s`.

This is now recorded as a **conditional root-rigidity theorem**.

---

## 3. Unconditional results retained

The following statements in `EQUALITY_LOCK_S5_ROOT_RIGIDITY_V1.md` do not use the missing subgroup closure and remain exact.

### 3.1 Abstract generation

The six channel transpositions

\[
S_r=E(K_{2,3})
\]

generate `S_5` as an abstract permutation group.

### 3.2 Edgewise affine-orbit table

For `Y,R in E_5`,

\[
Y+gR\in R_5
\qquad(\forall g\in S_5)
\]

holds exactly for

\[
(Y,R)=(0,\rho)
\quad\text{or}\quad
(\rho,0),
\qquad \rho\in R_5.
\]

This remains available once functorial `S_5` holonomy is proved.

### 3.3 Channel conjugation

For one physical component switch,

\[
H_s(x+t1_Z)
=
(H_s(x)\setminus Z)
\cup
(H_{\tau_t(s)}(x)\cap Z).
\]

This is the exact replacement for the unjustified fixed-generator multiplication.

### 3.4 Common intersection and parity

For an equality root `r`,

\[
\bigcap_{s\in S_r}H_s=x^{-1}(r),
\]

and

\[
\bigtriangleup_{s\in S_r}H_s=H_r.
\]

The common intersection is an `r`-matching.

### 3.5 Endpoint fan

Every marked `r=uv` endpoint with local triangle `{uv,uw,vw}` has the complementary three--three channel fan

\[
A_w=\{vw\}\cup\{ux:x\ne w\},
\]

\[
B_w=\{uw\}\cup\{vx:x\ne w\}.
\]

These are Type-X singleton profiles, and for `w\ne w'`

\[
A_w\triangle A_{w'}
=B_w\triangle B_{w'}
=\Gamma_{ww'},
\]

the exact DDD channel-cohomology class.

---

## 4. Finite counter-calibration

A state-level condition saying only that the six `H_s` are connected cycles with one common route does not imply rank-two/Tait structure.

Exact small-graph searches find:

- a cube root flow using six distinct roots with such a state;
- a dodecahedral root flow using six distinct roots with such a state.

For the displayed dodecahedral four-pole obtained by cutting the marked root edges, complete root-flow enumeration realises all ten boundary states:

\[
\Sigma(P)=\mathcal S.
\]

Thus the state escapes horizontally; it is not a complete fixed-route outer-sector lock.

This separates the correct target:

\[
\boxed{
\text{complete profile lock}
\ne
\text{one pure-gauge-looking cover state}.}
\]

A proof must use functorial closure of the complete locked profile or derive a profile escape from failure of that closure.

---

## 5. Revised equality target

The equality problem is now precisely:

> Starting from the channel-conjugation law and the fixed oriented boundary route, prove that either the spliced channel components form a functorial root-admissible local system, or the first failure of functoriality gives profile escape, a smaller separator, a DDD endpoint discrepancy, or a strictly smaller lock.

If functoriality holds, conditional root rigidity eliminates the affine part and leaves the pure-gauge graph sector.

If functoriality fails, the failure itself is the desired progress certificate.

This is sharper than assuming an `S_5` subgroup at the outset.

---

## 6. Trust boundary

This correction withdraws no exact finite table or channel formula. It withdraws only the unproved implication

\[
\text{six physical generators}
\Longrightarrow
\text{one physical affine }S_5\text{ subgroup}.
\]

No equality-lock elimination or global five-support theorem is claimed.
