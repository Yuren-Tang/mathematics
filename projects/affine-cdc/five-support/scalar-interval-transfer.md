# Elementary scalar intervals as finite Tait transfer states

## 1. Scope and purpose

A scalar circuit may contain many `g`-edges outside the witness set `\eta`.  Therefore two consecutive **witness** `g`-edges need not be joined by one non-`g` path.

This chapter concerns an **elementary scalar interval**: the non-`g` path between two consecutive `g`-incidences in the full scalar circuit, with no `g`-edge internally.  A witness-to-witness arc is, in general, a concatenation of elementary intervals separated by edges of `E_g\setminus\eta`.

For one elementary interval, all quotient-flow transport is finite.  The interval is a walk on a three-state triangle; its quotient monodromy is determined by its two endpoint colours and one parity bit; and the total side-output colour telescopes to the endpoint sum.

The concatenation of arbitrarily many elementary intervals is handled naturally by the physical `g`-component transition quotient, not by pretending that a quartic block contains only four `g`-edges.

## 2. Quotient-phase setup

Let

$$
c:E(Q)\to V\setminus\{0\},
\qquad
V=\langle g\rangle\oplus U,
\qquad
U\cong\mathbf F_2^2,
$$

and write

$$
c(e)=\sigma(e)g+\bar c(e).
$$

Fix one scalar sheet

$$
H_\phi,
\qquad
\lambda_\phi=\alpha+\phi\circ\pi.
$$

The three non-`g` colours selected by this sheet are

$$
A_\phi
=
\{x:\lambda_\phi(x)=1,\ x\ne g\}.
$$

Projection gives a bijection

$$
A_\phi\cong U\setminus\{0\}.
$$

The three nonzero omitted colours are

$$
W_\phi^\times
=
\ker\lambda_\phi\setminus\{0\}.
$$

For distinct `x,y\in A_\phi`, their sum lies in `W_\phi^\times`.  Hence `A_\phi` is the vertex set of a triangle whose edge labels are the three elements of `W_\phi^\times`.

## 3. Elementary intervals and local turns

Let an elementary interval have non-`g` path edges

$$
f_0,f_1,\ldots,f_n,
$$

with

$$
x_t=c(f_t)\in A_\phi,
\qquad
q_t=\bar c(f_t)\in U\setminus\{0\}.
$$

For `1\le t\le n`, let `d_t` be the third edge at the internal vertex between `f_{t-1}` and `f_t`.

### Lemma 3.1 — local turn law

At every internal vertex:

$$
\boxed{
 c(d_t)=x_{t-1}+x_t,
 \qquad
 \bar c(d_t)=q_{t-1}+q_t.
}
$$

Moreover `x_{t-1}\ne x_t`, `q_{t-1}\ne q_t`, and `c(d_t)\in W_\phi^\times`.

#### Proof

The internal vertex is not incident with a `g`-edge, because every `g`-edge belongs to `H_\phi` and would create degree three in the scalar subgraph.  Thus it is an ordinary quotient vertex.  The two path edges are the selected pair, and Kirchhoff conservation gives the third colour as their sum. ∎

Consequently an elementary interval is exactly a walk

$$
x_0,x_1,\ldots,x_n
$$

on the three-colour triangle, with side-output word

$$
c(d_1),\ldots,c(d_n).
$$

## 4. Telescoping output

### Theorem 4.1 — side-sum theorem

$$
\boxed{
\sum_{t=1}^n c(d_t)=x_0+x_n,
\qquad
\sum_{t=1}^n\bar c(d_t)=q_0+q_n.
}
$$

#### Proof

Sum the local identities.  Every internal path colour occurs twice and cancels. ∎

Thus arbitrary elementary-interval length contributes no new total side-output colour.

## 5. Eighteen quotient transfer states

For each turn, let `\tau_t\in GL(U)\cong S_3` be the unique transposition exchanging `q_{t-1},q_t` and fixing `q_{t-1}+q_t`.  Define

$$
\mu(P)=\tau_n\cdots\tau_1.
$$

### Theorem 5.1 — finite monodromy

One has

$$
\mu(P)(q_0)=q_n,
$$

and the permutation parity of `\mu(P)` is `n\bmod2`.  Therefore `\mu(P)` is uniquely determined by

$$
\boxed{(q_0,q_n,n\bmod2).}
$$

#### Proof

The product carries each successive quotient colour to the next.  For fixed nonzero `q_0,q_n`, exactly two elements of `S_3` map `q_0` to `q_n`; they have opposite parity. ∎

### Corollary 5.2

There are exactly

$$
3\cdot3\cdot2=18
$$

oriented elementary-interval transfer states.  For a fixed sheet, the state also determines the full endpoint colours and hence the total full side-output colour.

The states compose under concatenation of elementary intervals whenever the intervening `g`-incidence and its transition are recorded.  Reversal inverts the monodromy.

## 6. Backtracks and reduced words

An immediate backtrack has continuation word

$$
x,y,x.
$$

Its two side-output colours are equal, and the two local transpositions cancel.

### Proposition 6.1 — algebraically neutral backtrack

Deleting an immediate backtrack preserves:

- the endpoint colours;
- quotient monodromy;
- total side-output colour.

It removes two turns.

After all immediate backtracks are deleted, a walk on a triangle is forced to continue periodically around the three colours.  Thus every reduced elementary interval has a three-periodic continuation and side-output word.

Deletion here is only an algebraic word reduction.  The two equal-coloured side edges may have different external attachments.

## 7. Witness arcs and the transition quotient

Let `C` be a scalar circuit and let `e,e'\in C\cap\eta` be consecutive **witness** edges in the cyclic order on `C\cap\eta`.  The arc of `C` from `e` to `e'` may have the form

$$
e,\ P_0,\ h_1,\ P_1,\ h_2,\ldots,h_r,\ P_r,\ e',
$$

where

$$
h_j\in E_g\setminus\eta
$$

and every `P_j` is an elementary non-`g` interval.

Hence a quartic block supplies four witness-to-witness arcs, but not necessarily four elementary intervals.  Each arc is a transition walk through the physical `g`-component quotient `\Gamma_g`.

### Corollary 7.1 — corrected finite layer

For every elementary segment in a witness arc, the quotient transfer belongs to the eighteen-state groupoid.  The complete witness arc is obtained by composing these finite transfers with the intervening `g`-edge transitions in `\Gamma_g`.

No bound on the number of intervening `E_g\setminus\eta` edges is asserted.

## 8. Consequence for localisation

The elementary non-`g` algebra is finite.  The remaining unbounded layers are:

1. the number and arrangement of intervening `g`-edges outside `\eta`;
2. the transition matchings inside the components of `Q-E_g`;
3. the ordered side attachments along periodic elementary segments;
4. simultaneous compatibility across all four scalar sheets.

These are precisely the data retained by the physical transition quotient and its four transition systems.

A composition theorem should force a separator or transition split in `\Gamma_g`, where every internal quotient cut lifts exactly to `Q`.

## 9. Reliability boundary

Proved here:

- every elementary `g`-to-`g` scalar interval is a three-state triangle walk;
- its full and quotient side-output sums telescope;
- its quotient monodromy is determined by two endpoint colours and one parity bit;
- there are eighteen oriented elementary transfer states;
- reduced elementary words are three-periodic.

Explicitly not claimed:

- that consecutive witness edges are consecutive `g`-edges;
- that a quartic block has only four elementary intervals;
- that finite elementary states alone classify an entire witness arc;
- composition-safe deletion of backtracks or periodic cells;
- the global five-support theorem.

No Lean, independent-review, peer-review, publication, release, arXiv, or DOI status is implied.
