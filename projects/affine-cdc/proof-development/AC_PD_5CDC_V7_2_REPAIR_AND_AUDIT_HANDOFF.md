# AC-PD-5CDC v7.2 — repair and focused independent-audit handoff

**Producer:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Frozen RL input:** `research/affine-cdc-five-cdc-v1@094ca09f6d3982b785a3f3428d9ec079dbba0855`  
**Candidate:** the exact PDL commit containing this handoff  
**Classification:** `PARTIAL RECONSTRUCTION / ONE NAMED BLOCKER / NOT A FULL-THEOREM AUDIT CANDIDATE`.

---

## 1. Scope of the next review

The next independent role should not audit the old candidate `1f57422...` again
and should not assume the RL classification of v7.2.  It should perform two
separate tasks.

### Part A — verify reconstructed v7.2 units

Independently recompute:

1. first-cancellation target synchronization;
2. target category at every parallel root NNI;
3. the four structural branches at the first cancellation;
4. arbitrary-flow inverse insertion rows;
5. the source-level missing-index NNI;
6. state-walk run/switch indexing;
7. all six-port seam conditions;
8. the two-seam reduced-backtrack construction;
9. literal seam/run endpoint gluing;
10. the exact 2/3/4-cut and bounded terminal ledger.

### Part B — attack the pure-NNI blocker

Determine whether the frozen source proves, or can be repaired to prove,

`AC-PD-V7.2-PURE-NNI-TARGET-REINSERTION`.

The reviewer must distinguish:

- erasing a supplied singular track;
- producing a root path between crossed resolutions;
- realizing the prescribed ordinary parent pairing;
- lowering the target topology distance.

These are not equivalent statements.

---

## 2. Exact PDL files

Controlling v7.2 files:

- `AC_PD_5CDC_PROOF_DAG_AND_STATUS.md`;
- `AC_PD_5CDC_V7_2_FIRST_CANCELLATION_AND_SINGLE_POP.md`;
- `AC_PD_5CDC_V7_2_STATE_WALK_CELLWISE_RECONSTRUCTION.md`;
- `AC_PD_5CDC_V7_2_PURE_NNI_TARGET_REINSERTION_OBSTRUCTION.md`;
- `AC_PD_5CDC_V7_2_TERMINAL_CENSUS_AND_ORDINARY_INDUCTION_BOUNDARY.md`;
- this handoff.

Older PDL files may be used only as explicitly cited local inputs.  Their old
complete-proof classifications are superseded.

---

## 3. Mandatory finite checks

### Doubled-disjoint borrowing

Recompute all ordered `(a,b,d,e)` with roots `a perpendicular b`, `d+e=a`.
Required result:

\[
180=120\text{ good}+60\text{ missing-index}.
\]

For the normal form

\[
a=12,\ b=34,\ d=15,\ e=25,
\]

verify the exact source tree

\[
(34,25,Q_1)-(Q_1,15,Q_5)-(Q_5,12,34)
\]

and the root-lowering NNI with new edge

\[
34+Q_5=12.
\]

Confirm that the output has exactly one persistent `Q_5` atom and preserves all
five exterior dart slots.

### Six-port switch cells

Enumerate every ordered nonbacktracking

\[
x\to s\to t\to y.
\]

Required result:

- `120` cases;
- `z=x+t`, `w=s+y` are always distinct intersecting roots;
- the middle word is `(z,z,w,w)`;
- pairing pattern `(0,2,2)`;
- both turn corollas remain fixed under the zero/one relative root NNI.

---

## 4. Exact blocker witness

Use

\[
(A,B,C,D)=(12,34,13,24).
\]

The prescribed parent topology

\[
AB\mid CD
\]

has central co-root `Q_5`; the crossed topologies have central roots `23` and
`14`.

The audit must answer:

1. Which frozen theorem changes this fixed boundary word?
2. Which source history returns to `AB|CD` with a root central edge?
3. Which complete-state measure strictly decreases if the scheduler alternates
   the crossed resolutions?
4. Where is the target-side boundary map of the periodic root crosscut?
5. If an ambient cut/route terminal is forced, which exact theorem proves it?

A response saying only that the track is finite, nonbranching, cellwise
rootifiable, or periodic is insufficient.

---

## 5. Accepted repair shapes

A repair passes only if it gives one of:

1. **prescribed-parent theorem:** a finite source-faithful pure-NNI history to the
   stated parent topology;
2. **strict rank:** a fully defined well-founded rank on complete obligations,
   checked on the displayed two-state cycle;
3. **target-side cellwise theorem:** literal gluing from crosscut to the parent
   pairing;
4. **ambient terminal theorem:** the cycle forces one named route/cut/bounded
   result.

The repair may not use:

- a new `2--0` cancellation;
- a lower-order call;
- `Q_N`, `M_N`, `d_N`, nested bubbles or terminal frames;
- arbitrary root/Kempe connectivity;
- the statement that target-boundary preservation is automatic;
- RL/PDL authorial status as evidence.

---

## 6. Terminal audit checklist

For each terminal, record:

- the exact current graph;
- whether a root flow is supplied or chosen by lower ordinary existence;
- strict order decrease if induction is used;
- the labelled boundary and global support permutation used for gluing;
- the identity map back to the stored pure-NNI prefix.

Special attention:

- a descendant `K_i` state is not automatically an original-profile state;
- disconnected cancellation is a parent cut/bounded result, not a child;
- same-matching direct closure is zero-bridge first, then crossed to theta;
- an explicit theta flow is permissible only as an ordinary existential terminal,
  not as a witnessed recolouring of an inherited flow;
- no generic `separator` flag may replace a 2/3/4-cut consumer.

---

## 7. Verdict format

Return exactly one:

- `PASS-V7.2-PARTIAL`: all reconstructed units verified, blocker correctly
  isolated;
- `REPAIR-VERIFIED`: one accepted repair closes the blocker and the conditional
  induction genuinely becomes complete;
- `BLOCKED-PROOF`: smallest additional defect with an explicit witness;
- `COUNTEREXAMPLE`: an actual graph/source counterexample to a stated theorem.

Until `REPAIR-VERIFIED`, no complete cubic theorem, five-support theorem or
5-CDC theorem is established by this branch.
