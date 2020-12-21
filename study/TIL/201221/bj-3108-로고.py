import sys
from collections import deque
input = sys.stdin.readline

'''
FD x: 거북이를 x만큼 앞으로 전진
LT a: 거북이를 반시계 방향으로 a도 만큼 회전
RT a: 거북이를 시계 방향으로 a도 만큼 회전
PU: 연필을 올린다
PD: 연필을 내린다.
'''

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def fillRect(x1, y1, x2, y2):
  for i in range(x1, x2+1):
    if i == x1 or i == x2:
      for j in range(y1, y2+1):
        # 위 아래
        maps[i][j] = 1
    else:
      # 왼쪽, 오른쪽
      maps[i][y1] = 1
      maps[i][y2] = 1
      

def bfs(a, b):
  que = deque([(a, b)])
  visited[a][b] = 1

  while que:
    x, y = que.popleft()
    for i in range(4):
      nx, ny = x + dx[i], y + dy[i]
      if 0<=nx<2001 and 0<=ny<2001:
        if maps[nx][ny] == 1 and not visited[nx][ny]:
          que.append((nx, ny))
          visited[nx][ny] = 1
  

n = int(input())
maps = [['.' for _ in range(2001)] for _ in range(2001)]
visited = [[0 for _ in range(2001)] for _ in range(2001)]
vertex = []
for _ in range(n):
  a, b, c, d = map(int, input().split())
  a, b, c, d = (a+500)*2, (b+500)*2, (c+500)*2, (d+500)*2
  vertex.append((a, b, c, d))
  fillRect(a, b, c, d)

ans = 0
for v in vertex:
  a, b, c, d = v
  if not visited[a][b] and maps[a][b] == 1:
    bfs(a, b)
    ans += 1
  if not visited[c][d] and maps[c][d] == 1:
    bfs(c, d)
    ans += 1

# for i in range(2001):
#   for j in range(2001):
#     if maps[i][j] == 1 and not visited[i][j]:
#       bfs(i, j)
#       ans += 1

if maps[1000][1000] == 1:
  ans -= 1

print(ans)