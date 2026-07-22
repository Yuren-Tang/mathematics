# AC-RL reactivation and regional Stokes frontier checkpoint

## Control

- Active programme issue: `Yuren-Tang/research-workbench#41`
- PORT-DIR reactivation comment consumed: `5038619692`
- AC-RL ACK comment: `5043719842`
- Exact reactivation head: `034bf45d76d89a667cc3e7503e7d3b16047bd117`
- Continuing branch: `research/affine-cdc-five-cdc-v1`

## New branch-native theorem chain after reactivation

1. `PHYSICAL_TRANSLATION_WORD_STOKES_V1.md`
   - explicit affine `A3` translation cocycle;
   - frame translation word `Theta_fr`;
   - reduction to three six-step translation generators;
   - finite regional Stokes theorem;
   - nonsplitting of the four-bit curvature sequence;
   - correction from an absolute odd lift to a torsor-valued Stokes target.

2. `PHYSICAL_TRANSLATION_CELL_ANALYSIS_V1.md`
   - exact parallel-challenge identity
     `H_(lambda+delta)=H_lambda triangle H_delta`;
   - canonical closed scalar subgraph for each weight-two matching direction.

3. `LOCKED_SCALAR_COMPONENT_ROUTING_V1.md`
   - componentwise Boolean-cube toggles;
   - pair-changing versus pair-preserving dichotomy;
   - interlacing implies route change;
   - irreducible pair-preserving families must be laminar.

4. `MINIMAL_LAMINAR_INTERVAL_SURGERY_V1.md`
   - minimal laminar component has a four-port binary interface;
   - crossing side attachments return to the escape branch;
   - the remaining obstruction is a separated/four-port side-root signature;
   - explicit descent target for replacement, separator, DDD/defect atom, or profile escape.

## Current exact frontier

The finite algebra, state space, and holonomy languages are no longer the main bottleneck. The live source-graph theorem is:

`minimal laminar four-port interval + side-root signature`

must yield one of:

- root-admissible smaller replacement;
- composition-safe cyclic separator/four-pole;
- bounded DDD/zero/co-root defect unit;
- Kempe/profile escape.

The next research direction is to control the external side-root signature by the existing root-fibre and enriched co-root-strip machinery, without enlarging the routing alphabet.

No canonical corpus, main, Lean, manuscript, release, DOI, or publication surface was changed.
