import sys

input = lambda: sys.stdin.readline().strip()

n = int(input())
maps = []
for _ in range(n):
  maps.append(list(map(int, input().split())))

dp = [[0]*n for _ in range(n)]
dp[0][0] = 1

for i in range(n):
  for j in range(n):
    if i == n-1 and j == n-1:
      break
    value = maps[i][j]
    down = i + value
    right = j + value
    
    if down < n:
      dp[down][j] += dp[i][j]
    if right < n:
      dp[i][right] += dp[i][j]

print(dp[n-1][n-1])