#!/usr/bin/env python3
"""Finite certificate for AC-RL-ONE-ATOM-01 local overlap macros.

The proof is human.  This script exhausts the fixed five-leaf coefficient
alphabet used by the source-prefix scheduler:
  * all conserved ordered five-root boundary words;
  * the induced root-topology graph on the 15 labelled five-leaf trees;
  * the singular third-resolution type on every root NNI edge;
  * the directed standard-co-root pentagon rows.

No graph-level recurrence, SCC argument, or generic connectivity claim is made.
"""

from __future__ import annotations

import hashlib
import itertools
import json
from collections import Counter, deque
from typing import FrozenSet, Iterable, Sequence

Root = FrozenSet[int]
Pair = tuple[int, int]
Topology = tuple[Pair, Pair]

ROOTS: tuple[Root, ...] = tuple(
    frozenset(x) for x in itertools.combinations(range(1, 6), 2)
)


def add(*values: Iterable[int]) -> Root:
    out: set[int] = set()
    for value in values:
        out.symmetric_difference_update(value)
    return frozenset(out)


def is_root(value: Root) -> bool:
    return len(value) == 2


def all_topologies() -> tuple[Topology, ...]:
    result: list[Topology] = []
    for singleton in range(5):
        rem = [x for x in range(5) if x != singleton]
        first = rem[0]
        for second in rem[1:]:
            p = tuple(sorted((first, second)))
            rest = [x for x in rem if x not in p]
            q = tuple(sorted(rest))
            topology = tuple(sorted((p, q)))
            if topology not in result:
                result.append(topology)
    assert len(result) == 15
    return tuple(result)


TOPOLOGIES = all_topologies()

# One labelled associahedral pentagon:
# T0=BC|A|DE, T1=AC|B|DE, T2=AC|E|BD,
# T3=AE|C|BD, T4=AE|D|BC.
PENTAGON: tuple[Topology, ...] = (
    ((1, 2), (3, 4)),
    ((0, 2), (3, 4)),
    ((0, 2), (1, 3)),
    ((0, 4), (1, 3)),
    ((0, 4), (1, 2)),
)


def internal_values(word: Sequence[Root], topology: Topology) -> tuple[Root, Root]:
    return tuple(add(word[i], word[j]) for i, j in topology)  # type: ignore[return-value]


def valid(word: Sequence[Root], topology: Topology) -> bool:
    return all(is_root(x) for x in internal_values(word, topology))


def adjacent(a: Topology, b: Topology) -> bool:
    return len(set(a) & set(b)) == 1


def third_resolution(a: Topology, b: Topology) -> Topology:
    common = next(iter(set(a) & set(b)))
    candidates = [t for t in TOPOLOGIES if common in t and t not in (a, b)]
    assert len(candidates) == 1
    return candidates[0]


def singular_type(word: Sequence[Root], a: Topology, b: Topology) -> str:
    third = third_resolution(a, b)
    lengths = sorted(len(x) for x in internal_values(word, third))
    if lengths == [2, 2]:
        return "root"
    if 4 in lengths:
        return "co-root"
    if 0 in lengths:
        return "zero"
    raise AssertionError(lengths)


def cycle_diameter(vertices: list[int], edges: list[tuple[int, int, str]]) -> int:
    graph = {v: set() for v in vertices}
    for u, v, _ in edges:
        graph[u].add(v)
        graph[v].add(u)
    maximum = 0
    for source in vertices:
        distance = {source: 0}
        queue = deque([source])
        while queue:
            u = queue.popleft()
            for v in graph[u]:
                if v not in distance:
                    distance[v] = distance[u] + 1
                    queue.append(v)
        assert len(distance) == len(vertices)
        maximum = max(maximum, max(distance.values()))
    return maximum


def encode_root(root: Root) -> str:
    return "".join(str(x) for x in sorted(root))


def main() -> None:
    conserved = [
        word
        for word in itertools.product(ROOTS, repeat=5)
        if len(add(*word)) == 0
    ]
    assert len(conserved) == 6240

    sector_counts: Counter[str] = Counter()
    pentagon_rows: Counter[str] = Counter()
    canonical_records: list[dict[str, object]] = []
    max_cycle_diameter = 0

    for word in conserved:
        vertices = [i for i, t in enumerate(TOPOLOGIES) if valid(word, t)]
        edges: list[tuple[int, int, str]] = []
        for i, j in itertools.combinations(vertices, 2):
            if adjacent(TOPOLOGIES[i], TOPOLOGIES[j]):
                edges.append((i, j, singular_type(word, TOPOLOGIES[i], TOPOLOGIES[j])))

        edge_types = Counter(kind for _, _, kind in edges)
        if not vertices:
            sector = "empty"
            assert not edges
        elif len(vertices) == 5:
            sector = "C5_all_coroot"
            assert len(edges) == 5 and edge_types == Counter({"co-root": 5})
            max_cycle_diameter = max(max_cycle_diameter, cycle_diameter(vertices, edges))
        elif len(vertices) == 6:
            assert len(edges) == 6
            if edge_types == Counter({"zero": 6}):
                sector = "C6_all_zero"
            else:
                sector = "C6_mixed"
                assert edge_types == Counter({"co-root": 4, "zero": 2})
            max_cycle_diameter = max(max_cycle_diameter, cycle_diameter(vertices, edges))
        else:
            raise AssertionError((len(vertices), edges))
        sector_counts[sector] += 1

        pvalid = [valid(word, t) for t in PENTAGON]
        t0_values = internal_values(word, PENTAGON[0])
        standard_coroot_t0 = (
            sorted(len(x) for x in t0_values) == [2, 4]
            and pvalid[1]
            and not pvalid[0]
        )
        if standard_coroot_t0:
            pattern = "".join("1" if flag else "0" for flag in pvalid)
            pentagon_rows[pattern] += 1

        canonical_records.append(
            {
                "word": [encode_root(x) for x in word],
                "sector": sector,
                "edge_types": sorted(edge_types.items()),
                "pentagon": "".join("1" if flag else "0" for flag in pvalid),
                "standard_coroot_t0": standard_coroot_t0,
            }
        )

    assert sector_counts == Counter(
        {
            "empty": 600,
            "C5_all_coroot": 1440,
            "C6_all_zero": 600,
            "C6_mixed": 3600,
        }
    )
    assert pentagon_rows == Counter(
        {
            "01000": 360,
            "01100": 120,
            "01110": 240,
        }
    )
    assert max_cycle_diameter == 3

    payload = {
        "schema": "AC-RL-ONE-ATOM-01-five-leaf-overlap-v1",
        "root_count": len(ROOTS),
        "topology_count": len(TOPOLOGIES),
        "conserved_word_count": len(conserved),
        "sector_counts": dict(sorted(sector_counts.items())),
        "directed_standard_coroot_pentagon_rows": dict(sorted(pentagon_rows.items())),
        "max_root_cycle_diameter": max_cycle_diameter,
        "records": canonical_records,
    }
    digest = hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()

    summary = dict(payload)
    summary.pop("records")
    summary["canonical_digest"] = digest
    print(json.dumps(summary, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
