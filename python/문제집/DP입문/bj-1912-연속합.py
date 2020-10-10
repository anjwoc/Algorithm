n = int(input())
arr = list(map(int, input().split()))

# -1001로 모두 초기화 하는 방법보다 ans 변수를 두고 계속해서 비교하는 방법이 더 빠르다.
# dp = [-1001 for _ in range(n+1)]
# 시간 차이는 약 2배정도 차이난다.
dp = [0 for _ in range(n+1)]
ans = -1001

for i in range(n):
  dp[i] = max(dp[i - 1] + arr[i], arr[i])
  ans = max(ans, dp[i])
print(ans)