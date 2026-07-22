# Even Ptolemy defect tracks admit an explicit root-valued tube filling

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `d5899bd3f9b714363cf47c4ea1528dacc519127b`.

**Parents:**

- `PTOLEMY_CONTEXTUAL_COHERENCE_SCOPE_CORRECTION_V1.md`;
- `PTOLEMY_TRACK_FORCED_BACKBONE_SINK_ELIMINATION_V1.md` read only through its retained track/backbone and odd-cycle statements;
- `FORCED_BACKBONE_EVEN_CYCLE_SINK_SCOPE_CORRECTION_V1.md`;
- `PACHNER_FIRST_FAILURE_CRITICAL_OVERLAP_V1.md`;
- `PETERSEN_SIMPLE_CYCLE_OUTPUT_CLASSIFICATION_V1.md`;
- `PETERSEN_RESOLUTION_PARITY_V1.md`;
- `PETERSEN_CYCLE_MONODROMY_V1.md`.

**Status:** exact history-space filling theorem for the two surviving even forced-backbone tracks. A closed nonbranching first-failure track in a lifted Ptolemy van Kampen diagram has an annular regular neighbourhood. Its local triality cells form a cycle multipole whose boundary labels are exactly the emitted side-root word of the reduced Petersen core. For `C6` and `C8`, explicit root labels on the longitudinal edges solve every local cubic equation and close around the annulus. Replacing the singular resolution choices inside the tube by this root filling removes the entire defect circle while leaving the outer lift, side labels, attachments, and cap route unchanged. Therefore neither even simple Petersen cycle can support global contextual monodromy. Together with odd-cycle exclusion, no closed multi-cell first-failure track survives.

**Not implied:** final global five-support theorem before reverse dependency audit, canonical acceptance, independent audit, Lean verification, manuscript integration, release, publication, or DOI status.

---

## 1. Lifted Ptolemy diagrams and defect tracks

Let two fixed-order root-surgery histories on one marked triangle surface be compared by a finite Ptolemy van Kampen diagram. Its 2-cells are involution digons, disjoint squares, and adjacent-flip pentagons.

Lift the boundary histories by root-valued flows as far as possible. Whenever one local inverse resolution is non-root, mark the corresponding local triality edge. The critical-overlap theorem gives:

1. the marked locus does not branch;
2. a zero mark inside a pure flip block has an immediate root alternative and disappears;
3. every persistent mark is co-root/DDD;
4. a bad overlap may transiently create two adjacent co-roots, but one local defect-tree normalization returns to one mark.

After smoothing these bounded local normalizations, the persistent defect locus in the van Kampen disk is a compact one-manifold. Its components are arcs ending at genuine exits or embedded circles.

We study one embedded circular component

\[
\gamma.
\]

Because the ambient van Kampen diagram is a disk, a sufficiently small regular neighbourhood

\[
N(\gamma)
\]

is an annulus.

---

## 2. The annular triality tube

Traverse `gamma` through its successive local triality cells. At the `i`-th turn, let

\[
F_{i-1}=\{s_{i-1},s_i\},
\qquad
F_i=\{s_i,s_{i+1}\}
\]

be the consecutive DDD states of the retained forced-backbone dictionary. The two cells share the pivot root `s_i`.

Let

\[
z_i
\]

be the actual root label on the side incidence leaving the track at that turn. Petersen transport gives

\[
\boxed{z_i=s_{i-1}+s_{i+1}.}
\]

The annulus `N(gamma)` has a dual cycle multipole:

- one dual cubic vertex for every turn of `gamma`;
- one longitudinal dual edge between consecutive turns;
- one boundary/side semiedge labelled `z_i` at the `i`-th vertex.

The exterior of the tube meets it only through these side incidences. Hence changing the longitudinal labels while keeping all `z_i` fixed changes no exterior root value, attachment, or ordered cap data.

### Definition 2.1 — root tube filling

A root tube filling is a cyclic sequence

\[
x_0,x_1,\ldots,x_{n-1}\in R_5
\]

such that

\[
\boxed{x_{i-1}+x_i=z_i}
\qquad(i\bmod n).
\]

Then every dual tube vertex carries the root triangle

\[
(x_{i-1},x_i,z_i),
\]

so the complete tube is root-valued.

---

## 3. Prefix criterion

Fix one initial root `x_0`. The equations force

\[
x_i=x_0+z_1+\cdots+z_i.
\]

Because a closed Petersen output word satisfies

\[
\sum_i z_i=0,
\]

cyclic closure is automatic. Therefore:

### Lemma 3.1 — tube criterion

A closed side word `z_0,...,z_(n-1)` admits a root tube filling if and only if there is one root `x` such that every prefix translate

\[
x,
\quad x+z_0,
\quad x+z_0+z_1,
\quad\ldots,
\quad x+z_0+\cdots+z_{n-2}
\]

is a root.

The exterior side labels are then preserved exactly.

---

## 4. Six-cycle filling

Every simple Petersen six-cycle is the identity hexagon of one active root. Its side word is, up to support permutation, cyclic shift, and reversal,

\[
\boxed{(a,b,c,a,b,c),}
\]

where `a,b,c` are the three roots of one support triangle and

\[
a+b+c=0.
\]

### Theorem 4.1 — explicit `C6` filling

The cyclic longitudinal word

\[
\boxed{(b,c,a,b,c,a)}
\]

is a root tube filling.

### Proof

At the six successive tube vertices the required sums are

\[
\begin{aligned}
a+b&=c,\\
b+c&=a,\\
c+a&=b,
\end{aligned}
\]

repeated twice. Thus every local triple is exactly the same support triangle in cyclic order. ∎

### Corollary 4.2

A closed `C6` first-failure track can be replaced inside its annular neighbourhood by a completely root-valued tube with the same six side roots.

No identity-hexagon semantic defect remains on the track: the filling fixes the complete labelled tube boundary, not merely its support monodromy.

---

## 5. Eight-cycle normal form

Every simple Petersen eight-cycle lies in one `S_5` orbit and is canonically attached to one DDD state. Use the representative side word

\[
\boxed{
(24,34,23,12,13,34,14,12).
}
\]

Its output multiset is

\[
E(K_{\{1,2,3,4\}})\sqcup\{12,34\}.
\]

The fifth support index is `5`.

### Theorem 5.1 — explicit `C8` filling

The cyclic longitudinal word

\[
\boxed{
(25,45,35,25,15,35,45,15)
}
\]

is a root tube filling of the representative `C8` word.

### Proof

Successive sums are

\[
\begin{array}{c|c}
\text{longitudinal pair}&\text{side root}\\
\hline
25+45&24\\
45+35&34\\
35+25&23\\
25+15&12\\
15+35&13\\
35+45&34\\
45+15&14\\
15+25&12.
\end{array}
\]

Every longitudinal value is a root through the fifth support index. The final value closes to the initial `25`. ∎

### Corollary 5.2 — all eight-cycles

All simple Petersen eight-cycles form one `S_5` orbit. Applying the same support permutation to the side and longitudinal words gives a root tube filling for every `C8` track.

The filling is canonical up to the stabiliser of the labelled DDD octagon and reversal of the tube orientation.

---

## 6. Surgery on the lifted diagram

Let `gamma` be a closed even defect track and let

\[
x_0,\ldots,x_{n-1}
\]

be the filling from Section 4 or 5.

Inside `N(gamma)`, replace the singular/co-root longitudinal choices by the root labels `x_i`. Keep:

- every side label `z_i`;
- every cell outside `N(gamma)`;
- every exterior triangle and edge value;
- the outer four-port boundary word;
- the ordered cap shore and route;
- the combinatorial van Kampen diagram.

At each tube vertex the flow equation holds because

\[
x_{i-1}+x_i+z_i=0.
\]

The two boundary circles of the annulus see exactly the same side incidences and root labels as before. Therefore the modified lift glues to the unchanged exterior.

### Theorem 6.1 — even-track removal

A closed forced-backbone defect track with reduced core `C6` or `C8` can be removed from the lifted Ptolemy diagram without:

1. changing any exterior root value;
2. changing the outer route/profile state;
3. introducing another defect component;
4. altering the underlying histories outside the annular neighbourhood.

After the modification, the entire former tube is root-valued.

### Trust note

This is a history-space filling, not a claim that the coefficient spine was already a four-pole in one source graph. It therefore avoids the interface error quarantined in `FORCED_BACKBONE_EVEN_CYCLE_SINK_SCOPE_CORRECTION_V1.md`.

---

## 7. Complete closed-track disposition

The reduced forced-backbone classification gives simple cycle lengths

\[
5,6,8,9.
\]

- `C5` and `C9` have odd resolution parity and cannot close in an oriented cap lock.
- `C6` and `C8` admit the root tube fillings above and therefore are removable.

### Theorem 7.1 — no closed multi-cell defect track

A lifted fixed-route Ptolemy diagram contains no essential closed first-failure component.

Every putative closed component is either:

1. odd and incompatible with the ordered resolution sheet;
2. even and removable by root tube filling.

There is no third simple-cycle core, and constant runs/backtracks do not affect this conclusion.

---

## 8. Global same-order coherence

Return to the finite contextual state graph at one cap-target order. Suppose a nonterminal sink strongly connected component existed.

A recurrent same-order first failure cannot be zero and therefore gives a persistent co-root track. Removing constant runs and backtracks produces a repeated pivot and hence one closed simple Petersen subtrack.

Theorem 7.1 either forbids or removes that subtrack. In the removable case, the lifted history has strictly fewer defect-track cells while retaining the same exterior state, contradicting minimality of a recurrent representative. In the odd case, fixed-route orientation is violated.

### Theorem 8.1 — no same-order contextual sink

The fixed-order contextual state graph has no nonterminal sink strongly connected component.

Consequently every same-order state has a finite path to one of:

1. complete root-valued transfer;
2. route-changing matching flip and cap lift;
3. separator/category exit;
4. bounded direct-pairing completion;
5. a first failure behind an equal-face cancellation.

---

## 9. Well-founded contextual transfer

The target-order correction proves that a first failure behind at least one cancellation has cap-context target order smaller by at least two. Pure flip prefixes remain at fixed order and are handled by Theorem 8.1.

Induct on cap-target vertex order. Within one order use same-order progress; after a cancellation invoke the induction hypothesis.

### Theorem 9.1 — contextual inverse-transfer synthesis

Every cap-compatible root state obtained at the terminal of an equality or oriented DDD descent transfers back to the original cap context, unless the original instance is already discharged by:

\[
\boxed{
\text{cap-profile lift},
\quad
\text{separator/category reduction},
\quad
\text{bounded direct-pairing completion}.}
\]

Repeated contextual recursion is well founded.

This closes the side-output enclosure problem for the only two even global defect tracks and supplies the missing multi-cell coherence theorem.

---

## 10. Consequence for the AffineCDC frontier

The local/compositional frontier now has theorem-level consumers for:

- equality and DDD current-flow descent;
- first-failure localisation;
- same-order zero removal;
- multi-cell co-root track/backbone identification;
- odd-track orientation exclusion;
- even-track history-space filling;
- corrected strict-order recursion;
- matching-flip cap escape;
- bounded direct-pairing termination.

The next task is a reverse dependency audit from the global minimal-counterexample setup. No global theorem is claimed before checking every cut-gluing, reconnection-category, and induction dependency.

---

## 11. Trust boundary

### Exact here

- annular regular neighbourhood of one embedded closed defect track;
- dual cycle-multipole interpretation of the triality tube;
- root tube prefix criterion;
- explicit root filling of every `C6` word;
- explicit root filling of every `C8` word;
- preservation of all side roots and exterior contextual data;
- removal of every even closed defect track;
- complete odd/even closed-track disposition;
- fixed-order sink elimination;
- combination with corrected strict-order descent;
- contextual inverse-transfer synthesis.

### External/topological boundary

The existence of a regular annular neighbourhood for an embedded circle in a van Kampen disk and the standard Ptolemy cell structure are classical topological inputs. The coefficient fillings and local gluing checks are proved explicitly here.

### Still open

- reverse global proof-DAG audit;
- final minimal-counterexample closure theorem and well-founded packaging;
- independent mathematical audit;
- canonical acceptance, Lean verification, manuscript integration, release, publication;
- the global five-support theorem.
