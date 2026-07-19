# Scalar intervals as finite Tait transfer states

## 1. Purpose

The quartic split-or-peel theorem leaves one genuinely physical source of unboundedness.  A closed scalar component meeting the witness in four `g`-edges is divided by those edges into four non-`g` intervals, and those intervals may have arbitrary graph length and arbitrary side attachments.

This chapter isolates the exact flow information carried by one such interval.  For a fixed scalar sheet, every non-`g` interval is a walk on a three-state triangle.  Its quotient transport is determined by its two endpoint colours and one parity bit, and the total colour emitted through all side edges telescopes to the sum of the endpoint colours.

Thus interval length carries no additional quotient-flow monodromy.  The unresolved information is the ordered side-attachment word and its graph semantics, not the flow algebra itself.

## 2. Route-locked quotient-phase setup

Let

$$
c:E(Q)\longrightarrow V\setminus\{0\},
\qquad
V\cong\mathbf F_2^3,
$$

be a route-locked flow with terminal colour `g`.  Choose

$$
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
\lambda_\phi=\alpha+\phi\circ\pi,
\qquad
\phi\in U^*.
$$

Its edge indicator is

$$
h_\phi(e)
=
\lambda_\phi(c(e))
=
\sigma(e)+\phi(\bar c(e)).
$$

The three non-`g` colours selected by this sheet are

$$
A_\phi
=
\{x\in V:\lambda_\phi(x)=1,\ x\ne g\}.
$$

Projection to `U` gives a bijection

$$
A_\phi
\xrightarrow{\sim}
U\setminus\{0\}.
$$

The three nonzero colours omitted by the sheet form

$$
W_\phi^\times
=
\ker(\lambda_\phi)\setminus\{0\}.
$$

For distinct `x,y\in A_\phi`, one has

$$
x+y\in W_\phi^\times.
$$

Hence `A_\phi` is the vertex set of a triangle whose three edge labels are the three elements of `W_\phi^\times`.

## 3. Scalar intervals

A scalar interval in `H_\phi` is a path between two endpoints of `g`-edges, containing no `g`-edge internally.  Write its non-`g` path edges in order as

$$
f_0,f_1,\ldots,f_n,
$$

and put

$$
x_t=c(f_t)\in A_\phi,
\qquad
q_t=\bar c(f_t)\in U\setminus\{0\}.
$$

For `1\le t\le n`, let `d_t` be the third edge at the internal vertex between `f_{t-1}` and `f_t`.

### Lemma 3.1 — local turn law

At every internal vertex:

1. `x_{t-1}\ne x_t` and `q_{t-1}\ne q_t`;
2. the side edge is not in `H_\phi`;
3. its full colour and quotient colour are
   $$
   \boxed{
   c(d_t)=x_{t-1}+x_t,
   \qquad
   \bar c(d_t)=q_{t-1}+q_t;
   }
   $$
4. `c(d_t)` is one of the three nonzero colours of `\ker\lambda_\phi`.

#### Proof

At an ordinary cubic vertex the three full flow values are distinct nonzero vectors summing to zero.  The scalar even subgraph has degree two there, so `f_{t-1},f_t` are the two selected edges and `d_t` is omitted.  Kirchhoff conservation gives the displayed sum.  Applying `\lambda_\phi` gives

$$
\lambda_\phi(c(d_t))
=1+1=0.
$$

Nonzeroness follows from `x_{t-1}\ne x_t`.  Projection gives the quotient identity.  ∎

Thus a scalar interval is exactly a walk

$$
x_0,x_1,\ldots,x_n
$$

on the triangle with vertex set `A_\phi`, and the side-output word is the sequence of triangle-edge labels

$$
c(d_1),\ldots,c(d_n).
$$

## 4. Telescoping side output

### Theorem 4.1 — interval side-sum theorem

For every scalar interval,

$$
\boxed{
\sum_{t=1}^n c(d_t)
=
x_0+x_n.
}
$$

Equivalently, in the quotient,

$$
\boxed{
\sum_{t=1}^n \bar c(d_t)
=
q_0+q_n.
}
$$

#### Proof

Using the local turn law,

$$
\sum_{t=1}^n c(d_t)
=
\sum_{t=1}^n(x_{t-1}+x_t).
$$

Every internal path colour `x_1,\ldots,x_{n-1}` occurs twice and cancels over `\mathbf F_2`, leaving `x_0+x_n`.  Projection gives the quotient formula.  ∎

### Corollary 4.2

The total side-output colour of an arbitrarily long interval is determined by its two endpoint continuation colours.  No interior length or colour-word parameter survives in the total sum.

This is a conservation statement for the output sum, not for the ordered side-output word or the attached subgraphs.

## 5. Canonical quotient monodromy

For each turn from `q_{t-1}` to `q_t`, let

$$
\tau_t\in GL(U)\cong S_3
$$

be the unique transposition that exchanges `q_{t-1}` and `q_t` and fixes their sum

$$
q_{t-1}+q_t.
$$

Define the oriented interval monodromy

$$
\mu(P)
=
\tau_n\cdots\tau_1.
$$

### Theorem 5.1 — finite interval monodromy

The interval monodromy satisfies:

1. 
   $$
   \boxed{\mu(P)(q_0)=q_n;}
   $$
2. its permutation parity is
   $$
   \boxed{\operatorname{sgn}\mu(P)=n\pmod2;}
   $$
3. `\mu(P)` is uniquely determined by the triple
   $$
   \boxed{(q_0,q_n,n\bmod2).}
   $$

#### Proof

Each `\tau_t` sends `q_{t-1}` to `q_t`, so the product sends `q_0` to `q_n`.  It is a product of `n` transpositions, giving the parity statement.

For fixed nonzero `q_0,q_n`, exactly two elements of `GL(U)\cong S_3` send `q_0` to `q_n`.  They differ by the nontrivial element of the stabiliser of `q_n`, hence have opposite permutation parity.  The parity therefore selects exactly one of them.  ∎

### Corollary 5.2 — eighteen quotient transfer states

An oriented scalar interval has only

$$
3\cdot3\cdot2=18
$$

possible quotient monodromy states

$$
(q_0,q_n,n\bmod2).
$$

The full endpoint colours `x_0,x_n` are uniquely determined by `q_0,q_n` and the sheet `\phi`, because each nonzero quotient class has exactly one lift in `A_\phi`.  Hence the same state also determines the total full side-output colour `x_0+x_n`.

## 6. Composition and reversal

Suppose two scalar intervals concatenate through a common continuation colour `q`.  Then their monodromies compose:

$$
\mu(P_2P_1)=\mu(P_2)\mu(P_1),
$$

and their turn parities add.  Reversing an interval gives

$$
\mu(P^{-1})=\mu(P)^{-1}.
$$

Thus the eighteen states form a finite groupoid over the three quotient endpoint colours.

The total side-output sum is also compositional: if the intermediate full continuation colour is `x`, then

$$
(x_0+x)+(x+x_n)=x_0+x_n.
$$

## 7. Backtracks and reduced normal form

An immediate backtrack in the triangle walk has the form

$$
x_{t-1},x_t,x_{t-1}.
$$

The two corresponding side-output colours are equal:

$$
x_{t-1}+x_t
=
x_t+x_{t-1}.
$$

Conversely, two consecutive equal side-output colours force an immediate backtrack.

### Proposition 7.1 — algebraically neutral backtrack

Deleting an immediate backtrack:

1. preserves the two endpoint continuation colours;
2. preserves the interval monodromy;
3. preserves the total side-output colour;
4. removes two turns.

#### Proof

The two local transpositions are equal and square to the identity.  The two equal side-output colours also sum to zero.  ∎

After all immediate backtracks are deleted, a nonempty reduced walk on a triangle is forced by its first oriented edge: at every later step, the walk must continue around the triangle rather than reverse.  Consequently its continuation colours and side-output colours are periodic of period three.

### Corollary 7.2 — interval normal form

Every scalar interval word reduces algebraically to:

1. its two endpoint colours;
2. one orientation of the three-cycle;
3. a reduced winding length;
4. a collection of deleted backtrack pairs.

Only the endpoint colours and turn parity survive in the finite quotient monodromy.  The reduced winding number and the locations of side attachments remain potentially unbounded physical data.

Deletion here is an algebraic word reduction, not a valid graph replacement.  The two side edges of a backtrack may have different external attachments even though they carry the same flow colour.

## 8. Four-interval blocks

A closed scalar component meeting the witness in four `g`-edges has:

- a cyclic order of those four witness edges;
- four scalar intervals between successive witness edges;
- one eighteen-state quotient transfer for each interval;
- one ordered side-output word on each interval.

### Corollary 8.1 — finite algebraic block state

After the cyclic order and endpoint quotient labels are fixed, the quotient monodromy and total side-output sums of the entire four-interval block lie in a finite state space independent of interval lengths.

The only unbounded information not captured by this algebraic block state is:

- reduced winding along the three-colour triangle;
- the ordered side-output word;
- the graph components attached to those side edges;
- simultaneous compatibility with the other three scalar sheets.

## 9. Consequence for the quartic frontier

The physical split-or-peel problem can now be separated into two layers.

### Closed finite layer

The following are finite:

- the canonical `K_6` defect gadget of the terminal distribution;
- cyclic order of the four witness edges in a block;
- endpoint aligned/crossed labels;
- the eighteen-state transfer of each scalar interval;
- total side-output colours;
- the two-vertex shell rotations in a concentrated peel.

### Remaining unbounded layer

The remaining obstruction is the side-semantic word:

$$
\boxed{
\text{periodic reduced Tait word}
+
\text{external attachments}
+
\text{simultaneous four-sheet compatibility}.
}
$$

A composition theorem must show that a long side-semantic word either:

1. contains a composition-safe neutral backtrack;
2. contains two repeated enriched transfer states with matching attachments;
3. exposes a smaller cyclic separator;
4. yields a bounded four-pole transfer;
5. or winds irreducibly in the canonical `D_8` class.

The scalar-flow algebra itself is no longer unbounded.

## 10. Reliability boundary

Proved here:

- every scalar interval is a walk on a three-state colour triangle;
- the full and quotient side-output sums telescope to the endpoint sums;
- interval quotient monodromy is determined by two endpoint colours and one parity bit;
- there are exactly eighteen oriented quotient transfer states;
- immediate triangle backtracks are algebraically neutral;
- reduced interval words are periodic three-colour walks.

Not proved here:

- that an algebraically neutral backtrack is composition-safe in the graph;
- that eighteen-state equality suffices for replacement when side attachments differ;
- finite classification of enriched side-semantic words;
- simultaneous shell removal across all four sheets;
- the global five-support theorem.

No Lean, independent-review, peer-review, publication, release, arXiv, or DOI status is implied.
