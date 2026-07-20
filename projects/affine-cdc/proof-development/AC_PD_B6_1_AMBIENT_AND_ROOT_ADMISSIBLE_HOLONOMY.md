# AC-PD-B6.1 — ambient affine holonomy and local root-admissibility

**Proof-development state:** `COMPLETE-DRAFT / GLOBAL-WITNESS-OPEN`  
**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Exact initial corpus base:** `main@960c92b7ff231c78b387894149779083060a75eb`  
**Validated sources:** `FIVE_CDC_RAINBOW_CHOICE_PARITY_SQUARE_V1.md`, `FIVE_CDC_RAINBOW_RESIDUAL_QUOTIENT_COORDINATES_V1.md`, `FIVE_CDC_INTERIOR_AFFINE_HOLONOMY_NORM_V1.md`, and `FIVE_CDC_ROOT_ADMISSIBLE_HOLONOMY_LINEARIZATION_V1.md`  
**Depends on:** B2.1 minus-type root space; B5 Type H boundary mechanism  
**Immediate consumers:** B6.2 path-family mechanisms; B6.3 BBD/DDD synthesis; B7 route-lock  
**External mathematical inputs:** none

## 0. Scope

Let $P$ be a connected four-pole. Write

$$
E_5=\{v\in\mathbf F_2^5:\sum_i v_i=0\},
\qquad
R_5=\{\varepsilon_i+\varepsilon_j:i<j\}.
$$

Let

$$
M_P=Z_1(P)\otimes E_5.
$$

The ambient affine theory treats all $E_5$-valued cycle tensors. Root-valued five-support covers form a nonlinear subset: every edge coordinate must lie in $R_5$. Ambient linearizability is therefore necessary but not sufficient for root-admissible linearization.

## 1. Interior holonomy datum

Represent an indexed support cover by

$$
x\in C_1(P)\otimes E_5.
$$

Suppose a lifted quotient loop starts at $x$, ends at $x^\gamma$, and closes its support-unordered boundary state with support-index transport $\pi\in S_5$:

$$
\partial x^\gamma=\pi(\partial x).
$$

Define

$$
z_\gamma=x^\gamma+\pi x.
$$

### Proposition 1.1

$$
\boxed{z_\gamma\in M_P.}
$$

### Proof

The two chains $x^\gamma$ and $\pi x$ have identical indexed terminal traces. Their difference is therefore coordinatewise an interior cycle; both are $E_5$-valued. $\square$

The pair

$$
(\pi,z_\gamma)
$$

is the ambient interior holonomy datum.

## 2. Repeatability boundary

A lifted loop is **repeatable** when the chosen sequence of indexed switches may be transported through the resulting support labels and traversed again. Only under this hypothesis does iteration act on the ambient difference torsor by one fixed affine map

$$
A_{\pi,z}(u)=\pi u+z.
$$

Boundary monodromy alone does not prove repeatability inside the nonlinear root-valued state space.

## 3. Origin change and norm

Changing affine origin by $y\in M_P$ replaces

$$
z\longmapsto z+(1+\pi)y.
$$

Let

$$
m=\operatorname{ord}(\pi),
\qquad
N_\pi=1+\pi+\cdots+\pi^{m-1}.
$$

### Theorem 3.1 — iteration and norm defect

For every $r\ge1$,

$$
A_{\pi,z}^r(u)
=
\pi^ru+
\sum_{j=0}^{r-1}\pi^jz.
$$

In particular,

$$
A_{\pi,z}^m(u)=u+d,
\qquad
\boxed{d=N_\pi z},
$$

and $\pi d=d$. Moreover $d$ is invariant under every origin change.

### Proof

Induct on $r$. The origin invariance follows from

$$
N_\pi(1+\pi)=1+\pi^m=0.
$$

$\square$

## 4. Exact cohomology table

For the four rainbow support-permutation types, the action on $E_5$ has:

$$
\begin{array}{c|c|c|c|c|c}
\text{type}&m&\dim E_5^\pi&\operatorname{rank}N_\pi&\operatorname{rank}(1+\pi)&\dim H^1\\
\hline
2^2 1&2&2&2&2&0\\
4 1&4&1&1&3&0\\
3 2&6&1&1&3&0\\
5&5&0&0&4&0.
\end{array}
$$

Here

$$
H^1(\langle\pi\rangle,E_5)
=
\ker N_\pi/\operatorname{im}(1+\pi).
$$

### Theorem 4.1

For all four types,

$$
\boxed{
\operatorname{im}N_\pi=E_5^\pi,
\qquad
\ker N_\pi=\operatorname{im}(1+\pi).}
$$

### Proof

Use canonical representatives.

- For $(12)(34)$, fixed even words are $(a,a,b,b,0)$, a two-space. Both $N_\pi=1+\pi$ and $1+\pi$ have rank two.
- For $(1234)$, fixed even words are multiples of $11110$. The norm maps onto this line. The kernel of $1+\pi$ is that fixed line, so $1+\pi$ has rank three; the norm kernel also has dimension three.
- For $(123)(45)$, fixed even words are multiples of $00011$. The norm maps onto this line; both the norm kernel and image of $1+\pi$ have dimension three.
- For $(12345)$, the only fixed even word is zero. The norm is zero because it sums all five coordinates and the total parity is zero; $1+\pi$ is invertible on $E_5$.

The universal inclusion $\operatorname{im}(1+\pi)\subseteq\ker N_\pi$ and the dimension equalities give the result. $\square$

Tensoring with the trivially acted-on cycle space yields

$$
H^1(\langle\pi\rangle,M_P)=0.
$$

## 5. Complete ambient affine classification

### Theorem 5.1

For a repeatable ambient affine loop $A(u)=\pi u+z$ of one of the four types:

1. if $d=N_\pi z\ne0$, then $A^m$ is the nontrivial translation by $d$ and $A$ has order $2m$;
2. if $d=0$, then $z=(1+\pi)y$ for some $y\in M_P$, and translation by $y$ conjugates $A$ to the pure linear action $u\mapsto\pi u$.

Thus $N_\pi z$ is the complete ambient affine-conjugacy obstruction.

### Proof

The first part follows from Theorem 3.1 and the fact that a nonzero binary translation has order two. For the second, $d=0$ places $z$ in $\ker N_\pi=\operatorname{im}(1+\pi)$. $\square$

This theorem does not assert root-valued conjugacy.

## 6. Boundary choice quotient

For a BBD rainbow triangle, the six raw role/path bits form $q\in\mathbf F_2^6$. Exact finite tables show a common two-dimensional redundancy kernel

$$
K_{\mathrm{raw}}
=
\langle010001,101000\rangle,
$$

so the sixteen support monodromies are parametrized by

$$
\mathbf F_2^6/K_{\mathrm{raw}}\cong\mathbf F_2^4.
$$

Four coordinates may be chosen as

$$
(\nu,\rho,\sigma,\tau).
$$

The first two have theorem-level mechanism meanings conditional on the exact table:

- $\rho=0$: rank-one path branch;
- $\rho=1$: full-rank XOR-cover branch;
- $\nu$ selects the support cycle type within that rank branch.

The residual coordinates $(\sigma,\tau)$ distinguish four monodromies in each parity cell but do not form a common Klein-four subgroup action in $S_5$. These assertions remain exact finite classification data.

## 7. Local root-admissible conjugation

Put

$$
Q_\pi=1+\pi.
$$

For a current edge root $x\in R_5$, define

$$
\mathcal A_\pi(x)
=
\{Q_\pi y:y\in E_5,\ x+y\in R_5\}.
$$

### Theorem 7.1 — root-image formula

$$
\boxed{
\mathcal A_\pi(x)=Q_\pi x+Q_\pi(R_5).}
$$

### Proof

The condition $x+y\in R_5$ means $y=x+r$ for some $r\in R_5$. Apply $Q_\pi$. $\square$

Thus the forbidden set is a translate of

$$
\mathcal F_\pi
=
\operatorname{im}Q_\pi\setminus Q_\pi(R_5).
$$

## 8. Exact four-type local table

For canonical representatives:

$$
\begin{array}{c|c|c}
\text{type}&|\operatorname{im}Q_\pi|&\mathcal F_\pi\\
\hline
2^2 1&4&\varnothing\\
4 1&8&\{0\}\\
3 2&8&\{k_\pi\}\\
5&16&Q_\pi(\{0\}\cup R_5^{(4)}).
\end{array}
$$

Here $k_\pi$ is the root fixed by the transposition in type $3\,2$, and $R_5^{(4)}$ is the set of five weight-four nonzero singular words.

### Proof

- For $2^2 1$, direct images of the ten two-subsets cover the four-dimensional-image set of size four.
- For $4 1$, no root is fixed, so zero is omitted; the seven nonzero image values occur.
- For $3 2$, the transposed pair root maps to zero; direct orbit calculation shows the unique omitted image value is that fixed root $k_\pi$.
- For a $5$-cycle, $Q_\pi$ is invertible. The ten roots therefore give ten distinct values; the six omitted values are the images of zero and the five weight-four words.

$\square$

Hence the local exclusion counts are

$$
\boxed{0,1,1,6.}
$$

## 9. Global root-admissible problem

If the ambient norm vanishes, one seeks

$$
y\in M_P
$$

such that

$$
Q_\pi y=z
$$

and, on every edge $e$,

$$
x(e)+y(e)\in R_5.
$$

The ambient equation is linear. The root condition is a translated edgewise list constraint with exclusion size $0,1,1,$ or $6$ according to the monodromy type.

Local admissibility at every edge separately does not imply the existence of one globally cycle-consistent $y$.

## 10. Exact frontier

The first mature but unresolved statements are:

1. type $2^2 1$: prove that every zero-norm ambient conjugator has a globally root-admissible cycle-tensor representative, or identify the precise global obstruction;
2. types $4 1$ and $3 2$: prove a one-forbidden-value cycle-space avoidance theorem, with failure forcing a cut or serial decomposition;
3. type $5$: understand the six-forbidden-value geometry under cycle constraints;
4. prove repeatability/root realizability of the lifted boundary loop;
5. prove a common interior witness across the four residual monodromies in one parity cell.

These are genuine nonlinear/source obligations.

## 11. Assurance boundary

The ambient chain, norm classification, cohomology vanishing, root-image formula, and local four-type table are theorem-level. The raw-choice quotient, parity square, residual coordinates, monodromy list, and DDD counts remain exact finite certificate data. No global root-admissible or common-witness theorem is claimed.

## 12. Completion assessment

`AC-PD-B6.1` is `COMPLETE-DRAFT / GLOBAL-WITNESS-OPEN`. The next unit audits the genuine path-family theorems that convert zero-norm rank branches into Tait escape or missed-vertex/uncovered-edge certificates.