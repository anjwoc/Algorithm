import sys
input = lambda: sys.stdin.readline().strip()

n = int(input())
m = int(input())
dp = [[100001 for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
  # a = start, b = end, c = cost
  a, b, c = map(int, input().split())
  dp[a][b] = min(c, dp[a][b])

# 플로이드-워셜 알고리즘
for k in range(1, n+1):
  for i in range(1, n+1): # 경로 for문이 가장 상위단계여야 누락되지 않는다.
    for j in range(1, n+1):
      if i==j: # 자기 자신으로 오는 경우는 없다
        dp[i][j] = 0
      else: # 중간 경로를 경유하는 경우 i -> k, k -> j 와 i->j를 비교해서 더 작은 값으로
        dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

for row in dp[1:]:
  for col in row[1:]:
    if col == 100001:
      print(0, end='')
    else:
      print(col, end=" ")
  print()



