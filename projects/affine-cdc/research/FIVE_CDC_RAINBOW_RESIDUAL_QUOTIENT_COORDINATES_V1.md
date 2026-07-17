# Residual coordinates in the rainbow choice quotient

**Programme:** `AffineCDC — Research Lead`  
**Status:** exact finite coordinate theorem and negative coset result; geometric interior interpretation remains open  
**Parent:** `FIVE_CDC_RAINBOW_CHOICE_PARITY_SQUARE_V1.md`

## 1. Purpose

The BBD raw-choice quotient is

\[
F_2^6/K_{\mathrm{raw}}\cong F_2^4,
\]

while the parity square uses only two quotient coordinates

\[
(\nu,\rho).
\]

This packet identifies two additional linear coordinates and determines exactly what they do and do not provide.

Write

\[
q=(\alpha_0,\beta_0,\alpha_1,\beta_1,\alpha_2,\beta_2).
\]

Define

\[
\boxed{
\sigma:=\alpha_2,
\qquad
\tau:=\beta_0+\beta_2.
}
\]

## 2. Complete coordinate theorem

### Computational Theorem 2.1

The map

\[
\boxed{
[q]
\longmapsto
(\nu,\rho,\sigma,\tau)
}
\]

is a bijection

\[
F_2^6/K_{\mathrm{raw}}
\xrightarrow{\sim}
F_2^4.
\]

Equivalently:

1. every quadruple `(nu,rho,sigma,tau)` has exactly four raw representatives;
2. all four raw representatives yield the same support monodromy;
3. distinct quadruples yield distinct support monodromies.

Thus the support monodromy is uniquely parametrised by four binary quotient coordinates.

#### Proof status

Exact dependency-free enumeration of all `64` raw choices. ∎

The first two coordinates have established meanings:

- `rho` selects rank-one versus full-rank path geometry;
- `nu` selects the support cycle type inside that rank class.

The last two coordinates distinguish the four actual monodromies in one parity cell.

## 3. The quotient parametrisation is not a group representation

One might hope that the four monodromies in every parity cell form a left or right coset of one common Klein-four subgroup of `S_5`.  This is false.

### Computational Proposition 3.1 — no common `V_4` coset

Choose a base monodromy in each parity cell.  Form either the left difference set

\[
\{\pi\pi_0^{-1}\}
\]

or the right difference set

\[
\{\pi_0^{-1}\pi\}
\]

over the four monodromies in that cell.

The resulting four-point sets:

- are not the same for all four cells;
- are not subgroups of `S_5`.

Therefore the residual coordinates `(sigma,tau)` do not define a common `V_4` gauge action on the monodromy set.

#### Proof status

Exact finite computation. ∎

## 4. Interpretation

The quotient

\[
F_2^6/K_{\mathrm{raw}}
\cong F_2^4
\]

is an affine coordinate space for **choice classes**, not a group whose addition is transported to multiplication in `S_5`.

The map

\[
F_2^4\longrightarrow S_5
\]

is nonlinear.

Accordingly:

- `(nu,rho)` are genuine coarse invariants with direct graph-theoretic meaning;
- `(sigma,tau)` are exact residual transport coordinates, but not yet a geometric symmetry group;
- their correct home is the lifted reconfiguration groupoid, where composition need not be ordinary vector addition.

This negative result prevents an incorrect simplification of the four monodromies in each cell to a single Klein-four orbit.

## 5. Updated control diagram

\[
\boxed{
\begin{array}{c}
q\in F_2^6
\\ \downarrow/K_{\mathrm{raw}}\\
(\nu,\rho,\sigma,\tau)\in F_2^4
\\ \downarrow\\
\pi=\Phi(\nu,\rho,\sigma,\tau)\in S_5
\\ \downarrow\\
\begin{cases}
\rho=0:&\text{rank-one spanning-path test},\\
\rho=1:&\text{full-rank XOR-cover test},
\end{cases}
\\ \downarrow\\
(d_\lambda,U_\lambda,X_\lambda).
\end{array}
}
\]

The next theorem should determine how `(sigma,tau)` act on the interior obstruction signature, not search for a nonexistent common `V_4` action on support permutations alone.

## 6. Trust boundary and next task

Exact:

- `(nu,rho,sigma,tau)` bijectively parametrize the sixteen support monodromies;
- every coordinate quadruple has four raw representatives;
- the monodromy map is not a common Klein-four coset representation.

Open:

- a geometric interpretation of `(sigma,tau)` as path-component or repeated-trace transport;
- the induced action on norm defects, uncovered-edge sets, and missed-vertex sets;
- a common-witness theorem across the four residual coordinates in one parity cell.
