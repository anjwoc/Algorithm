from collections import deque


def bfs(sz, sx, sy):
    de = deque()
    de.append([sz, sx, sy])
    ch[sz][sx][sy] = 0

    while de:
        z, x, y = de.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0 <= nz < l and 0 <= nx < r and 0 <= ny < c:
                if a[nz][nx][ny] == 'E':
                    print('Escaped in', ch[z][x][y] + 1, 'minute(s).')
                    return

                if ch[nz][nx][ny] == -1 and a[nz][nx][ny] == '.':
                    ch[nz][nx][ny] = ch[z][x][y] + 1
                    de.append([nz, nx, ny])

    print('Trapped!')


dx = [-1, 0, 1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

while True:

    l, r, c = map(int, input().split())

    if l == 0 and r == 0 and c == 0:
        break

    a = [[[]*c for i in range(r)] for j in range(l)]

    ch = [[[-1]*c for i in range(r)] for j in range(l)]

    for i in range(l):
        a[i] = [list(input()) for i in range(r)]
        input()

    for i in range(l):
        for j in range(r):
            for k in range(c):
                if a[i][j][k] == 'S':
                    bfs(i, j, k)
