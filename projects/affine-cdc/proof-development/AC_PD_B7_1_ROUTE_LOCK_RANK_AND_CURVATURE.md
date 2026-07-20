# AC-PD-B7.1 — route-lock rank escape and curvature duality

**Proof-development state:** `COMPLETE-DRAFT / LOCALISATION-OPEN`  
**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Exact initial corpus base:** `main@960c92b7ff231c78b387894149779083060a75eb`  
**Validated sources:** `FIVE_CDC_ROUTE_LOCK_RANK_TWO_TAIT_ESCAPE_V1.md`, `FIVE_CDC_ATOM_ROUTE_LOCK_CURVATURE_V1.md`, and `FIVE_CDC_FULL_RANK_CURVATURE_DUAL_CERTIFICATE_V1.md`  
**Depends on:** B6.4 locked quotient  
**Immediate consumers:** B7.2 localisation frontier; B9 global composition  
**External mathematical inputs:** none

## 0. Locked quotient

Universal route-lock at a repeated-matching atom state produces, conditional on the exact finite challenge quotient, a nowhere-zero flow

$$
c:E(Q)\to E_4\setminus\{0\}
\cong\mathbf F_2^3\setminus\{0\},
$$

with all four terminal values

$$
g=1111
$$

and four scalar coordinate even subgraphs, each pairing the terminals as $12\mid34$.

## 1. Rank one is impossible

### Lemma 1.1

A nowhere-zero flow on an internal cubic graph cannot have one-dimensional colour span.

### Proof

A rank-one flow uses one nonzero colour $a$. At an internal cubic vertex the incident sum is

$$
a+a+a=a\ne0,
$$

contradicting conservation. $\square$

Thus every rank-drop locked quotient has rank exactly two.

## 2. Rank two is a Tait colouring

Let

$$
L=\langle c(E(Q))\rangle
$$

be two-dimensional. Since the terminal colour is $g$, one has

$$
L\setminus\{0\}=\{a,b,g\},
\qquad a+b=g.
$$

### Theorem 2.1

Every internal cubic vertex sees the three distinct colours $a,b,g$. Hence $c$ is a proper Tait three-edge-colouring of the quotient four-pole.

### Proof

The three incident colours are nonzero and sum to zero. Equality of two would force the third to be zero, so they are the three nonzero elements of $L$. $\square$

## 3. Root-triangle section

For the finite challenge quotient

$$
\chi:E_5\twoheadrightarrow E_4,
$$

every two-dimensional plane $L\le E_4$ containing $g$ admits a section

$$
s_L:L\setminus\{0\}\to R_5
$$

such that

$$
\chi s_L(x)=x
$$

and the three section roots sum to zero.

This is an exact finite root-fibre classification; canonical representatives have been enumerated for all three planes through $g$.

### Theorem 3.1 — rank-two escape

The edge assignment

$$
\widetilde r(e)=s_L(c(e))
$$

is a root-valued $E_5$ flow. All terminal roots equal $s_L(g)$, so the induced five-support boundary state is

$$
A.
$$

Therefore a rank-two universally locked atom strictly escapes every Type H triangle profile.

The only surviving locked sector has full rank three.

## 4. Scalar sheets in the full-rank sector

Let

$$
H_j
$$

be the four scalar relative even subgraphs. Each consists of:

- one terminal path joining $1,2$;
- one terminal path joining $3,4$;
- closed cycle components.

Let

$$
E_g=\{e:c(e)=g\}.
$$

Every $g$-edge belongs to all four sheets.

Choose side bit zero on each $12$ path and one on each $34$ path. Closed scalar cycles have arbitrary side bits. At a $g$-edge, the parity failure of the four local side bits is a curvature bit. This gives

$$
\omega\in\mathbf F_2^{E_g}.
$$

Changing the side of a closed scalar component $C$ adds

$$
\mathbf1_{C\cap E_g}.
$$

Put

$$
W=
\left\langle
\mathbf1_{C\cap E_g}:
C\text{ a closed component of one scalar sheet}
\right\rangle
$$

and define

$$
\Omega(c)=[\omega]\in\mathbf F_2^{E_g}/W.
$$

## 5. Flat potential theorem

### Theorem 5.1

The following are equivalent.

1. $\Omega(c)=0$.
2. Closed-cycle side bits can be chosen so that every $g$-edge has zero curvature.
3. There is a potential
   $$
   p:V(Q)\to E_4
   $$
   with terminal values $0,0,g,g$ and
   $$
   \boxed{
   p(u)+p(v)\in\{0,c(uv)+g\}
   }
   $$
   on every internal edge.

### Proof

The first two statements are the quotient definition. With zero curvature, the three or four active sheet-side values at every cubic vertex satisfy the unique affine parity relation and extend to one word $p(v)\in E_4$.

Across an edge of colour $c(e)$, the endpoint words agree on the support of $c(e)$. The even words vanishing on that support are precisely $0$ and $c(e)+g$. Conversely the edge law recovers scalar side labels with zero curvature. $\square$

This potential partitions the four-pole into at most eight fibres. It is structure, not yet a finite transfer theorem: same-fibre subgraphs may have unbounded internal semantics.

## 6. Nonflat dual witness

### Theorem 6.1 — curvature duality

The class $\Omega(c)$ is nonzero if and only if there is

$$
\eta\subseteq E_g
$$

such that

$$
\langle\eta,\omega\rangle=1
$$

and

$$
|\eta\cap C|\equiv0\pmod2
$$

for every closed scalar component $C$.

### Proof

A nonzero quotient vector is separated by a linear functional annihilating the subspace $W$. Identify the functional with its support in $E_g$. $\square$

## 7. Common scalar-sheet cut

### Theorem 7.1

For each scalar sheet $H_j$, the same physical edge set $\eta$ lies in its cut space:

$$
\boxed{
\eta=\delta_{H_j}h_j
}
$$

for some binary potential $h_j$.

### Proof

The cycle space of $H_j$ is generated by its closed cycle components. The dual witness has even intersection with each such component, hence is orthogonal to the sheet cycle space and lies in its cut space. $\square$

Thus nonflat curvature produces one edge set, consisting entirely of common-colour $g$ edges, that is simultaneously a cut in all four scalar circuit partitions.

## 8. Odd terminal word

Choose $h_j$ with $\delta h_j=\eta$. Define

$$
b_j(\eta)=h_j(t_3)+h_j(t_4).
$$

### Theorem 8.1

$$
\boxed{
\langle\eta,\omega\rangle
=
\sum_{j=1}^4b_j(\eta).
}
$$

Hence the terminal word

$$
b(\eta)=(b_1,\ldots,b_4)
$$

has odd parity and represents the nonzero class in

$$
\mathbf F_2^4/E_4\cong\mathbf F_2.
$$

### Proof

Closed sheet components contribute evenly to the pairing. The $12$ path has side zero. On the $34$ path, the parity of $\eta$ is its endpoint potential difference. Sum over the four sheets. $\square$

This one-dimensional coefficient class resembles the unique DDD $D_8$ cohomology bit, but no graph-level comparison map identifying them has been proved.

## 9. Exact full-rank dichotomy

The surviving universally locked atom sector has:

$$
\boxed{
\begin{array}{c|c}
\Omega(c)=0&
\text{eight-state affine potential }p;\\
\Omega(c)\ne0&
\text{common scalar-sheet cut }\eta
\text{ with odd terminal word}.
\end{array}}
$$

No finite boundary-state enumeration remains in this dichotomy.

## 10. Localisation boundary

The theorem does **not** prove:

1. $\eta$ is a cut in the underlying four-pole $Q$;
2. $\eta$ has bounded size or connected support;
3. $\eta$ gives a Whitney, dot-product, transition-matroid, or four-pole replacement;
4. the odd terminal bit is the physical DDD class;
5. the flat potential fibres admit a bounded transfer-state compression;
6. either branch decreases a graph-theoretic measure.

These are the exact localisation/composition obligations.

## 11. Completion assessment

`AC-PD-B7.1` is `COMPLETE-DRAFT / LOCALISATION-OPEN`. The next unit isolates the Type T and full-rank flat/nonflat source-localisation gaps and returns them to AC-RL in a nonredundant form.