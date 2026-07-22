# Exact census of the six-vertex equality annulus and its complete root profile

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `afda5f8d2331049204df14d5addb7ae501ecc5c2`.

**Parents:**

- `EQUALITY_LOCK_IDENTITY_HEXAGON_CORE_V1.md`;
- `EQUALITY_LOCK_TWO_BOUNDARY_ANNULUS_REDUCTION_V1.md`;
- `EQUALITY_LOCK_PRIVATE_MATCHING_TAIT_DECOMPOSITION_V1.md`;
- the ten-state four-terminal orbit classification.

**Status:** exact finite certificate for the minimal flat equality core. Among all labelled six-vertex properly three-edge-coloured connected four-poles with four boundary semiedges of one colour and equal open responses in the other two bicoloured systems, there are `360` labelled cores and exactly one colour-preserving isomorphism type. It is the identity hexagon. Forgetting the auxiliary Tait colouring, this graph has `5700` root-valued `E_5` flows and realises all `640` conserved ordered root quadruples. The exact cap-compatibility census recovers the ten-state multiplicities and shows that the only ordered boundaries with no root-valued two-vertex cap pairing are the equality state `A` and the three direct-pairing DDD states `C_i`.

**Not implied:** that every larger equality carrier transfers every identity-hexagon boundary state, cover-independent inverse transfer through a surgery history, elimination of complete-profile reconfiguration-component gaps, global proof-DAG closure, canonical acceptance, Lean verification, manuscript integration, release, publication, or the global five-support theorem.

---

## 1. Six-vertex coloured-core model

Let the six internal vertices be labelled

\[
0,1,2,3,4,5.
\]

A properly three-edge-coloured cubic four-pole with colours

\[
r,s,t
\]

and four `r`-boundary semiedges is specified by:

1. one internal `r`-edge; its two endpoints are the two vertices without `r`-boundary semiedges;
2. one perfect matching of the six vertices in colour `s`;
3. one perfect matching in colour `t`.

Require:

- the internal graph to be connected;
- the open `rs` path system to pair the four boundary ports by one matching `M`;
- the open `rt` path system to give the same matching `M`.

This is exactly the six-vertex double-equal Tait response

\[
(r^4;M,M,\varnothing).
\]

---

## 2. Labelled and isomorphism census

Complete enumeration of:

- the `15` choices of internal `r`-edge;
- the `15` perfect matchings for `s`;
- the `15` perfect matchings for `t`;

followed by connectedness and equal-response filtering gives

\[
\boxed{360}
\]

labelled coloured cores.

Canonicalisation under all

\[
6!=720
\]

vertex permutations gives:

### Theorem 2.1 — unique six-vertex coloured core

\[
\boxed{
360\text{ labelled cores}
\quad/\quad S_6
\quad=\quad
1\text{ colour-preserving isomorphism type}.}
\]

A canonical representative has:

\[
B=\{0,1,2,3\},
\]

\[
r=45,
\]

\[
s=01\mid24\mid35,
\]

\[
t=04\mid15\mid23.
\]

The two open responses both pair

\[
01\mid23.
\]

The union of the `s` and `t` matchings is one alternating six-cycle. This is the canonical identity hexagon.

### Structural proof

The annulus theorem already proves uniqueness without enumeration: a flat connected equality surface has two boundary components, and equality in the bound

\[
|V|\ge b+2=6
\]

forces two boundary corollas joined by one transverse two-vertex bridge. The finite census is an independent labelled certificate.

---

## 3. Full root-flow enumeration

Now forget the auxiliary Tait colouring. At each cubic vertex choose:

1. one support triangle
   \[
   T\in\binom{[5]}3;
   \]
2. one of the six bijections from the three root edges of `T` to the three incident source slots.

Thus there are

\[
10\cdot6=60
\]

possible assigned local root-triangle states per vertex.

Impose equality of the root label at the two ends of every internal edge and record the four ordered boundary roots.

### Theorem 3.1 — complete identity-hexagon profile

Exact backtracking gives

\[
\boxed{5700}
\]

root-valued flows on the labelled identity hexagon and

\[
\boxed{640}
\]

distinct ordered boundary quadruples.

The number of conserved ordered root quadruples is itself

\[
\boxed{640}.
\]

Hence:

\[
\boxed{
\text{every conserved ordered root quadruple extends across the identity hexagon}.}
\]

This independently verifies the universal ordered-root completion theorem for the six-vertex annulus.

---

## 4. Ten-state route-sum census

For one conserved ordered root quadruple

\[
(a_1,a_2,a_3,a_4),
\]

compute the common central sum for each of the three terminal pairings. Its weight belongs to

\[
\{0,2,4\}.
\]

The `640` ordered boundaries split exactly as follows.

### Equality state

\[
(0,0,0):\qquad 10.
\]

These are the ten quadruples

\[
(a,a,a,a).
\]

### Adjacent direct-pairing states

For each matching index `i`, the route-sum pattern is a permutation of

\[
(0,2,2).
\]

The multiplicity is

\[
\boxed{60\text{ for each }B_i.}
\]

### Disjoint direct-pairing states

For each matching index `i`, the route-sum pattern is a permutation of

\[
(0,4,4).
\]

The multiplicity is

\[
\boxed{30\text{ for each }C_i.}
\]

### Four-distinct / one-co-root states

For each matching index `i`, the route-sum pattern is a permutation of

\[
(2,2,4).
\]

The multiplicity is

\[
\boxed{120\text{ for each }D_i.}
\]

Thus

\[
10+3\cdot60+3\cdot30+3\cdot120=640.
\]

The finite census exactly recovers the complete ten-state orbit decomposition.

---

## 5. Cap-compatibility census

A two-vertex cap for one terminal pairing is root-valued exactly when the two roots entering each cap vertex are distinct and intersecting. Equivalently, the central pairing sum has weight two.

For each ordered conserved boundary, record the three cap-compatibility bits.

Exact enumeration gives:

\[
\boxed{
\begin{array}{c|c}
\text{compatibility mask}&\text{number of boundaries}\\
\hline
011&180\\
101&180\\
110&180\\
000&100.
\end{array}}
\]

No boundary is compatible with exactly one or all three cap pairings.

### Theorem 5.1 — singular cap boundaries

The `100` boundaries with mask `000` are exactly:

\[
\boxed{
A
\sqcup
C_0
\sqcup
C_1
\sqcup
C_2.}
\]

Indeed:

- `A` contributes `10` quadruple-equality words;
- each `C_i` contributes `30` doubled-disjoint words;
- total:
  \[
  10+3\cdot30=100.
  \]

Every `B_i` or `D_i` ordered boundary is root-compatible with exactly two of the three two-vertex cap topologies.

### Consequence 5.2

When a cap-compatible identity-hexagon state is reversed through a root-surgery history, the first failure can enter no new bounded boundary type. The only cap-singular terminal fibres are precisely the already isolated equality and DDD direct-pairing fibres.

---

## 6. Independent Wolfram certificate

An independent exact Wolfram Language evaluation returned:

\[
\boxed{
\begin{aligned}
&\texttt{labelledEqualResponseCores}=360,\\
&\texttt{coloredIsomorphismTypes}=1,\\
&\texttt{conservedOrderedBoundaries}=640,\\
&\texttt{boundariesExtended}=640,\\
&\texttt{totalRootExtensions}=5700.
\end{aligned}}
\]

The cap masks were:

\[
000:100,
\qquad
011:180,
\qquad
101:180,
\qquad
110:180.
\]

The human annulus and route-sum arguments are controlling; the computations are reproducible finite certificates.

---

## 7. Trust boundary

### Exact here

- complete labelled six-vertex coloured-core enumeration;
- one colour-preserving isomorphism type;
- identity-hexagon representative;
- `5700` root-flow count;
- all `640` conserved ordered boundaries;
- complete ten-state ordered multiplicities;
- complete cap-compatibility mask census;
- identification of the `100` singular words with `A` and the three `C_i` fibres.

### Still open

- profile transfer from a larger carrier to the identity hexagon and back;
- reconfiguration-component comparison among all root flows of a fixed graph;
- outer-route preservation across nested equality/DDD returns;
- complete local transfer synthesis;
- global proof-DAG assembly;
- canonical acceptance, independent audit, Lean verification, manuscript integration, release, publication, and the global five-support theorem.
