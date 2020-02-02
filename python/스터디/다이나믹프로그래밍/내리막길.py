import sys
input = lambda: sys.stdin.readline().strip()

n, m = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

maps = []
dp = [[-1] * m for _ in range(n)]

for _ in range(n):
  maps.append(list(map(int, input().split())))


def dfs(x, y):
  global dp, maps
  if dp[x][y] != -1:
    return dp[x][y]
  if x<0 or x>=n or y<0 or y>=m:
    return 0
  if x==0 and y==0:
    return 1
  dp[x][y] = 0
  for i in range(4):
    nx = i + dx[i]
    ny = i + dy[i]
    if maps[x][y] < maps[nx][ny]:
      dp[x][y] += dfs(nx, ny)  

  return dp[x][y]
dfs(n-1, m-1)
print(dp)



