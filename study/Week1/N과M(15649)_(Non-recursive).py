from itertools import *
import sys

n, m = map(int, sys.stdin.readline().split())
arr = [n for n in range(1,n+1,1)]
per = list(permutations(arr, m))
for val in per:
    print(*val)

'''
per = permutations(["빨","주","노","초"],2)

from itertools import product
per1 = product((["빨","주","노","초"]), repeat=2)
'''