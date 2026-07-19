# Periodic scalar intervals as rigid Kempe ladders

## 1. Purpose

A backtrack-free scalar interval is a chain of three-turn periodic cells.  Each cell has two path ports and three side ports.  The scalar-interval normal form determines the colour pattern, but the remaining obstruction lies in the way the other three sheet differences traverse those ports.

This chapter computes that traversal exactly.

For a chain of periodic cells, the three quotient Kempe systems form a rigid three-rail ladder:

1. one system joins two side ports inside each cell;
2. one system joins a side port of cell `t` to a side port of cell `t+1`;
3. the third system gives the other shifted inter-cell rail.

No additional internal routing choice appears as the chain length grows.  All remaining freedom lies outside the ladder, in the way its side ports are joined through the rest of the graph.

## 2. One periodic cell

Fix a scalar sheet `H_\phi` and one oriented periodic cell with continuation-colour word

$$
a,b,c,a.
$$

Let the three internal vertices be

$$
v_1,v_2,v_3,
$$

and let the path edges be

$$
a_L,\ b,\ c,\ a_R
$$

in order.  The side ports at the three vertices have colours

$$
d_1=a+b,
\qquad
d_2=b+c,
\qquad
d_3=c+a.
$$

Put

$$
q_a=\bar a,
\qquad
q_b=\bar b,
\qquad
q_c=\bar c.
$$

These are the three nonzero elements of `U`, with

$$
q_a+q_b+q_c=0.
$$

For each `x\in\{a,b,c\}`, let

$$
\delta_x\in U^*\setminus\{0\}
$$

be the unique nonzero functional satisfying

$$
\delta_x(q_x)=0.
$$

It is one on the other two nonzero quotient colours.

The three quotient Kempe systems are

$$
K_{\delta_a},
\qquad
K_{\delta_b},
\qquad
K_{\delta_c}.
$$

## 3. Local Kempe wiring table

### Theorem 3.1 — periodic-cell Kempe wiring

The restrictions of the three Kempe systems to one cell are:

$$
\begin{array}{c|c|c}
\text{Kempe system}&\text{selected boundary ports}&\text{internal routing}\\
\hline
K_{\delta_a}&d_1,d_3&d_1\longleftrightarrow d_3\\
K_{\delta_b}&a_L,d_1,d_2,a_R
&(a_L\longleftrightarrow d_1)\ \sqcup\ (d_2\longleftrightarrow a_R)\\
K_{\delta_c}&a_L,d_2,d_3,a_R
&(a_L\longleftrightarrow d_2)\ \sqcup\ (d_3\longleftrightarrow a_R).
\end{array}
$$

The omitted side port is respectively

$$
d_2,
\qquad
d_3,
\qquad
d_1.
$$

#### Proof

A Kempe system `K_\delta` contains exactly the non-`g` edges whose quotient colour evaluates to one under `\delta`.

For `\delta_a`, the path colours `b,c` are selected and `a` is omitted.  The side quotient colours are

$$
\bar d_1=q_c,
\qquad
\bar d_2=q_a,
\qquad
\bar d_3=q_b.
$$

Hence `d_1,d_3` are selected and `d_2` is omitted.  The selected edges form the path

$$
d_1-v_1-b-v_2-c-v_3-d_3.
$$

For `\delta_b`, the selected path colours are `a,c`, while `b` is omitted.  The selected side ports are `d_1,d_2`.  The two routes are local at `v_1` and through `c` from `v_2` to `v_3`, giving the displayed pairing.

For `\delta_c`, the selected path colours are `a,b`, while `c` is omitted.  The selected side ports are `d_2,d_3`.  The two routes are through `b` from `v_1` to `v_2` and local at `v_3`.  ∎

### Corollary 3.2 — finite simultaneous cell state

The complete interaction of all three quotient Kempe systems with one periodic cell is fixed by the oriented colour order `(a,b,c)`.  There is no further local routing parameter.

Reversing the cell exchanges left and right and reverses the cyclic order, producing the only other oriented local type.

## 4. Chains of cells

Consider a chain of `N\ge1` cells with continuation word

$$
a,b,c,a,b,c,a,\ldots,b,c,a.
$$

For cell `t`, write its side ports as

$$
d_{1,t},d_{2,t},d_{3,t},
$$

and its path boundary ports as

$$
a_{t-1},a_t.
$$

When consecutive cells are joined, the right `a_t` semiedge of cell `t` is joined to the left `a_t` semiedge of cell `t+1`.

### Theorem 4.1 — three-rail Kempe ladder

The three Kempe systems route through the chain as follows.

#### First rail: cellwise rungs

For every `t`,

$$
\boxed{
K_{\delta_a}:
 d_{1,t}\longleftrightarrow d_{3,t}.
}
$$

The path boundary edges `a_0,\ldots,a_N` are absent from this Kempe system, so the rungs are mutually disjoint inside the chain.

#### Second rail: forward shift

For `1\le t<N`,

$$
\boxed{
K_{\delta_b}:
 d_{2,t}\longleftrightarrow d_{1,t+1}.
}
$$

At the ends,

$$
a_0\longleftrightarrow d_{1,1},
\qquad
 d_{2,N}\longleftrightarrow a_N.
$$

#### Third rail: the other forward shift

For `1\le t<N`,

$$
\boxed{
K_{\delta_c}:
 d_{3,t}\longleftrightarrow d_{2,t+1}.
}
$$

At the ends,

$$
a_0\longleftrightarrow d_{2,1},
\qquad
 d_{3,N}\longleftrightarrow a_N.
$$

#### Proof

Apply the one-cell wiring table and glue the common path port `a_t` between consecutive cells.

For `K_{\delta_b}`, the right route of cell `t` ends at `a_t` from `d_{2,t}`, and the left route of cell `t+1` starts at the same edge and exits at `d_{1,t+1}`.  Their concatenation gives the forward shift.  The end routes remain attached to `a_0,a_N`.

The `K_{\delta_c}` statement is identical with `d_3` and `d_2` in the corresponding positions.  The `K_{\delta_a}` system never uses an `a` path edge and therefore remains cellwise.  ∎

## 5. Port incidence

Each side port belongs to exactly two of the three Kempe systems:

$$
\begin{array}{c|c}
\text{port type}&\text{Kempe systems containing it}\\
\hline
d_1&K_{\delta_a},K_{\delta_b}\\
d_2&K_{\delta_b},K_{\delta_c}\\
d_3&K_{\delta_a},K_{\delta_c}.
\end{array}
$$

Thus one periodic chain carries a triangular incidence pattern repeated along its length.  The three rail types are permuted by `GL(U)\cong S_3`.

## 6. Exact internal rigidity

### Corollary 6.1 — no internal Kempe entropy

As the number of cells grows, the chain acquires no new internal Kempe routing choice.  Once the following are fixed:

- orientation of the three-colour period;
- number of cells `N`;
- the two path endpoint colours;

all three Kempe restrictions inside the chain are forced.

The remaining data are entirely external:

- which outside `K_{\delta_a}` paths close the cellwise rungs;
- how the outside graph joins the shifted `K_{\delta_b}` rail ports;
- how it joins the shifted `K_{\delta_c}` rail ports;
- how these closures interact with the other scalar components and the four-pole boundary.

## 7. Two-cell periodic block

For two consecutive cells, the path monodromy is the identity and each side colour occurs twice.  The Kempe ladder consists of:

- two `K_{\delta_a}` rungs;
- one internal `K_{\delta_b}` shift and two end branches;
- one internal `K_{\delta_c}` shift and two end branches.

### Proposition 7.1 — bounded neutral ladder block

A two-cell block is algebraically neutral on the path ports and has a completely fixed simultaneous three-Kempe wiring on its six side ports.

Therefore any two two-cell blocks with the same enriched external closure state are composition candidates for pumping or replacement.

The existence of two blocks with the same quotient wiring is automatic; equality of the external closure state is not.

## 8. Relation to nucleus shells

In a concentrated nucleus peel, each distinguished scalar circuit has four intervals.  If no interval contains a backtrack cap, each interval is a periodic Kempe ladder with bounded ends.

Hence the entire new nucleus layer consists of:

1. the bounded two-vertex pairwise transition shell;
2. at most sixteen bounded interval ends;
3. periodic three-rail Kempe ladders between the shell ports;
4. external closure data on the ladder side ports.

All flow, route, and internal Kempe information is finite or periodic.  The sole unbounded object is the external closure pattern of the ladder ports.

## 9. Updated decomposition target

A physical composition theorem may now be stated purely in terms of Kempe-ladder closures.

For a periodic chain, prove one of:

1. an outside Kempe component closes on a proper subchain, exposing a smaller cyclic separator or a transition two-sum;
2. two two-cell blocks have the same enriched closure state and the intervening chain is replaceable;
3. the external closures cross in a way that creates an alternate scalar route and breaks route-lock;
4. the closure pattern is forced into one irreducible periodic orbit carrying the physical `D_8` class.

This is narrower than classifying arbitrary scalar intervals: the internal ladder is already rigid.

## 10. Reliability boundary

Proved here:

- the exact restrictions of all three quotient Kempe systems to one periodic cell;
- the three-rail ladder wiring for a chain of any length;
- the fixed incidence of side-port types with the three Kempe systems;
- absence of any new internal Kempe routing choice as the chain grows;
- complete simultaneous quotient wiring of a two-cell neutral block.

Not proved here:

- finite classification of external Kempe closures;
- a proper-subchain separator theorem;
- pumping with side attachments;
- alternate-route escape from crossing closures;
- identification of the irreducible closure orbit with the physical `D_8` class;
- the global five-support theorem.

No Lean, independent-review, peer-review, publication, release, arXiv, or DOI status is implied.
