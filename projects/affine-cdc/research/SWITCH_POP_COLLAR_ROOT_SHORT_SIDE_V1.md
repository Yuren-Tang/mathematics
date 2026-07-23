# A switch--pop birth collar has a genuine root-valued short side

## Research Lead endpoint-interface theorem v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`

**Parents:**

- `WELD_SUPPORT_SWITCH_SOURCE_POP_V1.md`;
- `SUSPENDED_ANCESTOR_MARK_AND_SWITCH_POP_SCOPE_CORRECTION_V1.md`;
- `OPEN_TRACK_ROOT_STRIP_ENDPOINT_SCOPE_CORRECTION_V1.md`;
- the immediate `A/B/C` insertion-normalization table.

**Status:** exact endpoint theorem for the normalized fixed-order consumer. A terminal lower-order support switch followed by its inverse-weld pop is not an internal Ptolemy cell. If the returned insertion is root-valued, no singular track is born. If it returns one normalized co-root atom, the combined switch--pop macro has an initial predecessor-order `B` insertion which is fully root-valued; a small endpoint collar may be chosen with its short side lying entirely in that initial root boundary. The unique singular half-track begins on the opposite side of the collar. Therefore the collar is a root-normalized endpoint in the precise sense needed by the corrected open-strip theorem.

The theorem does not claim a root-valued path through the raw singular support-switch correction.

---

## 1. Before the terminal switch

Let the two lower-order output edges carry roots

\[
p,q\in R_5,
\qquad
p\ne q,
\qquad
|p\cap q|=1.
\]

Their predecessor-order inverse insertion has central root

\[
r=p+q\in R_5.
\]

Denote this complete root-valued expanded state by

\[
X^-.
\]

It includes:

- the four ordered output half-edge incidences;
- the two inserted vertex slots;
- central root `r`;
- every exterior root label;
- cap block, route, side and surviving/suspended mark data.

---

## 2. Terminal lower support switch

Let one legal lower-order support-pair component switch in direction `h` change the output roots to

\[
p'=p+\epsilon_p h,
\qquad
q'=q+\epsilon_q h.
\]

The child switch is root-valued on the lower graph. It is terminal for the child frame:

- a separating rescue;
- a route/profile exit;
- a horizontal endpoint rootification;
- or a bounded terminal sequence.

If the parent branch continues, evaluate the returned insertion central value

\[
r'=p'+q'=r+(\epsilon_p+\epsilon_q)h.
\]

Exactly one of the `A/B/C` rows occurs.

---

## 3. Root output

If `r'` is a root, immediate inverse insertion/normalization gives a fully root-valued parent state

\[
X^+.
\]

The switch--pop collar contains no persistent singular edge.

### Proposition 3.1

A root-valued switch--pop output is part of a root/terminal history and creates no endpoint of the co-root singular locus.

---

## 4. One-atom output

Assume the output pair first leaves `B` and immediate normalization gives one standard co-root atom.

Let the normalized parent state be

\[
A^+.
\]

Every edge of `A^+` except the atom is a root. The atom carries its two crossed root resolutions and complete full-state data.

Combine into one bounded macro collar:

1. the root state `X^-` before the terminal child switch;
2. the lower root-valued switch;
3. the raw predecessor-order insertion lift;
4. the returned `A/C` row;
5. immediate normalization to `A^+`.

The raw global correction cell is retained inside the collar only. It is not an internal cell of the later Ptolemy track.

---

## 5. Location of the short side

Choose a sufficiently small regular neighbourhood of the unique singular half-edge leaving the collar toward the later one-token history.

Place the transverse short side immediately before the first singular central value is created, on the `X^-` boundary of the collar.

This short side is completely root-valued because `X^-` is the original `B` insertion state.

It fixes literally:

- all ordered exterior incidences;
- both inserted vertex slots;
- the central root `r`;
- cap block and route orientation;
- all side roots and rooted attachments;
- every surviving or suspended ancestor mark.

The singular locus meets the collar in one half-edge whose endpoint lies after this root short side and whose continuation is the standard co-root track from `A^+`.

### Theorem 5.1 — root short side of a birth collar

A switch--pop macro which outputs one normalized co-root atom is a valid root-normalized birth endpoint for the open-track theorem. Its short side is the initial root-valued `B` insertion boundary `X^-`, not a path through the raw singular correction.

---

## 6. Death collar

Reverse the above local history.

If an incoming standard co-root track is consumed by a terminal support-switch/pop normalization, choose the short side on the final root-valued `B` insertion boundary.

### Corollary 6.1 — root short side of a death collar

The reverse switch--pop collar is a valid root-normalized death endpoint for an open singular track.

---

## 7. Open-strip interface

Let an open standard co-root track have one endpoint at a switch--pop collar.

Replace a small initial segment of the track together with the collar by the normalized endpoint model above. The resulting regular rectangle has:

- a root-valued short side supplied by Theorem 5.1 or Corollary 6.1;
- two root-valued long side histories adjacent to the track;
- complete labelled exterior data.

Hence this endpoint is Type 1 in the corrected scope of
`OPEN_TRACK_ROOT_STRIP_ENDPOINT_SCOPE_CORRECTION_V1.md`.

If the other endpoint is also root-normalized/accepted, the root-strip theorem applies.

If the other endpoint is the unresolved original outer cap context, the collar theorem does not discharge that outer endpoint; periodic or other outer-endpoint analysis remains necessary.

---

## 8. Forbidden overreadings

This theorem does not assert:

- that a support switch is an ordinary `2--2` Pachner cell;
- that the raw co-root insertion has a root-valued transverse path through its centre;
- that every support switch may occur inside a closed singular core;
- that one root-normalized endpoint suffices when the other endpoint is unresolved;
- that the child and parent histories have the same order before bubble compression.

---

## 9. Assurance boundary

### Exact here

- existence of the initial root-valued `B` insertion state;
- complete switch--pop collar construction;
- absence of a singular component in the root-output row;
- one singular half-track in the normalized co-root row;
- explicit location of a root-valued short side;
- birth/death endpoint compatibility with the corrected open strip;
- preservation of full cap/route/mark data on the short side.

### Not claimed

- PDL reconstruction;
- the complete open-strip or periodic-seam theorem;
- final R2.6/R2.7 assurance;
- cap restoration, global five-support, Lean, manuscript, curation, release or publication status.
