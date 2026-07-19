# Type H Tait resolution forces boundary-profile escape

**Programme:** `AffineCDC — Research Lead`  
**Status:** theorem-level elimination of the zero-norm root-linearizable Type H branch, using exact finite identification of the three physical rainbow-triangle orbits  
**Parents:** `FIVE_CDC_ROUTING_WEIGHT_AND_HOLONOMY_DICHOTOMY_V1.md`, `FIVE_CDC_RAINBOW_SWITCH_FLOW_TAIT_RESOLUTION_V1.md`

## 1. Purpose

The routing classification leaves two residual mechanisms across a cyclic four-edge cut:

\[
P_5\mid P_5
\qquad\text{or}\qquad
P_4\mid C_3.
\]

The second mechanism, Type H, contains a shore whose deterministic routing automaton is a rainbow triangle.  The preceding packet proves that every zero-norm lifted rainbow loop is either:

1. root-linearizable, equivalently its switch flow admits a Tait resolution; or
2. obstructed by a zero edge, an all-zero cubic vertex, or an odd component of a matching-complement two-factor.

This packet eliminates the first alternative inside every minimal Type H kernel.

The key point is not merely that a Tait resolution produces another cover.  Its three bicoloured supports force two nominally different Kempe challenges at a `B_i` state to have the same underlying symmetric-difference subgraph and hence the same terminal route.  Every BBD Type H triangle demands distinct routes for those two challenges.  The DDD triangle is even simpler: the Tait resolution itself creates a `B_i` state outside the profile.

Consequently:

\[
\boxed{
\text{Type H}
+
\text{zero norm}
+
\text{root linearization}
\Longrightarrow
\text{boundary-profile escape}.
}
\]

No five-cycle double cover theorem is claimed.  The nonzero-norm and oddness-certificate branches remain open.

## 2. Tait covers of a four-pole

Let `P` be a cubic four-pole with a proper three-edge-colouring by colours

\[
a,b,c.
\]

Assume its four terminal semiedges have colours

\[
a,a,b,b.
\]

Let `X` be the two terminals coloured `a`, let `Y` be the two terminals coloured `b`, and let

\[
M_i=X\mid Y
\]

be the induced terminal matching.

Define the three bicoloured relative even subgraphs

\[
F_{ab}=E_a\cup E_b,
\qquad
F_{ac}=E_a\cup E_c,
\qquad
F_{bc}=E_b\cup E_c.
\]

At every internal cubic vertex each of these has degree two.  Their terminal traces are respectively

\[
\partial F_{ab}=X\cup Y,
\qquad
\partial F_{ac}=X,
\qquad
\partial F_{bc}=Y.
\]

Adding two empty supports gives the five-support boundary cover

\[
\boxed{
\varnothing,
\varnothing,
F_{ac},
F_{bc},
F_{ab},
}
\]

whose support-unordered boundary state is `B_i`.

### Lemma 2.1 — Tait challenge coincidence

In the displayed `B_i` cover, the two complementary support-pair challenges have the same symmetric difference:

\[
\boxed{
\varnothing\triangle F_{ab}
=
F_{ac}\triangle F_{bc}
=
F_{ab}.
}
\]

Therefore the empty/full challenge and the partition/partition challenge realize exactly the same terminal path pairing.

#### Proof

The first equality is immediate.  Since

\[
F_{ac}=E_a\cup E_c,
\qquad
F_{bc}=E_b\cup E_c,
\]

the `c`-coloured edges cancel in symmetric difference and the `a,b` edges remain:

\[
F_{ac}\triangle F_{bc}=E_a\cup E_b=F_{ab}.
\]

The terminal routing is determined by the path components of this same relative even subgraph. ∎

The common route need not be the equal-colour matching `M_i`; its value depends on the parity of the two alternating terminal paths.  Only its equality for the two challenges is used.

## 3. The three physical Type H triangle shores

The four minimal disjoint routing kernels collapse to three physical triangle shores, in two state-combinatorial forms.

### BBD triangles

\[
\boxed{
\mathcal T_1=\{B_1,B_2,D_0\},
\qquad
\mathcal T_2=\{B_0,B_1,D_2\}.
}
\]

Their rainbow cycles may be taken as

\[
B_1\xrightarrow{0}B_2\xrightarrow{1}D_0\xrightarrow{2}B_1,
\]

and

\[
B_0\xrightarrow{2}B_1\xrightarrow{0}D_2\xrightarrow{1}B_0.
\]

### DDD triangle

\[
\boxed{
\mathcal T_D=\{D_0,D_1,D_2\},
}
\]

with rainbow cycle

\[
D_0\xrightarrow{2}D_1\xrightarrow{0}D_2\xrightarrow{1}D_0.
\]

The exact routing-game verifier proves these are the three triangle shores occurring in the Type H kernel representatives, up to simultaneous colour permutation and shore exchange.

A direct ordered-signature enumeration gives:

- `16` lifted monodromies for each BBD triangle, four of each support cycle type `5`, `4`, `3+2`, `2+2`;
- `4` lifted monodromies for the DDD triangle, two of type `4` and two of type `2+2`;
- in every lift, the first and third switch coefficients agree.

The exact monodromy counts are not needed for the escape proof; they verify that the Tait-resolution machinery applies to all physical triangle orbits rather than only the canonical BBD representative.

## 4. BBD triangles cannot contain a Tait resolution

The deterministic safety-game policies on the B-states of the two BBD triangles are as follows.

### Triangle `T_1={B_1,B_2,D_0}`

At `B_1`:

\[
\operatorname{route}(\mathrm{ef})=2,
\qquad
\operatorname{route}(\mathrm{pp}_1)=0.
\]

At `B_2`:

\[
\operatorname{route}(\mathrm{ef})=1,
\qquad
\operatorname{route}(\mathrm{pp}_2)=0.
\]

### Triangle `T_2={B_0,B_1,D_2}`

At `B_0`:

\[
\operatorname{route}(\mathrm{ef})=1,
\qquad
\operatorname{route}(\mathrm{pp}_0)=2.
\]

At `B_1`:

\[
\operatorname{route}(\mathrm{ef})=0,
\qquad
\operatorname{route}(\mathrm{pp}_1)=2.
\]

Thus at every B-state belonging to a BBD triangle, the unique route that remains in the triangle differs between the empty/full and partition/partition challenges.

### Theorem 4.1 — BBD Tait escape

Let a four-pole have complete boundary profile equal to one of the BBD triangle profiles.  Then it admits no Tait-coloured cover whose induced `B_i` state belongs to that triangle.

More precisely, from any such Tait cover, at least one of the two canonical Kempe switches realizes a boundary state outside the triangle.

#### Proof

By Lemma 2.1, the empty/full and partition/partition challenges in the Tait-induced `B_i` cover have the same underlying symmetric-difference subgraph, hence the same actual terminal routing matching.

But the unique deterministic policy of the BBD triangle requires two different routing matchings for the two challenges at that `B_i`.  The actual common route can agree with at most one of them.  Applying the other genuine Kempe-path switch therefore produces a boundary state outside the triangle. ∎

This is a graph-theoretic contradiction to profile equality, not merely a failure of one abstract policy choice: both switches are actual switches of the displayed Tait cover.

## 5. DDD triangles escape immediately

### Theorem 5.1 — DDD Tait escape

Let a four-pole have complete boundary profile

\[
\{D_0,D_1,D_2\}.
\]

Then it admits no Tait resolution of a lifted rainbow loop.

#### Proof

Every Tait resolution is a proper three-edge-colouring of the four-pole.  Its four terminal colours occur in two equal pairs in the rainbow switch-flow boundary pattern.  Section 2 therefore constructs an indexed five-support cover in some state `B_i`.

No `B_i` belongs to the DDD profile.  Hence the complete profile strictly expands. ∎

## 6. Type H zero-norm root-linearizable branch is eliminated

### Theorem 6.1 — Type H Tait-escape theorem

Let `P` be the triangle shore of a Type H minimal routing kernel.  Suppose its lifted rainbow loop has zero interior norm defect and is root-admissibly linearizable.

Then

\[
\boxed{
\Sigma(P)
\text{ strictly contains the corresponding minimal triangle profile.}
}
\]

Consequently no Type H minimal kernel can realize this alternative.

#### Proof

By the rainbow switch-flow theorem, zero norm plus root-admissible linearization is equivalent to the existence of a Tait resolution.

If the triangle is BBD, apply Theorem 4.1.  If it is DDD, apply Theorem 5.1.  These exhaust the physical Type H triangle shores. ∎

### Corollary 6.2 — residual Type H alternatives

In a Type H minimal kernel, every lifted rainbow loop must lie in one of the following two unresolved classes:

1. **nonzero norm defect**
   \[
   N_\pi z\ne0,
   \]
   yielding after `ord(pi)` traversals a nontrivial pure interior translation and period doubling;

2. **zero norm but no Tait resolution**, witnessed exactly by:
   - a zero edge for support types `4` or `5`;
   - an all-zero cubic vertex for types `3+2` or `2+2`;
   - an odd component of the matching-complement degree-two system for types `3+2` or `2+2`.

The root-linearizable zero-norm class is no longer part of the residual obstruction.

## 7. Updated mechanism diagram

The Type H branch is now

\[
\boxed{
\begin{array}{c}
\text{rainbow triangle in a minimal kernel}
\\ \downarrow
\\
(\pi,z)\in (Z_1(P)\otimes E_5)\rtimes S_5
\\ \downarrow
\\
d=N_\pi z
\\ \downarrow
\\
\begin{cases}
d\ne0
&\Rightarrow\text{pure interior translation / period doubling},
\\[1mm]
d=0
&\Rightarrow\text{Tait-resolution dichotomy}.
\end{cases}
\\ \downarrow
\\
\begin{cases}
\text{Tait resolution}
&\Rightarrow\textbf{profile escape},
\\[1mm]
\text{no Tait resolution}
&\Rightarrow\text{zero or oddness certificate}.
\end{cases}
\end{array}
}
\]

Thus the remaining Type H proof target has only two forms:

\[
\boxed{
\text{nonzero interior translation}
\quad\text{or}\quad
\text{concrete zero/oddness certificate}.
}
\]

This is a strict mechanism reduction: a complete algebraically soluble half-branch has been removed rather than redescribed.

## 8. Relation to the global programme

The cyclic four-cut programme now has the form

\[
\boxed{
\begin{array}{c}
\text{minimal counterexample with cyclic four-cut}
\\ \downarrow
\\
\text{deterministic policy}
\\ \downarrow
\\
\begin{cases}
\text{Type T: }P_5\mid P_5
&\Rightarrow\text{unique-linkage decomposition target},
\\
\text{Type H: }P_4\mid C_3
&\Rightarrow
\begin{cases}
\text{nonzero norm translation},\\
\text{zero/vertex/oddness certificate}.
\end{cases}
\end{cases}
\end{array}
}
\]

The next sought theorem should unify these outputs under a strict progress principle:

- a pure interior translation must enlarge an orbit beyond the rigid profile or reveal a bounded reconfiguration-contractible fragment;
- an odd component must admit an odd-ring transfer/replacement or expose a smaller separator;
- a zero edge or all-zero vertex must localize one of the switch paths strongly enough to force serial decomposition;
- Type T unique routing should produce the same replacement certificates from the acyclic side.

## 9. Trust boundary

The following are theorem-level:

- construction of a `B_i` cover from a Tait colouring;
- Tait challenge coincidence;
- BBD Tait escape;
- DDD Tait escape;
- elimination of the zero-norm root-linearizable Type H branch.

The following are exact finite computations:

- identification of the two BBD and one DDD physical triangle shores;
- their unique route policies;
- the monodromy counts for all three triangle orbits;
- equality of the first and third switch coefficients in every enumerated lift.

The following remain open:

- elimination of nonzero norm defects;
- strict reduction from zero-edge, all-zero-vertex, and odd-component certificates;
- repeatability and compatibility of all lifted loops with the complete interior reconfiguration groupoid;
- Type T decomposition;
- the full five-cycle double cover conjecture.

## 10. Next exact tasks

1. Formulate the odd-component transfer state under four-cut gluing and test whether odd rings compose serially.
2. Prove an orbit-size lower bound for a nonzero pure interior translation inside the root-valued reconfiguration component.
3. Determine whether a zero edge forces two of the three rainbow switch paths to coincide or cancel on a subpath.
4. Compare the Tait-resolved triangle contraction with recent flow-reconfiguration notions of contractible subgraphs.
5. Seek one common replacement invariant for Type T unique linkage and Type H oddness/translation.
