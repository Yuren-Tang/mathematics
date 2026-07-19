# Periodic elementary intervals as rigid Kempe ladders

## 1. Scope

A backtrack-free **elementary** scalar interval—between consecutive `g`-incidences of the full scalar circuit—is a chain of three-turn periodic cells.  This chapter computes the restrictions of the three quotient Kempe systems to such a chain.

A witness-to-witness arc may contain additional `g`-edges from `E_g\setminus\eta`; it is therefore a transition walk in `\Gamma_g` whose elementary non-`g` pieces may carry the ladders described here.  No assertion is made that a quartic witness block consists of four ladders.

For one elementary periodic chain:

1. one Kempe system joins two side ports inside each cell;
2. one joins a side port of cell `t` to one of cell `t+1`;
3. the third gives the other shifted rail.

All internal Kempe routing is rigid.  Remaining freedom lies in the surrounding non-`g` component and its transition matching.

## 2. One periodic cell

Fix one scalar sheet and an oriented cell with continuation word

$$
a,b,c,a.
$$

Let its path edges be

$$
a_L,b,c,a_R
$$

and its side ports

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
\qquad q_b=\bar b,
\qquad q_c=\bar c.
$$

For each `x\in\{a,b,c\}`, let `\delta_x` be the unique nonzero functional with

$$
\delta_x(q_x)=0.
$$

## 3. Local Kempe wiring

### Theorem 3.1

The three Kempe systems restrict to the cell as follows:

$$
\begin{array}{c|c}
\text{system}&\text{routes}\\
\hline
K_{\delta_a}&d_1\longleftrightarrow d_3\\
K_{\delta_b}&(a_L\longleftrightarrow d_1)\ \sqcup\ (d_2\longleftrightarrow a_R)\\
K_{\delta_c}&(a_L\longleftrightarrow d_2)\ \sqcup\ (d_3\longleftrightarrow a_R).
\end{array}
$$

The omitted side port is respectively `d_2,d_3,d_1`.

#### Proof

A system `K_\delta` contains exactly the non-`g` edges whose quotient colour evaluates to one.  For example, `\delta_a` selects continuation colours `b,c` and side colours `d_1,d_3`, producing the first path.  The other two rows follow identically. ∎

Thus the simultaneous three-Kempe state of one oriented cell has no additional local parameter.

## 4. Chains of cells

Consider `N\ge1` consecutive cells.  Write the side ports of cell `t` as

$$
d_{1,t},d_{2,t},d_{3,t}
$$

and its path boundary edges as

$$
a_{t-1},a_t.
$$

### Theorem 4.1 — three-rail ladder

The internal routes are:

$$
\boxed{
K_{\delta_a}:d_{1,t}\longleftrightarrow d_{3,t}
}
$$

for every cell;

$$
\boxed{
K_{\delta_b}:d_{2,t}\longleftrightarrow d_{1,t+1}
}
$$

for `1\le t<N`, with end routes

$$
a_0\longleftrightarrow d_{1,1},
\qquad
d_{2,N}\longleftrightarrow a_N;
$$

and

$$
\boxed{
K_{\delta_c}:d_{3,t}\longleftrightarrow d_{2,t+1}
}
$$

for `1\le t<N`, with end routes

$$
a_0\longleftrightarrow d_{2,1},
\qquad
d_{3,N}\longleftrightarrow a_N.
$$

#### Proof

Glue the one-cell routing tables along the common `a_t` path edge. ∎

## 5. Port incidence and rigidity

Each side port belongs to exactly two Kempe systems:

$$
\begin{array}{c|c}
d_1&K_{\delta_a},K_{\delta_b}\\
d_2&K_{\delta_b},K_{\delta_c}\\
d_3&K_{\delta_a},K_{\delta_c}.
\end{array}
$$

### Corollary 5.1 — no internal Kempe entropy

Once the period orientation, cell count, and endpoint colour are fixed, all three Kempe restrictions inside the elementary chain are forced.

The chain length creates no new local routing choice.

## 6. Two-cell neutral block

Two consecutive cells have identity quotient monodromy and each side colour appears twice.

### Proposition 6.1

A two-cell block is algebraically neutral on its path ports and has a fixed simultaneous three-Kempe wiring on its six side ports.

This makes it a candidate bounded transfer block.  Equality of the surrounding component transition state is still required for an actual replacement.

## 7. Passage to the transition quotient

All side edges and all elementary intervals of one witness arc lie in components of

$$
Q-E_g.
$$

Contracting those components produces `\Gamma_g`.  At one quotient vertex, the full internal elementary ladders are remembered only through the four scalar transition matchings

$$
T_\phi(R).
$$

### Corollary 7.1 — correct role of Kempe ladders

Periodic ladders are local realizations of transition pairs inside one quotient vertex.  A witness-to-witness arc is a walk alternating between:

1. quotient `g`-edges, including possible edges of `E_g\setminus\eta`;
2. transition pairs realized by elementary cap-or-ladder paths inside quotient vertices.

Thus the ladder theorem supplies finite local realizability data for the transition quotient; it does not bound the number of quotient edges in a witness arc.

## 8. Updated decomposition target

A physical composition theorem should now work on `\Gamma_g`.

For the transition walk supporting a marked quartic shell, prove one of:

1. a proper terminal-even quotient region closes under the relevant transition pairs, yielding a two-cut or four-cut;
2. repeated quotient transition states give a transition-matroid two-sum;
3. a local elementary segment exposes the bounded backtrack cap;
4. crossing Kempe realizations create an alternate transition and break route-lock;
5. the transition-indecomposable remainder carries the physical `D_8` class.

Every internal quotient cut then lifts exactly to the original four-pole.

## 9. Reliability boundary

Proved here:

- exact three-Kempe wiring of one periodic elementary cell;
- rigid three-rail wiring for a chain of elementary cells;
- fixed port-incidence pattern;
- absence of internal Kempe routing entropy;
- fixed two-cell neutral wiring.

Explicitly not claimed:

- that a witness block contains only four `g`-edges;
- that a witness-to-witness arc is one elementary ladder;
- bounded length of a transition walk in `\Gamma_g`;
- replacement without matching component transition semantics;
- the global five-support theorem.

No Lean, independent-review, peer-review, publication, release, arXiv, or DOI status is implied.
