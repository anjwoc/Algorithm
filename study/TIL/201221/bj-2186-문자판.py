import sys
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y, idx):
  if idx == len(target):
    return 1
  if check[x][y][idx] != -1:
    return check[x][y][idx]
  
  check[x][y][idx] = 0

  for i in range(4):
    cur_x, cur_y = x, y
    
    for _ in range(k):
      nx = cur_x + dx[i]
      ny = cur_y + dy[i]

      if 0<=nx<n and 0<=ny<m:
        if maps[nx][ny] == target[idx]:
          check[x][y][idx] += dfs(nx, ny, idx+1)
      cur_x, cur_y = nx, ny
  return check[x][y][idx]


n, m, k = map(int, input().split())
maps = [list(input().rstrip()) for _ in range(n)]
target = input().rstrip()

vertex = []
for i in range(n):
  for j in range(m):
    if maps[i][j] == target[0]:
      vertex.append((i, j))

ans = 0
check = [[[-1] * len(target) for _ in range(m)] for _ in range(n)]
for i in range(len(vertex)):
  x, y = vertex[i]
  ans += dfs(x, y, 1)

print(ans)