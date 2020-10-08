import sys
input = sys.stdin.readline
n = int(input())
arr = [int(input()) for _ in range(n)]
dp = [0 for _ in range(301)]

if n < 3:
  ans = 0
  for i in range(n):
    ans += arr[i]
  print(ans)
  exit(0)

dp[0] = arr[0]
dp[1] = arr[0] + arr[1]
dp[2] = max(arr[1] + arr[2], arr[0] + arr[2])

for i in range(3, n):
  # 전칸을 밟았거나 전전칸을 밟았거나
  dp[i] = max(dp[i - 2] + arr[i], arr[i - 1] + arr[i] + dp[i - 3])

print(dp[n-1])