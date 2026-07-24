# The fourteen-vertex full-channel lock has a literal ambient pure-NNI escape

## Research Lead source-movie certificate v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workstream:** `AC-RL-PURE-NNI-02`  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `7ee2e9df2c79f5ef6ad179cfd148f6a84c2edbd3`  
**Controlling input:** `PURE_NNI_PRESCRIBED_PARENT_PHASE_B_SUPPORT_CHANNEL_TRANSITION_OBJECT_V1.md`

**Verdict.** The Director candidate movie on `G_14` is correct. One ambient root NNI strictly lowers the established DDD potential and breaks two rescue-channel locks; one legal closed support-component switch then makes the prescribed parent root-valued; one final root NNI realizes the labelled parent topology literally. Every intermediate closed graph is connected, simple, loopless, bridgeless and cubic. The current, post-ambient-NNI and final parent topologies all have girth five and cyclic edge-connectivity five.

This is a finite model case, not yet the general `FC-PURE-NNI-ESCAPE` theorem.

---

## 1. Stable labelled input

Let `V={0,...,13}`. Stable edge identities, initial incidences and roots are

| edge id | endpoints | root |
|---|---:|---:|
| `05` | `0-5` | `23` |
| `06` | `0-6` | `13` |
| `07` | `0-7` | `12` |
| `18` | `1-8` | `24` |
| `1-10` | `1-10` | `23` |
| `1-11` | `1-11` | `34` |
| `24` | `2-4` | `23` |
| `25` | `2-5` | `24` |
| `29` | `2-9` | `34` |
| `39` | `3-9` | `14` |
| `3-11` | `3-11` | `24` |
| `3-13` | `3-13` | `12` |
| `47` | `4-7` | `13` |
| `4-10` | `4-10` | `12` |
| `58` | `5-8` | `34` |
| `6-12` | `6-12` | `12` |
| `6-13` | `6-13` | `23` |
| `7-11` | `7-11` | `23` |
| `8-12` | `8-12` | `23` |
| `9-12` | `9-12` | `13` |
| `10-13` | `10-13` | `13` |

The active edge is the stable edge `05`. Its ordered exterior darts are

\[
A=07=12,\qquad B=58=34,\qquad C=06=13,\qquad D=25=24.
\]

The current pairing is `AC|BD`, with central root `05=23`; the other crossed pairing is `AD|BC`, with central root `14`; the prescribed parent is `AB|CD`, whose initial forced central value is `Q_5`.

The initial vertex triangles are

\[
\begin{array}{c|cccccccccccccc}
v&0&1&2&3&4&5&6&7&8&9&10&11&12&13\\
\hline
\Delta_v&123&234&234&124&123&234&123&123&234&134&123&234&123&123.
\end{array}
\]

Thus the initial DDD potential is

\[
\Omega(S_0)=29.
\]

### Stable cap block

The Phase-B graph admits a cap block disjoint from every move below. Fix cap vertices `3,13`, cap edge `3-13=12`, and ordered cap darts

\[
t_1=39=14,\quad t_2=3\!-\!11=24,\quad t_3=6\!-\!13=23,\quad t_4=10\!-\!13=13.
\]

Its physical cap matching is

\[
(t_1t_2)\mid(t_3t_4),
\]

since both pairing sums equal `12`. None of the three source moves changes these four dart incidences, their roots, the cap vertices, or the cap edge. This completes the cap coordinate omitted from the abbreviated Phase-B display without changing its active state.

---

## 2. Ambient NNI on stable edge `24`

At vertex `2`, the exterior roots relative to `24` are

\[
25=24,\qquad 29=34,
\]

and at vertex `4` they are

\[
47=13,\qquad 4\!-\!10=12.
\]

Perform the labelled NNI which retains stable darts `25@2`, `47@4`, and the two central darts of `24`, while moving

\[
29@2\longmapsto29@4,
\qquad
(4\!-\!10)@4\longmapsto(4\!-\!10)@2.
\]

The outside darts `29@9` and `(4-10)@10` are fixed. Hence the incidence changes are exactly

\[
29:2-9\longmapsto4-9,
\qquad
4-10:4-10\longmapsto2-10.
\]

The new central value is

\[
24+12=13+34=14.
\]

The old local triangle pair and new pair are

\[
234+123\longmapsto124+134.
\]

All other edge roots and incidences are fixed. Thus

\[
\Omega(S_1)=28<29=\Omega(S_0).
\]

The complete post-NNI triangle row is

\[
\begin{array}{c|cccccccccccccc}
v&0&1&2&3&4&5&6&7&8&9&10&11&12&13\\
\hline
\Delta_v&123&234&124&124&134&234&123&123&234&134&123&234&123&123.
\end{array}
\]

No active dart, cap dart or prescribed-parent dart identity is changed.

---

## 3. Exact `H_14` and `H_23` decomposition

For a root `h`, an edge belongs to

\[
H_h=F_i\triangle F_j
\]

exactly when its current root intersects `h` in one support index.

In `S_1`, both `H_14` and `H_23` have the same fourteen selected stable edges and split into exactly two cycles.

The six-edge component containing `A=07` is

\[
\boxed{Z_A=\{06,07,29,47,6\!-\!12,9\!-\!12\}}.
\]

Its vertex cycle is

\[
0-6-12-9-4-7-0,
\]

where stable edge `29` now has incidence `4-9`.

The complementary eight-edge component containing `B=58` is

\[
Z_B=\{18,1\!-\!11,25,3\!-\!11,3\!-\!13,4\!-\!10,58,10\!-\!13\},
\]

with vertex cycle

\[
1-8-5-2-10-13-3-11-1.
\]

Consequently, in each of `H_14` and `H_23`,

\[
A,C\subset Z_A,
\qquad
B,D\subset Z_B.
\]

In particular both channel systems separate the marked parent roots `A` and `B`. The oriented full-channel-lock condition has therefore been broken by the single strict ambient NNI.

---

## 4. Closed `H_14` component switch

Switch the complete closed component `Z_A` by `h=14`. No incidence changes. The six root translations are

\[
\begin{array}{c|cccccc}
e&06&07&29&47&6-12&9-12\\
\hline
\text{before}&13&12&34&13&12&13\\
\text{after}&34&24&13&34&24&34.
\end{array}
\]

At each vertex of the switched cycle exactly two incident edges are translated, so every vertex equation remains root-valued. The affected triangle types become

\[
0,6,7,12:123\longmapsto234,
\]

while the equal-weight local exchanges at `4,9` retain type `134`.

The active word is now

\[
\boxed{(A,B,C,D)=(24,34,34,24)}.
\]

The stable active edge is unchanged:

\[
05=23,
\]

because `05` is not in `H_14`. At vertices `0,5` one has

\[
24+34=23,
\qquad
34+24=23.
\]

The support-unordered active state is now `B_2=(1,1,0)`, hence lies in the prescribed-cap-compatible sector

\[
B_2\in K_0.
\]

The prescribed parent obligation survives literally; only the root assignment and support-component partitions change.

---

## 5. Literal active parent NNI

Starting from the switched state, perform the NNI on stable edge `05` that groups `A,B` at vertex `0` and `C,D` at vertex `5`.

Keep `07@0`, `25@5`, both central darts of `05`, and all outside darts. Move exactly

\[
06@0\longmapsto06@5,
\qquad
58@5\longmapsto58@0.
\]

Thus stable edge identities acquire final incidences

\[
06:0-6\longmapsto5-6,
\qquad
58:5-8\longmapsto0-8.
\]

The forced central root is

\[
A+B=C+D=24+34=23.
\]

Hence the central stable edge `05` remains root `23`. Both final active vertices carry triangle `234`. The resulting labelled topology is exactly the stored `AB|CD` parent topology, not merely an isomorphic root graph.

The complete dart ancestry is the identity except for the four explicitly moved inside darts

\[
29@2,\ (4-10)@4,\ 06@0,\ 58@5.
\]

All corresponding outside darts and every cap dart remain fixed. This supplies the literal prefix-splicing map `alpha`.

---

## 6. Graph-category and terminal audit

Let

- `G_0` be the displayed initial topology;
- `G_1` the topology after the ambient NNI on `24`;
- `G_2` the final prescribed-parent topology after the NNI on `05`.

The support switch changes no topology, so its graph is also `G_1`.

For each graph, enumerate every proper vertex subset `X` containing vertex `0`. Retain `X` only when both induced shores contain a cycle, and compute the cut size `|delta(X)|`. This is an exact labelled `2^13-1` subset test.

The resulting certificates are

\[
\begin{array}{c|c|c|c|c|c|c}
&\text{connected}&\text{simple}&\text{cubic}&\text{bridges}&\text{girth}&\lambda_c\\
\hline
G_0&\text{yes}&\text{yes}&\text{yes}&0&5&5\\
G_1&\text{yes}&\text{yes}&\text{yes}&0&5&5\\
G_2&\text{yes}&\text{yes}&\text{yes}&0&5&5.
\end{array}
\]

The numbers of complementary shore representatives attaining cyclic cut size five, with the convention `0 in X`, are respectively

\[
7,\qquad6,\qquad7.
\]

Therefore no loop, parallel, bridge, triangle, theta, low-port, cyclic `2`-, `3`-, or `4`-cut terminal occurs at any stage. The only terminal effect is the successful cap-compatible/prescribed-parent realization itself.

---

## 7. Reproducible state encoding

Encode a state as the UTF-8 JSON array of rows

```text
[stable_edge_id, min(endpoint), max(endpoint), sorted_root_digits]
```

sorted lexicographically by `stable_edge_id`, with no whitespace. The SHA-256 digests are

| state | digest |
|---|---|
| initial `S_0` | `8dfd2d8e445c9bfc9dc55178bcd6768181b90c7c3eb9ad249ce5c9068fde4690` |
| post-ambient-NNI `S_1` | `09b7ab7f4640011030c14989ea7d6c0c99a737198d6408af2e00a7b3505b8558` |
| post-switch `S_2` | `f18d2b7cc900b6c83cab93dbe89dea41f00e2cbbd2439298fcd8aeb748c4ed80` |
| final parent `S_3` | `8716082e28f597f2a3116d1115d4c1669b8d78cfb44e84f9821ca735c902da9b` |

A reproducer needs only:

1. the initial table in Section 1;
2. symmetric difference of two-subset roots;
3. the two incidence swaps in Section 2;
4. the six root translations in Section 4;
5. the two incidence swaps in Section 5;
6. exhaustive subset enumeration for Section 6.

No graph-isomorphism quotient or heuristic search is used.

---

## 8. Model-case theorem

### Theorem `G14-AMBIENT-ESCAPE`

The complete prime fourteen-vertex oriented DDD full-channel lock of the Phase-B dossier admits the source-faithful fixed-order history

\[
\boxed{
\text{strict }\Omega\text{-lowering ambient root NNI}
\longrightarrow
\text{separating closed }H_{14}\text{ switch}
\longrightarrow
\text{literal prescribed-parent root NNI}.}
\]

Every state is root-valued; graph order remains fourteen; the stored cap block, prescribed topology, exterior dart identities and prefix ancestry are retained exactly as specified above; and no category terminal is used.

The old `240`-state horizontal SCC is therefore not closed under the full ambient root-NNI alphabet. It cannot support an architecture-change verdict.

---

## 9. Trust boundary

### Verified here

- every candidate edge/root/incidence datum;
- the exact `H_14=H_23` two-cycle decomposition after the ambient NNI;
- the Director-specified six-edge component;
- the complete support translation and active boundary map;
- literal parent topology realization;
- a stable cap block and its preservation;
- complete root-triangle rows;
- strict `Omega` decrease `29 -> 28` at the ambient NNI;
- connected/simple/loopless/bridgeless/cubic category at every stage;
- girth and cyclic edge-connectivity five for current, intermediate and final topologies.

### Not proved here

- the universal `FC-PURE-NNI-ESCAPE` theorem;
- classification of every `Omega`-minimal plateau;
- v7.2 induction closure;
- any five-support or five-CDC theorem;
- Lean, Curator, manuscript, release or publication status.
