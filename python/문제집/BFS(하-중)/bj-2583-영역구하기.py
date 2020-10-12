import sys
import collections
input = sys.stdin.readline

dx = (-1, 1, 0, 0)
dy = (0, 0, 1, -1)


def bfs(i, j, visited):
    que = collections.deque()
    visited.add((i, j))
    que.append((i, j))
    area = 1

    while que:
        x, y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                if arr[nx][ny] == 0:
                    que.append((nx, ny))
                    visited.add((nx, ny))
                    area += 1
    return area


m, n, k = map(int, input().split())
arr = [[0] * (n) for _ in range(m)]
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            arr[i][j] = 1

visited = set()

cnt = 0
areas = []

for i in range(m):
    for j in range(n):
        if arr[i][j] == 0 and (i, j) not in visited:
            areas.append(bfs(i, j, visited))
            cnt += 1

print(cnt)
for i in sorted(areas):
    print(i, end=' ')
