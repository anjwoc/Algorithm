import sys
input = sys.stdin.readline

n, east, west, south, north = list(map(int, input().split()))
probs = [east/100, west/100, south/100, north/100]
dx, dy = (-1, 1, 0, 0), (0, 0, 1, -1)
ans = 0


def dfs(x, y, act, prob, visited):
    global ans
    if act == n:
        if len(set(visited)) == n+1:
            # 같은 곳을 방문하면 n+1보다 작아진다.
            ans += prob
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (nx, ny) not in visited:
            visited.append((nx, ny))
            dfs(nx, ny, act+1, prob*probs[i], visited)
            visited.pop()


dfs(0, 0, 0, 1, [(0, 0)])
print(ans)
