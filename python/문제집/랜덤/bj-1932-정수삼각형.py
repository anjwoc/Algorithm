import sys
input = sys.stdin.readline

# DP[i][j]: i,j에 도착했을 때 최대값
# DP[i][j] = max(DP[i-1][j-1], DP[i-1][j]) + DP[i][j]

n = int(input())
# 입력 값을 저장하는 배열 A
A = [[0 for _ in range(n+1)] for _ in range(n+1)]
# DP 상태를 저장하는 배열
dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(1, n+1):
    # 입력으로 들어온 삼각형 모양과 동일하게 A배열에 저장
    tmp = list(map(int, input().split()))
    for j in range(1, i+1):
        A[i][j] = tmp[j-1]


for i in range(1, n+1):
    for j in range(1, i+1):
        # 이전 인덱스의 왼쪽 오른쪽 값의 합까지 중 큰 것과 현재 값을 더한다.
        dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + A[i][j]

print(max(dp[n]))
