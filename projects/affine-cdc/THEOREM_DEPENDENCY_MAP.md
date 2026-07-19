# AffineCDC theorem dependency map

This map separates the complete Cycle Double Cover spine from the open five-support strengthening and records the dependencies among the reconstructed chapters.

## 1. Complete CDC existence spine

$$
\boxed{
\begin{array}{c}
\text{bridgeless multigraph with finite active edge set}\\
\downarrow\;\text{delete loops}\\
\text{finite loopless bridgeless core}\\
\downarrow\\
\text{cubic expansion with nowhere-zero }\mathbf F_2^3\text{ flow}\\
\downarrow\\
\text{affine incidence datum }(\mathcal P_f,\kappa)\\
\downarrow\\
\text{rank-three Fano compatibility}\\
\downarrow\\
\text{compatible indexed support family}\\
\downarrow\\
\text{graph-level multiset even double cover}\\
\downarrow\\
\text{cut-even collapse transport}\\
\downarrow\\
\text{one finite circuit decomposition}\\
\downarrow\;\text{reinsert singleton loop circuits}\\
\text{cycle double cover.}
\end{array}}
$$

Controlling chapters:

- [`core/affine-incidence-and-obstruction.md`](core/affine-incidence-and-obstruction.md);
- [`core/rank-three-fano-compatibility.md`](core/rank-three-fano-compatibility.md);
- [`reduction/even-cover-and-collapse.md`](reduction/even-cover-and-collapse.md);
- [`reduction/outer-shell-and-binary-flow.md`](reduction/outer-shell-and-binary-flow.md).

This spine is paper-level mathematics with the formal boundaries stated in [`FORMAL_STATUS.md`](FORMAL_STATUS.md).

## 2. Five-support strengthening: object layer

$$
\boxed{
\begin{array}{c}
\text{indexed five-support even cover}\\
\Updownarrow\\
\text{root-valued }E_5\text{ flow}\\
\Updownarrow\\
\text{$K_5$ triangle labelling}\\
\Updownarrow\\
\text{matching + nowhere-zero }\mathbf F_2^2\text{ flow}\\
\Updownarrow\\
\text{quadratic-cycle / cographic formulation.}
\end{array}}
$$

Controlling chapter:
[`five-support/root-flow-lifting.md`](five-support/root-flow-lifting.md).

## 3. Projection/lifting layer

$$
\begin{array}{c}
\text{nowhere-zero Fano flow }f\\
\downarrow\\
\text{universal compatible eight-support root lift }g\\
\downarrow\;\text{choose plane/slice }W\\
\text{singular quotient and component obstruction}\\
\Updownarrow\\
\text{outside-colour cut parity}\\
\Updownarrow\\
\partial(x*y)=0\\
\Updownarrow\\
\text{vanishing against all relative stresses.}
\end{array}
$$

The fixed-plane theorem is complete after $f$ and $W$ are fixed. The global five-support statement requires varying the flow, lift, and componentwise surface map.

## 4. Surface/target layer

$$
\begin{array}{c}
\text{compatible root lift }g\\
\Updownarrow\\
\text{coloured cycle-face surface }S_g\\
\Updownarrow\\
\text{coloured dual triangulation }T_g\\
\downarrow\\
T_g^{(1)}\to\mathscr A_5\ ?
\end{array}
$$

The colour quotient factors this map as

$$
T_g^{(1)}\to J_g\to\mathscr A_5.
$$

The second route is a strict factorable subclass.

Dependencies:

- root-flow lifting;
- root-lift/surface correspondence;
- target half-cube geometry;
- marked obstruction certificates.

Controlling chapter:
[`five-support/surfaces-and-halfcube.md`](five-support/surfaces-and-halfcube.md).

## 5. Vertical gauge layer

$$
\begin{array}{c}
\text{fixed Fano flow }f\\
\downarrow\\
\text{root-lift torsor under }H_f^0\\
\downarrow/\text{global translations}\\
\text{reduced gauge code }B_f\\
\Updownarrow\\
\text{code-filtered partial Petrials}\\
\downarrow\\
\text{marked-core occurrence cosets }A_C\subseteq B_f.
\end{array}
$$

For a finite certificate library $\mathscr L$,

$$
\operatorname{Bad}_f(\mathscr L)=\bigcup_C A_C.
$$

Controlling chapters:

- [`five-support/gauge-and-reconfiguration.md`](five-support/gauge-and-reconfiguration.md);
- [`five-support/surfaces-and-halfcube.md`](five-support/surfaces-and-halfcube.md).

## 6. Horizontal flow layer

$$
\begin{array}{c}
\operatorname{NZFlow}(G;\mathbf F_2^3)\\
\subseteq Z_1(G)\otimes\mathbf F_2^3\\
\downarrow\;\text{connected-cycle rank-one switches}\\
\text{new Fano flow }f'\\
\downarrow\\
\text{new root-lift torsor and new obstruction arrangement.}
\end{array}
$$

Internal directions correct one fixed slice by the exact boundary-space image. External directions reslice the quotient.

Controlling chapter:
[`five-support/gauge-and-reconfiguration.md`](five-support/gauge-and-reconfiguration.md).

## 7. Source-interface layer

$$
\begin{array}{c}
\text{persistent marked obstruction or bad fibre}\\
\downarrow\\
\text{reserve code / harmonic quotient}\\
\downarrow\\
\begin{cases}
\text{cyclic three-cut} &\Rightarrow\text{glue immediately},\\
\text{cyclic four-cut} &\Rightarrow\text{ten-state shore profiles}.
\end{cases}
\end{array}
$$

For a four-cut:

$$
\begin{array}{c}
\text{cap forcing + Kempe closure}\\
\downarrow\\
\text{deterministic routing policy}\\
\downarrow\\
P_5\mid P_5
\quad\text{or}\quad
P_4\mid C_3.
\end{array}
$$

Controlling chapter:
[`five-support/cuts-four-poles-and-routing.md`](five-support/cuts-four-poles-and-routing.md).

## 8. Type H holonomy layer

$$
\begin{array}{c}
\text{rainbow routing triangle}\\
\downarrow\\
(\pi,z)\in(Z_1(P)\otimes E_5)\rtimes S_5\\
\downarrow\\
N_\pi z\\
\downarrow\\
\begin{cases}
N_\pi z\ne0&\text{ambient translation},\\
N_\pi z=0&\text{root-fibre section problem}.
\end{cases}\\
\downarrow\\
\begin{cases}
\text{Tait resolution}&\Rightarrow\text{profile escape},\\
\text{no section}&\Rightarrow\text{local/holonomy certificate}.
\end{cases}
\end{array}
$$

The BBD family strengthens this to one canonical $E_5$ flow by root rigidity and $H^1(S_5,E_5)=0$.

Controlling chapter:
[`five-support/holonomy-defects-and-atoms.md`](five-support/holonomy-defects-and-atoms.md).

## 9. Defect/atom layer

$$
\begin{array}{c}
\text{canonical or energy-minimal }E_5\text{ flow}\\
\downarrow\\
\text{induced defect forest}\\
\downarrow\\
\text{zero networks + co-root strips}\\
\downarrow\\
L(\mathrm{Petersen})\text{ transducer}\\
\downarrow\\
\text{one-edge co-root atoms and DDD triality}\\
\downarrow\\
\text{unique bad route / locked }K_{2,4}\text{ orbit}\\
\downarrow\\
\begin{cases}
\text{rank two}&\Rightarrow\text{Tait escape},\\
\text{full rank, }\Omega\ne0&\Rightarrow\text{common-cut witness},\\
\text{full rank, }\Omega=0&\Rightarrow\text{affine potential}.
\end{cases}
\end{array}
$$

Controlling chapter:
[`five-support/holonomy-defects-and-atoms.md`](five-support/holonomy-defects-and-atoms.md).

## 10. Open closure dependencies

The current frontier requires four bridges in this order.

1. **Atom localisation**  
   Common-cut witness or flat potential $\Rightarrow$ bounded interface, smaller separator, transition split, or DDD class.

2. **Forest pruning**  
   Local atom/interface results $\Rightarrow$ strict reduction of zero/co-root defect trees.

3. **Four-pole transfer**  
   Defect transfer data $\Rightarrow$ profile expansion, full cap set, serial replacement, or gluing.

4. **Horizontal/global theorem**  
   Persistent bad-flow component $\Rightarrow$ good exit or coherent decomposition certificate.

Target-library completeness may be developed in parallel but does not remove the need for source composition.

Controlling frontier chapter:
[`five-support/frontier-localisation.md`](five-support/frontier-localisation.md).

## 11. Secondary projections

These depend on a five-support solution but do not control its existence.

- orientable good lift $\Rightarrow$ nowhere-zero $\mathbf Z_5$ flow;
- Fano line-field flattening $\Rightarrow$ Tait colouring in the planar setting;
- coefficient holonomy describes transport of affine $\mathbf F_5$ structures;
- tensor/Schur and Fourier/stress complexes provide alternate algebraic projections.

## 12. Assurance axes

No arrow in this map automatically transfers:

- Lean status;
- independent audit;
- peer review;
- novelty or publication status;
- release or DOI status.

Those axes are recorded separately in [`FORMAL_STATUS.md`](FORMAL_STATUS.md).