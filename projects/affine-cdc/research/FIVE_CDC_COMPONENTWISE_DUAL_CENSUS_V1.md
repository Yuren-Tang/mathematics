# Componentwise dual-half-cube census around the fixed-Fano obstruction

**Programme:** `AffineCDC — Research Lead`  
**Status:** exact finite computational evidence with theorem-level displayed certificates; not a general theorem  
**Parents:** `FIVE_CDC_COLORED_SURFACE_DUAL_HALFCUBE_V1.md`, `FIVE_CDC_GAUGE_PARTIAL_PETRIAL_CORRESPONDENCE_V1.md`, `FIVE_CDC_HALFCUBE_SCOPE_CORRECTION_V1.md`

## 1. Purpose

The earlier census classified root lifts by the global-index-factorable condition

\[
J_g\to\mathscr A_5.
\]

The corrected same-embedding condition is

\[
T_g\to\mathscr A_5,
\]

where `T_g` is the full dual triangulation of the cycle-face embedding. This packet recomputes the thirty-vertex neighbourhood with the componentwise criterion.

It also separates:

- all nonzero binary-cycle words, which may have several connected components;
- connected source cycles, which are the actual edges of the nowhere-zero flow reconfiguration graph.

## 2. Exact computational method

For every switch pair `(a,z)`:

1. start from the thirty-vertex fixed obstruction flow;
2. require `z\in\mathcal C(G-E_a)` so the switched flow is nowhere zero;
3. solve the affine root-lift equations exactly over `\mathbf F_2` with one source-vertex translation fixed to zero;
4. enumerate the complete reduced root-lift torsor;
5. for each lift, construct all support-cycle components and the full uncolored dual triangulation `T_g`;
6. test first the quotient-factorable criterion using the exact `K_6/K_8-C_5` theorem;
7. when that fails, solve the graph-homomorphism problem `T_g\to\mathscr A_5` by exact backtracking with target automorphism normalization and forward propagation.

The old factorable totals are reproduced exactly, serving as a regression check.

## 3. All binary-cycle switches

The seven cycle-space dimensions are

\[
10,6,9,11,10,11,10,
\]

so the number of nonzero switch pairs is

\[
\sum_{a\ne0}(2^{\dim\mathcal C(G-E_a)}-1)=7737.
\]

These include disconnected unions of source cycles.

### Global-index-factorable criterion

\[
\begin{array}{c|r}
\text{fibre outcome}&\text{switch pairs}\\
\hline
\text{no reduced lift good}&3453\\
\text{some but not all good}&3060\\
\text{all reduced lifts good}&1224
\end{array}
\]

### Full componentwise criterion

\[
\begin{array}{c|r}
\text{fibre outcome}&\text{switch pairs}\\
\hline
\text{no reduced lift good}&1121\\
\text{some but not all good}&2128\\
\text{all reduced lifts good}&4488
\end{array}
\]

The transition table is

\[
\begin{array}{c|ccc}
&\text{componentwise none}&\text{componentwise some}&\text{componentwise all}\\
\hline
\text{factorable none}&1121&988&1344\\
\text{factorable some}&0&1140&1920\\
\text{factorable all}&0&0&1224
\end{array}
\]

Thus

\[
\boxed{2332}
\]

switch pairs whose entire fibre was quotient-factorable bad become componentwise good, and

\[
\boxed{1344}
\]

of them become componentwise good in every reduced lift.

## 4. Genuine connected-cycle neighbours

Exactly

\[
\boxed{2801}
\]

of the `7737` binary-cycle words have connected support. These are the actual single-edge neighbours in the reconfiguration graph.

### Factorable outcomes

\[
\begin{array}{c|r}
\text{none}&1245\\
\text{some}&1133\\
\text{all}&423
\end{array}
\]

### Componentwise outcomes

\[
\begin{array}{c|r}
\text{none}&360\\
\text{some}&783\\
\text{all}&1658
\end{array}
\]

Hence

\[
\boxed{2441/2801}
\]

connected-cycle neighbours have at least one componentwise-good root lift.

The full transition table is

\[
\begin{array}{c|ccc}
&\text{componentwise none}&\text{componentwise some}&\text{componentwise all}\\
\hline
\text{factorable none}&360&344&541\\
\text{factorable some}&0&439&694\\
\text{factorable all}&0&0&423
\end{array}
\]

The shortest connected cycle giving at least one componentwise-good lift has length five. The shortest connected cycle for which every reduced lift is componentwise good has length six; the corresponding factorable threshold was seven.

## 5. Residual obstruction census

The `360` connected-cycle neighbours whose entire reduced fibre remains componentwise bad contain

\[
752
\]

reduced root lifts in total. Their fibre sizes split as:

\[
\begin{array}{c|r}
\text{reduced lifts in fibre}&\text{bad neighbour flows}\\
\hline
1&92\\
2&216\\
4&47\\
8&5
\end{array}
\]

For every one of these `752` lifts, the simple one-skeleton of the dual triangulation contains a `K_6`.

No example in this connected neighbourhood was found with

\[
\omega(T_g)\le5
\quad\text{but}\quad
T_g\nrightarrow\mathscr A_5.
\]

Thus, in this finite neighbourhood, the entire residual componentwise obstruction is explained by the elementary clique bound

\[
\omega(\mathscr A_5)=5.
\]

This is evidence only. It does not assert that `K_6` is the only obstruction for arbitrary dual triangulations.

## 6. Mechanism revealed by the correction

The enlarged freedom changes the interpretation of the previous programme.

1. The two-apex, pentagon, and one-star cores govern only maps that factor through the old eight-color quotient.
2. A componentwise map can split old support components and bypass those quotient defects.
3. Support pivots preserve the uncolored dual triangulation and therefore cannot change componentwise homomorphism existence directly.
4. Gauge moves are code-filtered partial Petrials and can change the dual triangulation.
5. Horizontal flow switches matter because they change the admissible gauge/Petrial code in the new fibre.

The corrected local picture is therefore:

\[
\boxed{
\text{bad embedding}
\xrightarrow{\text{code-filtered partial Petrials}}
\text{dual triangulation without the active obstruction}
\xrightarrow{}
\mathscr A_5.
}
\]

For the present certificate, the active residual obstruction is a dual `K_6` clique.

## 7. Next structural target

The next theorem-level problem is:

> Given a compatible cycle-face embedding whose dual triangulation contains a `K_6`, determine when an admissible gauge word / partial Petrial destroys every `K_6` in the dual, or else extract a coherent clique system forcing a topological decomposition.

This is more intrinsic than decreasing the old used-index density. It acts on the actual same-embedding obstruction and connects directly to the archived gauge–embedding and partial-Petrial programme.

No claim in this packet proves that every `K_6` obstruction can be removed, that every `K_6`-free dual maps to `\mathscr A_5`, or that every cubic graph has a five-support cover.
