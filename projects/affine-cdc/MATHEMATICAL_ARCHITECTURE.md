# AffineCDC mathematical architecture

## 1. Project scopes

1. **Affine compatibility core** — compatible affine families above nowhere-zero binary flows.
2. **Complete Cycle Double Cover theorem** — Programme A.
3. **Orientation refinement** — orientability of retained cycle-face surfaces and orientation-preserving outer transport.
4. **Five-support strengthening** — five indexed even supports, equivalently an $R_5$-valued flow.

Programme A is complete at paper level. The orientation refinement has a complete fixed-lift/fixed-fibre obstruction theory but open global existence. The five-support strengthening remains open and is not used in Programme A.

## 2. Current alignment

The orientation candidate is based exactly on

`curation/affine-cdc-programme-a-b1-b8-unified-v1@ec765cd03271abd3588ec36faec3d53d0f8aa03b`

and consumes the OR1 authorial epoch

`proof-development/affine-cdc-rigour-v1@9dc0b3a5c906e51f8f1816e00b85f7aa2a744b1b`.

DAG registration `29657f08253df87baa37ad09c88cce25904c189a` supplies dependency metadata only. B9 and unrelated PDL working-ahead material remain excluded.

## 3. Programme A — complete ordinary CDC

Controlling theorem:

> Every multigraph with finite active edge set and no singleton cut has a finite circuit double cover.

The controlling proof chain is:

```text
finite-active multigraph and circuit semantics
→ loop deletion
→ port-cycle cubic expansion
→ Seymour six-flow on finite connected loopless multigraph components
→ integral eight-flow
→ Z/8Z flow
→ internal equal-order transport to F₂³
→ affine pair complex
→ rank-three compatibility
→ graph/dart indexed support extraction
→ loopless parity adapter
→ cut-even collapse
→ circuit decomposition
→ loop reinsertion.
```

Independent Audit A verified the original spine subject to named Seymour input and three non-blocking explicitness repairs. Those repairs are integrated without theorem change; their prose has not been separately re-audited.

## 4. Orientation layer — natural placement

The orientation layer starts before Programme A discards the retained face-occurrence data.

```text
rank-three compatible labelled lift g
+ retained support index / partner / sigma / rho data
→ indexed cycle-face surface S_g
→ fixed-lift twist class omega(g).
```

It also consumes B4 vertical motion:

```text
fixed flow f
→ H_f^0 lift torsor
→ Lambda_f gauge code
→ partial Petrials
→ fixed-fibre obstruction Omega_f.
```

Finally it refines the outer shell:

```text
orientable retained face occurrences upstairs
→ enriched directed projection through collapse
→ directed closed trails
→ direction-preserving circuit decomposition
→ oriented CDC downstairs.
```

The support-only route remains the correct and sufficient architecture for the ordinary CDC theorem. The enriched route is a conditional refinement, not a replacement.

## 5. Fixed-lift object

For a compatible lift $g$, choose vertex-disc orientations and record the edge-band twist word $w(g)\in C^1(G)$. Vertex-disc reversals add cuts, so

$$
\omega(g)=[w(g)]\in C^1(G)/\operatorname{Cut}(G).
$$

The following are equivalent:

- $S_g$ is orientable;
- $w(g)$ is a cut;
- $\omega(g)=0$;
- all source-cycle twist holonomies vanish;
- the retained face occurrences traverse every edge in opposite directions.

The retained occurrences and rotations are essential. A generic decomposition of the underlying even supports is a different witness.

## 6. Fixed-flow fibre object

For fixed $f$, compatible labelled lifts form a torsor under $H_f^0$. The map

$$
\Lambda_f:H_f^0\to C^1(G)
$$

has image $\mathcal B_f$ and satisfies

$$
w(g^k)=w(g)+\Lambda_f(k)
$$

for transported local orientations.

The base-independent obstruction is

$$
\Omega_f\in C^1(G)/(\operatorname{Cut}(G)+\mathcal B_f).
$$

The fixed fibre contains an orientable lift if and only if $\Omega_f=0$.

- labelled orientable lifts: empty or one coset of $\ker\Lambda_{\mathrm{or}}$;
- unlabelled orientable Petrial words: empty or one coset of $\mathcal B_f\cap\operatorname{Cut}(G)$.

These classifications and the two obstruction classes have different quantifiers and must remain separate.

## 7. Orientation duality and counterexample

Define

$$
\operatorname{Stress}_{\mathrm{or}}(f)
=Z_1(G)\cap\mathcal B_f^\perp.
$$

Then $\Omega_f=0$ exactly when $w(g)$ annihilates every orientation stress. This is not Programme A's compatibility stress: compatibility decides whether the lift fibre exists; orientation stress decides whether it meets the orientable locus.

For the standard $K_4$ flow, the same fibre contains:

- a projective-plane lift with three four-cycle faces;
- a tetrahedral-sphere lift with four triangular faces.

Thus per-lift automatic orientability is false, but the example has $\Omega_f=0$ and is not a fixed-fibre counterexample.

## 8. Orientation frontier

Open:

- `AC-RL-OR-FIXED-FIBRE-VANISHING` — universal vanishing for every prescribed flow, or an exact fixed-fibre counterexample;
- `AC-RL-OR-GRAPH-EXISTENCE` — existence, on every bridgeless cubic graph, of some flow with $\Omega_f=0$.

These are genuine Research Lead questions. Collapse transport is closed once enriched orientation data are retained.

## 9. B1--B2 foundation

B1 controls exact five-support objects and quantifiers: root flows, $K_5$ triangles, matching/four-flow data, Fano-plane criteria, cycle-face surfaces, prescribed-dual holonomy, and old-colour factorability.

B2 enlarges the witness box to anisotropic $O^-(4,2)$ flows, quadratic cycle solutions, and cographic cycle-continuous maps; it separates fixed singular/Schur criteria and stress/Fourier dual layers. The false universal $2r$ orthogonal theorem remains superseded by the $q-2$ deleted permutation module.

## 10. B3--B8 five-support architecture

For fixed compatible lift $g$,

$$
J_g\to\mathscr A_5
\Longrightarrow
T_g^{(1)}\to\mathscr A_5
\Longrightarrow
\text{five-support cover}.
$$

$T_g^{(1)}$ is the full componentwise dual; $J_g$ is only the old-colour quotient.

B4 supplies vertical torsors, partial Petrials, connected-cycle switches, support pivots, and exact composite endpoint formulas. B5 supplies the cubic/four-pole interface, cap forcing, pairing alignment, and routing structure. B6 retains individual holonomy, root-fibre/Tait, Type H soluble escape, and DDD atoms, with the two BBD corrections. B7 retains rank/curvature theorems but not source localization or bounded composition. B8 normalizes finite assurance.

The six five-support obligations remain:

- `AC-RL-BBD-GROUPOID-CLOSURE`;
- `AC-RL-BBD-VARIATION-SLICE`;
- `AC-RL-TYPE-T-SERIALISATION`;
- `AC-RL-FLAT-POTENTIAL-INTERFACE`;
- `AC-RL-COMMON-CUT-LOCALISATION`;
- `AC-RL-TYPE-H-COMMON-WITNESS`.

## 11. Assurance boundary

Programme A's original spine passed Independent Audit A. B1--B8 remain pending Audit B. OR1 is `AUTHORIAL / CURATOR-INTEGRATED / READY-FOR-INDEPENDENT FIXED-CORPUS AUDIT`. The Lean checkpoint machine-checks retained dart/rotation ingredients and support-level extraction, not $\omega$, $\Omega_f$, orientation stress, the $K_4$ classification, enriched collapse, or global existence. No manuscript, publication, release, arXiv, DOI, novelty, timestamp, or canonical `main` status is created.
