# Routing weights and the tree/holonomy dichotomy for four-pole obstructions

**Programme:** `AffineCDC — Research Lead`  
**Status:** theorem-level boundary-coordinate mechanism plus exact finite policy classification; not canonical pending Director review and literature audit  
**Parents:** `FIVE_CDC_FOUR_POLE_KEMPE_CLOSURE_V1.md`, `FIVE_CDC_CAP_KEMPE_PAIRING_ALIGNMENT_V1.md`, `FIVE_CDC_FOUR_EDGE_CAP_FORCING_KERNELS_V1.md`

## 1. Purpose

The ten boundary states

\[
\mathcal S=\{A,B_i,C_i,D_i:i=0,1,2\}
\]

were previously treated as a finite alphabet with cap-forcing and Kempe-closure rules. The cap-pairing theorem then showed that every Kempe transition is controlled by the terminal matching realized by one four-endpoint support-pair symmetric difference.

This packet lifts that local table to a higher structural level.

The main conclusions are:

1. the ten states have three intrinsic cut-parity coordinates;
2. a Kempe switch with routing matching `M_i` preserves exactly the `i`-th coordinate;
3. the fixed-routing transition graph is the disjoint union `P_3 \sqcup C_4 \sqcup P_3`;
4. a uniformly routed shore cannot occur in a vertex-minimal counterexample;
5. every one of the four previous minimal mismatch kernels carries a unique deterministic routing policy;
6. after quotienting by matching symmetry and shore exchange, the four policy pairs collapse to two dynamical types:

\[
\boxed{
P_5\mid P_5
\qquad\text{or}\qquad
P_4\mid C_3.
}
\]

The first is an acyclic unique-linkage type. The second contains a rainbow routing triangle and therefore a genuine holonomy loop.

Thus the next obstruction theory should not enumerate more boundary profiles. It should eliminate two coherent routing mechanisms.

## 2. Three perfect matchings and cut-parity weights

Let the four labelled terminals be `1,2,3,4`. Write the three perfect matchings as

\[
M_i=X_i\mid Y_i,
\qquad i=0,1,2,
\]

where `X_i,Y_i` are the two terminal pairs.

Let

\[
\sigma=(S_1,\ldots,S_5)
\]

be one indexed boundary signature. Each `S_r` is an even subset of the four terminals, and every terminal belongs to exactly two of the five traces.

Define

\[
q_i(S_r)
=
|S_r\cap X_i|\pmod 2
\]

and

\[
\boxed{
\omega_i(\sigma)
=
\frac12\sum_{r=1}^5q_i(S_r).
}
\]

The sum is even, because

\[
\sum_r |S_r\cap X_i|
=2|X_i|=4.
\]

Hence

\[
\omega_i(\sigma)\in\{0,1,2\}.
\]

The definition is invariant under permutation of the five support indices, so it descends to the support-unordered boundary state.

## 3. Exact coordinate theorem

### Theorem 3.1 — routing-weight coordinates

The map

\[
\Omega:\mathcal S\longrightarrow\{0,1,2\}^3,
\qquad
S\longmapsto(\omega_0(S),\omega_1(S),\omega_2(S))
\]

is injective. Its exact values are

\[
\begin{array}{c|c}
S&\Omega(S)\\
\hline
A&(0,0,0)\\
B_0&(0,1,1)\\
B_1&(1,0,1)\\
B_2&(1,1,0)\\
C_0&(0,2,2)\\
C_1&(2,0,2)\\
C_2&(2,2,0)\\
D_0&(2,1,1)\\
D_1&(1,2,1)\\
D_2&(1,1,2).
\end{array}
\]

#### Proof

Insert the canonical A/B/C/D boundary traces into the definition. The ten displayed vectors are distinct. ∎

Thus the ten-state alphabet is not an arbitrary list. It is a ten-point coordinate geometry inside the ternary cube.

## 4. A routing matching is a conserved coordinate

Consider a complementary support pair `a,b`, so that

\[
S_a\triangle S_b=\{1,2,3,4\}.
\]

Suppose its two terminal paths realize matching

\[
M_i=X_i\mid Y_i.
\]

A Kempe-path switch exchanges support names `a,b` on one block, say `X_i`.

### Theorem 4.1 — coordinate conservation

A switch routed by `M_i` preserves `\omega_i`.

#### Proof

The two switched traces are toggled by `X_i`. Since

\[
|X_i\cap X_i|=2,
\]

toggling by `X_i` does not change `q_i` for either trace. All other traces are unchanged. ∎

For `j\ne i`, every block of `M_i` meets `X_j` in one terminal, so the same switch flips the two relevant `q_j` bits. Hence routing by `M_i` is exactly the choice to conserve coordinate `\omega_i` while allowing the other two coordinates to move.

This supplies an invariant meaning for the routing label.

## 5. Fixed-routing transition geometry

Let `\mathcal G_i` be the graph on `\mathcal S` whose edges are all abstract Kempe transitions obtained when the terminal pairing is fixed to `M_i`.

Let

\[
\{i,j,k\}=\{0,1,2\}.
\]

### Theorem 5.1 — three routing sectors

The connected components of `\mathcal G_i` are exactly the three level sets of `\omega_i`:

\[
\omega_i=0:
\qquad
A-B_i-C_i,
\]

\[
\omega_i=1:
\qquad
B_j-B_k-D_j-D_k-B_j,
\]

and

\[
\omega_i=2:
\qquad
C_j-D_i-C_k.
\]

Consequently

\[
\boxed{
\mathcal G_i\cong P_3\sqcup C_4\sqcup P_3.
}
\]

The middle component is exactly the standard-cap set

\[
\boxed{
\mathcal K_i
=
\{B_j,B_k,D_j,D_k\}.
}
\]

#### Proof

Coordinate conservation places every edge inside one level set. The canonical boundary calculation gives the displayed edges, and each level set is connected. ∎

### Corollary 5.2 — two routing colours have no common nontrivial state invariant

For distinct `i,j`, the union

\[
\mathcal G_i\cup\mathcal G_j
\]

is connected on all ten states. Its diameter is four.

Thus any state set closed under the full transition actions of two distinct routing matchings is either empty or all of `\mathcal S`.

The unresolved obstruction cannot therefore be explained by a second global conserved coordinate. It must correlate route choice with the current cover and complementary support pair.

## 6. Uniform-routing elimination

Call a four-pole `P` **globally `i`-routed** if, in every indexed five-support boundary cover of `P`, every complementary support-pair symmetric difference realizes terminal matching `M_i`.

### Theorem 6.1 — uniform routing forces a full cap sector

If `P` is globally `i`-routed, then its complete boundary profile `\Sigma(P)` is a union of connected components of `\mathcal G_i`.

If, in addition, `P` is a shore of a cyclic four-edge cut in a vertex-minimal counterexample, then

\[
\boxed{
\mathcal K_i\subseteq\Sigma(P).
}
\]

#### Proof

Every abstract `M_i`-transition from a realized indexed cover is a genuine Kempe-path switch and therefore produces another cover of `P`. Repeating switches shows that `\Sigma(P)` is a union of `\mathcal G_i` components.

The two path components

\[
\{A,B_i,C_i\},
\qquad
\{C_j,D_i,C_k\}
\]

contain only one B/D matching index, namely `i`. Any union avoiding `\mathcal K_i` therefore has B/D index projection of size at most one. This contradicts cap forcing, which requires at least two matching indices. ∎

### Corollary 6.2 — no uniformly routed shore in a minimal counterexample

Let `P,Q` be the two shores of a cyclic four-edge cut in a vertex-minimal counterexample. Neither shore is globally `i`-routed for any `i`.

#### Proof

If `P` were globally `i`-routed, Theorem 6.1 would give `\mathcal K_i\subseteq\Sigma(P)`. Cap forcing on `Q` supplies a B/D state of some index different from `i`, and every such state lies in `\mathcal K_i`. Hence

\[
\Sigma(P)\cap\Sigma(Q)\ne\varnothing,
\]

contradicting the exact gluing obstruction. ∎

This is a genuine graph-theoretic elimination theorem. Uniform linkage routing is not a residual obstruction.

## 7. Kempe closure as a safety game

For one support-unordered boundary state, choose one orbit of complementary support pairs. This is the **challenge**. The actual shore paths select one of the three matchings `M_i`, and the corresponding Kempe switch produces one target state.

Hence the finite closure problem is a safety game:

1. the challenge selects a complementary trace-pair type;
2. routing selects which coordinate `\omega_i` is conserved;
3. the state moves to the corresponding target.

A Kempe-closed profile is precisely a state set in which routing has a memoryless strategy to remain after every challenge.

The abstract game permits routing to choose a new conserved coordinate independently at every state and challenge. A real four-pole is more rigid: all choices arise from one internal path geometry and one reconfiguration groupoid of indexed covers.

This is the exact location of the higher-level mechanism gap.

## 8. The four kernels have unique routing policies

Apply the exact routing table to the four minimal disjoint cap-forced Kempe-closed profile pairs from the previous packet.

### Computational Theorem 8.1 — policy rigidity

For every shore profile in every one of the four kernel representatives, and for every state/challenge belonging to that profile, exactly one of the three routing matchings keeps the transition inside the profile.

Therefore each minimal kernel shore carries a unique deterministic routing policy.

The four kernels are not four arbitrary state sets. They are four rigid finite automata.

### Computational Theorem 8.2 — two policy-pair orbits

Quotient the deterministic policy pairs by:

- simultaneous permutation of the three routing colours;
- graph isomorphism of each shore automaton;
- exchange of the two shores.

Exactly two dynamical types remain.

### Type T — tree routing

Both shore automata are five-vertex paths:

\[
\boxed{
P_5\mid P_5.
}
\]

Along either path, the edge-colour word is

\[
a\,b\,b\,a
\]

up to colour permutation and reversal.

This type is represented by the first previous kernel orbit.

### Type H — routing holonomy

One shore is a four-vertex path whose three edges have three distinct routing colours. The other shore is a triangle whose three edges also have three distinct routing colours:

\[
\boxed{
P_4\mid C_3.
}
\]

The triangle is a rainbow triangle.

The remaining three previous kernel orbits all collapse to this policy type.

Thus the four case list reduces to two mechanisms:

\[
\boxed{
\text{acyclic unique routing}
\quad\text{or}\quad
\text{minimal three-colour holonomy}.
}
\]

## 9. Boundary holonomy of the rainbow triangle

Choose the canonical rainbow triangle

\[
B_1\longrightarrow B_2\longrightarrow D_0\longrightarrow B_1
\]

with routing colours `0,1,2` in cyclic order.

At each edge there can be:

- two choices of path component to switch;
- and, where a trace is repeated, two choices of the actual support occupying that trace role.

Lift the three quotient transitions to ordered support signatures and compose the induced support-index identifications around the triangle.

### Computational Theorem 9.1 — nontrivial boundary monodromy

There are exactly sixteen resulting support-index monodromies. None lies in the stabilizer of the initial ordered boundary signature modulo its repeated empty traces.

Their cycle types are distributed equally among

\[
2+2,
\qquad
4,
\qquad
3+2,
\qquad
5:
\]

four monodromies of each type.

The subgroup of `S_5` generated by these sixteen permutations is the full symmetric group:

\[
\boxed{
\langle\text{rainbow-loop monodromies}\rangle=S_5.
}
\]

This is a boundary-level holonomy statement. It is not yet a contradiction: support labels are gauge data, and the interior action of the loop remains to be analysed.

Its significance is that the `C_3` policy is not a harmless cyclic version of the tree policy. Every quotient loop lifts nontrivially in the indexed-cover system.

## 10. The new global proof target

The cyclic four-cut programme is no longer a four-kernel elimination problem. It has two branches.

### Branch T — tree routing implies decomposition

For Type T, prove that the deterministic `P_5` routing forces nested or unique terminal linkages. Convert this rigidity into one of:

- a smaller edge separator;
- a serial four-pole decomposition;
- a bounded replaceable fragment.

The termination measure must decrease explicitly, for example by vertex count or separator complexity.

### Branch H — holonomy implies expansion or decomposition

For Type H, lift the rainbow triangle from boundary signatures to the full indexed-cover reconfiguration groupoid. Prove that its nontrivial monodromy either:

- forces an additional boundary state and destroys profile disjointness;
- creates a smaller cut or linkage decomposition;
- or acts nontrivially on a finite interior code whose orbit necessarily escapes the kernel.

The decisive object is not another boundary state. It is the interior lift of the rainbow holonomy.

## 11. Relation to the full programme

The higher-level mechanism diagram is now

\[
\boxed{
\begin{array}{c}
\text{cyclic four-edge cut in a minimal counterexample}\\
\downarrow\\
\text{cap-forced routing safety game}\\
\downarrow\\
\text{uniform routing eliminated}\\
\downarrow\\
\text{unique deterministic residual policy}\\
\downarrow\\
P_5\mid P_5
\quad\text{or}\quad
P_4\mid C_3\\
\downarrow\\
\text{decomposition or holonomy escape}.
\end{array}
}
\]

This avoids an infinite hierarchy of increasingly decorated local case lists. The remaining local data have been organized by the two global phenomena they express: unique linkage and holonomy.

## 12. Trust boundary

The routing-weight definition, coordinate-conservation theorem, fixed-routing sector decomposition, and uniform-routing elimination are elementary theorem-level results.

The injective coordinate table, two-colour connectivity, unique-policy assertions, two policy-pair orbit classification, and rainbow monodromy counts are exact finite computations, independently reproducible by the Wolfram verifier in the private notebook.

No claim is made that tree routing already yields a graph decomposition, that rainbow holonomy already forces profile expansion, that every cyclic four-edge cut is reducible, or that the five-cycle double cover conjecture is proved.
