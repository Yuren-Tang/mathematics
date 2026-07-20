# AC-PD-B6 — holonomy, root-fibre defects, and atom map

**Proof-development state:** `READY-FOR-CURATOR / MATHEMATICAL-CORRECTION / AC-RL-GAPS-EXPLICIT`  
**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Exact initial corpus base:** `main@960c92b7ff231c78b387894149779083060a75eb`  
**Constituent units:** B6.1–B6.4  
**External mathematical inputs:** none  
**Assurance:** complete authorial proof-development checkpoint for the retained theorem layer and corrections; two exact BBD gaps returned to AC-RL

## 0. Correct hierarchy

The Type H interior programme has four levels.

1. One lifted loop gives an ambient affine holonomy $(\pi,z)$.
2. Zero ambient norm reduces root linearisation to a finite root-fibre section problem.
3. The genuine three-path word collapses this section problem to Tait resolution versus missed-vertex/uncovered-edge certificates.
4. Local DDD atoms admit a three-resolution triality and a unique-bad-route theorem.

A separate proposed BBD synthesis attempted to combine all loops into one global affine group and one canonical defect flow. That step requires an unproved physical composability theorem and is now conditional.

## 1. Individual ambient holonomy

For one physical lifted loop,

$$
z=x^\gamma+\pi x\in Z_1(P)\otimes E_5.
$$

Under repeatability, iteration is governed by

$$
d=N_\pi z.
$$

For all four rainbow monodromy types,

$$
H^1(\langle\pi\rangle,E_5)=0.
$$

Hence:

- $d\ne0$ gives period doubling and a nontrivial pure ambient translation;
- $d=0$ gives ambient translation-conjugacy to the pure permutation.

This is one-loop ambient classification, not root-valued conjugacy.

## 2. Edgewise root admissibility

For $Q_\pi=1+\pi$ and current root $x$,

$$
\mathcal A_\pi(x)
=Q_\pi x+Q_\pi(R_5).
$$

The local forbidden-set sizes are:

$$
\begin{array}{c|c}
2^2 1&0\\
4 1&1\\
3 2&1\\
5&6.
\end{array}
$$

These edgewise tables do not solve the global cycle-consistent section problem.

## 3. Genuine three-path reduction

A physical rainbow loop has

$$
t_\gamma
=(P_0\triangle P_2)\otimes u+P_1\otimes v.
$$

### Full-rank types $4\,1$ and $5$

Root linearisation exists exactly when

$$
E(P)=P_1\cup(P_0\triangle P_2).
$$

Failure is one uncovered edge.

### Rank-one types $2^2 1$ and $3\,2$

Zero norm forces

$$
P_1=P_0\triangle P_2,
\qquad
t_\gamma=\kappa\mathbf1_{P_1}.
$$

The old odd-closed-component branch disappears. A root lift exists exactly when $P_1$ is spanning; failure is one missed internal vertex.

## 4. Tait escape

A zero-norm genuine loop is root-admissibly linearizable exactly when its switch flow admits a Tait resolution.

In a minimal Type H kernel:

- a BBD Tait cover makes two nominal challenges share one actual relative subgraph, contradicting the distinct safe routes required by the deterministic triangle policy;
- a DDD Tait cover creates a $B_i$ boundary state outside the DDD profile.

Therefore

$$
\boxed{
\text{zero norm}+
\text{root linearisation}
\Longrightarrow
\text{strict profile escape}.}
$$

Every physical lift remaining in a minimal Type H kernel has one nontrivial signature:

$$
(d_\lambda,U_\lambda,X_\lambda).
$$

The missing family theorem is to find one common bounded geometric witness when every lift is obstructed.

## 5. BBD global-holonomy correction

Individual ambient transformations generated algebraically need not compose as physical root-preserving reconfiguration paths. A fixed path switch is valid only when its edge set remains the relevant support-pair component at the current state.

Therefore the claims

- physical translation kernel $T=0$;
- one global $S_5$ cocycle;
- one simultaneous common origin;
- one canonical BBD shifted flow

are conditional on a missing physical isotropy-groupoid closure theorem.

The abstract module theorem

$$
H^1(S_5,E_5)=0
$$

and the root-rigidity proof are valid once that group action exists.

## 6. Defect-forest correction

The stated variational domain is all $E_5$-flows with the original terminal roots. It already contains the original root-valued cover, so

$$
\min\delta=0.
$$

The resulting nontrivial residual forest does not follow. Restricting to the claimed unique common origin removes the cycle-toggle variation used in the proof.

Thus the canonical defect-minimal forest is not an active theorem. A new holonomy-compatible variation space or a different reduction is required.

The $K_6$ coefficient model, zero/co-root local grammar, and Petersen endpoint transport remain valid conditional local tools when a suitable defect flow or strip is supplied independently.

## 7. DDD atom triality

A nondegenerate two-vertex co-root atom is canonically one DDD $K_6$ one-factor. Its three terminal pairings force:

- the original co-root internal label;
- two crossed root internal labels.

The fifteen atoms are $S_5$-equivariantly the fifteen $K_6$ one-factors, with stabilizer $D_8$.

For every bad ordered atom state and full challenge, the original pairing is the unique route that remains bad; either a crossed physical route occurs and gives a local root resolution, or all challenges are universally route-locked.

## 8. Locked quotient

Exact finite root-image classification sends a universally locked $C$-state to a nowhere-zero

$$
c:E(Q)\to\mathbf F_2^3\setminus\{0\}
$$

with all four terminal values equal and four scalar sheets all routing the same terminal pairing.

Route-lock does not imply a graph two-edge cut. The residual quotient divides into rank-drop and full-rank curvature sectors passed to B7.

## 9. Exact AC-RL returns

### `AC-RL-BBD-GROUPOID-CLOSURE`

Construct or refute a root-preserving physical BBD isotropy groupoid supporting the claimed semidirect-product composition and full $S_5$ projection.

### `AC-RL-BBD-VARIATION-SLICE`

Construct a nontrivial holonomy-compatible variation space supporting defect-minimizing cycle toggles, or replace the forest route.

These were returned in research-workbench issue #8 comment `5019401145`.

## 10. B7 inputs

B7 receives:

1. Type T acyclic unique-routing policy;
2. individual Type H signatures $(d,U,X)$;
3. the DDD atom route-lock quotient;
4. rank-two Tait escape packets;
5. full-rank curvature and common-cut dual certificates;
6. the requirement that every local algebraic resolution transfer through the original four-pole incidence and decrease a strict measure.

It does not receive the unconditional BBD common flow or defect forest.

## 11. Completion assessment

`AC-PD-B6` is `READY-FOR-CURATOR / MATHEMATICAL-CORRECTION / AC-RL-GAPS-EXPLICIT`. B7 becomes active independently of the returned BBD questions.