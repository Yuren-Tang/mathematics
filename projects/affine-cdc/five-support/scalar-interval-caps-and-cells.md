# Elementary scalar-interval caps and periodic triangle cells

## 1. Scope

This chapter classifies an **elementary scalar interval**: a non-`g` path between consecutive `g`-incidences in one full scalar circuit, with no internal `g`-edge.

It does not assert that consecutive witness edges in `C\cap\eta` are consecutive `g`-edges of `C`.  A witness-to-witness arc may contain arbitrarily many edges of `E_g\setminus\eta` and therefore a chain of elementary intervals.  Those chains are represented by walks in the physical `g`-component transition quotient.

Within one elementary interval:

- an immediate colour backtrack is a standard two-vertex Tait cap with a complete four-sheet routing table;
- a backtrack-free interval is forced to be a periodic chain of three-turn triangle cells.

## 2. Fixed-sheet colour triangle

Fix a scalar sheet `H_\phi`.  Its three selected non-`g` colours are

$$
A_\phi=\{a,b,c\}.
$$

Their quotient images are the three nonzero elements of `U`, so

$$
\bar a+\bar b+\bar c=0.
$$

Since all three have scalar value one and their sum has quotient zero,

$$
\boxed{a+b+c=g.}
$$

The three nonzero omitted colours are

$$
W_\phi^\times
=
\{a+b,b+c,c+a\}
=
\{g+c,g+a,g+b\}.
$$

They are distinct and sum to zero.

## 3. Immediate backtracks

Suppose two consecutive internal vertices have continuation word

$$
a,b,a.
$$

Let the vertices be `v,w`, joined by the middle path edge of colour `b`.  The two outer path semiedges have colour `a`, and both side semiedges have colour

$$
d=a+b.
$$

### Theorem 3.1 — backtrack cap

If the two side incidences are distinct edges, the subgraph on `v,w` is the standard cubic two-vertex four-pole with:

- one internal edge of colour `b`;
- two boundary semiedges of colour `a`;
- two boundary semiedges of colour `d`.

If the side incidences are the same edge, the configuration is a bounded two-pole with two parallel internal edges.

#### Proof

Both cubic vertices have the distinct zero-sum colour triple `(a,b,d)`. ∎

## 4. Exact four-sheet cap routing

The plane

$$
L=\langle a,b\rangle=\{0,a,b,d\}
$$

does not contain `g`.  Restriction from

$$
\Lambda_g=\{\lambda:\lambda(g)=1\}
$$

to `L^*` is therefore a bijection.  The four value triples on `(a,b,d)` are

$$
(0,0,0),
\quad
(1,0,1),
\quad
(0,1,1),
\quad
(1,1,0).
$$

Label the boundary ports `a_L,d_L` at `v` and `a_R,d_R` at `w`.

### Theorem 4.1 — cap routing table

$$
\begin{array}{c|c}
(\lambda(a),\lambda(b),\lambda(d))&\text{boundary routing}\\
\hline
(0,0,0)&\text{empty}\\
(1,0,1)&(a_Ld_L)\mid(a_Rd_R)\\
(0,1,1)&d_L\longleftrightarrow d_R\\
(1,1,0)&a_L\longleftrightarrow a_R.
\end{array}
$$

Thus an elementary backtrack exposes exactly the standard finite cap used in the ten-state four-pole programme.  The table does not itself justify deleting or smoothing the cap.

## 5. Backtrack-free elementary intervals

Let

$$
x_0,x_1,\ldots,x_n
$$

be the continuation-colour word, with no immediate backtrack:

$$
x_{t-1}\ne x_{t+1}.
$$

### Theorem 5.1 — forced periodicity

After choosing the first orientation, the word is

$$
\boxed{a,b,c,a,b,c,\ldots}
$$

or its reverse.  The side-output word is

$$
\boxed{a+b,b+c,c+a,a+b,b+c,c+a,\ldots}.
$$

#### Proof

After two distinct colours, the next colour is neither the current nor the previous one; in a three-element set it is forced to be the third. ∎

## 6. Periodic triangle cells

One full period has continuation word

$$
a,b,c,a
$$

and three side ports of colours

$$
a+b,
\qquad
b+c,
\qquad
c+a.
$$

### Theorem 6.1 — triangle cell

A full three-turn period is a bounded five-pole with:

1. two path boundary semiedges of the same colour `a`;
2. three side boundary colours equal to the three nonzero elements of `\ker\lambda_\phi`;
3. zero total side-output colour;
4. quotient monodromy equal to the nontrivial element stabilising `\bar a` in `GL(U)`.

Two consecutive cells have identity quotient monodromy and each side colour occurs twice.  Their external attachments may still differ.

## 7. Elementary cap-or-cell normal form

### Theorem 7.1

Every elementary scalar interval satisfies one of:

1. it contains a standard two-vertex backtrack cap;
2. it is a bounded prefix, followed by a chain of full three-turn triangle cells, followed by a bounded suffix.

No new flow colour or quotient monodromy state appears as the number of cells grows.

## 8. Witness arcs

Let `e,e'\in C\cap\eta` be consecutive witness edges on a scalar circuit `C`.  The arc from `e` to `e'` may pass through edges

$$
h_1,\ldots,h_r\in E_g\setminus\eta.
$$

It is consequently a concatenation of elementary cap-or-cell segments, separated by the `g`-edge transitions at those `h_j`.

### Corollary 8.1 — corrected physical normal form

Every witness-to-witness arc becomes, after passage to the transition quotient:

- a walk through quotient `g`-edges and transition vertices;
- with each non-`g` transition path carrying either a bounded cap or a periodic triangle-cell chain.

There is no claim that one quartic block has only four elementary intervals.  It has four witness arcs, each of which may contain an unbounded number of elementary segments.

## 9. Consequence for the frontier

The elementary non-`g` part is rigid.  Remaining unboundedness lies in:

- intervening `g`-edges outside `\eta`;
- transition matchings of the non-`g` components;
- external attachments of periodic cells;
- simultaneous compatibility of all four transition systems.

These data are retained by `\Gamma_g`.  A successful theorem should force a cut or transition split there; every internal quotient cut then lifts exactly to the original four-pole.

## 10. Reliability boundary

Proved here:

- elementary backtracks are standard two-vertex Tait caps;
- the exact restrictions of all four scalar sheets to the cap;
- backtrack-free elementary intervals are three-periodic;
- every period is a bounded triangle cell;
- every elementary interval has the cap-or-cell normal form.

Explicitly not claimed:

- that consecutive witness edges are consecutive `g`-edges;
- that a quartic block has four elementary intervals;
- composition-safe removal of caps or cells;
- bounded length of a witness arc;
- the global five-support theorem.

No Lean, independent-review, peer-review, publication, release, arXiv, or DOI status is implied.
