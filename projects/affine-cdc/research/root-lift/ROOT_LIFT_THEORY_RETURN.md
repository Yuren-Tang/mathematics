# AC-ROOT-LIFT-01 theorem-and-novelty return

## 1. Exact controls

- role: `AffineCDC — Root-Lift Theory Scout` (`AC-ROOT-LIFT-01`);
- controlling issue: `Yuren-Tang/research-workbench#50` and its later AC-DIR control correction;
- frozen mathematical input:
  `Yuren-Tang/mathematics:curation/affine-cdc-orientation-obstruction-v1@e6af5645107d0f21ac6c262c63a1db5dab8f0fd1`;
- owned branch:
  `Yuren-Tang/mathematics:research/affine-cdc-root-lift-v1`;
- exact base:
  `e6af5645107d0f21ac6c262c63a1db5dab8f0fd1`;
- write boundary:
  `projects/affine-cdc/research/root-lift/**` only.

The branch was verified identical to the exact base before the scout wrote. It was not recreated, reset, rebased, or moved.

Issue #56 was not used. Issue #51 is the sole independent orientation audit and may proceed in parallel. No audit success is assumed. OR1 is treated only as

`AUTHORIAL / CURATOR-INTEGRATED / NOT YET INDEPENDENTLY VERIFIED`.

The exact final scout SHA is recorded in the authoritative issue #50 return because a commit cannot contain its own SHA.

## 2. Delivered paths

1. `ROOT_LIFT_DEFINITIONS_AND_EQUIVALENCE.md`;
2. `MOD2_REDUCTION_AND_FIXED_WITNESS_OBSTRUCTION.md`;
3. `Q5_ORIENTED_FIVE_SUPPORT_SPECIALISATION.md`;
4. `Q8_FANO_SPECIALISATION.md`;
5. `LITERATURE_AND_NOVELTY_AUDIT.md`;
6. `ROOT_LIFT_THEORY_RETURN.md`.

No path outside the owned directory is changed.

## 3. Principal scope correction

The proposed strongest equivalence is too strong.

A full indexed oriented $q$-CDC contains circuit occurrence partitions and cyclic orders. An $A_{q-1}$ root flow canonically contains only the directed indexed Eulerian support words. Circuit decomposition exists but is generally nonunique.

The corrected canonical theorem is

$$
\boxed{
\text{directed indexed Eulerian $q$-support systems}
\longleftrightarrow
\text{$A_{q-1}$ root flows}.}
$$

A full oriented $q$-CDC is obtained after choosing directed circuit decompositions coordinatewise. Conversely, forgetting a full witness to its support word and root flow is generally many-to-one.

The exact four-parallel-edge example gives two different circuit pairings with the same root flow.

## 4. Theorem table

| ID | Statement | Result | Assurance |
|---|---|---|---|
| RL-1 | reference-independent definition of $A_{q-1}$ root flow | proved | scout proof |
| RL-2 | directed indexed Eulerian $q$-supports $\leftrightarrow A_{q-1}$ root flows | proved, mutually inverse | scout proof |
| RL-3 | finite root flow gives some full oriented $q$-CDC | proved after directed circuit decomposition | scout proof + classical decomposition |
| RL-4 | root flow canonically recovers a prescribed/full circuit witness | false | exact four-parallel-edge counterexample |
| RL-5 | multiplicity-two, distinct indices, repeated supports, and empty indices are retained | proved at support-word level | scout proof |
| RL-6 | mod-$2$ root flow $\leftrightarrow$ unordered $K_q$ roots $\leftrightarrow$ indexed even supports | proved | scout proof |
| RL-7 | even-$q$ nondegenerate target is $E_I/\langle\mathbf1\rangle$, dimension $q-2$ | proved | scout linear algebra |
| RL-8 | $q=4$ quotient identifies complementary roots; $q\ge6$ even retains weight-two root labels | proved | scout linear algebra |
| RL-9 | prescribed full unoriented witness has a sign lift iff its occurrence twist word is a cut | proved | scout proof |
| RL-10 | fixed-support data without a prescribed decomposition has one canonical occurrence obstruction | false in general | scope correction |
| RL-11 | generic occurrence obstruction is literally $\omega(g)$ | false as an object identity | different cochain gauges |
| RL-12 | retained affine-face sign lift and $\omega(g)=0$ describe the same fixed event | precise comparison | final equivalence inherits frozen OR1 status |
| RL-13 | generic fixed-witness obstruction is literally $\Omega_f$ | false | different family quantifier |
| RL-14 | within the frozen Fano fibre, some integral sign lift exists iff $\Omega_f=0$ | precise specialization | inherits frozen OR1 status |
| RL5-1 | $A_4$ root flow specializes to directed five-support words | proved | scout proof |
| RL5-2 | reduction gives $R_5/K_5/O^-(4,2)$ data | proved | scout proof plus frozen binary model |
| RL5-3 | quadratic/Schur/cographic/stress data retain integral signs | false | scope correction |
| RL5-4 | global support coefficients $I\cong\mathbf F_5$ project an $A_4$ root flow to a nowhere-zero $\mathbf F_5$-flow | proved | scout proof |
| RL5-5 | arbitrary fixed $\mathbf F_5$-flow canonically reconstructs an oriented five-support witness | not proved; too strong as stated | separate lift/holonomy problem |
| RL8-1 | $A_7\to E_8\to O^+(6,2)\to\mathbf F_2^3$ hierarchy | proved | scout proof plus frozen binary model |
| RL8-2 | Fano compatible-lift torsor reduces family sign search to a linear quotient | established comparison | inherits frozen OR1 gauge package |
| RL8-3 | Fano or $O^+(6,2)$ structure forces per-lift orientability | false | frozen exact $K_4$ example |
| RL8-4 | universal fixed-fibre vanishing | open | existing RL frontier |

## 5. Exact witness hierarchy

The pass separates five levels.

1. **Full witness:** indexed circuit occurrences, cyclic order, and multiset identity.
2. **Directed support word:** one balanced directed edge set per index.
3. **Integral root flow:** the equivalent $A_{q-1}$ encoding of level 2.
4. **Binary unordered root flow:** mod-$2$ indexed supports and $K_q$ labels.
5. **Family quotient:** after specifying a reconfiguration torsor, quotient a fixed-lift obstruction by the accessible motion image.

Only levels 2 and 3 are canonically equivalent without further choices. Level 1 maps to them but is not reconstructed canonically. Level 4 loses signs. Level 5 has a different existential quantifier.

## 6. Fixed-witness obstruction

For a prescribed full unoriented witness $\mathcal W$, the occurrence adjacency multigraph $H_{\mathcal W}$ has one vertex per circuit occurrence and one edge per source edge. Preliminary circuit orientations define

$$
t_{\mathcal W}\in C^1(H_{\mathcal W};\mathbf F_2).
$$

Reversing a circuit occurrence adds a cut. Therefore

$$
\boxed{
\mathcal W\text{ has an opposite-direction sign lift}
\iff
[t_{\mathcal W}]=0
\text{ in }C^1(H_{\mathcal W})/\operatorname{Cut}(H_{\mathcal W}).}
$$

Equivalently, $t_{\mathcal W}$ annihilates every cycle of $H_{\mathcal W}$. When nonempty, sign choices form an affine torsor under componentwise global reversals.

This is the precise generic prescribed-witness obstruction.

## 7. Relation to $\omega(g)$ and $\Omega_f$

For a retained cubic affine lift $g$:

- the generic occurrence criterion tests orientation of the retained face circuits;
- $\omega(g)$ uses vertex-disc orientation gauge on the source graph;
- both vanish for the same retained-face orientability event, but their quotient spaces are not literally identified without the full cellular chain complex.

For a fixed Fano flow $f$:

- $\omega(g)$ tests one prescribed compatible lift;
- $\Omega_f$ quotients by accessible affine gauge/Petrial motion and tests whether some lift in the fibre succeeds.

Thus

$$
\text{fixed witness}
\ne
\text{fixed lift}
\ne
\text{fixed fibre}
$$

as obstruction objects and quantifiers.

No statement here upgrades the frozen OR1 proof assurance or anticipates issue #51.

## 8. $q=5$ conclusion

The integral oriented object is an $A_4$ root flow, equivalently a directed $K_5$-arc labelling whose incidence-adjusted local roots form directed triangles.

Modulo $2$ it becomes the existing unordered five-support box:

$$
R_5
\leftrightarrow
K_5\text{ triangles}
\leftrightarrow
O^-(4,2)\text{ anisotropic flow}.
$$

Quadratic, Schur, cographic, relative-stress, and Fourier formulations do not retain integral signs.

After one global bijection of support indices with $\mathbf F_5$, every $A_4$ root flow projects to a nowhere-zero $\mathbf F_5$-flow. The reverse fixed-data lift requires ordered pair labels and all five coordinate equations; local coefficient charts additionally require trivial transport holonomy. No equivalence with arbitrary nowhere-zero five-flows is claimed.

## 9. $q=8$ conclusion

The integral/binary/Fano hierarchy is

$$
A_7
\to
E_8
\to
E_8/\langle\mathbf1\rangle\cong O^+(6,2)
\to
\mathbf F_2^3.
$$

The affine quotient sends

$$
\varepsilon_a-\varepsilon_b
\longmapsto
a+b.
$$

For a fixed compatible pair lift, an integral $A_7$ sign lift is exactly an opposite orientation of all retained support-component occurrences. Within the frozen OR1 package this is $\omega(g)=0$; over the fixed compatible-lift torsor it is $\Omega_f=0$ for some member.

The Fano structure makes the family problem linear and computable. It does not force vanishing. The exact $K_4$ fibre already contains both orientability types.

## 10. Literature findings

Established literature already contains:

- directed/orientable cycle double covers and their embedding interpretation;
- group-valued Kirchhoff flows;
- signed and bidirected integral flows;
- directed Eulerian flow decomposition;
- type-$A$ roots as directed complete-graph incidence vectors in root/flow-polytope theory;
- deleted and fully deleted permutation modules.

No exact source was located combining all of:

- indexed directed $q$-support words;
- $A_{q-1}$ root values on an arbitrary source graph;
- full-witness versus support-word data loss;
- prescribed occurrence sign obstruction;
- $q=5$ scalar coefficient transport;
- $q=8$ Fano torsor and $\omega/\Omega$ comparison.

This supports a claim of useful synthesis and theorem organization, not novelty or priority. A specialist bibliography remains necessary before publication language.

## 11. Counterexamples and open obstructions

### Exact counterexample

The four-parallel-edge two-vertex graph proves that one root flow may admit distinct circuit decompositions. Therefore the proposed canonical full-witness equivalence is false.

### Frozen exact warning

The standard $K_4$ Fano fibre contains both a nonorientable and an orientable compatible lift. Therefore compatibility does not force per-lift sign lifting.

### Open obstructions

1. universal fixed-Fano-fibre vanishing of $\Omega_f$;
2. graph-level existence of some Fano flow with $\Omega_f=0$ if universal fixed-fibre vanishing fails;
3. exact characterization of which fixed nowhere-zero $\mathbf F_5$-flows lift to $A_4$ root flows;
4. functorial comparison of the occurrence-graph class with the primal $\omega(g)$ through a complete cellular chain complex;
5. reconfiguration quotients for generic $q$ beyond the Fano affine torsor.

## 12. Obligations recommended for PDL

### `AC-PDL-ROOT-LIFT-GENERIC-EQUIVALENCE`

Formalize the reference-orientation invariant equivalence between directed indexed Eulerian supports and $A_{q-1}$ root flows, including disconnected graphs, parallel edges, empty indices, and the explicit loop-dart extension.

### `AC-PDL-ROOT-LIFT-DECOMPOSITION-BOUNDARY`

Formalize directed circuit decomposition as an existence theorem, retain multiset occurrences, and include the four-parallel-edge nonuniqueness counterexample.

### `AC-PDL-ROOT-LIFT-PRESCRIBED-WITNESS-OBSTRUCTION`

Formalize the occurrence adjacency multigraph, twist cochain, cut/cycle criterion, and affine solution torsor.

### `AC-PDL-ROOT-LIFT-CELLULAR-COMPARISON`

Construct the full cellular comparison among occurrence reversal, face orientation, vertex-disc twist words, and $\omega(g)$ without asserting a false bare quotient isomorphism.

### `AC-PDL-ROOT-LIFT-MOD2-EDGE-CASES`

Formalize reduction to $E_I$, the even-$q$ fully deleted quotient, the $q=4$ complementary-root collision, and injectivity for even $q\ge6$.

### `AC-PDL-ROOT-LIFT-Q5-PROJECTION`

Formalize the global $A_4\to\mathbf F_5$ coefficient projection and state the converse only as a fixed-data lifting problem with explicit local-to-global holonomy.

### `AC-PDL-ROOT-LIFT-Q8-DIAGRAM`

Formalize the commutative $A_7/E_8/O^+(6,2)/\mathbf F_2^3$ diagram and isolate exactly which final arrows consume the frozen OR1 gauge law.

These are proof-expansion and interface obligations. Universal $\Omega_f$ vanishing remains an RL problem, not a PDL gap.

## 13. Programme recommendation

Do **not** establish a separate persistent root-lift programme yet.

Recommended next action:

1. create one bounded PDL normalization packet covering the seven obligations above;
2. keep universal $q=8$ fixed-fibre vanishing inside the existing orientation RL frontier;
3. open a distinct successor research programme only if either:
   - an exact fixed-fibre counterexample or a plausible universal-vanishing mechanism appears; or
   - the fixed $\mathbf F_5$-flow lift problem develops a nontrivial obstruction theory not reducible to the present sign/cut formalism.

At present, a permanent parallel programme would duplicate OR1 and Programme B more than it would add new mathematics.

## 14. Final classification

`SCOPE CORRECTION — PROPOSED EQUIVALENCE TOO STRONG`.

The corrected support-level $A_{q-1}$ equivalence, prescribed-witness obstruction, mod-$2$ hierarchy, and $q=5/q=8$ specializations are complete at bounded scout proof level. The full-witness canonical equivalence is false; the OR1-dependent final comparisons remain at their frozen authorial/Curator-integrated assurance; universal orientable-lift existence remains open.
