# AC-PD-B7.2 — localisation frontier and exact AC-RL return

**Proof-development state:** `COMPLETE-DRAFT / AC-RL-RETURN / GLOBAL-COMPOSITION-OPEN`  
**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Exact initial corpus base:** `main@960c92b7ff231c78b387894149779083060a75eb`  
**Depends on:** B5 Type T/H routing; B6 corrected holonomy/atom layer; B7.1 rank and curvature dichotomy  
**Immediate consumer:** B9 corrected global frontier  
**External mathematical inputs:** none

## 0. Disposition

After the corrected B6 and B7.1 theorem layers, the remaining source-side problem is no longer an algebraic classification. It consists of three exact localisation/composition theorems.

1. Type T acyclic routing must yield a smaller separator or bounded serial transfer object.
2. A flat full-rank route-locked potential must yield finite transfer data or strict decomposition.
3. A nonflat common scalar-sheet cut must be identified with a bounded graph interface or the physical DDD class.

These are genuine new-mathematics obligations and are returned to AC-RL. AC-PDL may continue with certificate normalization and final dependency assembly.

## 1. Type T input

The finite routing certificate gives an acyclic deterministic safe policy of type

$$
P_5\mid P_5.
$$

Uniform routing has already been eliminated. Thus the route selected by a support-pair challenge changes along the profile path in a rigid acyclic pattern.

The finite automaton alone does not prove that the corresponding internal terminal paths are nested, serial, or separated in the source four-pole. Different indexed covers may realize the same abstract policy by unrelated internal path systems.

### Required theorem `AC-RL-TYPE-T-SERIALISATION`

For every cubic four-pole whose complete indexed-cover routing realizes one of the Type T deterministic policies, prove one of:

1. a cyclic two- or three-level separator strictly smaller than the original four-cut;
2. a serial composition into smaller four-poles with an exact finite transfer state;
3. a bounded replaceable fragment preserving the ten-state boundary profile;
4. a genuine profile escape.

The theorem must include an explicit decreasing measure and an exact gluing map. A proof about the abstract policy graph alone is insufficient.

## 2. Flat full-rank input

The route-locked quotient is a full-rank nowhere-zero flow

$$
c:E(Q)\to E_4\setminus\{0\}
$$

with all terminal values $g$. If $\Omega(c)=0$, B7.1 gives

$$
p:V(Q)\to E_4
$$

with terminal values $0,0,g,g$ and

$$
p(u)+p(v)\in\{0,c(uv)+g\}.
$$

This partitions the vertices into at most eight potential fibres. Edges between distinct fibres have constrained colours; edges inside one fibre may contain arbitrary large subgraphs and semantics.

### Required theorem `AC-RL-FLAT-POTENTIAL-INTERFACE`

From the potential $p$, prove one of:

1. a proper separator between potential fibres;
2. a bounded transfer-state quotient under four-terminal gluing;
3. a replaceable repeated fibre or repeated enriched transition interval;
4. a root-valued crossed atom resolution or boundary-profile escape.

The output must reconstruct or transfer indexed support data, not merely quotient colours. Finite range of $p$ does not by itself imply bounded graph complexity.

## 3. Nonflat full-rank input

If $\Omega(c)\ne0$, B7.1 gives a support-minimal set

$$
\eta\subseteq E_g
$$

that is simultaneously a cut in all four scalar sheets and whose four terminal cut parities form an odd word.

This is stronger than four unrelated dual certificates, but it is not yet a graph cut of the underlying four-pole.

### Required theorem `AC-RL-COMMON-CUT-LOCALISATION`

For a support-minimal nonflat witness $\eta$, prove one of:

1. $\eta$ induces a bounded DDD/Petersen atom or four-pole factor;
2. consecutive witness edges determine a smaller cyclic separator;
3. the scalar-sheet cuts combine into a transition-matroid two-sum or Whitney-type replacement;
4. the odd terminal class maps canonically to the physical nontrivial $D_8$ affine cohomology class;
5. a counterexample demonstrating the exact weaker statement that is true.

Required intermediate points include:

- a comparison from scalar-sheet cut spaces to the underlying graph/interface;
- a size, connectivity, or interval control on a minimal $\eta$;
- a composition-safe transfer of support indices;
- a strictly decreasing parameter.

## 4. Type H family correlation

Independently of route-locked atoms, B6.2 shows that every physical Type H lift in a minimal kernel has one signature:

$$
(d_\lambda,U_\lambda,X_\lambda).
$$

### Required theorem `AC-RL-TYPE-H-COMMON-WITNESS`

If every physical lift is obstructed, prove that the norm cycles, uncovered-edge sets, or missed-vertex sets share one bounded connected source witness yielding profile escape or decomposition.

This theorem must use the correlation among lifts arising from the same three complementary support-pair path systems. Separate per-lift obstruction statements do not suffice.

This obligation overlaps with, but is not implied by, the route-locked atom localisation problems.

## 5. Interaction with the earlier BBD returns

The following B6.3 gaps remain independent:

- `AC-RL-BBD-GROUPOID-CLOSURE`;
- `AC-RL-BBD-VARIATION-SLICE`.

No localisation theorem should use the unconditional BBD common flow or defect forest until those gaps are resolved.

The DDD atom and route-lock branch remains valid without them.

## 6. Exact current source frontier

The corrected source theorem target is:

$$
\boxed{
\begin{array}{c}
\text{persistent bad four-pole or bad-flow component}\\
\Downarrow\\
\text{Type T serial interface}
\quad\text{or}\quad
\text{Type H common witness}
\quad\text{or}\quad
\text{flat/nonflat locked interface}\\
\Downarrow\\
\text{strictly smaller graph, bounded transfer object, or profile escape}.
\end{array}}
$$

No current packet supplies the final downward arrow in general.

## 7. Non-goals

The return does not ask AC-RL for:

- more ten-state enumeration;
- larger fixed-graph censuses;
- another equivalent algebraic formulation;
- an unbounded target obstruction library;
- a proof that route-lock is an ordinary two-edge cut;
- use of the invalid nontrivial BBD defect forest.

The required output is source localisation plus composition.

## 8. Completion assessment

`AC-PD-B7.2` is `COMPLETE-DRAFT / AC-RL-RETURN / GLOBAL-COMPOSITION-OPEN`. It defines the exact corrected frontier passed to AC-RL and B9.