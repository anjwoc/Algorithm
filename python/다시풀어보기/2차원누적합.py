import sys
input = sys.stdin.readline

arr = [[1 for i in range(10)] for j in range(10)]
dp = [[0 for _ in range(10)] for _ in range(10)]

for i in range(1, 10):
    for j in range(1, 10):
        # 왼쪽의 누적합 + 위쪽의 누적합 - 대각선 누적합 + 해당 인덱스의 값
        dp[i][j] = dp[i][j-1] + dp[i-1][j] + dp[i-1][j-1] + arr[i][j]
