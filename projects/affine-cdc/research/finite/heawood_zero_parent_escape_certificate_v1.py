from __future__ import annotations

from itertools import combinations
from collections import defaultdict
import hashlib
import json

ORIGINAL = {
    (1,2):"23",(1,6):"12",(1,14):"13",(2,3):"34",(2,11):"24",
    (3,4):"13",(3,8):"14",(4,5):"12",(4,13):"23",(5,6):"13",
    (5,10):"23",(6,7):"23",(7,8):"24",(7,12):"34",(8,9):"12",
    (9,10):"13",(9,14):"23",(10,11):"12",(11,12):"14",(12,13):"13",
    (13,14):"12",
}

def eid(u: int, v: int) -> str:
    a,b=sorted((u,v)); return f"e{a}_{b}"

def roots(s: str) -> frozenset[int]:
    return frozenset(map(int,s))

def rstr(s) -> str:
    return "".join(map(str,sorted(s)))

def xor_root(label: str, h) -> str:
    return rstr(set(roots(label)) ^ set(h))

def initial_records():
    return {eid(u,v): {"ends":[u,v], "label":lab} for (u,v),lab in ORIGINAL.items()}

def copy_records(records):
    return {k:{"ends":v["ends"][:],"label":v["label"]} for k,v in records.items()}

def labels_from_records(records):
    out={}
    for rec in records.values():
        edge=tuple(sorted(rec["ends"]))
        if edge in out: raise AssertionError(f"parallel edge {edge}")
        out[edge]=rec["label"]
    return out

def adjacency(labels, subset=None):
    vertices=set(); adj=defaultdict(set)
    for u,v in labels: vertices.update((u,v))
    if subset is None: subset=vertices
    subset=set(subset)
    for u,v in labels:
        if u in subset and v in subset:
            adj[u].add(v); adj[v].add(u)
    for v in subset: adj[v]
    return adj

def connected(labels, subset=None):
    adj=adjacency(labels,subset)
    if not adj: return True
    start=next(iter(adj)); seen={start}; stack=[start]
    while stack:
        x=stack.pop()
        for y in adj[x]:
            if y not in seen: seen.add(y); stack.append(y)
    return len(seen)==len(adj)

def edge_count(labels, subset):
    S=set(subset)
    return sum(1 for u,v in labels if u in S and v in S)

def bridges(labels):
    ans=[]
    for edge in sorted(labels):
        reduced={e:l for e,l in labels.items() if e!=edge}
        if not connected(reduced): ans.append(list(edge))
    return ans

def edge_connectivity(labels):
    V=sorted({x for e in labels for x in e}); v0=V[0]; best=10**9
    for r in range(1,len(V)):
        for tup in combinations(V,r):
            S=set(tup)
            if v0 not in S: continue
            cut=sum(1 for u,v in labels if (u in S)^(v in S))
            if cut<best: best=cut
    return best

def cyclic_edge_connectivity(labels):
    V=sorted({x for e in labels for x in e}); v0=V[0]
    best=10**9; witnesses=[]
    for r in range(1,len(V)):
        for tup in combinations(V,r):
            S=set(tup)
            if v0 not in S: continue
            T=set(V)-S
            if not T or not connected(labels,S) or not connected(labels,T): continue
            if edge_count(labels,S) < len(S): continue
            if edge_count(labels,T) < len(T): continue
            cut=sorted(tuple(sorted((u,v))) for u,v in labels if (u in S)^(v in S))
            k=len(cut); item=(S,T,cut)
            if k<best: best=k; witnesses=[item]
            elif k==best: witnesses.append(item)
    return best,witnesses

def triangle_at(labels,v):
    labs=[roots(lab) for e,lab in labels.items() if v in e]
    if len(labs)!=3: raise AssertionError((v,labs))
    total=set()
    for r in labs: total ^= set(r)
    support=set().union(*labs)
    expected={frozenset(c) for c in combinations(support,2)}
    if total or len(support)!=3 or set(labs)!=expected:
        raise AssertionError((v,labs,total,support))
    return rstr(support)

def in_H(label,h):
    return len(set(roots(label)) & set(h))==1

def h_components(labels,h):
    hedges={e for e,l in labels.items() if in_H(l,h)}
    adj=defaultdict(set)
    for u,v in hedges: adj[u].add(v); adj[v].add(u)
    seen=set(); comps=[]
    for start in sorted(adj):
        if start in seen: continue
        stack=[start]; seen.add(start); vs=set(); es=set()
        while stack:
            x=stack.pop(); vs.add(x)
            for y in sorted(adj[x]):
                es.add(tuple(sorted((x,y))))
                if y not in seen: seen.add(y); stack.append(y)
        comps.append((sorted(vs),sorted(es)))
    return comps

PORTS={"A":(3,4),"B":(5,6),"C":(4,13),"D":(5,10)}
def outside_matching(labels,h,active={4,5}):
    nodes=set(); adj=defaultdict(set)
    for (u,v),lab in labels.items():
        if not in_H(lab,h): continue
        if u in active and v in active: continue
        if u in active or v in active:
            outside=v if u in active else u
            p=next(name for name,e in PORTS.items() if set(e)=={u,v})
            adj[p].add(outside); adj[outside].add(p); nodes.update((p,outside))
        else:
            adj[u].add(v); adj[v].add(u); nodes.update((u,v))
    seen=set(); match=[]
    for start in sorted(nodes,key=str):
        if start in seen: continue
        stack=[start]; seen.add(start); comp=set()
        while stack:
            x=stack.pop(); comp.add(x)
            for y in adj[x]:
                if y not in seen: seen.add(y); stack.append(y)
        ps=sorted(x for x in comp if isinstance(x,str))
        if ps: match.append(tuple(ps))
    return sorted(match)

def state_summary(records):
    labels=labels_from_records(records); V=sorted({x for e in labels for x in e})
    cec,wits=cyclic_edge_connectivity(labels)
    return {
        "edges":[{"id":k,"ends":sorted(records[k]["ends"]),"root":records[k]["label"]} for k in sorted(records)],
        "triangles":{str(v):triangle_at(labels,v) for v in V},
        "connected":connected(labels),
        "simple":all(u!=v for u,v in labels) and len(labels)==len(records),
        "bridges":bridges(labels),
        "edge_connectivity":edge_connectivity(labels),
        "cyclic_edge_connectivity":cec,
        "cyclic_cut_witnesses":[{"shore":sorted(S),"cut":[list(e) for e in cut]} for S,T,cut in wits],
    }

def build_certificate():
    s0=initial_records()
    s1=copy_records(s0)
    s1["e12_13"]["ends"]=[12,14]
    s1["e1_14"]["ends"]=[1,13]
    lab1=labels_from_records(s1)
    comps=h_components(lab1,(3,5))
    assert comps == [
        ([1,2,3,4,13],[(1,2),(1,13),(2,3),(3,4),(4,13)]),
        ([5,6,7,9,10,12,14],[(5,6),(5,10),(6,7),(7,12),(9,10),(9,14),(12,14)]),
    ]
    Z0=set(comps[0][1])
    s2=copy_records(s1)
    for rec in s2.values():
        if tuple(sorted(rec["ends"])) in Z0:
            rec["label"]=xor_root(rec["label"],{3,5})
    s3=copy_records(s2)
    s3["e5_6"]["ends"]=[4,6]
    s3["e4_13"]["ends"]=[5,13]
    s3["e4_5"]["label"]="35"
    active_ids={"A":"e3_4","B":"e5_6","C":"e4_13","D":"e5_10","central":"e4_5"}
    cert={
        "name":"Heawood zero-parent escape movie",
        "normal_form":{"active_vertices":[4,5],"active_edge_id":"e4_5","word":["13","13","23","23"],"current_central":"12","parent_central":"0"},
        "steps":{"S0_original":state_summary(s0),"S1_remote_branch_swap":state_summary(s1),"S2_H35_switch_Z0":state_summary(s2),"S3_literal_parent_NNI":state_summary(s3)},
        "H35_after_remote":{"Z0_vertices":comps[0][0],"Z0_edges":[list(e) for e in comps[0][1]],"Z1_vertices":comps[1][0],"Z1_edges":[list(e) for e in comps[1][1]],"outside_matching":outside_matching(lab1,(3,5))},
        "active_after_switch":{k:{"edge_id":e,"ends":sorted(s2[e]["ends"]),"root":s2[e]["label"]} for k,e in active_ids.items()},
        "dart_moves":[
            {"step":"remote_branch_swap","edge_id":"e12_13","fixed_outside_dart_at":12,"moved_local_dart_from":13,"moved_local_dart_to":14,"root":"13"},
            {"step":"remote_branch_swap","edge_id":"e1_14","fixed_outside_dart_at":1,"moved_local_dart_from":14,"moved_local_dart_to":13,"root":"13"},
            {"step":"parent_NNI","edge_id":"e5_6","fixed_outside_dart_at":6,"moved_local_dart_from":5,"moved_local_dart_to":4,"root":"13"},
            {"step":"parent_NNI","edge_id":"e4_13","fixed_outside_dart_at":13,"moved_local_dart_from":4,"moved_local_dart_to":5,"root":"25"},
            {"step":"parent_NNI","edge_id":"e4_5","fixed_endpoints":[4,5],"root_from":"12","root_to":"35"},
        ],
        "cap_vertices":[7,12],
        "cap_dart_checks":{"vertex7_incident_edge_ids":["e6_7","e7_8","e7_12"],"vertex12_incident_edge_ids":["e7_12","e11_12","e12_13"],"all_cap_dart_ids_preserved":True,"only_opposite_endpoint_change_on_cap_incident_edge":{"edge_id":"e12_13","cap_endpoint":12,"other_endpoint_from":13,"other_endpoint_to":14,"root":"13"}},
    }
    return cert

if __name__ == "__main__":
    cert=build_certificate()
    canonical=json.dumps(cert,sort_keys=True,separators=(",",":"))
    digest=hashlib.sha256(canonical.encode()).hexdigest()
    expected="db160ee18300ead7aaf28c56cf83be1068c243b1e51aeabfc896f74c1615b14b"
    assert digest==expected,(digest,expected)
    print(json.dumps(cert,sort_keys=True,indent=2))
    print(f"sha256={digest}")
