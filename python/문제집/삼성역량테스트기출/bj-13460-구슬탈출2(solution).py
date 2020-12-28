import sys
from collections import deque
input = sys.stdin.readline

dx, dy = (-1, 1, 0, 0), (0, 0, 1, -1)

n, m = map(int, input().split())
check = [[[[False]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]
rIdx, bIdx = 0, 0
que = deque()

maps = [list(input().rstrip()) for _ in range(n)]

def init():
  rx, ry, bx, by = [0]*4
  for i in range(n):
    for j in range(m):
      if maps[i][j] == 'R':
        rx, ry = i, j
      elif maps[i][j] == 'B':
        bx, by = i, j

  que.append((rx, ry, bx, by, 0))
  check[rx][ry][bx][by] = True

def move(x, y, dx, dy, cnt):
  while maps[x+dx][y+dy] != '#' and maps[x][y] != 'O':
    x += dx
    y += dy
    cnt += 1
  return x, y, cnt

def bfs():
  while que:
    rx, ry, bx, by, dist = que.popleft()

    if dist >= 10:
      break

    for i in range(4):
      nrx, nry, rc = move(rx, ry, dx[i], dy[i], 0)
      nbx, nby, bc = move(bx, by, dx[i], dy[i], 0)

      if maps[nbx][nby] == 'O':
        continue
      
      if maps[nrx][nry] == 'O':
        print(dist+1)
        return
      
      if nrx == nbx and nry == nby:
        '''
        예제7의 경우에 #.O....RB# 로 R과 B가 일직선으로 나란히 있다.
        move함수로 이동을 하면 R, B 모두 O에 도착하게 되어서 겹치는 부분을 처리해준다.
        rc, bc는 각각 R과 B가 이동한 칸수로 더 많이 이동한 쪽을 현재 방향에 맞춰 값을 빼준다.
        '''
        if rc > bc:
          nrx, nry = nrx-dx[i], nry-dy[i]
        else:
          nbx, nby = nbx-dx[i], nby-dy[i]
      
      if not check[nrx][nry][nbx][nby]:
        check[nrx][nry][nbx][nby] = True
        que.append((nrx, nry, nbx, nby, dist+1))
  print(-1)

init()
bfs()