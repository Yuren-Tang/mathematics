# AC-5CDC-AUDIT-SHELL-01 — outer-shell definition/projection ledger

**Unit:** L — general finite bridgeless outer shell  
**Classification:** `ACCEPT`

| Obligation | Candidate construction | Independent check | Disposition |
|---|---|---|---|
| Standard object | A cycle is an even subgraph; a `5`-CDC has at most five members and covers every edge twice | This is the standard CDC convention.  Connected circuit decomposition is not part of the member count | `ACCEPT` |
| Indexed versus at most five | Work with five indexed supports | Empty supports may be omitted; repeated supports are repeated collection members.  No increase beyond five | `ACCEPT` |
| Disconnected cubic graph | Apply connected cubic theorem to each component using common indices `1,...,5`; union by index | Vertex parity and exact edge multiplicity are componentwise | `ACCEPT` |
| Loop deletion | Delete every loop to form `G_0` | Loops cross no cut.  Any nonloop bridge of `G_0` would be the same bridge in `G` | `ACCEPT` |
| Active degree lower bound | Expand every active vertex of nonloop degree `d>=2` | A vertex with exactly one nonloop incidence would make that edge a bridge; loop deletion may leave isolated vertices only | `ACCEPT` |
| Degree `d>=3` fibre | Replace incidences by ports joined in a `d`-cycle | Every port receives two internal incidences and one external incidence | `ACCEPT` |
| Degree `d=2` fibre | Join the two ports by two distinct parallel internal edges | This is a valid two-cycle in a multigraph; each port has internal degree two | `ACCEPT` |
| Parallel original edges | Each original edge occurrence becomes its own external edge | Distinct edge objects remain distinct; no simplicity assumption is introduced | `ACCEPT` |
| Looplessness upstairs | External edges come from nonloops; fibre edges join distinct ports | No auxiliary loop is created, including at degree two | `ACCEPT` |
| Cubicity upstairs | One external plus two internal incidences at every port | Degree is exactly three, with multiplicity counted | `ACCEPT` |
| Internal-edge bridgelessness | Every fibre edge lies on its fibre cycle | Includes both edges of a degree-two parallel pair | `ACCEPT` |
| External-edge bridgelessness | Lift a closed trail/circuit of `G_0` containing the original nonbridge edge and connect successive ports within fibres | Every external edge lies on a closed trail upstairs and hence is not a bridge | `ACCEPT` |
| Cubic theorem application | Apply five-support theorem to every edge-bearing component of `H` | All components satisfy finite, loopless, bridgeless, cubic hypotheses | `ACCEPT` |
| Vertex-even implies cut-even | Use the mod-two degree sum over a vertex set | For every support, the parity of a cut equals the sum of support degrees on one shore | `ACCEPT` |
| Exact cut correspondence | For `S subseteq V(G_0)`, compare `delta_{G_0}(S)` with `delta_H(pi^{-1}S)` | External edges correspond bijectively; no fibre edge crosses a union of whole fibres | `ACCEPT` |
| Memberwise projection | Keep original edge `e` in downstairs member `i` iff its external lift lies in upstairs member `i` | Projection is defined separately for every common support index | `ACCEPT` |
| Downstairs evenness | Projected member is cut-even for all `S` | Taking singleton `S={v}` gives even degree at every loopless downstairs vertex | `ACCEPT` |
| Exact multiplicity two | Each original nonloop edge has one lifted external edge | The same two support indices are inherited exactly | `ACCEPT` |
| No support-count increase | Do not decompose members into circuits | Exactly the same five indices survive collapse | `ACCEPT` |
| Loop reinsertion | Add every deleted loop to two fixed members, say `1,2` | A loop contributes degree two and crosses no cut; it is then covered exactly twice | `ACCEPT` |
| Empty graph / isolated vertices | Ignore isolated vertices; use empty supports if there are no edges | All parity and multiplicity conditions are vacuous | `ACCEPT` |
| Pure-loop components | Loops are deleted to isolated vertices and then added to members `1,2` | Every loop is an even one-edge subgraph under multigraph degree convention and is double-covered | `ACCEPT` |
| Full graph category | Finite bridgeless multigraphs, possibly disconnected, with loops and parallel edges | Every case in the project convention is covered | `ACCEPT` |

## Proof capsule

Let `G` be a finite bridgeless multigraph.  Delete loops, expand each active vertex into its port cycle, and call the resulting loopless cubic graph `H`.  Each edge of `H` lies on a cycle: fibre edges lie on fibre cycles, while an external edge lifts a circuit through the corresponding nonbridge edge of `G_0`.  Apply the cubic five-support theorem componentwise.

For a support `F'_i` upstairs and a vertex set `S` downstairs,

\[
|F_i^0\cap\delta_{G_0}(S)|
=
|F'_i\cap\delta_H(\pi^{-1}S)|
\equiv0\pmod2.
\]

Thus `F_i^0` is vertex-even by singleton cuts.  Each nonloop original edge is represented by one external edge and therefore retains exact multiplicity two.  Add every loop to two fixed members.  The resulting family contains at most five even subgraphs and covers every edge twice.

## Nondefects worth stating explicitly

1. The degree-two fibre must be two parallel edges, not one edge; the candidate gets this right.
2. The projection need not choose paths through fibre cycles.  Cut parity alone is sufficient and avoids a memberwise routing problem.
3. Circuit decomposition would generally increase the number of cover members and is correctly avoided.
4. The use of one common five-index set over components is essential and is explicit.
5. The proof requires only the cubic theorem.  It does not repair or conceal any cap-consumer defect upstream.