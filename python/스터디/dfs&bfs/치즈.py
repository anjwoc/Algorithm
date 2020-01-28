import sys
from collections import deque
input = lambda : sys.stdin.readline().strip()

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
  que = deque()
  que.append((0, 0))
  check = [[False] * m for _ in range(n)]
  check[0][0] = True
  while que:
    x, y = que.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx>=0 and nx<n and ny>=0 and ny<m:
        if not check[nx][ny]:
          if maps[nx][ny] >= 1:
            maps[nx][ny] += 1
          else:
            que.append((nx, ny))
            check[nx][ny] = True
  

def melt():
  global piece
  melted, cnt = False, 0
  for i in range(n):
    for j in range(m):
      if maps[i][j] >= 2:
        maps[i][j] = 0
        melted = True
        cnt += 1
  if cnt:
    piece = cnt
  return melted


n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
ans, piece = 0, 0
while True:
  bfs()
  if melt():
    ans += 1
  else: 
    break
print(ans)
print(piece)