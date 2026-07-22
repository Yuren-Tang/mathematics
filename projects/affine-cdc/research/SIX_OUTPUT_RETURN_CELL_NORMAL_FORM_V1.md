# Six-output return cells and the unique Petersen five-cycle core

## Research dossier v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `5cdea584584573e36e60ef2916e1ca11512df7df`  
**Parents:**

- `projects/affine-cdc/research/NONCROSSING_SIDE_SIGNATURE_WINDOW_V1.md`;
- `projects/affine-cdc/research/PETERSEN_PIVOT_RESOLUTION_V1.md`;
- `projects/affine-cdc/research/PETERSEN_BACKTRACK_TYPE_T_REDUCTION_V1.md`;
- `projects/affine-cdc/research/PETERSEN_CYCLE_MONODROMY_V1.md`;
- `projects/affine-cdc/research/PETERSEN_RESOLUTION_PARITY_V1.md`.

**Status:** exact coefficient-side normal form for every bounded six-output return cell: after formal Type-T reduction, the only cyclic core is one Petersen five-cycle with odd/type-`41` DDD holonomy. Graph-side transfer and affine calibration remain open.  
**Not implied:** canonical acceptance, independent audit, Lean verification, source-graph contraction, manuscript readiness, or the global five-support theorem.

---

## 1. Return-cell state walk

Let `W` be a same-outside-component return window supplied by the bounded noncrossing side-signature theorem inside a four-port co-root strip.

Write its Petersen-edge state walk as

\[
F_0,F_1,\ldots,F_m.
\]

Each transition

\[
F_{t-1}\longrightarrow F_t
\qquad(1\le t\le m)
\]

emits one side root. Therefore `m` is exactly the number of side outputs in the window.

The four-port return-window theorem gives

\[
\boxed{m\le6.}
\]

For every transition define its pivot

\[
s_t=F_{t-1}\cap F_t\in V(P),
\]

where `P` is the Petersen graph.

Thus the window has a pivot word

\[
s_1,s_2,\ldots,s_m.
\]

---

## 2. Pivot-change count

Partition the pivot word into maximal constant runs. Collapse each run to one pivot vertex and retain one Petersen edge at each change of pivot.

If there are `r` maximal constant runs, the linear pivot skeleton has

\[
k=r-1
\]

Petersen edges. Since every run contains at least one pivot occurrence,

\[
r\le m,
\]

and hence

### Lemma 2.1 — five-change ceiling

\[
\boxed{k\le m-1\le5.}
\]

Formal Type-T cancellation removes immediate Petersen backtracks and never increases the number of skeleton edges. Therefore the reduced pivot skeleton of `W` has length at most five.

---

## 3. Petersen girth localisation

The Petersen graph has girth five.

### Theorem 3.1 — open-path or five-cycle dichotomy

After formal Type-T backtrack cancellation, exactly one of the following holds.

1. **Empty core:** the reduced pivot skeleton has no edge.
2. **Open core:** it is a simple open Petersen path of length at most five.
3. **Cyclic core:** it is exactly one simple Petersen five-cycle.

No other reduced core occurs.

### Proof

The reduced skeleton has at most five edges by Lemma 2.1.

If it has no repeated pivot, it is a simple open path, or empty.

Suppose a pivot repeats. Choose two equal occurrences at minimum positive distance. The intervening subpath is closed and has no repeated internal pivot. Since the reduced path has no immediate backtrack, this subpath is a simple cycle. Petersen girth gives length at least five, while the whole reduced skeleton has length at most five. Therefore the subpath has length exactly five and consumes the complete reduced skeleton. It is one Petersen five-cycle. ∎

### Corollary 3.2 — exclusion of the larger simple cores

A six-output return cell cannot contain a reduced Petersen cycle of length six, eight, or nine.

Thus the even identity-monodromy simple-cycle cores do not occur inside the bounded return cell. The only cyclic coefficient core is the odd five-cycle.

---

## 4. Complete coefficient normal form

Restore the formally cancelled backtracks and the collapsed constant-pivot runs.

### Theorem 4.1 — six-output return-cell normal form

Every noncrossing same-component return cell with at most six side outputs factors coefficientwise into

\[
\boxed{
\text{rank-two constant-pivot runs}
+
\text{Type-T `abba` backtrack units}
+
\mathcal C,
}
\]

where the reduced core `C` is exactly one of:

- empty;
- a simple open Petersen path with at most five DDD switch states;
- one simple Petersen five-cycle.

There is no fourth coefficient mechanism.

### Proof

The pivot-resolution theorem gives the canonical factorisation into constant-pivot rank-two runs and DDD pivot changes. The backtrack theorem identifies every immediate inverse pair with an exact Type-T `abba` word and supplies the unique reduced path. Theorem 3.1 classifies that reduced path under the six-output bound. ∎

---

## 5. The cyclic core is the universal odd DDD core

Let `C_5` be the five-cycle case.

The Petersen cycle-monodromy theorem gives

\[
\Pi(C_5)\text{ of cycle type }41.
\]

It lies in the stabiliser of one canonically determined DDD/Petersen-edge state

\[
F_{C_5},
\qquad
\operatorname{Stab}_{S_5}(F_{C_5})\cong D_8,
\]

and acts as an order-four rotation.

The resolution-parity theorem gives

\[
\operatorname{Hol}_{\mathrm{res}}(C_5)=1\in\mathbf F_2,
\]

so the support monodromy exchanges the two crossed root resolutions of `F_(C_5)`.

### Theorem 5.1 — unique cyclic calibration target

Every cyclic obstruction inside a bounded six-output return cell is `S_5`-equivalent to one Petersen five-cycle and carries:

1. type-`41` support monodromy;
2. one canonical invariant DDD state;
3. nontrivial resolution-sheet parity.

Therefore one physical affine five-cycle calibration suffices for every cyclic six-output return cell.

### Trust boundary

This determines the linear support action and the resolution-sheet exchange. It does not yet identify the full side-root affine cocycle with the nonzero class in

\[
H^1(D_8,E_5)\cong\mathbf F_2.
\]

---

## 6. The acyclic core is a finite transfer object

In the open-core case, the reduced pivot skeleton has at most five edges and at most six pivot runs.

Every run is confined to one rank-two/Tait plane, and every edge between runs is one DDD atom with its two opposite forced resolutions.

Hence the complete coefficient transfer data of the acyclic core consist of:

- at most six rank-two run labels;
- at most five DDD switch states;
- at most six actual side-root outputs;
- the two longitudinal endpoint states;
- one returning outside component at the endpoint outputs;
- at most four interior singleton outside components, each port-bearing.

This is a bounded transfer object. It may still have arbitrarily large internal graph pieces inside the named outside components, but it has no unbounded coefficient word, no unbounded pivot skeleton, and no intrinsic closed holonomy.

---

## 7. Sharpened composition programme

The earlier six-output transfer lemma now splits into only two genuinely different tasks.

### Target 7.1 — acyclic return-cell transfer

For the bounded open-path core, prove one of:

1. serial contraction of the rank-two runs and Type-T units;
2. a smaller cyclic separator/four-pole determined by the returning component;
3. root-admissible profile escape through one port-bearing singleton component;
4. localisation of an empty fibre, empty vertex relation, zero edge, or DDD atom.

There is no holonomy obstruction beyond the finite endpoint transfer table.

### Target 7.2 — one five-cycle affine calibration

For one explicit Petersen five-cycle, compute the full physical side-root/full-frame affine cocycle and prove one of:

1. it is the nontrivial physical `D8` class;
2. one crossed DDD resolution gives a bounded route escape;
3. the five-cycle and its returning component form a bounded separator/defect unit.

Because all Petersen five-cycles form one `S5` orbit, no second odd cyclic calibration is required.

---

## 8. Strategic consequence

The composition frontier no longer contains an arbitrary enriched transducer or four different simple-cycle lengths.

Inside the first unavoidable noncrossing return cell:

\[
\boxed{
\text{unbounded side word}
\Longrightarrow
\text{at most six outputs}
\Longrightarrow
\begin{cases}
\text{bounded acyclic transfer path},\\
\text{one universal odd DDD five-cycle}.
\end{cases}
}
\]

The even six- and eight-cycle flat calibrations remain relevant to larger regional identity-return problems, but they are not needed to classify the minimal six-output return cell.

---

## 9. Trust boundary

### Exact here

- the equality between output count and transport-turn count in a linear co-root strip;
- the bound of at most five pivot changes in a six-output return cell;
- the open-path/five-cycle dichotomy from Petersen girth;
- exclusion of six-, eight-, and nine-cycle cores from the bounded return cell;
- the complete coefficient normal form;
- reduction of all cyclic return cells to one `S5` orbit of five-cycles;
- the finite size of the acyclic coefficient transfer object.

### Still open

- source-incidence-preserving Type-T contraction;
- transfer through the returning outside component;
- extraction of a composition-safe separator;
- full affine calibration of the Petersen five-cycle;
- equality with the nontrivial physical `D8` cohomology class;
- strict local descent, horizontal induction, and the global five-support theorem.
