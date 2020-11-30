import sys
input = sys.stdin.readline

n = int(input())
wine = [int(input()) for _ in range(n)]
wine.insert(0, 0)
dp = [0]
dp.append(wine[1]) # dp[1]

'''
1. N번째 잔을 마시지 않은 경우 => D[i-1]
2. N번째 잔이 연속 1잔째 마시는 경우 => D[i-2] + W[i]
3. N번째 잔이 연속 2잔째 마시는 경우 => D[i-3] + W[i] + W[N-1]
'''

if n > 1:
  dp.append(wine[1] + wine[2]) # dp[2]

for i in range(3, n + 1):
  # dp[i-1] 와인을 먹을지 말지 결정 -> 세 번째 포도주를 마시지 않는 경우
  # dp[i-3] + wine[i-1] + wine[i] -> 이전 포도주를 마시지 않고 현재 포도주를 마시는 경우
  # dp[i-2] + wine[i] -> 전전 와인 먹고 한 칸 뛰고 다음 와인 먹기
  dp.append(max(dp[i - 1], dp[i - 3] + wine[i - 1] + wine[i], dp[i - 2] + wine[i]))
  
print(dp[n])
