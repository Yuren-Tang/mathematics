# Cap-Kempe switching is controlled by four-terminal pairing alignment

**Programme:** `AffineCDC — Research Lead`  
**Status:** theorem-level local mechanism for the four-pole programme; not canonical pending Director review and literature audit  
**Parents:** `FIVE_CDC_FOUR_EDGE_BOUNDARY_SIGNATURES_V1.md`, `FIVE_CDC_FOUR_POLE_KEMPE_CLOSURE_V1.md`, `FIVE_CDC_SMALL_FOUR_POLE_PROFILE_CENSUS_V1.md`

## 1. Purpose

The standard two-vertex cap realizes four boundary states

\[
\mathcal K_i=\{B_j,D_j:j\ne i\}
\]

for one cap matching `M_i`. Vertex minimality guarantees that the shore profile meets `\mathcal K_i`, but does not immediately imply that it contains all four states.

This packet identifies the missing mechanism.

For a chosen pair of support indices, the useful Kempe switch exists precisely when the pairing of the four boundary endpoints inside the shore agrees with the pairing supplied by the cap.

Thus the full-cap-profile problem is not merely a ten-state closure problem. It is a compatibility problem between:

1. the boundary signature;
2. the internal path pairing of support-pair symmetric differences.

## 2. Standard cap

Let a four-pole `P` have boundary semiedges

\[
1,2,3,4.
\]

Fix the cap matching

\[
M_i=12\mid34
\]

after relabelling. Add cubic vertices `x,y`, attach terminals `1,2` to `x`, attach `3,4` to `y`, and add the cap edge `xy`.

Let

\[
\mathcal F=(F_1,\ldots,F_5)
\]

be an indexed five-support cycle double cover of the capped graph. Its restriction to `P` has one of the four signatures in `\mathcal K_i`.

## 3. Support-pair difference

Choose support indices `a,b` whose boundary traces differ at all four terminals:

\[
\partial F_a\triangle\partial F_b
=
\{1,2,3,4\}.
\]

Let

\[
X_{ab}=F_a\triangle F_b.
\]

In the closed capped graph, `X_{ab}` is an even subgraph and therefore a disjoint union of cycles.

Inside the shore `P`, its boundary-connected part consists of two terminal-to-terminal paths. These paths realize one of the three perfect matchings of the four terminals; call it

\[
M_P(a,b).
\]

Internal cycle components are irrelevant to the boundary pairing.

## 4. The cap pairing lemma

### Lemma 4.1

Inside the two-vertex cap, `X_{ab}` consists exactly of the two paths

\[
1-x-2,
\qquad
3-y-4.
\]

In particular the cap edge `xy` does not belong to `X_{ab}`, and the cap part realizes the matching `M_i=12\mid34`.

#### Proof

At every boundary terminal, exactly one of `F_a,F_b` is present, since their traces differ at all four terminals. Hence both terminal edges incident with `x` lie in `X_{ab}`. The symmetric difference has even degree at `x`; the two terminal edges already give degree two, so the cap edge is absent. The same argument applies at `y`. ∎

## 5. Pairing-alignment dichotomy

The union of the cap matching `M_i` and the shore matching `M_P(a,b)` is a two-regular multigraph on the four terminals.

### Theorem 5.1 — cap-Kempe pairing alignment

There are two cases.

### Aligned case

If

\[
M_P(a,b)=M_i,
\]

then the boundary-connected part of `X_{ab}` consists of two distinct cycles. Each cycle contains one cap path and one shore path.

Swapping the support names `a,b` on either one of these cycles gives another indexed five-support cycle double cover of the capped graph. After restriction to `P`, its boundary signature is generally a different member of the ten-state alphabet and is obtained by exchanging `a,b` on exactly one block of `M_i`.

### Misaligned case

If

\[
M_P(a,b)\ne M_i,
\]

then the union of the two matchings is one four-cycle. Consequently all four boundary terminals belong to one cycle component of `X_{ab}`.

Swapping `a,b` on that cycle exchanges their names at all four boundary terminals. Up to permutation of the five support indices, the restricted boundary signature is unchanged.

Thus:

\[
\boxed{
\text{a support-pair Kempe switch creates a new unlabelled cap state}
\iff
M_P(a,b)=M_i.
}
\]

#### Proof

Two equal perfect matchings form two doubled edges, corresponding here to two separate cap-shore cycles. Two distinct perfect matchings on four vertices have union a simple four-cycle, corresponding to one cap-shore cycle through all four terminals.

A support-pair switch on one of two separate cycles changes membership at exactly the two terminals on one cap block. In the one-cycle case it changes membership at all four terminals, which is exactly the global transposition of the two support names on the boundary and hence does not change the support-unordered signature. ∎

## 6. Exact local transition rule

Let a boundary state and a complementary support pair `a,b` be fixed. In the aligned case, the target state is determined purely by the boundary traces and the cap matching:

\[
(\partial F_a,\partial F_b)
\longmapsto
(\partial F_a\triangle P_i,
 \partial F_b\triangle P_i),
\]

where `P_i` is either one of the two blocks of `M_i`. Choosing the complementary block produces the same support-unordered target.

The finite A/B/C/D Kempe table is obtained by applying this operation to every complementary support pair. The theorem above supplies the geometric condition deciding whether that listed transition is genuinely available in a given capped cover.

## 7. Why cap forcing does not imply full cap by itself

Minimality gives, for each cap matching `M_i`, at least one capped cover and hence at least one state in `\mathcal K_i`.

However the existence of that cover does not say that any complementary support-pair difference inside the shore realizes `M_i`. If all relevant differences are misaligned, all available cap-crossing Kempe cycles pass through all four terminals and produce no new support-unordered boundary state.

Therefore the implication

\[
\Sigma(P)\cap\mathcal K_i\ne\varnothing
\quad\Longrightarrow\quad
\mathcal K_i\subseteq\Sigma(P)
\]

cannot be obtained from local cap geometry alone.

The missing statement must control shore pairings.

## 8. Refined full-cap target

For every connected cap-admissible cubic four-pole `P`, prove one of the following stronger alternatives.

### Alignment alternative

There exists a cap matching `M_i` and a capped five-support cover such that enough complementary support-pair differences satisfy

\[
M_P(a,b)=M_i
\]

to generate all four states in `\mathcal K_i` by cycle switches.

### Decomposition alternative

If all relevant pairings remain systematically misaligned, the resulting path system forces a bounded edge cut, serial four-pole decomposition, or another gluing interface.

Either alternative would imply the desired full-cap-profile theorem or reduce the four-pole to smaller pieces.

The mechanism target is therefore

\[
\boxed{
\text{pairing alignment}
\quad\text{or}\quad
\text{four-pole decomposition}.
}
\]

## 9. Relation to current evidence

The exhaustive four-pole census through six internal vertices found only profiles containing a complete `\mathcal K_i`. Exploratory larger-order searches found the same pattern.

The present theorem explains what a conceptual proof must establish: small examples are not succeeding merely because the ten-state closure is strong; their internal support-pair paths supply sufficient alignment.

A future verifier should therefore record, in addition to `\Sigma(P)`, the set of realized pairing-labelled transitions for every indexed boundary cover.

## 10. Trust boundary

The cap pairing lemma and the aligned/misaligned cycle decomposition are elementary theorems. They identify a necessary and sufficient condition for one specified support-pair Kempe switch to change the support-unordered boundary signature.

No claim is made that every admissible four-pole has a sufficiently aligned capped cover, that systematic misalignment always decomposes, or that the full-cap-profile theorem is proved.
