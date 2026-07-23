# AC-PD-5CDC R2.5A — pre-cancellation `C6` scope correction

**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Research correction consumed:** `PRE_CANCELLATION_C6_MOVIE_AND_MIXED_SCC_SCOPE_CORRECTION_V1.md`  
**State:** `CORRECTION / LOCAL MOVIE RETAINED / SAME-ORDER CONTEXTUAL EXIT WITHDRAWN`.

---

## 1. Corrected distinction

Three objects must remain separate.

1. A **local six-port chart**: the root cross path and the canonical star are joined by one relative root NNI.
2. An **annular history movie**: six compatible local charts are attached to six history cells and agree on rooted turn interfaces.
3. A **contextual state**: one cubic source graph or multipole, one complete root/token assignment, one active history position, and all cap, route and incidence data.

The first two do not by themselves produce the third.

---

## 2. Why the six canonical charts are not one cubic time slice

Let `R_i` be the rooted turn corolla shared by Cells `i-1` and `i`. In the canonical star of Cell `i`, its root-`z_i` spoke leads to centre `O_i`; in Cell `i-1`, the same rooted interface has a root-`z_i` spoke leading to `O_(i-1)`.

If both chart interiors are placed on the same side of one physical `R_i`, either:

- both spokes remain, violating cubicity at `R_i`; or
- the spokes are identified, forcing `O_i=O_(i-1)`.

Cyclic repetition of the second choice identifies all centres and again violates cubicity. Hence shared-corolla equality is a history-interface identity, not a simultaneous-subgraph instruction.

Therefore the previous PDL sentence that the two annular boundaries may be canonicalised to one common star-section state and joined by an identity root cylinder is withdrawn.

---

## 3. Retained exact mathematics

The following remain valid proof units.

1. For a fixed two-turn cell, the relative branch word is `(z,z,w,w)`.
2. Its three binary resolutions have type `(0,2,2)`.
3. Exactly two resolutions are root-valued: the cross path and canonical star.
4. They differ by one root NNI fixing both turn corollas and every exterior root incidence.
5. Adjacent cell movies are compatible as relative history movies.
6. Every canonical star contains one equal-face dipole with boundary word
   \[
   (z,z,w,w),\qquad z\ne w,\qquad z+w\in R_5.
   \]
7. The `C8` seam calculation remains a valid reduction to two compatible `C6` history cells.

These are local/history theorems. They do not prove a complete root-valued contextual time slice before cancellation.

---

## 4. Mixed SCC correction

A positive-prefix root state has an edge either to:

- a lower-prefix root state, if the next inverse move succeeds; or
- a normalized token state, if it first fails.

The second state may lie in the same strongly connected component and may return to a root state through an alternative root resolution. Hence a nonterminal sink SCC need not be token-only.

The valid statement is weaker:

> after deterministic successful inverse moves are contracted, every nonterminal recurrent component contains a persistent singular state.

Any controlling no-sink theorem must either prove a quotient from mixed root/token SCCs to a token transition system which preserves all exits, or analyse the mixed recurrent paths directly.

---

## 5. Consequence for the proof DAG

The prior PDL unit

`AC_PD_5CDC_R2_5_EVEN_TRACK_CYLINDER_ERASURE.md`

is retained only as a record of the correct local `(0,2,2)` and root-star calculations. Its claimed same-order contextual cylinder erasure is superseded by this correction.

The even-core status is now:

\[
\boxed{
\text{LOCAL/HISTORY MOVIE CLOSED}
/
\text{COMPLETE CONTEXTUAL EXIT OPEN}.}
\]

The load-bearing global return remains the marked-weld/cancellation-re-entry problem.

---

## 6. Trust boundary

### Exact here

- the distinction among local chart, annular movie and contextual state;
- the cubic-incidence obstruction to simultaneous six-chart gluing;
- retention of all local root-NNI and equal-face data;
- correction from token-only to potentially mixed root/token SCCs;
- withdrawal of the PDL cylinder-erasure consumer.

### Not claimed

- impossibility of an alternating-star time slice with additional structure;
- failure of the local `C6/C8` movies;
- impossibility of repairing marked-weld return;
- global five-support or five-CDC closure.