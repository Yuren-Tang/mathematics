# AC-PD-B5.3 — routing weights, fixed-route sectors, and uniform-routing elimination

**Proof-development state:** `COMPLETE-DRAFT / CERTIFICATE-BOUNDARY`  
**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Exact initial corpus base:** `main@960c92b7ff231c78b387894149779083060a75eb`  
**Validated source:** `FIVE_CDC_ROUTING_WEIGHT_AND_HOLONOMY_DICHOTOMY_V1.md`  
**Depends on:** B5.1 ten-state alphabet; B5.2 pairing alignment and cap forcing  
**Immediate consumers:** B5 consolidation; B6 Type T/Type H analysis  
**External mathematical inputs:** none

## 0. Terminal matching coordinates

Let the labelled terminals be $1,2,3,4$. For each perfect matching

$$
M_i=X_i\mid Y_i,
\qquad i=0,1,2,
$$

and each even boundary trace $S$, define

$$
q_i(S)=|S\cap X_i|\pmod2.
$$

For a five-trace signature $\sigma=(S_1,\ldots,S_5)$, define

$$
\omega_i(\sigma)
=\frac12\sum_{r=1}^5q_i(S_r).
$$

The sum is even because every terminal occurs exactly twice, so $\omega_i\in\{0,1,2\}$. The value is invariant under support permutation.

## 1. Coordinate table

### Theorem 1.1

The map

$$
\Omega:\mathcal S\to\{0,1,2\}^3,
\qquad
S\mapsto(\omega_0,\omega_1,\omega_2)
$$

is injective, with

$$
\begin{array}{c|c}
A&(0,0,0)\\
B_0&(0,1,1)\\
B_1&(1,0,1)\\
B_2&(1,1,0)\\
C_0&(0,2,2)\\
C_1&(2,0,2)\\
C_2&(2,2,0)\\
D_0&(2,1,1)\\
D_1&(1,2,1)\\
D_2&(1,1,2).
\end{array}
$$

### Proof

Insert the canonical traces of B5.1. The ten resulting triples are distinct. $\square$

## 2. Conserved coordinate of a routed switch

Suppose a complementary support pair has terminal paths realizing $M_i$, and switch the pair along one path with terminal block $X_i$.

### Theorem 2.1

The switch preserves $\omega_i$.

### Proof

Only two support traces are toggled by $X_i$. Since $|X_i|=2$, toggling by $X_i$ leaves the parity $|S\cap X_i|$ unchanged for each of them. $\square$

For $j\ne i$, each block of $M_i$ meets $X_j$ in one terminal, so the two relevant $q_j$ bits flip. Thus the routing matching is exactly the choice of one conserved coordinate.

## 3. Fixed-routing transition graph

Let $\mathcal G_i$ contain every abstract state transition obtained by a complementary-pair switch routed by $M_i$. If $\{i,j,k\}=\{0,1,2\}$, direct trace update gives:

$$
A-B_i-C_i,
$$

$$
B_j-B_k-D_j-D_k-B_j,
$$

and

$$
C_j-D_i-C_k.
$$

### Theorem 3.1

These are exactly the connected components of $\mathcal G_i$. Hence

$$
\boxed{
\mathcal G_i\cong P_3\sqcup C_4\sqcup P_3.}
$$

The three components are the level sets $\omega_i=0,1,2$, and the middle component is exactly

$$
\mathcal K_i=\{B_j,B_k,D_j,D_k\}.
$$

### Proof

Theorem 2.1 confines every edge to one level set. Applying the exact trace toggle from B5.2 lists the displayed edges; each level set is connected and no other state lies at that level. $\square$

## 4. Two routing colours destroy global state invariants

### Proposition 4.1

For $i\ne j$, the graph

$$
\mathcal G_i\cup\mathcal G_j
$$

is connected on all ten states; its diameter is four.

### Proof

Insert the three displayed component lists for $\mathcal G_i$ and $\mathcal G_j$. Their overlaps connect the three $\omega_i$ sectors, and direct breadth-by-layers inspection gives maximum distance four. This is a finite verification on the explicit ten-state graph, independent of any four-pole realizability computation. $\square$

Thus any subset closed under every transition of two fixed routing colours is either empty or all of $\mathcal S$. A residual obstruction must correlate route choice with the current indexed cover and support-pair challenge.

## 5. Uniform routing

Call a four-pole globally $i$-routed when, in every indexed boundary cover, every complementary support-pair difference realizes matching $M_i$.

### Theorem 5.1

If $P$ is globally $i$-routed, then $\Sigma(P)$ is a union of connected components of $\mathcal G_i$.

### Proof

For every realized cover and complementary pair, the routed path switch is an actual boundary-cover Kempe move. Global $i$-routing makes every abstract $M_i$ transition available. Iteration closes the profile under each connected component. $\square$

### Theorem 5.2 — uniform-routing elimination

If $P$ is a shore of a cyclic four-edge cut in a vertex-minimal counterexample and is globally $i$-routed, then

$$
\boxed{\mathcal K_i\subseteq\Sigma(P).}
$$

Consequently neither shore of such a cut is globally routed by one matching.

### Proof

The two path components of $\mathcal G_i$ contain B/D states only of matching index $i$; the middle component is $\mathcal K_i$ and contains the other two indices. Cap forcing requires at least two B/D matching indices. Therefore a component-union profile must contain the entire middle component.

For the opposite shore $Q$, cap forcing supplies a B/D state of some index different from $i$, hence a member of $\mathcal K_i$. This creates a common signature and contradicts the four-cut gluing obstruction. $\square$

Uniform linkage is therefore reducible; it is not a residual obstruction mechanism.

## 6. Kempe closure as a game

For a state and one orbit of complementary support-pair challenges, the internal path geometry selects one of three routing matchings, and the selected matching determines one target state. A Kempe-closed profile is a state set for which routing has a memoryless safe choice after every challenge.

This abstract safety game overapproximates a real four-pole: its route choices must arise coherently from one family of internal paths across all indexed covers.

## 7. Finite certificate layer

The following statements are exact finite classifications from the recovered packet, but are not rederived by the theorem proofs above:

1. after cap forcing and Kempe closure, four minimal disjoint profile-pair kernels remain;
2. every state/challenge in those kernels has one safe routing colour;
3. the policy pairs fall into two symmetry types:
   $$
   P_5\mid P_5
   \quad\text{and}\quad
   P_4\mid C_3;
   $$
4. the $C_3$ is rainbow-routed;
5. the sixteen lifted boundary monodromies have the stated cycle-type distribution and generate $S_5$.

These results require their exact transition tables or verifier for independent assurance. They are inputs to B6, not consequences of routing-weight conservation alone.

## 8. Genuine remaining mechanisms

After uniform routing is eliminated, the abstract residual policies have two forms.

- **Type T:** acyclic unique routing, expected to force nested linkage, serial composition, or a smaller separator.
- **Type H:** a rainbow routing loop, whose boundary support-name monodromy must be lifted to an interior affine/flow object before it can obstruct gluing.

Neither mechanism is eliminated by B5.1–B5.3.

## 9. Assurance boundary

The coordinate table, conserved-coordinate theorem, fixed-route sectors, two-colour connectivity, and uniform-routing elimination are theorem-level. Kernel counts, deterministic policies, Type T/H orbit classification, and monodromy census remain exact finite certificate data.

## 10. Completion assessment

`AC-PD-B5.3` is `COMPLETE-DRAFT / CERTIFICATE-BOUNDARY`. B5 can now be consolidated: mature separator and routing theorems are closed, while the alignment/decomposition and Type T/H elimination obligations pass explicitly to B6.