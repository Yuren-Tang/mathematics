# AC-PD-B4.2 — support-cycle pivots and connected-cycle reconfiguration

**Proof-development state:** `COMPLETE-DRAFT / SCOPE-NORMALIZATION`  
**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Exact initial corpus base:** `main@960c92b7ff231c78b387894149779083060a75eb`  
**Validated sources:** `FIVE_CDC_SUPPORT_CYCLE_PIVOT_AND_FLOW_RECONFIGURATION_V1.md`, `FIVE_CDC_FLOW_SWITCH_HARMONIC_QUOTIENT_SURGERY_V1.md`, and `FIVE_CDC_HALFCUBE_SCOPE_CORRECTION_V1.md`  
**Depends on:** B1.1 root triangles; B4.1 vertical/embedding separation  
**Immediate consumers:** B4.3 transport laws; B5 interfaces; B6–B7 route and holonomy dynamics  
**External mathematical inputs:** none

## 0. Scope

Let $G$ be a finite loopless cubic multigraph and let

$$
f:E(G)\to\Gamma\setminus\{0\},
\qquad
\Gamma=\mathbf F_2^3,
$$

be a nowhere-zero flow. A connected-cycle switch is one edge of the chosen flow-reconfiguration graph. A switch on a disconnected binary cycle is a commuting composition of such edges, not one edge.

## 1. Binary rank-one switches

For a binary cycle word $z\in\mathcal C(G)$ and $0\ne a\in\Gamma$, define

$$
f^{z,a}=f+a z.
$$

### Lemma 1.1 — flow and nowhere-zero condition

The map $f^{z,a}$ is a flow. It is nowhere zero exactly when

$$
\operatorname{supp}z\cap E_a=\varnothing,
\qquad
E_a=\{e:f(e)=a\}.
$$

### Proof

At every vertex, $z$ has even incidence degree, so the added contribution is an even multiple of $a$. On a switched edge, $f(e)+a=0$ exactly when $f(e)=a$. $\square$

Thus admissible switch words of direction $a$ are precisely

$$
\mathcal C(G-E_a).
$$

## 2. Connected components of a cubic cycle word

Since $G$ is cubic, every vertex of the support of a binary cycle word has support degree zero or two.

### Lemma 2.1

Every nonempty connected component of $\operatorname{supp}z$ is a circuit: an ordinary source cycle or a two-edge parallel digon.

### Proof

A finite connected graph in which every vertex has degree two is a polygonal cycle; parallel edges permit the two-edge case. $\square$

Hence there is a unique decomposition

$$
z=\mathbf1_{C_1}+\cdots+\mathbf1_{C_m}
$$

into edge-disjoint connected cycle components.

## 3. Commuting decomposition theorem

### Theorem 3.1

Let $z\in\mathcal C(G-E_a)$ have connected components $C_1,\ldots,C_m$. For every ordering of these components, define

$$
f_j=f+a\sum_{i=1}^j\mathbf1_{C_i}.
$$

Then every $f_j$ is nowhere zero, every consecutive pair differs only on the connected cycle $C_j$, and

$$
f_m=f^{z,a}.
$$

The component switches commute.

### Proof

Each $C_i$ is contained in $G-E_a$. Switching earlier disjoint components changes no edge of $C_i$, so the old value on every edge of $C_i$ is still different from $a$. Lemma 1.1 therefore applies at every stage. Disjoint support additions commute in the binary vector space. $\square$

### Corollary 3.2 — exact adjacency boundary

- If $m=1$, $f$ and $f^{z,a}$ are adjacent by one connected-cycle reconfiguration edge.
- If $m>1$, the displayed switch is canonically a commuting path of $m$ connected-cycle moves. It is not counted as one edge merely because the total difference has rank one as a tensor.

No claim is made that the displayed path is geodesically shortest among all possible reconfiguration paths.

## 4. Characterization of exponent-two adjacency

Suppose two nowhere-zero $\Gamma$-flows $f,f'$ agree outside one connected source cycle $C$.

### Proposition 4.1

There is a unique nonzero $a\in\Gamma$ such that

$$
f'=f+a\mathbf1_C.
$$

### Proof

The difference $d=f+f'$ is a flow supported on $C$. At every cycle vertex, conservation forces the two incident difference values to be equal. Connectedness propagates one constant value $a$ around $C$. Since the flows differ, $a\ne0$. $\square$

Thus connected admissible rank-one switches are exactly the edges of the exponent-two nowhere-zero-flow reconfiguration graph.

## 5. Support-cycle pivots

Let $g:E(G)\to E(K_8)$ be a compatible root lift of $f$. For a support index $c$, put

$$
F_c=\{e:c\in g(e)\}.
$$

Every connected nonempty component $C$ of $F_c$ is a source cycle. Write

$$
g(e)=\{c,s_e\}
\qquad(e\in C).
$$

Choose $d\ne c$ such that no edge of $C$ has root label $\{c,d\}$. Define

$$
g'(e)=
\begin{cases}
\{d,s_e\},&e\in C,\\
g(e),&e\notin C.
\end{cases}
$$

### Theorem 5.1 — root-Kempe pivot

The labelling $g'$ is a compatible root lift of

$$
f'=f+(c+d)\mathbf1_C.
$$

The switched flow is nowhere zero.

### Proof

At a vertex of $C$, the two cycle roots are the two local target-triangle edges incident with $c$. Replacing $c$ by $d$ produces the target triangle on $d$ and the same other two support indices; the third local root is unchanged. The hypothesis that $cd$ is absent on $C$ says $d\ne s_e$ on every cycle edge, so no new root degenerates.

Both endpoints of an edge perform the same replacement, preserving compatibility. On $e\in C$, the projected direction changes by

$$
(d+s_e)+(c+s_e)=c+d.
$$

Moreover $f(e)=c+s_e$ cannot equal $c+d$, again because $s_e\ne d$, so Lemma 1.1 gives nowhere-zeroness. $\square$

A support-cycle pivot is therefore an explicit root-level lift of one connected-cycle flow-reconfiguration edge.

## 6. Embedding effect of a support pivot

### Theorem 6.1

A support-cycle pivot preserves the uncoloured cycle-face embedding and its full dual triangulation. It recolours the one face component bounded by $C$ from $c$ to $d$.

### Proof

The same source cycle $C$ remains a support component; only its common index changes. Every other root incidence and every edge-side pairing is unchanged. Therefore the two-cell decomposition and uncoloured dual remain fixed. $\square$

Consequently the truth value of

$$
T_g^{(1)}\to\mathscr A_5
$$

is unchanged by a bare support-cycle pivot, although the old-colour quotient $J_g$, the Fano flow, and the gauge code of the new fibre may change.

This distinguishes the direct pivot from subsequent vertical exploration in the new fibre.

## 7. Not every connected switch is a support pivot

A connected-cycle switch $f\mapsto f+a\mathbf1_C$ admits the direct support-pivot lift above a given root lift $g$ only when there are indices $c,d$ with

$$
a=c+d
$$

such that $C$ is one connected component of $F_c$ and $cd$ is absent on $C$.

Thus:

- every support pivot gives a connected switch;
- a general connected switch may require solving the new root-lift affine system rather than pivoting the old lift directly.

The base reconfiguration graph and the partially lifted root-state graph are not identical.

## 8. Correct interpretation of the finite census

For the thirty-vertex laboratory, the number

$$
7737
$$

counts all nonzero admissible pairs $(a,z)$ with

$$
z\in\mathcal C(G-E_a).
$$

Exactly

$$
2801
$$

of these words have connected support and are genuine one-edge neighbours. The other 4936 pairs are commuting multi-component paths. Outcome tables over all 7737 and over the connected 2801 are different populations and must remain separately labelled.

All numerical counts are certificate data. The decomposition theorem explaining their scope is independent of the computation.

## 9. Vertical versus horizontal motion

The exact two-level motion table is

$$
\begin{array}{c|c|c}
\text{move}&\text{uncoloured embedding}&\text{projected flow}\\
\hline
\text{gauge / partial Petrial}&\text{may change}&\text{fixed}\\
\text{support-cycle pivot}&\text{fixed}&\text{one connected switch}\\
\text{general connected switch}&\text{new lift must be chosen/solved}&\text{one connected switch}\\
\text{disconnected binary switch}&\text{sequence of states}&\text{commuting path}.
\end{array}
$$

## 10. Completion assessment

`AC-PD-B4.2` is `COMPLETE-DRAFT / SCOPE-NORMALIZATION`. The next active unit is B4.3: prove exact transport of local triangles, used-root graphs, gauge spaces, and obstruction predicates under support pivots and general connected switches, separating universal formulas from finite laboratory data.