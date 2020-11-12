import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
T = int(input())
dx = (-1, 1, 0, 0)
dy = (0, 0, 1, -1)


def dfs(x, y):
    global maps, check
    if check[x][y] == 1:
        return

    check[x][y] = 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if maps[nx][ny] == 0 or check[nx][ny] == 1:
            continue
        dfs(nx, ny)


def process():
    global maps, check
    m, n, k = map(int, input().split())
    maps = [[0 for i in range(52)] for _ in range(52)]
    check = [[0 for i in range(52)] for _ in range(52)]

    for _ in range(k):
        x, y = map(int, input().split())
        maps[y+1][x+1] = 1
    ans = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            if maps[i][j] == 0 or check[i][j] == 1:
                continue
            dfs(i, j)
            ans += 1
    print(ans)


for _ in range(T):
    process()
