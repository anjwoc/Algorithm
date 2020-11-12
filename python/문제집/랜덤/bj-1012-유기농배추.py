import sys
from collections import deque
input = sys.stdin.readline

dx = (-1, 1, 0, 0)
dy = (0, 0, 1, -1)


def bfs(a, b):
    que = deque([(a, b)])

    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                if maps[nx][ny] == 1:
                    visited[nx][ny] = True
                    que.append((nx, ny))


for _ in range(int(input())):
    m, n, k = map(int, input().split())
    maps = [[0] * (n) for _ in range(m)]
    visited = [[False] * (n) for _ in range(m)]
    for _ in range(k):
        x, y = map(int, input().split())
        maps[x][y] = 1

    cnt = 0
    for i in range(m):
        for j in range(n):
            if maps[i][j] == 1 and not visited[i][j]:
                bfs(i, j)
                cnt += 1
    print(cnt)
