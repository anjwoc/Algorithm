import sys
input = sys.stdin.readline

def check(num):
  num = list(str(num))
  for i in num:
    if i in broken_btns:
      return False
  return True

n = int(input())
m = int(input())
broken_btns = list(input().rstrip())
# 시작 채널은 100번
ans = abs(n-100)

for i in range(1000001):
  if check(i):
    ans = min(ans, len(str(i)) + abs(n-i))

print(ans)