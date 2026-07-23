# AC-PD-5CDC R2.7 — fixed-order consumer compatibility

**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Programme:** compressed five-support proof, global-return unit `R2.7`  
**Classification:** `COMPLETE-DRAFT / HW3 CLOSED FOR THE CONTROLLING NORMAL-FORM EXECUTION / RAW SUPPORT-SWITCH CELLS ARE NOT INTERIOR PTOLEMY CELLS`.

This dossier closes the final variable-order compression interface.  It also
corrects one overbroad reading of the authorial nested-bubble packet: a raw
support-switch even correction with a zero/co-root insertion edge is not, by
itself, an ordinary Ptolemy cell and must not be placed unmodified inside the
closed-track theorem.

---

## 1. The fixed-order consumer

The retained closed/open/periodic singular-track theorems consume a lifted
history whose internal comparison cells are root `2--2` Pachner cells, together
with immediate bounded normalization of one first-failure atom.

They prove:

- internal closed standard co-root tracks erase;
- an open standard track with root-normalized or accepted short sides has a
  root strip;
- repeated unresolved outer endpoints form a fixed-order cylinder with a root
  seam discharge.

Their internal Petersen/annulus argument is not a theorem about an arbitrary
global even-correction cell.

---

## 2. Immediate state normalization

A raw insertion at marked roots `p,q` is not admitted as a persistent complete
state until its central row is normalized.

### `B` row

If `p,q` are distinct intersecting, the insertion is root-valued.

### `A` row

If `p=q`, use the adjacent-borrow alternative insertion.  The raw zero state
and its one-zero intermediate are internal to one bounded macro; the complete
state vertex is the root-valued alternative insertion or a bounded theta exit.

### `C` row

If `p\perp q`, use the doubled-disjoint borrowing dichotomy.

- good borrow: the complete state vertex is a root-valued alternative
  insertion;
- missing-index borrow: the raw doubled-disjoint atom is converted, through
  the bounded two-co-root transport unit, to one standard normalized co-root
  atom of the established `(Q_i,Q_j,ij)` grammar.

The transient two-co-root tree is internal to the normalization macro and is
not a state-graph vertex.

### Definition 2.1 — normalized insertion state

Write

\[
N(H,\lambda;e,f)
\]

for any output of the above complete local normalization, with deterministic
choice of the first available ordinary borrow and a fixed bounded tie-break.
Every normalized state is either fully root-valued, one standard co-root atom,
or an accepted exit.

This removes raw doubled-disjoint fibres from the global singular alphabet.

---

## 3. Normal form of the controlling witnessed history

The witnessed relative proposition `Q_N` may be proved using the following
move normal form.

### Internal locked descent

After the separating-channel test has failed and the fixed route has been
chosen, the equality and DDD positive Morse theorems select only:

1. one strictly potential-lowering root NNI;
2. one equal-face cancellation;
3. a route/profile terminal.

No nonterminal support switch is required in the interior of a locked Morse
episode.

### Support switches

A support-pair switch is used only as:

1. the initial separating equality/DDD rescue, which gives the cap immediately;
2. a route/profile escape;
3. a horizontal rootification of an endpoint atom;
4. a bounded theta terminal normalization.

In each case the switch is terminal for the current frame or is a
root-normalized endpoint cell.  Switches which preserve the blocked relation
without producing one of these outcomes are omitted from the deterministic
proof history.

### Theorem 3.1 — support-switch terminal normal form

The existence proof for `Q_N` can be chosen so that no support-switch correction
cell lies in the interior of a recurrent singular episode.

This is a choice of proof history, not a claim that arbitrary support switches
lack mathematical meaning.

---

## 4. Terminal switch--pop collars

Suppose an innermost child frame ends by a separating support switch or bounded
theta switch sequence and then returns through its paired insertion.

Do not retain the raw lifted support-switch cell as an internal fixed-order
cell.  Combine:

1. the terminal lower root-valued switch;
2. its raw insertion lift;
3. the returned `A/B/C` row;
4. immediate normalization from Section 2;

into one **switch--pop collar**.

The collar has:

- one root-valued child short side;
- one root-valued or standard-one-atom parent side;
- complete fixed ordered exterior incidences;
- the inherited cap block and route record;
- no persistent raw doubled-disjoint state.

If the output is root-valued, no singular arc begins.  If it is one standard
co-root atom, the collar is the birth endpoint of one ordinary open track.  The
reverse situation is a death endpoint.

### Lemma 4.1

A switch--pop collar is a root-normalized or accepted endpoint cell in the
sense required by the corrected open-strip theorem.  It is not an internal
Ptolemy cell.

---

## 5. Root-NNI generator lifts

Every nonterminal generator lift left after Section 3 is a finite sequence of
relative root NNIs with bounded local normalization.

For active-diagonal movies:

- `B`-preserving movies are fully root-valued;
- `B`-exit movies end in a raw `A/C` row which is normalized immediately by
  Section 2;
- reverse movies begin at the corresponding normalized endpoint;
- equal/opposite and adjacent-mark cases are finite NNI movies with at most one
  local atom after immediate normalization.

Hence their persistent singular states are exactly the standard first-failure
co-root states used by the full-state Petersen track theorem.

No new cell alphabet is introduced.

---

## 6. Shape of the flattened singular locus

Flatten all successful nested bubbles using:

- witnessed root-NNI lift paths;
- immediate insertion normalization;
- switch--pop collars at terminal support switches;
- identity gluing of complete labelled seams.

Then every connected component of the persistent singular locus has:

1. internal edges lying only in root-NNI/Ptolemy comparison cells and their
   established bounded critical-overlap normalization;
2. endpoints only at:
   - a normalized local root/atom cell;
   - a switch--pop collar with a root-valued short side;
   - an accepted route/bounded/separator exit;
   - the unresolved original outer endpoint.

In particular:

\[
\boxed{
\text{no support-switch correction cell belongs to an internal closed
singular component}.}
\]

### Proof

By Theorem 3.1 every support switch is terminal for its frame.  Bubble
compression pairs it with the immediate pop and replaces the pair by the
collar of Section 4.  Such a collar lies on the boundary of the resulting
singular arc.  All remaining internal moves are root NNI movies. ∎

---

## 7. Consumption by the retained track theorems

### Closed components

A closed singular component has no endpoint collar.  By Section 6 all of its
internal cells are Ptolemy/root-NNI cells.  Therefore
`PTOLEMY_CLOSED_DEFECT_TRACK_ERASURE_V1.md` applies without enlargement:
constant-pivot runs rootify, odd cores are impossible and even cores have root
annuli.

### Open components

If both endpoints are normalized collars or accepted exits, both short sides
are root-valued/discharged.  The corrected open-strip theorem applies.

If one endpoint is the unresolved original outer context, continue the
controlling finite episode.  A repeated complete endpoint state yields the
fixed-order periodic cylinder, and the root-seam discharge applies.

### Root-only support histories

Bounded theta switch histories and separating rescue switches lie wholly on
root-valued/terminal sides.  They neither create singular components nor alter
the Petersen core calculation.

### Theorem 7.1 — consumer compatibility

Every fixed-order history produced by the controlling normalized bubble
compression lies in the exact scope of the retained closed/open/periodic
track package.  No raw support-switch atom cell is consumed as though it were a
Ptolemy cell.

Thus:

\[
\boxed{\texttt{AC-PD-5CDC-HW3 CLOSED}.}
\]

---

## 8. Consequence for variable-order compression

Combining:

- `HW1`: inherited child history witnesses by simultaneous `P_N/Q_N`
  induction;
- `HW2`: full-labelled genealogy and seam gluing;
- `HW3`: fixed-order consumer compatibility;

proves the fixed-order episode-compression interface for the **chosen
controlling normal-form execution**.

### Corollary 8.1 — normalized FOC

Every finite successful variable-order continuation episode arising in the
controlling one-cross proof has a complete boundary-preserving fixed-order
replacement whose persistent singular locus is one nonbranching standard
co-root track system accepted by the fixed-order closed/open/periodic consumer.

This is the precise form of FOC needed by contextual transfer.  It is weaker
than an arbitrary mixed-history compression theorem and sufficient for the
existence proof.

---

## 9. Correction to the authorial nested-compression wording

The authorial list

> root NNIs; root support switches; one-atom raw support-switch cells; endpoint
> rootification cells

must not be read as four interchangeable internal cell types of one Ptolemy
van Kampen diagram.

Use instead:

- root NNIs and normalized critical-overlap cells internally;
- support switches only in terminal switch--pop collars or wholly root-valued
  bounded histories;
- raw `A/C` insertions only inside immediate normalization macros.

With this correction, the fixed-order consumer is not enlarged beyond its
proved source scope.

---

## 10. Trust boundary

### Closed here

- statewise elimination of raw zero/doubled-disjoint persistent states;
- controlling support-switch terminal normal form;
- switch--pop collar construction;
- normalized active-diagonal generator interface;
- proof that closed singular cores contain only Ptolemy cells;
- open/periodic endpoint compatibility;
- normalized FOC for the chosen proof execution;
- `HW3`.

### Still requires reconstruction before global completion

- the retained R2.4 full-state forced-backbone theorem;
- R2.5 orientation-hardened odd exclusion;
- R2.6 actual `C6/C8` root annulus/strip/seam source replacements;
- the final contextual-transfer synthesis using normalized FOC;
- cap restoration and global cubic/outer-shell assembly;
- independent audit, Lean verification, curation, manuscript integration,
  release, arXiv, DOI, peer review or publication.

### Current classification

\[
\boxed{
\text{VARIABLE-ORDER COMPRESSION INTERFACES HW1--HW3 CLOSED}
\;/\;
\text{R2.4--R2.6 AND FINAL SYNTHESIS REMAIN}.
}
