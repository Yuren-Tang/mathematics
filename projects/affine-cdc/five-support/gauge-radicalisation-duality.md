# Gauge radicalisation and persistent-intersection duality

## 1. Purpose

The physical response form of a signed ribbon realization is

$$
\mathcal B:
Z(G)\times Z(G)
\longrightarrow
\mathbf F_2,
$$

where

$$
Z(G)=\operatorname{Cycle}(G).
$$

A partial Petrial with edge word

$$
\lambda\in\mathbf F_2^{E(G)}
$$

changes the form by

$$
\mathcal B_\lambda(z,z')
=
\mathcal B(z,z')
+
(\lambda\odot z)\cdot z',
$$

where `\odot` denotes coordinatewise product.

In AffineCDC, only a linear code

$$
C\le\mathbf F_2^{E(G)}
$$

of Petrial words is admissible; for a fixed Fano flow this is the reduced gauge code, extended by zero on fixed route caps when necessary.

This chapter gives exact linear criteria for two operations.

1. **Radicalise one response cycle:** move a chosen cycle `z` into the radical of the intersection form.
2. **Orient the whole ribbon surface:** make the response form alternating.

Failure of radicalisation has a sharp dual certificate: a physical cycle `z'` which intersects `z` oddly on the surface, while their common-edge word

$$
z\odot z'
$$

is orthogonal to every admissible Petrial.

Thus the residual prime response branch is converted into an exact alternative:

$$
\boxed{
\text{admissible gauge radicalisation}
\quad\text{or}\quad
\text{gauge-invisible odd-intersection pair}.
}
$$

## 2. Cycle functionals and edge representatives

Let

$$
B(G)=\operatorname{Cut}(G).
$$

The edge dot product identifies

$$
\mathbf F_2^{E(G)}/B(G)
\cong
Z(G)^*.
$$

For a response cycle `z`, choose an edge word `a` representing the functional

$$
\mathcal B(z,-):Z(G)\to\mathbf F_2;
$$

that is,

$$
\boxed{
a\cdot z'
=
\mathcal B(z,z')
\quad
\text{for all }z'\in Z(G).
}
$$

The class `[a]` is independent of the chosen response lift because two representatives differ by a cut.

Under a Petrial word `\lambda`, the new representative is

$$
\boxed{
a_\lambda
=
a+\lambda\odot z.}
$$

Indeed,

$$
a_\lambda\cdot z'
=
\mathcal B(z,z')
+
\sum_e\lambda_ez_ez'_e
=
\mathcal B_\lambda(z,z').
$$

## 3. The radicalisation map

Fix

$$
z\in Z(G).
$$

Define the linear map

$$
\mu_z:C
\longrightarrow
\mathbf F_2^{E(G)}/B(G)
$$

by

$$
\boxed{
\mu_z(\lambda)
=
[\lambda\odot z].
}
$$

### Theorem 3.1 — exact radicalisation criterion

There exists an admissible Petrial

$$
\lambda\in C
$$

such that

$$
z\in\operatorname{rad}\mathcal B_\lambda
$$

if and only if

$$
\boxed{
[a]\in\operatorname{Im}\mu_z.
}
$$

Equivalently, radicalisation is possible exactly when

$$
\boxed{
a+\lambda\odot z\in B(G)}
$$

for some `\lambda\in C`.

#### Proof

The condition that `z` lie in the radical of the new form is

$$
\mathcal B_\lambda(z,z')=0
$$

for every `z'\in Z(G)`.  Using the representative `a_\lambda`, this is

$$
a_\lambda\cdot z'=0
$$

for every cycle `z'`.  The orthogonal complement of the cycle space is the cut space, so this is equivalent to

$$
a+\lambda\odot z\in B(G).
$$

Passing to the quotient gives `[a]=\mu_z(\lambda)`. ∎

For a cap cocircuit response `(z,a)`, successful radicalisation means that after an admissible gauge move and one cut-kernel adjustment the cocycle can be represented as

$$
(z,0,z).
$$

The remaining support is boundary-type rather than positive-genus response.

## 4. Dual annihilator

Let

$$
C^\perp
=
\{w\in\mathbf F_2^{E(G)}:w\cdot\lambda=0
\text{ for all }\lambda\in C\}.
$$

A physical cycle `z'` annihilates the image of `\mu_z` precisely when

$$
(\lambda\odot z)\cdot z'=0
$$

for every `\lambda\in C`.  Since

$$
(\lambda\odot z)\cdot z'
=
\lambda\cdot(z\odot z'),
$$

this is equivalent to

$$
z\odot z'\in C^\perp.
$$

### Theorem 4.1 — persistent-intersection duality

A response cycle `z` can be radicalised by an admissible Petrial if and only if

$$
\boxed{
\mathcal B(z,z')=0
}
$$

for every physical cycle `z'` satisfying

$$
\boxed{
z\odot z'\in C^\perp.}
$$

Equivalently, radicalisation fails if and only if there exists

$$
z'\in Z(G)
$$

such that

$$
\boxed{
\mathcal B(z,z')=1,
\qquad
z\odot z'\in C^\perp.
}
$$

#### Proof

By Theorem 3.1, radicalisation is possible exactly when `[a]` lies in `\operatorname{Im}\mu_z`.  In a finite-dimensional binary vector space, this holds if and only if every functional annihilating `\operatorname{Im}\mu_z` also annihilates `[a]`.

The annihilating functionals are represented by cycles `z'` with

$$
z\odot z'\in C^\perp.
$$

Their value on `[a]` is

$$
a\cdot z'
=
\mathcal B(z,z').
$$

This gives both formulations. ∎

The dual witness is entirely physical:

- `z,z'` are graph cycle vectors;
- `\mathcal B(z,z')=1` means odd ribbon-surface intersection;
- `z\odot z'` is the common-edge word;
- membership in `C^\perp` says that no admissible gauge word detects that common-edge word.

## 5. Support-restricted form

Only edges of `z` matter in `\mu_z`.  Let

$$
C|_z
=
\{\lambda|_{\operatorname{supp}z}:\lambda\in C\}
\le
\mathbf F_2^{\operatorname{supp}z}.
$$

Then

$$
\mu_z(C)
$$

depends only on the shortened code `C|_z`.

### Corollary 5.1 — private response support

If

$$
C|_z=0,
$$

then `z` is radicalisable if and only if it was already radical:

$$
\mathcal B(z,-)=0.
$$

If it is not radical, every cycle `z'` with odd intersection gives a persistent certificate because

$$
z\odot z'\in C^\perp.
$$

This is the response-form analogue of a marked obstruction core with zero reserve code.

### Corollary 5.2 — full support control

If the shortened gauge code contains every word on `\operatorname{supp}z`, then `z` is always radicalisable.

#### Proof

Choose one representative `a` of `\mathcal B(z,-)`.  Since only the restriction of `a` to `\operatorname{supp}z` matters in the equation

$$
a+\lambda\odot z\in B(G),
$$

full support control allows the required `\lambda` to match that representative on `\operatorname{supp}z`. ∎

The intermediate case is measured exactly by `\mu_z` and its dual certificate.

## 6. Orientability as one affine gauge equation

For a symmetric bilinear form over `\mathbf F_2`, the diagonal function

$$
q_{\mathcal B}(z)
=
\mathcal B(z,z)
$$

is linear, because mixed terms occur twice.

Thus

$$
q_{\mathcal B}\in Z(G)^*
\cong
\mathbf F_2^{E(G)}/B(G).
$$

Choose an edge representative

$$
w\in\mathbf F_2^{E(G)}
$$

with

$$
w\cdot z=q_{\mathcal B}(z).
$$

Topologically `[w]` is the first Stiefel--Whitney functional of the ribbon surface.

Under a Petrial `\lambda`,

$$
q_{\mathcal B_\lambda}(z)
=
q_{\mathcal B}(z)+\lambda\cdot z.
$$

### Theorem 6.1 — admissible orientability criterion

There exists

$$
\lambda\in C
$$

for which the Petrial surface is orientable if and only if

$$
\boxed{
[w]\in(C+B(G))/B(G).
}
$$

Equivalently,

$$
\boxed{
w+\lambda\in B(G)}
$$

for some `\lambda\in C`.

#### Proof

The new surface is orientable exactly when its intersection form is alternating, i.e. when

$$
q_{\mathcal B_\lambda}=0.
$$

This says

$$
(w+\lambda)\cdot z=0
$$

for every cycle `z`, equivalently `w+\lambda\in B(G)`. ∎

### Corollary 6.2 — orientability dual obstruction

An admissible orienting Petrial exists if and only if every cycle

$$
z\in Z(G)\cap C^\perp
$$

has

$$
\boxed{
\mathcal B(z,z)=0.
}
$$

Failure is certified by a gauge-invisible one-sided cycle:

$$
\boxed{
z\in Z(G)\cap C^\perp,
\qquad
\mathcal B(z,z)=1.}
$$

This sharpens the statement that the orientable locus is an affine slice of the gauge torsor.

## 7. Application to the route-locked cap response

Let

$$
G=\widehat Q
$$

and extend the active reduced gauge code by zero on the two fixed cap edges.  Let `(z,a)` be the physical response word of a prime coupled cap cocircuit.

The response branch now satisfies the exact trichotomy:

1. **admissibly radicalisable:**
   $$
   [a]\in\operatorname{Im}\mu_z;
   $$
   after gauge and cut adjustment the response is boundary-type;
2. **persistent odd pair:** there exists `z'` with
   $$
   \mathcal B(z,z')=1,
   \qquad
   z\odot z'\in C^\perp;
   $$
3. **self-persistent subcase:** one may take `z'=z`, giving
   $$
   \mathcal B(z,z)=1,
   \qquad
   z\in C^\perp,
   $$
   a gauge-invisible one-sided cycle.

The second case is the first exact obstruction which simultaneously remembers:

- the physical cycle projection;
- the ribbon genus interaction;
- the admissible vertical gauge code;
- the edge support on which the two cycles overlap.

## 8. Updated proof target

The next mathematical target is no longer an unrestricted response-form classification.  It is to localise the dual word

$$
z\odot z'\in C^\perp
$$

using the AffineCDC structure.

A successful theorem should show that a gauge-invisible odd-intersection pair yields one of:

1. a proper common support region and physical separator;
2. a bounded one-sided or symplectic handle supporting a replacement;
3. a connected-cycle Fano switch which changes the admissible code or destroys the pair;
4. the physical DDD support-label cocycle.

The condition

$$
z\odot z'\in C^\perp
$$

is now the exact bridge to the existing reserve-code, harmonic-quotient, and Fourier/stress annihilator machinery.

## 9. Reliability boundary

Proved here:

- exact radicalisation map `\mu_z`;
- necessary and sufficient gauge-radicalisation criterion;
- dual persistent-intersection certificate;
- shortened-code consequences;
- affine orientability equation;
- dual gauge-invisible one-sided-cycle certificate.

The interface with AffineCDC assumes that the code `C` acts on the response ribbon realization by the same partial Petrials as the active gauge code.  Establishing this compatibility for every route-capped endpoint remains a separate closure theorem.

Open:

- localisation of `z\odot z'\in C^\perp` in `\Gamma_g`;
- guaranteed genus reduction or radicalisation under the active gauge code;
- conversion of a persistent pair to a bounded replacement or horizontal switch;
- comparison with DDD;
- the global five-support theorem.

No Lean, independent-review, peer-review, publication, release, arXiv, DOI, or merge status is implied.
