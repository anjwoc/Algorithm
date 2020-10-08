import sys, heapq

input = sys.stdin.readline


def get_distance(v1, v2):
    a = v1[0] - v2[0]
    b = v1[1] - v2[1]
    return (a * a + b * b) ** (1 / 2)


def find(parent, node):
    if parent[node] != node:
        parent[node] = find(parent, parent[node])

    return parent[node]


def union(parent, u, v):
    a = find(parent, u)
    b = find(parent, v)

    if rank[a] > rank[b]:
        parent[b] = a
    else:
        parent[a] = b
        if rank[a] == rank[b]:
            rank[b] += 1

    # if a < b:
    #     parent[b] = a
    # else:
    #     parent[a] = b


def make_set(node):
    parent[node] = node
    rank[node] = 0


n, m = map(int, input().split())
edges = []
parent = {}
rank = {}
locations = []

for _ in range(n):
    x, y = map(int, input().split())
    locations.append((x, y))

length = len(locations)

for i in range(length - 1):
    for j in range(i + 1, length):
        edges.append((i + 1, j + 1, get_distance(locations[i], locations[j])))

for i in range(1, n + 1):
    parent[i] = i
    rank[i] = 0

for i in range(m):
    a, b = map(int, input().split())
    union(parent, a, b)

edges.sort(key=lambda data: data[2])

ans = 0
# mst = []
for a, b, cost in edges:
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        ans += cost
        # mst.append((a, b, cost))

print("%0.2f" % (ans))
