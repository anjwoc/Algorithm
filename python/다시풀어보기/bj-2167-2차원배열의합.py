import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        # 왼쪽 + 위쪽 - 대각선 왼쪽 + 현재 값
        dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + arr[i-1][j-1]

# dp[i][j]: (1, 1)부터 (i, j)까지의 부분합
for _ in range(int(input())):
    i, j, x, y = map(int, input().split())
    print(dp[x][y] - dp[i-1][y] - dp[x][j-1] + dp[i-1][j-1])
