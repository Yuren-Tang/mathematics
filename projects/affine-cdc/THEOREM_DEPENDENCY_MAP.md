# AffineCDC theorem and obligation dependency map

## 1. Programme A complete CDC DAG

```text
A0 finite-active multigraph, cut, circuit, and occurrence semantics
├─ A1 loop deletion and exact reinsertion
└─ A2 port-cycle cubic expansion and collapse data
   └─ A3 Seymour six-flow + internal order-eight transport
      └─ A4 affine pair complex and local-family classification
         └─ A5 rank-three compatibility
            └─ A6 graph/dart indexed support extraction
A0 + A6 → A7 loopless parity bridge
A2 + A6 + A7 → A8 collapse and multiplicity transport
A0 + A8 → A9 circuit decomposition
A1–A9 → A10 complete ordinary CDC theorem.
```

Audit A's three explicitness repairs clarify A3, A4, and the historical Tutte route without changing this DAG. Seymour remains the sole non-elementary external input.

## 2. OR1 retained-surface DAG

```text
A5 compatible labelled lift g
+ A6 retained indexed dart supports
+ partnerD / sigma / rho / rhoInv
→ OR1-A exact indexed cycle-face surface S_g.
```

```text
S_g
+ local vertex-disc orientations
→ twist word w(g) in C^1(G)
→ vertex reversals add Cut(G)
→ omega(g)=[w(g)] in C^1(G)/Cut(G).
```

```text
omega(g)=0
↔ w(g) in Cut(G)
↔ zero pairing with all z in Z_1(G)
↔ S_g orientable
↔ retained indexed face occurrences form an oriented CDC.
```

The last equivalence uses the retained face occurrences and circular cubic vertex links. It does not follow from a generic support decomposition.

## 3. OR1 fixed-fibre DAG

```text
fixed flow f
→ B4 labelled-lift torsor g+H_f^0
→ Lambda_f:H_f^0→C^1(G)
→ B_f=im Lambda_f.
```

```text
B4 gauge/partial-Petrial correspondence
→ w(g^k)=w(g)+Lambda_f(k)
→ omega(g^k)=omega(g)+[Lambda_f(k)].
```

```text
Lambda_or=q∘Lambda_f
→ orientable labelled lifts
  = Lambda_or^{-1}(omega(g))
→ empty or k_0+ker Lambda_or.
```

```text
change base lift within fixed f-fibre
→ quotient by B_f
→ Omega_f in C^1(G)/(Cut(G)+B_f)
→ fixed fibre contains orientable lift iff Omega_f=0.
```

Unlabelled orientable Petrial words form either the empty set or

$$
\lambda_0+\bigl(\mathcal B_f\cap\operatorname{Cut}(G)\bigr).
$$

This is not the same classification as the labelled lift torsor.

## 4. OR1 duality DAG

```text
(Cut(G)+B_f)^perp
= Z_1(G) intersection B_f^perp
= Stress_or(f).
```

```text
Omega_f=0
↔ <w(g),z>=0 for every z in Stress_or(f).
```

Using the integrated code identity,

$$
\operatorname{Stress}_{\mathrm{or}}(f)
=\mathcal C(G)\cap(\mathcal C(G)*\mathcal F_f).
$$

Programme A compatibility stress and OR1 orientation stress are distinct nodes: the former gives nonemptiness of the compatible-lift fibre; the latter tests intersection with the orientable locus.

## 5. OR1 $K_4$ branch

```text
standard K_4 Fano flow f
├─ g_0 → three four-cycle faces → chi=1 → projective plane
└─ k_u=u, Lambda_f(k)=1_E
   → g_1 → four triangular faces → chi=2 → sphere.
```

Hence one fixed fibre contains both orientability types. This refutes per-lift automaticity but proves no nonzero $\Omega_f$; in this example $\Omega_f=0$.

## 6. OR1 outer-shell DAG

### Support-only Programme A route

```text
A6 indexed even supports
→ A8 cut-even collapse and exact multiplicity
→ A9 generic undirected circuit decomposition
→ ordinary CDC.
```

This route discards face directions and rotations and therefore carries no orientation witness.

### Enriched orientation route

```text
OR1-B orientable retained face occurrences on H
+ A2 collapse datum
→ project directed lifted-edge sequences
→ empty word or directed closed trail on G_0
→ direction-preserving directed-trail decomposition
→ oriented CDC on G_0
→ opposite singleton-loop dart reinsertion.
```

Collapse transport is closed under the enriched hypothesis. The open arrow is existence of the orientable lift upstairs.

## 7. Exact orientation frontier

```text
AC-RL-OR-FIXED-FIBRE-VANISHING
→ decide whether Omega_f=0 for every fixed rank-three flow,
  or construct an exact fixed-fibre counterexample.
```

```text
if fixed-fibre vanishing fails:
AC-RL-OR-GRAPH-EXISTENCE
→ decide whether every bridgeless cubic graph has some flow f with Omega_f=0.
```

Either the stronger fixed-fibre theorem or the graph-existence theorem closes the orientation-existence input to the enriched outer route.

## 8. B1–B2 foundation DAG

```text
five supports
↔ R₅ flow
↔ K₅ triangles
↔ exact matching/four-flow data
↔ ∃ Fano flow/plane with empty compatibility obstruction
↔ ∃ cycle-face embedding with full-dual map to 𝒜₅
↔ anisotropic O⁻(4,2) flow
↔ quadratic cycle solution
↔ cographic cycle-continuous edge map.
```

Fixed singular/Schur branches retain quotient data. Stress and Fourier remain dual/counting interfaces. The false universal $2r$ orthogonal theorem is replaced by the $q-2$ lower bound and deleted permutation module.

## 9. B3 target DAG

```text
fixed lift g
↔ cycle-face surface S_g
↔ full dual T_g
→ componentwise same-embedding map T_g^(1) → 𝒜₅.
```

The old colouring gives $T_g^{(1)}\to J_g$, hence

```text
J_g → 𝒜₅
→ T_g^(1) → 𝒜₅
→ five-support cover.
```

No reverse implication to $J_g$ is automatic.

## 10. B4–B8 five-support DAG

B4:

```text
fixed f
→ H_f^0 torsor
→ reduced gauge code
→ accessible partial Petrials.

connected source cycle + direction
→ one horizontal switch
→ solve the new lift fibre.
```

A disconnected cycle word gives a commuting path, not one edge.

B5:

```text
cubic local law
→ three-cut gluing
→ ten four-pole states
→ profile intersection
→ cap forcing
→ path-pairing alignment
→ routing weights
→ uniform-routing elimination
→ Type T or Type H residual mechanism.
```

B6 retains individual holonomy/root-fibre/Tait and DDD chains. BBD common origin remains conditional on `AC-RL-BBD-GROUPOID-CLOSURE`; any nontrivial forest requires `AC-RL-BBD-VARIATION-SLICE`.

B7 retains rank-one impossibility, rank-two Tait escape, and the full-rank curvature dichotomy. Open arrows:

- `AC-RL-TYPE-T-SERIALISATION`;
- `AC-RL-FLAT-POTENTIAL-INTERFACE`;
- `AC-RL-COMMON-CUT-LOCALISATION`;
- `AC-RL-TYPE-H-COMMON-WITNESS`.

B8 retains the six finite assurance classes. B9 remains outside this candidate and blocked on global escape or strict source progress.

## 11. Assurance

Programme A's original spine passed Independent Audit A. B1--B8 remain pending dedicated Audit B. OR1-A through OR1-G are authorial Curator-integrated nodes ready for a fixed-corpus independent audit. Lean checks the retained dart and support ingredients only. No end-to-end Lean, manuscript, publication, release, arXiv, DOI, novelty, timestamp, or canonical movement follows.
