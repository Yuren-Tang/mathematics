# AC-PD-B4 — reconfiguration and transport hierarchy

**Proof-development state:** `READY-FOR-CURATOR / FRONTIER-EXPLICIT`  
**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Exact initial corpus base:** `main@960c92b7ff231c78b387894149779083060a75eb`  
**Constituent units:** B4.1–B4.3  
**External mathematical inputs:** none for the proved motion laws  
**Assurance:** complete authorial proof-development checkpoint for the exact vertical/horizontal mechanics; global escape remains open

## 0. The two-level state space

Let

$$
\mathscr E(G)
=
\{(f,g):f\text{ a nowhere-zero }\mathbf F_2^3\text{-flow},\ g\text{ a compatible root lift above }f\}.
$$

Projection to $f$ gives a family of affine fibres. There are two fundamentally different motions.

1. **Vertical:** change $g$ inside one fixed fibre by an admissible vertex translation.
2. **Horizontal:** change $f$ by a connected-cycle switch; choose or construct a lift in the new fibre.

A support-cycle pivot is a special horizontal edge with an explicit root-level lift that preserves the uncoloured embedding.

## 1. Vertical gauge motion

For fixed $f$, define

$$
H_f^0
=
\{k:V(G)\to\Gamma:
 k_u+k_v\in\langle f(e)\rangle\text{ on every }e=uv\}.
$$

The labelled root lifts above $f$ form a torsor under $H_f^0$:

$$
g^k(e)=\tau_{k_u}(g(e)).
$$

The edge bits

$$
k_u+k_v=\lambda_e f(e)
$$

define the gauge code $\mathcal B_f$. If $G$ has edge-bearing components $G_i$, then

$$
\mathcal B_f
\cong
H_f^0/\Gamma^{\pi_0(G)}.
$$

Thus the connected formula $H_f^0/\Gamma$ must not be applied unchanged to disconnected graphs.

## 2. Harmonic quotient and partial Petrial

For a nonzero gauge word $\lambda$ with support $S$, the potential is constant on every component of $G-S$. On the contracted quotient, crossing-edge labels are both a nowhere-zero flow and an exact tension.

Topologically, $\lambda_e$ records whether the two support-face sides are swapped across $e$. Hence

$$
\boxed{
S_{g^k}=S_g^{\tau(\operatorname{supp}\lambda)}.}
$$

The gauge code is exactly the code of partial Petrials accessible while the projected Fano flow is fixed.

Vertical motion may change the surface, full dual, old-colour quotient, and both notions of half-cube compressibility; it preserves the Fano flow.

## 3. Connected horizontal switches

For $0\ne a\in\Gamma$ and a binary cycle word $z$,

$$
f^{z,a}=f+az
$$

is nowhere zero exactly when $z$ avoids the colour class $E_a=f^{-1}(a)$.

In a cubic graph, the support of $z$ is a disjoint union of connected source cycles. If

$$
z=\mathbf1_{C_1}+\cdots+\mathbf1_{C_m},
$$

then the total switch is a commuting path through the $m$ component switches. Exactly the case $m=1$ is one edge of the nowhere-zero-flow reconfiguration graph.

Conversely, two exponent-two flows agreeing outside one connected source cycle differ by one constant nonzero value on that cycle.

## 4. Support-cycle pivots

If $C$ is a connected component of support $F_c$ and root $cd$ is absent on $C$, then

$$
\{c,s_e\}\mapsto\{d,s_e\}
$$

on $C$ produces a root lift of

$$
f+(c+d)\mathbf1_C.
$$

This operation:

- is one connected horizontal reconfiguration edge;
- preserves the uncoloured cycle-face embedding and full dual;
- recolours one face component;
- changes the Fano flow, old-colour quotient, and generally the new gauge code.

Not every connected switch is directly pivotable above a prescribed old lift.

## 5. Exact used-root update

For a support pivot, let $R_C$ be the old roots whose every occurrence lies on $C$, and let $A_{C,d}$ be the previously unused new roots introduced on $C$. Then

$$
\boxed{
U_{g'}=(U_g\cup R_C)\setminus A_{C,d}.}
$$

This is an exact factorable-quotient transport law. It says nothing by itself about the unchanged full dual's map to $\mathscr A_5$.

## 6. Gauge fibre after switching

Under a connected switch, only the edge-line constraints on the switched cycle change:

$$
\langle f(e)\rangle
\rightsquigarrow
\langle f(e)+a\rangle.
$$

There is no general invariance of

$$
\dim H_f^0,
\qquad
\mathcal B_f,
\qquad
\text{or the Petrial orbit}.
$$

A pivot gives one distinguished lift in the new fibre; the remaining fibre must be solved from the new admissible-translation system.

## 7. Fixed-plane internal corrections

For a plane $W=\ker b$ and coordinates $f=(b,x,y)$, an internal switch $t\in W$ may be normalized to

$$
f'=(b,x+z,y).
$$

The quotient $Q_W$ stays fixed and

$$
\boxed{
d_W(f')+d_W(f)=\partial_{Q_W}(y*z).}
$$

For all composite $t$-switch words, the exact correction image is

$$
q_*\bigl(\mathsf B(R_1)\cap\mathsf B(R_0)\bigr)
=
\sigma_q\mathcal C(\mathscr I_{W,t}).
$$

The dual obstructions are fibre-constant cut words of the bipartite component-incidence graph.

## 8. Fixed-plane external reslicing

For $t\notin W$, choose coordinates

$$
f=(b,x,y),
\qquad
f'=(b+z,x,y).
$$

The Schur word $p=x*y$ and the zero matching

$$
M=f^{-1}(t)
$$

remain fixed, while the quotient is resliced:

$$
\boxed{d_W(f')=\partial_{Q_{b+z}}(p).}
$$

All same-direction composite endpoints correspond exactly to even supports $B'\supseteq M$. Such an endpoint is good precisely when

$$
|M\cap\delta_G(K)|\equiv0\pmod2
$$

for every component $K$ of $G-B'$.

## 9. Connected versus composite correction

The linear internal image and the affine family of external reslicings range over all cycle words, including disconnected supports. They classify endpoints reachable by commuting same-direction paths.

One reconfiguration neighbour additionally requires connected support. The connected-neighbour correction set is generally not a vector subspace. Therefore phrases such as “one-switch correction is completely linear” must be read as “the composite same-direction endpoint problem is linear”.

For the thirty-vertex laboratory:

- 7737 counts all nonzero admissible pairs $(a,z)$;
- 2801 have connected support and are genuine one-edge neighbours;
- the corresponding success tables must remain separate certificate populations.

## 10. Exact preservation table

$$
\begin{array}{c|c|c|c}
\text{motion}&f&\text{uncoloured embedding}&\text{fibre action}\\
\hline
\text{gauge/Petrial}&\text{fixed}&\text{may change}&H_f^0\text{-translation}\\
\text{support pivot}&\text{changes}&\text{fixed}&\text{one explicit new lift}\\
\text{general connected switch}&\text{changes}&\text{not canonically transported}&\text{new affine solve}\\
\text{disconnected switch}&\text{path of changes}&\text{sequence}&\text{successive fibres}.
\end{array}
$$

## 11. Genuine unresolved reconfiguration questions

The proved mechanics do not imply any of the following.

1. Every fixed flow fibre contains a full-dual-good lift.
2. Every reconfiguration component contains a good flow.
3. Every factorably bad one-star core can be escaped by an actual source-realizable sequence.
4. The union of connected-neighbour correction sets always kills some plane defect.
5. A monotone compression potential exists along connected reconfiguration edges.

These are genuine source/global questions. They are not missing definitions or omitted linear-algebra proofs.

## 12. Programme transition

B4 closes the exact motion laws and exposes the source interfaces on which movement can fail. B5 becomes active: three-edge cuts, four-poles, boundary signatures, cap forcing, Kempe closure, and exact gluing.

The separator programme can proceed independently of a global escape theorem and may supply the decomposition alternative needed when reconfiguration is blocked.

## 13. Completion assessment

`AC-PD-B4` is `READY-FOR-CURATOR / FRONTIER-EXPLICIT`. No claim of universal flow connectedness or five-support existence is made.