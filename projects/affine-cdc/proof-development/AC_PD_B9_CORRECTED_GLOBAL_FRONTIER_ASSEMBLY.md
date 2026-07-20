# AC-PD-B9 — corrected global five-support frontier assembly

**Proof-development state:** `BLOCKED-FRONTIER / CORRECTED-ASSEMBLY / AC-RL-DEPENDENT`  
**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Exact initial corpus base:** `main@960c92b7ff231c78b387894149779083060a75eb`  
**Depends on:** Programme A and B1–B8  
**External mathematical inputs:** Seymour's six-flow theorem only through the complete CDC outer spine; none in the unresolved five-support closure arrow  
**Assurance:** exact current theorem and frontier map; no global five-support theorem claimed

## 0. Two different global statements

The complete Cycle Double Cover theorem and the five-support strengthening are distinct.

### Closed theorem

Every multigraph with finite active edge set and no singleton cut has a cycle double cover. Programme A supplies a complete authorial proof-development spine.

### Open strengthening

Every such graph should admit an indexed family of at most five cut-even supports covering every active edge exactly twice. In a cubic loopless graph, this is equivalent to every B1/B2 root-flow formulation.

No B1–B9 packet proves this strengthening globally.

## 1. Five-support outer reduction

### Definition 1.1

A **five-support even double cover** of a finite-active-edge multigraph $G$ is a five-tuple

$$
(F_1,\ldots,F_5)
$$

of finite cut-even edge supports such that every active edge belongs to exactly two indexed supports. Empty and repeated support values are allowed.

### Theorem 1.2 — loop deletion and reinsertion preserve five supports

Let $G_0$ be obtained by deleting every loop of $G$.

1. A five-support cover of $G$ restricts to one of $G_0$.
2. A five-support cover of $G_0$ extends to one of $G$ by placing every deleted loop into, for example, $F_1$ and $F_2$.

### Proof

Loops cross no cut. Deleting them preserves cut parity and nonloop multiplicities. Adding a loop to any support preserves cut parity, and placing it in exactly two indexed supports gives multiplicity two. $\square$

### Theorem 1.3 — cubic expansion and collapse preserve five supports

Let $G_0$ be finite, loopless, and bridgeless, and let $H$ be its port-cycle cubic expansion with original-edge injection

$$
\lambda:E(G_0)\hookrightarrow E(H).
$$

If $H$ has a five-support cover $(F'_i)_{i=1}^5$, then

$$
F_i=\{e\in E(G_0):\lambda(e)\in F'_i\}
$$

is a five-support cover of $G_0$.

### Proof

A8's pulled-back-cut bijection proves every $F_i$ cut-even. For every original edge $e$ and index $i$,

$$
e\in F_i
\iff
\lambda(e)\in F'_i,
$$

so the exact index multiplicity is preserved. Auxiliary edges disappear without changing the number of support occurrences. $\square$

### Corollary 1.4 — exact cubic core

The following global statements are equivalent.

1. Every finite-active-edge multigraph with no singleton cut has a five-support even double cover.
2. Every finite loopless bridgeless cubic multigraph has a five-support even double cover.

The nontrivial direction is Theorems 1.2–1.3; the reverse direction is specialization.

Thus no extra loop, high-degree, disconnected, parallel-edge, or ambient-carrier theorem remains after the cubic case.

## 2. Exact cubic witness package

For a finite loopless cubic graph $G$, five-support existence is equivalent to each full-witness formulation:

1. five indexed even supports;
2. an $R_5$-valued $E_5$ flow;
3. a $K_5$ triangle labelling;
4. an anisotropic $O^-(4,2)$ flow;
5. a quadratic cycle solution;
6. a cycle-continuous edge map $M(G)\to M^*(K_5)$;
7. exact matching/four-flow data;
8. existence of a Fano flow and plane with empty component-obstruction profile;
9. existence of a cycle-face embedding whose full dual maps to $\mathscr A_5$.

These are equivalent targets, not proofs of universal existence.

## 3. Exact fixed-data structure

For a fixed Fano flow $f$:

- compatible root lifts form an affine gauge torsor;
- a fixed plane has a complete component-parity/Schur/stress criterion;
- a fixed root lift is good exactly when its full dual maps to $\mathscr A_5$;
- the old-colour quotient gives only the factorable subroute;
- vertical motion is a code-filtered partial Petrial;
- horizontal adjacency is one connected-cycle switch;
- composite same-direction switch images are not one-edge neighbour sets.

Finite target and gauge classifications do not remove the existential choice of flow and lift.

## 4. Separator and routing reduction

A minimal cubic counterexample, if one exists, is cyclically four-edge-connected. Across a cyclic four-cut:

- each shore has a profile in the ten-state alphabet;
- the profiles are disjoint;
- cap forcing holds;
- genuine Kempe transitions require terminal-path pairing alignment;
- uniform routing is reducible.

The residual policy is Type T or Type H.

## 5. Correct Type H endpoint

For one genuine Type H loop:

- nonzero norm is an ambient obstruction;
- zero norm reduces to root-fibre lifting;
- a soluble zero-norm loop has a Tait resolution and strictly escapes;
- every residual physical lift has a norm cycle, uncovered edge, or missed vertex.

The BBD global common-origin and nontrivial defect-forest synthesis are not unconditional theorems. Their exact gaps were returned to AC-RL.

The independent DDD atom branch yields:

- local resolution triality;
- unique bad route;
- a locked $F_2^3$ quotient;
- rank-two Tait escape;
- in full rank, flat potential or nonflat common scalar-sheet cut.

Neither full-rank branch is yet converted into a smaller source graph or finite transfer interface.

## 6. Exact missing arrows

The corrected programme has six named new-mathematics obligations.

### BBD synthesis

1. `AC-RL-BBD-GROUPOID-CLOSURE`;
2. `AC-RL-BBD-VARIATION-SLICE`.

### Source localisation/composition

3. `AC-RL-TYPE-T-SERIALISATION`;
4. `AC-RL-FLAT-POTENTIAL-INTERFACE`;
5. `AC-RL-COMMON-CUT-LOCALISATION`;
6. `AC-RL-TYPE-H-COMMON-WITNESS`.

The first pair concerns one proposed BBD proof route. The second group is sufficient to continue the corrected DDD/four-pole route independently.

## 7. Two sufficient future closure packages

### Package E — global escape

It would suffice to prove:

> For every finite loopless bridgeless cubic graph, there exists a nowhere-zero Fano flow and one compatible root lift whose full dual maps to $\mathscr A_5$.

B1 then gives five supports, and Section 1 transports them to the natural multigraph theorem.

A weaker horizontally/vertically iterative theorem also suffices if it proves termination at such a state.

### Package D — strict decomposition

It would suffice to prove:

> Every persistent bad cubic state produces a cyclic cut or bounded transfer object whose pieces are strictly smaller and whose complete five-support boundary profiles glue.

B5 supplies the three-cut and four-cut gluing languages. The future theorem must preserve labelled terminal/support data and provide a well-founded decrease.

A mixture of escape and decomposition is equally sufficient.

## 8. What finite certificates can and cannot supply

Finite data establish exact behavior in named graphs, flows, fibres, target graphs, four-poles, routing automata, and root tables. They may:

- falsify overstrong universal statements;
- supply finite inputs to theorem arguments;
- identify candidate local mechanisms.

They cannot prove either Package E or Package D without one general source theorem.

The B8 assurance ledger is controlling for every count and verifier claim.

## 9. Corrections incorporated into the final frontier

1. Matching/four-flow requires the exact boundary datum.
2. Full dual and old-colour quotient are distinct.
3. Connected switches and disconnected composite cycle words are distinct.
4. The universal $2r$ orthogonal-root hierarchy is false; the correct dimension is $q-2$.
5. Stress/Fourier data are dual criteria, not independent source witnesses.
6. BBD physical affine group closure is unproved.
7. The stated defect-minimal forest variation is vacuous.
8. DDD atom theorems survive independently of that forest.
9. Scalar-sheet common cuts are not yet underlying graph cuts.
10. Finite certificates retain their exact assurance classes.

## 10. Current mathematical conclusion

The complete CDC theorem is closed. The five-support strengthening is not.

The strongest trustworthy present statement is:

$$
\boxed{
\begin{array}{c}
\text{the cubic five-support target and all mature local/fixed-data mechanisms are exact;}\\[2mm]
\text{global source localisation/composition remains open in six named obligations.}
\end{array}}
$$

No manuscript, release, priority, formalization, or publication claim follows from this checkpoint.

## 11. Persistent-role continuation

AC-PDL remains active for:

- exact repairs returned by Curator, audit, Lean, or manuscript projection;
- proof development on any AC-RL-returned localization packet;
- maintenance of the theorem/obligation DAG;
- integration-ready checkpoints as new proof units mature.

Without new AC-RL mathematics or a returned defect, the present B9 node remains `BLOCKED-FRONTIER`, not completed or abandoned.

## 12. Completion assessment

`AC-PD-B9` is `BLOCKED-FRONTIER / CORRECTED-ASSEMBLY / AC-RL-DEPENDENT`.