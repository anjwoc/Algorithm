import sys
input = sys.stdin.readline

# d[i] = d[i-1] + d[i-2]

n = int(input())
sys.setrecursionlimit(1000010)
dp = [0] * 1000001
dp[1] = 1
dp[2] = 2
for i in range(3, n+1):
  dp[i] = (dp[i-1] + dp[i-2]) % 15746

print(dp[n])