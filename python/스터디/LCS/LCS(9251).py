import sys
input = lambda: sys.stdin.readline().strip()

a = list(input())
b = list(input())
alen = len(a)
blen = len(b)

# dp[i][j] = i번째 문자와 j번째 문자 사이의 최장 거리
dp = [[0] * (alen+1) for _ in range(blen+1)]
for i in range(blen+1):
  for j in range(alen+1):
    # 1 : 왼쪽값과 위쪽값, 현재까지 LCS의 최댓값을 찾기 위한 조건
    # 2 : 왼쪽 대각선 값 + 1, 과거 LCS 최댓값에 같은 문자열이므로 + 1
    dp[i][j] = max(dp[i][j-1], dp[i-1][j], dp[i-1][j-1] + (a[j-1] == b[j-1]))



