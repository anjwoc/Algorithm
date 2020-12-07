import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
parent = [[] for _ in range(n + 1)]

# 트리를 그래프 형태로 생성
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(graph_list, start, parent):
    que = deque([start])

    while que:
        v = que.popleft()
        for i in graph_list[v]:
            parent[i].append(v)
            que.append(i)
            graph_list[i].remove(v)
    return parent


for i in bfs(graph, 1, parent)[2:]:
    print(*i)
