import sys
input = lambda: sys.stdin.readline().strip()

import heapq
def prim(v):
    q = []
    visited = [False]*(V+1)
    visited[v] = True
    d = 0
    cnt = 1
    for a in adj[v]:
        heapq.heappush(q, a)

    while q:
        c, v = heapq.heappop(q)
        if not visited[v]:
            visited[v] = True
            cnt += 1
            d += c
            for a in adj[v]:
                heapq.heappush(q, a)
        if cnt == V:
            return d
    return 0

V, E = map(int, input().split())
adj = [[] for _ in range(V+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    adj[a].append((c, b))
    adj[b].append((c, a))

print(prim(1))