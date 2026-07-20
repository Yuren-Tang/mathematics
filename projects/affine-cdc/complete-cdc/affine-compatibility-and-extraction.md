# Affine compatibility and graph-level even-support extraction

## 1. Cubic binary-flow data

Let `G` be a finite loopless cubic multigraph, not necessarily connected, and let

`f:E(G) → Γ\{0}`

be a nowhere-zero flow with `Γ = F₂³`. At a cubic vertex the three incident values are distinct nonzero vectors summing to zero; hence they are exactly the three nonzero points of a two-dimensional plane.

For an edge `e`, define the quotient plane

`Q_e = Γ / <f(e)>`.

The incidence space is the direct sum of one copy of `Q_e` for every vertex-edge incidence. Because the graph is loopless, every edge contributes exactly two dart summands, one at each endpoint.

## 2. Local affine families

At a vertex `v`, let the three incident flow directions be the nonzero elements of a plane `W_v`. For each incident edge direction `h`, the other two directions have the same class in `Q_h`; denote that class by `κ_{v,h}`.

The diagonal quotient map

`Δ_v: Γ → ⊕_{e incident to v} Q_e`

sends a point `m` to its three quotient classes. It is injective because the three direction lines have trivial common intersection. Let `L_v` be its image and `κ_v` the tuple of the distinguished classes.

### Theorem 2.1 — local-family torsor

The complete set of local even affine line families at `v` is exactly

`κ_v + L_v`.

A point parameter `m` translates the distinguished direction-`h` line by `[m]_h`. Every point of `Γ` lies on zero or two of the resulting three lines. Conversely, the local evenness condition reconstructs a unique deleted-point parameter.

Thus the local family space is an affine torsor under `L_v ≅ Γ`.

## 3. The affine pair complex

Let

- `E_f` be the incidence space;
- `L_vert` be the direct sum of the vertex translation spaces `L_v`;
- `κ` be the direct sum of the local offsets `κ_v`;
- `L_edge` be the direct sum, over edges `e=uv`, of the diagonal subspaces `{(x,x):x∈Q_e}`.

An incidence tuple is locally valid exactly when it lies in `κ + L_vert`; it is edge-compatible exactly when it lies in `L_edge`.

### Theorem 3.1 — affine compatibility intersection

Globally compatible local families are exactly

`(κ + L_vert) ∩ L_edge`.

Define the two-term pair complex

`P_f : L_vert ⊕ L_edge → E_f`,  `(ℓ,m) ↦ ℓ+m`.

Then

- `H⁰(P_f) = L_vert ∩ L_edge`;
- `H¹(P_f) = E_f / (L_vert + L_edge)`.

### Theorem 3.2 — obstruction and moduli

Compatible local families exist exactly when the distinguished class `[κ]` vanishes in `H¹(P_f)`. When nonempty, the compatible-family space is a torsor under `H⁰(P_f)`.

This is the complete centre of the compatibility problem, but it is not the whole graph-theoretic source object. A bare pair complex does not retain named vertices, edge objects, dart pairing, local-line interpretation, or support indices. The data `(G,Γ,f)` remain attached through graph-level extraction.

## 4. Quotient equation and stress dual

Quotienting the pair complex by the edge diagonal identifies the degree-one quotient with `⊕_e Q_e`. A vertex parameter tuple `(m_v)` has edge differential

`(δ_f m)_e = [m_u + m_v]_e`

for `e=uv`. Let `c_f` be the edgewise difference of the two endpoint offsets.

### Theorem 4.1 — quotient equation

A vertex parameter tuple gives a compatible family exactly when

`δ_f m = c_f`.

Thus the pair-complex obstruction and the quotient cokernel obstruction are the same.

Dually, identify `Q_e*` with the covectors on `Γ` annihilating `f(e)`. An equilibrium stress is an edge labelling by such covectors whose incident covectors sum to zero at every vertex.

### Theorem 4.2 — Fredholm criterion

Compatibility holds exactly when every equilibrium stress annihilates `κ`.

This stress presentation, the quotient equation, and the affine intersection are equivalent representations of one obstruction.

## 5. Canonical rank-three quadratic geometry

Every binary plane `Q_e` carries the canonical anisotropic quadratic form

- value zero at the zero vector;
- value one at every nonzero vector.

Its polar form is the unique nonzero alternating form on the plane and is nondegenerate.

For a vertex plane `W`, the direct sum of its three edge quotient planes is a six-dimensional nondegenerate quadratic space. The image `L_W` of the diagonal map `Γ → ⊕_{h∈W\{0}} Q_h` is a Lagrangian subspace.

The restriction of the quadratic form to `L_W` is the unique nonzero linear functional with kernel `W`. The distinguished local offset has exactly the corresponding polar pairing with `L_W`.

### Theorem 5.1 — local characteristic torsor

The local affine family is the characteristic torsor of the local Fano Lagrangian:

`κ_W + L_W = Char_q(L_W)`.

## 6. Characteristic-torsor intersection

Let `(E,q)` be a finite-dimensional nondegenerate quadratic space over `F₂`, with polar form `B`, and let `L` be Lagrangian. The characteristic torsor is

`Char_q(L) = {a : B(z,a)=q(z) for all z∈L}`.

It is a nonempty affine torsor under `L`.

### Theorem 6.1 — abstract intersection criterion

For Lagrangians `L` and `M`,

`Char_q(L) ∩ M` is nonempty

if and only if `q` vanishes on `L ∩ M`.

If `M` is totally singular, the intersection is automatically nonempty.

Proof: if a characteristic vector lies in `M`, isotropy of `M` forces `q=0` on `L∩M`. Conversely, vanishing on the intersection makes a characteristic representative orthogonal to `L∩M`; the identity `(L∩M)⊥ = L+M` yields a decomposition into an `L` part and an `M` part, producing an intersection point.

## 7. Automatic rank-three compatibility

On the global incidence space, take the direct sum of the canonical quotient quadratics.

- `L_vert` is Lagrangian and `κ + L_vert = Char_q(L_vert)`.
- For each edge, the endpoint diagonal is a totally singular Lagrangian in the two copies of `Q_e`.
- Therefore `L_edge` is a totally singular global Lagrangian.

### Theorem 7.1 — rank-three Fano compatibility

There exists

`x ∈ (κ + L_vert) ∩ L_edge`.

Hence every finite loopless cubic multigraph carrying a nowhere-zero `F₂³` flow admits a globally compatible collection of local affine even families. The full solution set is a torsor under `L_vert ∩ L_edge`.

No connectedness hypothesis is used. Every construction is a direct sum over edge-bearing components.

The quadratic handshaking proof and equilibrium-stress cancellation are lower-resolution projections of the same characteristic-torsor identity.

## 8. From compatible lines to graph supports

Retain the original graph and dart pairing. A compatible family assigns to every incidence `(v,e)` an affine line in `Γ` of direction `f(e)`. Edge compatibility makes the two endpoint lines equal; call the resulting two-point edge line `L_e`.

For each point `s∈Γ`, define

`F_s = {e∈E(G) : s∈L_e}`.

This gives an eight-index family `(F_s)_{s∈F₂³}`.

### Theorem 8.1 — local parity

For every vertex `v` and point `s`, the support `F_s` contains zero or two edges incident with `v`.

The three incident edge objects occupy the three distinct local direction slots. Local family evenness says that `s` lies on an even number of the three lines, hence zero or two.

### Theorem 8.2 — exact edge multiplicity

Every edge belongs to exactly two indexed supports.

Indeed the indices containing `e` are precisely the two points of its affine line `L_e`.

This is occurrence multiplicity. Equal supports at different point indices remain distinct occurrences. Empty supports are retained. Passing to the image multiset forgets index names but preserves one occurrence per index and therefore preserves exact edge multiplicity.

## 9. Dart-level retained-data boundary

The compatible dart set for one point is closed under the edge-reversal involution, so it descends to edge objects. At every selected dart there is a unique other selected dart at the same cubic vertex, giving a finite rotation structure.

The complete theorem uses only:

- edge-reversal closure for dart-to-edge descent;
- local evenness for support parity;
- two-point edge lines for multiplicity two.

It does not decompose the dart rotations into circuits before collapse. Circuit structure is not stable under the later fibre collapse.

This explains why graph/dart data cannot be discarded after forming the abstract pair complex.

## 10. The exact parity adapter

The current companion graph API counts an incident edge object once at a vertex. Intrinsic multigraph parity counts endpoint occurrences and therefore counts a loop twice.

### Theorem 10.1 — loopless equivalence

On a loopless multigraph, for every finite support:

`once-per-edge vertex-even`

if and only if

`intrinsic half-edge boundary-even`

if and only if

`cut-even`.

The first equivalence holds because every incident nonloop edge contributes exactly one endpoint occurrence. The second is the intrinsic cut-parity theorem from the foundations chapter.

Therefore every support `F_s` extracted above is cut-even, and the eight-index family is an intrinsic even double cover of the cubic graph.

Looplessness is exact. A singleton loop is intrinsically boundary-even and cut-even but is counted once by the once-per-edge incidence set. Loops remain under the separate deletion/reinsertion interface.

## 11. Formal correspondence boundary

The companion Lean checkpoint machine-checks substantial slices:

- local affine-family classification and translation;
- the original branching/cross-bit rank-three compatibility proof;
- dart gluing and edge-reversal closure;
- point-indexed dart supports and exact two-point coverage;
- graph-level support extraction in the cubic-flow setting.

The integrated invariant pair-complex and characteristic-torsor presentation is a complete authorial paper proof. It is not thereby a checked theorem in this form, and it does not make the full outer theorem machine-checked.

## 12. Exported interface

The final chapter may use:

1. a globally compatible collection of local affine families on the expanded cubic graph;
2. an eight-index family of finite graph edge supports;
3. intrinsic cut-evenness of every support;
4. exact occurrence multiplicity two at every expanded edge;
5. preservation of empty and repeated indexed members;
6. explicit graph, edge-object, incidence, and dart data;
7. no prior circuit decomposition.

## 13. Assurance and provenance

This chapter integrates A4–A7. The principal later independent-audit targets are:

- the local-family classification and its exact quotient formula;
- the characteristic cross-pairing in the Fano plane;
- the abstract characteristic-torsor intersection theorem;
- dart-to-edge descent and exact occurrence counting;
- the loopless boundary/cut parity adapter.

These are audit targets, not known defects.