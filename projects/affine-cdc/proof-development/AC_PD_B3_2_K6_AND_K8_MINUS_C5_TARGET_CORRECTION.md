# AC-PD-B3.2 — verified $K_6$ and $K_8-C_5$ half-cube obstructions

**Proof-development state:** `COMPLETE-DRAFT / PROVENANCE-REPAIR`  
**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Exact initial corpus base:** `main@960c92b7ff231c78b387894149779083060a75eb`  
**Validated controlling packet:** `FIVE_CDC_HALFCUBE_SUBGRAPH_CLASSIFICATION_V1.md` at `research/affine-cdc-five-cdc-v1@dad218dd18ed05d1b7cb730c2dc2431b4db5ec9c`  
**Depends on:** B1.4 target scope; B3.1 validated clique-link theory  
**Immediate consumers:** B3 target hierarchy; B8 certificate classification; B9 factorable-target route  
**External mathematical inputs:** none

## 0. Provenance repair

An earlier version of this dossier correctly proved

$$
K_6\not\to\mathscr A_5,
\qquad
K_8-C_5\not\to\mathscr A_5,
$$

but incorrectly claimed that recovered packets asserted a positive $K_8-C_5$ map, a count of 1920, and a defective witness table. No such controlling packet has been located, and the exact recovered classification already states that $K_8-C_5$ is a forbidden subgraph.

The mathematical no-go proofs below are retained as independent short proofs. The prior positive-certificate provenance claims are withdrawn.

## 1. Clique number of the half-cube

Let $\mathscr A_5$ be the graph on even words in $\mathbf F_2^5$, with adjacency at Hamming distance two.

Translate a clique so that it contains $0$. Every other clique vertex is a two-subset of $[5]$, and two such vertices are adjacent exactly when their two-subsets meet in one point. A pairwise-intersecting family of two-subsets has size at most four: it is either contained in a star, or is the three-edge triangle family. Hence

$$
\boxed{\omega(\mathscr A_5)=5.}
$$

A maximum clique is

$$
\{0,12,13,14,15\}.
$$

Therefore

$$
\boxed{K_6\not\to\mathscr A_5.}
$$

## 2. Triangle common link

Every target triangle is equivalent under translation and coordinate permutation to

$$
T_0=\{0,12,13\}.
$$

Its common neighbours are

$$
14,\qquad15,\qquad23.
$$

The first two are adjacent and the third is isolated. Thus

$$
\boxed{
\mathscr A_5[\Gamma(T)]\cong K_2\sqcup K_1
}
$$

for every triangle $T$.

## 3. The graph $K_8-C_5$

Let the deleted five-cycle use vertices $c_0,\ldots,c_4$, and let $u_0,u_1,u_2$ be the remaining vertices. Then

$$
U=\{u_0,u_1,u_2\}
$$

is a dominating triangle, while the induced graph on the $c_i$ is

$$
K_5-C_5\cong C_5.
$$

### Theorem 3.1

$$
\boxed{K_8-C_5\not\to\mathscr A_5.}
$$

### Proof

A homomorphism would map $U$ injectively to a target triangle $T$. Every $c_i$ is adjacent to every member of $U$, so the remainder would map into

$$
\mathscr A_5[\Gamma(T)]\cong K_2\sqcup K_1.
$$

The connected graph $C_5$ cannot use the isolated vertex, and it cannot map to $K_2$ because it is not bipartite. $\square$

This is exactly the rank-three instance of B3.1's validated capacity theorem:

$$
K_3\vee C_5\not\to\mathscr A_5.
$$

## 4. Exact eight-vertex classification

The controlling recovered packet proves the stronger theorem for every graph $J$ on a fixed eight-element vertex set:

$$
\boxed{
J\to\mathscr A_5
\quad\Longleftrightarrow\quad
K_6\nsubseteq J
\text{ and }
K_8-C_5\nsubseteq J.}
$$

Equivalently, writing $\overline J=K_8-J$,

$$
J\to\mathscr A_5
$$

if and only if $\overline J$ contains at least one of

$$
3K_2,
\qquad
K_3\sqcup K_2,
\qquad
K_4.
$$

Its proof is theorem-level rather than a bare finite witness table: it uses conflict graphs, an eight-vertex graph lemma, and elementary Clebsch-graph parameters. B3.3 therefore classifies this packet as a valid direct finite-target theorem.

## 5. AffineCDC scope

For an eight-colour used-label quotient $J_g$, the theorem gives an exact criterion for maps

$$
J_g\to\mathscr A_5.
$$

This is the global-old-colour-factorable compression route. It does not classify the full dual problem

$$
T_g^{(1)}\to\mathscr A_5,
$$

because different support-cycle components with the same old colour may receive different target values. The B1.4 scope correction remains controlling.

## 6. Completion assessment

`AC-PD-B3.2` is `COMPLETE-DRAFT / PROVENANCE-REPAIR`. The no-go theorems and exact eight-vertex classification are validated; no recovered positive $K_8-C_5$ certificate is superseded by this unit.