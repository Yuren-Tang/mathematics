# AC-OR1-AUDIT-01 counterexample and boundary checks

## 1. `rho`-orbit count test

Take one nonempty indexed support component that is an `n`-edge circuit, with no loops. Its dart set has `2n` elements. The permutation

`rho=partner o sigma`

has two `n`-element orbits, one for each direction. `sigma` exchanges them. The underlying support has only one connected component and the ribbon complex has only one boundary circle carrying that index.

Therefore a face occurrence cannot be identified with one bare directed `rho`-orbit. The correct object is either:

- the support component itself; or
- the unordered pair `{O,sigma O}` of reverse `rho`-orbits.

This is a direct counterexample to a literal reading that counts every directed orbit as a separate face, but not to the surface theorem after the local wording repair.

## 2. Two-parallel-edge test

Let a support component consist of two parallel edges between `u` and `v`. Each vertex has exactly the two support darts required by the partner rule. `rho` produces two reverse orbits of length two. The component is one legitimate multigraph circuit and caps by one disc.

This checks that:

- multiedges do not create a singularity;
- “cycle” must allow a two-edge circuit;
- dart orbits still come in a reverse pair;
- edge objects, not endpoint pairs, carry multiplicity.

## 3. Cubic vertex-link test

At a vertex with incident roots `{a,b}`, `{b,c}`, `{c,a}`, the three support corners are:

- the `a`-corner joining `{a,b}` to `{c,a}`;
- the `b`-corner joining `{a,b}` to `{b,c}`;
- the `c`-corner joining `{b,c}` to `{c,a}`.

The link alternates the three edge-end intervals and these three corners, giving one six-segment circle. No two corners are identified and no corner is missing because `a,b,c` are distinct. Hence capping the global boundary components cannot leave a cone point at the vertex.

This also identifies the exact place where cubic compatibility is used. An arbitrary even support family without the local root triangle would not by itself provide this link.

## 4. Hidden root-order test

Write one edge root as the unordered pair `{a,b}`. Temporarily enumerate it as `(a,b)` to compare endpoint attachments. If the enumeration is reversed at both ends, both local attachment descriptions reverse and the twist parity is unchanged. If one endpoint alone is reversed, that is not a harmless re-enumeration: it exchanges the two labelled support sides and is exactly a Petrial toggle.

Thus `w_e` has no hidden global root-side ordering, provided the side labels themselves are retained.

## 5. Vertex-switch test

On a nonloop edge `e=uv`, reversing the chosen disc orientation at `u` toggles the compatibility of the `u` attachment and hence toggles `w_e`; reversing at `v` does the same. Reversing both endpoints toggles twice and leaves `w_e` unchanged. Therefore the total change is

`x_u+x_v=(delta x)_e`.

For a disconnected graph the same calculation is componentwise. The kernel consists of constant vertex reversals on each component, as expected.

## 6. Gauge endpoint-convention test

Let the old root be `{a,b}` with `a+b=f(e)`.

- If `k_u+k_v=0`, both endpoint triangles are translated identically; no side exchange occurs.
- If `k_u+k_v=f(e)=a+b`, translation by the endpoint difference sends `a` to `b` and `b` to `a`; exactly one relative side exchange occurs.

Swapping the names `u,v` does not change the conclusion. Replacing the temporary root order `(a,b)` by `(b,a)` also does not change the parity. Hence `Lambda_f(k)` toggles exactly the stated coordinates under all endpoint conventions.

## 7. Labelled torsor versus word coset

The labelled lift parameters form an `H_f^0`-torsor. Componentwise constant translations lie in `ker Lambda_f`: they change all affine labels on a component but do not change the Petrial word.

After quotienting only by this kernel, the image is the word space `B_f`. The orientable image is a coset of `B_f intersect Cut`.

However, two different Petrial words may still yield isomorphic unlabelled surfaces through an automorphism of the source graph or an accidental homeomorphism. Therefore the candidate must not identify the word coset with a set of surface isomorphism classes. The exact quotient is “labelled lifts modulo componentwise affine translation,” not “all unlabelled surfaces modulo isomorphism.”

## 8. Fixed-lift versus fixed-fibre test on `K_4`

For the standard `K_4` flow in the plane `W`:

- `g_0` gives the projective plane and has `omega(g_0) != 0`;
- `g_1=g_0^k` gives the sphere and has `omega(g_1)=0`;
- both are in the same fixed fibre, so `Omega_f=0`.

Thus:

- nonzero `omega(g)` does not imply nonzero `Omega_f`;
- per-lift nonautomaticity does not obstruct fixed-fibre existence;
- the all-edge gauge word genuinely changes the fixed-lift class.

This is the decisive quantifier-separation test.

## 9. `K_4` connectedness and cellularity test

The Euler-characteristic identifications use two facts supplied independently of the count:

1. the one-skeleton is connected, hence the constructed surface is connected;
2. all boundary components are capped by discs, hence the embedding is cellular and the resulting surface is closed.

With those hypotheses:

- `chi=1` cannot be orientable and identifies the projective plane;
- `chi=2` identifies the sphere.

No hidden connectedness assumption remains. Without T1, the Euler counts alone would not justify the surface names; therefore the example depends on the retained surface theorem, not merely on support counts.

## 10. Ambient-rank test

The `K_4` flow takes values in `Gamma=F_2^3`, but all values lie in and span the plane `W`. It is valid input to the rank-three AffineCDC theorem because that phrase refers to the ambient coefficient group. It is not a full-span rank-three flow.

This is a terminology boundary, not a mathematical defect in the example.

## 11. Compatibility stress versus orientation stress

The compatibility stress is dual to the obstruction for existence of any compatible affine lift. In rank three that obstruction vanishes.

The orientation stress is

`Z_1(G) intersect B_f^perp`

and tests whether a nonempty compatible fibre meets the orientable locus. The `K_4` projective-plane lift already shows that compatibility does not force every lift to be orientable. No natural identification of the two stress spaces follows from Fano self-duality.

## 12. Projection-closure test

Take one directed circuit upstairs. After auxiliary edges are deleted, consider two consecutive retained lifted edges in the cyclic sequence. The deleted segment between them uses only edges within one collapse fibre. Hence the terminal collapse vertex of the first projected edge equals the initial collapse vertex of the next. The same argument across the cyclic end proves closure.

A projected word may revisit a collapse vertex, so it need not be a circuit. It cannot repeat an edge object because:

- the upstairs circuit is edge-simple;
- the edge lift is injective.

Thus “directed closed trail” is exact.

## 13. Directed decomposition test

Given a nonempty finite directed closed trail with a repeated vertex, cut the cyclic word at two visits to that vertex. This produces two shorter directed closed trails whose directed edge occurrences partition the original occurrences. Induction ends in directed circuits.

No edge is reversed at any step. Therefore if an original edge appears in the projected collection once in each direction before decomposition, it still appears once in each direction afterward.

Equal resulting circuit words must remain separate multiset occurrences.

## 14. Support-only data-loss test

An even support records only which edge objects occur. It does not record:

- which direction a face uses on an edge;
- the cyclic successor at a vertex;
- how segments are paired through a collapsed fibre.

Two opposite orientations of one support have the same support set. A generic undirected circuit decomposition therefore cannot recover the directed witness. This proves only a witness insufficiency statement; it does not prove that no orientation-preserving collapse exists when enriched data are retained.

## 15. Repeated and equal supports

Suppose `F_a=F_b` as edge sets with `a != b`. Since every root pair has two distinct indices, the `a`- and `b`-occurrences are different face discs even when their boundaries have the same edge sequence. They may be the two sides of all their common edges. Flattening them to one set would destroy exact occurrence multiplicity and can destroy the orientation statement.

The candidate correctly retains them separately.

## 16. Empty supports

An empty indexed support has no dart, no `rho`-orbit, no boundary component, and no face disc. It contributes no orientation equation. Retaining its index as bookkeeping does not alter the surface or cochain spaces.

## 17. Disconnected-union test

For a disjoint union `G=G_1 disjoint_union G_2`:

- the surface is `S_{g_1} disjoint_union S_{g_2}`;
- `C^1`, `Cut`, `B_f`, and the orientation stress split as direct sums;
- orientability holds iff it holds on both components;
- the labelled kernel contains one independent constant affine translation per edge-bearing component.

This confirms the componentwise formulas and rules out a hidden connectedness assumption in the obstruction theory.

## 18. Loop test

The obstruction chapters exclude loops. Under the declared external convention, a loop has two opposite darts and is restored by two singleton directed loop circuits, one per dart direction. This gives coverage two with opposite directions.

The convention is mathematically consistent but not part of the current Lean statement. Any theorem stated for graphs with loops must repeat it explicitly.

## 19. Open-boundary challenge

No argument in the candidate determines whether `Omega_f` vanishes for every fixed flow. The `K_4` example has vanishing `Omega_f`; it supplies no nonvanishing fibre. Likewise no argument chooses, for an arbitrary graph, some flow with vanishing `Omega_f`.

The two Research Lead obligations are therefore genuine and exhaustive at the stated orientation layer:

- universal fixed-fibre vanishing or an exact counterexample;
- graph-level existence of at least one favourable flow if universal vanishing fails.

## Boundary-check conclusion

No material counterexample to the fixed-lift, fixed-fibre, duality, `K_4`, or enriched-collapse theorems was found. The `rho`-orbit and unlabelled-coset tests expose local statement defects only; both have exact repairs without new mathematics.