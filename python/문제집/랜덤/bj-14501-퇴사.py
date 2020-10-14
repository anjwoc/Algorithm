import sys

input = sys.stdin.readline

n = int(input())
times = []
prices = []
dp = []
for _ in range(n):
    t, p = map(int, input().split())
    times.append(t)
    prices.append(p)
    dp.append(p)
dp.append(0)

for i in range(n-1, -1, -1):
    if times[i] + i > n:
        # 상담일이 퇴사일을 초과하면 i+1의 값이 최대금액
        dp[i] = dp[i+1]
    else:
        # 1일 금액 + 4일부터 받을 수 있는 최대 금액
        dp[i] = max(dp[i+1], prices[i] + dp[i + times[i]])

print(dp[0])
