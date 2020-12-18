import sys
from collections import deque
input = sys.stdin.readline

def find(x, k):
  que = deque([x])  
  times = [0] * 100001

  while que:
    v = que.popleft()
    if v == k:
      print(times[k])
      return
    for i in [v+1, v-1, 2*v]:
      if 0<=i<100001 and not times[i]:
        times[i] += times[v] + 1
        que.append(i)

n, k = map(int, input().split())

find(n, k)