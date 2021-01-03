from collections import deque, defaultdict


def solution(n, edge):
    adj = [[] for _ in range(n+1)]
    dist = [0 for _ in range(n)]
    visited = [0 for _ in range(n)]
    que = deque([0])
    visited[0] = 1

    for a, b in edget:
        adj[a].append(b)
        adj[b].append(a)

    while que:
        v = que.popleft()
        for i in adj[v]:
            if not visited[i]:
                visited[i] = 1
                dist[i] += 1
                que.append(i)

    dist.sort(reverse=True)
    ans = dist.count(dist[0])
