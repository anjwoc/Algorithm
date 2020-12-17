import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
shuffled = list(permutations(arr, n))

ans = 0
for lst in shuffled:
  tmp = 0
  for i in range(1, len(lst)):
    tmp += abs(lst[i-1] - lst[i])
  ans = max(ans, tmp)

print(ans)