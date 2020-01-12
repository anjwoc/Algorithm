import sys
import math
from itertools import combinations
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
  tmp = list(map(int, input().split()))
  arr.append(tmp)

# 두 개의 그룹으로 나눌 사람의 리스트
people = list(range(n))

print(people)
# 두 개의 그룹으로 나눈다. n명 중 n//2를 선택하는 경우의 수
candidate = list(combinations(people, n//2))
print(candidate)
ans = math.inf

for group in candidate:
  # 해당 그룹에 속하지 않는 나머지 사람들의 리스트
  rest = list(set(people) - set(group))
  group_sum, rest_sum = 0, 0
  # 두명 씩 짝지어 시너지를 확인해야 하므로, 다시 두 명씩 짝지어준다.
  group_combination = list(combinations(list(group), 2))
  rest_combination = list(combinations(rest, 2))

  for y, x in group_combination:
    group_sum += (arr[y][x] + arr[x][y])

  for y, x in rest_combination:
    rest_sum += (arr[y][x] + arr[x][y])

  # 두 그룹의 합계 차이가 최소가 되도록 구한다.
  if ans > abs(group_sum - rest_sum):
    ans = abs(group_sum - rest_sum)

print(ans) 
