# Five-support edge extension as a relative coloured-Pachner/weld problem

## Research Lead literature-and-mechanism synthesis v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `47ba5635dcb582fe0a9ecb3404d9531cc009fabc`.

**Purpose:** compare the root-triangle pseudocomplex and its Pachner histories with established colored bistellar-move theory, determine whether that theory supplies the fixed-topology bypass sought in `SINGLE_DEFECT_DIRECT_AUGMENTATION_BOUNDARY_V1.md`, and isolate the correct topological theorem that would genuinely simplify R2.

**Status:** exact conceptual identification and scope boundary. Existing colored Pachner theorems do not imply the five-support edge-extension theorem, because they assume that both endpoint triangulations are already properly colored. They nevertheless reveal the current singular contextual-confluence package as a concrete relative colored-weld theorem for a four-port pseudocomplex.

---

## 1. Root flows are proper five-colorings of triangle pseudocomplexes

Let

\[
\lambda:E(G)\to R_5
\]

be a root-valued flow on a cubic graph or four-pole. Every cubic vertex has one support triangle

\[
\Delta_v=\{i,j,k\}\subset[5],
\]

and every source edge of root `ij` glues two triangle sides with endpoint colors `i,j`.

The resulting triangle pseudocomplex

\[
\mathfrak T_\lambda
\]

has:

- one triangle for each source vertex;
- vertices colored from `[5]`;
- three distinct colors on every triangle;
- matching colored endpoints on every glued side;
- unglued sides at the four external ports.

Thus an `R_5`-valued flow is equivalently a proper five-coloring of the vertices of this two-dimensional triangle pseudocomplex, together with its fixed side identifications.

The complex may have disconnected vertex links. Splitting singular vertices converts it into a compact colored surface, possibly disconnected and with boundary, without changing the dual cubic graph or the local two-triangle moves. Any use of manifold theorems must nevertheless record this splitting and its compatibility with the four-port source context.

---

## 2. Root NNI is a color-preserving bistellar flip

Two adjacent distinct root triangles have the form

\[
ijk,\qquad ij\ell.
\]

The unique root-valued alternative replaces them by

\[
ik\ell,\qquad jk\ell,
\]

across the opposite diagonal `k\ell`.

On the triangle pseudocomplex this is exactly a color-preserving `2--2` bistellar/Pachner flip on the boundary of the four-color tetrahedron

\[
\{i,j,k,\ell\}.
\]

Two adjacent equal triangles admit the root-preserving `2--0` equal-face cancellation. In the colored-complex language this is a two-face weld/dipole removal. It is not merely another `2--2` flip: it changes the number of triangles and is the move through which target order decreases.

Hence the complete root-surgery alphabet is topologically:

\[
\boxed{
\text{properly five-colored }2--2\text{ flips}
\quad+
\text{colored two-face welds}.}
\]

The zero and co-root first failures are precisely the two ways an attempted inverse local move can fail to preserve proper five-colorability.

---

## 3. Established colored Pachner connectivity

Izmestiev--Klee--Novik prove the following colored Pachner theorem:

> If two closed combinatorial `d`-manifolds are PL homeomorphic and are both properly `m`-colored, with `m>=d+2`, then they are connected by bistellar flips preserving the vertex colors.

For the present dimensions,

\[
d=2,\qquad m=5,
\]

the numerical color hypothesis is amply satisfied.

They also prove that balanced triangulations of a closed manifold are connected by cross-flips, and give a relative coloring-extension theorem: a coloring prescribed on a subcomplex extends after stellar subdivision of the ambient relative complex.

### References

- Ivan Izmestiev, Steven Klee, Isabella Novik, *Simplicial moves on balanced complexes*, arXiv:1512.04384, especially Theorems 1.1, 1.2, and 3.1.
- Satoshi Murai, Yusuke Suzuki, *Balanced subdivisions and flips on surfaces*, arXiv:1701.08060.
- Michael Joswig, *Projectivities in Simplicial Complexes and Colorings of Simple Polytopes*, arXiv:math/0102186.

---

## 4. Why the colored Pachner theorem does not prove R2

The simple-edge extension problem begins with:

1. a properly five-colored pseudocomplex for one cross-reduced graph `G/e`;
2. the uncolored target pseudocomplex corresponding to the original graph `G`;
3. one inverse cap move relating their source topologies.

The colored Pachner theorem assumes that **both endpoints already possess proper colorings**. Applying it to the pair

\[
\mathfrak T_{G/e},\qquad \mathfrak T_G
\]

would therefore assume the desired root flow on `G`.

### Proposition 4.1 — endpoint-coloring circularity

Colored Pachner connectivity can compare two root flows after both exist. It cannot create the first root flow on the target source topology.

In particular, it does not imply the fixed-topology simulation target of `SINGLE_DEFECT_DIRECT_AUGMENTATION_BOUNDARY_V1.md`.

---

## 5. Why relative coloring extension still leaves the weld problem

The relative extension theorem allows one to retain a coloring on the fixed four-port boundary and stellarly subdivide the interior of the target until the coloring extends.

Thus one may hope to obtain a colored refinement

\[
\mathfrak T'_G
\]

of the uncolored target complex.

But the theorem sought is a coloring of the original unrefined source topology. One must therefore undo the introduced subdivisions by color-preserving welds.

At the last weld where proper coloring fails, the local obstruction is again:

\[
0
\quad\text{or}\quad
Q_i.
\]

This is exactly the first-failure one-edge atom of the current contextual-transfer theorem.

### Proposition 5.1 — refinement does not remove singular return

Relative coloring extension moves the obstruction from existence of a colored refinement to color-preserving contraction back to the prescribed source topology. The latter is the singular weld problem already solved authorially by the zero/co-root token grammar and contextual confluence.

Murai--Suzuki's surface result reinforces the general warning: even within balanced surface topology, balanced subdivisions and welds alone do not provide an unrestricted connectivity theorem; an additional local move such as pentagon contraction is needed in their setting. This result is not identified with the present Petersen `C5` mechanism, but it shows that colored weld control is mathematically substantive rather than formal bookkeeping.

---

## 6. Projectivity interpretation

Joswig associates to a strongly connected pure simplicial complex a projectivity group generated by transporting vertex identifications along facet paths. This group governs coloring obstructions and is combinatorial rather than purely topological.

The present forced-backbone mechanism has the same structural form:

- adjacent root triangles transport a local root-resolution choice;
- constant-pivot runs contribute canonical sections;
- a recurrent co-root token records projectivity/monodromy along a facet-path-like sequence;
- the cap distinguishes one oriented route block;
- odd projectivity is forbidden;
- even projectivity contains an explicit colored weld exit.

This does not identify the current Petersen transport group with Joswig's projectivity group without further proof. It suggests, however, that `O+` is best understood as a **relative projectivity-triviality condition** supplied by the ordered cap.

---

## 7. The correct general theorem behind R2

The current edge-extension theorem can be restated as follows.

### Proposed relative colored-weld theorem

Let `T_0` and `T_m` be finite five-colored triangle pseudocomplex contexts with the same ordered four-port boundary, where `T_m` is obtained from `T_0` by a finite sequence of colored `2--2` flips and colored two-face cancellations. Assume:

1. the four-port boundary carries one distinguished cap matching and block;
2. every intermediate root-valued move is category-safe;
3. the only failed inverse welds are the zero and co-root singular fibers;
4. the induced relative projectivity has no admissible odd closed subpath;
5. every even primitive projectivity core admits a colored cancellation movie.

Then every proper five-coloring of `T_m` returns to a proper five-coloring of `T_0` with the same boundary context.

This is precisely `SINGULAR_ROOT_TRIALITY_CONFLUENCE_MASTER_THEOREM_V3.md` translated into colored-Pachner language.

---

## 8. A genuine future bypass: Target F'

A broad theorem could replace the Petersen/Ptolemy-specific proof if one proved:

### Target F' — relative five-colored weld connectivity

For every compact two-dimensional triangle pseudocomplex with ordered four-port boundary and five available colors, any proper boundary-preserving coloring of a stellar refinement descends to the prescribed unrefined topology by a sequence of:

- color-preserving `2--2` flips;
- proper colored welds;
- strictly smaller relative colored contexts;

provided the boundary projectivity fixes one distinguished cap block.

Such a theorem would be a true fixed-topology bypass. The current authorial proof establishes only the special case generated by root triality, one-token critical overlaps, Petersen monodromy, and the explicit `C6/C8` movies.

No cited general colored Pachner theorem presently supplies Target F'.

---

## 9. Architectural consequence

The topological interpretation simplifies exposition without deleting a valid proof obligation:

1. **root-flow language** becomes proper five-coloring of the dual triangle pseudocomplex;
2. **root NNI** becomes a colored `2--2` Pachner flip;
3. **Morse carrier descent** becomes reduction in the colored flip graph;
4. **first failure** becomes one improper inverse weld;
5. **Petersen token transport** becomes relative projectivity;
6. **orientation-hardening** means projectivity fixes the distinguished cap block;
7. **`C6/C8` movies** are the primitive colored-weld exits;
8. **finite condensation** is reachability in the relative colored flip/weld graph.

The result should be presented as one relative colored-weld theorem, not as unrelated equality, DDD, Ptolemy, and Petersen theories.

---

## 10. PDL obligations

PDL should retain the following scope distinctions.

1. The root triangle complex can be a pseudomanifold with singular vertex links; manifold results require an explicit splitting/relative argument.
2. Colored Pachner connectivity assumes both endpoint colorings and cannot be used to prove the target coloring.
3. Relative coloring extension produces a colored subdivision, not a coloring of the prescribed unsplit source topology.
4. Undoing subdivisions is the load-bearing singular weld problem.
5. Projectivity language is interpretive until the full labelled transport is identified formally.
6. The current `C6/C8` source movies, not an abstract topological equivalence theorem, provide the controlling even-core exits.

---

## 11. Assurance boundary

### Exact synthesis

- root flows are proper five-colorings of the root triangle pseudocomplex;
- root NNI is a color-preserving bistellar `2--2` flip;
- equal-face cancellation is the relevant colored weld;
- existing colored Pachner connectivity is endpoint-coloring circular for R2;
- relative coloring extension leaves exactly the inverse-weld problem;
- current contextual confluence is a special relative colored-weld theorem.

### Proposed, not proved

- formal identification of forced Petersen transport with a projectivity subgroup in Joswig's sense;
- the general Target F' relative weld theorem;
- replacement of the concrete `C6/C8` proof by a general colored-topology theorem;
- PDL acceptance, Lean verification, manuscript integration, release, peer review, publication, or established truth of five-CDC.
