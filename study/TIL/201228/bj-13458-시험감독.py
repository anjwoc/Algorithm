import sys
input = sys.stdin.readline

'''
총감독관은 오직 1명만 있고, 부감독관은 여러 명 있어도 된다.
-> 총감독관은 무조건 1명이 있고 부감독관은 없어도 된다.

문제를 잘못 해석해서 여러 조건을 추가하다가 오답이 발생했는데
B가 A[i]보다 큰 경우엔 1명만 추가하고 그렇지 않은 경우엔
이미 총감독관이 1명 있으므로총감독관과 부감독관이 모두 있는 경우를 계산해야 한다.
'''

n = int(input())
arr = list(map(int, input().split()))
b, c = map(int, input().split())

ans = 0

for num in arr:
  if b >= num:
    ans += 1
    continue
  if (num-b) % c != 0:
    ans += 1 + ((num - b) // c) + 1
  else:
    ans += 1 + ((num - b) // c)

print(ans)