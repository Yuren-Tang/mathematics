# AC-PD-5CDC — proof DAG and current status

**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Research input:** `research/affine-cdc-five-cdc-v1`  
**PDL branch:** `proof-development/affine-cdc-rigour-v1`  
**State:** `ACTIVE / MAJOR AUTHORIAL CANDIDATE / ONE EXACT GLOBAL-RETURN INTERFACE OPEN`.

---

## 1. Preferred theorem spine

\[
\begin{array}{c}
\text{five indexed even supports}\
\Updownarrow\
R_5\text{-valued }E_5\text{ flow on a loopless cubic graph}\
\Downarrow\ R1\
\text{one smaller valid cross closure at every simple edge}\
\Downarrow\ R2\
\text{relative root-flow extension across the deleted two-vertex cap}\
\Downarrow\
\text{theta base + vertex-order induction}\
\Downarrow\
\text{cubic five-support theorem}\
\Downarrow\
\text{finite-active bridgeless multigraph five-CDC outer shell}.
\end{array}
\]

Only `R2` remains incomplete at PDL assurance level.

---

## 2. Closed proof units

| Unit | State | PDL source | Exact result |
|---|---|---|---|
| `R0` | integrated authority | Programme B1 | five indexed even supports, `R_5`-valued flows, `K_5` triangle labellings and anisotropic `O^-(4,2)` flows are equivalent |
| `R1` | `CLOSED` | `AC_PD_5CDC_R1_ONE_CROSS_STRUCTURAL_REDUCTION.md` | every simple edge has a connected loopless bridgeless cubic cross closure with two fewer vertices; theta is the no-simple-edge base |
| `R2.1` | `CLOSED` | `AC_PD_5CDC_R2_1_BOUNDARY_ROUTE_CERTIFICATE.md` | 640 conserved boundaries, ten states, exact `J_i/K_i`, sixteen route rows, `P_3 sqcup C_4 sqcup P_3`, fixed-route equality/DDD reduction |
| `R2.2` | `CLOSED` | `AC_PD_5CDC_R2_2_SINGULAR_MORSE_DESCENT.md` | positive equality and DDD Morse weights; complete no-local-minimum and termination proof |
| `R2.3` | `CLOSED-LOCAL` | `AC_PD_5CDC_R2_3_FIRST_FAILURE_AND_LOCAL_CONFLUENCE.md` | one zero/co-root first-failure atom; bounded critical overlaps; no persistent branching; category safety |
| `R2.E` | `CLOSED-CONDITIONAL-ON-P/O+` | `AC_PD_5CDC_R2_5_EVEN_TRACK_CYLINDER_ERASURE.md` | full-labelled `C6/C8` co-root tracks admit same-order relative root-cylinder erasure; no cancellation recursion needed for even co-root recurrence |

---

## 3. Partially reconstructed global units

### `R2.P` — forced backbone

Retained finite geometry:

- every persistent token is one co-root with two crossed root resolutions;
- constant-pivot runs have one unique root-admissible nonpivot section;
- after removing immediate backtracks, repeated pivots yield a shortest simple Petersen cycle;
- simple lengths are exactly `5,6,8,9`.

Remaining PDL task:

- consolidate all source-incidence, side-root, cap-block and history-position data into one exhaustive theorem from an arbitrary persistent complete-state SCC to the full-labelled annulus used by `E_cyl`.

State:

`HIGH-CONFIDENCE / FULL-LABELLED EXPANSION REQUIRED`.

### `R2.O+` — oriented odd exclusion

Closed linear statement:

\[
\operatorname{Hol}_{\rm res}(\gamma)=|\gamma|\pmod2.
\]

Remaining statement:

\[
\boxed{
\text{every physical pivot-closed subtrack preserves the same distinguished cap block}.}
\]

Only after this is expanded may odd `C5/C9` be excluded before a double traversal.

State:

`HIGH-CONFIDENCE / FULL-LABELLED EXPANSION REQUIRED`.

---

## 4. Unique current blocker

### `AC-PD-5CDC-EQ-RETURN`

**Problem.** Reverse an equal-face cancellation when the terminal flow on the smaller graph gives quadruple equality

\[
r,r,r,r.
\]

All three local pairing sums are zero, so no local root NNI exists.

Required output: one of

1. same-order rootification preserving the complete cap context;
2. a cap/route/category terminal;
3. a recursive contextual obligation with a rigorously decreasing complete-state measure;
4. a relative inverse-weld theorem preserving the two cancellation-interface roots.

Ordinary root-flow existence on the smaller graph is insufficient because another flow may give equal or disjoint interface roots.

This is the exact remaining load-bearing gap after same-order `C6/C8` cylinder erasure.

---

## 5. Supersession decisions

### Retained

- one-cross minimal proof architecture;
- ten-state boundary calculus;
- equality/DDD Morse functions as local search tools;
- first-failure one-token grammar;
- full-labelled Petersen transport;
- relative `C6/C8` movies;
- finite-condensation reasoning once every recursive edge is genuinely well founded.

### Superseded for controlling use

1. `SINGULAR_ROOT_TRIALITY_CONFLUENCE_MASTER_THEOREM_V3.md` claim that cancellation automatically yields an `N-2` relative obligation and permits induction only on `N`.
2. The same unproved cancellation-order implication in v1/v2, despite their `(N,m)` notation.
3. Use of the canonical-star equal-face cancellation as the necessary exit for co-root recurrence; same-order cylinder erasure is stronger.
4. Any proof summary saying the global theorem is complete before `AC-PD-5CDC-EQ-RETURN` is closed.

---

## 6. Literature boundary

Targeted precedent search found:

- classical and recent 5-CDC results for special graph classes and sufficient conditions;
- color-preserving bistellar connectivity when both endpoint triangulations are already coloured;
- balanced-surface results showing that subdivisions and welds alone need not give connectivity;
- simplicial projectivity theory as a structural analogy.

No located theorem supplies the relative inverse-weld result required by `AC-PD-5CDC-EQ-RETURN`.

Controlling note:

`AC_PD_5CDC_TARGETED_LITERATURE_AND_PRECEDENT_NOTE.md`.

---

## 7. Current exact classification

\[
\boxed{
\begin{array}{c}
R1\text{ closed}\
+\ R2\text{ finite/local core closed}\
+\ \text{co-root recurrence repaired by same-order cylinder erasure}\
+\ P,O^+\text{ need consolidated full-labelled expansion}\
+\ \text{one equality inverse-weld return obligation open}.
\end{array}}
\]

Therefore:

- not `COMPLETE-DRAFT`;
- not `READY-FOR-CURATOR`;
- no independent audit launch yet;
- no Lean/manuscript/release/publication consequence.

The dedicated complete-result notification must occur only after `P`, `O+`, and `AC-PD-5CDC-EQ-RETURN` are all closed and the final induction is reassembled without the invalid target-order shortcut.