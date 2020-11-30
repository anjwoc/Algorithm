import sys
input = sys.stdin.readline

MOD = 10007
n = int(input())
dp = [[0]*10 for _ in range(n+1)]
for i in range(10):
  dp[1][i] = 1

'''
2로 끝나는 3자리 수를 만든다고 하면
02 12 22가 있다.
이 경우는 0으로 끝나는 2자리 수 + 2로 끝나는 2자리 수의 합과 같다.
이 점화식을 코드로 옮기면 다음과 같다.
DP[i][j] = DP[i][j-1] + DP[i-1][j]
'''


for i in range(2, n+1):
  # i 자리수
  for j in range(10):
    # i 자리수에 끝 자리가 j인 경우
    for k in range(j + 1):
      # i-1 자리수에 끝자리 0~j까지인 경우의 수를 모두 더한다.
      dp[i][j] += dp[i-1][k]
      

print(sum(dp[n]) % MOD)
