# AC-PD-5CDC EQ-RETURN 2 — partial root-flow extension reconnaissance and shortcut quarantine

**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**State:** `EXACT REFORMULATION / GENERIC REPAIR RETIRED / PRECEDENT NOTE RETAINED`.

---

## 1. The single-constraint partial-flow formulation

Cutting the two reconnecting edges after an equal-face cancellation gives four marked semiedges. Inverse insertion is possible whenever the two current edge roots form the orbit

\[
B=\{(z,w):z\ne w,\ |z\cap w|=1\}.
\]

Thus, for one lower-order graph `H` and two distinguished edges `e,f`, the following are equivalent.

1. Some root flow on `H` has `(lambda(e),lambda(f)) in B`.
2. Cutting `e,f` gives a four-pole extending some ordered word `(z,z,w,w)` in the `B` orbit.
3. The two-mark relative context is orbit-relatively `R_5`-extendable for the weld relation.

This equivalence is exact for the **single weld constraint**.

---

## 2. Why this does not close cancellation return

A lower-order contextual call must satisfy at least two logically different requirements.

1. **Weld requirement:** the two reconnecting edges lie in `B`.
2. **Outer terminal requirement:** the returned state is compatible with the outer cap/profile/route obligation.

Separate nonemptiness does not imply simultaneous nonemptiness.

Exact SAT enumeration on `K_(3,3)` gives:

- every unordered edge pair is individually `B`-attainable;
- there are eighty-one unordered pairs of individually attainable `B` constraints which no single root flow realizes simultaneously.

The triangular prism gives eighteen analogous incompatible pairs of individually attainable constraints.

Therefore no graph-independent Helly or support-permutation argument may infer

\[
\Sigma_{B}(e,f)\ne\varnothing,
\quad
\Sigma_{\rm outer}\ne\varnothing
\Longrightarrow
\Sigma_B(e,f)\cap\Sigma_{\rm outer}\ne\varnothing.
\]

A global support permutation preserves relation type but cannot force two disjoint profile subsets to meet.

---

## 3. Retired shortcut

The following proposed macro-step is not controlling:

1. discard the inherited post-cancellation flow;
2. invoke ordinary lower-order root-flow existence;
3. choose another flow satisfying the weld pair;
4. independently choose an outer cap-compatible terminal;
5. identify the two choices.

Step 5 is unjustified.

Accordingly the former Target 6.1, even if proved as a generic single-pair theorem, would not by itself imply marked-weld return.

---

## 4. What remains useful

### Partial-flow precedent

Hong-Jian Lai's partial nowhere-zero `4`-flow extension theorem, group-connectivity theory, and recent flow-critical work remain structurally relevant precedents. They show how prescribed local flow data may lead to:

- extension;
- finite exceptional contractions;
- connectivity-dependent obstruction classes.

They cannot be imported because the admissible set here is the nonlinear weight-two orbit

\[
R_5\subset E_5\setminus\{0\}.
\]

### Single-pair reconnaissance

Generic two-edge `B` attainability remains useful for:

- finite base classification;
- source reductions such as triangle contraction;
- testing proposed obstruction theorems;
- identifying when componentwise support relabelling is sufficient.

It is not the controlling global repair.

---

## 5. Controlling inherited-flow formulation

The canonical equal-face cancellation produces a **particular inherited root flow** on the lower-order graph for which the reconnecting pair already lies in `B`.

The correct return problem is:

> deform this inherited `B` flow along a specified finite lower-order cap-return history while tracking the ordered marked incidences and the outer terminal obligation.

Exactly one of the following may occur.

1. The pair remains in `B` and the intended inverse weld succeeds.
2. At the first `B` exit the pair becomes equal or disjoint, producing one ordinary zero/co-root atom on a strict shorter history prefix.
3. A route/profile event solves the outer cap before the weld relation is lost.
4. A source separator isolates the constraints and permits componentwise relabelling.
5. A marked central edge is consumed by a lower-order cancellation and enters the nested-frame mechanism.

This is the inherited-flow relative path theorem of the current RL frontier.

---

## 6. Relation to the PDL stack theorem

`AC_PD_5CDC_EQ_RETURN_5_NESTED_STACK_ORDER.md` proves abstract well-foundedness once every cancellation push stores a strictly smaller parent continuation and every failed `B` pop returns to a strict shorter prefix.

Thus the remaining concrete burden is not generic partial-flow extension. It is:

\[
\boxed{
\text{continuation-normalized local progress for the inherited marked return history}.}
\]

The first-`B`-exit and ordered-incidence overlap dossiers supply the local transition alphabet; the mixed-state local rank remains to be verified.

---

## 7. Exact status

### Retained

- equivalence between a single weld constraint and two-edge `B` attainability;
- partial-flow literature and analogy;
- finite pair-flexibility reconnaissance;
- triangle/bounded source reductions.

### Retired as a global repair

- generic prime two-edge flexibility as sufficient for `MWR`;
- separate-selection plus support-permutation arguments;
- any inference from individual profile nonemptiness to simultaneous attainability.

### Live

- inherited canonical `B` flow;
- first-`B`-exit strict prefix;
- ordered-incidence transport through `2--0` overlaps;
- nested continuation stack;
- route-aware relative return.

No marked-weld return, cap restoration or universal five-CDC theorem is claimed.