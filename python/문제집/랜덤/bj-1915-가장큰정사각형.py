import sys
input: lambda: sys.stdin.readline().strip()

n, m = map(int, input().split())

# dp[i][j] = i, j 까지 왔을 때, 가장 큰 정사각형 한 변의 길이
# dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
arr = [[0 for _ in range(m+1)] for _ in range(n+1)]
for i in range(n):
    for idx, j in enumerate(list(map(int, list(input())))):
        arr[i+1][idx+1] = j

for i in range(1, n+1):
    for j in range(1, m+1):
        if arr[i][j]:
            dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
        else:
            # 사실 이미 초기화를 해놔서 해당 코드는 필요없지만 동작을 이해하기 위해
            dp[i][j] = 0

print(max([max(i) for i in dp])**2)  # 넓이

'''
input
4 4
0100
0111
1110
0010
'''
