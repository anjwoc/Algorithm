import sys
from collections import deque
input = sys.stdin.readline

dx = (-2, -2, -1, -1, 1, 1, 2, 2)
dy = (-1, 1, -2, 2, -2, 2, -1, 1)

def bfs(tx ,ty):
  global kx, ky
  que = deque([(kx ,ky, 0)])
  visited = set()
  visited.add((kx, ky))

  while que:
    x, y, dist = que.popleft()
    if x==tx and y==ty:
      print(dist)
      return
    for i in range(8):
      nx, ny = x + dx[i], y + dy[i]

      if 0<=nx<n and 0<=ny<n:
        if (nx, ny) not in visited:
          visited.add((nx, ny))
          que.append((nx, ny, dist+1))

  

n, m = map(int, input().split())
kx, ky = map(int, input().split())

for _ in range(m):
  x, y = map(int, input().split())
  bfs(x-1, y-1)
