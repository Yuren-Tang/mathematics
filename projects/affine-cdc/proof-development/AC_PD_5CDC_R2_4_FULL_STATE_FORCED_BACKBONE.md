# AC-PD-5CDC R2.4 — full-state forced Petersen backbone

**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Programme:** compressed five-support proof, extension unit `R2`  
**Classification:** `COMPLETE-DRAFT / FULL-STATE BACKBONE CLOSED / ORIENTATION AND EVEN-CORE CONSUMERS SEPARATE`.

This dossier reconstructs the full-state source theorem behind the Petersen
backbone.  It does not use formal coefficient free reduction as a substitute
for source composition.

---

## 1. Input state graph

Work at one fixed target order, fixed ordered cap shore, fixed cap block and
fixed physical route.  Every persistent singular state has already been
locally normalized to exactly one standard co-root atom.  Zero rows,
doubled-disjoint raw insertions and transient two-co-root trees are internal to
bounded macros and are not state vertices.

A state retains:

- the complete cubic source topology;
- every edge root and ordered incidence;
- the atom edge and missing index;
- both crossed root resolutions of the atom;
- side roots emitted by adjacent transport cells;
- support transport, cap block and route orientation.

Accepted route/profile, bounded, separator and category outcomes leave the
state graph.

---

## 2. One atom is one Petersen edge

Let a standard atom have co-root value `Q_i`.  Its ordered four-root triality
has exactly two crossed root resolutions

\[
s,t\in R_5,
\qquad s\perp t,
\qquad s+t=Q_i.
\]

Associate the Petersen edge

\[
F(A)=\{s,t\}\in E(KG(5,2)).
\]

The two endpoints are physical root resolution sheets, not abstract labels.

When the atom meets one adjacent root Pachner move, the bounded critical-pair
table has only:

1. strict commutation/rootification;
2. one standard relocation;
3. one transient two-co-root tree followed by immediate normalization;
4. accepted exit.

In the nonexit relocation case consecutive atom states share exactly one root
resolution.  Thus

\[
F(A)=\{s,t\}
\longrightarrow
F(A')=\{t,u\}
\]

with `s perp t` and `t perp u`.  This is one Petersen pivot turn

\[
s\to t\to u.
\]

Every side root and source attachment is retained by the local
critical-overlap movie.

---

## 3. Constant-pivot runs

A maximal run has states

\[
F_j=\{s,d_j\}
\]

with fixed pivot `s`.  At a transition, if `z_j` is the emitted side root,

\[
d_j+d_{j+1}+z_j=0.
\]

The cap-oriented local equation uniquely selects the nonpivot resolution
`d_j` at every state.

### Theorem 3.1 — full-state run section

Every maximal constant-pivot run has a unique simultaneous root section which:

- removes every atom in the run;
- preserves every emitted side-root occurrence;
- preserves every exterior rooted attachment and incidence order;
- preserves the cap block and route orientation;
- transports `d_0` to `d_m`.

The support monodromy of the run is retained in the rooted branch data and is
not set equal to the identity.

Hence a recurrent singular component may be reduced first by physically
rootifying all maximal constant-pivot runs.

---

## 4. One genuine pivot-change cell

After the two adjacent runs are root-resolved, one pivot change has the exact
six-port boundary

\[
(s,x,z\mid w,t,y),
\]

with

\[
x+t+z=0,
\qquad
s+y+w=0,
\qquad s\perp t.
\]

The three-cherry star table gives six left-right matchings:

- four give root-valued star completions;
- exactly two are forbidden;
- both forbidden matchings contain the pair `s--t`.

### Theorem 4.1 — star or forced backbone

At every pivot-change cell exactly one of:

1. a composition-compatible star route gives a root-valued relative
   replacement;
2. the physical route changes or a separator/category/bounded exit appears;
3. every compatible matching contains the forced pair `s--t`.

Inside a nonterminal trapped component only Case 3 remains.

The two residual pairings of the other four ports are exactly the crossed DDD
routes `X_F,Y_F` for `F={s,t}`.  Canonical Petersen transport maps the unordered
pair `{X_F,Y_F}` bijectively to the crossed pair at the next atom.  Consequently
one initial crossed sheet determines the whole forced chain; there is not an
independent binary choice at each cell.

---

## 5. One full-state pivot walk

After resolving constant runs and restricting to the forced branch, a
persistent atom component determines

\[
s_0,F_1,s_1,F_2,s_2,\ldots,
\qquad
F_j=\{s_{j-1},s_j\},
\]

one walk in the Petersen graph, together with:

- one transported crossed sheet;
- the full rooted carrier replacing each constant run;
- all side roots and attachments;
- the unchanged cap-oriented route block.

No branching atom alphabet and no chain of independent route bits remains.

---

## 6. Physical immediate-backtrack removal

An immediate pivot backtrack is

\[
s\to t\to s.
\]

Its forced shore-resolution word is

\[
t,s,s,t,
\]

the Type-T `abba` word.  This coefficient identity alone does not permit a
source contraction.

Instead work in a lifted Ptolemy comparison minimal in singular edge count.
Rootify the middle `t`-pivot run by Theorem 3.1, treating all of its side
attachments as fixed rooted branches.  The two remaining opposite
pivot-change cells form a labelled Type-T bigon in the history disc.  The local
involution/square/pentagon lift and the canonical disjoint-doubled root square
give a root-valued filling with the same complete boundary histories and
rooted attachments.

Replacing the bigon removes the two singular switch edges and changes no
outer state.  This contradicts minimality.

### Theorem 6.1 — no backtrack in a minimal lift

A singular-component-minimal full-state lifted comparison contains no
immediate Petersen pivot backtrack.

This is diagrammatic bigon removal.  It does not assert universal deletion of
an arbitrary embedded `abba` four-pole from the original graph.

---

## 7. Shortest repeated-pivot core

After Theorem 6.1 the pivot walk is reduced.  The Petersen graph has ten
vertices.

- A reduced open path with more than nine edges repeats a pivot.
- Choose a repeated pair at minimum positive distance.
- The interior pivots are distinct.
- The segment is not a two-edge return because backtracks are absent.

Therefore the segment is a simple Petersen cycle.  The complete simple-cycle
length list is

\[
\boxed{5,6,8,9}.
\]

### Theorem 7.1 — full-state recurrence core

Every nonterminal recurrent singular component contains, after physical
constant-run and bigon consumption, one shortest full-state pivot-closed
subtrack whose Petersen projection is a simple `C_5`, `C_6`, `C_8` or `C_9`.

All side attachments, the transported crossed sheet and the distinguished cap
block remain attached to this bounded core.

---

## 8. Output to R2.5 and R2.6

R2.4 supplies exactly:

1. one nonbranching physical Petersen walk;
2. no constant-pivot or immediate-backtrack ambiguity;
3. one simple bounded pivot-closed core;
4. full side/cap/route data retained.

It does not eliminate the core.

- R2.5 excludes `C_5,C_9` using the physical orientation kernel.
- R2.6 replaces `C_6,C_8` by root-valued annuli/strips/seams.

---

## 9. Trust boundary

### Closed here

- standard-atom/Petersen-edge dictionary;
- complete critical-overlap relocation alphabet;
- physical rootification of constant-pivot runs;
- six-port star/forced-backbone alternative;
- one transported crossed sheet;
- full-labelled pivot-walk construction;
- diagrammatic Type-T bigon removal;
- shortest simple-cycle extraction;
- retention of side, cap and route data.

### Not closed here

- orientation calibration and odd exclusion;
- `C6/C8` source replacements;
- contextual-transfer synthesis and cap restoration;
- universal five-support conclusion;
- independent audit, Lean verification, curation, manuscript integration,
  release, arXiv, DOI, peer review or publication.
