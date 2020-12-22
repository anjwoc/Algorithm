import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dx = (-1, 1, 0, 0)
dy = (0, 0, 1, -1)

def dfs(x, y):
  global check, ans
  for i in range(4):
    nx, ny = x+dx[i], y+dy[i]
    if 0<=nx<n and 0<=ny<m:
      if maps[nx][ny] not in check:
        check.add(maps[nx][ny])
        cnt = max(visited[x][y] + 1, visited[nx][ny])
        visited[nx][ny] = cnt
        ans = max(ans, cnt)
        dfs(nx, ny)
        check.remove(maps[nx][ny])
        
  


n, m = map(int, input().split())
maps= [list(input().rstrip()) for _ in range(n)]
visited = [[0 for _ in range(m+1)] for _ in range(n+1)]
ans = 0
check = set()
check.add(maps[0][0])
visited[0][0]=1
dfs(0, 0)
print(ans)
