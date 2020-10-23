import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = [1] * (n + 1)
dp2 = [1] * (n + 1)

for i in range(n):
  for j in range(i + 1):
    if arr[i] > arr[j] and dp[i] <= dp[j]:
      dp[i] = dp[j] + 1


for i in range(n-1, -1, -1):
  for j in range(i, n):
    if arr[i] > arr[j] and dp2[i] <= dp2[j]:
      dp2[i] = dp2[j] + 1

ans = dp[0] + dp2[0] - 1
for i in range(1, n):
  ans = max(ans, dp[i] + dp2[i] - 1)
print(ans)