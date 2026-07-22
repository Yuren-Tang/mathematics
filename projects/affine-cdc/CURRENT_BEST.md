# AffineCDC current mathematical state

## 1. Current integrated candidate

Current candidate branch:

`curation/affine-cdc-orientation-obstruction-v1`.

Exact base:

`curation/affine-cdc-programme-a-b1-b8-unified-v1@ec765cd03271abd3588ec36faec3d53d0f8aa03b`.

OR1 source:

`proof-development/affine-cdc-rigour-v1@9dc0b3a5c906e51f8f1816e00b85f7aa2a744b1b`.

The candidate preserves Programme A and B1--B8 and adds the orientation-obstruction layer only.

## 2. Complete CDC line

Programme A proves:

> Every multigraph with finite active edge set and no singleton cut has a finite circuit double cover.

The original candidate `68715fb29bb4b6555e2bc3e089603c5390d01566` passed Independent Audit A at `2fac31f4e76c819dd42a179a2772501c50ee93ad`, with result

`VERIFIED SUBJECT TO NAMED EXTERNAL THEOREMS / NON-BLOCKING EXPLICITNESS REPAIRS`.

The three explicitness repairs are closed and integrated:

1. exact Seymour loopless-multigraph convention, parallel edges permitted, componentwise assembly explicit;
2. complete A4 reverse local-family reconstruction;
3. old Tutte route historical and non-controlling.

They change no theorem or dependency. Seymour remains the sole non-elementary external logical input. The repaired prose has not been separately re-audited.

## 3. Orientation refinement of compatible lifts

For a finite loopless cubic multigraph $G$, a nowhere-zero rank-three flow $f$, and one compatible labelled lift $g$:

1. the retained indexed support occurrences together with $\operatorname{partner}$, $\sigma$, and $\rho$ reconstruct a closed cellular cycle-face surface $S_g$;
2. choosing vertex-disc orientations gives $w(g)\in C^1(G)$, well defined modulo cuts;
3. the fixed-lift class is
   $$
   \omega(g)=[w(g)]\in C^1(G)/\operatorname{Cut}(G);
   $$
4. $S_g$ is orientable exactly when $\omega(g)=0$, equivalently when the retained face occurrences traverse every edge once in each direction.

This criterion uses retained face occurrences, not a generic decomposition of the underlying supports.

## 4. Fixed-flow fibre classification

The compatible labelled lifts above fixed $f$ form a torsor under $H_f^0$. The gauge map

$$
\Lambda_f:H_f^0\to C^1(G)
$$

has image $\mathcal B_f$ and obeys

$$
w(g^k)=w(g)+\Lambda_f(k)
$$

for transported local orientations.

The base-independent fibre obstruction is

$$
\Omega_f\in C^1(G)/(\operatorname{Cut}(G)+\mathcal B_f).
$$

The fibre contains an orientable lift exactly when $\Omega_f=0$.

- labelled orientable lifts are empty or one coset of $\ker\Lambda_{\mathrm{or}}$;
- unlabelled orientable Petrial words are empty or one coset of $\mathcal B_f\cap\operatorname{Cut}(G)$.

These are different quotients. Likewise, $\omega(g)$ and $\Omega_f$ are different obstruction classes.

The dual orientation stress is

$$
\operatorname{Stress}_{\mathrm{or}}(f)
=Z_1(G)\cap\mathcal B_f^\perp.
$$

It tests orientability within an already compatible fibre and is not the Programme A compatibility stress.

## 5. Exact $K_4$ boundary

For the standard $K_4$ Fano flow, one compatible lift has three Hamiltonian four-cycle faces and gives the projective plane; another lift in the same fixed-flow fibre has four triangular faces and gives the tetrahedral sphere.

Therefore:

- per-lift automatic orientability is false;
- the gauge action genuinely changes $\omega(g)$;
- this example is not a fixed-fibre counterexample, because the sphere lift shows $\Omega_f=0$.

## 6. Oriented outer-shell transport

The existing Programme A support-only collapse retains cut parity and exact multiplicity but discards directed face occurrences, partner maps, and rotations before generic undirected decomposition. It proves no oriented witness.

An enriched route does hold:

```text
oriented retained face circuits upstairs
→ project lifted directed edges through collapse
→ directed closed trails downstairs
→ direction-preserving trail decomposition
→ oriented CDC downstairs.
```

Deleted loops are reinserted as two singleton loop occurrences in opposite dart directions.

The unresolved theorem is orientable-lift existence, not collapse transport.

## 7. Five-support object and witness hierarchy

For finite loopless cubic multigraphs, five indexed even supports are equivalent to root flows, $K_5$ triangle labellings, exact matching/four-flow data, existential Fano-flow/plane data, existential cycle-face surfaces with a full-dual map to $\mathscr A_5$, anisotropic $O^-(4,2)$ flows, quadratic cycle solutions, and cographic cycle-continuous edge maps.

Singular/Schur formulations are fixed-data criteria. Stress/Fourier are dual solvability/counting layers. The false universal $2r$ orthogonal theorem remains superseded by the $q-2$ deleted-permutation-module theorem.

## 8. B3--B8 retained state

- B3 retains the full-dual/factorable hierarchy, exact target links, capacity, eight-vertex factorable classification, unused-matching/core theory, and conditional flower obstruction. The correct all-parallel matching is $\{01,23,45\}$.
- B4 retains the $H_f^0$ torsor, gauge/Petrial motion, connected/composite switch distinction, support pivots, and new-fibre recomputation.
- B5 retains cubic local law, three-cut gluing, ten four-pole states, profile intersection, cap forcing, pairing alignment, routing weights, and uniform-routing elimination.
- B6 retains individual holonomy, root-fibre/Tait, Type H soluble escape, and DDD atom theorems. BBD common origin is conditional on `AC-RL-BBD-GROUPOID-CLOSURE`; the nontrivial defect forest is removed pending `AC-RL-BBD-VARIATION-SLICE`.
- B7 retains rank-one impossibility, rank-two Tait escape, and the full-rank flat/nonflat curvature dichotomy. Source localization and composition remain open.
- B8 retains the finite assurance classes without upgrading audit or reproducibility.

## 9. Exact open obligations

### Five-support frontier

- `AC-RL-BBD-GROUPOID-CLOSURE`;
- `AC-RL-BBD-VARIATION-SLICE`;
- `AC-RL-TYPE-T-SERIALISATION`;
- `AC-RL-FLAT-POTENTIAL-INTERFACE`;
- `AC-RL-COMMON-CUT-LOCALISATION`;
- `AC-RL-TYPE-H-COMMON-WITNESS`.

### Orientation frontier

- `AC-RL-OR-FIXED-FIBRE-VANISHING`;
- `AC-RL-OR-GRAPH-EXISTENCE`.

The two frontiers are distinct. The global five-support theorem and global oriented-existence theorem remain open.

## 10. Assurance

Programme A's original theorem spine passed Audit A; its repairs are integrated but not separately re-audited. B1--B8 remain pending dedicated Audit B. OR1 is an authorial proof package integrated by the Curator and ready for an independent fixed-corpus audit. The Lean checkpoint verifies retained dart/rotation ingredients and support-level extraction only, not the obstruction theory or enriched oriented collapse. No manuscript, publication, release, arXiv, DOI, novelty, timestamp, or canonical `main` status is created.
