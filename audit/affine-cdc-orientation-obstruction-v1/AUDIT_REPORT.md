# AC-OR1-AUDIT-01 independent audit report

## 1. Control and immutable input

- role: `AffineCDC — Independent Orientation Auditor` (`AC-OR1-AUDIT-01`);
- sole controlling issue: `Yuren-Tang/research-workbench#51`, including comment `5052309733`;
- deliberately unused duplicate: issue `#56`;
- immutable candidate: `Yuren-Tang/mathematics:curation/affine-cdc-orientation-obstruction-v1@e6af5645107d0f21ac6c262c63a1db5dab8f0fd1`;
- owned audit branch: `Yuren-Tang/mathematics:audit/affine-cdc-orientation-obstruction-v1`;
- verified branch base and pre-audit head: `e6af5645107d0f21ac6c262c63a1db5dab8f0fd1` (`0` ahead, `0` behind, identical merge base);
- checked Lean boundary: `Yuren-Tang/affine-cdc:main@ebd7098a7a8b824e8c0a511d3c71f61705672aa8`.

No inference of correctness was taken from issue #49, PDL authorship, Curator acceptance, Git ancestry, or the existence of partial Lean ingredients. The authorial and Curator documents were used only to identify statements and declared dependencies; every implication below was reconstructed independently.

## 2. Final classification

`VERIFIED SUBJECT TO NAMED NON-BLOCKING REPAIRS`

The fixed-lift and fixed-fibre orientation-obstruction package is mathematically sound at expoundable proof level. The conditional enriched-collapse theorem is also sound. No new lemma or counterexample is required to preserve the stated scope.

The candidate nevertheless contains two mathematically meaningful wording defects and three expository/terminological defects:

1. a geometric face occurrence is not one bare directed `rho_a`-orbit; it is the undirected support component, equivalently the pair of mutually reversed `rho_a`-orbits under `sigma`;
2. the unlabelled coset classifies accessible partial-Petrial **words** after forgetting componentwise affine translations, not homeomorphism or graph-automorphism classes of unlabelled surfaces;
3. the alternate code formula uses `C(G)`, `F_f`, and the Schur product without defining them locally;
4. “rank-three flow” should be read as an `F_2^3`-valued flow, not necessarily a flow whose values span all of `F_2^3`; this matters in the `K_4` example, whose values span a plane;
5. “oriented CDC” should be explicitly fixed to the directed-cycle-double-cover convention: each edge occurs exactly once in each direction.

All five repairs are local and non-blocking. Defect details are recorded in `DEFECT_AND_DEPENDENCY_LEDGER.md`.

## 3. Independent reconstruction summary

### 3.1 Retained surface

For each support index `a`, the support subgraph `F_a` is 2-regular on its incident vertices: at a cubic source vertex whose three roots are `{a,b}`, `{b,c}`, `{c,a}`, precisely the two darts belonging to `a` are paired by `partner_a`. Edge reversal is `sigma`, and

`rho_a = partner_a o sigma`

steps across one edge and then turns through the unique same-index corner. On each connected support component, `rho_a` has exactly two orbits, exchanged by `sigma`; these are the two directions around one undirected circuit. The component, not either parametrisation separately, is one face occurrence.

The local root triangle supplies a cyclic three-corner vertex link, unique up to reversal. Rectangular edge bands are attached with their two long sides labelled by the two elements of the root pair. Every point of the resulting ribbon complex has a disc or half-disc neighbourhood, every boundary component is one retained indexed support circuit, and capping all boundary components gives a closed cellular surface. Repeated equal supports at different indices remain different face discs.

### 3.2 Fixed-lift obstruction

After orienting every vertex disc, compare the two endpoint attachments of each nonloop edge band. The parity `w_e(g)` of a half-twist is independent of any temporary ordering of the unordered root pair: reversing the temporary order reverses it at both ends. Reversing the chosen orientation of one vertex disc reverses its local rotation and toggles precisely the incident edge signs. Hence

`w(g) -> w(g) + delta x`,

so

`omega(g) = [w(g)] in C^1(G)/Cut(G)`

is intrinsic. It is the pullback of the surface first Stiefel–Whitney class to the embedded graph.

The ribbon neighbourhood is orientable exactly when vertex orientations can make every band untwisted, equivalently `w(g)` is a cut. Capping boundary circles neither creates nor removes orientability. By cut-cycle orthogonality this is equivalent to zero twist holonomy on every binary source cycle. A global surface orientation induces opposite directions on the two face sides of each edge; conversely, coherent opposite face directions orient the bands and then the circular cubic vertex links. Thus the claimed directed CDC equivalence is correct for the retained face occurrences in the finite loopless cubic compatible setting.

### 3.3 Gauge and fixed fibre

For `k in H_f^0`, write

`k_u + k_v = lambda_e(k) f(e)`.

Transport the local cyclic order by the affine translation at each vertex. If `lambda_e=0`, the two endpoint translations identify the two side labels in the same order. If `lambda_e=1`, their difference is the root sum, which exchanges the two elements of the root pair at exactly one endpoint relative to the other. This is precisely one partial Petrial and toggles exactly one edge twist bit. Therefore

`w(g^k) = w(g) + Lambda_f(k)`

for transported local orientations, and the quotient law follows modulo cuts.

The compatible labelled lifts form an `H_f^0`-torsor. Consequently the orientable parameters are the inverse image of one vector under `q o Lambda_f`, hence empty or one affine torsor under `ker(q o Lambda_f)`. Passing from a base lift to any other base changes `w` by an element of `B_f=im Lambda_f` modulo cuts, so

`Omega_f in C^1/(Cut+B_f)`

is base-independent and vanishes exactly when the fixed fibre contains an orientable lift.

The image words giving orientable partial Petrials are empty or

`lambda_0 + (B_f intersect Cut)`.

This is the correct quotient of the labelled torsor by `ker Lambda_f`, but it is a coset of words, not a classification by surface isomorphism.

### 3.4 Duality

With the nondegenerate edge dot product,

`(Cut+B_f)^perp = Cut^perp intersect B_f^perp`.

Since `Cut^perp=Z_1(G)`, the orientation-stress space is exactly

`Stress_or(f)=Z_1(G) intersect B_f^perp`.

A base representative `w(g)` annihilates this space exactly when its class in `C^1/(Cut+B_f)` vanishes. Using the Programme B4 identity

`B_f=(C(G)*F_f)^perp`,

finite-dimensional double orthogonality gives

`Stress_or(f)=C(G) intersect (C(G)*F_f)`.

This is separate from the compatibility stress that tests whether the compatible-lift fibre is nonempty.

### 3.5 Exact `K_4` fibre

Let `W={0,x,y,x+y}` inside `Gamma=F_2^3`, and `f(uv)=u+v` on vertex set `W`.

- For `g_0(uv)=W-{0,f(uv)}`, the three nonempty indexed supports are the complements of the three direction matchings, hence three Hamiltonian four-cycles. The closed surface is connected and has `chi=4-6+3=1`, so it is the projective plane.
- For `k_u=u`, every edge has `lambda_e(k)=1`, and `g_1(uv)=W-{u,v}`. Its four supports are the four facial triangles of the tetrahedron, so `chi=4-6+4=2` and the surface is the sphere.

Both lifts are compatible and lie in the same fixed fibre. The all-edge word is not a cut in `K_4` because it pairs oddly with a triangle. Thus the example refutes only per-lift automatic orientability and proves `Omega_f=0` for this fibre.

### 3.6 Enriched collapse

For a directed circuit upstairs, deleting auxiliary edges leaves either no lifted edge or a cyclic sequence of lifted edges. Every deleted segment stays inside one collapse fibre, so consecutive projected endpoints match and cyclicity gives closure. Injectivity of the edge lift and edge-simplicity upstairs prevent repetition of a projected edge object. The result is an empty word or a directed closed trail, possibly revisiting vertices.

Splitting a nonempty directed closed trail at repeated vertices decomposes it into directed circuits without reversing any directed edge occurrence. Since every lifted original edge occurs upstairs exactly once in each direction, projection and decomposition retain exactly that multiplicity downstairs. Equal resulting circuits remain separate multiset occurrences. The enriched collapse theorem is therefore correct; the support-only theorem alone does not contain the needed direction and pairing data.

### 3.7 Loops and other conventions

The orientation obstruction itself is loopless. Under the declared loop-dart convention, each deleted loop is restored by two singleton loop circuits, one in each dart direction. This preserves directed multiplicity. Disconnected graphs split componentwise; multiedges and two-edge circuits cause no difficulty; repeated indexed supports retain distinct occurrence identities; empty supports contribute no face; and all coverage counts are multiset/occurrence counts.

## 4. Scope verdict

The package proves only a conditional classification inside one fixed compatible-lift fibre and the conditional transport of an orientable retained surface to a directed CDC downstairs. It does not prove either:

- `AC-RL-OR-FIXED-FIBRE-VANISHING`;
- `AC-RL-OR-GRAPH-EXISTENCE`.

No horizontal reconfiguration theorem, universal orientability theorem, or graph-level oriented CDC existence theorem follows from the audited linear algebra.

## 5. External mathematical anchors

The audit used the following standard external interfaces only:

- J. L. Gross and T. W. Tucker, *Topological Graph Theory* (1987), signed rotation systems, vertex switching, band decompositions, and orientability;
- the Heffter–Edmonds rotation principle for cellular embeddings;
- A. Jiménez and M. Loebl, *Directed cycle double covers and cut-obstacles* (2014), for the directed CDC convention that every edge is covered by two oppositely directed cycles;
- the classification of closed connected surfaces for the `K_4` Euler-characteristic identification;
- elementary finite directed-trail decomposition.

No external source supplies the affine/Fano compatibility theorem, the gauge code, or the fixed-fibre class; those remain dependencies on the exact Programme A/B4 corpus named in the theorem trace.

## 6. Mutation statement

This audit adds only the four issue-authorized reports under `audit/affine-cdc-orientation-obstruction-v1/`. It does not modify the immutable candidate or any PDL, Curator, Research Lead, Lean, Paper A, `main`, release, tag, arXiv, DOI, workflow, or publication surface.