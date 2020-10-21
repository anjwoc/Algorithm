import sys
input = sys.stdin.readline

n, east, west, south, north = list(map(int, input().split()))
visited = {}
probs = [east, west, south, north]
dx, dy = (-1, 1, 0, 0), (0, 0, 1, -1)
cnt = 0


def check(x, y, visited):
    if (x, y) in visited and visited[(x, y)] is True:
        return True
    return False


def dfs(n, x, y, visited):
    if n < 0:
        return 1
    if check(x, y, visited):
        return 0
    visited[(x, y)] = True
    ans = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        ans += probs[i] * dfs(n-1, nx, ny, visited)
    visited[(x, y)] = False
    return ans


print(dfs(n, 0, 0, visited) / (100 ** (n+1)))
