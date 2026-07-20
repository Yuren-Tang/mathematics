# AC-PD-B4.3 — switch transport, defect images, and connected-neighbour scope

**Proof-development state:** `COMPLETE-DRAFT / SCOPE-CORRECTION`  
**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Exact initial corpus base:** `main@960c92b7ff231c78b387894149779083060a75eb`  
**Validated sources:** `FIVE_CDC_ADMISSIBLE_SWITCH_IMAGE_V1.md`, `FIVE_CDC_SWITCH_INCIDENCE_GRAPH_V1.md`, `FIVE_CDC_INTERNAL_EXTERNAL_SWITCH_DICHOTOMY_V1.md`, `FIVE_CDC_BAD_LIFT_CONTAINER_DICHOTOMY_V1.md`, and the controlling scope correction  
**Depends on:** B1.3 fixed-plane criterion; B2.1 Schur quotient; B4.2 connected-switch decomposition  
**Immediate consumers:** B4 consolidation; B5 routing states; B6 holonomy; B7 localisation  
**External mathematical inputs:** none

## 0. Central scope correction

For fixed nonzero $t$, the admissible switch words form the linear space

$$
\mathcal C(G-E_t),
\qquad E_t=f^{-1}(t).
$$

Its full linear image describes endpoints reachable by a commuting sequence of connected $t$-switches. It does **not** generally describe only the one-edge neighbours of $f$: imposing connected support is nonlinear.

Accordingly this dossier uses:

- **connected switch** for one reconfiguration edge;
- **composite $t$-switch** for arbitrary $z\in\mathcal C(G-E_t)$;
- **linear correction image** for all composite endpoints.

## 1. Used-root transport under a support pivot

Let $g'$ be obtained from $g$ by pivoting the support-cycle component $C\subseteq F_c$ from centre $c$ to $d$. For a root $r$, let $m_g(r)$ be its total multiplicity. For every leaf $s$ occurring on $C$, let $m_C(s)$ count the $cs$-labelled edges of $C$.

Define

$$
R_C=
\{cs:m_g(cs)=m_C(s)>0\},
$$

and

$$
A_{C,d}=
\{ds:m_g(ds)=0,\ m_C(s)>0\}.
$$

Here $R_C$ is the set of old roots released from global use, and $A_{C,d}$ is the set of previously unused new roots consumed by the pivot.

### Theorem 1.1 — exact unused-root update

Writing $U_g=K_8-J_g$,

$$
\boxed{
U_{g'}=(U_g\cup R_C)\setminus A_{C,d}.}
$$

### Proof

An old root $cs$ becomes unused exactly when all its occurrences lay on $C$. A new root $ds$ ceases to be unused exactly when it was absent globally and is introduced on $C$. Every other root retains at least one occurrence status. $\square$

This formula concerns the factorable quotient $J_g$. The full dual triangulation is unchanged by the pivot.

## 2. Gauge-space transport under a flow switch

Let

$$
f'=f+a\mathbf1_C
$$

be a connected switch. The gauge space of the new flow is

$$
H_{f'}^0
=
\{k:k_u+k_v\in\langle f'(e)\rangle\text{ on every edge}\}.
$$

Only the edge constraints on $C$ change, from the lines $\langle f(e)\rangle$ to $\langle f(e)+a\rangle$.

### Proposition 2.1 — local constraint replacement

There is no general invariance of

$$
\dim H_f^0,
\qquad
\mathcal B_f,
\qquad
\text{or the Petrial orbit}
$$

under a connected switch. They are obtained by replacing precisely the cycle-edge blocks in the admissible-translation linear system.

A support pivot supplies one distinguished lift above $f'$, but the rest of the new fibre must be computed from $H_{f'}^0$; it is not transported canonically from $H_f^0$.

### Proof

The assertion follows directly from the defining edge-line constraints. The switched and unswitched lines need not agree, and their intersections across the cycle may change the rank in either direction. $\square$

Specific equal-rank phenomena in finite laboratories remain certificate facts, not general switch invariants.

## 3. Internal switch relative to a plane

Fix a plane

$$
W=\ker b
$$

and coordinates

$$
f=(b,x,y).
$$

Let $0\ne t\in W$ and choose coordinates so that $t$ is the $x$-direction. For $z\in\mathcal C(G-E_t)$,

$$
f'=(b,x+z,y).
$$

Thus $G_W$, its component quotient $Q_W$, and the plane-membership word $b$ remain fixed. The Schur word changes by

$$
(x+z)*y+x*y=z*y.
$$

### Theorem 3.1 — internal defect update

$$
\boxed{
d_W(f')+d_W(f)=\partial_{Q_W}(y*z).}
$$

### Proof

Use the Schur formula

$$
d_W(f)=\partial_{Q_W}(x*y)
$$

and linearity of the quotient boundary. $\square$

This endpoint update is linear in $z$ because the quotient is fixed.

## 4. Exact composite internal image

Let $A_t=E_t$, let $H_t=G_W-A_t$, and contract the connected components of $H_t$ to form the refined quotient $R_{W,t}$. Its edge set is the set of outside-plane edges. Split it into $R_0,R_1$ according to the remaining coordinate $y$.

Let

$$
q:V(R_{W,t})\twoheadrightarrow V(Q_W)
$$

be the final quotient induced by restoring the deleted $t$-matching.

### Theorem 4.1 — composite correction image

The set of all defect changes arising from arbitrary composite $t$-switch words is

$$
\boxed{
\operatorname{Im}\Delta^{\mathrm{comp}}_{W,t}
=
q_*\bigl(\mathsf B(R_1)\cap\mathsf B(R_0)\bigr).}
$$

### Proof

Contraction induces a surjection

$$
\mathcal C(G-A_t)\twoheadrightarrow\mathcal C(R_{W,t}).
$$

For a quotient cycle $Z=Z_1+Z_0$ split by the $y$-colour, one has

$$
\partial Z_1=\partial Z_0,
\qquad
y*Z=Z_1.
$$

Thus the pre-quotient correction is in both boundary spaces. Conversely, any common boundary is represented by edge sets $Z_1,Z_0$ with equal boundary; their sum is a quotient cycle. Fibrewise summation gives the $Q_W$ defect. $\square$

The dimension before $q_*$ is

$$
|V(R_{W,t})|-c(R_0)-c(R_1)+c(R_{W,t}).
$$

## 5. Component-incidence cycle code

Construct the bipartite multigraph $\mathscr I_{W,t}$ whose left vertices are the components of $R_0$, whose right vertices are the components of $R_1$, and whose edges are the vertices of $R_{W,t}$.

### Theorem 5.1

Under the natural identification

$$
\mathbf F_2^{V(R_{W,t})}
\cong
\mathbf F_2^{E(\mathscr I_{W,t})},
$$

one has

$$
\mathsf B(R_0)\cap\mathsf B(R_1)
\cong
\mathcal C(\mathscr I_{W,t}).
$$

Hence

$$
\operatorname{Im}\Delta^{\mathrm{comp}}_{W,t}
=
\sigma_q\mathcal C(\mathscr I_{W,t}).
$$

### Proof

Membership in $\mathsf B(R_i)$ is even coordinate sum on every $R_i$-component, exactly the even-degree condition at the corresponding side of the bipartite incidence graph. $\square$

The dual failure certificates are fibre-constant cut words of $\mathscr I_{W,t}$.

## 6. Connected-neighbour image

Define

$$
\operatorname{Im}\Delta^{\mathrm{conn}}_{W,t}
=
\{d_W(f+t\mathbf1_C)+d_W(f):
C\subseteq G-E_t\text{ a connected cycle}\}.
$$

Then

$$
\operatorname{Im}\Delta^{\mathrm{conn}}_{W,t}
\subseteq
\operatorname{Im}\Delta^{\mathrm{comp}}_{W,t},
$$

but the left side need not be a vector subspace and equality is not automatic.

Every element of the composite image is a sum of corrections along a path of connected $t$-switches, but the intermediate defect is evaluated after each switch. In the internal case the quotient stays fixed and the endpoint corrections add linearly, so the composite image is the linear span of the connected component corrections. This does not make every sum one adjacency.

Thus the statement

> the current defect lies in the linear image

means correction by a same-direction commuting path, not necessarily by one reconfiguration edge.

## 7. External reslicing

Now let $t\notin W$. Choose coordinates with

$$
f=(b,x,y),
qquad b(t)=1,
$$

and $x,y$ annihilating $t$. Then

$$
f'=(b+z,x,y).
$$

The Schur word

$$
p=x*y
$$

is fixed, while the zero subgraph and contracted quotient change.

### Theorem 7.1 — external endpoint formula

$$
\boxed{
d_W(f')=\partial_{Q_{b+z}}(p).}
$$

Thus an external switch is quotient reslicing rather than correction inside a fixed quotient.

Put

$$
M=\{e:(x_e,y_e)=(0,0)\}=f^{-1}(t).
$$

Then $M$ is a matching, and $w=(x,y)$ is a nowhere-zero $W$-flow on $G-M$.

### Theorem 7.2 — composite external criterion

As $z$ ranges over all of $\mathcal C(G-M)$, the possible new plane-membership supports are exactly the even supports

$$
B'\supseteq M.
$$

Such an endpoint is good for $W$ exactly when every component $K$ of $G-B'$ satisfies

$$
|M\cap\delta_G(K)|\equiv0\pmod2.
$$

### Proof

The initial support $B=\operatorname{supp}b$ is even and contains $M$. Another binary flow support $B'$ contains $M$ exactly when $b+b'$ is a cycle word vanishing on $M$. The fixed-plane colour-cut criterion gives the displayed component parity. $\square$

Again this classifies all same-direction composite endpoints. One connected external neighbour additionally requires that $B+B'$ be one connected source cycle.

## 8. Internal/external dichotomy

Relative to $W$:

$$
\begin{array}{c|c|c}
&t\in W&t\notin W\\
\hline
\text{operation}&\text{coordinate correction}&\text{quotient reslicing}\\
\text{fixed}&b,Q_W&x,y,p=x*y,M\\
\text{variable}&x\text{ or }y&b,G-B\\
\text{composite criterion}&\text{linear syndrome image}&\text{matching parity after reslicing}.
\end{array}
$$

The connected-neighbour subproblem must be imposed separately in both columns.

## 9. Assurance and finite data

The root update, gauge constraint replacement, internal/external formulas, composite image, incidence-code theorem, and connectedness scope are theorem-level. Ranks, fibre dimensions, and success counts in named laboratories remain certificate data.

## 10. Completion assessment

`AC-PD-B4.3` is `COMPLETE-DRAFT / SCOPE-CORRECTION`. The next unit consolidates B4 and identifies the first unresolved reconfiguration statement requiring more than mature proof normalization.