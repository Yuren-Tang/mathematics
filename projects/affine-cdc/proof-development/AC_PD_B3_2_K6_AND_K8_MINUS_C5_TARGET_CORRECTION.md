# AC-PD-B3.2 — corrected $K_6$ and $K_8-C_5$ half-cube target theorems

**Proof-development state:** `COMPLETE-DRAFT / MATHEMATICAL-CORRECTION`  
**Owner:** `AffineCDC — Proof Development Lead` (`AC-PDL`)  
**Exact initial corpus base:** `main@960c92b7ff231c78b387894149779083060a75eb`  
**Affected recovered packets:** `FIVE_CDC_K6_TARGET_NO_GO_V1.md`, `FIVE_CDC_K8_C5_TARGET_CLOSURE_V1.md`, and the displayed-table erratum inherited by the surface packet at `research/affine-cdc-five-cdc-v1@dad218dd18ed05d1b7cb730c2dc2431b4db5ec9c`  
**Depends on:** B1.4 target scope; B3.1 corrected common-link and dominating-clique theorems  
**Immediate consumers:** B3 target hierarchy; B8 certificate classification; B9 factorable-target route  
**External mathematical inputs:** none

## 0. Correction summary

The direct $K_6$ no-go for the five-coordinate half-cube is valid. The claimed positive result

$$
K_8-C_5\to\mathscr A_5
$$

is false.

In fact every target triangle has common-link graph

$$
K_2\sqcup K_1.
$$

The source graph $K_8-C_5$ has a universal triangle whose complement induces another $C_5$. Any homomorphism would therefore restrict to

$$
C_5\to K_2\sqcup K_1,
$$

which is impossible. Hence the correct raw homomorphism count is zero, not 1920.

The published corrected witness table in the recovered packet is not a homomorphism: one displayed required edge already maps to two target words at Hamming distance four.

## 1. The target half-cube

Let

$$
E_5=
\left\{x\in\mathbf F_2^5:\sum_i x_i=0\right\}
$$

and let $\mathscr A_5$ have vertex set $E_5$, with

$$
x\sim y
\quad\Longleftrightarrow\quad
\operatorname{wt}(x+y)=2.
$$

Translation by an even word and permutation of the five coordinates are graph automorphisms.

## 2. Clique number

Translate any clique so that it contains $0$. Every other clique vertex is then a weight-two word, identified with a two-subset of $[5]$. Two such vertices are adjacent exactly when their two-subsets meet in one point.

### Lemma 2.1

A pairwise-intersecting family of two-subsets of $[5]$ has cardinality at most four.

### Proof

If all pairs contain one common point, there are at most four. Otherwise choose two members $\{1,2\}$ and $\{1,3\}$ and a member not containing $1$. To meet both, it must be $\{2,3\}$. Any further pair must meet all three edges of this triangle and is therefore one of them. Thus the family has cardinality at most three in the non-star case. $\square$

### Corollary 2.2

$$
\omega(\mathscr A_5)=5.
$$

### Proof

The lemma gives at most four nonzero vertices after translation, hence clique size at most five. Equality is attained by

$$
\{0,
\varepsilon_1+arepsilon_2,
\varepsilon_1+arepsilon_3,
\varepsilon_1+arepsilon_4,
\varepsilon_1+arepsilon_5\}.
$$

$\square$

Therefore no homomorphism $K_6\to\mathscr A_5$ exists. Since a homomorphism from a complete loopless graph is injective on vertices, this is simultaneously the embedding no-go.

## 3. Transitivity and normal form of target triangles

Let $T=\{x_0,x_1,x_2\}$ be a target triangle. Translate by $x_0$, so the other two vertices are weight-two words $a,b$ with $\operatorname{wt}(a+b)=2$. Their two-subsets meet in exactly one coordinate. A coordinate permutation therefore sends the triangle to

$$
T_0=
\{00000,11000,10100\}.
$$

Thus every target triangle lies in one orbit under the affine coordinate automorphism group.

## 4. Exact common link of a triangle

A common neighbour of $T_0$ must be a weight-two word $y$, corresponding to a two-subset $Y\subseteq[5]$, such that

$$
|Y\cap\{1,2\}|=1,
\qquad
|Y\cap\{1,3\}|=1.
$$

The only possibilities are

$$
\{2,3\},
\qquad
\{1,4\},
\qquad
\{1,5\}.
$$

In word notation:

$$
01100,
\qquad
10010,
\qquad
10001.
$$

The last two are adjacent because their symmetric difference is $\{4,5\}$; the first is adjacent to neither because each symmetric difference has size four.

### Theorem 4.1

For every triangle $T$ of $\mathscr A_5$,

$$
\boxed{
\mathscr A_5[\Gamma(T)]\cong K_2\sqcup K_1.}
$$

### Proof

The calculation proves the result for $T_0$, and triangle transitivity transfers it to every $T$. $\square$

This is the exact common-link structure required by B3.1.

## 5. Source structure of $K_8-C_5$

Let

$$
J=K_8-C_5,
$$

where the removed five-cycle lies on vertices $c_0,\dots,c_4$. Let $u_0,u_1,u_2$ be the other three vertices.

Then:

1. $U=\{u_0,u_1,u_2\}$ induces a triangle;
2. every $c_i$ is adjacent to every $u_j$, so $U$ is a dominating clique;
3. the induced graph on the $c_i$ is
   $$
   K_5-C_5\cong C_5.
   $$

The last isomorphism holds because the complement of a five-cycle on five vertices is another five-cycle.

## 6. No homomorphism theorem

### Theorem 6.1

$$
\boxed{
K_8-C_5\not\to\mathscr A_5.}
$$

### Proof

Suppose $\phi:J\to\mathscr A_5$. The source triangle $U$ maps injectively to a target triangle $T$. Every vertex of $J-U$ is adjacent to all of $U$, so B3.1 gives a restricted homomorphism

$$
J-U\cong C_5
\longrightarrow
\mathscr A_5[\Gamma(T)]
\cong K_2\sqcup K_1.
$$

No vertex of the connected graph $C_5$ can map to the isolated target vertex: each source vertex has neighbours and the isolated target has none. Hence the image lies in $K_2$. This would be a proper two-colouring of the odd cycle $C_5$, impossible. $\square$

### Corollary 6.2

The raw homomorphism count is zero. In particular there are no injective homomorphisms and no target-automorphism orbits of homomorphisms.

## 7. Explicit failure of the recovered witness

The recovered corrected table includes

$$
\phi(u_2)=10100,
\qquad
\phi(c_1)=01001.
$$

The source vertices $u_2$ and $c_1$ are adjacent, but

$$
10100+01001=11101
$$

has Hamming weight four. Therefore their target images are not adjacent in $\mathscr A_5$.

Thus the table is not a graph homomorphism. The claimed count 1920 and one-orbit classification cannot be retained as certificate facts.

## 8. Correct status of the two recovered packets

### `FIVE_CDC_K6_TARGET_NO_GO_V1.md`

- the $K_6$ no-homomorphism/no-embedding theorem is correct;
- the subsequent displayed $K_8-C_5$ homomorphism witness is false;
- the packet is therefore only partially valid and must be split or superseded.

### `FIVE_CDC_K8_C5_TARGET_CLOSURE_V1.md`

- the claimed exact enumeration is false;
- the raw count, injective count, orbit count, and representative table must all be withdrawn;
- its scope distinction between quotient and full dual remains conceptually correct, but the asserted quotient map does not exist.

## 9. Consequence for the factorable target route

If an old-colour quotient is isomorphic to $K_8-C_5$, then

$$
J_g\not\to\mathscr A_5.
$$

Hence the old-colour-factorable compression route fails for that quotient.

By B1.4, this does **not** imply

$$
T_g^{(1)}\not\to\mathscr A_5.
$$

A full-dual map may distinguish different support-cycle components with the same old colour. No conclusion about the full dual follows without an independent theorem or certificate.

## 10. Certificate methodology correction

A finite homomorphism packet should record at least:

1. exact source and target adjacency conventions;
2. whether nonedges are constrained;
3. a machine-checkable witness whose every required source edge maps to a target edge;
4. raw and orbit counts independently recomputable from the same code;
5. the automorphism group action used for orbit reduction;
6. hashes of code and output;
7. a manual spot-check of load-bearing witness edges.

The recovered positive packet failed item 3 and therefore cannot support any count or orbit conclusion.

## 11. Curator correction requirement

Before B3 target material is promoted:

1. retain the direct $K_6$ no-go with the clique-number proof;
2. remove the false $K_8-C_5$ positive homomorphism, count, orbit, and table;
3. install Theorems 4.1 and 6.1;
4. mark the affected positive packet `SUPERSEDED / FALSE CERTIFICATE`;
5. correct every downstream mention of 1920 maps or one orbit;
6. retain the quotient/full-dual scope warning;
7. re-run any computation pipeline that used the false witness as a seed or regression test.

## 12. Completion assessment

`AC-PD-B3.2` is `COMPLETE-DRAFT / MATHEMATICAL-CORRECTION`. The next active unit is B3.3: audit the remaining target-capacity, marked-core, and dominating-clique finite packets against the corrected common-link theorem, separating direct valid no-go proofs from computations requiring regeneration.