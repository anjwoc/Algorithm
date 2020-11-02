import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [[] for _ in range(m+1)]
for _ in range(m):
    x, y, c = map(int, input().split())
    arr[x].append((y, c))
    arr[y].append((x, c))

r, c = map(int, input().split())


def bfs(r, c):
    que = deque()
    que.append(r)
    visited = [[100001] * (n+1) for _ in range(m+1)]
    while que:
        x = que.popleft()
        for vertex, weight in arr[x]:
            if visited[x][vertex] == 100001:
                que.append(vertex)
                visited[x][vertex] = min(visited[x][vertex], weight)
    return visited[r][c]


print(bfs(r, c))
