import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = [list(map(int, list(input().rstrip()))) for _ in range(n)]
dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

ans = max([max(i) for i in dp])

print(ans**2)
