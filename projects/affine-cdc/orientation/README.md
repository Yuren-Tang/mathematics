# AffineCDC orientation-obstruction layer

This directory records the orientation refinement of the rank-three affine/root-lift construction. It is logically downstream of compatible-lift existence and upstream of any oriented collapse conclusion.

## Controlling objects

For a finite loopless cubic multigraph $G$, a nowhere-zero $\mathbf F_2^3$-flow $f$, and a compatible labelled lift $g$:

- $S_g$ is the indexed cycle-face surface reconstructed from retained support occurrences and dart rotations;
- $w(g)\in C^1(G)$ is an edge-twist representative after choosing local vertex-disc orientations;
- $\omega(g)=[w(g)]\in C^1(G)/\operatorname{Cut}(G)$ is the obstruction of one fixed lift;
- $\Lambda_f:H_f^0\to C^1(G)$ is the gauge-word map and $\mathcal B_f=\operatorname{im}\Lambda_f$;
- $\Omega_f\in C^1(G)/(\operatorname{Cut}(G)+\mathcal B_f)$ is the base-independent obstruction of the whole fixed-flow fibre.

The two obstruction classes must not be conflated.

## Reading order

1. `surface-and-fixed-lift-obstruction.md` — exact retained-data reconstruction and $\omega(g)$;
2. `fixed-fibre-gauge-and-duality.md` — gauge law, $\Omega_f$, torsor/coset classification, and orientation stress;
3. `k4-and-oriented-collapse.md` — the exact $K_4$ counterexample, support-only data loss, enriched oriented collapse, and loop reinsertion.

## Exact source boundary

Authorial PDL checkpoint:

`proof-development/affine-cdc-rigour-v1@9dc0b3a5c906e51f8f1816e00b85f7aa2a744b1b`.

Dependency registration only:

`29657f08253df87baa37ad09c88cce25904c189a`.

Checked Lean reconstruction boundary:

`Yuren-Tang/affine-cdc:main@ebd7098a7a8b824e8c0a511d3c71f61705672aa8`.

Lean checks the retained dart/support/partner/rotation ingredients and the support-only graph extraction. It does not define $w$, $\omega$, $\Omega_f$, orientation stress, the $K_4$ fibre classification, or the enriched oriented-collapse theorem.

## Status

The fixed-lift and fixed-fibre obstruction theory is a Curator-integrated authorial proof package. It is ready for an independent fixed-corpus audit, but is not thereby independently audited or end-to-end Lean verified.

Global oriented existence remains open at exactly:

- `AC-RL-OR-FIXED-FIBRE-VANISHING`;
- `AC-RL-OR-GRAPH-EXISTENCE`.
