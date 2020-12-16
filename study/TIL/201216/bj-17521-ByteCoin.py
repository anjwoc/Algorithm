import sys
input = sys.stdin.readline

n, w = map(int, input().split())
prices = [int(input()) for _ in range(n)]
coin = 0

for i in range(n-1):
  if prices[i] < prices[i+1]:
    # 가격이 상승
    if w // prices[i] > 0:
      # (현금 // 현재 코인 가격)이 0보다 클 때
      # 구매
      coin = w // prices[i]
      w = w - (coin * prices[i])
  elif prices[i] > prices[i-1]:
    w += coin * prices[i]
    coin = 0
if coin > 0:
  w += coin * prices[-1]

print(w)
