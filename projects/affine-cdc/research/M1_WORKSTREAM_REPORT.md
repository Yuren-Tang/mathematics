# M1 workstream report — outer shell

**Conversation / worker:** AffineCDC — M1 Outer Shell  
**Direct supervisor:** AffineCDC — Director  
**Repository:** `Yuren-Tang/mathematics`  
**Owned branch:** `research/affine-cdc-outer-shell-v1`  
**Lifecycle result:** stopped at theorem-level closure

## 1. Revision boundary

- **Base SHA:** `749e0579581fcc838685138b3582f4de306b8e72`
- **Final mathematical-content SHA:** `10d25b93a44a25c99ed3bf4c50e697eedb2196e0`
- **Report-bearing branch head:** the commit containing this report; its exact SHA is supplied in the supervisor handoff because a Git commit cannot contain its own SHA.
- **Canonical files modified:** none.
- **New files:** `OUTER_SHELL_RESEARCH_V1.md` and this report only.

The branch was created from the exact required base. The research commit adds the theorem-level mathematical dossier without changing the approved public Statement or any canonical chapter.

## 2. Mathematical claims established

1. **Exact outer-shell existence.** Every loopless bridgeless multigraph with finite active edge set has a finite loopless cubic bridgeless port-cycle expansion `H`, exact collapse data `(π, λ)`, and a nowhere-zero `F₂³`-flow on `H`.
2. **Explicit expansion.** Vertices of `H` are incidence ports `(v,e)`; original edges become inter-fibre edges; each active vertex fibre is a cycle, with degree two represented by two parallel internal edges; isolated vertices have empty fibres.
3. **Exact size bounds.** The expansion can be chosen with `|V(H)| = 2|E(G)|` and `|E(H)| = 3|E(G)|`.
4. **Preservation of bridgelessness.** Internal edges have alternate routes within fibre cycles. Every lifted original edge has an alternate lifted route because its endpoints remain connected after deleting the original edge.
5. **Exact flow input.** Seymour's nowhere-zero six-flow theorem, followed by the monotonic implication `6-flow => 8-flow` and Tutte's equivalence for abelian groups of order eight, supplies the required nowhere-zero `F₂³`-flow.
6. **No simultaneous construction required.** The valid dependency is expansion first, global flow second. The expansion is independent of the flow.
7. **Sufficient weak output.** The outer shell need transport only a multiset cut-even double cover. Exact coverage and cut parity survive projection; circuit decomposition can be deferred until after collapse.
8. **Finiteness separated.** Active-edge finiteness supplies finite active vertices, finite cyclic orders, and a finite expansion. Cut transport needs support finiteness; ambient vertex and edge carriers need not be finite.
9. **Low-degree analysis.** Degrees zero, one, two, and three are treated explicitly; any fixed local binary flow extends across every fixed cycle order through degree seven.
10. **High-degree obstruction criterion.** For an ordered degree-`d` star with incident values `a_i`, a flow extends over its cycle gadget exactly when the proper prefix sums do not exhaust `F₂³`.
11. **Sharp fixed-order failure.** A degree-eight two-vertex eight-parallel-edge example with Gray-tour differences has prefix sums equal to all of `F₂³`, so the fixed flow does not extend over that fixed cyclic order.

## 3. Claims refuted

- Every preselected nowhere-zero `F₂³`-flow extends over every preselected port-cycle expansion.
- Expansion and flow may be freely constructed in either order without additional compatibility work.
- Connectedness may be imposed on the source or expansion without loss of generality.
- The collapse vertex map should be required to be surjective when isolated ambient vertices are allowed.
- Any connected cubic replacement gadget preserves bridgelessness.
- Upstairs circuits project circuit-by-circuit to downstairs circuits.
- Projected supports must remain nonempty or pairwise distinct.
- Active-edge finiteness implies ambient-carrier finiteness.

## 4. Assumptions and obligations not resolved

1. The current Mathlib/companion environment was not audited for a formal theorem already implementing the exact `BinaryEightFlow` interface.
2. The precise connectedness, loop, and parallel-edge conventions in the chosen formal source for Seymour and Tutte must be audited before formal import or axiomatization.
3. No Lean implementation of the port-cycle graph, cyclic successor choices, two-cycle edge objects, or active-edge API was attempted.
4. The graph-level multiset even-double-cover predicate and theorem are still not named in the companion formalization.
5. The cut-even/vertex-even bridge and pure collapse transport remain paper-level rather than machine-checked.
6. Loop deletion, singleton-loop reinsertion, and the public Statement migration remain outside M1 as directed.

## 5. Proposed promotions to canonical chapters

After Director review, promote the following spine, without editing the public Statement in the same change:

1. `active_degree_ge_two`;
2. `exists_port_cycle_expansion`;
3. `port_cycle_expansion_bridgeless`;
4. `binary_eight_flow` as an exact isolated classical interface;
5. `exists_affine_outer_shell`;
6. `project_cut_even_double_cover`;
7. `outer_shell_to_cut_even_double_cover`.

The canonical outer-shell chapter should terminate at a cut-even double cover of the loopless original core. Final circuit decomposition and loop reinsertion should remain separate generic nodes.

## 6. Recommended next workstream

**Recommended workstream:** `M2 — BinaryEightFlow interface and convention audit`.

Its bounded objective should be to select an exact formal theorem boundary for the classical flow input, verify multigraph and disconnected-component conventions, determine whether Mathlib already supplies any usable portion, and return a declaration-level specification. It should not begin formalizing Seymour's theorem unless the Director explicitly changes scope.

Only after that interface is approved should a Lean engineering workstream implement the port-cycle expansion and collapse data.

## 7. Higher possibility found

**Yes, but not pursued after closure.** Proposition 6.1 suggests an adaptive-ordering question: given a zero-sum multiset of nonzero elements of `F₂³`, can its terms always be cyclically ordered so that the proper prefix sums omit at least one group element? A positive answer would allow a preselected downstairs binary flow to determine a compatible port order and extend to the expansion. The degree-eight counterexample refutes only arbitrary fixed order, not adaptive order.

This possible strengthening is unnecessary for the closed outer shell, makes no current theorem claim, and should be proposed as a separate child workstream rather than silently added to M1.

## 8. Stop reason

The workstream stops because the requested expansion-flow-collapse package has a theorem-level closure with exact dependencies, while the principal tempting overstrong formulation has a decisive degree-eight counterexample. Further work would be formal engineering, source-interface audit, or a new strengthening rather than completion of M1.
