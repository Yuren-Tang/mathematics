# AC-OR1 dependency and frontier map

## 1. Incoming theorem interfaces

```text
Programme A rank-three compatibility
→ nonempty compatible labelled-lift fibre.

retained dart/support data
→ partner involutions and rotations
→ indexed cycle-face surface reconstruction.

B4 fixed-flow torsor
+ B4 gauge/partial-Petrial correspondence
→ exact motion of edge-band twist words.

Programme A collapse datum
→ support-only cut transport
and, after retaining directed face occurrences,
→ enriched oriented collapse.
```

Compatibility existence, vertical motion, and collapse transport are logically different interfaces.

## 2. Fixed-lift DAG

```text
compatible labelled lift g
+ retained indexed face occurrences
+ partner / sigma / rho data
→ closed cellular surface S_g
→ choose vertex-disc orientations
→ twist word w(g) in C^1(G)
→ vertex reversals add Cut(G)
→ omega(g)=[w(g)] in C^1(G)/Cut(G).
```

```text
omega(g)=0
↔ w(g) in Cut(G)
↔ zero pairing with every source cycle
↔ S_g orientable
↔ retained face occurrences traverse every edge in opposite directions.
```

This is a theorem about a prescribed lift and its retained face occurrences.

## 3. Fixed-fibre DAG

```text
fixed flow f
→ compatible lifts form an H_f^0 torsor
→ Lambda_f:H_f^0→C^1(G)
→ B_f=im Lambda_f.
```

```text
gauge/Petrial theorem
→ w(g^k)=w(g)+Lambda_f(k)
→ omega(g^k)=omega(g)+[Lambda_f(k)].
```

```text
orientable labelled lifts
= Lambda_or^{-1}(omega(g))
→ empty or k_0+ker Lambda_or.
```

```text
change base lift inside the fibre
→ quotient by B_f
→ Omega_f in C^1(G)/(Cut(G)+B_f).
```

```text
Omega_f=0
↔ fixed f-fibre contains an orientable lift.
```

The labelled inverse-image torsor and the unlabelled coset

$$
\lambda_0+(\mathcal B_f\cap\operatorname{Cut}(G))
$$

must remain separate.

## 4. Dual criterion

```text
(Cut+B_f)^perp
= Z_1(G) intersection B_f^perp
= Stress_or(f).
```

Hence

```text
Omega_f=0
↔ w(g) annihilates Stress_or(f).
```

Programme A compatibility stress tests nonemptiness of the compatible-lift fibre. `Stress_or(f)` tests whether that nonempty fibre meets the orientable locus. No equality between the two stress theories is assumed.

## 5. Exact $K_4$ branch

```text
standard K_4 Fano flow f
├─ g_0: three Hamiltonian four-cycle faces
│       chi=1, projective plane, omega(g_0) nonzero
└─ k_u=u, Lambda_f(k)=1_E
        → g_1: four triangular faces
          chi=2, tetrahedral sphere, omega(g_1)=0.
```

Consequences:

- per-lift automatic orientability is false;
- the gauge action changes orientation class;
- the example has $\Omega_f=0$ and is not a fixed-fibre counterexample.

## 6. Outer-shell DAG

### Existing support-only route

```text
indexed even supports upstairs
→ discard directions, partner maps, and rotations
→ project cut-even supports
→ generic undirected circuit decomposition
→ ordinary CDC downstairs.
```

This route proves the ordinary CDC theorem and carries no orientation witness.

### Enriched oriented route

```text
orientable retained face occurrences upstairs
→ directed face circuits
→ delete auxiliary fibre edges and project lifted edges
→ empty word or directed closed trail downstairs
→ direction-preserving directed-trail decomposition
→ oriented CDC downstairs
→ two opposite singleton-loop darts per deleted loop.
```

The enriched route does not change the existing ordinary CDC theorem; it adds a conditional oriented conclusion when an orientable lift exists.

## 7. Exact Research Lead frontier

### `AC-RL-OR-FIXED-FIBRE-VANISHING`

Determine whether

$$
\Omega_f=0
$$

for every nowhere-zero rank-three flow on every finite bridgeless cubic multigraph, or construct an exact fixed-fibre counterexample.

### `AC-RL-OR-GRAPH-EXISTENCE`

If fixed-fibre vanishing fails, determine whether every finite bridgeless cubic multigraph admits some nowhere-zero rank-three flow $f$ with

$$
\Omega_f=0.
$$

These are genuine new-mathematics obligations. They are not PDL proof-expansion gaps and are not closed by the $K_4$ example.

## 8. Separation from the five-support frontier

The existing six five-support obligations remain unchanged:

- `AC-RL-BBD-GROUPOID-CLOSURE`;
- `AC-RL-BBD-VARIATION-SLICE`;
- `AC-RL-TYPE-T-SERIALISATION`;
- `AC-RL-FLAT-POTENTIAL-INTERFACE`;
- `AC-RL-COMMON-CUT-LOCALISATION`;
- `AC-RL-TYPE-H-COMMON-WITNESS`.

OR1 refines the eight-support cycle-face output by orientation data. It neither proves nor is required by the five-support theorem.

## 9. Completion status

Closed at authorial proof level:

- retained-data surface reconstruction;
- fixed-lift obstruction and oriented-face criterion;
- gauge law;
- fixed-fibre quotient and empty-or-torsor classification;
- orientation-stress duality;
- exact $K_4$ same-fibre theorem;
- enriched oriented collapse and loop reinsertion convention.

Open:

- universal fixed-fibre vanishing;
- graph-level existence of some orientable affine lift.
