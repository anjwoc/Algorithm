import sys
from itertools import combinations
input = sys.stdin.readline

arr = sorted([int(input()) for _ in range(9)])
combi = list(combinations(arr, 7))

ans = [i for i in combi if sum(i) == 100]
for i in ans[0]:
    print(i)