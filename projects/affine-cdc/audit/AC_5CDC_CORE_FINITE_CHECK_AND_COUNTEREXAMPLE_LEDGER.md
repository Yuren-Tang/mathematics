# AC-5CDC-AUDIT-CORE-01 — finite-check and smallest-configuration ledger

**Fixed candidate:** `1f57422e0e415d8902d56eb294183815c0a0b640`  
**Purpose:** record independently reproduced finite facts and the smallest configurations witnessing proof-interface defects.

## 1. Finite model

Represent each root by a two-subset of `{1,2,3,4,5}`. Addition is symmetric difference. A vector is:

- zero when its support has size `0`;
- a root when its support has size `2`;
- a co-root when its support has size `4`.

The three terminal matchings are

\[
M_0=12|34,\qquad M_1=13|24,\qquad M_2=14|23.
\]

All enumerations below were performed independently from these definitions.

## 2. R2.1 boundary enumeration

### 2.1 Conserved words

Enumerate all ordered quadruples `(r_1,r_2,r_3,r_4)` of the ten roots and retain those with symmetric-difference sum empty.

**Output:** `640` conserved ordered words.

### 2.2 Routing weights

For each support coordinate `a`, form its even terminal trace `S_a`. For route `M_i=X_i|Y_i`, compute

\[
q_i(S_a)=|S_a intersect X_i| mod 2,
\qquad
omega_i=\frac12\sum_a q_i(S_a).
\]

**Output:**

| Triple | Count |
|---|---:|
| `(0,0,0)` | 10 |
| `(0,1,1),(1,0,1),(1,1,0)` | 60 each |
| `(0,2,2),(2,0,2),(2,2,0)` | 30 each |
| `(2,1,1),(1,2,1),(1,1,2)` | 120 each |

### 2.3 Direct and cap profiles

A direct reconnection at `M_i` is admitted iff the two roots in each matching block are equal. A cap at `M_i` is root-valued iff the common block sum is a root.

**Output:**

\[
J_i=\{A,B_i,C_i\},
\]

\[
K_0=\{B_1,B_2,D_1,D_2\},
\]

with the other `K_i` obtained by index permutation. Hence `J_j intersect K_i={B_j}` for `j != i`.

### 2.4 Complementary-support challenges

For every conserved word and every support pair `s` meeting each terminal root in exactly one index, switch the first block of each route by symmetric difference with `s`.

**Output:**

- `1680` labelled challenge instances;
- exactly `16` support-unordered route rows;
- for each fixed route, transition graph `P_3 sqcup C_4 sqcup P_3`;
- the equality and DDD locked rows have exactly one target outside the original cap profile, at the original matching route.

## 3. R2.2 flip enumeration

The local root triangles are the ten three-subsets of `[5]`. Two distinct triangles form a current side iff they meet in two supports. There are `30` unordered current sides. For

\[
T=abc,\qquad U=abd,
\]

the opposite side is `acd,bcd`.

### 3.1 Equality potential

Using the candidate's `nu` and `phi` tables:

- primary `nu` change: `9` negative, `12` zero, `9` positive;
- on the twelve primary-neutral sides: `6` negative secondary changes, `6` positive, `0` ties;
- every primary-negative side has nonpositive secondary change;
- scalar `w_Z=nu+phi+1`: `15` negative, `15` positive, `0` ties.

The independently generated nondecreasing rows coincide exactly with the candidate table.

### 3.2 DDD potential

Using the displayed DDD table and `w_D=omega+1`:

- `15` negative changes;
- `15` positive changes;
- `0` ties.

The independently generated nondecreasing rows coincide exactly with the candidate table.

## 4. R2.3 pairing census

For every conserved ordered four-root word, record the Hamming weights of the three matching-block sums. The complete profile census is:

| Weight triple | Count |
|---|---:|
| permutations of `(2,2,4)` | 120 each |
| permutations of `(0,2,2)` | 60 each |
| permutations of `(0,4,4)` | 30 each |
| `(0,0,0)` | 10 |

Consequences:

1. An inverse-flip zero failure has profile `(0,2,2)`: both crossed topologies are root-valued.
2. An inverse-flip co-root failure has profile `(4,2,2)`: it is a nondegenerate standard atom with two root resolutions.
3. Quadruple equality is `(0,0,0)` and cannot have a current root-valued crossed topology.
4. The inverse-cancellation doubled-disjoint row has profile `(4,0,4)` up to route permutation and is not a standard atom.

## 5. R2.4 Petersen and six-port checks

### 5.1 Standard atoms

For each missing index `i`, the complementary four-set has three perfect matchings. Choosing two distinct endpoint matchings leaves one omitted matching with two disjoint roots. There are

\[
5 times 3=15
\]

unordered standard atoms, in bijection with the fifteen Petersen edges.

### 5.2 Constant-pivot transitions

A pivot root has three Petersen neighbours. Ordered transitions between distinct neighbours therefore number

\[
10 times 3 times 2=60.
\]

All `60` satisfy:

- the emitted side root is the third edge of the complementary triangle;
- the pivot sheet is not root-admissible;
- the nonpivot endpoints are the unique root-admissible pair.

### 5.3 Genuine pivot-change cells

Ordered nonbacktracking four-pivot words number

\[
10 times 3 times 2 times 2=120.
\]

For all `120` words `x-s-t-y`:

\[
z=x+t,\qquad w=s+y
\]

are distinct intersecting roots.

For each six-port word `(s,x,z|w,t,y)`, enumerate the six bijections from the three left ports to the three right ports. Every case has:

- four root-valued star matchings;
- two non-root matchings;
- the two non-root matchings are exactly the two containing the disjoint pair `s--t`.

### 5.4 Petersen simple-cycle check

Independent graph enumeration gives simple cycle lengths and counts:

| Length | Count |
|---:|---:|
| 5 | 12 |
| 6 | 10 |
| 8 | 15 |
| 9 | 20 |

No other simple cycle length occurs.

## 6. Smallest unresolved configurations

These are not counterexamples to the underlying conjecture. They are the smallest configurations for which the candidate does not supply the required proof interface.

### E-MI-1 — doubled-disjoint inverse cancellation

Take

\[
p=12,\qquad q=34,\qquad Q_5=1234.
\]

Raw inverse insertion:

\[
(12,34\mid12,34),
\]

with central value `Q_5`.

The three pairing values are

\[
Q_5,0,Q_5.
\]

Therefore:

- it has no root crossed resolution;
- its endpoint matchings are equal;
- it is not one of the fifteen standard Petersen-edge atoms.

**Defect class:** source-topological / state-alphabet exhaustiveness.  
**Missing proof:** legal bounded borrow and normalization preserving complete data.  
**Downstream impact:** R2.4 and R2.6 begin after excluding this state.

### F-STAR-1 — coefficient star without physical-route theorem

Normalize

\[
s=12,\quad t=34,\quad x=35,\quad y=15,\quad z=45,\quad w=25.
\]

Six ports:

\[
(12,35,45\mid25,34,15).
\]

Forbidden matchings:

\[
(12-34,35-25,45-15)
\]

and

\[
(12-34,35-15,45-25).
\]

The other four are coefficient-valid root stars.

**Defect class:** source-topological / route interface.  
**Missing proof:** a theorem classifying exterior physical composition so that failure of all four root stars implies exactly a route change, separator/category exit, or forced `12--34` continuation.  
**Downstream impact:** the claimed physical Petersen backbone is not established by the finite table alone.

### F-RUN-1 — first nontrivial constant-pivot overlap

Take pivot `s=12` and state sequence

\[
\{12,34\}\to\{12,35\}\to\{12,45\}.
\]

The coefficient section is uniquely

\[
34,35,45.
\]

**Defect class:** source-topological / complete-boundary realization.  
**Missing proof:** an explicit simultaneous source strip showing that the two overlapping transition cells glue on ordered darts and retain all exterior attachments and route data.

### F-BIGON-1 — minimal immediate backtrack

Pivot word:

\[
12\to34\to12.
\]

Forced shore-resolution word:

\[
(34,12,12,34).
\]

**Defect class:** source-topological / diagrammatic filling.  
**Missing proof:** the actual labelled involution/square/pentagon movie and its complete boundary map.  
**Downstream impact:** backtrack deletion and reduced-track extraction are not source-certified.

## 7. Compact reproduction pseudocode

```python
roots = all 2-subsets of range(5)
add(a,b) = symmetric_difference(a,b)

words = [w in roots^4 if add(w[0],w[1],w[2],w[3]) == empty]
assert len(words) == 640

for w in words:
    compute support traces and omega triples
    test direct matching profiles
    test cap block sums
    for every complementary support pair:
        switch one route block and record target states

triangles = all 3-subsets of range(5)
for every adjacent pair T,U with |T intersect U| == 2:
    construct the opposite pair
    compare equality and DDD weight sums

Petersen adjacency = disjointness of roots
for every nonbacktracking path x-s-t-y:
    z = add(x,t)
    w = add(s,y)
    enumerate all six left-right port matchings
```

The numerical outputs above are the results of this independent execution.
