import sys
from collections import deque
input: lambda: sys.stdin.readline().strip()

dx = (-1, 1, 0, 0)
dy = (0, 0, 1, -1)


def bfs(arr, i, j):
    maps = [[0] * m for _ in range(n)]
    que = deque()
    que.append((i, j))
    visited = set()
    visited.add((i, j))
    maps[i][j] = 1
    ans = 0
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in visited:
                if arr[nx][ny] == 'L':
                    visited.add((nx, ny))
                    que.append((nx, ny))
                    maps[nx][ny] = maps[x][y] + 1
                    ans = max(maps[nx][ny], ans)
    return (ans, maps)


n, m = map(int, input().split())
arr = []

for _ in range(n):
    arr.append(list(input()))

ans = 0
result = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'L':
            tmp, maps = bfs(arr, i, j)
            if ans < tmp:
                ans = tmp
                result = maps
print(ans-1)
