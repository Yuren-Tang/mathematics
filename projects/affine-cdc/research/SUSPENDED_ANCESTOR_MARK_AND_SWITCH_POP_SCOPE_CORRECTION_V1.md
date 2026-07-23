# Scope correction: successful bubbles may suspend ancestor marks, and support switches are endpoint collars

## Research Lead correction and PDL-consumer alignment v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`

**Corrects the overbroad readings of:**

- `WELD_CENTRAL_MARK_CANCELLATION_POP_V1.md`;
- `CALL_FREE_CHILD_EPISODE_PARENT_LIFT_V1.md`;
- `VARIABLE_ORDER_RECURRENT_EPISODE_COMPRESSION_V2.md` v2.1;
- `ROOT_NORMALIZED_CONTEXTUAL_TRANSFER_MASTER_V6.md`;
- any statement placing a raw support-switch correction cell inside the ordinary Ptolemy closed-track consumer.

**Independent proof-development inputs:**

- `AC_PD_5CDC_R2_7_FULL_LABELLED_GENEALOGY_GLUING.md`;
- `AC_PD_5CDC_R2_7_FIXED_ORDER_CONSUMER_COMPATIBILITY.md`.

**Status:** exact scope correction. A central marked edge has no pointwise descendant in the raw lower-order graph, but a successful paired cancellation/return bubble may admit a boundary-equivalent fixed-order replacement in which a mark belonging to a surviving ancestor frame is carried as a suspended mark on the central dart pair of every raw insertion state. This is an explicit relative-history construction, not automatic genealogy through the deleted child edge. Consequently central-mark deletion is not an unconditional global descent coordinate.

Likewise, the source formula for lifting a lower support switch is correct, but a raw support-switch correction with singular central insertion is not an internal Ptolemy cell. For the controlling proof execution, support switches are chosen only as terminal rescue/route/bounded moves and are paired with the immediate child pop and insertion normalization into a switch--pop endpoint collar. Closed singular components then contain only root-NNI/Ptolemy cells and their established bounded critical-overlap normalization.

The resolved-call rank `(N,d_N)` remains valid and controlling because it does not rely on irreversible mark consumption or treat arbitrary support-switch cells as Ptolemy generators.

---

## 1. Three different notions of a mark

One must distinguish:

1. **raw child genealogy:** actual ordered darts present in the lower-order graph;
2. **surviving ancestor boundary mark:** a relative obligation belonging to a containing frame and required on both collars of a successful bubble replacement;
3. **call-local mark:** auxiliary ordered data introduced only for the child call and discarded when that frame is eliminated.

Conflating these gives two opposite errors:

- claiming pointwise survival of a deleted central edge in the lower graph;
- claiming that every successful bubble permanently destroys an ancestor boundary obligation.

Both are false.

---

## 2. Raw central cancellation

For an equal-face pair with central edge `e`, forward `2--0` cancellation deletes both endpoint darts of `e`. The lower-order graph contains no descendant central edge.

Thus `WELD_CENTRAL_MARK_CANCELLATION_POP_V1.md` remains exact for raw child genealogy:

\[
\boxed{
\text{central marked darts are absent from the lower graph}.}
\]

No output incidence may be called their pointwise descendant.

If the child exits and the parent branch terminates, no mark restoration is required.

---

## 3. Raw insertion states in a successful paired bubble

Suppose the forward cancellation is paired with a finite witnessed child history and a returned insertion.

For every child state

\[
(H_i,\lambda_i;p_i,q_i)
\]

form its predecessor-order raw insertion

\[
I(H_i,\lambda_i;p_i,q_i).
\]

This expanded state restores:

- the two parent vertex slots;
- the four ordered output half-edges;
- one central dart pair carrying `p_i+q_i`, possibly root, zero or co-root.

If the original central mark belongs to a still-live ancestor frame, mark this central dart pair as a **suspended ancestor mark**.

This mark is not asserted to exist in `H_i`. It is boundary-relative data of the fixed-order replacement strip.

---

## 4. Transport of the suspended mark

### Support switch

The lifted even correction changes the central coefficient according to

\[
r'=r+(\epsilon_p+\epsilon_q)h
\]

but fixes the two central dart slots of the raw insertion state. The suspended mark stays on those slots.

### Disjoint/exterior root NNI

The raw insertion support and child NNI commute or meet only in fixed exterior branches. The central marked dart pair is unchanged.

### Active-diagonal root NNI

The six-leaf predecessor-order lift has literal complete endpoint states. Its explicit labelled NNI path gives a one-to-one transport of the suspended central boundary mark through the mobile envelope. No duplication occurs.

### Endpoint normalization

- `B`: the mark lies on the root central edge of the original insertion;
- `A`: the labelled five-leaf alternative-insertion path transports it to the corresponding central edge of the alternative root topology;
- good `C`: the same holds for the good alternative insertion;
- missing-index `C`: it is carried to the unique normalized co-root atom and its crossed resolutions.

Hence a successful bubble has a completely marked fixed-order replacement, even though the raw lower graph had no central mark.

### Theorem 4.1 — suspended ancestor-mark gluing

A successful witnessed cancellation/child/return bubble preserves every ancestor mark required by its surrounding complete boundary, via an explicit suspended-mark fixed-order replacement. It does not assert pointwise lower-order ancestry.

---

## 5. Correct mark bookkeeping under innermost-call elimination

When eliminating one innermost call:

- passive surviving-frame marks are carried pointwise;
- a surviving ancestor central mark is carried by Theorem 4.1;
- call-local marks are discarded with the eliminated frame;
- a child exit terminates the branch and requires no pop mark;
- no mark is created without an explicit current boundary rule.

Therefore one-call elimination preserves the complete boundary data of the containing frame.

### Correction to mark monotonicity

The implication

\[
\text{central raw cancellation}
\Longrightarrow
\text{strict permanent decrease of every global active-mark count}
\]

is false for a successful paired bubble carrying a surviving ancestor obligation.

Mark count may be used as a local raw-call diagnostic, but not as a controlling global well-founded coordinate unless the theorem explicitly excludes suspended restoration.

The controlling resolved-call rank does not use it.

---

## 6. Support switches and the Ptolemy consumer

`WELD_SUPPORT_SWITCH_SOURCE_POP_V1.md` proves a valid source-level lifted correction. It does not prove that the resulting global correction cell is an ordinary Ptolemy `2--2` cell.

A raw support-switch insertion cell with central value `0` or `Q_i` must not be placed in the interior of the closed-track annulus argument.

### Controlling normal-form choice

Choose the witnessed relative proof so that every support switch is one of:

1. an initial separating rescue which immediately solves the cap;
2. a route/profile exit;
3. a horizontal endpoint rootification;
4. a bounded theta/direct terminal normalization.

No nonterminal support switch is retained in the interior of a locked recurrent Morse episode.

### Switch--pop collar

For a terminal child support switch, combine:

- the lower root-valued switch;
- its raw predecessor-order lift;
- the returned `A/B/C` insertion row;
- immediate insertion normalization;

into one bounded switch--pop collar.

The collar is:

- root-valued on its child short side;
- root-valued, accepted or one-standard-atom on its parent short side;
- an endpoint of an open singular track when an atom remains;
- not an internal Ptolemy cell.

### Theorem 6.1 — normalized fixed-order alphabet

For the chosen controlling proof execution, every persistent closed singular component contains only:

- root-NNI/Ptolemy comparison cells;
- established bounded critical-overlap normalization cells.

Support switches occur only on root/accepted histories or in endpoint switch--pop collars. Therefore the retained closed/open/periodic track package is used within its proved source scope.

---

## 7. Consequence for variable-order compression

The correct flattened history is not an arbitrary concatenation of root NNIs and raw support-switch cells.

It is obtained by:

1. lifting all nonterminal root-NNI child generators;
2. normalizing raw `A/C` insertion states immediately;
3. pairing every terminal support switch with its pop into a switch--pop collar;
4. gluing complete labelled seams, including suspended ancestor marks;
5. applying the track package only to the resulting normalized Ptolemy interior.

This is the precise fixed-order compression needed for the existence proof. It is weaker than arbitrary mixed-history compression and sufficient.

---

## 8. Consequence for v6

Read `ROOT_NORMALIZED_CONTEXTUAL_TRANSFER_MASTER_V6.md` with two corrections:

1. central raw mark deletion does not imply permanent ancestor-mark loss in a successful paired bubble; use suspended ancestor-mark gluing;
2. support-switch lift/pop cells are endpoint collars or terminal root histories, not arbitrary internal cells of the fixed-order closed-track diagram.

The remaining controlling architecture is unchanged:

- witnessed lower-order histories from inherited flows;
- innermost-call elimination;
- fixed-order track disposition after normalized flattening;
- resolved-call macro graph;
- shortest-distance rank `d_N`;
- lexicographic induction on `(N,d_N)` and then the original prefix.

---

## 9. Assurance boundary

### Exact here

- distinction between raw genealogy, suspended ancestor marks and call-local marks;
- explicit relative restoration of a surviving ancestor mark through a successful bubble;
- no contradiction with raw central-edge deletion;
- rejection of unconditional global mark monotonicity;
- terminal support-switch normal form;
- switch--pop endpoint collar;
- exclusion of raw support-switch cells from closed Ptolemy cores;
- corrected fixed-order compression alphabet.

### Still required downstream

- PDL reconstruction of the `C6/C8` annulus, strip and periodic-seam source replacements;
- final proof-development synthesis of R2.7;
- independent audit;
- cap restoration/global five-support consequences;
- Lean, manuscript, curation, release and publication work.
