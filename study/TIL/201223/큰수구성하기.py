import sys
from itertools import product
input = sys.stdin.readline

def solve(length):
  ans = 0
  for combi in product(arr, repeat=length):
    tmp = int(''.join(combi))
    if n >= tmp:
      ans = max(tmp, ans)

  return ans

n, k = map(int, input().split())
arr = input().split()

nlen = len(str(n))
if nlen >= k:
  print(solve(k))
elif nlen < k:
  print(solve(nlen))