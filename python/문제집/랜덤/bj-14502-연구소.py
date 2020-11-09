import sys
import copy
from collections import deque
input = sys.stdin.readline

start = time.time()

dx = (-1, 1, 0, 0)
dy = (0, 0, 1, -1)
ans = 0


def getSafeArea(copyed):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if copyed[i][j] == 0:
                cnt += 1
    return cnt


# def spreadVirus(x, y, copyed):
#     # bfs
#     que = deque([])
#     que.append((x, y))
#     while que:
#         r, c = que.popleft()
#         for i in range(4):
#             nr = r + dx[i]
#             nc = c + dy[i]

#             if 0 <= nr < n and 0 <= nc < m:
#                 if copyed[nr][nc] == 0:
#                     copyed[nr][nc] = 2
#                     que.append((nr, nc))

def spreadVirus(x, y, copyed):
    # dfs
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if copyed[nx][ny] == 0:
                copyed[nx][ny] = 2
                spreadVirus(nx, ny, copyed)


def setWall(start, depth):
    global ans, virus

    if depth == 3:
        copyed = copy.deepcopy(maps)

        length = len(virus)
        for i in range(length):
            vx, vy = virus[i]
            spreadVirus(vx, vy, copyed)

        ans = max(ans, getSafeArea(copyed))
        return

    for i in range(start, n*m):
        x = i // m
        y = i % m
        if maps[x][y] == 0:
            maps[x][y] = 1
            setWall(i + 1, depth + 1)
            maps[x][y] = 0


# 0은 빈칸, 1은 벽, 2는 바이러스
n, m = map(int, input().split())
maps = []
virus = []
for _ in range(n):
    maps.append(list(map(int, input().split())))

virus = [(nx, ny) for nx, row in enumerate(maps) for ny, val in enumerate(row) if val == 2]
setWall(0, 0)
print(ans)
