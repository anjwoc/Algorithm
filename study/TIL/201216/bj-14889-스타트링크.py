import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = 10000000000000

people = list(range(n))
combi = list(combinations(people, n//2))
for group in combi:
  rest = list(set(people) - set(group))

  group_sum, rest_sum = 0, 0

  # 두명 씩 짝지어야 하므로 다시 조합을 구한다.
  group_combination = list(combinations(group, 2))
  rest_combination = list(combinations(rest, 2))

  for y, x in group_combination:
    group_sum += (arr[y][x] + arr[x][y])

  for y, x in rest_combination:
    rest_sum += (arr[y][x] + arr[x][y])

  # 두 그룹의 합계의 차이가 최소가 되도록 구한다.
  if ans > abs(group_sum - rest_sum):
    ans = abs(group_sum - rest_sum)

print(ans)