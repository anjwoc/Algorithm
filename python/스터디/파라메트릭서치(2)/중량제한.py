import sys
from collections import deque

input = lambda: sys.stdin.readline().strip()

n, m = map(int, input().split())
maps = [[] for _ in range(n+1)]

check = [False] * 100001
for _ in range(m):
  a, b, c = map(int, input().split())
  maps[a].append((b, c))
  maps[b].append((a, c))

start, end = map(int, input().split())

def bfs(c):
  que = deque()
  que.append(start)
  visited = set()
  visited.add(start)
  ans = []
  while que:
    y = que.popleft()
    for x, w in maps[y]:
      # 갈 수 있는곳이고 무게 제한에 안걸리면
      if x not in visited and w>=c:
        visited.add(x)
        que.append(x)
  # 도착 지점을 방문할 수 있는 경우면 True, 아니면 False 리턴
  return True if end in visited else False

# 이분탐색으로 최대값 탐색
_min, _max = 1, 1000000000
while _min <= _max:
  mid = (_min + _max) // 2
  # 해당 무게로 start => end 까지 도착이 가능한 경우
  # 값을 저장하고, 최대값을 구하기 위해 _min값을 올린다.
  if bfs(mid):
    ans = mid
    _min = mid + 1
  else:
    _max = mid -1

print(ans)  








