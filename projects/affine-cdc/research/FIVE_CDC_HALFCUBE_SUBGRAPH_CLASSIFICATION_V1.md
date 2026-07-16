# Exact half-cube compression classification for subgraphs of `K_8`

**Programme:** `AffineCDC — Research Lead`  
**Status:** theorem-level research checkpoint; not canonical pending Director review and literature audit  
**Parents:** `FIVE_CDC_SOURCE_DEPENDENT_HALFCUBE_COMPRESSION_V1.md`, `FIVE_CDC_K6_LABEL_GRAPH_OBSTRUCTION_V1.md`

## 1. Statement

Let

\[
\mathscr A_5
\]

be the graph on `F_2^5` in which two words are adjacent exactly when their
Hamming distance is two. Its two parity components are isomorphic; write

\[
H_5=\{x\in F_2^5:\operatorname{wt}(x)\equiv0\pmod2\}
\]

for the even component.

Let `J` be a graph on a fixed eight-element vertex set, equivalently a spanning
subgraph of `K_8`. Put

\[
\overline J:=K_8-J.
\]

### Theorem 1.1 — exact eight-vertex half-cube classification

The following are equivalent.

1. There is a graph homomorphism
   \[
   J\longrightarrow\mathscr A_5.
   \]
2. The complement `\overline J` contains at least one of
   \[
   \boxed{3K_2,\qquad K_3\sqcup K_2,\qquad K_4.}
   \]
3. The graph `J` contains neither
   \[
   \boxed{K_6\qquad\text{nor}\qquad K_8-C_5}
   \]
   as a subgraph.

Here all containments are ordinary, not necessarily induced, subgraph
containments.

Consequently, an AffineCDC root flow with used-label graph `J_g` admits a
source-dependent cut-continuous compression to five supports if and only if
`J_g` contains neither `K_6` nor `K_8-C_5`.

This proves the finite classification previously observed only by private
enumeration.

## 2. The conflict graph

Suppose first that

\[
a:V(J)\longrightarrow\mathscr A_5
\]

is a homomorphism. Each connected component of `J` lies in one parity component
of `\mathscr A_5`; translating the image of each connected component separately
allows us to assume

\[
a(V(J))\subseteq H_5.
\]

Define the **conflict graph** `C_a` on `V(J)` by joining distinct vertices `u,v`
when

\[
a(u)=a(v)
\qquad\text{or}\qquad
\operatorname{wt}(a(u)+a(v))=4.
\]

Two distinct even words have distance two or four. Hence a pair is a conflict
exactly when its images are not adjacent in `\mathscr A_5`. Since `a` is a
homomorphism,

\[
\boxed{C_a\subseteq\overline J.}
\]

Thus the theorem reduces to determining what every conflict graph on eight
positions must contain.

## 3. A general eight-vertex graph lemma

### Lemma 3.1

Let `C` be a graph on eight vertices containing none of

\[
3K_2,\qquad K_3\sqcup K_2,\qquad K_4.
\]

Then exactly one of the following holds.

1. `\alpha(C)\geq6`;
2. `C=C_5\sqcup3K_1`.

#### Proof

The exclusion of `3K_2` gives

\[
\nu(C)\leq2.
\]

First assume that `C` is triangle-free.

If `C` is bipartite, Koenig's theorem gives

\[
\tau(C)=\nu(C)\leq2,
\]

and therefore

\[
\alpha(C)=8-\tau(C)\geq6.
\]

If `C` is not bipartite, let `P` be a shortest odd cycle. Triangle-freeness and
`\nu(C)\leq2` force

\[
P=C_5.
\]

No edge may meet a vertex outside this five-cycle. An edge entirely outside the
cycle, together with a matching of size two in `C_5`, would give `3K_2`. An edge
joining an outside vertex to a cycle vertex `v`, together with the two-edge
matching in `C_5-v=P_4`, would again give `3K_2`. There are no chords because
`C` is triangle-free. Hence

\[
C=C_5\sqcup3K_1.
\]

Now suppose that `C` contains a triangle

\[
T=\{a,b,c\}.
\]

Because `K_3\sqcup K_2` is forbidden, the five vertices outside `T` form an
independent set.

We claim that one vertex of `T` has no neighbour outside `T`. If every outside
vertex had at most one neighbour in `T` and all three vertices of `T` had an
outside neighbour, those three neighbours would be distinct and would give a
matching of size three. Therefore some outside vertex `s` is adjacent to two
vertices, say `a,b`, of `T`. It is not adjacent to `c`, since otherwise
`T\cup\{s\}` would be a `K_4`. If `c` had another outside neighbour `t`, then

\[
\{a,b,s\}\sqcup\{c,t\}
\]

would be a `K_3\sqcup K_2`. Thus `c` has no outside neighbour. Consequently

\[
\{c\}\cup(V(C)\setminus T)
\]

is an independent set of size six. ∎

## 4. The Clebsch conflict graph

On `H_5`, define a graph `\mathscr C_5` by joining distinct words when their
Hamming distance is four. This is the conflict graph on distinct target words;
it is the Clebsch graph.

### Lemma 4.1 — elementary Clebsch parameters

The graph `\mathscr C_5` is strongly regular with parameters

\[
\boxed{(16,5,0,2).}
\]

In particular it is triangle-free.

#### Proof

Translate one vertex to zero.

Its neighbours are the five weight-four words, so the degree is five. Two
adjacent vertices may be normalized to `0` and a weight-four word `y`. A common
neighbour would be a weight-four word `z` for which `z+y` also has weight four.
Two four-subsets of a five-set have intersection at least three, whereas
`\operatorname{wt}(z+y)=4` would require intersection two. Thus adjacent
vertices have no common neighbour.

Two nonadjacent distinct vertices may be normalized to `0` and a weight-two word
`y`. A common neighbour is a weight-four word `z` satisfying
`\operatorname{wt}(z+y)=4`, which is equivalent to `z` containing exactly one of
the two coordinates of `y`. There are exactly two such words. ∎

### Lemma 4.2 — maximum distance-two code

A set of pairwise adjacent vertices in `\mathscr A_5` has cardinality at most
five.

#### Proof

Translate one word to zero. Every other word then has weight two. Identifying
weight-two words with two-subsets of `[5]`, pairwise distance two means that the
corresponding two-subsets are pairwise intersecting. Such a family is contained
in a star, of size at most four, or is the three edges of a triangle. Including
the zero word gives at most five words. ∎

### Lemma 4.3 — an induced pentagon has one common nonneighbour

Let `S` induce a five-cycle in `\mathscr C_5`. Exactly one vertex of
`\mathscr C_5-S` has no neighbour in `S`.

#### Proof

For `i=0,1,2`, let `n_i` be the number of vertices outside `S` having exactly
`i` neighbours in `S`. Since `\mathscr C_5` is triangle-free, the neighbours of
an outside vertex form an independent set in `C_5`, so there are at most two.
Thus

\[
n_0+n_1+n_2=11.
\]

Each cycle vertex has degree five and two neighbours inside the cycle, so

\[
n_1+2n_2=5(5-2)=15.
\]

There are five nonadjacent pairs of vertices in the cycle. By the parameter
`\mu=2`, each has two common neighbours in `\mathscr C_5`; exactly one is the
intermediate cycle vertex, leaving exactly one outside common neighbour. An
outside vertex with two neighbours in `S` contributes to exactly one such pair.
Hence

\[
n_2=5.
\]

The displayed equations now give

\[
n_1=5,
\qquad
n_0=1.
\]

∎

## 5. Every eight-word conflict graph contains a template

### Theorem 5.1 — conflict-template theorem

For every map

\[
a:X\longrightarrow H_5,
\qquad |X|=8,
\]

the conflict graph `C_a` contains at least one of

\[
\boxed{3K_2,\qquad K_3\sqcup K_2,\qquad K_4.}
\]

#### Proof

Assume not. Lemma 3.1 applies.

If `\alpha(C_a)\geq6`, then six positions receive distinct words with no
conflict. Their images are pairwise at distance two, giving a six-clique in
`\mathscr A_5`, contrary to Lemma 4.2.

The only other possibility is

\[
C_a=C_5\sqcup3K_1.
\]

This graph is triangle-free, so all eight image words are distinct. Hence
`C_a` is an induced subgraph of the Clebsch graph `\mathscr C_5`. Its five-cycle
would then have three common nonneighbours, contradicting Lemma 4.3, which says
there is exactly one. ∎

## 6. Proof of the exact classification

We first prove `(1)⇒(2)`. Given a homomorphism `a:J→\mathscr A_5`, normalize its
component images into `H_5`. Its conflict graph satisfies

\[
C_a\subseteq\overline J.
\]

By Theorem 5.1, `C_a`, and therefore `\overline J`, contains one of the three
templates.

For `(2)⇒(1)`, fix a five-clique in `\mathscr A_5`, for example

\[
0,\quad e_1+e_2,\quad e_1+e_3,\quad e_1+e_4,\quad e_1+e_5.
\]

If `\overline J` contains `3K_2`, assign the same clique word to the two endpoints
of each of the three matching edges and assign the other two vertices two further
distinct clique words. The conflict graph is exactly `3K_2`.

If `\overline J` contains `K_3\sqcup K_2`, assign one clique word to the three
triangle vertices, a second word to the two edge vertices, and three further
distinct clique words to the remaining vertices. The conflict graph is exactly
`K_3\sqcup K_2`.

If `\overline J` contains `K_4`, assign one clique word to those four vertices and
four distinct further clique words to the remaining vertices. The conflict graph
is exactly `K_4`.

In every case all conflicts lie in `\overline J`, so adjacent vertices of `J`
map to adjacent vertices of `\mathscr A_5`.

It remains to compare `(2)` and `(3)`. Apply Lemma 3.1 to `\overline J`. If it
contains none of the three templates, then either

\[
\alpha(\overline J)\geq6,
\]

which means that `J` contains `K_6`, or

\[
\overline J=C_5\sqcup3K_1,
\]

which means that `J=K_8-C_5`.

Conversely, if `J` contains `K_6`, then no homomorphism `J→\mathscr A_5` exists,
because `\mathscr A_5` has clique number five by Lemma 4.2. If `J` contains
`K_8-C_5`, then a homomorphism would restrict to one on `K_8-C_5`; but its
complement is `C_5\sqcup3K_1`, which contains none of the three templates, so the
already proved equivalence `(1)⇔(2)` excludes such a homomorphism. Applying
`(1)⇔(2)` once more shows that in either case `\overline J` contains no template.
This proves Theorem 1.1. ∎

## 7. Consequences for AffineCDC root compression

Let

\[
g:E(G)\longrightarrow E(K_8)
\]

be an AffineCDC root flow and `J_g` its used-label graph. The source-dependent
half-cube theorem gives

\[
G\text{ has a five-support cover obtained from }g
\iff
J_g\longrightarrow\mathscr A_5.
\]

Therefore

\[
\boxed{
g\text{ compresses to five supports}
\iff
K_6\nsubseteq J_g
\text{ and }
K_8-C_5\nsubseteq J_g.
}
\]

Equivalently, compression succeeds exactly when the unused-root graph
`K_8-J_g` contains one of

\[
3K_2,\qquad K_3\sqcup K_2,\qquad K_4.
\]

The earlier unused-three-matching criterion is therefore only the first of three
complete positive templates.

## 8. Conceptual position

The target `\mathscr A_5` is the complement of the Clebsch graph on each parity
component. The exact classification is therefore a small Ramsey-type rigidity
statement:

- eight proposed support indices cannot avoid producing one of three repetition
  or distance-four conflict templates;
- the only abstract template-free eight-vertex graphs are controlled by a
  six-point independent set or a pentagon;
- the half-cube excludes the first by its clique number and the second by the
  strongly regular pentagon count.

Thus source-dependent five-support compression is governed by two and only two
dense used-label obstructions, `K_6` and `K_8-C_5`.

The next problem is no longer to classify target compression. It is to understand
whether the Hamming-Lagrangian moduli of AffineCDC root lifts can always be moved
away from these two dense regions, or whether source-graph decomposition permits
compatible piecewise target maps when one fixed root flow remains obstructed.
