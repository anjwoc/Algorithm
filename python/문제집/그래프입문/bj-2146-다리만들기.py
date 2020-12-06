import sys
from collections import deque
input = sys.stdin.readline

dx, dy = (0, 0, 1, -1), (1, -1, 0, 0)


def bfs(i, j):
    que = deque([(i, j)])
    maps[i][j] = gid
    while que:
        x, y = que.popleft()
        for t in range(4):
            nx, ny = x + dx[t], y + dy[t]
            if 0 <= nx < n and 0 <= ny < n:
                if maps[nx][ny] == 1:
                    maps[nx][ny] = gid
                    que.append((nx, ny))
                elif maps[nx][ny] == 0 and not (x, y) in ocean:
                    # 현재 좌표(nx, ny)가 0이면서 (x, y)가 ocean에 없다면
                    # 좌표가 바다와 맞닿아있으면 추가
                    # (x, y)를 추가
                    ocean.append((x, y))


def get_distance():
    loop = 0
    ans = sys.maxsize
    while ocean:
        loop += 1
        length = len(ocean)
        for _ in range(length):
            x, y = ocean.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if maps[nx][ny] == 0:
                        maps[nx][ny] = maps[x][y]
                        ocean.append((nx, ny))
                    elif maps[nx][ny] < maps[x][y]:
                        ans = min(ans, (loop - 1) * 2)
                    elif maps[nx][ny] > maps[x][y]:
                        ans = min(ans, loop * 2 - 1)
    return ans


n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]
ocean = deque()

gid = -1
for i in range(n):
    for j in range(n):
        if maps[i][j] > 0:
            bfs(i, j)
            gid -= 1

print(ocean)
print(get_distance())
