#!/usr/bin/env python3
"""Finite certificate for AC-RL-PURE-NNI-03.

Standard-library only. It verifies the Heawood H_35 source movie, graph
categories/cyclic edge connectivity, and the finite S_3-invariant rank table.
"""
from __future__ import annotations

from collections import defaultdict, deque
from copy import deepcopy
from hashlib import sha256
from itertools import combinations
import json


def edge_key(u: int, v: int) -> tuple[int, int]:
    return (u, v) if u < v else (v, u)


def xor_root(a: str, b: str) -> str:
    return "".join(sorted(set(a) ^ set(b)))


def in_channel(root: str, h: str) -> bool:
    return len(set(root) & set(h)) == 1


def adjacency(records: dict[str, dict]) -> dict[int, set[int]]:
    out: dict[int, set[int]] = defaultdict(set)
    for rec in records.values():
        u, v = rec["ends"]
        assert u != v
        assert v not in out[u]
        out[u].add(v)
        out[v].add(u)
    return out


def connected_components(vertices: set[int], edges: list[tuple[int, int]]) -> list[set[int]]:
    adj = {v: set() for v in vertices}
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    unseen = set(vertices)
    ans = []
    while unseen:
        start = next(iter(unseen))
        comp = {start}
        q = deque([start])
        unseen.remove(start)
        while q:
            u = q.popleft()
            for v in adj[u]:
                if v in unseen:
                    unseen.remove(v)
                    comp.add(v)
                    q.append(v)
        ans.append(comp)
    return ans


def channel_components(records: dict[str, dict], h: str) -> list[dict]:
    edges = []
    vertices = set()
    for rec in records.values():
        if in_channel(rec["root"], h):
            e = edge_key(*rec["ends"])
            edges.append(e)
            vertices.update(e)
    ans = []
    for comp in connected_components(vertices, edges):
        ces = sorted(e for e in edges if e[0] in comp and e[1] in comp)
        ans.append({"vertices": sorted(comp), "edges": ces})
    return sorted(ans, key=lambda x: x["vertices"])


def vertex_triangles(records: dict[str, dict]) -> dict[int, str]:
    roots = defaultdict(list)
    for rec in records.values():
        u, v = rec["ends"]
        roots[u].append(rec["root"])
        roots[v].append(rec["root"])
    ans = {}
    for v, rs in roots.items():
        assert len(rs) == 3
        support = "".join(sorted(set().union(*map(set, rs))))
        assert len(support) == 3
        expected = sorted("".join(p) for p in combinations(support, 2))
        assert sorted(rs) == expected
        ans[v] = support
    return dict(sorted(ans.items()))


def graph_properties(records: dict[str, dict]) -> dict:
    adj = adjacency(records)
    vertices = set(adj)
    assert all(len(adj[v]) == 3 for v in vertices)
    comps = connected_components(vertices, [edge_key(*r["ends"]) for r in records.values()])
    bridges = []
    for eid in records:
        edges = [edge_key(*r["ends"]) for k, r in records.items() if k != eid]
        if len(connected_components(vertices, edges)) > 1:
            bridges.append(eid)
    return {
        "vertices": len(vertices),
        "edges": len(records),
        "connected": len(comps) == 1,
        "simple": True,
        "bridges": sorted(bridges),
        "cubic": all(len(adj[v]) == 3 for v in vertices),
    }


def has_cycle(vertices: set[int], edges: list[tuple[int, int]]) -> bool:
    if not vertices:
        return False
    comps = connected_components(vertices, edges)
    return len(edges) >= len(vertices) - len(comps) + 1


def cyclic_edge_connectivity(records: dict[str, dict]) -> int:
    vertices = sorted(adjacency(records))
    all_edges = [edge_key(*r["ends"]) for r in records.values()]
    anchor = vertices[0]
    best = len(all_edges) + 1
    others = vertices[1:]
    for size in range(1, len(vertices)):
        for rest in combinations(others, size - 1):
            shore = {anchor, *rest}
            other = set(vertices) - shore
            inside_a = [e for e in all_edges if e[0] in shore and e[1] in shore]
            inside_b = [e for e in all_edges if e[0] in other and e[1] in other]
            if len(connected_components(shore, inside_a)) != 1:
                continue
            if len(connected_components(other, inside_b)) != 1:
                continue
            if not has_cycle(shore, inside_a) or not has_cycle(other, inside_b):
                continue
            cut = sum((u in shore) ^ (v in shore) for u, v in all_edges)
            best = min(best, cut)
    return best


INITIAL = [
    ("e1_2", 1, 2, "23"), ("e1_6", 1, 6, "12"),
    ("e1_14", 1, 14, "13"), ("e2_3", 2, 3, "34"),
    ("e2_11", 2, 11, "24"), ("e3_4", 3, 4, "13"),
    ("e3_8", 3, 8, "14"), ("e4_5", 4, 5, "12"),
    ("e4_13", 4, 13, "23"), ("e5_6", 5, 6, "13"),
    ("e5_10", 5, 10, "23"), ("e6_7", 6, 7, "23"),
    ("e7_8", 7, 8, "24"), ("e7_12", 7, 12, "34"),
    ("e8_9", 8, 9, "12"), ("e9_10", 9, 10, "13"),
    ("e9_14", 9, 14, "23"), ("e10_11", 10, 11, "12"),
    ("e11_12", 11, 12, "14"), ("e12_13", 12, 13, "13"),
    ("e13_14", 13, 14, "12"),
]


def records() -> dict[str, dict]:
    return {eid: {"ends": [u, v], "root": root} for eid, u, v, root in INITIAL}


def verify_heawood_movie() -> dict:
    r0 = records()
    assert vertex_triangles(r0)[4] == vertex_triangles(r0)[5] == "123"

    r1 = deepcopy(r0)
    r1["e12_13"]["ends"] = [12, 14]
    r1["e1_14"]["ends"] = [1, 13]
    assert vertex_triangles(r1) == vertex_triangles(r0)
    comps = channel_components(r1, "35")
    assert comps == [
        {"vertices": [1, 2, 3, 4, 13],
         "edges": [(1, 2), (1, 13), (2, 3), (3, 4), (4, 13)]},
        {"vertices": [5, 6, 7, 9, 10, 12, 14],
         "edges": [(5, 6), (5, 10), (6, 7), (7, 12), (9, 10), (9, 14), (12, 14)]},
    ]

    r2 = deepcopy(r1)
    z0 = {"e1_2", "e1_14", "e2_3", "e3_4", "e4_13"}
    for eid in z0:
        r2[eid]["root"] = xor_root(r2[eid]["root"], "35")
    assert [r2[e]["root"] for e in ["e3_4", "e5_6", "e4_13", "e5_10"]] == ["15", "13", "25", "23"]
    assert r2["e4_5"]["root"] == "12"

    r3 = deepcopy(r2)
    r3["e5_6"]["ends"] = [4, 6]
    r3["e4_13"]["ends"] = [5, 13]
    r3["e4_5"]["root"] = "35"
    tri3 = vertex_triangles(r3)
    assert tri3[4] == "135" and tri3[5] == "235"

    props = {name: graph_properties(r) for name, r in [("initial", r0), ("post_remote", r1), ("final_parent", r3)]}
    assert all(p["connected"] and p["simple"] and p["cubic"] and not p["bridges"] for p in props.values())
    cyclic = {"initial": cyclic_edge_connectivity(r0),
              "post_remote": cyclic_edge_connectivity(r1),
              "final_parent": cyclic_edge_connectivity(r3)}
    assert cyclic == {"initial": 6, "post_remote": 5, "final_parent": 5}
    return {"components": comps, "cyclic_edge_connectivity": cyclic, "final_triangles": tri3}


X = {"123", "124", "125"}
Y = {"134", "135", "145"}
Z = {"234", "235", "245"}
S = {"345"}


def e_weight(t: str) -> int:
    return 2 if t in X else 1 if t in Y or t in Z else 0


def y_weight(t: str) -> int:
    return int(t in Y)


ROWS = [
    ("12", "123", "124", "134", "234"),
    ("12", "123", "125", "135", "235"),
    ("12", "124", "125", "145", "245"),
    ("13", "123", "134", "124", "234"),
    ("13", "123", "135", "125", "235"),
    ("13", "134", "135", "145", "345"),
    ("14", "124", "134", "123", "234"),
    ("14", "124", "145", "125", "245"),
    ("14", "134", "145", "135", "345"),
    ("15", "125", "135", "123", "235"),
    ("15", "125", "145", "124", "245"),
    ("15", "135", "145", "134", "345"),
]


def verify_rank_table() -> list[dict]:
    for a, b in [("3", "4"), ("3", "5"), ("4", "5")]:
        for t in X | Y | Z | S:
            moved = "".join(sorted(b if c == a else a if c == b else c for c in t))
            assert e_weight(moved) == e_weight(t)
            assert y_weight(moved) == y_weight(t)

    out = []
    for root, a, b, c, d in ROWS:
        de = e_weight(c) + e_weight(d) - e_weight(a) - e_weight(b)
        dy = y_weight(c) + y_weight(d) - y_weight(a) - y_weight(b)
        assert de < 0 or (de == 0 and dy < 0)
        out.append({"root": root, "source": [a, b], "target": [c, d], "delta_E": de, "delta_Y": dy})
    return out


def main() -> None:
    movie = verify_heawood_movie()
    rows = verify_rank_table()
    payload = {
        "rank_orbits": {"X": sorted(X), "Y": sorted(Y), "Z": sorted(Z), "S": sorted(S)},
        "rank_rows": rows,
        "heawood_initial_edges": INITIAL,
        "remote_reattach": [["e12_13", [12, 13], [12, 14]], ["e1_14", [1, 14], [1, 13]]],
        "H35_components_after_remote": [
            {"vertices": [1, 2, 3, 4, 13], "edges": ["e1_2", "e2_3", "e3_4", "e4_13", "e1_14"]},
            {"vertices": [5, 6, 7, 9, 10, 12, 14], "edges": ["e5_6", "e6_7", "e7_12", "e12_13", "e9_14", "e9_10", "e5_10"]},
        ],
        "switch_Z0": ["e1_2", "e2_3", "e3_4", "e4_13", "e1_14"],
        "parent_reattach": [["e5_6", [5, 6], [4, 6]], ["e4_13", [4, 13], [5, 13]], ["e4_5", "12", "35"]],
        "cyclic_edge_connectivity": movie["cyclic_edge_connectivity"],
    }
    digest = sha256(json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    assert digest == "d22bce5ea026f5c461575f05ed81ed6e68c71a0c3c459ce6ada93d96f458422e"
    print(json.dumps({"status": "ok", "sha256": digest, "rank_rows": len(rows), "movie": movie["cyclic_edge_connectivity"]}, sort_keys=True))


if __name__ == "__main__":
    main()
