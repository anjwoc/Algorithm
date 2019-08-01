from itertools import *
import sys
n, m = map(int, sys.stdin.readline().split())
arr = [n for n in range(1,n+1,1)]
per = list(permutations(arr, m))
result = []
for val in per:
    #요소 하나하나가 tuple형태라 tuple로 캐스팅해서 비교
    is_sorted = (tuple(sorted(val)) == val)
    if(is_sorted):
        result.append(val)

for val in result:
    print(*val)

