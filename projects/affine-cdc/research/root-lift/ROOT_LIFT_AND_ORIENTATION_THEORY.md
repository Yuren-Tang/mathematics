# Root-lift and orientation theory

## Status and assurance

This chapter normalizes the authorial root-lift package at `81da79782da348fac629b42882e447f95e4c9d3a`. Its units are

`AUTHORIAL / CURATOR-INTEGRATED / READY FOR INDEPENDENT REVIEW`.

Statements comparing with `ω` or `Ω_f` inherit only the frozen OR1 assurance. This chapter creates no new independent or Lean assurance and no novelty or priority claim.

## 1. Five levels of data

1. **Full witness:** indexed circuit occurrences, cyclic orders and multiset occurrence identity.
2. **Directed support word:** one balanced directed edge support for each index.
3. **Integral root flow:** the type-`A` encoding of the directed support word.
4. **Binary unordered root flow:** mod-two indexed supports and unordered complete-graph roots.
5. **Family quotient:** after fixing a reconfiguration torsor, the quotient of a fixed-lift obstruction by the accessible motion image.

Only levels 2 and 3 are canonically equivalent. Passing from level 1 loses circuit partition and occurrence identity; passing to level 4 loses integral signs; level 5 changes the existential quantifier.

## 2. Root-flow definition and canonical equivalence

Fix an index set of size `q` and a reference orientation of each source edge. A type-`A_{q-1}` root flow assigns to every edge a root `ε_i-ε_j` so that the signed incidence sum vanishes at each vertex. Reversing the reference orientation changes both incidence sign and root sign, so the object is reference-independent.

The canonical theorem is

> directed indexed Eulerian `q`-support systems `↔` type-`A_{q-1}` root flows.

A full oriented `q`-CDC is obtained only after choosing a directed circuit decomposition in each coordinate. Such a decomposition exists for finite directed Eulerian supports but is generally nonunique.

## 3. RL-1–RL-14 normalized table

| ID | Normalized statement | Status |
|---|---|---|
| RL-1 | Reference-edge reversal preserves the type-`A` root-flow object. | proved, authorial |
| RL-2 | Directed indexed Eulerian supports and type-`A_{q-1}` root flows are mutually inverse at support-word level. | proved, authorial |
| RL-3 | A finite root flow yields some full oriented `q`-CDC after coordinatewise directed circuit decomposition. | proved existence; decomposition noncanonical |
| RL-4 | A root flow canonically recovers a prescribed full circuit witness. | false; four-parallel-edge counterexample |
| RL-5 | Multiplicity two, distinct indices, repeated supports and empty indices survive at support-word level; circuit partitions and occurrence names do not. | proved, authorial |
| RL-6 | Mod-two root flows, unordered `K_q` roots and indexed even supports are equivalent at unordered support level. | proved, authorial |
| RL-7 | For even `q`, the nondegenerate binary target is `E_I/<1>` of dimension `q-2`. | proved, authorial |
| RL-8 | At `q=4` complementary roots collide in the quotient; for even `q≥6` weight-two root labels remain distinct. | proved, authorial |
| RL-9 | A prescribed full unoriented witness has an opposite-direction sign lift iff its occurrence twist word is a cut. | proved, authorial |
| RL-10 | Fixed support without a prescribed circuit decomposition has one canonical occurrence obstruction. | false in general |
| RL-11 | The generic occurrence class is literally `ω(g)`. | false as an object identity; gauges differ |
| RL-12 | For a retained affine-face event, occurrence sign lifting and `ω(g)=0` test the same event. | scope-split comparison; inherits OR1 assurance |
| RL-13 | A generic fixed-witness obstruction is literally the fixed-fibre `Ω_f`. | false; family quantifier differs |
| RL-14 | In the frozen Fano fibre, some compatible integral sign lift exists iff `Ω_f=0`. | scope-split specialization; inherits OR1 assurance |

## 4. Exact information-loss counterexample

On the two-vertex graph with four parallel edges, the same balanced directed support word admits distinct pairings into circuit occurrences. Both pairings produce the same root flow. Therefore a root flow cannot canonically recover a prescribed circuit partition or full witness.

This refutes RL-4 and guards RL-3: decomposition is an existence step, not an inverse equivalence at full-witness level.

## 5. Prescribed-witness obstruction

For a prescribed full unoriented witness `W`, form the occurrence adjacency multigraph `H_W`: vertices are circuit occurrences and source edges become adjacency edges. Preliminary circuit orientations define a twist cochain

`t_W ∈ C^1(H_W;F_2)`.

Reversing an occurrence adds a cut. Hence

> `W` has an opposite-direction sign lift iff `[t_W]=0` in `C^1(H_W;F_2)/Cut(H_W)`,

or equivalently iff `t_W` annihilates every cycle of `H_W`. When nonempty, the set of sign choices is an affine torsor under componentwise global reversals.

This is the generic fixed-witness obstruction. It is not automatically a source-graph cohomology class.

## 6. Fixed witness, fixed lift, and fixed fibre

These three quantifiers must remain distinct.

- The occurrence criterion tests one prescribed circuit witness.
- `ω(g)` tests orientability of one retained compatible affine lift, using source-graph vertex-disc gauge.
- `Ω_f` tests whether some lift in a fixed compatible-lift fibre succeeds after quotienting by accessible affine/Petrial motion.

Thus

`fixed witness ≠ fixed lift ≠ fixed fibre`.

RL-12 compares two descriptions of the same fixed event without asserting a bare quotient-space identity. RL-14 is only the frozen Fano-fibre specialization.

## 7. The q=5 specialization

| ID | Statement | Status |
|---|---|---|
| RL5-1 | A type-`A_4` root flow is a directed indexed five-support word. | proved, authorial |
| RL5-2 | Mod-two reduction gives the `R_5 ↔ K_5 triangles ↔ O^-(4,2)` unordered hierarchy. | proved, authorial plus frozen binary model |
| RL5-3 | Quadratic, Schur, cographic and stress formulations retain integral orientation signs. | false |
| RL5-4 | After one global identification of support indices with `F_5`, every `A_4` root flow projects to a nowhere-zero `F_5` flow. | proved, authorial |
| RL5-5 | An arbitrary fixed nowhere-zero `F_5` flow canonically reconstructs an oriented five-support witness. | open/too strong as stated |

The projection is one-way. A converse requires ordered pair labels satisfying all five coordinate equations; local coefficient charts may also carry transport holonomy. No equivalence with arbitrary nowhere-zero five-flows is claimed.

## 8. The q=8 specialization

The safe one-way hierarchy is

`A_7 -> E_8 -> E_8/<1> ≅ O^+(6,2) -> F_2^3`.

| ID | Statement | Status |
|---|---|---|
| RL8-1 | The displayed integral/binary/orthogonal/Fano hierarchy is well-defined; reverse arrows are not automatic. | proved, authorial plus frozen binary model |
| RL8-2 | The compatible-lift torsor reduces family sign search to a linear quotient. | comparison inheriting frozen OR1 gauge package |
| RL8-3 | Fano or orthogonal compatibility forces every lift to be orientable. | false; exact frozen `K_4` fibre has both types |
| RL8-4 | Every fixed Fano fibre has vanishing `Ω_f`. | open |

The Fano structure makes family search linear and computable; it does not force vanishing.

## 9. Open provider and lift questions

1. Does every fixed Fano fibre have `Ω_f=0`?
2. If not, does every relevant graph admit some Fano flow whose compatible-lift fibre has a vanishing member?
3. Which fixed nowhere-zero `F_5` flows lift to type-`A_4` root flows?
4. Can the occurrence obstruction and `ω(g)` be compared functorially through a complete cellular chain complex?
5. What reconfiguration quotient replaces the Fano affine torsor for general `q`?
6. Which primitive provider theorems turn the local sign-lift interfaces into graph-level existence results?

These are research questions, not proof-development omissions that may be silently assumed.

## 10. Assurance boundary

- The root-flow equivalences and counterexamples are authorial and await independent review.
- OR1 comparisons do not upgrade the underlying frozen orientation package.
- No universal fixed-fibre vanishing is proved.
- No arbitrary `F_5` converse lift is proved.
- No root-lift statement proves the open five-support theorem.
- The bounded literature search supports terminology and synthesis only, not novelty, priority or publication readiness.

Canonical detailed sources remain the files in this directory and the exact theorem/scope units under `math.graph-theory.flows.indexed-oriented-supports.*`.