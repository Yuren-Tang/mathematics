# Scope correction: an abstract root tube is not yet a lifted Ptolemy history

## Independent reverse-audit dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Audited surface:** branch head containing `PTOLEMY_EVEN_TRACK_ROOT_TUBE_FILLING_V1.md`, `ORIENTED_FULL_CHANNEL_LOCK_ELIMINATION_SYNTHESIS_V1.md`, and `FIVE_SUPPORT_GLOBAL_MINIMAL_COUNTEREXAMPLE_CLOSURE_V1.md`.

**Corrects the assurance scope of:**

- `PTOLEMY_EVEN_TRACK_ROOT_TUBE_FILLING_V1.md`;
- the contextual-transfer conclusion imported by `ORIENTED_FULL_CHANNEL_LOCK_ELIMINATION_SYNTHESIS_V1.md`;
- the global candidate closure insofar as it imports that contextual-transfer conclusion.

**Status:** exact audit localisation. The `C6` and `C8` side-root words, their zero-sum property, the abstract cycle-multipole prefix criterion, and the displayed root-valued longitudinal fillings are correct. What is not yet proved is that one such abstract cycle-multipole filling induces a coherent root-valued lift of the original annular neighbourhood in the Ptolemy history diagram. The missing theorem must identify the complete local history-cell constraints with the single cubic equation `x_(i-1)+x_i=z_i` at every turn and must verify consistency on all shared history states. Until that realisation theorem is supplied, even-track removal, fixed-order sink elimination, contextual inverse transfer, full-channel lock elimination, and the global minimal-counterexample closure remain conditional at this interface.

**Not implied:** falsity of the five-support theorem, nonexistence of a valid tube-lift construction, failure of the Ptolemy/backbone route, invalidity of the algebraic `C6/C8` fillings, or existence of a counterexample.

---

## 1. Exact results retained

The following statements remain exact.

1. A closed nonbranching first-failure track has an annular regular neighbourhood in a Ptolemy van Kampen disk.
2. Persistent same-order atoms are co-root/DDD atoms.
3. After constant-run and backtrack reduction, a recurrent track contains one simple Petersen cycle of length
   \[
   5,6,8,\text{ or }9.
   \]
4. Odd `C5` and `C9` tracks reverse the oriented resolution sheet and cannot close in one oriented cap lock.
5. The emitted side-root word of a `C6` is, up to symmetry,
   \[
   (a,b,c,a,b,c),
   \qquad a+b+c=0.
   \]
6. The emitted side-root word of the standard `C8` is
   \[
   (24,34,23,12,13,34,14,12).
   \]
7. For a cyclic root word `z_0,...,z_(n-1)`, a root-valued abstract cycle multipole with one side semiedge `z_i` at each vertex is equivalent to roots `x_i` satisfying
   \[
   x_i+x_{i+1}=z_i
   \qquad(i\bmod n).
   \]
8. The displayed `C6` and `C8` longitudinal words satisfy these equations:
   \[
   C_6:\quad (b,c,a,b,c,a),
   \]
   and
   \[
   C_8:\quad (25,45,35,25,15,35,45,15).
   \]

Thus the algebraic tube fillings are genuine root-valued flows on the abstract cycle multipoles determined only by the emitted side words.

---

## 2. The additional history-space assertion

The load-bearing step in the contextual-transfer proof is stronger than Item 8 above.

Let `N(gamma)` be the annular regular neighbourhood of a closed defect track in a lifted Ptolemy van Kampen diagram. The proof needs:

> every abstract longitudinal solution `x_i+x_(i+1)=z_i` defines root-valued flows on all source graphs represented by the vertices of `N(gamma)`, makes every edge of the history diagram a root-valid source surgery, agrees on every shared history state, and preserves the complete exterior root data and ordered cap route.

This is a statement about a lift of a diagram of source graphs. It is not a formal consequence of the existence of a root-valued flow on the dual abstract cycle multipole.

The current tube dossier states that the triality cells of `N(gamma)` form a dual cycle multipole, but it does not construct the required equivalence between:

\[
\boxed{
\text{coherent root lifts of the Ptolemy annulus}}
\]

and

\[
\boxed{
\{(x_i):x_i\in R_5,\ x_i+x_{i+1}=z_i\}.}
\]

In particular, it does not explicitly verify the root labels on every source edge occurring in a history vertex or the compatibility of those labels across every Ptolemy digon, square, and pentagon incident with the track.

---

## 3. Why the missing identification is nontrivial

For one actual Petersen transition

\[
\{s,x\}\longrightarrow\{s,y\}
\]

with emitted side root `z`, `PETERSEN_PIVOT_RESOLUTION_V1.md` proves the unique-resolution theorem:

\[
\boxed{
 r^-+r^++z=0
 \iff
 (r^-,r^+)=(x,y),
}
\]

when

\[
r^-\in\{s,x\},
\qquad
r^+\in\{s,y\}.
\]

Therefore, if the original DDD atom states are held fixed, the local root pair is not an arbitrary decomposition of `z`; it is the unique pair of nonshared Petersen endpoints.

A tube filling is allowed in principle to change the internal atom states and not merely their selected resolutions. But that stronger relabelling requires an explicit construction on the whole history annulus. The scalar equation `x_i+x_(i+1)=z_i` alone does not establish it.

---

## 4. Exact finite sanity certificate

An independent exact enumeration reconstructs the standard simple cycles and compares the original unique transition pairs with the proposed tube pairs.

### 4.1 Six-cycle representative

Take the Petersen pivot cycle

\[
(12,34,25,14,23,45).
\]

Its emitted word is

\[
(35,15,13,35,15,13).
\]

The unique nonshared-endpoint pairs at the six turns are

\[
(45,34),
(12,25),
(34,14),
(25,23),
(14,45),
(23,12).
\]

The abstract tube filling is

\[
(15,13,35,15,13,35),
\]

whose consecutive pairs are

\[
(15,13),
(13,35),
(35,15),
(15,13),
(13,35),
(35,15).
\]

Every consecutive tube pair has the correct sum, but none is the original transition's unique nonshared-endpoint pair.

### 4.2 Eight-cycle representative

Take the Petersen pivot cycle

\[
(13,25,14,35,24,15,23,45).
\]

Its emitted word is exactly

\[
(24,34,23,12,13,34,14,12).
\]

The unique transition pairs are

\[
(45,25),
(13,14),
(25,35),
(14,24),
(35,15),
(24,23),
(15,45),
(23,13).
\]

The proposed longitudinal word

\[
(25,45,35,25,15,35,45,15)
\]

has consecutive pairs

\[
(25,45),
(45,35),
(35,25),
(25,15),
(15,35),
(35,45),
(45,15),
(15,25).
\]

They have the prescribed side-root sums at all eight turns, but agree with the original unique transition pair at only four alternating turns.

### Interpretation

This is not a counterexample to a global annular relabelling. It proves instead that the tube filling cannot be justified as a pointwise choice of the already established root resolution of each original atom transition. A new history-lift realisation theorem is indispensable.

---

## 5. Exact missing theorem

### Target 5.1 — annular Ptolemy tube-lift realisation

Let `gamma` be one closed nonbranching co-root track in a lifted Ptolemy van Kampen disk, and let `N(gamma)` be a regular annular neighbourhood. Let

\[
z_0,\ldots,z_{n-1}
\]

be its emitted exterior root data. Construct a finite constraint complex `T_gamma` and prove all of the following.

1. **Local cell parametrisation.**  For every turn of the track, coherent root lifts of the corresponding local Ptolemy critical cell are parametrised exactly by its incoming and outgoing longitudinal roots `x_i,x_(i+1)` satisfying
   \[
   x_i+x_{i+1}=z_i.
   \]
2. **History-vertex compatibility.**  The assignments contributed by all incident track cells agree on every edge of every source graph represented by a vertex of `N(gamma)`.
3. **History-edge compatibility.**  Every edge of the Ptolemy diagram inside `N(gamma)` is a legal root Pachner move, equal-face cancellation, or explicitly allowed normalized critical transition between the resulting root flows.
4. **Exterior identity.**  Every source edge and root label outside `N(gamma)` is unchanged.
5. **Boundary identity.**  The ordered outer four-port word, cap shore, and physical route are unchanged.
6. **Equivalence.**  Every solution of the cycle equations produces such a coherent lift; conversely every coherent lift restricts to one solution.

Only after this theorem may an abstract `C6` or `C8` longitudinal filling be used to remove a global defect track.

---

## 6. Possible repair routes

Three logically sufficient repairs are available.

### Route A — explicit local lift table

Write the complete labelled local Ptolemy critical-cell table, including every source edge shared with adjacent cells. Prove the parametrisation in Target 5.1 directly and glue the local tables around the annulus.

### Route B — genuine source enclosure

Prove that every closed forced-backbone track has a composition-safe source-graph neighbourhood whose actual dual cubic multipole is the displayed `C6` or `C8` tube with the stated exterior root semiedges. Then the existing root-flow filling applies as an ordinary source replacement.

### Route C — exhaustive bounded lifted-cell certificate

The reduced cores have lengths six and eight. Enumerate the complete lifted Ptolemy annuli, not merely their Petersen output words, modulo support and dihedral symmetry. For every admissible annulus verify a root-valued replacement fixing all exterior labelled incidences. A finite certificate must include the map back to every history vertex and edge.

---

## 7. Impact on the candidate proof

### Retained unconditionally

- arbitrary-edge three-reconnection category theorem;
- exact `J_i/K_i` profile interfaces;
- the three-reconnection fixed-route finite classification;
- horizontal equality/DDD rescue;
- equality and DDD current-flow potentials;
- first-failure localisation;
- local critical-overlap classification;
- forced Petersen-backbone identification;
- odd-track orientation exclusion;
- bounded direct-pairing and matching-flip exits;
- all algebraic `C6/C8` side-word and tube equations.

### Conditional on Target 5.1

- removal of every even closed multi-cell defect track;
- no-sink theorem for the same-order contextual state graph;
- complete contextual inverse transfer;
- `ORIENTED_FULL_CHANNEL_LOCK_ELIMINATION_SYNTHESIS_V1.md`, Section 8 onward;
- `FIVE_SUPPORT_GLOBAL_MINIMAL_COUNTEREXAMPLE_CLOSURE_V1.md`.

Thus the global candidate proof is not rejected, but it is not yet gap-free under independent reverse audit.

---

## 8. Trust boundary

### Exact here

- distinction between an abstract root-valued cycle multipole and a coherent lift of a Ptolemy history annulus;
- uniqueness of the root resolution when original Petersen atom states are fixed;
- exact `C6` and `C8` mismatch certificates above;
- identification of the missing annular tube-lift realisation theorem;
- precise dependency impact on contextual transfer and the global candidate closure.

### Not claimed

- impossibility of the tube-lift realisation theorem;
- a counterexample to contextual transfer;
- falsity of full-channel lock elimination;
- falsity of the five-support theorem.

### Next action

Prove or refute Target 5.1 before restoring unconditional contextual-transfer and global-closure status.
