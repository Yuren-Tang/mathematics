# Gauge torsors, partial Petrials, and horizontal flow motion

## 1. The two-level state space

Fix a finite cubic graph $G$. The total AffineCDC state space relevant to five supports consists of pairs

$$
(f,g),
$$

where $f$ is a nowhere-zero $\mathbf F_2^3$ flow and $g$ is a compatible root lift above it.

Projection to $f$ separates two fundamentally different motions:

1. **vertical motion:** change $g$ while keeping $f$ fixed;
2. **horizontal motion:** change $f$ by a nowhere-zero cycle switch and then solve the new root-lift problem.

A support-cycle pivot is a partially lifted horizontal move: it changes the Fano flow but preserves the underlying uncoloured cycle-face surface. It must not be confused with a vertical gauge move.

## 2. The fixed-flow gauge torsor

For one Fano flow $f$, compatible root lifts form an affine torsor under the homogeneous compatibility space $H_f^0$. Quotienting global support translations gives the reduced gauge code

$$
B_f\subseteq\mathbf F_2^{E(G)}.
$$

A gauge word records on which source edges the two incident support sides are exchanged.

### Theorem 2.1 — piecewise translation form

Every homogeneous gauge difference can be represented by vertex translations that are constant on suitable source regions. Across an edge of direction $h$, the endpoint translations differ by either $0$ or $h$. The binary edge word recording the latter case is the gauge codeword.

### Theorem 2.2 — gauge/Petrial correspondence

Under the cycle-face surface interpretation, a reduced gauge word is exactly an admissible partial Petrial:

- bit $0$: preserve the two face-side identifications across the source edge;
- bit $1$: swap the two face sides.

Thus the fixed-flow root-lift fibre and the code-filtered partial-Petrial orbit are the same object.

## 3. Three distinct operations

The programme uses three transformations with different invariants.

### 3.1 Support-cycle pivot

Choose one support-cycle component of old support colour $c$ and translate its colour to $d$. The uncoloured surface and dual triangulation remain fixed, while the old eight-colouring changes. The projected Fano flow generally changes.

### 3.2 Gauge/Petrial move

Choose $\lambda\in B_f$. The Fano flow remains fixed; the edge-side matching changes; hence the embedding, face circuits, and dual triangulation may change.

### 3.3 Connected-cycle flow switch

Choose a connected binary cycle $C$ and a nonzero direction $a$ absent from the switched edges. Set

$$
f'(e)=f(e)+a1_C(e).
$$

This is one edge in the nowhere-zero Fano-flow reconfiguration graph.

A disconnected binary-cycle switch is the commuting composition of the switches on its connected components. It is a path in the reconfiguration graph, not one adjacency.

## 4. The horizontal base as an arrangement complement

The full space of $\Gamma$-valued flows is

$$
\operatorname{Flow}(G;\Gamma)
\cong
Z_1(G;\mathbf F_2)\otimes\Gamma.
$$

For every source edge $e$, evaluation is linear. Nowhere-zero flows form the complement

$$
\operatorname{NZFlow}(G;\Gamma)
=
\operatorname{Flow}(G;\Gamma)
-
\bigcup_{e\in E(G)}\ker\operatorname{ev}_e.
$$

Connected-cycle switches are the rank-one tensor moves

$$
z\otimes a.
$$

Thus both levels have finite-field arrangement geometry:

- vertical bad certificates form affine-subspace arrangements in $B_f$;
- horizontal flow states form an arrangement complement in $Z_1(G)\otimes\Gamma$.

The unresolved theorem concerns transport between these two levels.

## 5. Internal and external switch directions

Fix a plane $W\le\Gamma$ and its fixed-plane obstruction.

### 5.1 Internal switch

If the switch direction $t$ lies in $W$, then membership in $W$ is preserved. The quotient $Q_W$ remains fixed, and the switch changes the Schur/component defect linearly.

Delete the dangerous colour matching $A_t=f^{-1}(t)$ and contract the components of $G_W-A_t$ to obtain a refined quotient $R_{W,t}$. The outside colours split its edges into $R_0,R_1$.

### Theorem 5.1 — exact internal correction image

The possible defect changes under admissible $t$-switches are

$$
\boxed{
\operatorname{Im}\Delta_{W,t}
=
q_*\bigl(\mathsf B(R_1)\cap\mathsf B(R_0)\bigr),
}
$$

where $\mathsf B(R_i)$ is the binary boundary space and $q_*$ sums over the fibres of the refinement map to $Q_W$.

The dual annihilator consists of quotient functions whose pullback is the sum of one function constant on $R_0$ components and one constant on $R_1$ components.

This is a complete linear theorem for one fixed internal direction.

### 5.2 External switch

If $t\notin W$, the switch changes which edges lie in the slicing plane. The old quotient is not preserved. Nevertheless, the projected four-flow or Schur word may be transported to a newly selected plane.

An external switch is therefore a **reslicing operation**, not a correction within one fixed quotient.

### Dichotomy

$$
\boxed{
\begin{array}{c|c}
t\in W&\text{linear syndrome correction on fixed quotient},\\
t\notin W&\text{reslice while preserving lower-rank flow data}.
\end{array}
}
$$

## 6. Root-admissible switching and finite-state obstruction

A linear correction in the projected quotient need not lift through the finite root fibres. The root-admissible problem has a precise local-to-global form.

For each edge, the quotient value has a finite set of root preimages. At each cubic vertex, allowed triples are those summing to zero. A global corrected root lift is a section of this finite constraint system.

Failure can appear at three levels:

1. an empty edge fibre;
2. nonempty edge fibres but an empty vertex relation;
3. locally nonempty relations with nontrivial component holonomy.

In the genuine rainbow-switch branch, the unrestricted four-valued tension universe collapses to the much smaller Tait-resolution system developed in the holonomy chapter.

## 7. Marked-core occurrence and reserve codes

Let $\mathcal C$ be a marked family of exact face circuits in one gauge state. Its face zone $Z_{\mathcal C}$ is the union of traversed source edges and its reserve is

$$
R_{\mathcal C}=E(G)\setminus Z_{\mathcal C}.
$$

The occurrence direction is the shortened gauge code

$$
L_{\mathcal C}=B_f\cap\mathbf F_2^{R_{\mathcal C}}.
$$

Therefore:

- $L_{\mathcal C}=0$: the marked core is private to one gauge state;
- $\dim L_{\mathcal C}=1$: the core persists on a line;
- higher dimension: the occurrence locus is a larger affine subspace.

This theorem applies to clique cores, common-neighbour chromatic cores, and every other finite certificate described by marked face circuits.

## 8. Renewal modules

Finite fibres can be covered by obstruction cosets even when no individual certificate is rigid.

### 8.1 Three-cube module

Some fixed-flow fibres contain an eight-state affine cube in which each state has one private obstruction core. The cube is controlled by a three-dimensional gauge quotient.

### 8.2 Six-cube module

A larger sixty-four-state module has point renewal together with redundant line directions. Its essential quotient separates genuinely distinct obstruction motion from invisible gauge directions.

### 8.3 Structural interpretation

These modules are exact finite models of vertical renewal. They do not prove that arbitrary fixed-flow fibres have cube structure, and they are not graph-level counterexample atoms.

The thirty-vertex source graph carrying them is explicitly three-edge-colourable and hence has a three-support cycle double cover through another flow.

## 9. Fixed lift, fixed flow, and graph level

Let

$$
\mathfrak B(G)
$$

be the set of nowhere-zero Fano flows whose entire compatible root-lift fibre is bad.

Then:

- a bad lift is one obstructed state;
- a bad fixed flow lies in $\mathfrak B(G)$;
- a graph has no five-support cover only if every nowhere-zero Fano flow lies in $\mathfrak B(G)$.

Conversely, a five-support cover determines a Fano projection and a compatible good lift, so graph-level failure is equivalent to

$$
\mathfrak B(G)=\operatorname{NZFlow}(G;\mathbf F_2^3).
$$

This quantifier distinction controls every laboratory interpretation.

## 10. Calibrating laboratories

### 10.1 Thirty-vertex graph

- graph-level easy: explicit three-edge-colouring;
- fixed-flow hard: large wholly bad fibres and renewal cubes;
- horizontal boundary large: most connected-cycle neighbours expose a good state.

### 10.2 Petersen graph

All $28560$ Fano flows are classified. Every flow has a good compatible lift:

$$
\mathfrak B(P)=\varnothing.
$$

Some fibres contain one bad projective-plane $K_6$ state, but gauge motion escapes to torus or Klein-bottle $K_5$ states. The full connected-cycle flow graph is connected, yet horizontal motion is unnecessary for existence.

### 10.3 Flower snark $J_5$

A displayed flow has a wholly bad two-state fibre renewing between a $K_6$ state and a $K_6$-free $K_2\vee W_5$ state. Nevertheless, most one-step connected-cycle neighbours have a good lift. Thus bad flows exist, but the displayed bad flow is not horizontally trapped.

These laboratories distinguish three logically different phenomena; no one of them predicts the global theorem by itself.

## 11. Ideal target pivots and source dependence

If one ignores source realizability and performs the maximal target-side support pivot on the unused-root graph $U$, then every bad core of cover number two and the exceptional pentagon has an abstract one-step escape. The only ideal one-pivot traps are graphs with

$$
\tau(U)\le1,
$$

namely empty or one-star cores.

This theorem locates the remaining difficulty on the source side:

- the desired root may fail to be released by one connected source cycle;
- required leaves may lie on different components;
- a consumed root may destroy the witness;
- the necessary support-cycle component may not exist.

The ideal-pivot theorem belongs to the exact factorable subtheory. After the componentwise correction, it is a useful dynamical model but not a complete obstruction classification.

## 12. The natural global transport problem

The correct two-level object is a decorated reconfiguration system:

$$
\boxed{
\begin{array}{c}
\operatorname{NZFlow}(G;\Gamma)\\
\text{with rank-one connected-cycle edges}\\
\downarrow\\
\text{over each }f:\text{ gauge torsor }B_f\\
\text{decorated by marked-core affine arrangements.}
\end{array}
}
$$

The global theorem must prove one of:

1. some vertical or horizontal sequence reaches an uncovered good state;
2. every persistent bad component carries coherent transfer data forcing a cut, four-pole decomposition, bounded replacement, or other strictly smaller instance.

More finite neighbour counts cannot substitute for this transport/decomposition theorem.

## 13. Reliability boundary

The torsor/gauge description, partial-Petrial correspondence, face-transition model, occurrence-coset theorem, internal correction image, internal/external switch dichotomy, and flow-space arrangement description are theorem-level.

Renewal cubes, Petersen classifications, thirty-vertex counts, and $J_5$ neighbourhoods are exact finite computation. Ideal target pivots are exact target-side theorems with source realizability explicitly omitted. No result currently proves horizontal escape for every bad-flow component or excludes a graph for which every Fano flow is bad.