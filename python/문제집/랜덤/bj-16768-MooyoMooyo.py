import sys
from collections import deque

input: lambda: sys.stdin.readline().strip()


def new_array(N):
    return [[False for i in range(10)] for _ in range(N)]


dx = (-1, 1, 0, 0)
dy = (0, 0, 1, -1)

n, k = map(int, input().split())
maps = [list(input()) for _ in range(n)]
ck = new_array(n)  # 그룹에 속해있는지를 체크
ck2 = new_array(n)  # 지워도 되는가를 체크


def dfs(x, y):
    ans = 1
    ck[x][y] = True

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= 10:
            continue
        if ck[nx][ny] or maps[x][y] != maps[nx][ny]:
            continue
        ans += dfs(nx, ny)
    return ans


def remove(x, y, val):
    ck2[x][y] = True
    maps[x][y] = '0'
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= 10:
            continue
        if ck2[nx][ny] or maps[nx][ny] != val:
            continue
        remove(nx, ny, val)


def down():
    for i in range(10):
        tmp = []
        for j in range(n):
            if maps[j][i] != '0':
                tmp.append(maps[j][i])

        for j in range(n-len(tmp)):
            maps[j][i] = '0'
        for j in range(n-len(tmp), n):
            maps[j][i] = tmp[j - (n - len(tmp))]


while True:
    exist = False
    ck = new_array(n)  # 그룹에 속해있는지를 체크
    ck2 = new_array(n)  # 지워도 되는가를 체크
    for i in range(n):
        for j in range(10):
            if maps[i][j] == '0' or ck[i][j]:
                continue
            res = dfs(i, j)  # 개수 세기
            if res >= k:
                remove(i, j, maps[i][j])  # 지우기
                exist = True

    if not exist:
        break
    down()

for i in maps:
    print(''.join(i))
