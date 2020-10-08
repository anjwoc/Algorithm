mygraph = {
    "vertices": ["A", "B", "C", "D", "E", "F", "G"],
    "edges": [
        (7, "A", "B"),
        (5, "A", "D"),
        (7, "B", "A"),
        (8, "B", "C"),
        (9, "B", "D"),
        (7, "B", "E"),
        (8, "C", "B"),
        (5, "C", "E"),
        (5, "D", "A"),
        (9, "D", "B"),
        (7, "D", "E"),
        (6, "D", "F"),
        (7, "E", "B"),
        (5, "E", "C"),
        (7, "E", "D"),
        (8, "E", "F"),
        (9, "E", "G"),
        (6, "F", "D"),
        (8, "F", "E"),
        (11, "F", "G"),
        (9, "G", "E"),
        (11, "G", "F"),
    ],
}

parent = dict()
rank = dict()


def find(node):
    # path compression 기법
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]


def union(v, u):
    r1 = find(v)
    r2 = find(u)

    # union-by-rank 기법
    if rank[r1] > rank[r2]:
        parent[r2] = r1
    else:
        parent[r1] = r2
        if rank[r1] == rank[r2]:
            rank[r2] += 1


def make_set(node):
    parent[node] = node
    rank[node] = 0


def kruskal(graph):
    mst = []

    # 초기화
    for node in graph["vertices"]:
        make_set(node)

    # 간선 기반 정렬
    edges = graph["edges"]
    edges.sort()

    # 간선 연결
    for edge in edges:
        weight, v, u = edge
        if find(v) != find(u):
            union(v, u)
            mst.append(edge)
    return mst


print(kruskal(mygraph))