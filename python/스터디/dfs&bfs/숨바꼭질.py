import sys
input = sys.stdin.readline

n, k = map(int, input().split())

# 걷게 되면 1초 후에 -1 또는 +1로 이동
# 순간이동을 하면 2*X위치

dx = [-1, 1, 2]
visited = [False]*100001
times = [-1]*100001
times[n] = 0
que = [n]

while que:
  x = que.pop()
  for cur_x in [x-1, x+1, 2*x]:
    if cur_x <= 100000 and cur_x >= 0 and not times[cur_x]==-1:
      times[cur_x] += times[x]+1
      que.append(cur_x)


