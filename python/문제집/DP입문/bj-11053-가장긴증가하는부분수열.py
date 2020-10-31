import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = [1] * (n + 1)

for i in range(len(arr)):
  # 0 ~ n-1
  for j in range(i + 1):
    # i ~ i+1
    if arr[i] > arr[j]:
      dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))      