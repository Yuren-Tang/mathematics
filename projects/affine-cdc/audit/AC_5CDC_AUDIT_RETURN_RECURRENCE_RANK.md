# AC-5CDC-AUDIT-RETURN-01 — recurrence and rank audit

## 1. Claimed architecture

The candidate proposes the following chain.

1. Every failed ordinary parent edge `T -> p(T)` retains that literal target
   boundary while its zero/co-root discrepancy is normalized.
2. Fixed-order closed, open and periodic singular tracks are replaced without
   changing that boundary.
3. A finite resolved parent relation `M_N` is formed after lower-order calls are
   expanded and returned.
4. Every terminal-free sink SCC is expanded, compressed to fixed order, and
   converted obligation by obligation into strict `d_top` descent.
5. Terminal reachability then permits
   `d_N(x)=dist_{M_N}(x,X_N)` and lexicographic induction on `(N,d_N)`.

Items 1--2 are plausible only with the marked-seam repair recorded in the seam
ledger.  Items 3--4 are not proved by the current text.

## 2. Fixed-order target-parent theorem

`AC_PD_5CDC_R2_7_RESOLVED_CALL_CONTEXTUAL_TRANSFER.md`, Theorem 5.1,
minimizes `(U,C,S)` among comparisons with the same complete target-parent outer
boundary.  Subject to G-MARK-1, the component-removal argument does support the
following **relative** statement:

> Given an already constructed fixed-order comparison whose two ordinary sides
> are the selected obligation `T -> p(T)`, singularity removal does not replace
> `p(T)` by an arbitrary root topology.

The candidate must not strengthen this into either of the following without an
additional construction:

- every coefficient-equivalent root loop has endpoint `p(T)`;
- every arbitrary complete state automatically carries a fixed-order comparison
  to its selected parent.

The report therefore accepts Theorem 5.1 only as a relative normalization lemma,
not as a total scheduler theorem.

## 3. Definition and saturation of `M_N`

Section 6 says that `M_N` is “saturated” under every displayed
boundary-equivalent macro.  This does not specify a finite transition schema or
prove the following required closure properties.

1. **Totality on reachable nonterminals.**  A singleton nonterminal SCC with no
   outgoing edge is a sink SCC but has no positive directed cycle.  The proof
   begins by choosing a cycle and therefore silently assumes totality.
2. **Active-obligation coordinate.**  Every parent state must record either no
   active obligation or one exact ordered pair `(T,p(T))` and a phase.
3. **Detour invariance.**  Every direct normalization and every resolved-call
   macro internal to an obligation must preserve that exact coordinate.
4. **Success rule.**  The only macro allowed to change the active ordinary
   topology must end on `p(T)` and then initialize the next obligation.
5. **No reset.**  No direct normalization, returned call, endpoint collar or
   reinitialization may restore a topology of equal or larger `d_top` without
   first leaving through a terminal.
6. **Compositional saturation.**  If an expanded cycle is compressed or one
   obligation segment is replaced, the new endpoint must still be the literal
   initial state of the next segment.

Finiteness of the state set does not imply any of these properties.

## 4. Target-parent segmentation gap

Theorem 6.1 expands a cycle of resolved macros, eliminates innermost calls, and
then says to apply Theorem 5.1 to every target-parent obligation.  The missing
step is a segmentation/re-splicing theorem.

Suppose a compressed cycle is written as consecutive witnessed segments

`D_1 * D_2 * ... * D_k`,

where `D_i` is annotated by `T_i -> p(T_i)`.  Replacing `D_i` by a new relative
history ending at `p(T_i)` changes its terminal complete state.  To concatenate
with `D_{i+1}`, one must prove that the initial complete state of `D_{i+1}` is
literally that same `p(T_i)` state, with identical darts, marks, cap, route,
support data and active-obligation phase.  The current genealogy theorems prove
identity gluing inside an innermost bubble; they do not prove this global
obligation-by-obligation re-splicing after a parent success.

The sentence “because `K` is sink and contains no terminal, only parent successes
are possible” excludes exits, but it does not exclude topology-restoring direct
or resolved macros.  Sinkness says endpoints remain in `K`; it does not impose
monotonicity of `d_top` on all edges of `K`.

## 5. Small finite countermodel to the stated no-sink inference

This is a countermodel to the **argument schema**, not a counterexample to the
5-CDC theorem.

Let the ordinary target tree have distances

- `d_top(T_2)=2`,
- `d_top(T_1)=1`,
- `d_top(T_0)=0`, with `T_0` terminal.

Let the resolved parent relation have complete nonterminal states `x` on `T_2`
and `y` on `T_1`, and edges

- `x -> y`, a successful realization of `T_2 -> T_1`;
- `y -> x`, a finite returned normalization/reset macro.

Then `{x,y}` is a terminal-free sink SCC.  The first edge is strict parent-tree
progress, but the second restores the lost distance.  Every edge may have a
finite source witness; finiteness and expansion/compression alone do not rule it
out.  To exclude this model one needs precisely the missing no-reset and
segmentation invariants above.

An even smaller failure mode is one reachable nonterminal vertex with no
outgoing macro.  It is a sink SCC, but the proof's instruction to choose a cycle
cannot begin.

## 6. Why `d_N` is not yet available

Directed distance to a terminal is a valid rank only after terminal reachability
has been proved.  The finite-graph implication

> every reachable sink SCC contains a terminal => every reachable state reaches a terminal

is correct.  The defect lies earlier: Theorem 6.1 does not establish its premise.
Consequently Section 7's definition of `d_N` is presently circular as a proof of
termination: the needed reachability is exactly what the unresolved no-sink
step was meant to prove.

The original-prefix coordinate itself is sound.  It is lowered before each
predecessor-order normalization and the inner strategy does not explicitly
restore it.  But that outer induction cannot compensate for the missing
within-level rank.

## 7. Required repair theorem

A sufficient repair would be a new source-level theorem of the following form.

### Obligation-stratified resolved relation theorem

For each fixed order `N`, define a finite reachable state set with an explicit
phase and active-obligation coordinate.  Prove:

1. every reachable nonterminal state has at least one chosen outgoing macro;
2. every internal fixed-order or resolved-call detour preserves the exact active
   obligation and its two complete labelled collars;
3. innermost-call compression preserves the ordered segmentation into active
   obligations;
4. a completed obligation changes the ordinary topology exactly from `T` to
   `p(T)` and initializes no state with larger `d_top`;
5. every other macro is a declared terminal;
6. restored child separators have a proved parent disposition.

Then any terminal-free SCC contains a success edge and every success strictly
lowers `d_top`, while all other edges preserve it.  A directed cycle is
impossible.  Only after this theorem may `d_N` be defined.

This is not an editorial amendment.  It is a new global compatibility and
well-foundedness lemma connecting the already proved local source movies.

## 8. Audit disposition for J

- target-parent annotation: present;
- relative fixed-order component removal: conditionally credible;
- saturation/totality: not proved;
- cycle expansion: finite;
- preservation of obligation segmentation under compression: not proved;
- obligation-by-obligation re-splicing: not proved;
- no-reset monotonicity: not proved;
- no-terminal-sink: not established;
- `d_N`: unavailable;
- `(N,d_N)` induction: blocked.

**Classification: `BLOCKED-PROOF`.**
