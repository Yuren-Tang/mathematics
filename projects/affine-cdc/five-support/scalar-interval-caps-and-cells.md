# Scalar interval backtrack caps and periodic triangle cells

## 1. Purpose

The scalar-interval transfer theorem reduces every non-`g` interval to a walk on the three continuation colours of one scalar sheet.  Its quotient monodromy has only eighteen states, but the ordered side-attachment word can still be arbitrarily long.

This chapter gives the exact physical normal form of that word.

- An immediate colour backtrack is not merely algebraically neutral.  It is a standard two-vertex Tait cap with a complete four-sheet routing table.
- If no backtrack occurs, the interval is forced to run periodically around the three-colour triangle.  Every three turns form a bounded cell whose three side colours are the three nonzero elements of the complementary scalar plane and sum to zero.

Hence every scalar interval contains a bounded four-pole cap, or is a chain of bounded periodic triangle cells with bounded prefix and suffix.

## 2. Fixed-sheet colour triangle

Fix a scalar sheet `H_\phi`.  Its three non-`g` selected colours form

$$
A_\phi
=
\{a,b,c\}.
$$

Their quotient images are the three nonzero elements of `U\cong\mathbf F_2^2`, so

$$
\bar a+\bar b+\bar c=0.
$$

Since each of `a,b,c` has scalar value one and their sum has quotient zero,

$$
\boxed{a+b+c=g.}
$$

The three nonzero colours in the complementary scalar plane are therefore

$$
W_\phi^\times
=
\{a+b,b+c,c+a\}
=
\{g+c,g+a,g+b\}.
$$

They are distinct and sum to zero.

## 3. Immediate backtracks

Consider two consecutive internal vertices of a scalar interval whose continuation-colour sequence is

$$
a,b,a.
$$

Let the two vertices be `v,w`, joined by the middle path edge of colour `b`.  The two outer path semiedges have colour `a`.  By Kirchhoff conservation, both side semiedges have the same colour

$$
d=a+b.
$$

If the two side incidences are distinct edges, the subgraph on `v,w` is a cubic four-pole with:

- one internal edge of colour `b`;
- two boundary semiedges of colour `a`;
- two boundary semiedges of colour `d`.

### Theorem 3.1 — backtrack cap theorem

Every immediate scalar-colour backtrack exposes the standard two-vertex Tait cap with boundary colour pattern

$$
(a,a,d,d),
\qquad
b=a+d.
$$

If the two side incidences are the same edge, the configuration degenerates to a bounded two-pole with two parallel internal edges; this is an even smaller interface.

#### Proof

The two cubic vertices have incident colour triples

$$
(a,b,d),
$$

and

$$
(b,a,d).
$$

In each case the three values are distinct nonzero vectors summing to zero.  The asserted four-pole is exactly the induced two-vertex multipole.  ∎

## 4. Complete four-sheet routing table of the cap

The plane

$$
L=\langle a,b\rangle
=
\{0,a,b,d\}
$$

does not contain `g`: none of `a,b,d` equals `g`, because the two vertices are internal to a non-`g` scalar interval.

Therefore restriction from

$$
\Lambda_g
=
\{\lambda\in V^*:\lambda(g)=1\}
$$

to `L^*` is a bijection.  Across the four scalar sheets, the value triples on `(a,b,d)` are exactly

$$
(0,0,0),
\quad
(1,0,1),
\quad
(0,1,1),
\quad
(1,1,0).
$$

Label the boundary semiedges

$$
a_L,d_L
$$

at `v`, and

$$
a_R,d_R
$$

at `w`.

### Theorem 4.1 — exact cap routing

The four scalar sheets restrict to the backtrack cap as follows:

$$
\begin{array}{c|c|c}
(\lambda(a),\lambda(b),\lambda(d))
&\text{selected cap edges}
&\text{boundary routing}\\
\hline
(0,0,0)&\varnothing&\text{empty}\\
(1,0,1)&a_L,d_L,a_R,d_R
&(a_Ld_L)\mid(a_Rd_R)\\
(0,1,1)&b,d_L,d_R
&d_L\mid d_R\\
(1,1,0)&a_L,b,a_R
&a_L\mid a_R.
\end{array}
$$

Here the last two rows denote the unique through path joining the indicated equal-colour boundary pair.

#### Proof

At each cubic vertex a scalar sheet selects either zero or two incident edges.  Substituting the four value triples gives the four restrictions directly.  When `b` is selected, it joins the two vertices and creates the displayed through path.  When `b` is absent, the selected pair is local at each vertex.  ∎

### Corollary 4.2 — bounded four-pole certificate

An immediate backtrack yields a completely explicit bounded four-pole transfer object.  It is the same two-vertex cap used in cap forcing, now detected internally by scalar interval dynamics.

This does not by itself prove that deleting or smoothing the cap preserves a five-support cover; the four sheets realize different pairings.  It does place the configuration inside the already finite ten-state four-pole language.

## 5. Backtrack-free intervals

Let

$$
x_0,x_1,\ldots,x_n
$$

be the continuation-colour word of a scalar interval.  Assume it has no immediate backtrack:

$$
x_{t-1}\ne x_{t+1}
$$

whenever both sides are defined.

### Theorem 5.1 — forced three-periodicity

After choosing the orientation of the first transition, the continuation colours are forced:

$$
\boxed{
 a,b,c,a,b,c,\ldots
}
$$

or the reverse cyclic order.

The side-output colours are correspondingly

$$
\boxed{
 a+b,\ b+c,\ c+a,\ a+b,\ b+c,\ c+a,\ldots
}
$$

and have period three.

#### Proof

After two distinct consecutive colours, the next colour cannot equal the current colour and cannot equal the previous colour by the no-backtrack assumption.  Since `A_\phi` has exactly three elements, it must be the third colour.  Induction gives the periodic word.  The side-output formula follows from the local turn law.  ∎

## 6. Periodic triangle cells

A full period consists of the continuation word

$$
a,b,c,a.
$$

It contains three internal vertices and three side semiedges with colours

$$
a+b,
\qquad
b+c,
\qquad
c+a.
$$

### Theorem 6.1 — triangle-cell theorem

Every full three-turn period is a bounded five-pole cell with:

1. two path boundary semiedges of the same colour `a`;
2. three side boundary semiedges carrying the three distinct nonzero colours of `\ker\lambda_\phi`;
3. zero total side-output colour:
   $$
   (a+b)+(b+c)+(c+a)=0;
   $$
4. quotient monodromy equal to the nontrivial element of the stabiliser of `\bar a` in `GL(U)`.

#### Proof

The first three statements follow from the periodic word and cancellation.  The cell has three turns, so its monodromy is odd.  It begins and ends at `\bar a`, hence lies in the order-two stabiliser of `\bar a`; being odd, it is the nontrivial element.  ∎

The three side colours form a root triangle in the binary plane `\ker\lambda_\phi`.  Thus a periodic cell carries one bounded Tait triangle of side outputs.

### Corollary 6.2 — paired cells

Two consecutive full cells have:

- identity quotient monodromy;
- equal path endpoint colour;
- each of the three side-output colours occurring twice;
- zero total side-output colour.

They form a six-turn algebraically neutral periodic block.  Their external side attachments may still differ, so algebraic neutrality is not yet a valid graph deletion.

## 7. Complete interval dichotomy

### Theorem 7.1 — cap-or-periodic-chain normal form

Every scalar interval satisfies one of the following.

1. **Backtrack case.**  It contains a standard two-vertex Tait cap with the exact four-sheet routing table of Theorem 4.1.
2. **Reduced case.**  It has no backtrack and is a bounded prefix, followed by a chain of full three-turn triangle cells, followed by a bounded suffix.

The prefix and suffix together contain fewer than six turns.

#### Proof

If a backtrack occurs, Theorem 3.1 applies.  Otherwise Theorem 5.1 gives a periodic continuation word.  Divide its number of turns by three and isolate the incomplete initial and final portions according to the chosen cell boundary.  By shifting the cell origin, the total incomplete remainder can be taken to have fewer than six turns.  ∎

### Corollary 7.2 — exact remaining unbounded object

After bounded cap interfaces are separated, the only unbounded scalar interval is a chain of identical colour-pattern triangle cells.  Its unbounded data consist solely of:

- the number of cells;
- the external graph attached to the three side semiedges of each cell;
- the simultaneous way those side edges lie in the other scalar sheets.

No new flow colour or monodromy state appears as the chain grows.

## 8. Relation to the concentrated nucleus shell

Every distinguished block in a concentrated peel has four scalar intervals.  Applying the cap-or-periodic-chain theorem to each interval gives:

1. a bounded internal Tait cap, which enters the finite four-pole transfer language; or
2. a periodic chain of triangle cells connecting two shell witness edges.

Consequently, if no bounded cap is exposed, every new shell interval is periodic.  The entire concentrated nucleus layer is then a bounded `D_8` shell whose ports are joined by periodic Tait-cell chains.

The next theorem must analyse the attachments along those chains.  A successful statement would prove that a sufficiently long chain either:

- repeats one enriched cell state with matching side semantics and can be replaced;
- exposes a smaller cyclic separator through its side attachments;
- splits in the transition matroid;
- or realizes the irreducible physical `D_8` class.

## 9. Reliability boundary

Proved here:

- immediate scalar backtracks are standard two-vertex Tait caps;
- the exact restrictions of all four scalar sheets to such a cap;
- backtrack-free scalar intervals are forced three-periodic walks;
- every full period is a bounded triangle cell with zero side-output sum;
- every scalar interval is a bounded cap case or a periodic triangle-cell chain with bounded ends.

Not proved here:

- composition-safe removal of the backtrack cap;
- replacement of two periodic cells with different side attachments;
- a finite complete state for the external attachments;
- simultaneous reduction of all four intervals in a nucleus shell;
- the global five-support theorem.

No Lean, independent-review, peer-review, publication, release, arXiv, or DOI status is implied.
