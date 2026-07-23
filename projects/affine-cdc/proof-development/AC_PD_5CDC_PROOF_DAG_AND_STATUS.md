# AC-PD-5CDC — proof DAG and current status

**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Research input:** `research/affine-cdc-five-cdc-v1`  
**PDL branch:** `proof-development/affine-cdc-rigour-v1`  
**State:** `ACTIVE / R1 AND LOCAL R2 RETAINED / R2.7 MARKED-WELD FRONTIER OPEN`.

---

## 1. Preferred theorem spine

\[
\begin{array}{c}
\text{five indexed even supports}\\
\Updownarrow\\
R_5\text{-valued }E_5\text{ flow on a loopless cubic graph}\\
\Downarrow\ R1\\
\text{one smaller valid cross closure at every simple edge}\\
\Downarrow\ R2\\
\text{relative root-flow extension across the deleted two-vertex cap}\\
\Downarrow\\
\text{theta base + vertex-order induction}\\
\Downarrow\\
\text{cubic five-support theorem}\\
\Downarrow\\
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
| `R2.2` | `CLOSED` | `AC_PD_5CDC_R2_2_SINGULAR_MORSE_DESCENT.md` | positive equality and DDD Morse weights; complete no-local-minimum and termination proof for the inherited current flow |
| `R2.3` | `CLOSED-LOCAL` | `AC_PD_5CDC_R2_3_FIRST_FAILURE_AND_LOCAL_CONFLUENCE.md` | one zero/co-root first-failure atom; bounded critical overlaps; no local atom proliferation; category safety |
| `R2.6-local` | `CLOSED-LOCAL/HISTORY` | `AC_PD_5CDC_R2_5A_PRE_CANCELLATION_SCOPE_CORRECTION.md` | relative `(0,2,2)` `C6` chart, root cross-to-star NNI, interface compatibility, equal-face weld word, seam-compatible `C8` reduction; no complete time-slice exit claimed |

---

## 3. Partially reconstructed global units

### `R2.4` — forced backbone

Retained finite geometry:

- every persistent token is one co-root with two crossed root resolutions;
- constant-pivot runs have one unique root-admissible nonpivot section;
- after removing immediate backtracks, repeated pivots yield a shortest simple Petersen cycle;
- simple lengths are exactly `5,6,8,9`.

Remaining PDL task:

- consolidate source incidence, side-root, cap-block and history-position data into one exhaustive theorem from a mixed complete-state recurrent component to an actual full-labelled track.

State:

`HIGH-CONFIDENCE / FULL-LABELLED EXPANSION REQUIRED`.

### `R2.5` — oriented odd exclusion

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

### `R2.6-global` — even history core

The actual `C6/C8` local and annular movies are retained. The previous PDL claim that all canonical charts form one cubic contextual state or an identity root cylinder is withdrawn. A complete contextual exit is available only after a valid marked-weld return or another strict rank theorem.

State:

`LOCAL/HISTORY CLOSED / CONTEXTUAL EXIT DEPENDS ON R2.7`.

---

## 4. Current blocker

### `AC-PD-5CDC-EQ-RETURN / R2.7`

A genuine equal-face cancellation produces a lower-order graph with two distinguished reconnecting edges. An arbitrary lower-order root flow may label them:

1. distinct intersecting — inverse weld succeeds;
2. equal — quadruple equality and one zero atom;
3. disjoint — one co-root atom.

Thus lower target order alone does not complete the cancel--solve--reinsert macro-transition.

The sufficient marked boundary is

\[
W=(z,z,w,w),
\qquad z\ne w,
\qquad |z\cap w|=1.
\]

Preservation of the ordered intersecting-pair orbit under one global `S_5` permutation is enough; literal support names are not required.

Controlling PDL file:

`AC_PD_5CDC_EQ_RETURN_1_MARKED_WELD_REDUCTION.md`.

Current decomposition:

1. different marked components are closed by independent support relabelling;
2. root NNIs and first-failure normalizations are already relative when frozen marks remain exterior branches;
3. unrestricted two-edge flow selection is false on bounded graphs (`K_4`, triangular prism);
4. exact SAT census finds no bad pair in Petersen, Möbius--Kantor, Heawood, Pappus or Desargues;
5. the live prime target is a two-edge full-channel flexibility/separator theorem;
6. marked route switches, direct terminals and component genealogy remain to be integrated.

Required output is one of:

- marked-weld relative contextual return (`MWR`);
- prime two-edge root-adjacency selection with bounded/separator exits;
- history-coherent terminal selection;
- a cancel--solve--reinsert macro-rank proved to decrease.

---

## 5. Supersession decisions

### Retained

- one-cross minimal proof architecture;
- ten-state boundary calculus;
- equality/DDD Morse functions as local search tools;
- first-failure one-token grammar;
- full-labelled Petersen transport inputs;
- relative `C6/C8` local/history movies;
- finite-condensation reasoning once every recursive or marked edge is genuinely well founded.

### Superseded for controlling use

1. `SINGULAR_ROOT_TRIALITY_CONFLUENCE_MASTER_THEOREM_V3.md` claim that cancellation automatically yields a completed `N-2` relative obligation.
2. The same hidden implication in contextual masters v1/v2.
3. `AC_PD_5CDC_R2_5_EVEN_TRACK_CYLINDER_ERASURE.md` as a global consumer: the local calculations remain useful, but the six charts do not form one cubic contextual time slice merely by interface identification.
4. The claim that a nonterminal sink SCC is necessarily token-only; mixed root/token SCCs are possible without a proved quotient or rank.
5. Any proof summary saying cap restoration or universal five-CDC is complete before R2.7 is closed.

---

## 6. Literature boundary

Targeted precedent search found:

- classical and recent 5-CDC results for special graph classes and sufficient conditions;
- color-preserving bistellar connectivity when both endpoint triangulations are already coloured;
- balanced-surface results showing that subdivisions and welds alone need not give connectivity;
- simplicial projectivity theory as a structural analogy.

No located theorem supplies `MWR` or the prime two-edge flexibility theorem.

Controlling note:

`AC_PD_5CDC_TARGETED_LITERATURE_AND_PRECEDENT_NOTE.md`.

---

## 7. Current exact classification

\[
\boxed{
\begin{array}{c}
R1\text{ closed}\\
+\ R2\text{ finite/local core closed}\\
+\ C6/C8\text{ local and annular movies retained}\\
+\ P,O^+\text{ need consolidated full-labelled expansion}\\
+\ R2.7\text{ marked-weld/prime-flexibility frontier open}.
\end{array}}
\]

Therefore:

- not `COMPLETE-DRAFT`;
- not `READY-FOR-CURATOR`;
- no independent audit launch yet;
- no Lean/manuscript/release/publication consequence.

The dedicated complete-result notification must occur only after `R2.4`, `R2.5` and `R2.7` are closed and the final induction is reassembled without the invalid cancellation shortcut.