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
  '''
  -k ~ k+1까지 범위를 지정하면 k가 1인 경우
  t에는 -1, 0, 1 값이 나온다.
  0인 경우는 제외를 하게되면 it, jt에는 (i-1, j-1), (i+1, j+1)이 나오게 되고
  it, jt가 정상 범위 일때 (it, j) or (i, jt)의 좌표로 넘겨주게 되므로
  dx, dy를 사용하는 것과 동일하지만 반복하는 횟수는 반절로 줄어든다.
  원래라면 4방향의 4와 k만큼 반복을해수 4*k번을 돌아야하지만
  아래와 같이 하면 2*k만큼만 반복하면 된다.
  '''
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

