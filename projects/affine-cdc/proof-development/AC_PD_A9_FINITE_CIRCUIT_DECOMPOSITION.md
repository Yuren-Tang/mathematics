# AC-PD-A9 — finite circuit decomposition and multiplicity preservation

**Proof-development state:** `COMPLETE-DRAFT`  
**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Initial baseline:** `main@960c92b7ff231c78b387894149779083060a75eb`  
**Depends on:** `AC-PD-A0`, `AC-PD-A8`  
**Immediate consumer:** `AC-PD-A10`  
**External mathematical inputs:** none

## 0. Main output

Every finite cut-even support in a multigraph is a disjoint union of finitely many circuits. Applying this memberwise to a finite indexed cut-even double cover and concatenating all circuit occurrences produces a cycle double cover with the same edge multiplicities.

The decomposition theorem itself permits loops and parallel edges. In the complete AffineCDC spine it is applied once to the loopless original core after collapse; loops are later restored by A1.

## 1. Parity under symmetric difference

For finite supports `A,B\subseteq E(G)`, let

\[
A\triangle B
:=(A\setminus B)\cup(B\setminus A).
\]

### Lemma 1.1 — boundary additivity

The intrinsic mod-two boundary satisfies

\[
\partial_G(A\triangle B)
=
\partial_GA\triangle\partial_GB.
\]

Equivalently, for every vertex,

\[
\deg^{\mathrm{half}}_{A\triangle B}(v)
\equiv
\deg^{\mathrm{half}}_A(v)+
\deg^{\mathrm{half}}_B(v)
\pmod2.
\]

#### Proof

Each edge occurrence belonging to both supports is counted twice and cancels modulo two; occurrences belonging to exactly one support remain. This holds for nonloop endpoint occurrences and for the two endpoint occurrences of a loop. ∎

### Corollary 1.2 — cut-even supports form a binary vector space

If `A` and `B` are cut-even, then `A\triangle B` is cut-even.

#### Proof

A0 identifies cut-evenness with empty intrinsic boundary. Apply Lemma 1.1. ∎

If `B\subseteq A`, then

\[
A\triangle B=A\setminus B.
\]

Thus removing a cut-even sub-support from a cut-even support preserves cut-evenness.

## 2. Existence of a circuit inside a nonempty support

A0 proves that every nonempty finite boundary-even support contains a polygonal cycle support and that polygonal cycle supports are exactly circuits. Therefore:

### Lemma 2.1 — circuit sub-support

If `F` is nonempty, finite, and cut-even, then there exists a circuit `C` with

\[
C\subseteq F.
\]

The circuit may be:

- a singleton loop;
- a two-edge parallel digon;
- an ordinary simple cycle.

No connectedness hypothesis on `F` or `G` is required.

## 3. Terminating decomposition

### Theorem 3.1 — finite circuit decomposition

Let `F\subseteq E(G)` be finite and cut-even. Then there exists a finite indexed family of circuits

\[
(C_j)_{j\in J}
\]

such that:

1. the circuit supports are pairwise edge-disjoint;
2. their union is exactly `F`;
3. for every edge `e`,
   \[
   |\{j\in J:e\in C_j\}|
   =
   \begin{cases}
   1,&e\in F,\\
   0,&e\notin F.
   \end{cases}
   \]

#### Proof

Induct on the natural number `|F|`.

If `F=\varnothing`, take the empty index set and empty family.

Suppose `F\ne\varnothing`. By Lemma 2.1 choose a circuit `C\subseteq F`. Put

\[
R:=F\setminus C.
\]

Both `F` and `C` are cut-even, so Corollary 1.2 gives that `R=F\triangle C` is cut-even. Since `C` is nonempty,

\[
|R|<|F|.
\]

Apply the induction hypothesis to `R`, obtaining pairwise edge-disjoint circuits `(C_j)_{j\in J}` whose union is `R`. Add one new index `*` with `C_*=C`. Because `R\cap C=\varnothing`, the enlarged family is pairwise edge-disjoint and has union

\[
R\cup C=F.
\]

The edgewise `0/1` count follows from disjointness and exact union. The cardinality strictly decreases at every recursive step, so termination is explicit. ∎

### Corollary 3.2 — multiset form

Every finite cut-even support is the union of a finite multiset of circuits with each edge of the support occurring in exactly one circuit occurrence.

The circuit values in the multiset need not be distinct as abstract subsets across different applications, but within one decomposition of one support they are edge-disjoint and hence distinct unless both are empty; circuits are nonempty.

## 4. Componentwise interpretation

### Proposition 4.1 — decomposition respects components

Every circuit in a decomposition lies in one edge-bearing connected component. A decomposition may be obtained by decomposing each component restriction separately and concatenating.

#### Proof

A0's circuit characterization places every circuit in one connected component. Conversely, cut-evenness restricts componentwise, so Theorem 3.1 applies independently. ∎

The induction proof itself needs no prior component split.

## 5. Memberwise decomposition of an indexed cover

Let

\[
\mathcal F=(F_i)_{i\in I}
\]

be a finite indexed family of finite cut-even supports. For each index `i`, choose a decomposition

\[
F_i=\bigsqcup_{j\in J_i}C_{i,j}
\]

as in Theorem 3.1.

Define the total circuit index set

\[
K:=\{(i,j):i\in I,\ j\in J_i\}.
\]

Since `I` and every `J_i` are finite, `K` is finite.

### Proposition 5.1 — exact local count

For every parent index `i` and edge `e`,

\[
|\{j\in J_i:e\in C_{i,j}\}|
=
\mathbf1_{e\in F_i}.
\]

This is Theorem 3.1(3).

### Theorem 5.2 — global multiplicity preservation

For every edge `e`,

\[
\boxed{
|\{(i,j)\in K:e\in C_{i,j}\}|
=
|\{i\in I:e\in F_i\}|.
}
\]

#### Proof

Partition the left-hand index set by its first coordinate. Then

\[
\begin{aligned}
|\{(i,j):e\in C_{i,j}\}|
&=
\sum_{i\in I}
|\{j\in J_i:e\in C_{i,j}\}|\\
&=
\sum_{i\in I}\mathbf1_{e\in F_i}\\
&=
|\{i\in I:e\in F_i\}|.
\end{aligned}
\]

All sums are finite. ∎

### Corollary 5.3 — even double cover to cycle double cover

If `(F_i)_{i\in I}` is an intrinsic even double cover, then the concatenated circuit family `(C_{i,j})_{(i,j)\in K}` is a cycle double cover.

#### Proof

Every member is a circuit. The parent multiplicity of every edge is two; Theorem 5.2 preserves that multiplicity exactly. ∎

## 6. Empty and repeated parent occurrences

### Empty support occurrence

If `F_i=\varnothing`, choose `J_i=\varnothing`. It contributes no circuit occurrence and changes no edge multiplicity.

Thus empty occurrences may be dropped at the decomposition stage without changing the resulting circuit family, even though retaining them earlier was important for faithful indexed transport.

### Repeated parent supports

If `F_i=F_{i'}` for distinct indices, decompose each occurrence separately. The resulting circuit occurrences are counted separately. One may reuse the same decomposition values, but occurrence multiplicity remains doubled.

### Repeated circuit values across parents

The same circuit subset may arise from different parent indices. Both occurrences remain in the final multiset, as required by exact coverage counting.

## 7. Loops and parallel edges

### Loops

If `F` contains a loop `\ell`, the singleton circuit `{\ell}` may be removed at one induction step. Intrinsic cut parity is unchanged because the singleton loop is cut-even.

### Parallel digons

Two distinct parallel edges may form a circuit and are removed together. Their edge-object identities remain distinct.

The complete theorem route applies A9 before loop reinsertion, so its actual decompositions are loopless; these general cases establish that the theorem matches A0's natural circuit semantics.

## 8. AffineCDC specialization

A8 supplies a finite indexed cut-even double cover of the loopless original core. Apply Corollary 5.3 to obtain a finite multiset of circuits covering every core edge exactly twice.

No upstairs circuit, dart rotation, or fibre-cycle decomposition enters this step. The only inputs are:

- finite support;
- intrinsic cut parity;
- exact indexed edge multiplicity.

## 9. Exported interface

A10 may cite:

1. every finite cut-even support decomposes into finitely many edge-disjoint circuits;
2. the decomposition terminates by strict support-cardinality descent;
3. empty supports produce no circuit occurrences;
4. memberwise decompositions concatenate over a finite indexed family;
5. global edge multiplicity is preserved exactly;
6. therefore every finite intrinsic even double cover refines to a cycle double cover.

## 10. Completion assessment

`AC-PD-A9` is `COMPLETE-DRAFT`. No contradiction or new-mathematics gap arose. The next dependency-respecting unit is `AC-PD-A10`: assemble the full finite-active-edge bridgeless multigraph theorem, with exact invocation order, all boundary cases, source ledger, and assurance status.
