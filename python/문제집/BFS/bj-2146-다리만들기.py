import sys
from collections import deque

input = sys.stdin.readline
dx = (-1, 1, 0, 0)
dy = (0, 0, 1, -1)


def bfs(visited, i, j):
    que = deque()
    que.append((i, j))
    start = (i, j)
    end = ()
    while que:
        x, y = que.popleft()
        end = (x, y)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if arr[nx][ny] == 1:
                    visited[nx][ny] = True
                    que.append((nx, ny))
    return [start, end]


def search(i, j, r, c):
    que = deque()
    que.append((i, j))
    arr[i][j] = 1
    cnt = 0
    while que:
        x, y = que.popleft()
        if x == r and y == c:
            return cnt
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny] == 0:
                    arr[nx][ny] = arr[x][y] + 1
                    que.append((nx, ny))


n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

visited = [[False] * n for _ in range(n)]

positions = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 and not visited[i][j]:
            positions.append(bfs(visited, i, j))
ans = 1e9
for i in range(len(positions)):
    for j in range(i+1, len(positions)):
        for x1, y1 in positions[i]:
            for x2, y2 in positions[j]:
                dist = search(x1, y1, x2, y2)
                print("-------")
                print(arr[x2][y2])
                for i in arr:
                    print(i)
                print("-------")


print(ans)
