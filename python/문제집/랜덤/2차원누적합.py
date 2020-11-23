import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for i in range(m+1)] for _ in range(n+1)]


'''
2 3
1 2 4
8 16 32
3
1 1 2 3
1 2 1 2
1 3 2 3
'''

# 누적합 계산
for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + arr[i-1][j-1]

# (i, j)부터 (x, y)까지의 부분합
for _ in range(int(input())):
    i, j, x, y = map(int, input().split())
    print(dp[x][y] - dp[i-1][y] - dp[x][j-1] + dp[i-1][j-1])
