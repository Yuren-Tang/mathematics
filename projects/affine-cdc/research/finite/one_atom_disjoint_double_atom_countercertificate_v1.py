#!/usr/bin/env python3
"""Exact certificate for the disjoint-prefix double-atom obstruction.

Standard library only.  It reconstructs the labelled Heawood state, performs
the 25-cycle switch, checks the unique standard Q4 atom, applies the literal
stored root NNI at 5-6, and verifies that the output has two disjoint Q4 atoms
while remaining category-safe.
"""

from __future__ import annotations

import hashlib
import itertools
import json
from collections import deque
from typing import Iterable

Vertex = int
Edge = tuple[int, int]
Value = frozenset[int]


def edge(u: int, v: int) -> Edge:
    return (u, v) if u < v else (v, u)


def value(text: str) -> Value:
    return frozenset(int(ch) for ch in text)


def show(x: Value) -> str:
    return "0" if not x else "".join(str(i) for i in sorted(x))


def add(*xs: Iterable[int]) -> Value:
    out: set[int] = set()
    for x in xs:
        out.symmetric_difference_update(x)
    return frozenset(out)


BASE_DATA = [
    (1, 2, "23"), (1, 6, "12"), (1, 14, "13"),
    (2, 3, "34"), (2, 11, "24"), (3, 4, "13"),
    (3, 8, "14"), (4, 5, "12"), (4, 13, "23"),
    (5, 6, "13"), (5, 10, "23"), (6, 7, "23"),
    (7, 8, "24"), (7, 12, "34"), (8, 9, "12"),
    (9, 10, "13"), (9, 14, "23"), (10, 11, "12"),
    (11, 12, "14"), (12, 13, "13"), (13, 14, "12"),
]

BASE_EDGES = {edge(u, v) for u, v, _ in BASE_DATA}
BASE_LABELS = {edge(u, v): value(s) for u, v, s in BASE_DATA}
VERTICES = set(range(1, 15))
SWITCH_CYCLE = (1, 2, 11, 10, 5, 4, 13, 14)
SWITCH_ROOT = value("25")


def adjacency(edges: set[Edge]) -> dict[Vertex, set[Vertex]]:
    adj = {v: set() for v in VERTICES}
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    return adj


def components(edges: set[Edge]) -> list[set[Vertex]]:
    adj = adjacency(edges)
    unseen = set(VERTICES)
    result: list[set[Vertex]] = []
    while unseen:
        start = min(unseen)
        comp = {start}
        queue = deque([start])
        unseen.remove(start)
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if v in unseen:
                    unseen.remove(v)
                    comp.add(v)
                    queue.append(v)
        result.append(comp)
    return result


def connected(edges: set[Edge]) -> bool:
    return len(components(edges)) == 1


def bridge_count(edges: set[Edge]) -> int:
    return sum(not connected(edges - {e}) for e in edges)


def girth(edges: set[Edge]) -> int:
    adj = adjacency(edges)
    best = 10**9
    for start in VERTICES:
        dist = {start: 0}
        parent = {start: None}
        queue = deque([start])
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if v not in dist:
                    dist[v] = dist[u] + 1
                    parent[v] = u
                    queue.append(v)
                elif parent[u] != v:
                    best = min(best, dist[u] + dist[v] + 1)
    return best


def component_has_cycle(edges: set[Edge], vertices: set[Vertex]) -> bool:
    internal = sum(u in vertices and v in vertices for u, v in edges)
    return internal >= len(vertices)


def cyclic_edge_connectivity(edges: set[Edge], maximum: int = 7) -> int:
    ordered = sorted(edges)
    for size in range(1, maximum + 1):
        for cut in itertools.combinations(ordered, size):
            remaining = edges - set(cut)
            comps = components(remaining)
            cyclic = [c for c in comps if component_has_cycle(remaining, c)]
            if len(cyclic) >= 2:
                return size
    raise AssertionError("cyclic cut not found in requested range")


def verify_graph(edges: set[Edge], expected_girth: int, expected_cyclic: int) -> dict[str, object]:
    adj = adjacency(edges)
    assert len(edges) == 21
    assert all(len(adj[v]) == 3 for v in VERTICES)
    assert connected(edges)
    assert bridge_count(edges) == 0
    assert girth(edges) == expected_girth
    assert cyclic_edge_connectivity(edges) == expected_cyclic
    return {
        "connected": True,
        "simple": True,
        "cubic": True,
        "bridges": 0,
        "girth": expected_girth,
        "cyclic_edge_connectivity": expected_cyclic,
    }


def verify_conservation(edges: set[Edge], labels: dict[Edge, Value]) -> None:
    adj = adjacency(edges)
    for u in VERTICES:
        incident = [labels[edge(u, v)] for v in adj[u]]
        assert add(*incident) == frozenset(), (u, list(map(show, incident)))


def switch_cycle(labels: dict[Edge, Value]) -> dict[Edge, Value]:
    result = dict(labels)
    for i, u in enumerate(SWITCH_CYCLE):
        v = SWITCH_CYCLE[(i + 1) % len(SWITCH_CYCLE)]
        e = edge(u, v)
        result[e] = add(result[e], SWITCH_ROOT)
    return result


def apply_literal_source_nni(edges: set[Edge], labels: dict[Edge, Value]) -> tuple[set[Edge], dict[Edge, Value]]:
    # Central stable edge 5-6 is retained.  Stable edges 6-7 and 5-10 move.
    out_edges = set(edges)
    out_edges.remove(edge(6, 7))
    out_edges.remove(edge(5, 10))
    out_edges.add(edge(5, 7))
    out_edges.add(edge(6, 10))

    out_labels = dict(labels)
    root_67 = out_labels.pop(edge(6, 7))
    root_510 = out_labels.pop(edge(5, 10))
    out_labels[edge(5, 7)] = root_67
    out_labels[edge(6, 10)] = root_510
    out_labels[edge(5, 6)] = add(out_labels[edge(1, 6)], out_labels[edge(6, 10)])
    return out_edges, out_labels


def main() -> None:
    verify_conservation(BASE_EDGES, BASE_LABELS)
    base_metrics = verify_graph(BASE_EDGES, expected_girth=6, expected_cyclic=6)

    # The stored predecessor side of f=5-6 is root-valued in the original source flow.
    assert add(BASE_LABELS[edge(1, 6)], BASE_LABELS[edge(5, 10)]) == value("13")
    assert add(BASE_LABELS[edge(6, 7)], BASE_LABELS[edge(4, 5)]) == value("13")

    switched = switch_cycle(BASE_LABELS)
    verify_conservation(BASE_EDGES, switched)
    assert [e for e, x in switched.items() if len(x) != 2] == [edge(1, 14)]
    assert switched[edge(1, 14)] == value("1235")

    # Existing atom 1-14 is standard: its two crossed restrictions are roots 25 and 13.
    crossed = {
        add(switched[edge(1, 2)], switched[edge(9, 14)]),
        add(switched[edge(1, 2)], switched[edge(13, 14)]),
    }
    assert crossed == {value("25"), value("13")}

    # Current f cell remains root-valued.
    assert add(switched[edge(1, 6)], switched[edge(6, 7)]) == value("13")
    assert add(switched[edge(4, 5)], switched[edge(5, 10)]) == value("13")

    out_edges, out_labels = apply_literal_source_nni(BASE_EDGES, switched)
    verify_conservation(out_edges, out_labels)
    post_metrics = verify_graph(out_edges, expected_girth=5, expected_cyclic=5)

    nonroots = {e: x for e, x in out_labels.items() if len(x) != 2}
    assert nonroots == {
        edge(1, 14): value("1235"),
        edge(5, 6): value("1235"),
    }
    assert set(edge(1, 14)).isdisjoint(edge(5, 6))

    payload = {
        "schema": "AC-RL-ONE-ATOM-01-disjoint-double-atom-v1",
        "base_edges": {f"{u}-{v}": show(BASE_LABELS[(u, v)]) for u, v in sorted(BASE_EDGES)},
        "switch_cycle": list(SWITCH_CYCLE),
        "switch_root": show(SWITCH_ROOT),
        "post_switch_edges": {f"{u}-{v}": show(switched[(u, v)]) for u, v in sorted(BASE_EDGES)},
        "existing_atom": {
            "edge": "1-14",
            "value": "1235",
            "crossed_roots": ["13", "25"],
        },
        "source_step": {
            "central_edge": "5-6",
            "base_current_root": "13",
            "base_predecessor_root": "13",
            "moved_edges": [
                {"edge": "6-7", "from": 6, "to": 5},
                {"edge": "5-10", "from": 5, "to": 6},
            ],
            "post_switch_predecessor_value": "1235",
        },
        "metrics": {"pre": base_metrics, "post": post_metrics},
        "persistent_nonroot_edges_after_step": [
            {"edge": "1-14", "value": "1235"},
            {"edge": "5-6", "value": "1235"},
        ],
    }
    digest = hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()
    assert digest == "dd4afccb8578e3ab8e48c33bddaad39e763f18dac398fe8e2d83e80ceeb57aea"

    summary = dict(payload)
    summary["canonical_digest"] = digest
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
