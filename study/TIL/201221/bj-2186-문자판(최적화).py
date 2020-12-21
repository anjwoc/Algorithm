import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dx = (-1, 0, 0, 1)
dy = (0, 1, -1, 0)

def dfs(i, j, idx):
  global k
  if visited[i][j][idx] >= 0:
    return visited[i][j][idx]
  if maps[i][j] != word[idx]:
    return 0
  
  idx += 1
  if idx == length:
    visited[i][j][idx-1] = 1
    return 1
  
  tmp = 0
  for t in range(-k,k+1):
    if t==0:
      continue
    it, jt = i+t, j+t
    if 0<=it<n:
      tmp+=dfs(it,j,idx)
    if 0<=jt<m:
      tmp+=dfs(i,jt,idx)
  visited[i][j][idx-1]=tmp
  return tmp

n, m, k = map(int, input().split())
maps = [list(input().rstrip()) for _ in range(n)]
word = input().rstrip()
length = len(word)
visited = [[[-1 for _ in range(length)] for _ in range(m)] for _ in range(n)]

ans = 0
for i in range(n):
  for j in range(m):
    if maps[i][j] == word[0]:
      ans += dfs(i, j, 0)

print(ans)

