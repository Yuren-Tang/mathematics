# AC-OR1-AUDIT-01 theorem trace

## Trace key

- `V`: independently verified as stated;
- `V-R`: verified after the named local repair;
- `D`: dependency consumed but not re-proved inside OR1;
- `O`: genuinely open boundary.

Exact fixed candidate: `e6af5645107d0f21ac6c262c63a1db5dab8f0fd1`.

## T0. Incoming compatibility and retained data

### Claim

For every finite loopless cubic multigraph with a nowhere-zero `Gamma=F_2^3`-valued flow, the compatible labelled-lift fibre is nonempty and carries retained indexed support/dart data.

### Exact inputs

- `projects/affine-cdc/core/rank-three-fano-compatibility.md`, especially Theorem 7.1, at Programme-A base `ec765cd03271abd3588ec36faec3d53d0f8aa03b`;
- `Yuren-Tang/affine-cdc:main@ebd7098a7a8b824e8c0a511d3c71f61705672aa8`, `lean/AffineCDC/Cycle.lean`;
- Lean declarations `partnerD`, `partnerD_mem`, `partnerD_ne`, `partnerD_partnerD`, `Msupp_vertex_unique`, `rho`, `rhoInv`, `rhoInv_rho`, `rho_rhoInv`, and `exists_indexed_dart_cover`.

### Audit

The Fano characteristic-torsor theorem supplies nonemptiness and the full vertical moduli space. Lean independently checks the exact-two support membership per dart, the unique same-vertex partner, sigma-closure, and inverse rotations. Lean does not construct the topological surface or any orientation class.

### Verdict

`D` for global compatible-lift existence; `V` for the logical adequacy of the retained data as input to the topological reconstruction.

---

## T1. Retained support occurrences reconstruct a closed cellular surface

### Candidate statement

`surface-and-fixed-lift-obstruction.md`, Theorem 3.1.

### Reconstruction

At a cubic vertex the three incident root pairs are `{a,b}`, `{b,c}`, `{c,a}` with distinct `a,b,c`. For each index, the partner involution joins the two incident darts containing that index. These three pairings are precisely the three corners of one triangle. They determine a cyclic order of the three edge ends up to reversal, hence one unoriented vertex disc.

For an edge labelled `{a,b}`, attach one rectangle whose long sides are labelled `a` and `b`; attach its end intervals to the corresponding two corners at the endpoints. The labels remove any endpoint ambiguity. The local link at an interior vertex is the three-edge circle obtained by alternating edge-end intervals and the three labelled corners. Thus no cone point or pinching occurs.

The boundary walk with index `a` advances by crossing an edge with `sigma` and turning through the `a`-corner with `partner_a`, namely by `rho_a`. Each connected 2-regular support component gives two oppositely directed `rho_a`-orbits, interchanged by `sigma`; together they are the two parametrisations of one geometric boundary circle. Cap that circle once.

After capping all boundary components, the result is closed. The complementary regions are exactly the added discs, so the embedding is cellular. The construction is componentwise over the source graph.

### Repair

Replace “directed face boundaries are the `rho_a`-orbits” by one of:

- “each face occurrence is a connected component of `F_a`, and its two directed boundary parametrisations are the paired `rho_a`-orbits exchanged by `sigma`”; or
- “directed face boundaries are `sigma`-paired classes of `rho_a`-orbits.”

Without this repair, a literal orbit count doubles the number of geometric faces.

### Verdict

`V-R`.

---

## T2. Twist word and vertex switching

### Candidate statement

`surface-and-fixed-lift-obstruction.md`, Sections 4–5.

### Reconstruction

Choose an orientation on each vertex disc. An edge band has two endpoint attachments. Their compatibility or incompatibility with the chosen local orientations gives one parity bit. A temporary enumeration `(a,b)` of the two side labels may be used to compute the parity, but replacing it by `(b,a)` changes both endpoint descriptions and leaves the parity unchanged. Reversing a coordinate along the edge band likewise changes both ends and leaves the parity unchanged.

Reversing one vertex-disc orientation reverses its local rotation and toggles the sign of every incident nonloop band. Over `F_2`, simultaneous reversals prescribed by `x in C^0(G)` add `delta x`. Hence the signed-rotation switching class is exactly `[w(g)] in C^1/Cut`.

### External anchor

Standard signed rotation systems: switching at a vertex reverses the local rotation and changes all incident edge signs; equivalent signed rotations encode the same embedding.

### Verdict

`V`.

---

## T3. Fixed-lift orientability criterion

### Candidate statement

`surface-and-fixed-lift-obstruction.md`, Theorem 5.1 and Corollary 5.2.

### Reconstruction

The band-and-disc neighbourhood is orientable iff local vertex orientations can be chosen so every band is untwisted. This is exactly solvability of `w+delta x=0`, or `w in Cut`. Since the binary cycle space is `Cut^perp`, this is equivalent to zero pairing with every source cycle.

Capping boundary circles preserves orientability in both directions. A global orientation gives opposite induced boundary directions on the two sides of every band. Conversely, face-disc orientations that traverse each edge in opposite directions orient every band; the cyclic three-corner link then extends the orientation across each vertex disc.

Each retained support component is an edge-simple circuit in the loopless cubic setting, including possible two-edge parallel circuits. Exact two-index membership gives one occurrence in each direction per edge.

### Scope

The equivalence is between orientability of the retained cycle-face surface and a directed CDC made from those retained occurrences. It does not apply to an arbitrary circuit decomposition of the support sets.

### Verdict

`V`, with the terminology repair that “oriented CDC” be explicitly identified with the directed CDC convention.

---

## T4. Gauge/partial-Petrial law

### Candidate statement

`fixed-fibre-gauge-and-duality.md`, Theorem 2.1.

### Exact dependency

`projects/affine-cdc/five-support/gauge-and-reconfiguration.md`, Theorem 3.1, at `ec765cd03271abd3588ec36faec3d53d0f8aa03b`.

### Reconstruction

For `k in H_f^0`, endpoint translations satisfy

`k_u+k_v=lambda_e f(e)`.

Let the old root pair on `e` be `{a,b}`, so `f(e)=a+b`.

- If `lambda_e=0`, the two endpoint translations coincide. Transporting each local triangle orientation by translation preserves the side matching.
- If `lambda_e=1`, the endpoint translations differ by `a+b`, and translation by `a+b` exchanges `a` and `b`. Relative to the transported endpoint triangles, exactly one endpoint side assignment is exchanged. This inserts one half-twist in that edge band.

No edge orientation or choice of endpoint is privileged: interchanging `u,v` gives the same parity. Thus every coordinate with `lambda_e=1` and only those coordinates undergo a Petrial toggle.

### Conclusion

`w(g^k)=w(g)+Lambda_f(k)` for transported local orientations. Fresh local choices add a cut.

### Verdict

`V`.

---

## T5. Labelled orientable-lift torsor

### Candidate statement

`fixed-fibre-gauge-and-duality.md`, Theorem 3.1.

### Reconstruction

Let `q:C^1 -> C^1/Cut` and `Lambda_or=q o Lambda_f`. The fixed-lift theorem and T4 give

`S_{g^k} orientable iff Lambda_or(k)=omega(g)`.

The inverse image of one point under a linear map is either empty or one affine coset of the kernel. Since compatible labelled lifts form an `H_f^0`-torsor, the orientable labelled lifts are therefore empty or

`k_0 + ker Lambda_or`.

### Verdict

`V`.

---

## T6. Base-independent fixed-fibre class

### Candidate statement

`fixed-fibre-gauge-and-duality.md`, Section 4.

### Reconstruction

Changing the base from `g` to `g^k` changes a twist representative by `Lambda_f(k)` plus a cut. Therefore the image of `w(g)` in

`C^1/(Cut+B_f)`

is independent of the base. Its vanishing is equivalent to `w(g)` lying in `Cut+B_f`, which is exactly the existence condition from T5.

The quantifiers are distinct:

- `omega(g)` concerns one prescribed labelled lift;
- `Omega_f` concerns whether the complete compatible-lift fibre above one fixed flow meets the orientable locus.

### Verdict

`V`.

---

## T7. Unlabelled Petrial coset

### Candidate statement

`fixed-fibre-gauge-and-duality.md`, Corollary 5.1.

### Reconstruction

The image words satisfying orientability are

`P_g={lambda in B_f : w(g)+lambda in Cut}`.

If nonempty and `lambda_0 in P_g`, then

`lambda in P_g iff lambda+lambda_0 in B_f intersect Cut`.

Thus

`P_g=lambda_0+(B_f intersect Cut)`.

The quotient map from labelled parameters is `H_f^0 -> B_f`, whose kernel consists of componentwise constant affine translations. This forgets affine face names while retaining the exact Petrial word relative to the base band decomposition.

### Repair

Do not call the coset a classification of homeomorphism classes or graph-automorphism classes of unlabelled surfaces. Distinct words may produce isomorphic surfaces. The exact theorem classifies accessible orientable Petrial words, or labelled lifts modulo `ker Lambda_f`.

### Verdict

`V-R`.

---

## T8. Orientation-stress duality

### Candidate statement

`fixed-fibre-gauge-and-duality.md`, Theorem 6.1 and alternate code form.

### Reconstruction

Finite-dimensional nondegeneracy gives

`(Cut+B_f)^perp=Cut^perp intersect B_f^perp`.

Putting `Z_1=Cut^perp` yields the stated stress space. A class in `C^1/(Cut+B_f)` vanishes iff it annihilates the annihilator of `Cut+B_f`; hence `Omega_f=0` iff `w(g)` pairs trivially with every orientation stress.

The Programme B4/tensor identity

`B_f=(C(G)*F_f)^perp`

implies `B_f^perp=C(G)*F_f`, and therefore

`Stress_or(f)=C(G) intersect (C(G)*F_f)`.

The argument is componentwise and remains valid for disconnected graphs.

### Repair

Define locally:

- `C(G)` as the binary cycle space;
- `F_f` as the span of the binary coordinate words of the flow;
- `*` as the span of coordinatewise products.

### Verdict

`V`, with a non-blocking dependency-definition repair.

---

## T9. Exact `K_4` same-fibre example

### Candidate statement

`k4-and-oriented-collapse.md`, Theorems 2.1 and 3.1.

### Reconstruction

The direct support calculation gives three Hamiltonian four-cycles for `g_0` and four triangles for `g_1`. The one-skeleton is connected, so each closed surface is connected. Euler characteristics `1` and `2` identify the projective plane and sphere, respectively.

The field `k_u=u` satisfies `k_u+k_v=f(uv)`, so its gauge word is the all-edge word and it sends `g_0` to `g_1`. The all-edge word pairs oddly with any triangle and is not a cut.

### Terminology repair

The flow takes values in the ambient rank-three group `F_2^3`, but its values span the two-dimensional plane `W`. Avoid wording that suggests full value-span rank three.

### Verdict

`V`.

---

## T10. Support-only loss and enriched oriented collapse

### Candidate statement

`k4-and-oriented-collapse.md`, Proposition 4.1, Lemmas 5.1 and 6.1, Theorem 6.2, Corollary 6.3.

### Exact dependency

`projects/affine-cdc/reduction/even-cover-and-collapse.md`, collapse datum and cut-parity transport, at `ec765cd03271abd3588ec36faec3d53d0f8aa03b`.

### Reconstruction

The existing outer shell retains only supports and multiplicities. It does not retain a direction on each face occurrence, the partner/rotation data, or the pairing of segments through a collapsed fibre. Therefore no directed witness can be recovered from that witness alone.

Under the enriched datum, delete auxiliary edges from one directed upstairs circuit. A segment between successive lifted edges lies in one fibre, so the projected endpoints match. Cyclicity gives closure. An upstairs circuit uses no edge object twice, and the edge lift is injective, so no projected edge object repeats. The projection is empty or a directed closed trail.

Split at a repeated vertex and induct to decompose a directed closed trail into directed circuits, never reversing a directed edge occurrence. Every original edge has one lifted edge occurring once in each direction upstairs; projection and decomposition preserve those two directed occurrences.

### Verdict

`V`.

---

## T11. Loops, components, multiedges, repeated supports, empty supports, multiplicity

### Candidate statement

All three orientation chapters, especially `k4-and-oriented-collapse.md`, Section 7.

### Audit

- loops: excluded from the obstruction construction; restored externally as two singleton loop circuits, one per dart direction;
- components: all cochain spaces, surfaces, torsors, and stresses split componentwise;
- multiedges: edge objects remain distinct; two parallel edges may form a circuit;
- repeated/equal supports: different affine indices are distinct occurrences even when edge sets coincide;
- empty supports: indexed but contribute no boundary or face disc;
- multiplicity: cover and post-collapse circuit collections are multisets; equal circuit values are retained as separate occurrences.

### Verdict

`V` under the declared conventions. Loop reinsertion is not part of the current Lean boundary.

---

## T12. Global existence boundary

### Candidate statement

`AC_OR1_DEPENDENCY_AND_FRONTIER_MAP.md`, Section 7, and both orientation control chapters.

### Audit

The linear classification proves neither universal fixed-fibre vanishing nor existence of a favourable flow on every graph. The `K_4` example proves only that one fibre contains both orientability types and has `Omega_f=0`. No horizontal reconfiguration theorem is available.

### Verdict

- `AC-RL-OR-FIXED-FIBRE-VANISHING`: `O`;
- `AC-RL-OR-GRAPH-EXISTENCE`: `O`.

## Final trace conclusion

Every theorem needed for the conditional fixed-lift/fixed-fibre classification and enriched collapse is verified. T1 and T7 require precise local wording repairs; T8, T9, and the directed-CDC terminology require expository clarification. No candidate theorem requires new mathematics or a changed quantifier.