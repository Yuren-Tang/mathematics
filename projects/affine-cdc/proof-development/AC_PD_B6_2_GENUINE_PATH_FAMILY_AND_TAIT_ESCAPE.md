# AC-PD-B6.2 — genuine rainbow path families and Type H Tait escape

**Proof-development state:** `COMPLETE-DRAFT / RESIDUAL-CERTIFICATES-LOCALIZED`  
**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Exact initial corpus base:** `main@960c92b7ff231c78b387894149779083060a75eb`  
**Validated sources:** `FIVE_CDC_RAINBOW_SWITCH_FLOW_TAIT_RESOLUTION_V1.md`, `FIVE_CDC_GENUINE_RAINBOW_PATH_FAMILY_REDUCTION_V1.md`, and `FIVE_CDC_TYPE_H_TAIT_ESCAPE_V1.md`  
**Depends on:** B5 Type H triangle mechanism; B6.1 ambient/root-admissible holonomy  
**Immediate consumers:** B6.3 BBD/DDD synthesis; B7 route-lock and localisation  
**External mathematical inputs:** none

## 0. Genuine three-path word

Let a physical lifted Type H rainbow loop switch three actual terminal-path components

$$
P_0,\qquad P_1,\qquad P_2
$$

in routing-colour order. The first and third transported support-pair coefficients agree; write them as $u$, and write the middle coefficient as $v$, with

$$
W=\langle u,v\rangle\cong\mathbf F_2^2.
$$

If $x$ is the initial indexed root cover and $x^\gamma$ the final indexed cover before quotienting support names, then

$$
\boxed{
 t_\gamma=x+x^\gamma
 =(P_0\triangle P_2)\otimes u+P_1\otimes v.}
$$

Put

$$
A=P_0\triangle P_2,
\qquad
B=P_1,
\qquad
\kappa=u+v.
$$

Edgewise,

$$
\begin{array}{c|c|c}
1_A&1_B&t_\gamma\\
\hline
0&0&0\\
1&0&u\\
0&1&v\\
1&1&\kappa.
\end{array}
$$

This formula is stronger than the description of an arbitrary low-rank quotient flow: the support chains are three selected terminal paths, not an unrestricted path-plus-cycle decomposition.

## 1. Quotient-flow lift equation

Let $\pi$ be the support monodromy and put

$$
Q_\pi=1+\pi.
$$

For the interior affine defect

$$
z=x^\gamma+\pi x,
$$

one has

$$
t_\gamma=Q_\pi x+z.
$$

Assume the ambient norm defect vanishes. By B6.1,

$$
z=Q_\pi y
$$

for some absolute cycle tensor $y$. Put $r=x+y$.

### Theorem 1.1 — root linearization as quotient-flow lifting

The zero-norm loop is root-admissibly conjugate to its pure support permutation if and only if there is a root-valued flow

$$
r:E(P)\to R_5
$$

with the prescribed terminal roots and

$$
\boxed{Q_\pi r=t_\gamma.}
$$

### Proof

If $y$ is a root-admissible conjugator, $r=x+y$ is root-valued and satisfies the equation. Conversely, if $r$ is such a lift, then $y=x+r$ is an absolute cycle tensor because $x,r$ have the same terminal data, and

$$
Q_\pi y=Q_\pi x+t_\gamma=z.
$$

$\square$

## 2. Full-rank types

For monodromy types $4\,1$ and $5$, the actual image of $Q_\pi$ on the switch plane is all of $W$, but zero has no root preimage.

### Proposition 2.1 — zero-edge criterion

For types $4\,1$ and $5$, a root lift exists if and only if

$$
t_\gamma(e)\ne0
$$

for every edge.

### Proof for type $5$

The map $Q_\pi$ is invertible on $E_5$. Every nonzero value of $W$ has one root preimage; the three preimages over $u,v,\kappa$ form one root triangle. Thus the unique edgewise lift automatically satisfies every cubic vertex equation and the prescribed terminal data.

### Proof for type $4\,1$

Let $k_0$ generate $\ker Q_\pi$. Choose a linear section $s:W\to E_5$ with $s(t)$ root-valued for $t\ne0$ and

$$
s(u)+s(v)+s(\kappa)=0.
$$

Every root over nonzero $t$ is $s(t)+bk_0$. At a cubic vertex, root conservation is exactly the binary equation

$$
b_1+b_2+b_3=0.
$$

The prescribed terminal bits have even total because both the original roots and the section values have zero terminal sum. On a connected four-pole, such boundary bits extend to a binary flow. $\square$

By the edge table,

$$
t_\gamma(e)=0
\quad\Longleftrightarrow\quad
 e\notin P_1\cup(P_0\triangle P_2).
$$

### Theorem 2.2 — full-rank XOR-cover criterion

For types $4\,1$ and $5$, the following are equivalent:

1. root-admissible linearization;
2. no zero edge;
3. the path chains cover every edge:
   $$
   \boxed{E(P)=P_1\cup(P_0\triangle P_2);}
   $$
4. the switch flow admits a Tait resolution.

Failure is witnessed by the nonempty uncovered set

$$
U_\lambda
=E(P)\setminus
\bigl(P_1\cup(P_0\triangle P_2)\bigr).
$$

## 3. Rank-one types

For monodromy types $2^2 1$ and $3\,2$, zero norm forces every switch-flow value into

$$
\{0,\kappa\}.
$$

Comparing the $u$ and $v$ coordinates in the genuine path formula gives:

### Theorem 3.1 — middle-path identity

$$
\boxed{P_1=P_0\triangle P_2.}
$$

Consequently

$$
\boxed{t_\gamma=\kappa\mathbf1_{P_1}.}
$$

### Proof

The only values $0,\kappa$ are those with equal $u$- and $v$-coordinates. Those coordinates are respectively $\mathbf1_{P_0\triangle P_2}$ and $\mathbf1_{P_1}$. $\square$

Thus the nonzero support is the single selected middle terminal path. Closed odd components admitted by a general rank-one quotient-flow model do not occur in a genuine three-path loop.

## 4. Spanning-path dichotomy

If $P_1$ omits an internal cubic vertex, all three incident switch-flow values are zero. The rank-one root fibres admit no root triangle over the all-zero local relation:

- for type $3\,2$, the zero fibre is one nonzero root;
- for type $2^2 1$, the zero fibre consists of two independent roots;
- no sum of three roots from either zero fibre is zero.

### Proposition 4.1

A nonspanning middle path gives an all-zero internal vertex and prevents root lifting.

Now suppose $P_1$ is spanning. Its complement is a matching of the internal cubic vertices, together with the two zero-valued terminal semiedges. The nonzero-support degree-two system has only the one terminal path $P_1$. A cubic four-pole has an even number of internal vertices because

$$
3|V_{\mathrm{int}}|=2|E_{\mathrm{int}}|+4.
$$

Hence the terminal path contains an even number of internal vertices. The exact alternating root assignment along an even component provides the root lift for both rank-one types.

### Theorem 4.2 — genuine rank-one dichotomy

For types $2^2 1$ and $3\,2$ with zero ambient norm, exactly one occurs:

1. $P_1$ is nonspanning, and the missed-vertex set
   $$
   X_\lambda=V_{\mathrm{int}}(P)\setminus V(P_1)
   $$
   is nonempty;
2. $P_1$ is spanning, a root lift exists, and the loop admits a Tait resolution.

## 5. Unified Tait criterion

### Theorem 5.1

A zero-norm genuine rainbow loop is root-admissibly linearizable if and only if its physical switch flow admits a Tait resolution.

For the full-rank types, the Tait flow is the nowhere-zero $W$-flow $t_\gamma$. For the rank-one types, colour the complement matching by $\kappa$ and alternate $u,v$ along the even middle path.

The old arbitrary-flow “odd closed component” obstruction is absent from the genuine three-path family. The exact zero-norm residual certificates are only:

- an uncovered edge in the full-rank branch;
- a missed internal vertex in the rank-one branch.

## 6. Tait-induced five-support cover

A Tait-coloured four-pole with terminal colours $a,a,b,b$ determines three bicoloured even supports

$$
F_{ab},\qquad F_{ac},\qquad F_{bc}
$$

and two empty supports. Its boundary state is some $B_i$.

The empty/full challenge and partition/partition challenge have the same symmetric difference:

$$
\varnothing\triangle F_{ab}
=
F_{ac}\triangle F_{bc}
=
F_{ab}.
$$

Therefore they realize the same terminal routing matching.

## 7. BBD profile escape

In either physical BBD triangle profile, the deterministic safe routing policy at every $B_i$ state requires different routes for the empty/full and partition/partition challenges.

### Theorem 7.1 — BBD Tait escape

A BBD triangle shore cannot contain a Tait cover inducing one of its $B_i$ states without strictly enlarging its complete boundary profile.

### Proof

The two genuine Kempe challenges in the Tait cover use the same relative even subgraph and hence the same actual route. The deterministic BBD policy requires two different safe routes. The common actual route can agree with at most one; applying the other genuine Kempe switch produces a state outside the triangle profile. $\square$

The exact identification of the two BBD triangle policies is finite certificate data. Once accepted, the escape argument is graph-theoretic.

## 8. DDD profile escape

### Theorem 8.1 — DDD Tait escape

A DDD triangle profile

$$
\{D_0,D_1,D_2\}
$$

cannot contain a Tait resolution of its lifted rainbow loop.

### Proof

The Tait colouring produces a five-support boundary cover in some state $B_i$. No $B_i$ belongs to the DDD profile. $\square$

## 9. Type H elimination of the soluble branch

### Theorem 9.1

For the triangle shore of a minimal Type H routing kernel,

$$
\boxed{
\text{zero norm}
+
\text{root-admissible linearization}
\Longrightarrow
\text{strict boundary-profile escape}.}
$$

Thus the root-linearizable zero-norm branch is eliminated.

The residual Type H alternatives are:

1. nonzero interior norm defect;
2. zero norm with a nonempty uncovered-edge set in the full-rank branch;
3. zero norm with a nonempty missed-vertex set in the rank-one branch.

## 10. Physical-family obstruction signature

For each physical lifted loop $\lambda$, record

$$
\mathfrak S(\lambda)
=
\begin{cases}
(\mathrm A,d_\lambda),&d_\lambda\ne0,\\
(\mathrm F,U_\lambda),&d_\lambda=0\text{ and full rank},\\
(\mathrm R,X_\lambda),&d_\lambda=0\text{ and rank one}.
\end{cases}
$$

In a minimal Type H kernel, every physical lift has one nontrivial signature. Conversely a lift with zero norm and empty corresponding $U_\lambda$ or $X_\lambda$ gives Tait escape.

This is the complete current family-level obstruction object.

## 11. Certificate and frontier boundary

The genuine path identity and the lift/Tait dichotomies are theorem-level. The exact list of physical BBD/DDD triangle shores, sixteen/four lifted monodromies, and deterministic routing policies are finite certificate inputs.

The remaining open statement is a common-witness theorem: if every physical lift has a nonzero signature, prove that their norm cycles, uncovered edges, or missed vertices share a bounded connected region, cut, odd ring, or replaceable fragment.

The conditional $27$-state cube obtained by independently trivializing three path-choice torsors is not presently a theorem.

## 12. Completion assessment

`AC-PD-B6.2` is `COMPLETE-DRAFT / RESIDUAL-CERTIFICATES-LOCALIZED`. The next unit audits the BBD/DDD global synthesis and canonical-defect packets, retaining only those implications whose hypotheses do not assume the missing common-witness theorem.