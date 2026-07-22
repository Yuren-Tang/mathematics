# Final composition bridge: one spine--attachment theorem remains

## Research synthesis v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `b10d6f64f4ce90aad42aed12ff2a58021359dc2f`  
**Purpose:** targeted synthesis before the final composition attack.  

**Primary parents:**

- `ORIENTED_CHANNEL_LOCK_BOUNDARY_CALIBRATION_V1.md`;
- `CONSTANT_PIVOT_ORIENTED_ROOT_SECTION_V1.md`;
- `EQUALITY_CHANNEL_FUNCTORIALITY_DEFECTS_V1.md`;
- `PIVOT_CHANGE_SIX_PORT_STAR_COMPLETION_V1.md`;
- `FORCED_DDD_BACKBONE_BINARY_TRANSPORT_V1.md`;
- `PETERSEN_SIMPLE_CYCLE_OUTPUT_CLASSIFICATION_V1.md`;
- `MINIMAL_LAMINAR_INTERVAL_SURGERY_V1.md`;
- `KEMPE_BLOCKER_TAIT_SIDE_NETWORK_V1.md`;
- `FOUR_PORT_TAIT_DIPOLE_PEELING_V1.md`;
- the physical cycle--cut response form and ribbon-intersection response geometry.

**Status:** synthesis and proof-target selection. The finite coefficient, boundary-state, orientation, and pivot-skeleton classifications are complete at research-theorem level. The remaining local burden is one source-composition theorem for a low-rank spine with arbitrary attached components.  

**Not implied:** proof of that theorem, a completed global induction, canonical acceptance, independent audit, Lean verification, manuscript integration, release, or the global five-support theorem.

---

## 1. Executive assessment

The programme has passed the obstruction-discovery stage.

The remaining work is not the classification of another unknown finite alphabet. Every surviving local failure has already been reduced to one of the following known carriers:

\[
\boxed{
\begin{array}{c}
\text{rank-one scalar cycle},\\
\text{rank-two Tait carrier},\\
\text{embedded Type-T backtrack},\\
\text{short forced DDD backbone},\\
\text{identity hexagon},\\
\text{DDD octagon}.
\end{array}}
\]

The only datum which may still be unbounded is the graph-incidence pattern of the root-valued components attached to such a carrier.

Thus the final local problem is one **spine--attachment composition problem**.

It is deep because an attachment can retain global graph information not visible in the finite boundary state. It is concentrated because the spine, its coefficient language, its route response, and its possible finite cores are all explicit.

---

## 2. What is already closed

### 2.1 Boundary mismatch

Physical disjoint-support commutation eliminates every abstract Type-T and Type-H four-pole mismatch kernel.

Consequently a vertex-minimal counterexample has no cyclic three- or four-edge cut after the established gluing theorems and may be assumed cyclically five-edge-connected.

### 2.2 Inverse-dipole value alphabet

The inverse lift has only:

1. immediate intersecting-root lift;
2. equality/zero failure;
3. disjoint-root/co-root DDD failure.

One separating Kempe component rescues either failure. A surviving failure is a full-channel lock.

### 2.3 Fixed route and orientation

Three-reconnection forcing and cap blocking reduce the complete outer profile to a globally fixed terminal matching.

The cap labels the two blocks of that matching. Hence a DDD full-channel lock is oriented, and the exceptional `D_8` cocycle restricts to a coboundary. No independent orientation bit survives.

### 2.4 Constant-pivot DDD strips

Every constant-pivot Petersen strip has a unique nonpivot root section. It preserves every emitted side root and the ordered boundary route.

Therefore constant-pivot runs are genuine rank-two root-valued/Tait spines, not residual co-root obstructions.

### 2.5 Equality functoriality

For the normalised equality generators, every failure of affine functoriality is either:

\[
\boxed{
\text{one single-root closed scalar-cycle flow}}
\]

or

\[
\boxed{
\text{one root-triangle-plane Tait flow}.}
\]

If neither defect occurs, the equality reconfiguration sector is functorial and contains no new higher-rank affine obstruction.

### 2.6 One pivot change

The complete six-port table for one pivot change has:

- four root-valued four-vertex star completions;
- two failures, both forcing the disjoint pivot pair as one DDD backbone.

The two residual pairings are exactly the two crossed routes of the central DDD atom.

### 2.7 Long forced backbones

The crossed-route choice is transported as one two-sheeted local system. It is not one bit per pivot change. In an oriented lock the return holonomy is trivial.

Formal Petersen reduction leaves only:

1. a short open reduced path;
2. Type-T backtracks;
3. a simple cycle core.

The simple even cycle cores are exactly:

- a root-labelled identity hexagon with doubled rank-two output;
- a DDD-labelled octagon.

There is no third bounded cycle species.

---

## 3. The common geometric picture

Let `R` be a support-minimal residual interval or carrier.

Write

\[
R=S\cup\mathcal A,
\]

where:

- `S` is the classified low-rank **spine**;
- `\mathcal A` is the family of external root-valued components attached to ports or side edges of `S`.

The spine has bounded route width:

- four ports for a laminar interval;
- at most six essential ports for one pivot-change carrier;
- bounded finite response for identity and DDD cycle cores.

All unboundedness is therefore contained in `\mathcal A`.

The attachment pattern has only three topological behaviours.

### Crossing

An attached component interlaces the ordered spine intervals.

Then its Kempe switch changes the locked terminal matching or expands the physical profile.

This is the established route/profile escape branch.

### Split

The attachments separate into two noninteracting incidence classes.

Then the spine ports and the separating attachment boundary expose a two-, three-, or four-edge separator, or a genuine transition two-sum.

The resulting shores are smaller and lie in the established gluing regime.

### Laminar/serial

All attachments are noncrossing and nested.

Choose an inclusion-minimal active attachment interval. Its binary interface has at most four ports. Matching-plus-Tait decomposition and dipole peeling reduce it unless its complete boundary response is prime.

The only unresolved case is this last prime laminar response.

---

## 4. The exact final local theorem

### Target 4.1 — spine--attachment descent

Let `R` be a support-minimal oriented residual carrier in a cyclically five-edge-connected minimal-counterexample instance. Assume its spine is one of the classified carriers above.

Prove at least one of:

1. **profile escape:** a crossing attachment supplies a route-changing Kempe switch;
2. **separator:** a split attachment exposes a two-, three-, or four-edge cut or transition two-sum;
3. **root replacement:** the spine and all enclosed attachments admit a boundary-preserving root-valued replacement of smaller vertex count;
4. **horizontal descent:** a switch produces a strictly smaller residual carrier with the same ordered route;
5. **bounded completion:** one of the explicit star, direct-pairing, identity, or DDD carriers realises the complete locked profile;
6. **contradiction:** the residual response cannot occur in a cyclically five-edge-connected source graph.

No seventh obstruction branch is permitted.

---

## 5. The prime-response bottleneck

Suppose crossing and split alternatives fail and no local star completion is admitted.

Then every admissible response forces one distinguished backbone pair. This is the common residue of:

- the two forbidden six-port pivot-change matchings;
- the fixed-route equality/DDD sector;
- blocked crossed star routes;
- the serial laminar interval.

This should be expressed in the physical Lagrangian response code.

Let

\[
\mathscr L_G\subset Z(G)\oplus\mathbf F_2^{E(G)}
\]

be the physical cycle--cut response space, controlled by the symmetric form

\[
\mathcal B_G:Z(G)^2\to\mathbf F_2.
\]

The ribbon interpretation identifies

\[
\operatorname{rad}\mathcal B_G
\]

with boundary-cycle homology.

### Target 5.1 — forced-backbone radical lemma

For a support-minimal prime response with one pair forced in every admissible completion, construct a nonzero cycle class

\[
\rho\in Z(G)
\]

such that

\[
\boxed{
\mathcal B_G(\rho,z)=0
\qquad(\forall z\in Z(G)).}
\]

Hence

\[
\rho\in\operatorname{rad}\mathcal B_G.
\]

Under the ribbon-intersection theorem, `rho` is homologous to a sum of boundary components.

### Target 5.2 — boundary-to-separator conversion

Show that the boundary class `rho` containing the forced cap/backbone pair yields one of:

1. a proper boundary component meeting the spine in two ports, hence a two-sum;
2. a boundary component meeting it in three or four ports, hence a gluable small separator;
3. a disc/annulus/Möbius carrier covered by the existing Tait-surface reductions;
4. a reducible boundary-parallel band which removes at least two source vertices.

Together Targets 5.1 and 5.2 would close the prime-response branch.

---

## 6. Why the radical route is plausible but not yet proved

The response form already gives:

\[
\operatorname{rad}\mathcal B_G
=
\operatorname{im}H_1(\partial\mathfrak R;\mathbf F_2).
\]

A forced pair behaves like a coloop/direct summand in the restricted response relation: no admissible response can separate its two incidences.

In a Lagrangian relation, a universally fixed coordinate normally creates an orthogonal one-dimensional factor. The missing proof is to show that physical support-minimality and the prescribed cap coordinates promote this linear factor to a nonzero cycle class, rather than merely a coordinate artefact removable by diagonal gauge.

The required extra inputs are exactly the data absent from an arbitrary Lagrangian code:

- common root flow;
- ordered terminal matching;
- channel-conjugation law;
- rank-one/rank-two defect restriction;
- four/six-port support minimality;
- cyclic five-edge connectivity.

Thus the radical lemma is not a purely abstract matroid statement. It is a physical response theorem.

---

## 7. Alternative proof route if the radical lemma stalls

There is a second, more combinatorial route.

### Target 7.1 — innermost enclosure preservation

Choose an innermost laminar attachment surrounding a forced backbone cell. Peel every matching or Tait side component permitted by the existing dipole theorems.

Prove that if the inverse lift still fails, then:

1. the ordered cap route is inherited;
2. the new failure is enclosed in a strict subinterval;
3. the new spine belongs to the same classified carrier list.

This gives infinite descent in the interval measure.

The radical route and the enclosure route should be regarded as two formulations of the same phenomenon:

- radical boundary = topological enclosure;
- strict subinterval = combinatorial enclosure.

The proof may use one to establish the other.

---

## 8. Recommended well-founded measure

Use a lexicographic measure with a multiset extension on split branches:

\[
\boxed{
\mathcal D(R)=
\bigl(
|V(R)|,
N_{\mathrm{active}}(R),
N_{\mathrm{pivot}}(R),
\gamma(R),
|\Sigma(R)|,
\beta(R),
D_{\mathrm{nest}}(R)
\bigr).}
\]

Here:

- `|V(R)|` is the enclosed source size;
- `N_active` counts external components meeting the spine;
- `N_pivot` counts reduced pivot-change states;
- `gamma` is response/ribbon Euler genus;
- `|Sigma|` is side-signature size;
- `beta` is cycle rank;
- `D_nest` is maximal laminar depth.

Expected decreases:

- star/direct replacement lowers `|V|`;
- component peeling lowers `N_active` or `|V|`;
- Petersen backtrack removal lowers `N_pivot`;
- Möbius-to-disk switch lowers `gamma` before vertex descent;
- separator uses the multiset extension on two smaller carriers;
- profile escape exits the locked induction branch.

The first coordinate may need to be replaced by the pair

\[
(|V(R)|,|\delta R|)
\]

if a replacement temporarily preserves vertices while reducing interface width.

---

## 9. Proof DAG after the synthesis

### Local bridge

1. formulate the restricted response relation of one forced six-port/backbone carrier;
2. prove forced pair implies an orthogonal/radical cycle class;
3. convert the radical class to a boundary enclosure;
4. obtain separator, known surface carrier, or strict replacement.

### Equality consumer

5. rank-one scalar defects enter the same boundary enclosure theorem;
6. rank-two braid defects enter Tait peeling and then the same theorem;
7. functorial Type-Z sector either has a scalar boundary class or a direct root lift.

### DDD consumer

8. four admissible star routes lift immediately;
9. forced backbone reduces to a short path, backtrack, identity hexagon, or DDD octagon;
10. each bounded carrier enters the same response/enclosure theorem.

### Global package

11. combine vertex reduction, horizontal rescue, separator gluing, and carrier descent;
12. prove every recursive call strictly decreases the global multiset measure;
13. conclude that a minimal counterexample cannot exist.

---

## 10. Risk assessment

### Low remaining classification risk

The coefficient and finite-state alphabets have been repeatedly closed from independent directions:

- ten-state boundary profiles;
- quadratic channel fibres;
- Tait surface curvature;
- Petersen pivot transport;
- DDD orientation cover;
- simple Petersen cycle census.

A genuinely new finite obstruction species is now unlikely.

### Moderate structural risk

The forced-pair-to-radical implication may require a more delicate restricted-response statement than the naive coloop intuition.

The cube examples already warn that support-minimal response words may have disconnected physical cycle projection. The proof must use the full response functional, not only one visible cycle.

### High proof-engineering risk

Even after the local bridge is proved, the global induction must avoid circular uses of:

- vertex minimality;
- profile minimality;
- interval minimality;
- defect minimality.

The measure and the precise category-preservation/separator statements must be fixed before claiming completion.

### Overall assessment

The problem is now a hard final bridge, not an open-ended research landscape.

The most plausible failure mode is that the radical lemma needs an additional hypothesis or a slightly larger bounded carrier, not that a new unbounded obstruction theory appears.

---

## 11. Decision after review

A broad retrospective review is no longer useful.

The targeted review has produced the needed unification:

\[
\boxed{
\text{all residual branches}
\longrightarrow
\text{one low-rank spine with attached components}
\longrightarrow
\text{one response-radical/enclosure theorem}.}
\]

The next direct task is therefore:

> Prove the forced-backbone radical lemma first in the minimal six-port pivot-change carrier, with the four star completions as the admissible response basis and the two forced-backbone matchings as the excluded pair.

If the radical class appears, convert it to a ribbon boundary and separator. If the calculation instead gives a nonradical response, use the witnessing cycle to construct the missing crossed star route and obtain profile escape.

This is the controlling first attack on the final composition bridge.

---

## 12. Trust boundary

### Exact synthesis inputs

- all abstract four-cut mismatch kernels are physically impossible;
- equality nonfunctoriality has rank at most two;
- constant-pivot DDD strips have a unique root section;
- one pivot-change cell has four star completions and two forced-backbone failures;
- forced backbones carry one transported crossed-route sheet;
- even simple Petersen cores are identity hexagons or DDD octagons;
- the response code is Lagrangian;
- its symmetric response form is ribbon intersection;
- its radical is boundary homology.

### Not proved here

- forced pair implies a radical cycle class;
- every radical class yields a composition-safe small separator in the original cubic graph;
- strict enclosure preservation under every peeling move;
- one complete well-founded global induction;
- the global five-support theorem.
