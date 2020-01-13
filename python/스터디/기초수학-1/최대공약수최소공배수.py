import sys
input = sys.stdin.readline

n1, n2 = map(int, input().split())

# 유클리드 호제법 이용
def gcd(x, y):
  mod = x % y
  while mod > 0:
    x = y
    y = mod
    mod = x % y
  return y
print(gcd(n1, n2))
print(n1*n2 // gcd(n1, n2))