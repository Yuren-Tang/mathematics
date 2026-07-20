# Interior holonomy, corrected BBD scope, DDD atoms, and curvature

## 1. Individual-loop affine holonomy

For a four-pole `P`, indexed five-support chains with the same boundary differ by

$$
M_P=Z_1(P;\mathbf F_2)\otimes E_5.
$$

A lifted routing loop has support permutation `\pi\in S_5` and translation part `z\in M_P`, acting by

$$
u\longmapsto\pi u+z.
$$

If `m=\operatorname{ord}(\pi)`, the cyclic norm

$$
d=N_\pi z,
\qquad
N_\pi=1+\pi+\cdots+\pi^{m-1}
$$

is invariant under change of affine origin.

### Theorem 1.1 — individual cyclic classification

For monodromy types `2^21`, `41`, `32`, and `5`, the cyclic cohomology vanishes. Hence:

- `d\ne0` gives period doubling and a nontrivial pure translation after one permutation period;
- `d=0` gives an ambient action conjugate to the pure permutation.

This is an individual-loop ambient theorem. The conjugating origin need not preserve edgewise roots, and different physical loops are not thereby composed into one root-preserving group.

## 2. Root-fibre section problem

In the zero-norm case, root-admissible linearisation asks for a root-valued flow `r` satisfying

$$
(1+\pi)r=t_\gamma,
$$

where `t_\gamma` is the actual switch flow. Edge fibres and cubic zero-sum relations form a finite local system.

Failure may occur through:

1. an empty edge fibre;
2. nonempty edge fibres but an empty vertex relation;
3. locally nonempty relations with nontrivial component holonomy.

## 3. Genuine rainbow path family

A physical rainbow loop is the composite of three terminal-path switches `P_0,P_1,P_2`, with first and third coefficients equal. For independent `u,v\in E_5`,

$$
\boxed{
t_\gamma
=(P_0\triangle P_2)\otimes u
+P_1\otimes v.}
$$

Thus the physical switch flow lies in a two-plane and is much smaller than the unrestricted abstract tension universe.

### Theorem 3.1 — root lifting iff Tait resolution

A genuine zero-norm rainbow loop is root-admissibly linearizable exactly when its switch flow admits the corresponding Tait resolution.

- full-rank types are obstructed by uncovered edges;
- rank-one types are obstructed by missed vertices or odd component holonomy;
- for the genuine three-path word, the apparent extra closed-component branch disappears.

## 4. Type H soluble-branch escape

A Tait colouring yields a boundary state `B_i`. In every BBD deterministic triangle, two challenges that become the same physical symmetric-difference subgraph are required by the abstract policy to use different routes. One genuine switch therefore exits the triangle profile. In the DDD triangle, a Tait colouring immediately creates a `B_i` state outside the DDD profile.

### Theorem 4.1

$$
\text{zero norm}
+
\text{root-admissible linearisation}
\Longrightarrow
\text{strict Type H profile expansion}.
$$

The soluble zero-norm Type H branch is eliminated.

## 5. BBD simultaneous-origin correction

Earlier corpus text asserted an unconditional chain:

```text
all physical BBD loops generate a root-preserving affine group
→ pure translation kernel vanishes
→ one simultaneous common origin
→ one canonical E_5 flow.
```

This chain is not presently unconditional.

Individual ambient affine data do not automatically compose as physical root-preserving switch paths. Before the translation kernel or a simultaneous origin can be defined in the claimed way, one needs a closure theorem for the physical reconfiguration groupoid.

### Controlling conditional statement

Assuming `AC-RL-BBD-GROUPOID-CLOSURE`, the root-rigidity and cohomological argument may be applied to the resulting physical group. Without that premise, the simultaneous-origin conclusion is not an active theorem.

Exact open return:

`AC-RL-BBD-GROUPOID-CLOSURE`.

The finite BBD monodromy table remains valid as data about individual loops. It does not discharge this premise.

## 6. Defect-forest correction

The earlier variational domain was all `E_5` flows with the original terminal roots. The original root-valued cover itself lies in this domain and has zero defect.

Therefore minimizing the number of zero/co-root edges over that domain is vacuous and cannot produce a nontrivial canonical defect forest.

Restricting to a claimed simultaneous origin does not repair the proof automatically: it removes the arbitrary cycle toggles used in the minimization inequalities.

### Controlling status

The nontrivial defect-minimal forest and induced-tree theorem are removed from the active theorem layer pending a valid nontrivial holonomy-compatible variation space.

Exact open return:

`AC-RL-BBD-VARIATION-SLICE`.

Local finite facts about zero wires, co-root degree patterns, `K_6` coefficients, and Petersen endpoint transitions remain valid. They become theorem inputs only when a defect strip is independently supplied.

## 7. Conditional local defect geometry

The fifteen nonzero vectors of `E_5` identify with the fifteen edges of `K_6`: ten roots correspond to `K_5` edges and five co-roots to edges incident with the sixth vertex. Three distinct nonzero values sum to zero exactly when the corresponding `K_6` edges form a triangle or a perfect matching.

Consequently, if a co-root strip is independently supplied:

- internal degree-two transport moves through adjacent edges of the Petersen graph in its Kneser model;
- endpoint states form edges of `L(\mathrm{Petersen})`;
- each turn emits a side-root label.

State repetition alone does not imply pumping or deletion because the side-root output and attached components may differ.

## 8. DDD atoms and triality

A nondegenerate co-root atom is one co-root edge between two one-factor leaves. Its four terminal roots admit exactly three pairings:

- the original co-root realization;
- two crossed root-valued resolutions.

The fifteen atoms are equivariantly identified with the fifteen one-factors of `K_6`; the stabilizer is `D_8`.

### Theorem 8.1 — unique bad route

Under every full challenge, the original atom pairing is the unique route that remains bad. Both crossed routes rootify the atom.

This theorem is independent of the corrected BBD forest claim. A crossed resolution changes terminal incidence and still needs a composition theorem.

## 9. Locked quotient and rank escape

Conditional on the exact finite locked-challenge table, a universally route-locked atom quotient gives a nowhere-zero `\mathbf F_2^3` flow whose four terminal values equal one colour `g`.

### Rank one

Impossible.

### Rank two

Every rank-two plane through `g` has a root-triangle section. The resulting root lift is a Tait sector with boundary state `A` and escapes Type H.

Thus only full rank remains.

## 10. Full-rank curvature

For full-rank locked quotient `c`, the four scalar sheets define a curvature class `\Omega(c)` on the terminal-colour edge set `E_g`.

### Theorem 10.1 — flat branch

The following are equivalent:

1. `\Omega(c)=0`;
2. scalar side choices make every local four-bit word affine;
3. there is an eight-state potential `p` with the exact edge law
   $$
   p(u)+p(v)\in\{0,c(e)+g\}.
   $$

### Theorem 10.2 — nonflat branch

If `\Omega(c)\ne0`, duality supplies one support `\eta\subseteq E_g` that is simultaneously a cut in all four scalar sheets and has odd terminal parity. The terminal word is the nonzero class in `\mathbf F_2^4/E_4`.

## 11. Localization boundary

The B7 curvature theorem does not prove that `\eta`:

- is a cut in the original source four-pole;
- has bounded or connected support;
- yields a DDD, Whitney, transition-matroid, or other composition-safe factor;
- represents the physical `D_8` cohomology class.

Likewise, an eight-state potential does not by itself give a bounded interface; a potential fibre may carry unbounded internal semantics.

Exact open returns:

- `AC-RL-COMMON-CUT-LOCALISATION`;
- `AC-RL-FLAT-POTENTIAL-INTERFACE`;
- `AC-RL-TYPE-H-COMMON-WITNESS`.

The Type T branch separately retains `AC-RL-TYPE-T-SERIALISATION`.

## 12. DDD cohomology boundary

The physical DDD subgroup is `D_8`, and its one-dimensional affine exception remains a separate phenomenon. A canonical identification between that class and the B7 curvature bit is open. It is not inherited from any BBD simultaneous-origin claim.

## 13. Provenance and assurance

Programme B6 source:

`proof-development/affine-cdc-rigour-v1@404f7511f16d1225e066a91842a57e2084943c72`.

Programme B7 source:

`proof-development/affine-cdc-rigour-v1@164f7655f9ec7c0e0a73d49303cf66230fb26487`.

States retained:

- B6: `READY-FOR-CURATOR / MATHEMATICAL-CORRECTION / AC-RL-GAPS-EXPLICIT`;
- B7: `READY-FOR-CURATOR / AC-RL-GAPS-EXPLICIT / GLOBAL-COMPOSITION-OPEN`.

Individual-loop, root-fibre, Tait-escape, DDD triality, route-lock, rank, and curvature results are Curator-integrated authorial mathematics in the exact scopes above. BBD simultaneous origin is conditional; the nontrivial forest is not an active theorem. Finite challenge and monodromy tables retain their B8 assurance classes.

No independent-audit, Lean, manuscript, publication, release, arXiv, or DOI status is created.