import sys
from collections import deque
input: lambda: sys.stdin.readline().strip()
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]


def bfs(k, i, j):
    que = deque()
    que.append((k, i, j))
    maps[k][i][j] = 0

    while que:
        z, x, y = que.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nz < l and 0 <= nx < r and 0 <= ny < c:
                if arr[nz][nx][ny] == 'E':
                    print('Escaped in %d minute(s).' % (maps[z][x][y] + 1))
                    return
                if arr[nz][nx][ny] == '.' and maps[nz][nx][ny] == -1:
                    que.append((nz, nx, ny))
                    maps[nz][nx][ny] = maps[z][x][y] + 1
    print('Trapped!')


while True:
    l, r, c = map(int, input().split())
    if l == 0 and r == 0 and c == 0:
        break
    arr = [[[]*c for _ in range(r)] for __ in range(l)]

    for i in range(l):
        arr[i] = [list(input()) for i in range(r)]
        input()
    maps = [[[-1] * c for _ in range(r)] for _ in range(l)]

    for i in range(l):
        for j in range(r):
            for k in range(c):
                if arr[i][j][k] == 'S':
                    bfs(i, j, k)
