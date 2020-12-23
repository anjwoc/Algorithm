import sys
from collections import deque
input = sys.stdin.readline

dx = (-2, -2, -1, -1, 1, 1, 2, 2)
dy = (-1, 1, -2, 2, -2, 2, -1, 1)

n, m = map(int, input().split())
x, y = map(int, input().split())
enemy = [list(map(int, input().split())) for _ in range(m)]


que = deque([(x, y)])
visited = [[-1 for _ in range(n+1)] for _ in range(n+1)]
visited[x][y] = 0

while que:
  x, y = que.popleft()
  
  for i in range(8):
    nx, ny = x + dx[i], y + dy[i]
    # 좌표 범위를 잘못 제한해서 틀림
    if 1<=nx<=n and 1<=ny<=n:
      if visited[nx][ny] == -1:
        visited[nx][ny] = visited[x][y] + 1
        que.append((nx, ny))

  
for a, b in enemy:
  print(visited[a][b], end=' ')


