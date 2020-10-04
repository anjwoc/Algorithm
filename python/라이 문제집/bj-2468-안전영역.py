import sys
from collections import deque

input = sys.stdin.readline
dx = (-1, 1, 0, 0)
dy = ( 0, 0, 1, -1)

def bfs(x, y, visited, cnt, H):
    visited[x][y] = 1
    que = deque()
    que.append((x, y))
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and arr[nx][ny] > H:
                visited[nx][ny] = 1
                que.append((nx, ny))

n = int(input())
arr = []
max_height = -1
ans = 1
for _ in range(n):
    data = list(map(int, input().split()))
    max_height = max(max_height, max(data))
    arr.append(data)

for height in range(max_height+1):
    cnt = 1
    visited = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0 and arr[i][j] > height:
                bfs(i, j, visited, cnt, height)
                cnt += 1
    # print("----------------")
    # print(visited)
    # print(cnt-1)
    # print("----------------")
    ans = max(ans, cnt-1)

print(ans)
