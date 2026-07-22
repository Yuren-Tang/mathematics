# The Type-T kernel as a square-envelope exclusion

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `eb5747a53ecb34eed213f42410c4cfb63c0031f6`  
**Parents:**

- `projects/affine-cdc/research/FOUR_POLE_CAP_LIBRARY_TEN_STATE_PROFILES_V1.md`;
- `projects/affine-cdc/research/FOUR_ROOT_INTERFACE_TYPE_T_SQUARE_V1.md`;
- `projects/affine-cdc/research/PETERSEN_BACKTRACK_TYPE_T_REDUCTION_V1.md`;
- `projects/affine-cdc/five-support/cuts-four-poles-and-routing.md`;
- retired exact sources `FIVE_CDC_FOUR_POLE_KEMPE_CLOSURE_V1.md` and `FIVE_CDC_ROUTING_WEIGHT_AND_HOLONOMY_DICHOTOMY_V1.md` at `dad218dd18ed05d1b7cb730c2dc2431b4db5ec9c`.

**Status:** exact finite synthesis of the Type-T ten-state kernel with the square profiles. The two Type-T shores partition the complete ten-state alphabet. Every state/challenge has one safe route; every other route lands on the opposite shore and therefore gives immediate signature intersection. Each shore is contained in a unique relevant square profile, and the square adds exactly four opposite-shore states while omitting one opposite `B` state. Thus Type T is precisely the physical exclusion of a square envelope, not a missing finite boundary state.  
**Not implied:** that every physical unique-linkage shore realises its square envelope, source-graph contraction without enclosure, universal state-set inclusion, canonical acceptance, Lean verification, manuscript readiness, or the global five-support theorem.

---

## 1. Canonical Type-T profile pair

After a simultaneous permutation of the three matching indices and exchange of shores, the Type-T kernel is represented by

\[
P=\{A,B_0,C_1,D_0,D_1\},
\]

\[
Q=\{B_1,B_2,C_0,C_2,D_2\}.
\]

These sets are disjoint and satisfy

\[
\boxed{P\sqcup Q=\mathcal S.}
\]

They are the first of the four exact Kempe-stable mismatch-kernel orbits.

---

## 2. Unique deterministic policies

The exact ten-state transition table gives the unique safe route at every state and challenge.

### Shore `P`

The undirected state graph is

\[
\boxed{
A\xleftrightarrow{0}B_0
\xleftrightarrow{2}D_1
\xleftrightarrow{2}D_0
\xleftrightarrow{0}C_1.}
\]

Its routing-colour word is

\[
\boxed{0,2,2,0.}
\]

### Shore `Q`

The undirected state graph is

\[
\boxed{
C_0\xleftrightarrow{2}D_2
\xleftrightarrow{0}B_1
\xleftrightarrow{0}B_2
\xleftrightarrow{2}C_2.}
\]

Its routing-colour word is

\[
\boxed{2,0,0,2.}
\]

Both are `P5` paths with the Type-T `abba` word.

### Exact directed rows

For `P`, the unique safe transitions are:

\[
A\xrightarrow{0}B_0,
\]

\[
B_0\xrightarrow{0}A,
\qquad
B_0\xrightarrow{2}D_1,
\]

\[
D_1\xrightarrow{2}B_0,
\qquad
D_1\xrightarrow{2}D_0,
\]

\[
D_0\xrightarrow{2}D_1,
\qquad
D_0\xrightarrow{0}C_1,
\]

\[
C_1\xrightarrow{0}D_0,
\]

where the two outgoing rows at `B_0,D_1,D_0` correspond to their two complementary-trace challenge types.

The `Q` rows are obtained by the displayed second path and the same exact transition table.

---

## 3. Every non-policy route glues

### Theorem 3.1 — total opposite-shore escape

At every Type-T state/challenge, the two routing matchings other than the unique policy route produce states in the opposite profile.

### Proof

The exact routing computation gives one in-profile target for each row. The Type-T profiles partition all ten states. Since the other targets are not in the current minimal profile and every abstract transition target belongs to `\mathcal S`, they lie in the opposite shore. Direct inspection of the ten-state table verifies the statement row by row. ∎

### Corollary 3.2

In a physical cyclic four-cut realising the Type-T mismatch pair, every relevant four-endpoint support-pair system is forced to use the displayed unique terminal matching.

Any alternate matching yields

\[
\Sigma(P)\cap\Sigma(Q)\ne\varnothing
\]

and the four-cut glues.

Thus Type T is a genuine unique-linkage mechanism, not merely a five-state subset of the boundary alphabet.

---

## 4. Square envelopes

Let `\square_i` be the cyclic square whose diagonal matching is `M_i`. The cap-library theorem gives

\[
\Sigma(\square_i)=\mathcal S\setminus\{B_i\}.
\]

### Theorem 4.1 — first shore envelope

\[
\boxed{
\Sigma(\square_2)
=
P\sqcup(Q\setminus\{B_2\}).}
\]

### Proof

`P` contains no `B_2`. Its complement is `Q`, and deleting `B_2` from the complete state alphabet gives exactly the displayed union. ∎

### Theorem 4.2 — second shore envelope

\[
\boxed{
\Sigma(\square_0)
=
Q\sqcup(P\setminus\{B_0\}).}
\]

The proof is identical.

### Interpretation

The relevant square does not merely contain the marked central `abba` state. It contains the entire Type-T shore profile and exactly four states of the opposite shore.

Hence any physical enlargement

\[
P\subsetneq\Sigma_{\mathrm{phys}}
\subseteq\Sigma(\square_2)
\]

or

\[
Q\subsetneq\Sigma_{\mathrm{phys}}
\subseteq\Sigma(\square_0)
\]

which realises even one square-added state destroys the mismatch by signature intersection.

---

## 5. The four forbidden square states

For shore `P`, the square-added states are

\[
\boxed{B_1,C_0,C_2,D_2.}
\]

The sole opposite-shore state not realised by `\square_2` is

\[
B_2.
\]

For shore `Q`, the square-added states are

\[
\boxed{A,C_1,D_0,D_1,}
\]

and the sole omitted opposite state is

\[
B_0.
\]

Therefore the physical Type-T theorem no longer needs to generate an arbitrary common state. It suffices to generate **one of four explicit square-envelope states** on either shore.

---

## 6. Relation to the Petersen `abba` backtrack

The central repeated routing colour in each path is the two-step backtrack colour:

\[
B_0-D_1-D_0
\]

for `P`, and

\[
D_2-B_1-B_2
\]

for `Q`.

The Petersen pivot theorem identifies the corresponding root-resolution boundary word as

\[
a,b,b,a,
\qquad a\cap b=\varnothing.
\]

The four-root interface theorem identifies this as the unique `(0,4,4)` route-sum orbit and supplies its minimal square root completion.

Thus the finite boundary and physical pivot descriptions agree:

\[
\boxed{
\text{Type-T policy backtrack}
\longleftrightarrow
\text{disjoint-root `abba`}
\longleftrightarrow
\text{square envelope}.}
\]

---

## 7. Revised graph-theoretic target

To eliminate Type T it is enough to prove the following source theorem.

### Target 7.1 — square-envelope or separator

For a four-pole shore carrying the Type-T deterministic policy, one of:

1. a non-policy linkage occurs and realises one of the four square-added opposite states;
2. the unique-linkage systems are nonlaminar and produce a crossed route, again giving an opposite state;
3. all relevant systems are laminar and a minimal interval encloses the `abba` unit as a four-port region;
4. that region is horizontally response-equivalent to the canonical square;
5. failure of enclosure or replacement yields a two-, three-, or four-cut or a bounded zero/DDD cell.

The finite state problem is finished. The remaining content is unique-linkage localisation and composition.

---

## 8. Trust boundary

### Exact here

- the canonical Type-T shore profiles;
- their partition of all ten states;
- their exact `P5` automata and `abba` edge-colour words;
- unique policy at every state/challenge;
- every non-policy target lies on the opposite shore;
- square-envelope identities;
- the explicit four square-added escape states on each shore;
- agreement of the policy backtrack, disjoint-root `abba`, and square normal form.

### Still open

- source proof that a physical Type-T shore realises one square-added state or yields a separator;
- enclosure of the central `abba` unit with all external side attachments;
- horizontal replacement of the enclosed interval by the square in the controlling category;
- universal state-set inclusion if graph induction rather than horizontal descent is used;
- global well-founded descent and the five-support theorem.
