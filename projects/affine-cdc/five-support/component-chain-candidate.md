# Fixed-channel component-chain — failed general theorem and retained local core

## 1. Exact sources and verdict

Authorial source:

`research/affine-cdc-five-cdc-v1@02b37476198e9eaa2b4cd8d2a2edd76782bdcd49`.

PDL reconstruction:

`proof-development/affine-cdc-rigour-v1@e36ba22f09e3a9fc6358f3b03615f8fde6c00d96`.

Independent audit:

`audit/affine-cdc-component-chain-v1@a4f20f05532c307a3a8f9d98ac4c5162e7b8ad57`.

Verdict:

`GENERAL COMPONENT-CHAIN THEOREM FAILED / MATERIAL FALSE SCOPE`.

The theorem and its PDL reconstruction remain exact failed candidates and repair provenance. They are not active universal proof components.

## 2. Retained independently verified local mathematics

The audit independently verified:

- $H_h$-degree is zero or two at every support triangle;
- the unique inactive triangle is $I_h=[5]\setminus h$;
- all six canonical active/inactive root-NNI rows;
- all twenty-four ordered inactive-continuation configurations;
- all six distinct active/active rows;
- all nine equal-endpoint root branch swaps, separated from the zero pairing;
- all eighty-four ordered final-terminal configurations: forty-two reach each crossed matching and none preserve the old matching;
- the explicit co-root `6-7` route-changing movie;
- the exact zero-parent Heawood `H_35` movie.

These are Tier-I local tables and models. They do not imply universal chain totality.

Local-row digest:

`75ed977851a944f2cd80577e629a2f6936da5dfce49ad9d5a9e0e82c8b2494d4`.

Aggregate recomputation digest:

`2353b22b111c9dd47319b2c14637c08d93ae2f4eac10605a00f29c5f46842fe8`.

## 3. The failed statement

The written theorem chooses two distinguished terminal path components $P_0,P_1$ and a shortest witnessed quotient path between them. Its proof handles an internal node only when that node is:

- one inactive singleton; or
- one closed channel component.

It does not require $P_0,P_1$ to be the only terminal path components. A third terminal path may therefore occur internally, outside both proof cases.

## 4. Exact counterexample

The audit gives a complete labelled Heawood carrier:

```text
h=14
cut channel edges: 1-14:13, 10-11:12, 13-14:12

P_0={1,2,3,4,5,6,11}
X_1={7,8,9,10,12,13}
P_1={14}

shortest quotient chain:
P_0 -- 3-8:14 -- X_1 -- 9-14:23 -- P_1.
```

Here $X_1$ is a third terminal path.

At the first connector the root NNI is

```text
134+124 -> 234+123, central 14 -> 23
retain 2-3@3, 8-9@8
move 7-8@8 -> 3, 3-4@3 -> 8.
```

The original $P_0$ terminal darts are split between two $H_{14}$ components, so no inherited $P_0'$ exists. The claimed retained path rank is destroyed.

Enumeration:

```text
18 non-cut central edges
36 labelled root-NNI movies
36 category-safe outputs
0 inherited length-1 chains between the original P_0 and P_1 terminal pairs.
```

Counterexample digest:

`d24c63ab56320803b9c795ac08389674b6f67edf89dc5c4ef9a729c5436a3e61`.

## 5. Consequences for the corollaries

### Co-root

The `Xi` same-arc counterexample remains permanent. The local two-arc arithmetic and the explicit `6-7` movie pass bounded independent checks. No universal co-root return follows because terminal-component exhaustion was not proved.

### Zero parent

The exact Heawood `H_35` model and its crossed-matching/switch/parent-NNI interface pass bounded checks. No universal zero-parent return follows from one model.

### Induction

The complete inverse-parent table and ordinary induction remain blocked because both singular universal rows depended on the failed general theorem.

## 6. Active replacement obligation

`AC-FRONTIER-COMPONENT-CHAIN-TERMINAL-EXHAUSTION` asks for one of:

1. prove that every application carrier has exactly two terminal paths and all other nontrivial channel components are closed;
2. generalize the contraction theorem to internal terminal paths while preserving the distinguished terminal darts and paths;
3. replace the chain mechanism by another literal source-faithful return.

Every repair must retain the exact third-terminal-path witness and receive a new independent audit.

## 7. Permanent inference guard

The following implication is forbidden:

```text
two distinguished terminal paths
⇒ the internal nodes of a shortest chain are only inactive singletons or closed cycles.
```

Physical connector labels and correct local root arithmetic do not repair a missing global terminal-component hypothesis.