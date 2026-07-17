# Atom route-lock and quadratic curvature

**Programme:** `AffineCDC — Research Lead`  
**Status:** theorem-level reduction of one-edge co-root atoms to a universal route-lock sector; exact finite quotient and lock-fibre computation; strict graph replacement remains open  
**Parents:** `FIVE_CDC_DDD_ATOM_RESOLUTION_TRIALITY_V1.md`, `FIVE_CDC_DEFECT_MINIMAL_FOREST_PETERSEN_TRANSPORT_V1.md`

## 1. Purpose

A nondegenerate one-edge co-root atom has four terminal roots and three possible terminal pairings.  The original pairing forces a co-root internal label, while the two crossed pairings force the two root labels at the endpoints of the corresponding Petersen edge.

The remaining composition question is whether the opposite shore supplies a genuine Kempe path whose route realises one of the crossed pairings.  This packet proves that failure has a unique finite form:

\[
\boxed{
\text{the atom survives every full challenge}
\iff
\text{every full challenge uses the original atom pairing.}
}
\]

This is called **universal route-lock**.

The locked sector then admits a canonical quotient to a nowhere-zero `F_2^3` flow with four scalar sheets, all routing the terminals in the same pairing.  Its next obstruction is not an ordinary edge cut but a quadratic transition-curvature class.

No five-cycle double cover theorem or strict replacement theorem is claimed.

## 2. Ordered boundary data

Let

\[
\ell=(\ell_1,\ell_2,\ell_3,\ell_4)\in R_5^4,
\qquad
\ell_1+\ell_2+\ell_3+\ell_4=0.
\]

Fix the atom pairing

\[
P_0=12\mid34
\]

and define its internal defect

\[
d=\ell_1+\ell_2=\ell_3+\ell_4.
\]

The state is **bad** when `d` is not a root, hence when

\[
d=0
\quad\text{or}\quad
\operatorname{wt}(d)=4.
\]

A root `a in R_5` is a **full challenge** when

\[
\ell_j+a\in R_5
\qquad(j=1,2,3,4).
\]

Equivalently, the support of `a` meets the support of every terminal root in exactly one point.

## 3. Universal bad-route theorem

For a full challenge `a`, switch one terminal path component.  There are three possible route pairings:

\[
12\mid34,
\qquad
13\mid24,
\qquad
14\mid23.
\]

### Theorem 3.1 — unique bad route

For every bad ordered state and every full challenge:

\[
\boxed{
\begin{array}{c|c}
\text{route}&\text{new internal sum}\
\hline
12\mid34&d,\\
13\mid24&d+a,\\
14\mid23&d+a.
\end{array}}
\]

Moreover `d+a` is always a root.  Hence the original atom pairing is the unique route that remains bad.

#### Proof

Switching a path whose endpoints lie in the same side of `12|34` adds `a` twice to the corresponding side sum, hence leaves `d` unchanged.  A crossed route changes exactly one of `ell_1,ell_2`, hence changes the side sum to `d+a`.

If `d=0`, then `d+a=a` is a root.  Suppose `d` is a co-root.  Since `a` is full, it meets both `ell_1` and `ell_2` oddly, so

\[
\langle d,a\rangle
=
\langle\ell_1,a\rangle+
\langle\ell_2,a\rangle
=0.
\]

A two-subset cannot be disjoint from the four-point support of a co-root, so the intersection has size two.  Thus `a` lies inside the co-root support and `d+a` has weight two. ∎

### Corollary 3.2 — composition dichotomy

For a physical atom:

\[
\boxed{
\begin{array}{l}
\text{some full challenge takes a crossed route}
\Rightarrow
\text{the atom becomes root-valued};\\[1mm]
\text{the atom survives all full challenges}
\Rightarrow
\text{every full challenge is locked to }12\mid34.
\end{array}}
}
\]

The first line is a local algebraic resolution.  Transferring the resulting cover through the changed terminal incidence still requires the four-pole composition theorem.

## 4. Exact ordered-state census

There are exactly

\[
640
\]

ordered root quadruples with total sum zero.  Of these:

\[
280
\]

are bad, and

\[
180
\]

have a co-root defect.

Exact enumeration verifies Theorem 3.1 on all bad-state/full-challenge pairs: the bad-route word is always

\[
(1,0,0)
\]

in the route order `12|34,13|24,14|23`.

### Fixed-fibre lock graph

Fix:

1. a co-root defect `q`;
2. the ordered right pair `(ell_3,ell_4)`.

The left ordered pair `(ell_1,ell_2)` has six possible values.  Join two such states when a full challenge is switched along the left path `12` and remains inside the fixed fibre.

### Computational Theorem 4.1

Every fixed fibre is the graph

\[
\boxed{K_{2,4}.}
\]

There are

\[
5\cdot6=30
\]

such fibres.  If both left and right path switches are allowed, the six-state fibres glue into five larger thirty-six-state components, one for each co-root defect.

The two degree-four vertices in a fibre are the repeated-matching `C` states; the four degree-two vertices are the distinct-matching `D` states.

## 5. From a locked C-state to `F_2^3`

At either repeated-matching `C` vertex in a lock fibre, there are exactly four full challenges

\[
\mathcal A=\{a_1,a_2,a_3,a_4\}.
\]

Define

\[
\chi:E_5\longrightarrow F_2^4,
\qquad
\chi(x)=
(\langle x,a_1\rangle,\ldots,\langle x,a_4\rangle).
\]

Let `q` be the co-root defect of the fibre.

### Computational Theorem 5.1 — challenge quotient

\[
\boxed{
\ker\chi=\langle q\rangle=\{0,q\},
}
\]

and

\[
\boxed{
\chi(R_5)=
E_4\setminus\{0\},
\qquad
E_4=\{u\in F_2^4:\sum_j u_j=0\}.
}
\]

Every terminal root of the `C` state maps to

\[
g=(1,1,1,1).
\]

Consequently, the opposite root-valued four-pole projects to a nowhere-zero `E_4` flow

\[
c:E(Q)\to E_4\setminus\{0\}
\cong F_2^3\setminus\{0\},
\]

with all four terminal values equal to `g`.

The four coordinate projections of `c` are exactly the four full-challenge relative even subgraphs.  Universal route-lock says that all four pair the terminals as

\[
12\mid34.
\]

Thus the atom composition problem has become:

\[
\boxed{
\text{a nowhere-zero }F_2^3\text{-flow with four scalar sheets, all同路.}
}
\]

## 6. Rank-drop is not an ordinary small cut

One might expect four scalar sheets with the same route to force a separating two-edge cut.  This is false.

### Exact witness

Take eight internal vertices `0,...,7`, terminals attached at

\[
4\mapsto1,
\quad5\mapsto2,
\quad6\mapsto3,
\quad7\mapsto4,
\]

and internal edges with `F_2^3` labels written as binary integers:

\[
\begin{array}{c|c@\qquad c|c}
02&7&04&4\\
06&3&13&7\\
15&3&16&4\\
25&4&27&3\\
34&3&37&4.
\end{array}
\]

All four nonzero linear functionals `lambda` satisfying `lambda(g)=1` have route `12|34`.  The colour span has rank two, but the minimum edge cut separating terminals `{1,2}` from `{3,4}` has size four.

Hence:

\[
\boxed{
\text{route-lock}
\not\Rightarrow
\text{graph two-separation}.
}
\]

The rank-drop sector must be treated as a genuine low-rank flow/transition system, not replaced by an unsupported cut claim.

## 7. Scalar sheets and quadratic curvature

Identify

\[
E_4
\]

with the eight affine Boolean functions on the four points of `AG(2,2)`.  The vector `g=1111` is the constant-one function.

For each of the four coordinate flows, label the terminal path joining `1,2` by side `0` and the terminal path joining `3,4` by side `1`.  Every closed scalar cycle has an arbitrary side bit.

At an internal cubic vertex:

- if no incident edge has colour `g`, exactly three scalar sheets are active; their three side bits extend uniquely to an affine word in `E_4`;
- if a `g`-edge is incident, all four sheets are active; they extend to an affine word if and only if their parity is zero.

Since every sheet is constant along an active edge, the parity at the two ends of a `g`-edge agrees.  Thus each `g`-edge carries a curvature bit.

Let

\[
E_g=\{e:c(e)=g\}.
\]

For every closed component `C` of one scalar sheet, changing its arbitrary side bit toggles the curvature on

\[
C\cap E_g.
\]

Define the **quadratic transition class**

\[
\boxed{
\Omega(c)
\in
F_2^{E_g}
\Big/
\left\langle
1_{C\cap E_g}:
C\text{ a closed scalar component}
\right\rangle.
}
\]

### Theorem 7.1 — flatness criterion

The following are equivalent:

1. `Omega(c)=0`;
2. the closed-cycle side bits can be chosen so that every `g`-edge has zero curvature;
3. there exists a potential
   \[
   p:V(Q)\to E_4\cong F_2^3
   \]
   taking terminal values
   \[
   0,0,g,g
   \]
   and satisfying, for every internal edge `uv`,
   \[
   \boxed{
   p(u)+p(v)\in\{0,c(uv)+g\}.
   }
   \]

#### Proof

The equivalence of the first two statements is the definition of the quotient class.  If all curvature bits vanish, the three or four active side values at every vertex extend to a unique affine word `p(v)`.

On an edge of colour `c`, the endpoint affine words agree on the support of `c`.  The only even words vanishing on that support are

\[
0
\quad\text{and}\quad
c+g,
\]

which gives the edge law.  Conversely, the edge law makes every coordinate of `p` constant along its active scalar components and recovers side labels with zero curvature. ∎

## 8. Updated composition trichotomy

A nondegenerate co-root atom now has the following exact reduction:

\[
\boxed{
\begin{array}{c}
\text{physical full challenges}\
\downarrow\\
\begin{cases}
\text{a crossed route occurs}
&\Rightarrow\text{root resolution candidate};\\
\text{all routes are locked}
&\Rightarrow c:Q\to F_2^3\setminus\{0\}.
\end{cases}\\
\downarrow\\
\begin{cases}
\operatorname{rank}\langle c(E)\rangle\le2
&\Rightarrow\text{rank-drop transition sector};\\
\operatorname{rank}=3,\ \Omega(c)=0
&\Rightarrow\text{flat affine-potential sector};\\
\operatorname{rank}=3,\ \Omega(c)\ne0
&\Rightarrow\text{quadratic/DDD curvature sector}.
\end{cases}
\end{array}}
\]

This is a mechanism reduction, not yet a strict graph reduction.

## 9. Trust boundary

Exact/theorem-level:

- the unique bad-route theorem;
- the counts `640`, `280`, and `180`;
- thirty fixed `K_{2,4}` lock fibres;
- the quotient `E_5/<q> ~= E_4 ~= F_2^3`;
- all four scalar sheets have the locked pairing;
- the affine-word edge law;
- the explicit rank-two route-lock witness with minimum pair-separating cut four.

Open:

- converting a crossed root resolution into a cover of the original incidence graph;
- reducing the rank-drop sector;
- converting a flat potential into a Whitney/dot-product replacement or smaller separator;
- interpreting nonzero `Omega` as the unique physical `D_8` class or a transition-matroid obstruction;
- extending the atom theorem along a whole Petersen-transducer path and then through zero branches.

## 10. Next theorem target

Prove a composition theorem of the form

\[
\boxed{
\begin{array}{c}
\text{universal route-lock}\
\Downarrow\\
\text{rank-drop reducible}
\quad\text{or}\quad
\text{flat potential gives a safe resolution}
\quad\text{or}\quad
\Omega\ne0\text{ localises to a }D_8\text{ atom/factor}.
\end{array}}
\]

The mainline should now study the flat-potential and curvature sectors separately; further raw boundary-state enumeration is no longer the bottleneck.
