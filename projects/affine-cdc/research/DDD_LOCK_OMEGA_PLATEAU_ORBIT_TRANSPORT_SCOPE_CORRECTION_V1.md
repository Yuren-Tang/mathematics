# Scope correction: exterior component energy is not a two-vertex local shift

## Research Lead adversarial correction v1

**Role:** `AffineCDC — Research Lead` (`AC-RL`)  
**Workstream:** `AC-RL-PURE-NNI-02`  
**Workspace:** `Yuren-Tang/mathematics:research/affine-cdc-five-cdc-v1`  
**Exact parent head:** `764fa396ed7573dd5e50922cf4ef37817f87fc0e`

**Corrects:** `DDD_LOCK_OMEGA_PLATEAU_ESCAPE_MASTER_THEOREM_V1.md`.

**Controlling verdict.** Theorem 4.1 of that master dossier, and every unconditional conclusion depending on its local plateau-energy inequality, are **not controlling**. A closed support-component switch changes every triangle along the physical component, not only one triangle of the equal-face cell. The current seam/run package preserves the complete boundary of a specified comparison; it does not by itself construct an energy-preserving bijection between the entire source and target support-switch orbits.

The strict ambient-NNI theorem and the fourteen-vertex source movie remain valid.

---

## 1. Exact overclaim

The quarantined statement asserted that an equal-face component-switch/NNI macro induces plateau endpoint classes `P_-`,`P_+` with

\[
\mu(P_+)\le \mu(P_-)+\Delta_{\rm local},
\]

where `Delta_local` is calculated from only the two displayed triangle slots.

This does not follow from component switching. If `Z` is the selected physical `H_h` component, then

\[
\Omega(S^Z)-\Omega(S)
=
\sum_{v\in V(Z)}
\bigl(\omega(\tau_h\Delta_v)-\omega(\Delta_v)\bigr).
\]

The summands away from the equal-face cell need not cancel and can have either sign. A root rectangle fixing the exterior of one **given** history does not identify minima over all component-switch words on the two different local topologies.

---

## 2. Reproducible `G_14` derived witness against the local shift formula

Use the canonical state encoding

```text
[stable_edge_id,min(endpoint),max(endpoint),sorted_root_digits]
```

sorted by stable edge id with no whitespace.

Take the following complete locked root state in the `G_14` full horizontal closure:

```text
[["05",0,5,"35"],["06",5,6,"25"],["07",0,7,"15"],["1-10",1,10,"12"],["1-11",1,11,"23"],["10-13",10,13,"25"],["18",1,8,"13"],["24",2,7,"12"],["25",0,2,"13"],["29",2,9,"23"],["3-11",3,11,"13"],["3-13",3,13,"15"],["39",3,9,"35"],["4-10",4,10,"15"],["47",4,7,"25"],["58",5,8,"23"],["6-12",6,12,"15"],["6-13",6,13,"12"],["7-11",4,11,"12"],["8-12",8,12,"12"],["9-12",9,12,"25"]]
```

Its SHA-256 digest is

`286a274751ca44679e2832c5317db69c13dcdcb8b7d40eb8bceb15c33ee9c18a`.

Under its compatible DDD normalisation:

- stable edge `47` is the productive equal face `(T,r)=(123,23)`;
- the displayed productive direction `h=14` corresponds in the actual support labels to `h=13`;
- one legal closed component is
  
  \[
  Z=\{1\!-\!10,1\!-\!11,4\!-\!10,7\!-\!11\};
  \]
- the source is a complete oriented lock with `Omega=32`.

Switching `Z` gives a locked root state of energy `28`, digest

`2b51930d5dde1d38b9ed436267a918aa5af9cdab78f5f5ebb94cfc922ed11a98`.

The resulting distinct local pair has a strict root NNI, giving the locked state

```text
[["05",0,5,"35"],["06",5,6,"25"],["07",0,4,"15"],["1-10",1,10,"23"],["1-11",1,11,"12"],["10-13",10,13,"25"],["18",1,8,"13"],["24",2,7,"12"],["25",0,2,"13"],["29",2,9,"23"],["3-11",3,11,"13"],["3-13",3,13,"15"],["39",3,9,"35"],["4-10",4,10,"35"],["47",4,7,"13"],["58",5,8,"23"],["6-12",6,12,"15"],["6-13",6,13,"12"],["7-11",7,11,"23"],["8-12",8,12,"12"],["9-12",9,12,"25"]]
```

of energy `27` and digest

`a69c9afa618aff6e10b1ef4f2edc209ff12029e4cffb0ca3b6e1ebfbf4101315`.

Now restrict only to closed `H_13` component switches on the source and target labelled topologies. Exact enumeration gives:

\[
\min\Omega(\mathcal O_{H_{13}}^{\rm source})=20,
\qquad
\min\Omega(\mathcal O_{H_{13}}^{\rm target})=27.
\]

The target orbit minimum is **higher**, although the two-vertex coefficient row is locally decreasing. Hence no universal local-shift formula can be deduced merely by quotienting by that component-switch orbit.

This witness does not refute an eventual full-alphabet plateau escape theorem: larger target closure already contains route-changing states. It refutes only the claimed automatic orbit-energy transport.

---

## 3. Second missing interface: zero overlap

When commuting an arbitrary support-switch word through a root dipole insertion, a one-sided switch in the central direction `h=p+q` can change the insertion pair from distinct intersecting roots `(p,q)` to equality `(q,q)` or `(p,p)`. The raw central value is then zero and the four local exterior copies are equal.

`CELLWISE_ROOT_SEAM_AND_CONSTANT_RUN_TRACK_ERASURE_V1.md` controls a normalized nonbranching **co-root** track with root-valued endpoint collars. It does not, by itself, turn a quadruple-equality zero insertion into a co-root track or a root endpoint. Therefore the master proof also overread the one-atom package when it treated every zero/co-root critical overlap as one already-erased co-root rectangle.

An equality alternative insertion, an exact route exit, or a separate root endpoint theorem is required for this row.

---

## 4. Retained mathematics from the quarantined master

The following statements remain exact.

1. The complete plateau state/interface definition and the warning that finiteness alone gives no exit.
2. The local three-matching lemma:
   an equal-face branch swap either changes the oriented route or one branch placement has the two local `H_h` passages in distinct components.
3. The five coefficient rows
   
   \[
   (123,23),\ (125,25),\ (235,25),\ (245,25),\ (345,45),
   \]
   and their displayed one-sided switch/root-NNI local movies.
4. Conditional on a source-level strict plateau transition for those rows, the five-type residual reduction
   
   \[
   \{124,134,135,145,234\}
   \]
   is exact.
5. For that residual alphabet, the `H_13/H_14` route-sector contradiction is exact.

Thus the finite coefficient and route analysis has reduced the open plateau problem to one transport statement; it has not proved that statement.

---

## 5. Correct smallest remaining implication

Call the missing theorem

\[
\boxed{\texttt{DDD-PLATEAU-PRODUCTIVE-ROW-ESCAPE}.}
\]

For a complete prime oriented DDD lock with no strict `Omega`-lowering ambient NNI, and for a forced productive equal face in one of the five exact rows, prove one of:

1. the equal-face branch swap changes the oriented route;
2. a legal component switch reaches `K_i` or a separating channel;
3. a named cut/bounded terminal occurs;
4. a finite complete source movie reaches a locked state of strictly smaller **proved complete-state rank**;
5. or the complete pure-NNI/support-switch closure contains a genuine nonterminal SCC.

The rank in Item 4 may use exterior component data, but it may not be replaced by the two-vertex coefficient difference or by an undefined orbit minimum.

Once this implication is proved, the retained five-type residual route contradiction completes `FC-PURE-NNI-ESCAPE`.

---

## 6. Controlling status after correction

\[
\boxed{
\begin{array}{c}
G_{14}\text{ ambient escape movie: VERIFIED}\\
+\ \text{strict }\Omega\text{ ambient-NNI trichotomy: COMPLETE}\\
+\ \text{five productive coefficient rows: COMPLETE}\\
+\ \text{residual }H_{13}/H_{14}\text{ contradiction: COMPLETE}\\
\hline
\texttt{DDD-PLATEAU-PRODUCTIVE-ROW-ESCAPE}:\ \text{OPEN}.
\end{array}}
\]

Accordingly `DDD_LOCK_OMEGA_PLATEAU_ESCAPE_MASTER_THEOREM_V1.md` is an authorial **candidate attempt with a quarantined load-bearing lemma**, not a completed `FC-PURE-NNI-ESCAPE` proof.

No v7.2 repair, induction closure, five-support theorem or five-CDC theorem follows until the corrected implication is established and reconstructed.
