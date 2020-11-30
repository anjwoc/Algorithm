import sys
input = sys.stdin.readline

MOD = 10007
n = int(input())
DP = [[1] * 10 for _ in range(n + 1)]

'''
2로 끝나는 3자리 수를 만든다고 하면
02 12 22가 있다.
이 경우는 0으로 끝나는 2자리 수 + 2로 끝나는 2자리 수의 합과 같다.
이 점화식을 코드로 옮기면 다음과 같다.
DP[i][j] = DP[i][j-1] + DP[i-1][j]
'''

for i in range(1, n):
  for j in range(1, 10):
    DP[i][j] = DP[i][j - 1] + DP[i - 1][j]

print(sum(DP[n-1]) % MOD)
