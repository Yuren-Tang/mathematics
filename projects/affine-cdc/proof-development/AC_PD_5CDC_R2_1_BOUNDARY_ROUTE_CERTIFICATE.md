# AC-PD-5CDC-R2.1 — boundary states and fixed-route certificate

**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Programme:** compressed five-support proof, extension unit `R2`  
**Classification:** `COMPLETE-DRAFT / FINITE CERTIFICATE RECONSTRUCTED`.

This dossier independently reconstructs the finite boundary layer consumed by:

- `ONE_CROSS_SINGULAR_FIXED_ROUTE_REDUCTION_V1.md`;
- `TEN_STATE_BOUNDARY_GRAPH_RIGIDITY_V1.md`;
- `ONE_CROSS_CAP_RESTORATION_THEOREM_V1.md`.

The reconstruction uses an explicit exhaustive enumeration over the ten roots of `E_5`, checked with Wolfram Language. The finite output is also derived below from the boundary formulas. It is a certificate for the stated finite claims, not a proof of the later singular-confluence theorem.

---

## 1. Root model

Identify a root with a two-subset of `[5]`, or equivalently a binary word of length five and Hamming weight two:

\[
R_5=\{e_a+e_b:1\le a<b\le5\}.
\]

There are ten roots. For two roots `p,q`:

- `p=q` gives `p+q=0`;
- distinct intersecting roots have a weight-two sum, hence another root;
- disjoint roots have a weight-four sum, hence one co-root.

The exhaustive pair count is:

\[
10\text{ roots},\qquad
30\text{ intersecting unordered distinct pairs},\qquad
15\text{ disjoint pairs}.
\]

---

## 2. Conserved ordered four-root boundaries

Let the ordered terminals be `1,2,3,4`. A boundary word is

\[
\mathbf r=(r_1,r_2,r_3,r_4)\in R_5^4
\]

with

\[
r_1+r_2+r_3+r_4=0.
\]

For each support coordinate `a\in[5]`, define the even trace

\[
S_a=\{t\in[4]:a\in r_t\}.
\]

Conservation is equivalent to every `S_a` having even cardinality. Every terminal belongs to exactly two traces.

Direct enumeration gives exactly

\[
\boxed{640}
\]

ordered conserved root quadruples.

---

## 3. Routing-weight coordinates and the ten states

Use the matchings

\[
M_0=12\mid34,
\qquad
M_1=13\mid24,
\qquad
M_2=14\mid23.
\]

For `M_i=X_i\mid Y_i`, define

\[
q_i(S)=|S\cap X_i|\pmod2,
\qquad
\omega_i(\mathbf r)=\frac12\sum_{a=1}^5q_i(S_a).
\]

The value is in `\{0,1,2\}`. Exhaustion of the 640 words gives exactly the following ten triples:

\[
\begin{array}{c|c|c}
\text{state}&(\omega_0,\omega_1,\omega_2)&\text{ordered-word count}\\
\hline
A&(0,0,0)&10\\
B_0&(0,1,1)&60\\
B_1&(1,0,1)&60\\
B_2&(1,1,0)&60\\
C_0&(0,2,2)&30\\
C_1&(2,0,2)&30\\
C_2&(2,2,0)&30\\
D_0&(2,1,1)&120\\
D_1&(1,2,1)&120\\
D_2&(1,1,2)&120.
\end{array}
\]

The counts sum to 640 and the coordinate map is injective on support-unordered states.

---

## 4. Direct reconnection profiles

The zero-vertex reconnection `E_i` pairs the terminals according to `M_i`. A boundary word extends across `E_i` exactly when the two roots in each matching block are equal.

The exhaustive profiles are therefore

\[
\boxed{
\Sigma(E_i)=J_i=\{A,B_i,C_i\}.}
\]

For example,

\[
\Sigma(E_0)=
\{(0,0,0),(0,1,1),(0,2,2)\}.
\]

The three cases correspond respectively to equal paired roots `p=q` at the two reconnection edges, distinct intersecting paired roots, and disjoint paired roots.

---

## 5. Two-vertex cap profiles

For the standard cap `cap_i`, the two terminals in a block meet one cap vertex. The internal edge value is the sum of the two boundary roots in that block. Since the total boundary sum is zero, the two block sums agree.

The cap extends root-valuedly exactly when this common sum has weight two. Hence

\[
\boxed{
\Sigma(cap_i)=K_i=\{B_j,B_k,D_j,D_k\},
\qquad \{i,j,k\}=\{0,1,2\}.}
\]

For `i=0`,

\[
K_0=\{B_1,B_2,D_1,D_2\}.
\]

In particular, for a selected cross `j\ne i`,

\[
\boxed{J_j\cap K_i=\{B_j\}.}
\]

Thus the selected cross boundary is immediately cap-compatible precisely in its intersecting-root state `B_j`; the remaining selected states are equality `A` and DDD/co-root `C_j`.

---

## 6. Complementary support-pair challenge

Let `s=e_a+e_b\in R_5` be a support-pair transposition. It is a four-terminal complementary challenge for `\mathbf r` when every boundary root contains exactly one of `a,b`:

\[
|r_t\cap\{a,b\}|=1
\qquad(t=1,2,3,4).
\]

Equivalently, the two support traces differ at all four terminals.

For route `M_i=X_i\mid Y_i`, switch the connected component with terminal block `X_i`:

\[
r'_t=
\begin{cases}
r_t+s,&t\in X_i,\\
r_t,&t\notin X_i.
\end{cases}
\]

Every changed label is again a root because it is the symmetric difference of two intersecting distinct roots. Switching the other block `Y_i` differs from this word by applying the global support transposition `(a\ b)` at all four terminals, so both choices have the same support-unordered target. Thus each labelled challenge has one well-defined target for each of the three physical routes.

---

## 7. Complete route rows

The exhaustive row types, written as

\[
\text{source}\longmapsto
(M_0\text{-target},M_1\text{-target},M_2\text{-target}),
\]

are:

\[
\begin{array}{c|c}
A&(B_0,B_1,B_2)\\
B_0&(A,B_2,B_1)\\
B_0&(C_0,D_2,D_1)\\
C_0&(B_0,D_1,D_2)\\
B_1&(B_2,A,B_0)\\
B_1&(D_2,C_1,D_0)\\
C_1&(D_0,B_1,D_2)\\
B_2&(B_1,B_0,A)\\
B_2&(D_1,D_0,C_2)\\
C_2&(D_0,D_1,B_2)\\
D_0&(C_1,D_2,B_1)\\
D_0&(C_2,B_2,D_1)\\
D_1&(B_2,D_0,C_2)\\
D_1&(D_2,B_0,C_0)\\
D_2&(B_1,C_0,D_0)\\
D_2&(D_1,C_1,B_0).
\end{array}
\]

Repeated labelled challenge instances collapse to these sixteen support-unordered rows.

For fixed route `M_0`, the resulting undirected transition graph is

\[
\boxed{
A-B_0-C_0
\quad\sqcup\quad
B_1-B_2-D_1-D_2-B_1
\quad\sqcup\quad
C_1-D_0-C_2.}
\]

The other two route graphs follow by permuting matching indices. Hence

\[
\boxed{\Gamma_i\cong P_3\sqcup C_4\sqcup P_3,}
\]

with components `J_i,K_i,L_i`.

---

## 8. Exact one-cross fixed-route consequence

Fix the original cap index `i=0`; the other cases follow by symmetry. Then

\[
K_0=\{B_1,B_2,D_1,D_2\}.
\]

### Equality sector

The selected equality state `A` has route targets

\[
(B_0,B_1,B_2).
\]

Exactly the `M_0` target avoids `K_0`. At `B_0`, the two row types have targets

\[
(A,B_2,B_1),
\qquad
(C_0,D_2,D_1),
\]

and at `C_0` the target triple is

\[
(B_0,D_1,D_2).
\]

Again exactly the `M_0` target avoids `K_0`. Therefore a cap-blocked equality orbit is confined to

\[
A-B_0-C_0
\]

and every realised nonseparating challenge is physically routed by `M_0`.

### DDD sector

For selected cross `j=1`, the DDD state is `C_1`. Its target triple is

\[
(D_0,B_1,D_2),
\]

so only route `M_0` avoids `K_0`. The two rows at `D_0` are

\[
(C_1,D_2,B_1),
\qquad
(C_2,B_2,D_1),
\]

and the row at `C_2` is

\[
(D_0,D_1,B_2).
\]

Thus the blocked DDD orbit is confined to

\[
C_1-D_0-C_2
\]

and every realised challenge is routed by `M_0`.

Consequently the finite statement used by the compressed proof is verified:

\[
\boxed{
\text{one selected cross flow}
\Longrightarrow
\text{immediate cap compatibility, separating rescue, or one fixed-route equality/DDD lock}.}
\]

The distinction between a separating challenge component and a full-channel lock is graph-theoretic and remains part of the next singular-carrier proof unit.

---

## 9. Reproducible computation boundary

The Wolfram enumeration used only:

1. the ten weight-two binary vectors in `\mathbf F_2^5`;
2. ordered quadruples with binary sum zero;
3. the trace and `\omega_i` formulas;
4. equality on matching blocks for `E_i`;
5. the root test for the cap block sum;
6. the complementary-challenge intersection test and block switch above.

It returned:

- `640` conserved words;
- the ten triples and counts in Section 3;
- `J_i` and `K_i` exactly;
- the sixteen route-row types;
- `P_3\sqcup C_4\sqcup P_3` for each fixed matching.

No physical interior-route existence is inferred from the boundary enumeration alone. The table classifies the target of a challenge conditional on its actual terminal matching. The later lock theorem must still prove the required physical carrier, recurrence and return statements.