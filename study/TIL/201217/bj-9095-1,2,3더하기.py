import sys
input = sys.stdin.readline

dp = [0] * 21
dp[0] = 0
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 11):
  dp[i] = dp[i-1] + dp[i-2] + dp[i-3]


# DP[i] = i를 1,2,3의 합으로 나타내는 방법의 수
for _ in range(int(input())):
  n = int(input())
  print(dp[n])