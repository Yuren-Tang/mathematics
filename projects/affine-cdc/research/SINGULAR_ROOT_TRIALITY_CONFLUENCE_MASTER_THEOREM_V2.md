# Singular root-triality confluence — orientation-hardened master theorem

## Research Lead master theorem v2

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `281072af7add96b67f36c831ff9ec9e82ef8623e`.

**Supersedes for controlling use:** `SINGULAR_ROOT_TRIALITY_CONFLUENCE_MASTER_THEOREM_V1.md`.

**Correction:** v1 stated odd-core exclusion as failure of an odd token cycle to return the oriented resolution sheet. The controlling hypothesis is stronger: no odd pivot-closed physical subtrack is admissible. This rules out double traversal of an odd Petersen cycle before it can form a full-state recurrence.

**Status:** exact abstract confluence theorem conditional on the concrete full-labelled hypotheses. It adds no independent assurance to those hypotheses.

---

## 1. Contexts and orders

A root context records:

1. the ordered source multipole;
2. complete exterior incidences and root word;
3. the distinguished cap matching and one distinguished cap block;
4. all physical route data required by inverse transfer.

A finite forward surgery history is

\[
C_0\to C_1\to\cdots\to C_m.
\]

Use lexicographic induction on

\[
\boxed{(N(C_0),m),}
\]

where `N` is closed cap-context vertex order.

A successful inverse root move lowers `m`. A genuine equal-face cancellation lowers `N` by two.

---

## 2. First-failure token

### Hypothesis F

The first failed inverse move produces exactly one non-root central edge, labelled

\[
0
\quad\text{or}\quad
Q_i,
\]

while preserving every exterior root, incidence, cap index, and distinguished cap block.

No defect cloud is created.

---

## 3. Same-order token grammar

### Hypothesis L

Every same-order token transition is one of:

1. immediate zero-to-root triality resolution;
2. nonbranching co-root relocation through a labelled critical overlap;
3. full-state constant-pivot resolution;
4. production of a cap-compatible route/theta terminal;
5. production of a strict equal-face cancellation.

Every persistent token is therefore one co-root atom with two crossed root resolutions.

---

## 4. Finite full-state graph

### Hypothesis S

At fixed target order and history prefix, the complete labelled token state graph is finite.

A state retains:

- source topology and token position;
- ordered exterior incidences;
- all critical-neighbourhood roots;
- support transport;
- distinguished cap block;
- current route orientation;
- history position.

Coefficient-only or collapsed-pivot quotients are not the state graph.

---

## 5. Forced-backbone reduction

### Hypothesis P

In a terminal-free same-order recurrent component:

1. zero cannot persist;
2. co-root critical overlaps form one nonbranching Petersen pivot walk;
3. constant-pivot runs are resolved without deleting their support transport or side attachments;
4. immediate inverse backtracks may be removed;
5. every repeated pivot contains a shortest positive-length pivot-closed subtrack whose reduced projection is one simple Petersen cycle.

The possible simple lengths are

\[
5,6,8,9.
\]

---

## 6. Orientation-hardened odd exclusion

### Hypothesis O+

The original cap distinguishes one block of the fixed route. Every physical pivot-closed transport segment lies in the stabiliser of that distinguished block.

The crossed-resolution orientation character equals pivot-length parity. Hence every pivot-closed physical segment has even length:

\[
\boxed{
s_m=s_0
\Longrightarrow
m\equiv0\pmod2.
}
\]

This hypothesis is supplied concretely by `ORIENTED_ODD_PETERSEN_SUBTRACK_EXCLUSION_V1.md`.

### Consequence

The shortest repeated-pivot subtrack of Hypothesis P cannot be `C5` or `C9`. It must be `C6` or `C8`.

An abstract double traversal of an odd cycle is irrelevant: its first lap is already an odd pivot-closed segment and is not an admissible physical path.

---

## 7. Even-core strict exit

### Hypothesis E

1. Every primitive `C6`, with full rooted side attachments retained, is at most one root-valued `(0,2,2)` NNI from a canonical star.
2. The canonical star contains an equal-face dipole.
3. Cancelling it lowers target order by two.
4. Every `C8` decomposes into two seam-compatible `C6` source cells and has the same strict exit.

No abstract longitudinal tube assignment is substituted for a source movie.

---

## 8. No-sink theorem

### Theorem 8.1

Under Hypotheses L, S, P, O+, and E, the fixed-order token state graph has no reachable sink strongly connected component without an exit to:

1. rootification;
2. a cap-compatible root terminal;
3. strict cancellation.

### Proof

Assume such a sink SCC exists. It contains a persistent co-root token. Hypothesis P supplies a shortest repeated-pivot simple Petersen subtrack.

Hypothesis O+ makes its length even, so it is `C6` or `C8`. Hypothesis E supplies a strict cancellation exit, contradicting sinkness. ∎

The proof no longer reasons from failure of a full-state odd cycle to closure; it excludes the odd pivot-closed subtrack itself.

---

## 9. Cover-independent contextual transfer

### Theorem 9.1

Assume for every target order at most `N`:

1. finite forward singular-carrier reduction;
2. Hypotheses F, L, S, P, O+, and E;
3. conversion of route and direct-pairing outcomes to cap-compatible terminals;
4. componentwise induction after every genuine cancellation.

Then every cap-compatible terminal root state on `C_m` transfers to a cap-compatible root state on `C_0`.

### Proof

Induct lexicographically on `(N(C_0),m)`.

- If the last inverse step succeeds root-valuedly, reverse it and lower `m`.
- If it first fails, Hypothesis F gives one token.
- Theorem 8.1 gives a path to rootification, a cap-compatible strict-prefix terminal, or cancellation.
- Rootification and a strict-prefix terminal lower `m`.
- Cancellation lowers `N`.

Every branch lowers the induction pair. ∎

---

## 10. Concrete hypothesis map

### Finite singular-carrier reduction

- `SINGULAR_CARRIER_DISCRETE_MORSE_UNIFICATION_V1.md`;
- its Type Z and Type D finite weight certificates.

### F

- `PACHNER_HISTORY_FIRST_FAILURE_ONE_EDGE_ATOM_V1.md`.

### L

- root triality and zero removal;
- critical-overlap normalisation;
- route-change terminal transfer;
- direct-pairing-to-theta normalisation.

### S and P

- full-state contextual graph construction;
- forced Petersen backbone;
- constant-pivot full-state consumption;
- full-state cycle correction.

### O+

- oriented channel-lock boundary calibration;
- forced-backbone binary transport;
- Petersen resolution parity;
- `ORIENTED_ODD_PETERSEN_SUBTRACK_EXCLUSION_V1.md`.

### E

- canonical `C6` star section;
- relative `C6` source movie;
- automatic category safety;
- seam-compatible `C8` reduction.

---

## 11. PDL reconstruction target

PDL should prove O+ in the following exact order:

1. the cap distinguishes one route block on every descendant context;
2. forced-backbone transport carries that same physical block;
3. every pivot-closed physical subsegment has zero orientation character;
4. the orientation character equals pivot-length parity;
5. therefore no odd simple pivot subtrack occurs;
6. only then extract `C6/C8` and apply the even movie.

This prevents any appeal to the weaker statement that an odd full-state cycle fails to close in one lap.

---

## 12. Trust boundary

### Proved abstractly here

- no-sink implication with O+;
- exclusion of odd double-lap recurrence;
- lexicographic contextual-transfer induction.

### Not proved anew

- concrete orientation calibration;
- forced-backbone exhaustiveness;
- `C6/C8` source movies;
- one-cross cap restoration;
- global five-CDC acceptance, Lean verification, manuscript, release, or publication status.
