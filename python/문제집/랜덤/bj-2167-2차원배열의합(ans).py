import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for i in range(m+1)] for _ in range(n+1)]


# 1 <= N, M <= 300
# 1 <= K <= 10000
# 90000 * 10000 = 약 9억이기 때문에 단순한 구현으로는 절대 풀리지 않는다.

'''
2 3
1 2 4
8 16 32
3
1 1 2 3
1 2 1 2
1 3 2 3
'''

# DP[i][j] = (1, 1)부터 (i, j)까지의 부분합
for i in range(1, n+1):
    for j in range(1, m+1):
        # 위에서 구한 누적합 + 왼쪽에서 구한 누적합 - 교집합 + 자신의 값
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + arr[i-1][j-1]

for _ in range(int(input())):
    i, j, x, y = map(int, input().split())
    print(dp[x][y] - dp[i-1][y] - dp[x][j-1] + dp[i-1][j-1])
