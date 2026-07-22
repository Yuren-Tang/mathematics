# Erdős 306 theorem-dependency map

## 1. Authority nodes

```text
F0  released community theorem Erdos306.erdos_306
RS1 Rosser–Schoenfeld Corollary 3
RS2 Rosser–Schoenfeld Theorem 5
PNT prime number theorem
AI(mu) common-threshold construction interface
```

Status:

- $F0$: Lean-closed at `v0.0.3@4582185...`;
- $RS1,RS2$: the only nonstandard released assumptions;
- `PNT`: external theorem for the preferred human backend, not a released axiom;
- `AI(mu)`: human dependency interface, not a single declaration in v0.0.3.

## 2. Analytic fork

```text
RS1 -> explicit dyadic density
RS2 -> explicit inclusive reciprocal-window mass
        \_______________________________/
                    AI_RS

PNT -> tail-uniform Abel summation
    -> local reciprocal-prime law A_k=1/k+o(1/k)
    -> eventual dyadic density
    -> eventual inclusive mass
        \_______________________________/
                    AI_PNT

AI_RS or AI_PNT -> AI(mu) -> common downstream construction.
```

No premise or assurance status transfers between the two provider branches.

## 3. Downstream construction DAG

```text
AI(mu)
  |
  +-> dense dyadic blocks
  |     -> control graph and sigmaCtrl lower bound
  |     -> common high-prime reservoir
  |
  +-> reciprocal window
        -> pair-pool mass

finite Fourier identity
  |
control graph + centred CRT
  -> local nondominant forcing
  -> dominant labels and exceptions
  -> corrected adjacent-label penalty
  -> global level-set encoder
  -> localisation:
       off-main -> high floor or global diagonal
  -> high-floor Laplace tail
  -> diagonal Gaussian tail
  -> block-minor estimate

pair-pool mass + fixed control/auxiliary load
  -> greedy reciprocal completion
  -> theta window and exact expected mass
  -> no-wrap
  -> variance comparison

theta window
  -> Bernoulli Fourier damping c_F
  -> major-arc Taylor lower bound

squarefree b + common prime reservoir
  -> sibling mismatch prime
  -> beta_b^G damping
  -> sibling-minor estimate

major lower
+ block-minor upper
+ sibling-minor upper
+ non-circular budget order
  -> positive weighted count
  -> exact representation of 1/b avoiding T
  -> b=1,2 closure
  -> numerator induction
  -> finite increasing tuple
  -> F0.
```

## 4. Exact load-bearing boundaries

The following implications must not be compressed away.

1. Large denominators alone do not prove small control load; an elementary block-cardinality upper bound is used.
2. Distinct adjacent labels do not by themselves force boundary energy; all corrected hypotheses are required.
3. The level-set count has a structural per-block entropy factor $e^{AJ}$.
4. Wrapped large labels are controlled by injection into a fixed small-label fibre.
5. The low-energy diagonal identity requires the centred CRT range.
6. The pair-pool lower bound has no hidden positive surplus; fixed forbidden load is cancelled by already-spent base load.
7. The linear term cancels only because the uniform weights have exact expected reciprocal mass $1/b$.
8. The principal logarithm requires Bernoulli factors to be nonzero in a right-half-plane disk.
9. The block and sibling classes form a partition only inside the genuine Fourier-minor set.
10. The factors $b$ and $b(2N+1)$ are exact CRT/frequency cardinalities.
11. One common $G$-prime reservoir must work for every mismatch prime dividing $b$.
12. All terminal constants are fixed before $k_0$.
13. The selected object is finite; the formal initial value $1$ is a dummy anchor excluded from the sum.

## 5. Residual nodes

### Finite/kernel residuals

Named Lean declarations may close:

- rational constant chases;
- cast, floor, and endpoint arithmetic;
- finite threshold maxima;
- inverse-square numerical bounds;
- aggregate Taylor constants;
- final explicit budget inequalities;
- finite-set-to-tuple index identities.

They are legitimate only because the mathematical implication and hypotheses are explicit in the corpus.

### Source gate

`E306-PDL-RS-PUBLISHER-SCAN` remains open: compare the two released axiom transcriptions symbol by symbol with the publisher scan on pp. 69–70.

This is a source-certification obligation, not a downstream proof gap.

### Non-blocking architecture map

`E306-PDL-C4-RELEASE-REFACTOR-CORRESPONDENCE` remains a useful exact declaration genealogy between v0.0.3 and the orphan frozen refactor. It is not needed to justify the theorem or this corpus.
