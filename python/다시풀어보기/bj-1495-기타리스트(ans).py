import sys
from collections import deque
input = sys.stdin.readline


n, s, m = map(int, input().split())
volume = list(map(int, input().split()))

dp = [[0] * (m+1) for _ in range(n+1)]

dp[0][s] = 1

for i in range(1, n+1):  # 곡의 개수
    for p in range(m+1):  # 볼륨
        if dp[i-1][p] == 0:
            continue
        if p - volume[i-1] >= 0:
            dp[i][p - volume[i-1]] = 1
        if p + volume[i-1] <= m:
            dp[i][p + volume[i-1]] = 1


ans = -1
for i in range(m, -1, -1):
    if dp[n][i] == 1:
        ans = i
        break
print(ans)
