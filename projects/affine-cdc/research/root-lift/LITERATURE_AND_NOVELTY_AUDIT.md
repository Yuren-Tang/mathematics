# Current literature and novelty audit

## 1. Audit date, method, and limitation

Search date: **2026-07-23**.

The audit searched publisher records, DOI metadata, arXiv, and broad web indexes using combinations of:

- directed/orientable cycle double cover;
- orientable circuit double cover and graph embedding;
- group-valued, integral, signed, and bidirected graph flows;
- type-$A$ roots $\varepsilon_i-\varepsilon_j$, flow polytopes, and Kostant partition functions;
- deleted and fully deleted permutation modules;
- root-valued graph flow, indexed support flow, and prescribed-witness sign lift.

This was a serious bounded search, not a priority-grade exhaustive bibliography. Subscription-only MathSciNet/zbMATH citation graphs, unpublished manuscripts, and terminology not discoverable by the chosen queries may contain closer precedents. Therefore “no exact source located” below is not a claim of novelty or priority.

## 2. Directed and orientable cycle double covers

The directed cycle double cover object is established literature. In the standard formulation, every edge is covered twice with opposite directions.

Key sources:

1. F. Jaeger, “A Survey of the Cycle Double Cover Conjecture,” *North-Holland Mathematics Studies* **115** (1985), 1–12. DOI: `10.1016/S0304-0208(08)72993-1`.
2. A. Jiménez and M. Loebl, “Directed Cycle Double Cover Conjecture: Fork Graphs,” arXiv:`1310.5539`.
3. A. Jiménez and M. Loebl, “Directed cycle double covers and cut-obstacles,” arXiv:`1405.6929`.
4. M. N. Ellingham and X. Zha, “Orientable embeddings and orientable cycle double covers of projective-planar graphs,” *European Journal of Combinatorics* **32** (2011), 495–509. DOI: `10.1016/j.ejc.2011.01.001`; arXiv:`0911.2713`.

The cubic embedding equivalence—directed/orientable cycle double covers versus suitable orientable cellular embeddings—is therefore not new in substance.

Recent adjacent work located by the audit includes:

5. B. Ghanbari and R. Šámal, “Facial diagrams and cycle double cover,” arXiv:`2605.01410`, studying edge twists of cellular embeddings.
6. M. Weiß, R. Akpanya, and A. C. Niemeyer, “On 3-Connected Planar Graphs with Unique Orientable Circuit Double Covers,” arXiv:`2601.10171`.

These confirm that orientable embeddings, circuit-double-cover witnesses, twists, and uniqueness remain active subjects. No source found in this search used the present general $A_{q-1}$ indexed-root packaging.

## 3. Group-valued and integral flows

Kirchhoff flows with values in abelian groups are classical.

7. W. T. Tutte, “A Contribution to the Theory of Chromatic Polynomials,” *Canadian Journal of Mathematics* **6** (1954), 80–91. DOI: `10.4153/CJM-1954-010-9`.

Integral and signed/bidirected flow theories already provide mature frameworks for edge signs and half-edge orientations:

8. A. Bouchet, “Nowhere-zero integral flows on a bidirected graph,” *Journal of Combinatorial Theory, Series B* **34** (1983), 279–292. DOI: `10.1016/0095-8956(83)90041-2`.
9. A. Khelladi, “Nowhere-zero integral chains and flows in bidirected graphs,” *Journal of Combinatorial Theory, Series B* **43** (1987), 95–115. DOI: `10.1016/0095-8956(87)90032-3`.
10. M. DeVos, “Flows on Bidirected Graphs,” arXiv:`1310.8406`.
11. M. Beck and T. Zaslavsky, “The Number of Nowhere-Zero Flows on Graphs and Signed Graphs,” *Journal of Combinatorial Theory, Series B* **96** (2006), 901–918; arXiv:`math/0309331`.

These theories are relevant analogues, but they do not by themselves identify an edge value with two support indices and require the two coordinate uses to be opposite. The present object is an ordinary source-graph flow whose **target values** are type-$A$ roots; it is not merely a flow on a signed source graph.

## 4. Type-$A$ roots and network flows

The identification of a directed target edge $j\to i$ with the type-$A$ root

$$
\varepsilon_i-\varepsilon_j
$$

is standard in the literature on root polytopes, flow polytopes, and Kostant partition functions.

12. W. Baldoni and M. Vergne, “Kostant partition functions and flow polytopes,” *Transformation Groups* **13** (2008), 447–469. DOI: `10.1007/s00031-008-9019-8`.
13. K. Mészáros and A. H. Morales, “Flow Polytopes of Signed Graphs and the Kostant Partition Function,” *International Mathematics Research Notices* **2015** (2015), 830–871. DOI: `10.1093/imrn/rnt212`; arXiv:`1208.0140`.
14. K. Rietsch and L. Williams, “Root polytopes, flow polytopes, and order polytopes,” arXiv:`2406.15803`.

This literature generally places type-$A$ roots on the **edges of a target or network graph** and studies nonnegative scalar flows, netflow vectors, polytopes, or enumeration. The present correspondence instead places one root value on each edge of an arbitrary source graph and imposes source Kirchhoff conservation. The algebraic verification is elementary coordinatewise, so the correspondence should be described as a natural synthesis or repackaging unless a stronger literature search establishes otherwise.

## 5. Circuit decomposition

The fact that a finite balanced directed edge set decomposes into directed circuits is classical network-flow theory, often traced to Gallai’s 1958 network-flow work:

15. T. Gallai, “Maximum-Minimum Sätze über Graphen,” *Acta Mathematica Academiae Scientiarum Hungaricae* **9** (1958). DOI: `10.1007/BF02020271`.

Modern flow-decomposition theorems explicitly note that decompositions need not be unique. The four-parallel-edge example in the definitions dossier is an exact elementary witness of that nonuniqueness.

Therefore the step

$$
\text{directed Eulerian support}\Rightarrow\text{some circuit decomposition}
$$

is known, while a claim of canonical recovery of a prescribed full witness is false.

## 6. Deleted permutation and orthogonal modules

The deleted permutation module

$$
E_I=\ker\left(\mathbf F_2^I\to\mathbf F_2\right)
$$

and, when $q$ is even, the fully deleted quotient

$$
E_I/\langle\mathbf1_I\rangle
$$

are standard representation-theoretic objects. The radical calculation and dimensions $q-1$ or $q-2$ are immediate linear algebra.

The project’s quadratic form

$$
q([z])=\operatorname{wt}(z)/2\pmod2
$$

and the identification of the weight-two classes as anisotropic roots give:

- $q=5$: the four-dimensional minus space $O^-(4,2)$;
- $q=8$: the six-dimensional plus space $O^+(6,2)$.

The audit found no reason to treat these finite-dimensional identifications themselves as novel. Their use as a **universal unordered-support target**, and the sharp correction from a false $2r$ tower to dimension $q-2$, belongs to the existing AffineCDC project package and was not independently re-audited here.

## 7. Prescribed-witness sign obstruction

For a fixed full circuit witness, the occurrence-adjacency graph construction gives a cochain

$$
t_{\mathcal W}\in C^1(H_{\mathcal W};\mathbf F_2)
$$

and the exact criterion

$$
[t_{\mathcal W}]=0
\quad\text{in}\quad
C^1(H_{\mathcal W})/\operatorname{Cut}(H_{\mathcal W}).
$$

This is elementary signed-graph/cellular-orientability linear algebra: preliminary circuit orientations are vertex signs, and reversing one circuit adds a cut. Its substance is close to standard orientability tests for face systems and signed graphs. No priority or deep novelty claim is warranted for the cut criterion by itself.

What appears project-specific is the explicit four-level separation:

1. full circuit occurrences;
2. directed support words;
3. unordered root/support data;
4. family-level quotients such as $\Omega_f$;

and the warning that their obstruction classes live on different graphs and have different gauges.

No exact prior source was located that simultaneously states this hierarchy for indexed $q$-CDC witnesses and compares it to an affine-lift torsor.

## 8. $q=5$ literature position

The binary equivalences

$$
R_5\text{ flow}
\leftrightarrow
K_5\text{ triangle labels}
\leftrightarrow
O^-(4,2)\text{ anisotropic flow}
$$

are finite linear algebra and already belong to the frozen AffineCDC corpus. The quadratic, Schur, cographic, stress, and Fourier formulations concern binary/unordered witness existence or counting.

The additional integral statement

$$
A_4\text{ root flow}
\to
\mathbf F_5\text{ nowhere-zero flow}
$$

requires a global bijection of support indices with $\mathbf F_5$ and is an immediate homomorphic projection. The converse is a nontrivial fixed-data lift problem, not a standard equivalence found in the searched literature.

No exact paper was located that identifies oriented five-support CDCs with $A_4$ root flows or separates global affine coefficient transport from local charts and support-label holonomy. This is a candidate for useful exposition, not yet a novelty claim.

## 9. $q=8$ literature position

The exceptional binary module

$$
E_8/\langle\mathbf1\rangle\cong O^+(6,2)
$$

and the affine quotient

$$
\{a,b\}\longmapsto a+b\in\mathbf F_2^3\setminus\{0\}
$$

are standard finite-geometry constructions. The inherited AffineCDC contribution is the compatible-lift torsor and its gauge code above a fixed Fano flow.

The new scout synthesis is the commutative hierarchy

$$
A_7\text{ sign lift}
\to
E_8\text{ unordered root lift}
\to
O^+(6,2)
\to
\mathbf F_2^3\text{ Fano flow},
$$

with explicit nonconverses and the comparison to $\omega(g)$ and $\Omega_f$.

No exact prior source was located for that whole hierarchy. Its final two obstruction identifications inherit the frozen OR1 assurance and must not be advertised as independently verified by this scout.

## 10. Novelty classification table

| Item | Literature classification | Scout classification |
|---|---|---|
| directed/orientable CDC definition | established | known |
| orientable embedding interpretation | established | known |
| group-valued Kirchhoff flow | classical | known |
| signed/bidirected flow frameworks | established | adjacent, not identical |
| directed Eulerian circuit decomposition | classical | known |
| type-$A$ roots as directed complete-graph incidence vectors | established | known |
| directed indexed supports $\leftrightarrow A_{q-1}$ root flow | no exact CDC source located; elementary coordinate synthesis | useful reformulation, not priority claim |
| full witness canonically equivalent to root flow | contradicted by decomposition nonuniqueness | false / scope correction |
| prescribed full-witness cut obstruction | standard-type sign/cut argument | theorem packaging, low novelty |
| four-level witness hierarchy | no exact source located | potentially useful project-specific organization |
| $q=5$ integral/binary/scalar hierarchy | no exact combined source located | theorem candidate / exposition candidate |
| $q=8$ integral/orthogonal/Fano/OR1 hierarchy | no exact combined source located | theorem candidate, OR1-dependent at final layer |
| universal sign-lift or $\Omega_f$ vanishing | no proof located | genuinely open in present project |

## 11. Claims that must not be made

The literature audit does **not** support any of the following:

- “root flows are a newly discovered class of graph flows”;
- “the type-$A$ encoding itself is novel”;
- “mod-$2$ orthogonal models retain orientation signs”;
- “every unordered root flow has a prescribed-witness sign lift”;
- “every nowhere-zero five-flow is equivalent to an oriented five-support witness”;
- “Fano compatibility forces orientability”;
- “the present search proves priority or absence of prior art”;
- “the OR1 candidate has passed independent audit.”

## 12. Recommended citation posture

A future paper may safely present the generic correspondence as:

> a direct type-$A$ root-lattice reformulation of directed indexed Eulerian support systems, followed by a noncanonical classical circuit decomposition.

It should cite:

- Jaeger and later directed-CDC literature for the oriented object;
- Tutte for group-valued flows;
- Gallai or a standard network-flow source for decomposition;
- root/flow-polytope literature for $\varepsilon_i-\varepsilon_j$ as directed type-$A$ roots;
- signed/bidirected-flow literature as a nearby but distinct sign framework.

Any stronger novelty language should await a specialist bibliography and an independent mathematical audit of the final theorem package.
