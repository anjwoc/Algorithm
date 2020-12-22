import sys
input = sys.stdin.readline

dx = (-1, 1, 0, 0)
dy = (0, 0, 1, -1)

def dfs(i, j):
  ans = 0
  que = set()
  que.add((i, j, maps[i][j]))

  while que:
    x, y, char = que.pop()
    ans = max(ans, len(char))

    if ans == 26:
      return 26
    
    for i in range(4):
      nx, ny = x + dx[i], y + dy[i]
      if 0<=nx<n and 0<=ny<m:
        if maps[nx][ny] not in char:
          que.add((nx, ny, char + maps[nx][ny]))
  return ans

n, m = map(int, input().split())
maps= [list(input().rstrip()) for _ in range(n)]

print(dfs(0, 0))
