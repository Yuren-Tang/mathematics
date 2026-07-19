# Context-limit recovery verification: route lock, quotient, and curvature witnesses

**Programme:** `AffineCDC — Research Lead`  
**Recovery incident:** `AC-RL-RECOVERY-02`  
**Exact parent:** `research/affine-cdc-five-cdc-v1@03dc04b109a81bddc0f2fc8694b4aaa056c9977c`  
**Status:** bounded successor recovery unit; exact finite verification and one recovered finite counterexample; research-active, not canonical and not independently audited  
**Saved parents:** `FIVE_CDC_DDD_ATOM_RESOLUTION_TRIALITY_V1.md`, `FIVE_CDC_ATOM_ROUTE_LOCK_CURVATURE_V1.md`, `FIVE_CDC_ROUTE_LOCK_RANK_TWO_TAIT_ESCAPE_V1.md`, `FIVE_CDC_FULL_RANK_CURVATURE_DUAL_CERTIFICATE_V1.md`

## 1. Scope and evidence boundary

The predecessor conversation ended during an unsaved computation.  The owner-rescued notebook preserved prose and code fragments, but its final combined verifier was incomplete and retained an unidentified failing assertion.  This packet reconstructs the definitions from the committed parent packets and reruns only the bounded finite modules required by the Tier A recovery packet.

The computation was executed in a fresh Python process using only the standard library.  Every assertion in the reconstructed verifier passed.  The historical identity of the predecessor's failing assertion cannot be recovered because the copied `routeWords` expression is truncated and the pair-separating cut routine ends mid-definition.  Accordingly:

- the old notebook remains `CODE-PARTIAL`;
- the mathematical assertions listed below are independently rechecked;
- no claim is made about omitted notebook state or hidden reasoning.

Conventions:

- roots are the ten two-subsets of `[5]`, represented as five-bit masks;
- addition is symmetric difference;
- an ordered boundary state is `(ell_1,ell_2,ell_3,ell_4)` with total sum zero;
- the atom pairing is `12|34`, with defect `d=ell_1+ell_2`;
- a state is good when `d` is a root;
- a root `a` is a full challenge when `|a cap ell_i|=1` for all four terminals;
- the three route pairings are `12|34`, `13|24`, and `14|23`;
- for an `F_2^3` colour `x` and functional `lambda`, the scalar sheet contains exactly the edges with `lambda(x)=1`.

## 2. Canonical challenge and route-transition reconstruction

For the canonical ordered `D_0` terminal-incidence data

$$
(23,45,24,35),
$$

the roots meeting all four terminal labels oddly are exactly

$$
X=25,
\qquad
Y=34.
$$

Using route order `12|34`, `13|24`, `14|23`, the reconstructed ten-state transition table is

$$
\begin{array}{c|ccc}
&12|34&13|24&14|23\\
\hline
25&C_2&B_2&D_1\\
34&C_1&D_2&B_1.
\end{array}
$$

The original route sends the two canonical challenges to the two repeated-matching `C` states.  Either crossed route reaches a root-valued state type, agreeing with the saved atom-resolution triality.

## 3. Universal unique-bad-route census

Direct enumeration gives:

$$
\boxed{
640\text{ ordered zero-sum root states},
\quad
280\text{ bad states},
\quad
180\text{ co-root-defect states}.
}
$$

There are `840` bad-state/full-challenge rows.  On every row the **good-target** word is

$$
(0,1,1),
$$

or equivalently the **bad-route** word is

$$
\boxed{(1,0,0)}.
$$

Thus the original atom pairing is always the unique bad route and both crossed routes rootify the defect.  This independently reproduces the committed unique-bad-route theorem.

## 4. Six-state fixed fibre

Fix the co-root

$$
q=1234
$$

and the ordered right pair `(12,34)`.  The six possible ordered left pairs form a graph under full-challenge switching along the `12` path.

Exact output:

- vertices: `6`;
- edges: `8`;
- degree multiset: `(2,2,2,2,4,4)`;
- state types: `4D_0+C_1+C_2`;
- each `D_0` vertex is adjacent to both `C` vertices and there are no other edges.

Hence the fixed fibre is exactly

$$
\boxed{K_{2,4}},
$$

not the Type-T `P_5` kernel.

## 5. Challenge quotient

At the canonical locked `C` state

$$
(35,24,24,35),
$$

the four full challenges are

$$
23,
\quad25,
\quad34,
\quad45.
$$

Let

$$
\chi(x)=
(\langle x,23\rangle,
 \langle x,25\rangle,
 \langle x,34\rangle,
 \langle x,45\rangle).
$$

The clean enumeration gives

$$
\ker(\chi|_{E_5})=\{0,2345\}=\langle2345\rangle,
$$

$$
\chi(E_5)=E_4,
\qquad
|\chi(E_5)|=8,
$$

and

$$
\chi(R_5)=E_4\setminus\{0\}.
$$

The two terminal root values `35` and `24` both map to

$$
g=1111.
$$

This independently reproduces the saved quotient

$$
E_5/\langle q\rangle\cong E_4\cong F_2^3.
$$

## 6. Rank-two route-lock witnesses

### 6.1 Owner-rescued witness

Take terminal vertices in order

$$
(0,1,2,3)
$$

and the following internal edges, with colours written as binary integers in `F_2^3`:

$$
\begin{array}{c|c@\qquad c|c}
06&4&05&5\\
14&5&17&4\\
26&5&25&4\\
37&5&34&4\\
45&1&67&1.
\end{array}
$$

Checks:

- vertices `0,1,2,3` have internal degree two and boundary sum `g=1`;
- vertices `4,5,6,7` have degree three and colour sum zero;
- the colour span has rank two;
- for the four functionals `lambda in {1,3,5,7}` with `lambda(g)=1`, every scalar sheet routes `12|34`;
- exhaustive enumeration of the `2^4` placements of the four nonterminal vertices gives minimum pair-separating cut size four.

Therefore this is a finite-verified route-lock witness with no graph two-cut.

### 6.2 Committed parent witness

The distinct witness displayed in `FIVE_CDC_ATOM_ROUTE_LOCK_CURVATURE_V1.md` was also rerun independently.  Its terminal colour is `g=7`; its colour rank is two; all four relevant functionals `1,2,4,7` route `12|34`; and the minimum pair-separating cut is four.

Thus the recovered witness and the committed certificate agree on the exact negative conclusion

$$
\boxed{
\text{route-lock}
\not\Rightarrow
\text{graph-theoretic two-edge separation}.
}
$$

The committed theorem was already `REMOTE-EXACT`; this rerun supplies an independent recovery check rather than a new trust upgrade.

## 7. Full-rank nonflat curvature witness

Take terminal vertices in the order

$$
(0,2,1,3)
$$

and the edge-coloured four-pole

$$
\begin{array}{c|c@\qquad c|c}
06&3&09&2\\
15&2&13&3\\
29&6&27&7\\
34&2&48&5\\
46&7&57&6\\
56&4&78&1\\
89&4&&
\end{array}
$$

### Proposition 7.1 — recovered finite nonflat witness

This four-pole has a nowhere-zero full-rank `F_2^3` flow with all four terminal values equal to `g=1`, all four scalar sheets locked to `12|34`, and nonzero curvature class.

#### Certificate

1. The terminal vertices have internal degree two and boundary sum `1`; every other vertex has degree three and colour sum zero.
2. The used colours are all seven nonzero vectors, so the colour span has rank three.
3. For `lambda=1,3,5,7`, the four scalar routes are respectively
   
   $$
   12|34,
   \quad12|34,
   \quad12|34,
   \quad12|34.
   $$
4. The unique physical `g`-edge is
   
   $$
   E_g=\{78\}.
   $$
5. Give every `12` terminal path side zero and every `34` terminal path side one.  The component containing edge `78` is the `12` path for `lambda=1,5,7` and the `34` path for `lambda=3`.  Hence its four sheet-side values are
   
   $$
   \boxed{0100}.
   $$
6. The edge `78` lies on a terminal path in every sheet.  Therefore no closed scalar component contains the unique `g`-edge, so every generator `1_{C cap E_g}` is zero.  The quotient toggle space is zero on this coordinate.
7. The curvature bit is the parity of `0100`, namely one.  Thus
   
   $$
   \boxed{\Omega(c)\ne0}.
   $$

Consequently the overstrong automatic-flatness statement is false:

$$
\boxed{
\text{universal scalar route-lock}
\not\Rightarrow
\Omega(c)=0
\not\Rightarrow
\text{automatic affine potential}.
}
$$

This does not contradict the saved flat/nonflat dichotomy.  It realises its nonflat branch and confirms that graph/matroid localisation of the common-cut witness is genuinely necessary.

## 8. Isolation of the historical failing assertion

The owner-rescued transcript does not contain a complete assertion list for the final combined verifier:

- the segmented `routeWords` expression is syntactically unfinished;
- the `separatedQ` definition stops after `VertexList ->`;
- the later notebook object reportedly having length `48` has no recovered constructor;
- no assertion label or segmented output identifies the line that failed.

After reconstructing the modules separately, **no mathematical assertion in either displayed witness fails**.  The rank-two route, rank, and min-cut tests pass; the full-rank route, rank, unique-`g`-edge, side-word, and curvature tests pass.  The remaining historical failure is therefore isolated to unavailable/incomplete verifier state, but its exact old source cannot honestly be named.

This is a recovery conclusion, not a claim that the lost code was repaired verbatim.

## 9. Reliability classification after rerun

| Item | Classification after recovery |
|---|---|
| Saved DDD triality, unique-bad-route theorem, `640/280/180`, fixed `K_{2,4}` fibres, quotient theorem, committed rank-two witness, rank-two Tait escape, flatness criterion, common-cut dual certificate | `REMOTE-EXACT`; independently rerun where finite |
| Canonical route-transition table and owner-rescued six-state/quotient descriptions | `FINITE-VERIFIED`; agree with committed parents |
| Owner-rescued rank-two witness | `FINITE-VERIFIED`; confirms the same negative theorem as the committed witness |
| Owner-rescued full-rank one-`g`-edge witness with side word `0100` | `FINITE-VERIFIED`; recovered counterexample to automatic flatness |
| Truncated combined verifier and omitted notebook objects | `CODE-PARTIAL`; historical failing line unavailable |
| Safe graph resolution from a flat potential | `OPEN` |
| Support-minimal common-cut localisation to bounded DDD/Petersen atom, smaller cyclic separator/reducible interval, transition-matroid two-sum, or physical `D_8` class | `OPEN` |
| Identification of the odd curvature class with the physical DDD cohomology class | `OPEN` |

No claim in this packet changes canonical, formal, independent-review, peer-review, release, DOI, or publication status.

## 10. Consequence and next frontier boundary

The recovery unit closes the finite-state uncertainty without enlarging the state space:

- arbitrary route choice is no longer the bottleneck;
- the rank-two sector escapes algebraically by the saved Tait lift even though it need not have a graph two-cut;
- the full-rank locked sector genuinely contains both flat and nonflat examples;
- the nonflat example shows that the dual common-cut theorem is not vacuous.

The next frontier question remains exactly the saved one.  Choose a support-minimal dual witness

$$
\eta\subseteq E_g.
$$

Localise it to a bounded DDD/Petersen factor, a smaller cyclic separator or reducible transition interval, a transition-matroid two-sum, or produce a precise counterexample forcing a weaker localisation statement.  No such graph-level localisation is claimed here.

## Appendix A. Reproducible verifier outline

The checks use only bit masks, exhaustive products, connected components, binary rank reduction, and exhaustive terminal-separating cuts.  The following compact pseudocode records the complete assertion surface:

```python
roots = all_two_subsets(range(5))
states = [s for s in roots**4 if xor(s) == 0]
bad = [s for s in states if weight(s[0] ^ s[1]) != 2]
assert (len(states), len(bad), count_coroot(bad)) == (640, 280, 180)

for s in bad:
    for a in full_challenges(s):
        assert tuple(is_root(defect(switch(s, a, route)))
                     for route in (12_34, 13_24, 14_23)) == (False, True, True)

assert canonical_full_challenges == [(2, 5), (3, 4)]
assert canonical_transitions == {
    (2, 5): ("C2", "B2", "D1"),
    (3, 4): ("C1", "D2", "B1"),
}

assert fixed_fibre.size == 6
assert fixed_fibre.edge_count == 8
assert sorted(fixed_fibre.degrees) == [2, 2, 2, 2, 4, 4]
assert fixed_fibre.types == Counter({"D0": 4, "C1": 1, "C2": 1})
assert fixed_fibre.is_complete_bipartite(2, 4)

assert quotient.full_challenges == [(2, 3), (2, 5), (3, 4), (4, 5)]
assert quotient.kernel == [0, mask(2, 3, 4, 5)]
assert quotient.image == even_words_of_length_4
assert quotient.root_image == even_words_of_length_4 - {0}
assert all(quotient.code(r) == 0b1111 for r in terminal_roots)

assert rescued_rank_two.flow_boundary == [1, 1, 1, 1]
assert rescued_rank_two.rank == 2
assert rescued_rank_two.routes == ["12|34"] * 4
assert rescued_rank_two.minimum_pair_cut == 4

assert committed_rank_two.flow_boundary == [7, 7, 7, 7]
assert committed_rank_two.rank == 2
assert committed_rank_two.routes == ["12|34"] * 4
assert committed_rank_two.minimum_pair_cut == 4

assert full_rank.flow_boundary == [1, 1, 1, 1]
assert full_rank.rank == 3
assert full_rank.routes == ["12|34"] * 4
assert full_rank.g_edges == [(7, 8)]
assert full_rank.side_word == (0, 1, 0, 0)
assert full_rank.closed_sheet_toggle_space_on_Eg == 0
assert full_rank.Omega_nonzero
```

Fresh-process output:

```text
state counts: 640 / 280 / 180
bad-state/full-challenge rows: 840; good-target word 011 throughout
canonical full challenges: 25, 34
canonical transitions: 25 -> C2,B2,D1; 34 -> C1,D2,B1
fixed fibre: 6 vertices, 8 edges, degrees 2,2,2,2,4,4, types 4D0+C1+C2, graph K2,4
quotient: kernel {0,2345}, image size 8, root image size 7, terminal code 1111
rescued rank-two witness: rank 2, routes 12|34 x4, minimum pair cut 4
committed rank-two witness: rank 2, routes 12|34 x4, minimum pair cut 4
full-rank witness: rank 3, routes 12|34 x4, g=1, E_g={78}, side word 0100, Omega nonzero
all reconstructed assertions passed
```
