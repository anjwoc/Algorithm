import sys
from collections import deque
input = sys.stdin.readline

dx, dy = (-1, 1, 0, 0), (0, 0, 1, -1)
directions = {
  'up': (-1, 0),
  'down': (1, 0),
  'left': (0, -1),
  'right': (0, 1)
}
n, m = map(int, input().split())
maps = []
rIdx, bIdx = 0, 0
for i in range(n):
  row = list(input().rstrip())
  maps.append(row)
  try: 
    rIdx = (i, row.index('R'))
    bIdx = (i, row.index('B'))
  except:
    pass

def move(x, y, direction, visited):
  


  if maps[x][y] != 'R' and maps[x][y] != 'B':
    return (x, y)

  while True:
    nx, ny = x+i, y+j
    if visited[nx][ny]: 
      break
    if maps[nx][ny] == '#':
      break
    if 1<=nx<n and 1<=ny<m:
      visited[nx][ny] = 1
      maps[nx][ny], maps[x][y] = maps[x][y], maps[nx][ny]
      x, y = nx, ny
  return (x, y)



def bfs():
  que = deque([(i, j, a, b)])
  visited = [[0 for _ in range(m+1)] for _ in range(n+1)]
  visited[i][j] = 1
  visited[a][b] = 1

  while que:
    x, y, a, b = que.popleft()
    
    for direction in ['left', 'right', 'up', 'down']:
      kx, ky = directions[direction]
      nx, ny, na, nb = nx+kx, ny+ky, na+kx, nb+ky
      nx, ny = move(nx, ny, direction, visited)
      na, nb = move(na, nb, direction, visited)
      que.append((nx, ny, na, nb))
      
bfs(*rIdx, *bIdx)
