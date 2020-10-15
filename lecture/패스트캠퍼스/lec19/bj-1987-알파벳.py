import sys
from collections import deque
input: lambda: sys.stdin.readline().strip()

dx, dy = (-1, 1, 0, 0), (0, 0, 1, -1)


def bfs(x, y):
    global ans
    que = set()
    que.add((x, y, arr[x][y]))

    while que:
        x, y, step = que.pop()
        ans = max(ans, len(step))
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if arr[nx][ny] not in step:
                    # print('step: %s arr[nx][ny]: %s' % (step, arr[nx][ny]))
                    que.add((nx, ny, step + arr[nx][ny]))


r, c = map(int, input().split())
arr = []
ans = 0
for _ in range(r):
    arr.append(list(input()))

bfs(0, 0)
print(ans)
