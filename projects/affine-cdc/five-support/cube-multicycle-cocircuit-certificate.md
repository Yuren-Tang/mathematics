# Cube certificate: a cocircuit with disconnected physical projection

## 1. Purpose

Cocircuit minimality does not force the natural physical projection to be one connected graph circuit.  The following exact `IAS` certificate on the cubic cube graph has projection equal to two disjoint four-cycles.

## 2. Data

Order the cube edges as

```text
01, 03, 04, 12, 17, 23, 26, 35, 45, 47, 56, 67.
```

Use the symmetric interlacement matrix `A` with rows

```text
011000000000
100110011100
100110000100
011011011100
011100000000
000100100000
000001010010
010100100000
010100000111
011100001011
000000101101
000000001110
```

and representation

$$
IAS(A)=(I\mid A\mid I+A).
$$

The canonical local transitions in the same edge order are

```text
chi, phi, phi, phi, chi, chi,
phi, chi, psi, psi, psi, psi.
```

Take

$$
y=(0,0,1,0,1,1,1,1,0,0,0,0)
$$

and put `D=y IAS(A)`.

Its nonzero transition pairs are

```text
01 : {chi,psi}
04 : {phi,chi}
17 : {phi,chi}
23 : {phi,chi}
26 : {phi,psi}
35 : {phi,chi}
47 : {chi,psi}
56 : {chi,psi}
```

All other triples are zero, so `|D|=16`.

## 3. Exact minimality check

Enumerating all `2^12-1=4095` nonzero row vectors `u` gives no nonempty support

$$
\operatorname{supp}(u IAS(A))
$$

properly contained in `D`.  Hence `D` is a cocircuit.

The matrix, row, and inclusion test above are a complete finite certificate; no hidden graph generation is required.

## 4. Physical projection

Every active pair contains the canonical local transition.  Therefore

$$
Z(D)
=
\{01,04,17,47\}
\sqcup
\{23,26,35,56\}.
$$

These are the disjoint four-cycles

$$
0-1-7-4-0
$$

and

$$
2-3-5-6-2.
$$

Thus

$$
\boxed{Z(D)\text{ is disconnected}.}
$$

The residual theorem must use the complete cycle--cut response word `(z,a)`, not merely replace `z` by a single circuit.

## 5. Scope

This certificate only disproves the universal single-projected-circuit lemma.  It does not assert that this cube cocircuit occurs in a route-locked AffineCDC endpoint or satisfies the prescribed two-cap residue conditions.
