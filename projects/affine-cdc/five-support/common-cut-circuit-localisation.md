# Common-cut circuit localisation

## 1. Purpose

The full-rank route-locked atom endpoint produces a nowhere-zero flow

$$
c:E(Q)\longrightarrow V\setminus\{0\},
\qquad
V\cong\mathbf F_2^3,
$$

with all four terminal values equal to one colour $g$.  For

$$
\Lambda_g=\{\lambda\in V^*: \lambda(g)=1\},
$$

the four scalar relative even subgraphs all route the terminals as

$$
12\mid34.
$$

In the nonflat sector, curvature duality gives a support-minimal set

$$
\eta\subseteq E_g,
\qquad
E_g=\{e:c(e)=g\},
$$

which is a cut in every scalar sheet and has odd terminal parity.

This chapter identifies the exact finite-dimensional object carried by such a witness.  The witness is not an arbitrary graph cut.  It is a curvature-odd circuit of a four-partite scalar-component incidence matroid.  A rank count then leaves only three possibilities:

1. one enriched $g$-edge atom;
2. a two-edge scalar transition interval;
3. a rigid quartic near-resolution core of size $4k+1$.

The third case is the only remaining unbounded nonflat incidence pattern.

## 2. Scalar-component incidence

For each $\lambda\in\Lambda_g$, write the scalar sheet as

$$
H_\lambda
=
P^{12}_\lambda
\sqcup
P^{34}_\lambda
\sqcup
\bigsqcup_{C\in\mathcal Z_\lambda} C,
$$

where $P^{12}_\lambda$ and $P^{34}_\lambda$ are the two terminal paths and $\mathcal Z_\lambda$ is the set of closed scalar components.

Every edge of $E_g$ belongs to every $H_\lambda$.  Hence, for each sheet, a $g$-edge belongs to exactly one of:

- $P^{12}_\lambda$;
- $P^{34}_\lambda$;
- one closed component $C\in\mathcal Z_\lambda$.

Put

$$
\mathcal Z
=
\bigsqcup_{\lambda\in\Lambda_g}
\mathcal Z_\lambda.
$$

Define the binary closed-component incidence matrix

$$
A=A(c)
\in
\mathbf F_2^{\mathcal Z\times E_g}
$$

by

$$
A_{C,e}=1
\quad\Longleftrightarrow\quad
e\in C.
$$

The row blocks indexed by one fixed $\lambda$ have pairwise disjoint supports.  Equivalently, $A$ is the incidence matrix of a rank-at-most-four, four-partite hypergraph:

- the vertices are the closed scalar components;
- a $g$-edge $e$ is incident with the closed component containing it in each sheet in which it is closed;
- in each of the four parts, a hyperedge meets at most one vertex.

Choose the standard side convention:

- side $0$ on every $P^{12}_\lambda$;
- side $1$ on every $P^{34}_\lambda$;
- side $0$ on every closed scalar component.

This gives one representative

$$
\omega\in\mathbf F_2^{E_g}
$$

of the curvature class, with

$$
\omega_e
=
\sum_{\lambda\in\Lambda_g}
1_{e\in P^{34}_\lambda}
\pmod2.
$$

Changing a closed-cycle side adds the corresponding row of $A$.  Therefore the pairing of $\omega$ with any vector in $\ker A$ is gauge-independent.

## 3. Common cuts are the kernel of the component matrix

### Lemma 3.1 — sheet-cut criterion

For a subset $S\subseteq E_g$, the following are equivalent:

1. $S$ is a cut vector in every scalar sheet $H_\lambda$;
2. $S$ meets every closed scalar component evenly;
3. its characteristic vector $x_S$ satisfies
   $$
   Ax_S=0.
   $$

#### Proof

A scalar sheet is a disjoint union of two paths and closed cycles.  A subset of a path is always a cut vector on that path.  On a cycle, a subset is a cut vector exactly when it has even cardinality.  Applying this independently to all components of all four sheets gives the equivalence.  ∎

Thus the dual witnesses for nonzero curvature are precisely the vectors

$$
x\in\ker A
$$

such that

$$
\langle\omega,x\rangle=1.
$$

## 4. Support-minimal witnesses are matroid circuits

### Theorem 4.1 — odd-circuit theorem

Let $\eta\subseteq E_g$ satisfy

$$
A1_\eta=0,
\qquad
\langle\omega,1_\eta\rangle=1.
$$

Then $\eta$ is support-minimal among all such witnesses if and only if:

1. $\eta$ is a circuit of the binary column matroid $M(A)$;
2. its curvature weight is odd:
   $$
   \langle\omega,1_\eta\rangle=1.
   $$

#### Proof

Assume first that $\eta$ is support-minimal.  Since $A1_\eta=0$, the columns indexed by $\eta$ are dependent.  Suppose that a nonempty proper subset $U\subsetneq\eta$ also satisfies

$$
A1_U=0.
$$

If $\langle\omega,1_U\rangle=1$, then $U$ is a smaller odd witness.  If $\langle\omega,1_U\rangle=0$, then

$$
A1_{\eta\setminus U}=0,
\qquad
\langle\omega,1_{\eta\setminus U}\rangle=1,
$$

so $\eta\setminus U$ is a smaller odd witness.  Both alternatives contradict minimality.  Hence no proper nonempty subset is dependent, and $\eta$ is a circuit of $M(A)$.

Conversely, let $\eta$ be a circuit with odd curvature weight.  Any proper nonempty subset is independent and therefore cannot be a common-cut witness.  Thus $\eta$ is support-minimal among odd witnesses.  ∎

### Corollary 4.2 — exact rank

If

$$
n=|\eta|,
$$

then

$$
\operatorname{rank} A|_\eta=n-1.
$$

The common-cut localisation problem is therefore a circuit-localisation problem in a four-partite binary incidence matroid.

## 5. The physical-cut expectation is false

The common-cut theorem does not imply that $\eta$ is a cut in the underlying four-pole $Q$.

### Proposition 5.1 — scalar-common cut without physical cut

In the exact full-rank nonflat witness from the context-limit recovery certificate, the unique $g$-edge is

$$
e=78.
$$

It lies on a terminal path in each of the four scalar sheets, with side word

$$
0100,
$$

so

$$
\eta=\{78\}
$$

is the support-minimal common-cut witness.  Nevertheless $78$ is not a bridge of the underlying graph.  After deleting it, there remain, for example, the paths

$$
7-2-9-8
$$

and

$$
7-5-6-4-8.
$$

Hence

$$
\boxed{
\eta\text{ common cut in all scalar sheets}
\not\Rightarrow
\eta\text{ cut in }Q.
}
$$

The former open wording “prove that $\eta$ is an underlying cut” must therefore be retired.  Any localisation theorem must retain the scalar-component or transition structure.

## 6. Terminal counts and closed-component blocks

Fix a support-minimal witness $\eta$ and put $n=|\eta|$.  For each $\lambda\in\Lambda_g$, define:

$$
t_\lambda
=
|\eta\cap(P^{12}_\lambda\cup P^{34}_\lambda)|,
$$

and let

$$
r_\lambda
=
|\{C\in\mathcal Z_\lambda:C\cap\eta\ne\varnothing\}|.
$$

Because every closed component meets $\eta$ evenly,

$$
\boxed{
 t_\lambda\equiv n\pmod2.
}
$$

Moreover, if no closed component meets $\eta$ in exactly two edges, every nonempty $C\cap\eta$ has even cardinality at least four, so

$$
\boxed{
 r_\lambda
 \le
 \left\lfloor\frac{n-t_\lambda}{4}\right\rfloor.
}
$$

## 7. The localisation trichotomy

### Theorem 7.1 — singleton, transition pair, or quartic core

Let $\eta$ be a support-minimal odd-curvature witness.  Exactly one of the following holds.

#### I. Singleton atom

$$
|\eta|=1.
$$

The unique edge lies on a terminal path in every scalar sheet and on no closed scalar component.

#### II. Two-edge scalar transition

There is a closed scalar component $C$ with

$$
|C\cap\eta|=2.
$$

The two witness edges cut $C$ into two scalar transition intervals and give a physically marked series pair in the witness circuit.

#### III. Quartic near-resolution core

There is an integer $k\ge1$ such that

$$
|\eta|=4k+1.
$$

For every $\lambda\in\Lambda_g$:

1. exactly one witness edge lies on the two terminal paths:
   $$
   t_\lambda=1;
   $$
2. the remaining $4k$ witness edges are partitioned into exactly $k$ closed scalar components;
3. each such component contains exactly four witness edges;
4. all $4k=n-1$ closed-component incidence rows, over all four sheets, are linearly independent;
5. the four terminal witness edges, one distinguished by each sheet, are pairwise distinct;
6. an odd number of the four distinguished edges lie on the corresponding $P^{34}_\lambda$.

#### Proof

Assume that case II does not hold.  If $n=1$, the circuit column is zero, so the edge lies on no closed scalar component.  Since

$$
t_\lambda\equiv n\equiv1\pmod2
$$

and only one witness edge exists, it lies on a terminal path in every sheet.  This is case I.

Now assume $n>1$.  Every nonempty closed-component intersection has size at least four.  By Corollary 4.2,

$$
n-1
=
\operatorname{rank}A|_\eta
\le
\sum_{\lambda\in\Lambda_g}r_\lambda
\le
\sum_{\lambda\in\Lambda_g}
\left\lfloor\frac{n-t_\lambda}{4}\right\rfloor.
\tag{7.1}
$$

We analyse $n$ modulo four.

### Case $n\equiv2\pmod4$

Every $t_\lambda$ is even.  If $n=4k+2$, each summand in (7.1) is at most $k$, so the right side is at most

$$
4k=n-2<n-1,
$$

a contradiction.

### Case $n\equiv3\pmod4$

Every $t_\lambda$ is odd and therefore at least one.  If $n=4k+3$, every summand is at most $k$, so the right side is at most

$$
4k=n-3<n-1,
$$

a contradiction.

### Case $n\equiv0\pmod4$

Every $t_\lambda$ is even.  Odd terminal parity implies that some witness edge lies on a terminal path, so not all $t_\lambda$ vanish.

If at least two $t_\lambda$ are positive, at least two summands in (7.1) drop by one, and the right side is at most $n-2$.

Thus equality could only be approached if exactly one sheet has positive terminal count and the other three have $t_\lambda=0$.  In each zero-terminal sheet, the closed-component rows partition all of $\eta$, so the sum of the rows in that sheet is the all-ones vector $1_\eta$.  The three sheet sums therefore give at least two independent relations among the rows.  Hence

$$
\operatorname{rank}A|_\eta
\le
\sum_\lambda r_\lambda-2
\le
n-3,
$$

again a contradiction.

### Case $n\equiv1\pmod4$

Write $n=4k+1$.  Each $t_\lambda$ is odd and at least one.  Therefore every summand in (7.1) is at most $k$, and the sum is at most

$$
4k=n-1.
$$

Since equality is required throughout (7.1), we obtain:

- $t_\lambda=1$ for every sheet;
- $r_\lambda=k$ for every sheet;
- every nonempty closed-component intersection has size exactly four;
- the total number of rows is $4k=n-1$ and their rank is $n-1$, so all rows are independent.

Let $e_\lambda$ be the unique witness edge on a terminal path in sheet $\lambda$.  In that sheet, the sum of all closed-component rows is

$$
1_\eta+1_{e_\lambda}.
$$

If $e_\lambda=e_\mu$ for two different sheets, the two block sums are equal, giving a nontrivial relation among the globally independent rows.  Hence the four distinguished edges are pairwise distinct.  Finally, the odd curvature pairing is exactly the parity of the number of sheets for which $e_\lambda\in P^{34}_\lambda$.  This number is odd.  ∎

## 8. The residual quartic design

Case III has a concrete combinatorial form.

### Definition 8.1 — quartic witness design

A quartic witness design on a set $\eta$ of size $4k+1$ consists of four near-resolutions

$$
\mathcal R_\lambda
$$

such that:

1. $\mathcal R_\lambda$ partitions
   $$
   \eta\setminus\{e_\lambda\}
   $$
   into $k$ four-element blocks;
2. the four omitted points $e_\lambda$ are distinct;
3. the $4k$ block incidence vectors form a basis of the even-weight space
   $$
   E_\eta
   =
   \{x\in\mathbf F_2^\eta:\sum_{e\in\eta}x_e=0\};
   $$
4. the four omitted points carry an odd $12/34$ terminal-side word.

Theorem 7.1 says that every non-singleton, non-transition support-minimal common-cut witness is a physically realised quartic witness design.

This is the only remaining unbounded object visible to common-cut parity alone.  The physical flow supplies additional data not present in the design:

- the cyclic order of each four-edge block on its scalar circuit;
- the two endpoint decompositions of $g$ at every witness edge;
- the three local complementary-pair directions;
- the intervening non-$g$ path systems;
- compatibility among the four scalar sheets coming from one $\mathbf F_2^3$ flow.

Any proof that bounds or eliminates the quartic core must use some of this physical information.  Pure common-cut parity has now been exhausted.

## 9. The bounded singleton interface

Let $\eta=\{e\}$, with $e=uv$ and $c(e)=g$.  At the two endpoints, cubic conservation gives complementary colour pairs

$$
\{a,a+g\}
\qquad\text{and}\qquad
\{b,b+g\}.
$$

There are exactly two local types.

### Theorem 9.1 — singleton atom classification

#### Aligned type

If

$$
\{a,a+g\}=\{b,b+g\},
$$

the four side colours are

$$
a,\ a+g,\ a,\ a+g.
$$

The three terminal pairings force internal labels

$$
\boxed{g,\ g,\ 0.}
$$

Thus one crossed resolution is a zero/equality-wire resolution.

#### Crossed type

If the complementary pairs are distinct, let

$$
\{r,r+g\}
$$

be the third complementary pair of nonzero colours summing to $g$.  The four side colours are distinct, and the three terminal pairings force

$$
\boxed{g,\ r,\ r+g.}
$$

This is the quotient form of DDD/Petersen resolution triality.

In both cases, the singleton curvature word is odd and therefore represents the unique nonzero class in

$$
\mathbf F_2^{\Lambda_g}/\operatorname{Aff}(AG(2,2),\mathbf F_2).
$$

Up to the stabiliser of $g$ and affine side gauge, the aligned and crossed types are the only bounded singleton interfaces.  ∎

The theorem localises the singleton branch to two vertices and four incident semiedges.  It does not yet prove that the zero or DDD resolution transfers a five-support cover back to the original incidence graph.

## 10. Exact finite realisations

The following certificates show that the first two branches are physically nonempty.  Terminals are attached at vertices $0,1,2,3$ unless another order is stated; all terminal colours are $g=1$.  Edge colours are written as nonzero binary integers in $\mathbf F_2^3$.

### 10.1 Crossed singleton

Use terminal order

$$
(0,2,1,3)
$$

and internal edges

$$
\begin{array}{c|c@\qquad c|c}
06&3&09&2\\
15&2&13&3\\
29&6&27&7\\
34&2&48&5\\
46&7&57&6\\
56&4&78&1\\
89&4&&
\end{array}
$$

The unique $g$-edge is $78$.  Its scalar statuses, for $\lambda=1,3,5,7$, are

$$
P^{12},\ P^{34},\ P^{12},\ P^{12}.
$$

The endpoint complementary pairs are

$$
\{6,7\},\qquad\{4,5\},
$$

so this is crossed type.  The flow has rank three, all scalar routes are $12\mid34$, the curvature word is $0100$, and deleting $78$ leaves the graph connected.

### 10.2 Aligned singleton

Take

$$
\begin{array}{c|c@\qquad c|c}
07&3&04&2\\
15&3&18&2\\
29&7&23&6\\
36&7&48&1\\
46&3&57&7\\
59&4&67&4\\
89&3&&
\end{array}
$$

The unique $g$-edge is $48$.  Its scalar statuses are

$$
P^{34},\ P^{12},\ P^{12},\ P^{12}.
$$

Both endpoint complementary pairs are

$$
\{2,3\}.
$$

This is aligned type.  The flow has rank three, all scalar routes are $12\mid34$, the curvature word is odd, and deleting $48$ leaves the graph connected.

### 10.3 Two-edge transition witness

Take

$$
\begin{array}{c|c@\qquad c|c}
01&7&08&6\\
15&6&24&2\\
23&3&37&2\\
45&4&46&6\\
59&2&68&7\\
67&1&79&3\\
89&1&&
\end{array}
$$

The two $g$-edges are

$$
67,\qquad89.
$$

Their scalar statuses for $\lambda=1,3,5,7$ are

$$
\begin{array}{c|cccc}
67&C&P^{34}&P^{12}&P^{34}\\
89&C&P^{12}&P^{12}&P^{34}.
\end{array}
$$

In the first sheet, the unique closed scalar circuit containing them is

$$
6-7-9-8-6.
$$

Thus the closed-component incidence matrix on these two edges is the single row

$$
(1,1),
$$

and the curvature vector restricts to

$$
(0,1).
$$

Hence

$$
\eta=\{67,89\}
$$

is an odd circuit of size two.  The flow has rank three and all four scalar routes are $12\mid34$.

These certificates are exact finite evidence.  They do not supply the missing composition theorem.

## 11. Updated localisation frontier

The nonflat branch is now reduced to the following proof programme.

### Singleton branch

Turn one of the two bounded enriched atoms into strict graph progress:

- aligned type $\Rightarrow$ composition-safe zero/equality-wire resolution;
- crossed type $\Rightarrow$ composition-safe DDD/Petersen resolution or the physical $D_8$ class.

### Transition-pair branch

If a closed scalar circuit meets $\eta$ in two edges, use the two intervening scalar intervals and their finite endpoint matching data to obtain:

- a smaller cyclic separator;
- a ten-state four-pole transfer state;
- a transition-matroid two-sum;
- or a bounded replaceable interval.

### Quartic-core branch

If neither reduction occurs, use the physical compatibility of the four near-resolutions to:

- rule out the quartic design;
- force the $k=1$ five-edge core;
- identify the DDD $D_8$ class;
- or produce a genuine larger physical counterexample and the exact weaker theorem it forces.

The immediate mathematical bottleneck is no longer “localise an arbitrary common cut”.  It is:

$$
\boxed{
\text{compose a singleton/series interface}
\quad\text{or eliminate the quartic near-resolution core.}
}
$$

## 12. Reliability boundary

Proved in this chapter:

- the closed-component incidence formulation;
- the odd-circuit theorem;
- the scalar-common-cut/physical-cut separation;
- the singleton/transition/quartic-core trichotomy;
- the complete quartic near-resolution constraints;
- the aligned/crossed singleton classification.

Exact finite certificates:

- crossed singleton;
- aligned singleton;
- two-edge transition circuit.

Still open:

- composition-safe use of the aligned zero resolution;
- composition-safe use of the crossed DDD resolutions;
- physical transfer across a two-edge scalar interval;
- existence or elimination of quartic cores with $k\ge1$;
- canonical identification with the physical $D_8$ cohomology class;
- defect-forest pruning and the global five-support theorem.

No Lean, independent-review, peer-review, publication, release, arXiv, or DOI status is implied.