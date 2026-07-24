# AC-5CDC-AUDIT-CORE-01 — exact dependency and interface ledger

**Fixed candidate:** `proof-development/affine-cdc-rigour-v1@1f57422e0e415d8902d56eb294183815c0a0b640`  
**Frozen RL source:** `research/affine-cdc-five-cdc-v1@71a10f9ba86c1d2b8b7885e78fa9baa303c77818`

## 1. Dependency policy

A dependency is accepted here only when its exact imported statement matches the consumer and its proof can be reconstructed without using completion status as evidence. A finite coefficient theorem does not automatically supply a physical source-replacement theorem. Equality of root labels does not automatically supply equality of ordered source darts, route sheets, cap blocks, or suspended marks.

## 2. Unit-level ledger

| Unit | Controlling candidate file / source | Exact imported interface | Audit state |
|---|---|---|---|
| R0 | `AC_PD_B1_1_ROOT_FLOW_TRIANGLE_EQUIVALENCE.md` | finite loopless cubic multigraph; indexed vertex-even supports; exact multiplicity two | `ASSURED` |
| R1 | `AC_PD_5CDC_R1_ONE_CROSS_STRUCTURAL_REDUCTION.md` | connected loopless bridgeless cubic multigraph; one simple edge | `ASSURED` |
| R2.1 | `AC_PD_5CDC_R2_1_BOUNDARY_ROUTE_CERTIFICATE.md` | ordered four-root boundary; three terminal matchings; complementary support switch | `ASSURED` at finite target level |
| R2.2 | `AC_PD_5CDC_R2_2_SINGULAR_MORSE_DESCENT.md` | root-triangle `2--2` move; equal-face `2--0` cancellation; equality or DDD boundary | `ASSURED` for current-flow termination |
| R2.3 | `AC_PD_5CDC_R2_3_FIRST_FAILURE_AND_LOCAL_CONFLUENCE.md` | inverse history step; one standard zero/co-root atom; adjacent ordinary root surgery | `PARTLY ASSURED`; raw doubled-disjoint entrance missing |
| R2.4 | `AC_PD_5CDC_R2_4_FULL_STATE_FORCED_BACKBONE.md` | normalized one-standard-atom state; complete physical source cell; ordered route sheets; labelled bigon relations | `NOT ASSURED` at source level |

## 3. R0 interfaces

### Assured

- `A0` graph semantics: finite loopless cubic multigraph, edge objects distinct, parallel edges allowed.
- Exact multiplicity two is indexed multiplicity, not multiplicity of distinct support edge sets.
- Vertex-evenness is once-per-edge incidence parity because loops are excluded.

### No hidden import

The root-flow equivalence and local triangle law require no external theorem.

## 4. R1 interfaces

### Assured

- Original graph is connected, loopless, bridgeless, cubic.
- The reduced edge is simple.
- Cross closures retain incidence multiplicity and may initially have loops; looplessness is proved for the selected closure.

### Output match

The output is exactly one smaller connected loopless bridgeless cubic multigraph. The theorem does not claim extension of a root flow; this is correctly left to R2.

## 5. R2.1 interfaces

### Assured finite interface

- Boundary words are ordered.
- `J_i` and `K_i` are target-state profiles.
- A route row is conditional on a physically realised matching.
- Support-unordered state classification is separated from labelled support transport.

### Explicit non-import

R2.1 does **not** prove:

- existence of an interior challenge component with a chosen route;
- source composition of the target matching;
- cap-return through a surgery history.

The candidate respects this boundary.

## 6. R2.2 interfaces

### Assured

- Every local triangle pair in the finite tables is a legal root-valued `2--2` coefficient move.
- The positive Morse function strictly decreases on selected flips.
- Equal-face cancellation is a declared exit and lowers the positive vertex sum.

### Deferred correctly

R2.2 does not prove inverse return after cancellation. It supplies a finite current-flow history only. This is an appropriate boundary for the unit.

## 7. R2.3 interfaces

### Assured inputs and outputs

The following exact local interface is reconstructed:

1. before the first failed inverse step all current edges are roots;
2. the restored central edge alone may be zero or a co-root;
3. ordered exterior incidences, old/new pairing, cap block, and route orientation are retained;
4. for a **standard nondegenerate** co-root atom, one adjacent root surgery has the stated bounded critical-overlap grammar;
5. a transient two-token tree reduces to at most one token.

### Unassured interface E-MI

A failed inverse cancellation with disjoint reconnected roots produces

\[
(p,q\mid p,q),\qquad p perpendicular q,
\]

whose central values over the three pairings are `Q_i,0,Q_i`. This state is not a standard atom.

The consumer requires a map

\[
\text{raw doubled-disjoint insertion}
\longrightarrow
\{
\text{root state},
\text{accepted bounded exit},
\text{one standard atom}
\}
\]

with literal preservation of:

- source vertices and edge objects;
- ordered dart slots;
- outer root labels;
- old/new terminal pairing;
- cap block;
- physical route;
- support transport.

No such theorem is present in R2.3. The later phrase “doubled-disjoint borrowing dichotomy” is a claimed interface, not a supplied source proof.

### Downstream consumers affected

- R2.4 state definition excludes raw doubled-disjoint states.
- R2.6 fixed-order input excludes them again.
- R2.7 normal-form compression assumes they are internal to bounded macros.

Therefore the omission is load-bearing.

## 8. R2.4 interfaces

### 8.1 Atom/Petersen dictionary

**Assured only for standard atoms.** A nondegenerate atom has two distinct endpoint matchings and an omitted third matching `{s,t}`. The two root resolutions are `s,t`.

**Not supplied:** an ordered source isomorphism identifying the two resolutions with retained cap-route sheets.

### 8.2 Local transport

The coefficient theorem

\[
\{s,x\}\to\{s,y\},\qquad x+y+z=0
\]

and the unique nonpivot choice are assured.

The consumer additionally needs a source-cell map that:

- changes the correct physical pairing by a legal NNI;
- fixes every exterior edge object and dart;
- transports the selected route block;
- identifies the complete state on overlapping cells.

This stronger map is asserted but not exhibited.

### 8.3 Six-port star interface

The finite theorem “four root stars, two `s--t` failures” is assured.

The required physical theorem is:

> Given the actual exterior source components and ordered route data of one pivot-change cell, either one coefficient-valid star matching is realised by a legal relative source replacement, or the exterior decomposition proves a declared route/profile/separator/category exit, or the physical matching is forced to contain `s--t`.

No proof of this theorem appears in the R2.4 file, and no exact dependency is cited for it.

### 8.4 Ordered route-sheet transport

The Petersen-edge endpoints give an unordered two-sheet set. The consumer needs transition maps between **ordered** sheets. To prove “no independent route bit”, it must show:

1. the local map is uniquely determined by the physical source cell;
2. it preserves the cap-oriented block convention;
3. compositions around a track have the asserted monodromy;
4. no independent sign can be inserted at a seam.

No explicit map or cocycle proof is supplied.

### 8.5 Backtrack bigon

The required theorem is a finite labelled history disc for

\[
s\to t\to s
\]

whose boundary is the exact two-cell source history and whose interior uses only legal root-valued source moves.

R2.4 names an involution/square/pentagon lift and a disjoint-doubled root square but gives:

- no exact source filename;
- no exact theorem identifier;
- no move list;
- no intermediate graphs;
- no ordered boundary map.

This dependency is therefore `NOT ASSURED`.

### 8.6 Full-data retention

Downstream consumers require literal equality, not orbit equivalence, of:

- source topology;
- vertex and dart identities;
- edge-root values;
- crossed-resolution sheet;
- side-root occurrences;
- support transport;
- cap block;
- route orientation;
- surviving and suspended marks.

R2.4 states retention but does not define the maps that establish it.

## 9. Exact repair interfaces

### Repair E1 — doubled-disjoint normalization

Prove a bounded theorem with input `(p,q|p,q)`, `p perpendicular q`, and complete source decorations. Its output must be root-valued, accepted, or one nondegenerate standard atom. Include all parallel-edge and theta cases.

### Repair F1 — source-cell critical-overlap table

Replace the coefficient-only list by finitely many labelled source movies, with explicit pre/post graphs and dart maps.

### Repair F2 — six-port physical composition theorem

Define composition compatibility from exterior component incidence and prove the star/exit/forced-pair trichotomy.

### Repair F3 — ordered-sheet transport theorem

Give the transition permutation on the two sheets for every cell and prove compatibility with the cap route and with concatenation.

### Repair F4 — labelled backtrack disc

Write the exact root-valued move sequence filling the `s-t-s` bigon and prove literal boundary equality.

### Repair F5 — preservation ledger

For every macro, provide a table mapping every retained datum from input to output.

## 10. Downstream impact

Until E1 and F1–F5 are supplied:

- the standard one-atom state alphabet is not exhaustive;
- the nonbranching physical Petersen track is not proved;
- R2.6 cannot assume every singular component is a standard track with source-faithful cells;
- R2.7 cannot consume literal full-labelled seam equality;
- the cap-return and global five-CDC synthesis remain unassured.

**Dependency verdict:** `MATERIAL CORE GAP — NO 5-CDC ACCEPTANCE`.
