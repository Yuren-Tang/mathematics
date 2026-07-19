# A K6-free obstruction to half-cube homomorphism

**Programme:** `AffineCDC — Research Lead`  
**Status:** theorem-level graph-homomorphism warning; not a compatible-triangulation obstruction theorem  
**Parents:** `FIVE_CDC_COMPONENTWISE_DUAL_CENSUS_V1.md`, `FIVE_CDC_COLORED_SURFACE_DUAL_HALFCUBE_V1.md`

## 1. Purpose

The corrected componentwise census around the thirty-vertex fixed-Fano obstruction found that every residual bad dual triangulation contains a `K_6`. This packet records a sharp warning against promoting that local observation to a general graph-homomorphism theorem.

Let `\mathscr A_5` denote the even half-cube: its vertices are the even words in `\mathbf F_2^5`, and two words are adjacent when their Hamming distance is two.

## 2. The Mycielski graph of K5

Let `M(K_5)` have:

- original clique vertices `v_1,\ldots,v_5`;
- shadow vertices `u_1,\ldots,u_5`;
- one apex `w`.

Its edges are:

- all `v_iv_j` with `i\ne j`;
- `u_iv_j` whenever `i\ne j`;
- all `wu_i`.

The shadow vertices are mutually nonadjacent.

### Proposition 2.1

\[
\omega(M(K_5))=5.
\]

In particular `M(K_5)` is `K_6`-free.

#### Proof

The original vertices form a `K_5`. A clique containing the apex contains at most one shadow and no original vertex adjacent through the apex, hence has size at most two. A clique containing a shadow `u_i` but not the apex may use at most the four original vertices `v_j` with `j\ne i`, so has size at most five. ∎

## 3. K5 cliques in the half-cube

### Lemma 3.1

Every `K_5` in `\mathscr A_5` is, after translating all words by one target word and permuting coordinates, equal to

\[
Q=\{0,12,13,14,15\},
\]

where `ij` denotes `e_i+e_j`.

#### Proof

Translate one clique vertex to zero. The other four vertices are weight-two words, and pairwise distance two means that the corresponding two-subsets of a five-set are pairwise intersecting. Four pairwise-intersecting two-subsets cannot be the three edges of a triangle, so they share one common coordinate. Permute coordinates to obtain the displayed star. ∎

### Lemma 3.2

For every `q\in Q`, the unique target vertex adjacent to all four vertices of `Q-\{q\}` is `q` itself.

#### Proof

For `q=0`, a direct weight check shows that the only even word at distance two from each of `12,13,14,15` is zero. For `q=1i`, translate by `q` and permute the remaining four coordinates; this reduces to the preceding case. ∎

## 4. The obstruction theorem

### Theorem 4.1

\[
\boxed{M(K_5)\not\longrightarrow\mathscr A_5.}
\]

#### Proof

Assume a homomorphism exists. The original `K_5` must map injectively to a target `K_5`; normalize its image to

\[
Q=\{q_1,\ldots,q_5\}.
\]

The shadow `u_i` is adjacent to the four original vertices other than `v_i`. By Lemma 3.2 its image is forced to be `q_i`. Hence the five shadows map onto the same target `K_5`.

The apex `w` is adjacent to every shadow, so its image would have to be adjacent to all five vertices of `Q`. Together with `Q` this would form a `K_6` in `\mathscr A_5`, contradicting `\omega(\mathscr A_5)=5`. ∎

## 5. Strategic scope

This theorem shows that

\[
K_6\nsubseteq H
\]

is not sufficient for an arbitrary graph `H` to map to `\mathscr A_5`.

It does **not** yet provide a compatible closed dual triangulation with the same property. The current AffineCDC evidence therefore separates into two levels:

1. in the complete connected-cycle neighbourhood of the thirty-vertex certificate, every residual compatible dual obstruction contains `K_6`;
2. in general graph-homomorphism theory, deeper `K_6`-free obstructions already exist.

The next programme must therefore pursue both:

- admissible partial-Petrial surgery on visible `K_6` cliques;
- a search or structural theorem for compatible `K_6`-free dual triangulations that still fail to map to `\mathscr A_5`.

No claim here proves that such a compatible triangulation exists, or that `M(K_5)` itself occurs as a dual triangulation in the current root-lift class.