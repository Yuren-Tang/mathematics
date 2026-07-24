# Questions for external reviewers

## 1. Inherited physical-chain fidelity

Let

$$
X_0,X_1,\ldots,X_\ell
$$

be the selected shortest path in the channel quotient, with each quotient edge represented by one fixed physical non-channel edge.

After the root NNI contracting $X_0X_1$:

- do the exact representatives of $X_1X_2,\ldots,X_{\ell-1}X_\ell$ survive;
- are their endpoints still in the claimed successor components;
- can a local reconnection merge, split or reroute a later component so that the retained path no longer exists;
- does the proof use inheritance of one path or silently recompute a new shortest path?

A counterexample here would materially defeat the current rank.

## 2. Active/active local transition and final matching

For every pair of active endpoint triangles joined by a non-channel edge:

- enumerate the legal NNI pairings;
- identify which pairing is root-valued;
- verify its effect on the two local $H_h$ passages;
- treat equal endpoint triangles without using the zero branch;
- prove that the last connector between two terminal paths changes their perfect matching.

Is there a source configuration in which the root-valued alternative preserves the terminal matching or fails to merge the intended components?

## 3. Co-root marked-arc totality

The same-arc Heawood witness refutes selection of an arbitrary equal face. Does the full physical quotient construction always provide a finite connector path between the two marked arcs in every category-safe co-root lock?

Check especially:

- whether cutting the marked edges can create a disconnected carrier not covered by a named terminal;
- whether inactive vertices or closed channel cycles can shield the arcs;
- whether the final connector can lie at or cross the active parent cell or cap;
- whether the route/cap consumer after matching change is literally applicable.

## 4. Zero-parent terminal-path return

In the `(13,13,23,23)` row:

- is the carrier after deleting the active cell connected under exactly the stated category hypotheses;
- does the chain always reach a crossed outside matching;
- can the crossed-sheet alignment be achieved by zero or one legal root branch swap;
- is the selected `H_35` support component closed and switchable;
- does the resulting word always admit the literal parent NNI with root `35`;
- are all exterior darts, support names, cap and stored-prefix maps unchanged?

A smallest exceptional four-port carrier is particularly valuable.

## 5. End-to-end integration and assurance

Assuming the standalone chain theorem, does the entire ordinary-induction candidate follow without another gap?

Audit:

- exact output type of every chain/category branch;
- exhaustive terminal consumption;
- target-topology normalization after the one pop;
- active-central-mark lineage in seam/run return;
- no reset between component-chain length, target distance and stored prefix;
- one and only one lower-order call;
- compatibility with the independently accepted general outer shell.

State separately:

1. the standalone chain verdict;
2. each co-root/zero corollary verdict;
3. the full integration verdict.

## Desired response format

For each question return one of:

- `VERIFIED IN EXACT SCOPE`;
- `VERIFIED SUBJECT TO NAMED LOCAL REPAIR`;
- `MATERIAL GAP`;
- `COUNTEREXAMPLE`;
- `DEPENDENCY NOT ASSURED`.

Name the smallest configuration, exact source lines/files, and any finite certificate required.