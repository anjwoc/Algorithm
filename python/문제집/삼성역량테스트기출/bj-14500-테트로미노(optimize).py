import sys
from collections import deque
input = sys.stdin.readline

def dfs(k, sums, x, y):
  global ans
  if sums + max_value * (3-k) <= ans:
    return
  
  if k == 3:
    ans = max(ans, sums)
    return
  
  for i in range(4):
    nx, ny = x + dx[i], y + dy[i]
    
    if nx < 0 or nx >= n or ny < 0 or ny >= m or visited[nx][ny]:
      continue

    if k == 1:
      visited[nx][ny] = True
      dfs(k+1, sums+maps[nx][ny], x, y)
      visited[nx][ny] = False

    visited[nx][ny] = True
    dfs(k+1, sums+maps[nx][ny], x, y)
    visited[nx][ny] = False


dx = (1, 0, -1, 0)
dy = (0, -1, 0, 1)

n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
max_value = max(map(max, maps)) # 최대값
visited = [[False]*m for _ in range(n)]
ans = 0


for i in range(n):
  for j in range(m):
    visited[i][j] = True
    dfs(0, maps[i][j], i, j)
    visited[i][j] = False
    
print(ans)

