# AC-5CDC-AUDIT-SHELL-01 — end-to-end theorem-interface map

**Fixed candidate:** `1f57422e0e415d8902d56eb294183815c0a0b640`  
**Scope:** exported interfaces from contextual return through the cubic induction and general finite bridgeless outer shell.

## 1. Shortest claimed route

\[
R0\to R1\to R2.1\to R2.2\to R2.3\to R2.4\to R2.6\to R2.7
\to Q_N\to P_N\to\text{outer shell}.
\]

| Node | Required export | Immediate consumer | Interface audit | Status |
|---|---|---|---|---|
| `R0` | Five indexed vertex-even supports with exact multiplicity two `iff` root-valued `E_5` flow on loopless cubic graph | `R1/R2` root-flow proof | No distinctness or nonemptiness premise on supports | `ACCEPT` |
| `R1` | At each simple edge, one valid smaller cross closure; theta exact base | `P_N` | One selected cross suffices; all-three reconnection theorem unnecessary | `ACCEPT` |
| `R2.1` | `J_j={A,B_j,C_j}`, `K_i`, unique immediate intersection, route rows, unique original-cap blocked route | cap consumer and locked descent | Independent finite recomputation agrees | `ACCEPT` |
| `R2.2` | Finite selected current-flow history of root NNIs/cancellations or declared terminal | R2.3--R2.7 | Internal Morse proof belongs to core audit; exported finiteness assumed here only for interface attack | `OUT OF SCOPE / DEPENDENCY NOT ASSURED` |
| `R2.3` | One normalized zero/co-root first-failure atom and bounded local grammar | R2.4/R2.6 | Internal local-confluence proof belongs to core audit | `OUT OF SCOPE / DEPENDENCY NOT ASSURED` |
| `R2.4` | One complete-labelled nonbranching physical track retaining cap/route/darts | R2.6 | Internal physical-backbone proof belongs to core audit | `OUT OF SCOPE / DEPENDENCY NOT ASSURED` |
| `R2.6` | Boundary-preserving erasure/rootification of every normalized closed/open/periodic track in scope | R2.7 | Internal seam theorem belongs to core audit | `OUT OF SCOPE / DEPENDENCY NOT ASSURED` |
| `R2.7` | Every cap-compatible descendant terminal returns to original cap context, or an exactly consumed exit; recursive child calls retain inherited-flow histories | `Q_N` | Direct terminal is introduced by unrelated recolouring; generic exits remain disjunctive | `BLOCKED-PROOF` |
| `Q_N` | For every specified inherited selected-cross flow, a finite decorated history from that flow to a cap-compatible solution, or a fully consumed proof exit | `P_N`; nested bubble compression | Direct terminal does not start from inherited labels; not every exit has an exact root-flow consumer | `BLOCKED-PROOF` |
| `P_N` | Every connected loopless bridgeless cubic graph of order at most `N` has a root flow | outer shell | Phase order is noncircular, but same-level `Q_N` premise is unavailable | `BLOCKED-PROOF` |
| Outer shell | Cubic theorem implies finite bridgeless multigraph `5`-CDC with at most five members | headline theorem | Port-cycle expansion and memberwise collapse are sound | `ACCEPT` |
| Headline | Every finite bridgeless multigraph has a `5`-CDC | AC-DIR / synthesis | Upstream `Q_N/P_N` break prevents conclusion | `BLOCKED-PROOF` |

## 2. Exact cap-consumer case tree

Starting from one specified selected-cross flow:

\[
\sigma\in J_j=\{A,B_j,C_j\}.
\]

### Branch B — immediate intersection

\[
B_j\in J_j\cap K_i
\Longrightarrow
\text{root-valued cap insertion}
\Longrightarrow
\text{one global }S_5\text{ alignment}
\Longrightarrow
\text{solution}.
\]

**Interface:** closed.

### Branch A/C — separating rescue

\[
\text{separating nonoriginal route}
\Longrightarrow
K_i\text{ state on the original four-pole}
\Longrightarrow
\text{global }S_5\text{ alignment}
\Longrightarrow
\text{solution}.
\]

**Interface:** closed, conditional on the physical separating-channel theorem.

### Branch A/C — locked original route

\[
\text{fixed }M_i\text{ descent}
\Longrightarrow
\begin{cases}
\text{descendant route change},\\
\text{direct matching},\\
\text{connected cancellation child},\\
\text{disconnected cancellation},\\
\text{other declared exit}.
\end{cases}
\]

- **Descendant route change:** correctly sent through R2.7 before original-profile gluing.
- **Connected child:** correctly formulated as a lower inherited `Q` call, but requires every child terminal to return a witnessed history.
- **Disconnected child:** standard cyclic two-cut branch.
- **Direct matching:** blocked by inherited-flow discontinuity.
- **Other declared exit:** blocked until an exhaustive consumer ledger is supplied.

## 3. Direct-terminal interface failure as a commuting-diagram failure

The candidate needs a commuting diagram

\[
\begin{array}{ccc}
(G_j,\lambda) & \xrightarrow{\text{declared forward history}} & (E_r,\lambda_r)\\
\downarrow Q_N && \downarrow\text{terminal closure}\\
(G,\Lambda) & \xleftarrow{\text{contextual inverse transfer}} & (\Theta,\tau)
\end{array}
\]

where `tau` is connected to the inherited terminal assignment `lambda_r` by declared moves and the complete terminal boundary data agree.

What is proved is only

\[
\exists\tau\;[\tau\text{ is a root flow on the unlabelled terminal theta}],
\]

obtained by assigning an arbitrary root triangle or newly chosen intersecting loop roots.  The missing arrow is

\[
(E_r,\lambda_r)\rightsquigarrow(\Theta,\tau).
\]

Without that arrow the lower `Q` call does not return the witness required by the stored parent cancellation, so the diagram does not commute in the complete labelled contextual category.

## 4. Quantifier ledger

| Statement | Needed quantifier | Frozen candidate actually establishes |
|---|---|---|
| Selected cross | For each simple edge, there exists one valid cross | Correct |
| Initial flow | For every specified root flow on that selected cross | Correctly stated |
| Boundary trichotomy | For the boundary induced by that specified flow | Correct |
| Direct terminal | A cap-compatible terminal reachable from the inherited terminal flow | Only existence of some root flow on the same terminal graph |
| Child recursion | Every inherited child flow returns a decorated history | Fails on direct-terminal child branch |
| Accepted exits | Every exit disjunct implies a root flow on the current original graph | Not exhaustively stated or proved in the controlling route |
| `Q_N` | Universal in specified inherited flow | Not proved |
| `P_N` | Existential root solubility for every cubic graph | Cannot be derived without `Q_N` |
| Outer shell | If cubic theorem, then general finite bridgeless theorem | Correct |

## 5. Graph-category ledger

| Transition | Source category | Target category | Audit note |
|---|---|---|---|
| R1 deletion/reconnection | connected loopless bridgeless cubic | same, order `N-2` | one cross exists |
| Root NNI | complete labelled current context | same order/category or explicit exit | core dependency |
| Equal-face cancellation | connected loopless bridgeless cubic | connected lower child, or cyclic two-cut exit | child fidelity interface acceptable |
| Direct terminal cap closure | zero-source four-pole | theta or loop-bridge singular graph | topology census correct; inherited labels not respected |
| Port expansion | loopless bridgeless multigraph, min active degree two | loopless bridgeless cubic multigraph | sound, including degree two |
| Collapse | cubic support family upstairs | even support family on loopless core | cut correspondence exact |
| Loop reinsertion | loopless-core cover | cover of original multigraph | exact multiplicity retained |

## 6. Hidden-choice ledger

- Choosing one valid cross: harmless existential choice; finite graph, no canonical choice needed.
- Choosing one root flow on the smaller cross via `P_{N-2}`: harmless at top level because `Q_N` is universally quantified over the specified choice.
- Choosing the finite strategy/macro at each state: harmless if the no-sink rank and complete state relation are proved.
- Choosing one trace-matching permutation: harmless; one finite `S_5` permutation is applied globally.
- Choosing new root labels at the direct terminal: **not harmless**; it changes the specified inherited flow and lacks a history witness.
- Declaring a generic state an accepted exit: **not harmless** unless an exact theorem consumes that flag to a root flow in the current original context.

## 7. Final interface conclusion

The outer shell is a valid conditional theorem.  The cubic induction is a valid conditional skeleton.  The condition actually needed is the universal witnessed extension proposition `Q_N`; the frozen cap consumer does not prove it.  Hence the endpoint theorem is not assembled.