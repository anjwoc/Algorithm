import sys
from collections import deque
input: lambda: sys.stdin.readline().strip()

dx = (-1, 1, 0, 0)
dy = (0, 0, 1, -1)

n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
dist = [[[0, 0] for _ in range(m)] for _ in range(n)]


def bfs(start):
    que = deque()
    que.append(start)
    dist[0][0][0] = 1

    while que:
        x, y, w = que.popleft()

        if x == n-1 and y == m-1:
            return dist[x][y][w]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if dist[nx][ny][w]:
                continue

            if arr[nx][ny] == '0':
                # 이동 가능
                dist[nx][ny][w] = dist[x][y][w] + 1
                que.append((nx, ny, w))
            if arr[nx][ny] == '1' and w == 0:
                # 벽
                dist[nx][ny][1] = dist[x][y][w] + 1
                que.append((nx, ny, 1))
    return -1


print(bfs((0, 0, 0)))
