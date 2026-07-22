# Global co-root Ptolemy tracks are forced Petersen backbones and admit no fixed-order sink

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `f8b51c96d58b74a4f22df788ca9b7b7bbfe51a95`.

**Parents:**

- `PTOLEMY_CONTEXTUAL_COHERENCE_SCOPE_CORRECTION_V1.md`;
- `PACHNER_FIRST_FAILURE_CRITICAL_OVERLAP_V1.md`;
- `FIVE_LEAF_PACHNER_PENTAGON_ROOT_INTERVAL_V1.md`;
- `FORCED_DDD_BACKBONE_BINARY_TRANSPORT_V1.md`;
- `PETERSEN_RESOLUTION_PARITY_V1.md`;
- `PETERSEN_SIMPLE_CYCLE_OUTPUT_CLASSIFICATION_V1.md`;
- `EQUALITY_LOCK_GLOBAL_PACHNER_POTENTIAL_V1.md`;
- `DDD_LOCK_GLOBAL_PACHNER_POTENTIAL_V1.md`;
- `CONTEXTUAL_TRANSFER_TARGET_ORDER_CORRECTION_V1.md`.

**Status:** exact multi-cell track identification and fixed-order sink elimination. In a same-order contextual-transfer block, a zero first failure from an inverse flip is immediately replaced by its alternative root topology, while equality/doubled-disjoint failures arise only at an inverse cancellation and therefore leave the pure flip block. Hence every persistent same-order token is co-root/DDD. Its two crossed root resolutions form one Petersen edge. Every nontrivial adjacent relocation shares one resolution root with the next atom, giving a Petersen pivot walk; under continued fixed-route failure, the six-port pairing is necessarily the forced-backbone pairing. After cancelling history backtracks, an infinite or recurrent token path contains one simple Petersen cycle. Odd cycles contradict oriented resolution return. Even cycles are equality identity hexagons or DDD octagons; in a hypothetical finite sink component, the corresponding full-ten-triangle potential supplies a same-boundary strictly lowering root move, contradicting sink minimality. Therefore no same-order contextual sink exists. Combined with strict target-order descent behind cancellations, contextual inverse transfer is well founded.

**Not implied:** final global five-support theorem before reverse dependency audit of all separator/gluing hypotheses, canonical acceptance, independent audit, Lean verification, manuscript integration, release, publication, or DOI status.

---

## 1. Contextual state graph at fixed target order

Fix:

- a cap-target vertex order `N`;
- an ordered outer four-port incidence set;
- the fixed-route cap orientation;
- the connected bridgeless cubic category, with separator and bounded-degeneration exits retained.

A **same-order contextual state** consists of:

1. one cap-context graph of order `N` obtained by root Pachner modifications of the complementary four-pole;
2. either a root-valued `E_5` flow or one normalized first-failure flow with exactly one zero/co-root edge;
3. the active local inverse-transfer position;
4. its ordered four-root boundary and resolution sheet;
5. the outer cap route.

Allowed transitions at fixed order are:

- successful inverse root flips;
- root-valued alternative NNI resolutions;
- horizontal Kempe rescue;
- root Pachner moves selected by the equality/DDD current-flow descent;
- one-atom relocation and immediate two-defect normalization;
- disjoint square and pentagon scheduling relations.

A transition leaves the fixed-order graph when it produces:

- an equal-face cancellation;
- a smaller cap-context target;
- route/profile escape;
- separator/category exit;
- bounded direct-pairing completion.

Because there are finitely many cubic combinatorial types, root assignments, marked local positions, and one-atom labels at order `N`, the same-order contextual state graph is finite.

---

## 2. Zero atoms do not persist at fixed order

Suppose a first failed inverse move in a pure `2--2` Pachner block has central value zero.

The equality recursion theorem gives the exact boundary form

\[
a,a,b,b
\]

with `a,b` distinct intersecting roots. Both crossed pairings have the root central value

\[
a+b.
\]

### Theorem 2.1 — immediate zero removal

Every zero atom arising inside a same-order flip block admits an immediate root-valued alternative topology. Hence it can be replaced by a root state without:

- changing target order;
- creating another atom;
- changing the outer terminal word.

The only singular zero branch, quadruple equality, occurs when reversing a `2--0` cancellation and therefore lies outside the pure same-order block.

### Corollary 2.2

A persistent atom path in the same-order contextual state graph is necessarily co-root/DDD.

The doubled-disjoint branch also arises at inverse cancellation and is treated by the Type-T/DDD cancellation exit, not by a same-order Ptolemy track.

---

## 3. Canonical DDD state of one co-root atom

Let a co-root atom have central value

\[
Q_i.
\]

Its ordered four-root boundary has exactly two root-valued crossed resolutions. Let their central root values be

\[
s,t\in R_5.
\]

Then:

\[
\boxed{s\perp t,}
\qquad
\boxed{s+t=Q_i.}
\]

### Definition 3.1 — atom state

Associate to the atom the Petersen edge

\[
\boxed{F(A)=\{s,t\}\in E(KG(5,2)).}
\]

The two roots `s,t` are the two resolution sheets of the atom. The third local topology is the co-root topology.

This construction depends only on the ordered four-root boundary and not on a chosen root resolution.

---

## 4. One bad overlap gives adjacent Petersen states

Let a co-root atom `A` interact with one adjacent root Pachner move. In the only nontrivial bad-overlap case, write the old defect as

\[
Q_i
\]

and the newly created adjacent defect as

\[
Q_j.
\]

The critical-overlap theorem gives the transport vertex

\[
(Q_i,Q_j,ij).
\]

Let the old atom resolutions be

\[
F(A)=\{s,t\}.
\]

At the overlap, exactly one of these two root resolutions is retained by the new four-root boundary; call it `t`. The other new crossed resolution is one root `u` disjoint from `t`. Therefore

\[
\boxed{F(A')=\{t,u\}.}
\]

### Theorem 4.1 — atom-track/Petersen-step dictionary

Every nontrivial same-order relocation of a co-root atom gives two adjacent DDD states

\[
\boxed{
F(A)=\{s,t\}
\longrightarrow
F(A')=\{t,u\}.}
\]

Equivalently it records one pivot turn

\[
s\longrightarrow t\longrightarrow u
\]

in the Petersen graph.

### Proof

The two atom states are the two one-factor decompositions of consecutive four-root trialities. The unchanged root topology on the common side of the critical pentagon supplies the shared root resolution `t`. Both pairs are disjoint-root pairs, hence Petersen edges. ∎

---

## 5. Why a trapped track is the forced-backbone branch

At one pivot-change neighbourhood, the six external root branches have the form

\[
(s,x,z\mid w,t,y)
\]

of the six-port star theorem. Four cross matchings admit root-valued star completions. The remaining two contain the forced pair `s-t` and are exactly the crossed route sheets

\[
X_F,
\qquad
Y_F
\]

of the central DDD state.

If a non-forced star matching is physically available, then one obtains:

- a root-compatible commutation of the atom past the move;
- or a change of the fixed cap route;
- or a separator/category exit.

All are exits from a hypothetical trapped same-order component.

### Theorem 5.1 — trapped implies forced

Inside a same-order contextual component with no route, category, or transfer exit, every pivot-change cell of a persistent co-root track lies in the forced-backbone branch.

Therefore the crossed-route sheet transports canonically from one atom state to the next, with one initial binary choice and no independent cell bits.

---

## 6. The global atom track is one Petersen pivot walk

Let

\[
A_1,A_2,\ldots
\]

be consecutive persistent co-root states along a same-order schedule. By Theorem 4.1 write

\[
F(A_k)=\{s_{k-1},s_k\}.
\]

Then

\[
\boxed{
s_0,F(A_1),s_1,F(A_2),s_2,\ldots
}
\]

is one walk in the Petersen graph.

### Constant cells

A repeated atom state or a sequence with no pivot change contributes no new sheet datum and contracts to one constant-pivot run.

### Immediate backtrack

If

\[
s_{k-1}=s_{k+1},
\]

the two turns form

\[
s_{k-1}\to s_k\to s_{k-1}.
\]

At the history level, the two critical relocations undo each other after immediate atom normalization. Their resolution flips occur twice and cancel. Thus the backtrack deletes from a length-minimal schedule.

This is the scheduling counterpart of the coefficient Type-T `abba` unit and does not require contracting an embedded source subgraph.

### Theorem 6.1 — reduced track

After deleting constant runs and immediate backtracks, every persistent same-order atom track is represented by a reduced Petersen path with one globally transported crossed-route sheet.

---

## 7. Repetition produces one simple Petersen cycle

The Petersen graph has ten vertices. Hence a reduced open path with more than nine edges repeats one pivot. A shortest repeated-pivot subpath is a simple Petersen cycle.

The complete simple-cycle list is

\[
\boxed{C_5,C_6,C_8,C_9.}
\]

The forced-backbone orientation theorem gives trivial crossed-route return in one oriented inverse-dipole lock.

The resolution-parity theorem gives return parity equal to cycle length modulo two.

### Theorem 7.1 — odd cycles are impossible

The simple cycles `C5` and `C9` exchange the resolution sheet. They cannot be closed subtracks of an oriented fixed-route contextual component.

Thus every recurrent trapped track contains an even simple cycle `C6` or `C8`.

---

## 8. Even cycles carry fixed equality/DDD boundaries

The simple-cycle classification identifies the even cores exactly.

### Six-cycle

A simple `C6` is the identity hexagon of one active root `r`. Its four-port boundary is the equality boundary

\[
\boxed{r,r,r,r}
\]

with double-equal oriented response. The complete carrier lies in the domain of the equality global Pachner potential

\[
\mathcal P_{\mathrm{eq}}=(E,\Phi,|V|).
\]

### Eight-cycle

A simple `C8` is canonically attached to one DDD state

\[
F=\{p,q\},
\qquad p\perp q.
\]

Its four-port boundary is

\[
\boxed{p,p,q,q}
\]

with the fixed crossed DDD route. The complete carrier lies in the domain of the DDD global potential

\[
\mathcal P_{\mathrm{DDD}}=(\Omega,|V|).
\]

In both cases, internal root Pachner moves preserve the relevant ordered boundary root word.

---

## 9. Sink-SCC elimination

Assume, for contradiction, that contextual transfer at one fixed target order has a nonempty set of states from which no exit is reachable.

In the finite directed state graph choose a sink strongly connected component

\[
\mathscr K.
\]

It has no transition to:

- complete transfer;
- route/profile escape;
- separator/category exit;
- bounded terminal;
- lower target order.

By Theorem 2.1 every atom state in `K` has an outgoing resolution to a root-valued state. Hence `K` contains root states.

If no persistent atom track repeats a pivot, every track has length at most nine and must terminate at a root state or an exit. Since `K` is recurrent, it therefore contains an even simple-cycle carrier.

### Case 9.1 — equality `C6`

Consider all root states of `K` carrying the fixed equality boundary `r^4` of this cycle. Choose one minimizing

\[
\mathcal P_{\mathrm{eq}}.
\]

The full-ten-triangle equality descent theorem supplies either:

1. a strictly potential-lowering root Pachner flip;
2. an equal-face cancellation;
3. route/category/terminal exit.

Options 2--3 leave `K`, impossible for a sink with no exits. Option 1 preserves the equality boundary and gives another root state reachable from the chosen state. Sinkness puts it in `K`, contradicting minimality of the potential.

### Case 9.2 — DDD `C8`

Choose, among states of `K` carrying its fixed DDD boundary `p,p,q,q`, one minimizing

\[
\mathcal P_{\mathrm{DDD}}.
\]

The DDD full-ten-triangle descent gives the identical contradiction.

### Theorem 9.1 — no fixed-order sink

The same-order contextual state graph has no nonterminal sink strongly connected component.

---

## 10. Fixed-order reachability

Let `S` be any same-order contextual state arising during inverse transfer. Consider its finite reachable subgraph.

If no exit were reachable, that finite graph would contain a sink SCC with no exit, contradicting Theorem 9.1.

### Corollary 10.1 — same-order contextual progress

From every same-order state, some finite sequence of allowed contextual moves reaches one of:

1. complete root transfer;
2. route-changing cap escape;
3. separator/category exit;
4. bounded direct-pairing completion;
5. an inverse cancellation and hence the strict-order layer.

No confluence or unique scheduling choice is required; existence of one progress path is sufficient.

---

## 11. Full well-founded contextual transfer

The target-order correction gives:

- pure Pachner prefixes stay in the fixed-order layer and are handled by Corollary 10.1;
- crossing an equal-face cancellation lowers the cap-context target order by two before any recursive return behind that cancellation;
- target order is a nonnegative integer.

Induct on cap-target order. At each fixed order use Corollary 10.1. If the process reaches the strict-order layer, apply the induction hypothesis. Every other branch exits constructively through transfer, cap lift, separator, or bounded completion.

### Theorem 11.1 — contextual inverse-transfer theorem

Every cap-compatible terminal root state of an equality or oriented DDD root-surgery descent can be transferred to the original cap context, unless the original graph is already discharged by:

\[
\boxed{
\text{route/profile cap lift},
\quad
\text{separator/category reduction},
\quad
\text{bounded direct-pairing completion}.}
\]

Nested contextual transfer is well founded.

This supplies the global defect-track theorem missing from the local Ptolemy relation analysis.

---

## 12. Interaction with the Ptolemy scope correction

The Ptolemy groupoid remains useful to show that arbitrary same-order history ambiguity is generated by local flip relations. The scope correction observed that a defect track may cross many cells.

The present theorem fills exactly that gap:

- multi-cell co-root tracks are forced Petersen backbones;
- odd cycle holonomy is forbidden;
- even cycle recurrence contradicts the already established source-level potentials in a finite sink SCC.

Therefore the conditional conclusions of Sections 8--10 of `ROOT_FLOW_PTOLEMY_CONTEXTUAL_COHERENCE_V1.md` become valid when read through Theorem 11.1 rather than through the quarantined local-`C5/C6` shortcut.

---

## 13. Consequence for the project frontier

The following local/compositional obligations are now theorem-level closed:

1. equality and DDD current-flow termination;
2. first-failure localisation to one atom;
3. corrected strict-order bookkeeping;
4. same-order zero elimination;
5. multi-cell co-root track/backbone identification;
6. odd-cycle orientation exclusion;
7. even-cycle sink elimination by equality/DDD potentials;
8. contextual terminal-to-source inverse transfer.

The next task is a reverse global proof-DAG audit from the minimal-counterexample statement, checking:

- every two-/three-/four-cut exit invokes a proved gluing theorem;
- every category-safe replacement is used in the correct direction;
- no local theorem assumes the global conclusion;
- the initial three-reconnection reduction reaches exactly the equality/DDD frontier consumed here;
- all trust-boundary corrections are reflected in the final ordering.

No global five-support theorem is claimed before that audit.

---

## 14. Trust boundary

### Exact here

- same-order persistence only for co-root atoms;
- canonical DDD/Petersen-edge state of one atom;
- adjacent-atom/shared-resolution dictionary;
- forced-backbone hypothesis in a no-exit component;
- reduction of a global track to one Petersen pivot walk;
- backtrack cancellation at the history level;
- simple-cycle recurrence;
- odd-cycle exclusion by oriented resolution parity;
- equality/DDD boundary identification of even cycles;
- finite sink-SCC contradiction using the full-ten-triangle potentials;
- same-order reachability of a progress exit;
- induction with strict order descent behind cancellations;
- complete contextual inverse-transfer theorem.

### Still open

- reverse global dependency audit;
- final minimal-counterexample closure theorem and well-founded packaging;
- independent mathematical audit;
- canonical acceptance, Lean verification, manuscript integration, release, publication;
- the global five-support theorem.
