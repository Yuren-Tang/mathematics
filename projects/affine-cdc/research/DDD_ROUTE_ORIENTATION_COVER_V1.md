# DDD crossed-route orientation covers and octahedral parity

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Parents:**

- `projects/affine-cdc/research/OCTAHEDRAL_OVERLAP_TRANSPORT_V1.md`;
- `projects/affine-cdc/research/DDD_COHOMOLOGY_GENERATOR_V1.md`;
- `projects/affine-cdc/research/DDD_ROUTE_LOCK_TRANSGRESSION_V1.md`.

**Status:** exact finite orientation-cover theorem; graph-level bounded localisation remains open.  
**Not implied:** canonical acceptance, independent audit, Lean verification, manuscript readiness, or the global five-support theorem.

---

## 1. Setup

Fix

\[
r_1=12,
\qquad
r_2=34,
\qquad
c=r_1+r_2=1234,
\]

and let

\[
D_8=\operatorname{Stab}_{S_4}(\{r_1,r_2\}).
\]

Write

\[
g=a^{\epsilon_1}b^{\epsilon_2}p^\sigma,
\]

where

\[
a=(12),
\qquad
b=(34),
\qquad
p=(13)(24).
\]

Define

\[
\kappa(g)=\epsilon_1+\epsilon_2,
\qquad
\chi(g)=\sigma.
\]

The nontrivial DDD cocycle is

\[
\alpha(g)=\epsilon_1r_2+\epsilon_2r_1.
\]

Let the two crossed matchings be

\[
X=\{13,24\},
\qquad
Y=\{14,23\}.
\]

The affine action is

\[
g\star x=gx+\alpha(g).
\]

The previous route-lock theorem shows that `X` and `Y` are each invariant as unordered two-point root sets.

---

## 2. Exact block-orientation characters

Choose one block in each crossed matching:

\[
x=13\in X,
\qquad
y=14\in Y.
\]

The antipodal blocks are

\[
x+c=24,
\qquad
y+c=23.
\]

### Theorem 2.1 — oriented crossed-route transport

For every `g in D_8`,

\[
\boxed{
g\star x=x+\kappa(g)c,}
\]

and

\[
\boxed{
g\star y=y+(\kappa(g)+\chi(g))c.}
\]

Thus the two crossed matching sets are fixed, while their two blocks are exchanged according to the characters

\[
\boxed{\nu_X=\kappa,
\qquad
\nu_Y=\kappa+\chi.}
\]

In particular,

\[
\boxed{\nu_X+\nu_Y=\chi.}
\]

### Proof

The explicit coboundary identities are

\[
\alpha(g)+\kappa(g)c=x+gx
\]

and

\[
\alpha(g)+(\kappa(g)+\chi(g))c=y+gy.
\]

Rearranging gives the two affine-action formulas.

The first identity is checked on the generators:

- for `a`, `alpha(a)+c=r_2+c=r_1=x+ax`;
- for `b`, `alpha(b)+c=r_1+c=r_2=x+bx`;
- for `p`, both sides are zero because `p` fixes `x=13`.

The second is analogous with `y=14`.

---

## 3. Orientation double covers

An unordered physical route is a perfect matching, i.e. an unordered pair of terminal blocks. Choosing one of its two blocks is an orientation of that route.

For the crossed route `X`, the stabiliser of one oriented block is

\[
D_X=\ker\kappa.
\]

For the crossed route `Y`, it is

\[
D_Y=\ker(\kappa+\chi).
\]

### Theorem 3.1 — trivialisation on the orientation covers

The DDD cocycle becomes a coboundary after restriction to either oriented-route cover:

\[
\boxed{
\alpha|_{D_X}=\delta x,
}
\]

and

\[
\boxed{
\alpha|_{D_Y}=\delta y.
}
\]

### Proof

On `D_X`, `kappa=0`, so the first identity of Theorem 2.1 gives

\[
\alpha(g)=x+gx.
\]

On `D_Y`, `kappa+chi=0`, so the second gives

\[
\alpha(g)=y+gy.
\]

### Interpretation

The exceptional DDD class disappears after choosing and consistently transporting one block of a crossed matching. It survives on the physical base precisely because the two blocks of a terminal matching are unordered and a consistent orientation need not return around a loop.

Hence the nontrivial class is an orientation-descent obstruction, not a bare exchange of the original bad root sheets.

---

## 4. Why `alpha+kappa*c` is not a competing physical cocycle

The identity

\[
\alpha+\kappa c=\delta x
\]

shows that adding `kappa c` trivialises the cocycle. This operation is exactly the passage from the unordered crossed route `X` to its oriented double cover with distinguished block `x`.

Therefore:

- `alpha` is the canonical affine action on the **unoriented** physical route;
- `alpha+kappa c` is its pointwise trivialisation after an extra block orientation is supplied;
- using the latter on the physical base silently assumes the very global orientation whose failure is measured by `[alpha]`.

The two expressions are not two equally available physical laws. One lives on the base route system, the other on its orientation cover.

The ordinary bad-sheet exchange character remains different:

\[
\chi c=\delta r_1.
\]

It changes affine origin and is gauge-trivial without orienting a crossed route.

---

## 5. Extraction from an octahedral overlap word

Let

\[
y_0,y_1,\ldots,y_n
\]

be an oriented fixed-co-root overlap walk in the octahedral graph `L(K_4)`. Each step has side root

\[
w_i=y_{i-1}+y_i
\]

and canonical transport transposition

\[
\tau_{w_i}.
\]

The cumulative transport is

\[
\pi_\gamma=\tau_{w_n}\cdots\tau_{w_1}\in S_4.
\]

Assume the walk returns to the same unoriented bad matching, so

\[
\pi_\gamma\in D_8.
\]

### Theorem 5.1 — internal twist equals path-length parity

\[
\boxed{
\kappa(\pi_\gamma)=n\pmod2.
}
\]

### Proof

Every local transport `tau_{w_i}` is a transposition and hence has odd sign. Therefore

\[
\operatorname{sgn}(\pi_\gamma)=(-1)^n.
\]

Inside `D_8`, the generators `a,b` are odd and `p` is even, so

\[
\operatorname{sgn}(g)=(-1)^{\epsilon_1+\epsilon_2}=(-1)^{\kappa(g)}.
\]

Comparing gives the result.

### Corollary 5.2 — explicit crossed-route return bits

For the two crossed routes,

\[
\boxed{
\nu_X(\gamma)=n\pmod2,
}
\]

and

\[
\boxed{
\nu_Y(\gamma)=n+\chi(\pi_\gamma)\pmod2.
}
\]

Thus the enriched overlap word already determines both orientation holonomies from:

1. path-length parity;
2. the bad-sheet return bit `chi`.

No additional unidentified local `C_2` datum remains.

---

## 6. Möbius-type interpretation

A return with

\[
\kappa(\pi_\gamma)=1
\]

reverses the orientation of crossed route `X`. The route itself returns as an unordered matching, but a chosen block returns as its antipode.

This is the precise analogue of a Möbius return:

- on the orientation double cover the affine cocycle is trivial;
- on the unoriented base the descent obstruction is the nonzero DDD class.

The DDD class can therefore be described equivalently as:

\[
\boxed{
\text{the obstruction to orienting a crossed terminal matching around the overlap return.}
}
\]

For `X`, this obstruction is detected by odd octahedral path length. For `Y`, it is detected by path length plus bad-sheet exchange.

---

## 7. Relation to unique bad route

The route-lock quotient has four points

\[
O,B,X,Y,
\]

where `B` is the original atom pairing and `X,Y` are the crossed routes. Under the nontrivial internal twist:

- `X,Y` return as the same unordered routes, with their block orientations governed by Theorem 2.1;
- `O,B` are exchanged in the affine quotient.

Thus the same return simultaneously produces:

1. two root-valued crossed route sections at the unordered level;
2. one bad route that transgresses into the defect coset;
3. a possible orientation reversal inside each crossed route.

This gives a single finite mechanism behind crossed-route safety, the unique bad route, and the exceptional affine class.

---

## 8. Revised physical frontier

The orientation bit is no longer an unknown choice: it is extracted from the octahedral transport product.

The remaining graph-level task is localisation and composition.

### Target 8.1 — first odd-return localisation

For a support-minimal overlap segment with

\[
\kappa(\pi_\gamma)=1,
\]

localise the first crossed-route orientation reversal and prove one of:

1. it forms a bounded DDD blossom with the same unordered route interface;
2. it exposes a common-cut/full-channel curvature witness;
3. it enters a zero/co-root defect-tree unit;
4. it yields a smaller cyclic separator.

### Target 8.2 — even-return reduction

If

\[
\kappa(\pi_\gamma)=0,
\]

then crossed route `X` has a consistent oriented origin along the return. Use the explicit coboundary origin `x` to construct a root-admissible gauge/serial reduction, profile escape, or smaller interface. Ambient triviality alone is insufficient; edgewise root admissibility must be retained.

### Target 8.3 — simultaneous two-route compatibility

The two orientation characters differ by `chi`. Determine whether a nontrivial bad-sheet exchange can be absorbed by the known coboundary `chi c=delta r_1` without changing the external route profile. This should separate harmless sheet exchange from genuine internal twist at the physical replacement level.

---

## 9. Trust boundary

### Exact here

- the block-orientation formulas for both crossed matchings;
- the orientation-cover subgroups;
- trivialisation of `alpha` on each orientation cover;
- interpretation of `alpha+kappa c` as oriented-route trivialisation rather than a competing base cocycle;
- `kappa(pi_gamma)=length(gamma) mod 2`;
- extraction of both crossed-route orientation return bits from the octahedral word;
- the Möbius-type descent interpretation.

### Still open

- root-admissible bounded replacement for even returns;
- bounded DDD/common-cut/defect localisation for odd returns;
- simultaneous compatibility of both crossed-route orientations with external four-pole semantics;
- Type T/Type H composition, horizontal/global induction, and the global five-support theorem.
