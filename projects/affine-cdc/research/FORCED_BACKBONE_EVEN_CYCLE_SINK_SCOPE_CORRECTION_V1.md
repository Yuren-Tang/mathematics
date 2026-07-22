# Scope correction: an even Petersen core is not automatically a four-pole

## Research dossier v1 — correction quarantine

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `4133638ba396c7d77596eef17e30f1e4e829b277`.

**Corrects:** `PTOLEMY_TRACK_FORCED_BACKBONE_SINK_ELIMINATION_V1.md`.

**Retains exactly:**

- persistence of only co-root atoms in a pure same-order flip block;
- canonical Petersen-edge state of one co-root atom;
- adjacent-atom/shared-resolution dictionary;
- identification of a no-exit multi-cell track with a forced Petersen backbone;
- deletion of history backtracks;
- reduction of recurrence to one simple Petersen cycle;
- exclusion of odd `C5` and `C9` tracks by oriented resolution parity.

**Quarantines:** Sections 8--11 of the corrected dossier insofar as they apply the four-port equality/DDD global potentials directly to a simple `C6` or `C8` pivot core.

**Status:** exact interface correction. A simple Petersen six-cycle is an identity-hexagon coefficient core with six side-root outputs, and a simple eight-cycle is a DDD-octagon coefficient core with eight side-root outputs. The cycle classification does not state that the complete physical region bounded by a multi-cell defect track is a four-pole with boundary `r^4` or `p,p,q,q`. Arbitrary side components may attach to those outputs. Therefore the existing full-ten-triangle four-pole potentials cannot be invoked until an enclosure/compression theorem reduces the side-output carrier to a composition-safe four-port object, route escape, or separator.

**Not implied:** failure of the forced-backbone identification, existence of a new coefficient obstruction, failure of the overall proof route, canonical acceptance, Lean verification, manuscript integration, release, publication, or the global five-support theorem.

---

## 1. Exact even-cycle outputs

The simple-cycle classification gives:

### Six-cycle

One root-labelled identity hexagon with emitted side-root word

\[
(xy,xz,yz,xy,xz,yz).
\]

It has six output occurrences, not four.

### Eight-cycle

One DDD octagon attached to a disjoint root pair

\[
F=\{p,q\}.
\]

Its output multiset is

\[
E(K_4)\sqcup F,
\]

with eight occurrences.

These are exact coefficient cores. Their physical source realizations may have external components attached at every output occurrence.

---

## 2. Why the four-pole potential does not apply immediately

The equality global potential assumes one connected root-labelled four-pole whose only boundary roots are

\[
r,r,r,r.
\]

The DDD global potential assumes one connected root-labelled four-pole whose boundary multiset is

\[
p,p,q,q.
\]

Neither hypothesis follows merely from the pivot/output classification of a six- or eight-cycle.

To apply those potentials one must first prove that:

1. the side outputs pair or enclose into the required four-port boundary;
2. surplus output attachments can be peeled or separated;
3. the ordered cap route survives the enclosure;
4. no unbounded outside component carries independent return semantics.

These are precisely the composition statements left open in the simple-cycle dossier.

---

## 3. Correct status of the sink-SCC argument

Suppose a finite same-order contextual state graph has a nonterminal sink SCC. The forced-backbone theorem still implies that any recurrent co-root track contains an even simple cycle.

What is not yet proved is that one may choose a root state inside the SCC to which `P_eq` or `P_DDD` applies.

The even cycle may be only a bounded coefficient spine decorated by a six-/eight-output attachment system. The full physical state need not lie in either four-pole domain.

Therefore the contradiction by choosing a minimum four-pole potential inside the SCC is not yet valid.

---

## 4. Corrected remaining theorem

### Target 4.1 — even-track enclosure

Let one closed nonbranching Ptolemy defect track have reduced forced-backbone core `C6` or `C8`. Prove one of:

1. a side attachment changes the transported route and gives cap-profile escape;
2. the outputs split through a two-, three-, or four-edge separator;
3. a serial/laminar output interval peels with strict descent;
4. the complete track encloses a composition-safe equality four-pole (`C6`) or DDD four-pole (`C8`);
5. the complete carrier is a bounded direct-pairing/identity/DDD terminal;
6. a strictly smaller contextual track remains.

Only after Alternative 4 may the global four-pole potentials be invoked.

---

## 5. Relation to the earlier final-composition synthesis

The corrected target is exactly the spine--attachment theorem identified before the Pachner programme:

- the spine is now canonically `C6` or `C8`;
- its coefficient and orientation data are completely known;
- the only unbounded datum is the attachment of outside components to six or eight output occurrences;
- crossing attachments must yield route escape;
- split attachments must yield a small separator;
- laminar attachments must admit peeling or a smaller enclosed carrier.

Thus no new obstruction species has appeared. The proof has returned, in a more rigid form, to the same final composition bridge.

---

## 6. Trust boundary

### Exact here

- six/eight output counts of the even Petersen cores;
- distinction between a coefficient core and a complete four-pole source region;
- invalidity of the direct four-pole-potential application without enclosure;
- preservation of the multi-cell track/backbone identification and odd-cycle exclusion;
- exact revised even-track target.

### Quarantined

- unconditional sink-SCC elimination from the equality/DDD four-pole potentials;
- unconditional same-order contextual reachability in the corrected dossier;
- unconditional contextual-transfer theorem based on that sink argument.

### Still open

- even-track side-output enclosure/compression;
- sink-SCC elimination after enclosure;
- complete contextual transfer;
- reverse global dependency audit and global theorem packaging;
- canonical acceptance, independent audit, Lean verification, manuscript integration, release, publication;
- the global five-support theorem.
